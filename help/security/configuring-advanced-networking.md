---
title: Configuring Advanced Networking for AEM as a Cloud Service
description: Learn how to configure advanced networking features like VPN or dedicated egress IP address for AEM as a Cloud Service
---

# Configuring Advanced Networking for AEM as a Cloud Service {#configuring-advanced-networking}

AEM as a Cloud Service offers several types of advanced networking capabilities, which can be configured by customers using Cloud Manager APIs. These include:

* Flexible Port egress - configure AEM CS to allow outbound traffic out of non-standard ports
* Dedicated egress IP address - configure traffic out of AEM CS to originate from a unique IP
* Virtual Private Network - secure traffic between a customer's infrastructure and AEM CS, for customer's who have VPN technology

This article describes each of these options in detail, including how they can be configured. As a general configuration strategy, the `/networkInfrastructures` API endpoint is invoked at the program level to declare the desired type of advanced networking, followed by a call to the `/advancedNetworking` endpoint for each environment to enable the infrastructure and configure environment-specific parameters. Please reference the appropriate endpoints in the Cloud Manager API documentation for each formal syntax, as well as sample requests and responses.

When deciding between flexible port egress and dedicated egress IP address, it is recommended you choose flexible port egress if a specific IP address is not required because Adobe can optimize performance of flexible port egress traffic.

>[!INFO]
>
>Advanced networking is not available for the sandbox program.

>[!NOTE]
>
>Customers already provisioned with legacy dedicated egress technology who need to configure one of these options should not do so or site connectivity may be impacted. Please contact Adobe Support for assistance.

## Flexible Port Egress {#flexible-port-egress}

This advanced networking feature allows you to configure AEM as a Cloud Service to egress traffic through ports other than HTTP (port 80) and HTTPS (port 443), which are the defaults.

### Considerations {#flexible-port-egress-considerations}

Flexible port egress is the recommended choice if you don't need VPN and don't need a dedicated egress IP address since traffic that doesn't rely on a dedicated egress can achieve higher throughput.

### Configuring the Provision {#configuring-flexible-port-egress-provision}

Once per program, the POST `/program/<programId>/networkInfrastructures` endpoint is invoked, simply passing the value of `flexiblePortEgress` for the `kind` parameter and region. The endpoint responds with the `network_id`, as well as other information including the status. The full set of parameters and exact syntax should be referenced in the API docs.

Once called, it typically takes approximately 15 minutes for the networking infrastructure to be provisioned. A call to the Cloud Manager's environment GET endpoint would show a status of "ready".

If the program-scoped flexible port egress configuration is ready, the `PUT /program/<program_id>/environment/<environment_id>/advancedNetworking` endpoint must be invoked per environment to enable networking at the environment level and to declare any routing rules. Parameters are configurable per environment in order to offer flexibility.

Routing rules should be declared for any ports other than 80/443 by specifying the set of destination hosts (names or IP, and with ports). For each destination host, customers must map the intended destination port to a port from 50000 through 59999.

The API should respond in just a few seconds, indicating a status of updating and after about 10 minutes, the endpoint's `GET` method should indicate that advanced networking is enabled.

### Updating the Provision {#updating-flexible-port-egress-provision}

The program level configuration can be updated by invoking the `PUT /api/program/<program_id>/network/<network_id>` endpoint.

>[NOTE!]
>
> The "kind" parameter (VPN, dedicatedEgressIP) cannot be modified. Contact customer support for assistance, describing what has already been created and the reason for the change.

The per environment routing rules can be updated by again invoking the `PUT /program/{programId}/environment/{environmentId}/advancedNetworking` endpoint, making sure to include the full set of configuration parameters, rather than a subset.

### Deleting or Disabling the Provision {#deleting-disabling-flexible-port-egress-provision}

In order to **delete** the network infrastructure, submit a customer support ticket, describing what has been created and why it needs to be deleted.

In order to **disable** flexible port egress from a particular environment, invoke `DELETE /program/{programId}/environment/{environmentId}/advancedNetworking`.

## Dedicated Egress IP Address {#dedicated-egress-IP-address}

>[!NOTE]
>
>If you have been provisioned with a dedicated egress IP before 2021.09.30, please reference the [Legacy Dedicated Egress Address Customers](#legacy-dedicated-egress-address-customers).

Upon request, AEM as a Cloud Service will provision a static, dedicated, IP address for HTTP (port 80) and HTTPS (port 443) outbound traffic programmed in Java code. 

### Benefits {#benefits}

This dedicated IP address can enhance security when integrating with SaaS vendors (like a CRM vendor) or other integrations outside of AEM as a Cloud Service that offer an allowlist of IP addresses. By adding the dedicated IP address to the allowlist, it ensures that only traffic from the customer's AEM Cloud Service is permitted to flow into the external service. This is in addition to traffic from any other IPs allowed. 

Without the dedicated IP address feature enabled, traffic coming out of AEM as a Cloud Service flows through a set of IPs shared with other customers.

### Configuring the Provision {#configuring-dedicated-egress-provision}

Configuring dedicated egress IP address is identical to [flexible port egress](#configuring-flexible-port-egress-provision).

The only difference is that traffic will always egress from a dedicated, unique IP. To find that IP, use a DNS resolver to identify the IP address associated with `p{PROGRAM_ID}.external.adobeaemcloud.com`. The IP address is not expected to change, but if it must change in the future advanced notification will be provided.

When deciding between flexible port egress and dedicated egress IP address, customers should choose flexible port egress if a specific IP address is not required since Adobe can optimize performance of flexible port egress traffic.

## Legacy Dedicated Egress Address Customers {#legacy-dedicated-egress-address-customers}

To enable a dedicated IP address, submit a request to Customer Support, who will provide the IP address information. The request should specify each environment and additional requests should be made if new environments need the feature after the initial request. Sandbox program environments are not supported.

### Feature Usage {#feature-usage}

The feature is compatible with Java code or libraries that result in outbound traffic, provided they use standard Java system properties for proxy configurations. In practice, this should include most common libraries. 

Below is a code sample:

```java
public JSONObject getJsonObject(String relativePath, String queryString) throws IOException, JSONException {
  String relativeUri = queryString.isEmpty() ? relativePath : (relativePath + '?' + queryString);
  URL finalUrl = endpointUri.resolve(relativeUri).toURL();
  URLConnection connection = finalUrl.openConnection();
  connection.addRequestProperty("Accept", "application/json");
  connection.addRequestProperty("X-API-KEY", apiKey);

  try (InputStream responseStream = connection.getInputStream(); Reader responseReader = new BufferedReader(new InputStreamReader(responseStream, Charsets.UTF_8))) {
    return new JSONObject(new JSONTokener(responseReader));
  }
}
```

Some libraries require explicit configuration to use standard Java system properties for proxy configurations.

An example using Apache HttpClient, that requires explicit calls to
[`HttpClientBuilder.useSystemProperties()`](https://hc.apache.org/httpcomponents-client-4.5.x/current/httpclient/apidocs/org/apache/http/impl/client/HttpClientBuilder.html) or use
[`HttpClients.createSystem()`](https://hc.apache.org/httpcomponents-client-4.5.x/current/httpclient/apidocs/org/apache/http/impl/client/HttpClients.html#createSystem()):

```java
public JSONObject getJsonObject(String relativePath, String queryString) throws IOException, JSONException {
  String relativeUri = queryString.isEmpty() ? relativePath : (relativePath + '?' + queryString);
  URL finalUrl = endpointUri.resolve(relativeUri).toURL();

  HttpClient httpClient = HttpClientBuilder.create().useSystemProperties().build();
  HttpGet request = new HttpGet(finalUrl.toURI());
  request.setHeader("Accept", "application/json");
  request.setHeader("X-API-KEY", apiKey);
  HttpResponse response = httpClient.execute(request);
  String result = EntityUtils.toString(response.getEntity());
}
```

The same dedicated IP is applied to all of a customer's programs in their Adobe Organization and for all environments in each of their programs. It applies to both author and publish services.

Only HTTP and HTTPS ports are supported. This includes HTTP/1.1, and HTTP/2 when encrypted.

### Debugging Considerations {#debugging-considerations}

In order to validate that traffic is indeed outgoing on the expected dedicated IP address, check logs in the destination service, if available. Otherwise, it may be useful to call out to a debugging service such as [https://ifconfig.me/IP](https://ifconfig.me/IP), which will return the calling IP address.

## Virtual Private Network (VPN) {#vpn}

VPN allows for connecting to an on-premise infrastructure or datacenter from author, publish, or preview. For example, for the means of accessing a database. 

It also allows Connecting to SaaS vendors such as a CRM vendor that supports VPN or connecting from a corporate network to AEM as a Cloud Service author, preview, or publish.

Most VPN devices with IPSec technology are supported. Consult the list of devices at [this page](https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices#devicetable), based on the information in the **RouteBased configuration instructions** column. Configure the device as described in the table.

### General Considerations {#general-vpn-considerations}

* Support is limited to a single VPN connection
* The Splunk forwarding capability is not possible over a VPN connection.

### Development Considerations {#development-vpn-considerations}

<u>**Traffic Types**</u>

**VPN Traffic**

This is secure, private network traffic flowing between a customer's VPN connection and AEM as a Cloud Service. It corresponds to any of:

* http/s traffic, as long as it is **not** declared in the nonProxyHosts list
* any traffic declared in the `portForwards` list

In order to direct traffic between your internal network and Adobe through the VPN, you must create a CNAME DNS entry in your DNS to map any of the following to `p{PROGRAM_ID}.inner.adobeaemcloud.net`, based on the use case, as exemplified below (note the .net suffix):

* `author-p{PROGRAM_ID}-e{ENVIRONMENT_ID}.adobeaemcloud.com`
* `publish-p{PROGRAM_ID}-e{ENVIRONMENT_ID}.adobeaemcloud.com`
* a custom publish domain

In case the IP address is needed, customers can use a DNS resolver tool to identify the IP address, which is not expected to change. That IP address is within the gateway's address space, which is declared by the customer in the /networkinfrastructures API payload.

**Non-VPN Dedicated Egress Traffic**

There may be use cases where traffic should egress from AEM outside of the private network. For example, outbound integration into a SaaS application such as a CRM vendor. It corresponds to any of:

* Non-http/s traffic declared in the `nonProxyHosts` list
* Http/s traffic **not** declared in the `portForwards` list

In case you want to lock down the traffic going into the external application, a DNS entry with a unique dedicated IP is provided. The pattern is `p{PROGRAM_ID}.external.adobeaemcloud.com` (note the .com suffix). If needed, customers can use a DNS resolver tool to identify the IP address, which is not expected to change. If it must change in the future, advanced notification will be provided.

**Regular Traffic**

Traffic that does not need to egress through the dedicated private egress or dedicated public egress will egress to the Internet through non-dedicated IPs. This traffic has access to a wider I/O pipe.

This corresponds to any of:

* Http/s traffic declared in the `nonProxyHosts` list
* Non-http/s that is **not** declared in the `portForwards` list
* Egress traffic with a host name in Adobe's network. For example, connections to another Adobe product
* Egress traffic with a host name in Azure.

<u>**Custom Code**</u>

Http/s protocol traffic sent out via custom code that respects standard Java proxy settings will automatically route through the private network as VPN traffic.

If the custom code sending out http/s protocol traffic doesn't respect Java proxy settings, it should configure its proxy by reading from the following system properties:

* `http.proxyHost` (also exposed as environment variable `AEM_PROXY_HOST`)
* `http.proxyPort`
* `http.nonProxyHosts` 

For non-http/s traffic sent out by custom code, customer must use the `/advancedNetworking` endpoint to map the destination host/post combinations to a port from 50000 through 59999, and then reference that latter port. As an example, if the payload looks like:

```json
{
  "portForwards": [
  {
    "name": "mysql.example.com",
    "portDest": 3306,
    "portOrig": 50336
   }
  ]
}
```

then in Java, then you should set the host to `http.proxyHost` and port to 50336:

```
DriverManager.getConnection("jdbc:mysql://" + System.getProperty("http.proxyHost") + ":53306/test");
```

or

```
DriverManager.getConnection("jdbc:mysql://" + System.getenv("AEM_PROXY_HOST") + ":53306/test");
```

Useful for Apache or Dispatcher configuration, the environment variables `AEM_HTTP_PROXY_HOST` and `AEM_HTTP_PROXY_HOST` are set to the value of the VPN proxy. The following configuration snippets show how to proxy incoming requests from `/somepath` to `example.com` through the VPN, which may be useful if integrating with an application in your infrastructure, such as Solr:

```
ProxyRemote "http://example.com" "http://${AEM_HTTP_PROXY_HOST}:${AEM_HTTP_PROXY_PORT}"
ProxyPass "/somepath" "http://example.com"
ProxyPassReverse "/somepath" "http://example.com"
```

```
SSLProxyEngine on //needed for https backends
 
ProxyRemote "https://example.com" "http://${AEM_HTTP_PROXY_HOST}:${AEM_HTTP_PROXY_PORT}"
ProxyPass "/somepath" "https://example.com"
ProxyPassReverse "/somepath" "https://example.com"
```

<u>**Locking Down AEM to Traffic Ingressing Through VPN Only**</u>

If you want to allow only VPN access to AEM, environment allowlists can be configured in Cloud Manager so only the IP defined by `p{PROGRAM_ID}.external.adobeaemcloud.com` is allowed to talk to the environment. This can be done the same way as any other IP-based allowlist in Cloud Manager.

Only allowlists for the entire environment are supported. Per path IP allowlists are not. 

In the case you need a per host allowlist, you can use standard http directives at the Dispatcher level to deny/allow certain IPs as an alternative. You should ensure that the desired paths are also not cacheable at the CDN level so that the request always gets to origin.

Find an httpd configuration example below:

```
Order deny,allow
Deny from all
Allow from 192.168.0.1
Header always set Cache-Control private
```