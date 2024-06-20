---
title: Configuring CDN Credentials and Authentication
description: Learn how to configure CDN credentials and authentication by declaring rules in a configuration file that is then deployed by using the Cloud Manager Configuration Pipeline.
feature: Dispatcher
exl-id: a5a18c41-17bf-4683-9a10-f0387762889b
role: Admin
---
# Configuring CDN Credentials and Authentication {#cdn-credentials-authentication}

>[!NOTE]
>This feature is not yet generally available. To join the early-adopter program, email `aemcs-cdn-config-adopter@adobe.com`.

The Adobe-provided CDN has several features and services, some of which rely on credentials and authentication in order to ensure an appropriate level of enterprise security. By declaring rules in a configuration file deployed by using the [Cloud Manager Configuration Pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#config-deployment-pipeline), customers can configure, in a self-service way, the following:

* The HTTP header value used by the Adobe CDN to validate requests coming from a Customer-managed CDN.
* The API token used to purge resources in the CDN cache.

Each of these, including the configuration syntax, is described in its own section below. The [Common Setup](#common-setup) section illustrates the setup common to both, as well as deployment. Finally, there is a section on how to [rotate keys](#rotating-secrets), which is considered a good security practice.

## Customer-managed CDN HTTP header value {#CDN-HTTP-value}

As described in the [CDN in AEM as a Cloud Service](/help/implementing/dispatcher/cdn.md#point-to-point-CDN) page, customers may choose to route traffic through their own CDN, which is referred to as the Customer CDN (also sometimes called BYOCDN).

As part of the setup, the Adobe CDN and the Customer CDN must agree on a value of the `X-AEM-Edge-Key` HTTP Header. This value is set on each request, at the Customer CDN, before it is routed to the Adobe CDN, which then validates that the value is as expected, so it can trust other HTTP headers, including those that help route the request to the appropriate AEM origin.  

The `X-AEM-Edge-Key` value is declared with the syntax below. See the [Common Setup](#common-setup) section to learn how to deploy it.

```
kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  experimental_authentication:
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

The syntax for the `X-AEM-Edge-Key` value includes:

* Kind, version, and metadata.
* Data node that contains a child `experimental_authentication` node (the experimental prefix will be removed when the feature is released).
* Under experimental_authentication, with one authenticator node and one rules node, both of which are arrays.
* Authenticators: Lets you declare a type of token or credential, which in this case is an edge key. It includes the following properties:
   * name - a descriptive string.
   * type - must be edge.
   * edgeKey1 - its value must reference a secret token, which should not be stored in git, but rather declared as a [Cloud Manager Environment Variable](/help/implementing/cloud-manager/environment-variables.md) of type secret. For the Service Applied field, select All. It is recommended that the value (for example,`${{CDN_EDGEKEY_052824}}`) reflects the day it was added.
   * edgeKey2 - used for the rotation of secrets, which is described in the [rotating secrets section](#rotating-secrets) below. At least one of `edgeKey1` and `edgeKey2` must be declared.
<!--   * OnFailure - defines the action, either `log` or `block`, when a request doesn't match either `edgeKey1` or `edgeKey2`. For `log`, request processing will continue, while `block` will serve a 403 error. The `log` value is useful when testing a new token on a live site since you can first confirm that the CDN is correctly accepting the new token before changing to `block` mode; it also reduces the chance of lost connectivity between the customer CDN and the Adobe CDN, as a result of an incorrect configuration. -->
* Rules: Lets you declare which of the authenticators should be used, and whether it's for the publish and/or preview tier.  It includes:
   * name - a descriptive string.
   * when - a condition that determines when the rule should be evaluated, according to the syntax in the [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md) article. Typically, it will include a comparison of the current tier (for example., publish) so all live traffic is validated as routing through the customer CDN.
   * action - must specify "authenticate", with the intended authenticator referenced.

>[!NOTE]
>The Edge Key must be configured as a [Cloud Manager Environment Variable](/help/implementing/cloud-manager/environment-variables.md) variable of type `secret`, before the configuration referencing it is deployed.

## Purge API Token {#purge-API-token}

Customers can [purge the CDN cache](/help/implementing/dispatcher/cdn-cache-purge.md) by using a declared Purge API token. The token is declared with the syntax below.  See the [Common Setup](#common-setup) section to learn how to deploy it.

```

kind: "CDN"
version: "1"
metadata:
  envTypes: ["dev"]
data:
  experimental_authentication:
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

The syntax includes:

* kind, version, and metadata.
* data node that contains a child `experimental_authentication` node (the experimental prefix will be removed when the feature is released).
* Under `experimental_authentication`, with a single one authenticators node.
* Authenticators: Lets you declare a type of token or credential, which in this case is an purge key. It includes the following properties::
  * name - a descriptive string.
  * type - must be purge.
  * purgeKey1 - its value must reference a secret token, which should not be stored in git, but rather declared as [Cloud Manager Environment Variables](/help/implementing/cloud-manager/environment-variables.md) of type `secret`.
  * For the Service Applied field, select All. It is recommended that the value (for example, `${{CDN_PURGEKEY_031224}}`) reflects the day it was added.
  * purgeKey2 - used for rotation of secrets, which is described in the [rotating secrets section](#rotating-secrets) section below. At least one of `purgeKey1` and `purgeKey2` must be declared.
* Rules: Lets you declare which of the authenticators should be used, and whether it's for the publish and/or preview tier.  It includes:
  * name - a descriptive string
  * when - a condition that determines when the rule should be evaluated, according to the syntax in the [Traffic Filter Rules](/help/security/traffic-filter-rules-including-waf.md) article. Typically, it will include a comparison of the current tier (for example., publish).
  * action - must specify "authenticate", with the intended authenticator referenced.

>[!NOTE]
>The Edge Key must be configured as a [Cloud Manager Environment Variable](/help/implementing/cloud-manager/environment-variables.md) variable of type `secret`, before the configuration referencing it is deployed.

## Common Setup {#common-setup}

All authenticators are set up as follows:

* First, create the following folder and file structure in the top-level folder of your Git project:

```

config/
     cdn.yaml

```

* Secondly, the `cdn.yaml` configuration file should contain the nodes described in the examples below. The `kind` property should be set to `CDN` and the version should be set to the schema version, which is currently `1`. The metadata node has a "envTypes" property, which indicates on which environment types (dev, stage, prod)this configuration will be evaluated.

* Lastly, Create a targeted deployment config pipeline in Cloud Manager. See [configuring production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) and [configuring non-production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md).

Note that:

 * RDEs do not currently support the configuration pipeline.
 * You can use `yq` to validate locally the YAML formatting of your configuration file (for example, `yq cdn.yaml`).

## Rotating secrets {#rotating-secrets}

It is good security practice to occasionally change credentials. This can be accomplished as exemplified below, using the example of an edge key, although the same strategy is used for purge keys.

* Initially just `edgeKey1` has been defined, in this case referenced as `${{CDN_EDGEKEY_052824}}`, which as a recommended convention, reflects the date it was created.

```

experimental_authentication:
  authenticators:
    - name: edge-auth
      type: edge
      edgeKey1: ${{CDN_EDGEKEY_052824}}

```

* When it's time to rotate the key, create a new Cloud Manager secret, for example `${{CDN_EDGEKEY_041425}}`.
* In the configuration, reference it from `edgeKey2` and deploy.

```
experimental_authentication:
  authenticators:
    - name: edge-auth
      type: edge
      edgeKey1: ${{CDN_EDGEKEY_052824}}
      edgeKey2: ${{CDN_EDGEKEY_041425}}

```

* Once you are sure the old edge key is not used anymore, remove it by removing `edgeKey1` from the configuration.

```
experimental_authentication:
  authenticators:
    - name: edge-auth
      type: edge
      edgeKey2: ${{CDN_EDGEKEY_041425}}

```

* Delete the old secret reference (`${{CDN_EDGEKEY_052824}}`) from Cloud Manager and deploy.
* When ready for the next rotation, follow the same procedure, however this time you will add `edgeKey1` to the configuration, referencing a new Cloud Manager environment secret named, for example, `${{CDN_EDGEKEY_031426}}`.

```
experimental_authentication:
  authenticators:
    - name: edge-auth
      type: edge
      edgeKey2: ${{CDN_EDGEKEY_041425}}
      edgeKey1: ${{CDN_EDGEKEY_031426}}

```
