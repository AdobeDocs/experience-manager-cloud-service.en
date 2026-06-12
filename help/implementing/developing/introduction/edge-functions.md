---
title: AEM Edge Functions
description: Learn how to execute JavaScript at the CDN layer with AEM Edge Functions to enable personalization, security, and dynamic experiences close to the end user.
feature: Developing, Edge Delivery Services
role: Developer
exl-id: 9cebe65c-6aea-4096-9c58-f88295a80639
---
# AEM Edge Functions {#aem-edge-functions}

>[!IMPORTANT]
>
>AEM Edge Functions is a **beta** feature. Features and documentation may change without notice. To join the early access program and provide feedback, email [aemcs-edgecompute-feedback@adobe.com](mailto:aemcs-edgecompute-feedback@adobe.com).

AEM Edge Functions lets you execute JavaScript at the CDN layer, bringing data processing closer to the end user. This reduces latency and enables responsive, dynamic experiences without a round trip to your origin.

Common use cases include:

- Personalizing content based on information like geolocation, device type, or user attributes
- Acting as middleware between the CDN and your origin
- Reformatting or aggregating responses from third-party APIs before they reach the browser
- Composing and serving server-rendered HTML at the edge using content stitched from multiple backends

AEM Edge Functions is compatible with both Edge Delivery Services and the AEM as a Cloud Service Java-stack.

## Key Benefits {#key-benefits}

| Benefit | Description |
|---|---|
| **Performance** | Fast TTFB through edge SSR returning fully rendered HTML. Low-latency API calls via parallel fetches and optimized network hops. |
| **SEO / GEO** | Server HTML is indexed on first crawl. Fully rendered content is ready for AI crawlers. |
| **Security** | Keep API credentials server-side, hidden from client JavaScript. Authenticate with an identity provider and restrict content access. |
| **Personalisation** | Personalize content before the page loads based on geo and device signals. Run audience lookups at the edge for targeted delivery. |

## Prerequisites {#prerequisites}

- An AEM as a Cloud Service environment
- The AEM Administrator Product Profile on the author instance of your Cloud Service environment, **or** the Cloud Manager Deployment Manager role in Admin Console for Edge Delivery Services sites
- [Node.js and npm](https://nodejs.org/)

## Setup {#setup}

### Install the Adobe CLI {#install-adobe-cli}

Install the Adobe Developer CLI (`aio`):

```bash
npm install -g @adobe/aio-cli
```

Install the AEM Edge Functions plugin:

```bash
aio plugins install @adobe/aio-cli-plugin-aem-edge-functions
```

Authenticate and configure the plugin for your environment:

```bash
aio login
aio aem edge-functions setup
```

The setup command prompts you to sign in and then select the AEM environment on which you want to use AEM Edge Functions.

### Clone the Boilerplate {#boilerplate}

Copy the [aem-edge-functions-boilerplate](https://github.com/adobe/aem-edge-functions-boilerplate) to your own repository, then install dependencies:

```bash
npm install
```

## Create Your First Function {#create-your-function}

AEM Edge Function services are declared in a YAML configuration file and deployed through the Cloud Manager configuration pipeline.

### 1. Set Up a Configuration Pipeline {#configuration-pipeline}

Before creating an edge function, ensure that a configuration pipeline exists for your environment in Cloud Manager. If not, [create a configuration pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) first.

>[!NOTE]
>
>If you are using a Rapid Development Environment (RDE), you can deploy configuration directly with `aio aem rde:install -t env-config ./config` instead of going through a configuration pipeline.

### 2. Declare Your Edge Function Services {#declare-services}

Create a file named `edgeFunctions.yaml` in your configuration directory:

```yaml
kind: "EdgeFunctions"
version: "1"
data:
  functions:
    - name: my-edge-function
    # Uncomment to enable secrets
    # secrets:
    #   - key: API_TOKEN
    #     value: ${{ API_TOKEN_SECRET }}
```

The default limit is 1 function for AEM as a Cloud Service environments and 3 for Edge Delivery Services sites. The top-level keys are:

| Key | Description |
|---|---|
| `functions` | List of edge functions, each identified by a `name`. For backward compatibility, `services` is also accepted but `functions` is the preferred key. Using both in the same file is not allowed. |
| `configs` | Key/value pairs exposed to all edge functions as environment variables. |
| `secrets` | Key/value pairs referencing Cloud Manager secrets, exposed to all edge functions. |
| `kvs` | Boolean toggle to provision a KV store for runtime read/write key-value data shared across all edge functions. |

### 3. Add CDN Origin Selector Rules {#cdn-routing}

Edge functions are invoked by routing CDN traffic to them via origin selector rules. Add the following to your `cdn.yaml` configuration file (or create one if it does not exist):

```yaml
kind: 'CDN'
version: '1'
data:
  originSelectors:
    rules:
      - name: route-weather-to-edge-function
        when: { reqProperty: path, equals: "/weather" }
        action:
          type: selectAemOrigin
          originName: edgefunction-my-edge-function
      - name: route-hello-world-to-edge-function
        when: { reqProperty: path, equals: "/hello-world" }
        action:
          type: selectAemOrigin
          originName: edgefunction-my-edge-function
```

The origin selector rules let you route traffic to your edge functions based on any condition available in the CDN rules engine, such as a specific path, domain, or request header. Multiple rules can route different paths to the same edge function. See [Origin Selectors](/help/implementing/dispatcher/cdn-configuring-traffic.md#origin-selectors) for the full rule syntax.

### 4. Deploy the Configuration {#deploy-configuration}

Commit both `edgeFunctions.yaml` and `cdn.yaml` to your Cloud Manager Git repository and trigger the configuration pipeline. Once the pipeline completes successfully, your edge function endpoints are available at:

- `publish-pXXXXX-eYYYYY.adobeaemcloud.com/weather`
- `publish-pXXXXX-eYYYYY.adobeaemcloud.com/hello-world`

where `pXXXXX-eYYYYY` are your environment coordinates. If a custom domain is configured, the functions are also reachable at those domain paths (for example, `example.com/weather`).

## Build and Deploy AEM Edge Function Code {#build-deploy}

### Build {#build}

Package your edge function code for deployment:

```bash
aio aem edge-functions build
```

### Deploy {#deploy}

Deploy the built package to a named edge function service. The `function-name` argument must match the `name` value in `edgeFunctions.yaml`:

```bash
aio aem edge-functions deploy <function-name>
```

## Local Development {#local-development}

### Run Locally {#local-run}

Start a local development server at `http://127.0.0.1:7676`:

```bash
aio aem edge-functions serve
```

See this [Compute JavaScript documentation](https://www.fastly.com/documentation/guides/compute/javascript/) for details on what the local runtime supports.

### Test {#test}

Run the test suite with [Mocha](https://mochajs.org/):

```bash
npm run test
```

### Remote Debugging {#remote-debugging}

Adobe Managed CDN does not expose a remote debugger, but does expose log streaming. Tail the logs for a deployed function to receive `console.log` output directly in your terminal:

```bash
aio aem edge-functions tail-logs <function-name>
```

## Caching and Cache Purging {#caching}

Edge Functions can significantly reduce origin load and improve response times by caching data at the edge. However, caching requires intentional design — particularly in Edge Functions where **two independent cache layers** are involved:

```
Browser → AEM CDN (CDN Cache) → AEM Edge Functions (Fetch Cache) → Backend (AEM, APIs, etc.)
```

Before configuring caching, consider how your content behaves:

- **Truly unique-per-request content** (session tokens, real-time pricing for a specific user) should bypass caching to avoid serving incorrect results.
- **Cohort-based personalization** (content tailored by region, device type, or audience segment) can often be cached with shorter TTLs or `Vary` headers, since many users share the same variant.
- **Stable, shared content** (product catalogs, CMS pages, API responses that change on a known schedule) benefits from aggressive caching with explicit invalidation via surrogate keys.
- **Getting it wrong in either direction has consequences.** Over-caching causes stale content bugs that are difficult to diagnose across two cache layers. Under-caching defeats the performance and origin-offload purpose of using Edge Functions at all.

Because the CDN and the Edge Function's internal fetch cache operate independently, a change to underlying data requires deliberate invalidation of **both** layers. Understanding this architecture is essential for reliable cache management.

For the detailed technical guidance on configuring caching behavior, controlling cache lifetimes, using surrogate keys, and purging cached content, see [Caching in AEM Edge Functions](/help/implementing/developing/introduction/edge-functions-caching.md).

## Limitations {#limitations}

Each Edge Function invocation runs inside a sandbox with resource limits enforced by the underlying compute platform.

### Maximum Outbound Fetch Calls per Invocation {#max-fetch-calls}

AEM Edge Functions enforce a hard limit of **32 backend requests per execution** (that is, per incoming request handled by your function). Once this limit is reached, any further `fetch()` calls fail with the following error:

```
Requested backend named '…' does not exist
```

When you see this error and your origin configuration is correct, the most likely cause is that the per-invocation backend request quota has been exhausted. See [Fastly Compute resource limits](https://docs.fastly.com/products/compute-resource-limits#default-limits) for the full list of platform limits.

## Configuration Reference {#configuration-reference}

### Origins {#origins}

By default, edge functions can fetch from any origin. To restrict a function to a defined set of origins, declare them under `origins` in `edgeFunctions.yaml`:

```yaml
origins:
  - name: my-origin-name
    domain: example.com
```

Reference the named origin in your function code using the `backend` fetch option:

```js
const request = new Request("https://example.com/test");
const response = await fetch(request, { backend: "my-origin-name" });
```

>[!NOTE]
>
>Service stores (`configs`, `secrets`, and `kvs`) are not available in [sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md). Edge function services themselves run normally on sandbox environments — only the stores are not provisioned.

### Service Configuration {#service-configuration}

Expose environment variables to your functions using the `configs` key in `edgeFunctions.yaml`. Values are stored in a config store named `config_default`:

```yaml
configs:
  - key: LOG_LEVEL
    value: DEBUG
```

Read configuration values in your function code:

```js
import { ConfigStore } from "fastly:config-store";

const config = new ConfigStore('config_default');
const logLevel = config.get('LOG_LEVEL') || 'info';
```

>[!NOTE]
>
>- The config store is always named `config_default`.
>- Key names are case-sensitive.
>- The config store is shared across all edge function services in the same environment.

### Service Secrets {#service-secrets}

Secrets are referenced, not stored, in `edgeFunctions.yaml`. The `value` field must point to a Cloud Manager secret using the `${{SECRET_REFERENCE}}` syntax. Define the underlying secret in Cloud Manager first — see [Cloud Manager Secret Variables](/help/implementing/cloud-manager/environment-variables.md).

```yaml
secrets:
  - key: API_TOKEN
    value: ${{ API_TOKEN_SECRET }}
```

Retrieve secrets in your function code using the `SecretStoreManager` helper from the boilerplate:

```js
import { SecretStoreManager } from "./lib/config";

const apiToken = await SecretStoreManager.getSecret('API_TOKEN');
```

>[!NOTE]
>
>- The secret store is always named `secret_default`.
>- Key names are case-sensitive.
>- Secrets are immutable once created.
>- The secret store is shared across all edge function services in the same environment.

### Service KV Store {#service-kv-store}

Edge functions can read and write arbitrary key-value data at runtime through a KV store. To enable it, set `kvs: true` in `edgeFunctions.yaml`:

```yaml
kvs: true
```

This provisions an empty KV store named `kv_default`. Populate it at runtime from your edge function code using the [Fastly KV Store API](https://js-compute-reference-docs.edgecompute.app/docs/fastly:kv-store/KVStore):

```js
import { KVStore } from "fastly:kv-store";

const kv = new KVStore('kv_default');

// Read a value
const entry = await kv.get('visit-count');
const count = entry ? Number(await entry.text()) : 0;

// Write a value
await kv.put('visit-count', String(count + 1));
```

>[!NOTE]
>
>- The KV store is always named `kv_default`.
>- The KV store is empty at provision time; populate it at runtime via the [Fastly KV Store API](https://js-compute-reference-docs.edgecompute.app/docs/fastly:kv-store/KVStore). Declarative key/value entries in `edgeFunctions.yaml` are not supported.
>- The KV store is shared across all edge function services in the same environment.

### Logging {#logging}

AEM Edge Functions integrates with the [AEM Log Forwarding](/help/implementing/developing/introduction/log-forwarding.md) feature. Create a `logForwarding.yaml` file alongside your `edgeFunctions.yaml`:

```yaml
kind: "LogForwarding"
version: "1"
metadata:
  envTypes: ["rde", "dev", "stage", "prod"]
data:
  splunk:
    default:
      enabled: true
      host: "splunk-host.example.com"
      token: "${{SPLUNK_TOKEN}}"
      index: "AEMaaCS"
```

Use the logger in your function code to write structured log entries:

```js
import { Logger } from "fastly:logger";

const logger = new Logger("customerSplunk");
logger.log(JSON.stringify({
  method: event.request.method,
  url: event.request.url
}));
```

>[!NOTE]
>
>CDN logs — which include AEM Edge Function log entries — can be downloaded from Cloud Manager for Java-stack environments, but not for Edge Delivery Services sites.
>
