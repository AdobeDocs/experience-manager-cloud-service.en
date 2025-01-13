---
title: Configuring CDN Credentials and Authentication
description: Learn how to configure CDN credentials and authentication by declaring rules in a configuration file that is then deployed by using the Cloud Manager config pipeline.
feature: Dispatcher
exl-id: a5a18c41-17bf-4683-9a10-f0387762889b
role: Admin
---

# Configuring CDN Credentials and Authentication {#cdn-credentials-authentication}

The Adobe-provided CDN has several features and services, some of which rely on credentials and authentication in order to ensure an appropriate level of enterprise security. By declaring rules in a configuration file deployed by using the Cloud Manager [config pipeline,](/help/operations/config-pipeline.md) customers can configure, in a self-service way, the following:

* The X-AEM-Edge-Key HTTP header value used by the Adobe CDN to validate requests coming from a Customer-managed CDN.
* The API token used to purge resources in the CDN cache.
* A list of username/password combinations that can access restricted content, by submitting a Basic Authentication form.

Each of these, including the configuration syntax, is described in its own section below. 

There is a section on how to [rotate keys](#rotating-secrets), which is a good security practice.

## Customer-managed CDN HTTP header value {#CDN-HTTP-value}

As described in the [CDN in AEM as a Cloud Service](/help/implementing/dispatcher/cdn.md#point-to-point-CDN) page, customers may choose to route traffic through their own CDN, which is referred to as the Customer CDN (also sometimes called BYOCDN).

As part of the setup, the Adobe CDN and the Customer CDN must agree on a value of the `X-AEM-Edge-Key` HTTP Header. This value is set on each request at the Customer CDN, before it is routed to the Adobe CDN, which then validates that the value is as expected, so it can trust other HTTP headers, including those that help route the request to the appropriate AEM origin.  

The *X-AEM-Edge-Key* value is referenced by the `edgeKey1` and `edgeKey2` properties in a file named `cdn.yaml` or similar, somewhere under a top-level `config` folder. Read [Using Config Pipelines](/help/operations/config-pipeline.md#folder-structure) for details about the folder structure and how to deploy the configuration.  The syntax is described in the example below.

For further debugging information and common errors, please check [Common Errors](/help/implementing/dispatcher/cdn.md#common-errors).

>[!WARNING]
>Direct access without a correct X-AEM-Edge-Key will be denied for all requests matching the condition (in the sample below that means all requests to the publish tier). If you need to gradually introduce authentication, please see the [Migrating safely to reduce the risk of blocked traffic](#migrating-safely) section.

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  authentication:
    authenticators:
      - name: edge-auth
        type: edge
        edgeKey1: ${{CDN_EDGEKEY_052824}}
        edgeKey2: ${{CDN_EDGEKEY_041425}}
    rules:
      - name: edge-auth-rule
        when: { reqProperty: tier, equals: "publish" }
        action:
          type: authenticate
          authenticator: edge-auth

```

See [Using Config Pipelines](/help/operations/config-pipeline.md#common-syntax) for a description of the properties above the `data` node. The `kind` property value should be *CDN* and the `version` property should be set to `1`.

See [Configure and deploy HTTP Header validation CDN rule](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/content-delivery/custom-domain-names-with-customer-managed-cdn#configure-and-deploy-http-header-validation-cdn-rule) tutorial step for more details.

Additional properties include:

* `Data` node that contains a child `authentication` node.
* Under `authentication`, one `authenticators` node and one `rules` node, both of which are arrays.
* Authenticators: Lets you declare a type of token or credential, which in this case is an edge key. It includes the following properties:
   * name - a descriptive string.
   * type - must be `edge`.
   * edgeKey1 - the value of the *X-AEM-Edge-Key*, which must reference a [Cloud Manager secret-type environment variable](/help/operations/config-pipeline.md#secret-env-vars). For the Service Applied field, select All. It is recommended that the value (for example,`${{CDN_EDGEKEY_052824}}`) reflects the day it was added.
   * edgeKey2 - used for the rotation of secrets, which is described in the [rotating secrets section](#rotating-secrets) below. Define it similarly to edgeKey1. At least one of `edgeKey1` and `edgeKey2` must be declared.
<!--   * OnFailure - defines the action, either `log` or `block`, when a request doesn't match either `edgeKey1` or `edgeKey2`. For `log`, request processing will continue, while `block` will serve a 403 error. The `log` value is useful when testing a new token on a live site since you can first confirm that the CDN is correctly accepting the new token before changing to `block` mode; it also reduces the chance of lost connectivity between the customer CDN and the Adobe CDN, as a result of an incorrect configuration. -->
* Rules: Lets you declare which of the authenticators should be used, and whether it's for the publish and/or preview tier.  It includes:
   * name - a descriptive string.
   * when - a condition that determines when the rule should be evaluated, according to the syntax in the [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md) article. Typically, it will include a comparison of the current tier (for example., publish) so all live traffic is validated as routing through the customer CDN.
   * action - must specify "authenticate", with the intended authenticator referenced.

>[!NOTE]
>The Edge Key must be configured as a [secret type Cloud Manager environment variable](/help/operations/config-pipeline.md#secret-env-vars), before the configuration referencing it is deployed. It is recommended to use a unique random key of minimum 32 bytes length; for example, the Open SSL cryptographic library can generate a random key by executing the command `openssl rand -hex 32`.

### Migrating safely to reduce the risk of blocked traffic {#migrating-safely}

If your site is already live, exercise caution when migrating to customer-managed CDN since a misconfiguration can block public traffic; this is because only requests with the expected X-AEM-Edge-Key header value will be accepted by the Adobe CDN. An approach is recommended where an additional condition is temporarily included in the authentication rule, which causes it to block the request only if a test header is included or if a path is matched:

```
    - name: edge-auth-rule
        when:
          allOf:  
            - { reqProperty: tier, equals: "publish" }
            - { reqHeader: x-edge-test, equals: "test" }
        action:
          type: authenticate
          authenticator: edge-auth
```

```
    - name: edge-auth-rule
        when:
          allOf:
            - { reqProperty: tier, equals: "publish" }
            - { reqProperty: path, like: "/test*" }
        action:
          type: authenticate
          authenticator: edge-auth
```

The following `curl` request pattern can be used:

```
curl https://publish-p<PROGRAM_ID>-e<ENV-ID>.adobeaemcloud.com -H "X-Forwarded-Host: example.com" -H "X-AEM-Edge-Key: <CONFIGURED_EDGE_KEY>" -H "x-edge-test: test"
```

After successfully testing, the additional condition can be removed and the configuration redeployed.

## Purge API Token {#purge-API-token}

Customers can [purge the CDN cache](/help/implementing/dispatcher/cdn-cache-purge.md) by using a declared Purge API token. The token is declared in a file named `cdn.yaml` or similar, somewhere under a top-level `config` folder. Read [Using Config Pipelines](/help/operations/config-pipeline.md#folder-structure) for details about the folder structure and how to deploy the configuration. 

The syntax is described below:

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  authentication:
    authenticators:
       - name: purge-auth
         type: purge
         purgeKey1: ${{CDN_PURGEKEY_031224}}
         purgeKey2: ${{CDN_PURGEKEY_021225}}
    rules:
       - name: purge-auth-rule
         when: { reqProperty: tier, equals: "publish" }
         action:
           type: authenticate
           authenticator: purge-auth

```

See [Using Config Pipelines](/help/operations/config-pipeline.md#common-syntax) for a description of the properties above the `data` node. The `kind` property value should be *CDN* and the `version` property should be set to `1`.

Additional properties include:

* `data` node that contains a child `authentication` node.
* Under `authentication`, one `authenticators` node and one `rules` node, both of which are arrays.
* Authenticators: Lets you declare a type of token or credential, which in this case is a purge key. It includes the following properties:
  * name - a descriptive string.
  * type - must be purge.
  * purgeKey1 - its value must reference a [Cloud Manager secret-type Environment Variable](/help/operations/config-pipeline.md#secret-env-vars). For the Service Applied field, select All. It is recommended that the value (for example, `${{CDN_PURGEKEY_031224}}`) reflects the day it was added.
  * purgeKey2 - used for rotation of secrets, which is described in the [rotating secrets](#rotating-secrets) section below. At least one of `purgeKey1` and `purgeKey2` must be declared.
* Rules: Lets you declare which of the authenticators should be used, and whether it's for the publish and/or preview tier.  It includes:
  * name - a descriptive string
  * when - a condition that determines when the rule should be evaluated, according to the syntax in the [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md) article. Typically, it will include a comparison of the current tier (for example., publish).
  * action - must specify "authenticate", with the intended authenticator referenced.

>[!NOTE]
>The Purge Key must be configured as a [secret type Cloud Manager Environment Variable](/help/operations/config-pipeline.md#secret-env-vars), before the configuration referencing it is deployed. It is recommended to use a unique random key of minimum 32 bytes length; for example, the Open SSL cryptographic library can generate a random key by executing the command openssl rand -hex 32

You may reference [a tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/caching/how-to/purge-cache) focused on configuring purge keys and performing the CDN cache purge.

## Basic Authentication {#basic-auth}

Protect certain content resources by popping up a basic auth dialog requiring a username and password. This feature is primarily intended for light authentication use cases such as business stakeholder review of content, rather than as a full-fledged solution for end-user access rights.

The end user will experience a basic auth dialog popping up like the following:

 ![basicauth-dialog](/help/implementing/dispatcher/assets/basic-auth-dialog.png)


The syntax is as follows:

```

kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  authentication:
    authenticators:
       - name: my-basic-authenticator
         type: basic
         credentials:
           - user: johndoe
             password: ${{JOHN_DOE_PASSWORD}}
           - user: janedoe
             password: ${{JANE_DOE_PASSWORD}}
    rules:
       - name: basic-auth-rule
         when: { reqProperty: path, like: "/summercampaign" }
         action:
           type: authenticate
           authenticator: my-basic-authenticator

```

See [Using Config Pipelines](/help/operations/config-pipeline.md#common-syntax) for a description of the properties above the `data` node. The `kind` property value should be *CDN* and the `version` property should be set to `1`.

In addition, the syntax includes:

* a `data` node that contains an `authentication` node.
* Under `authentication`, one `authenticators` node and one `rules` node, both of which are arrays.
* Authenticators: in this scenario declare a basic authenticator, which has the following structure:
  * name - a descriptive string
  * type - must be `basic`
  * an array of up to 10 credentials, each of which includes the following name/value pairs, which end-users can enter in the basic auth dialog:
    * user - the name of the user.
    * password - its value must reference a [Cloud Manager secret-type environment variable](/help/operations/config-pipeline.md#secret-env-vars), with **All** selected as the service field.
* Rules: Lets you declare which of the authenticators should be used, and which resources should be protected. Each rule includes:
  * name - a descriptive string
  * when - a condition that determines when the rule should be evaluated, according to the syntax in the [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md) article. Typically, it will include a comparison of the publish tier or specific paths. 
  * action - must specify "authenticate", with the intended authenticator referenced, which is basic-auth for this scenario

>[!NOTE]
>The passwords must be configured as [secret type Cloud Manager environment variables](/help/operations/config-pipeline.md#secret-env-vars), before the configuration referencing it is deployed.

## Rotating secrets {#rotating-secrets}

1. It is good security practice to occasionally change credentials. This can be accomplished as exemplified below, using the example of an edge key, although the same strategy is used for purge keys.

1. Initially just `edgeKey1` has been defined, in this case referenced as `${{CDN_EDGEKEY_052824}}`, which as a recommended convention, reflects the date it was created.

    ```
    authentication:
      authenticators:
        - name: edge-auth
          type: edge
          edgeKey1: ${{CDN_EDGEKEY_052824}}
    ```
1. When it's time to rotate the key, create a new Cloud Manager secret, for example `${{CDN_EDGEKEY_041425}}`.
1. In the configuration, reference it from `edgeKey2` and deploy.
    ```
    authentication:
      authenticators:
        - name: edge-auth
          type: edge
          edgeKey1: ${{CDN_EDGEKEY_052824}}
          edgeKey2: ${{CDN_EDGEKEY_041425}}
    ```

1. Once you are sure the old edge key is not used anymore, remove it by removing `edgeKey1` from the configuration.    
    ```
    authentication:
      authenticators:
        - name: edge-auth
          type: edge
          edgeKey2: ${{CDN_EDGEKEY_041425}}
    ```       
1. Delete the old secret reference (`${{CDN_EDGEKEY_052824}}`) from Cloud Manager and deploy.

1. When ready for the next rotation, follow the same procedure, however this time you will add `edgeKey1` to the configuration, referencing a new Cloud Manager environment secret named, for example, `${{CDN_EDGEKEY_031426}}`.

    ```
    authentication:
      authenticators:
        - name: edge-auth
          type: edge
          edgeKey2: ${{CDN_EDGEKEY_041425}}
          edgeKey1: ${{CDN_EDGEKEY_031426}}

    ```
