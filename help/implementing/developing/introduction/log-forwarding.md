---
title: Log Forwarding for AEM as a Cloud Service
description: Learn about forwarding logs to logging vendors in AEM as a Cloud Service
exl-id: 27cdf2e7-192d-4cb2-be7f-8991a72f606d
feature: Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Log Forwarding {#log-forwarding}

>[!NOTE]
>
>A beta for mutual TLS (mTLS) authentication is available for Splunk, Elasticsearch/OpenSearch, and HTTPS destinations, for AEM logs (including Apache/Dispatcher) and CDN logs. To join, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID and environment IDs. See [Mutual TLS (mTLS) authentication](#mtls).

>[!NOTE]
>
>Log Forwarding is now configured in self-serve way, different from the legacy method, which required submitting an Adobe Support ticket. See the [Migrating](#legacy-migration) section if your log forwarding was setup by Adobe.

>[!NOTE]
>
>AEM as a Cloud Service also supports sending logs over OpenTelemetry (OTLP), as part of [OpenTelemetry (Limited Availability)](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/opentelemetry-apm-integration.html). If you enable both at the same destination, you receive duplicate log messages there — see that page for details.

Customers with a license with a logging vendor or who host a logging product can have AEM logs (including Apache/Dispatcher) and CDN logs forwarded to the associated logging destination. AEM as a Cloud Service supports the following logging destinations:

<table>
  <tbody>
    <tr>
      <th>Log Technology</th>
      <th>AEM</th>
      <th>Dispatcher</th>
      <th>CDN</th>
      <th>mTLS</th>
    </tr>
    <tr>
      <td>Amazon S3</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Beta [1]</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Azure Blob Storage</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>No</td>
    </tr>
    <tr>
      <td>DataDog</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Dynatrace</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Beta [1]</td>
      <td>No</td>
    </tr>
    <tr>
      <td>ElasticSearch<br>OpenSearch</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Beta</td>
    </tr>
    <tr>
      <td>HTTPS</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Beta</td>
    </tr>
    <tr>
      <td>New Relic</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Beta [1]</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Splunk</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Beta</td>
    </tr>
    <tr>
      <td>Sumo Logic</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>Yes</td>
      <td>No</td>
    </tr>
  </tbody>
</table>

[1] CDN log forwarding to Amazon S3, Dynatrace, and New Relic is in beta. To request access, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID. After access is enabled, you also turn on CDN logs for each destination with `cdn.enabled: true`. See [CDN logs for Amazon S3, Dynatrace, and New Relic (beta)](#cdn-opt-in).

>[!NOTE]
>
> Log Technologies marked **Beta** in the mTLS column support client certificate authentication (mutual TLS) for AEM, Dispatcher, and CDN logs. mTLS is in beta; to request access, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID and environment IDs. See [Mutual TLS (mTLS) authentication](#mtls).

Log forwarding is configured in a self-service manner by declaring a configuration in Git, and can be deployed via Cloud Manager config pipelines to dev, stage, and production environment types. The configuration file can be deployed to Rapid Development Environments (RDEs) using command line tooling.

There is an option for the AEM and Apache/Dispatcher logs to be routed through AEM's advanced networking infrastructure, such as dedicated egress IP. CDN logs are always sent directly from the CDN and do not use advanced networking. See [Transport & Advanced Networking](#transport-advancednetworking).

## How This Article is Organized {#how-organized}

This article is organized in the following way:

* Setup - common for all logging destinations
* Transport & Advanced Networking - consideration should be given to network setup before creating logging configuration
* Mutual TLS (mTLS) authentication (beta) - authenticating to Splunk, Elasticsearch/OpenSearch, and HTTPS destinations with a client certificate
* Logging destination configurations - each destination has a slightly different format
* CDN logs for Amazon S3, Dynatrace, and New Relic (beta) - how to request access to CDN logs for these destinations and enable them
* Log Entry Formats - information about the log entry formats
* Migrating from legacy log forwarding - how to move from log forwarding previously setup by Adobe to the self-serve approach

## Setup {#setup}

1. Create a file named `logForwarding.yaml`. It should contain metadata, as described in the [Configuration Pipeline](/help/operations/config-pipeline.md#common-syntax) article (**kind** should be set to `LogForwarding` and version set to "1"), with a configuration similar to the following (we use Splunk as an example).

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     splunk:
       default:
         enabled: true
         host: "splunk-host.example.com"
         token: "${{SPLUNK_TOKEN}}"
         index: "AEMaaCS"

   ```

1. Place the file somewhere under a top level folder named *config* or similar, as described in [Using Config Pipelines](/help/operations/config-pipeline.md#folder-structure).

1. For environment types other than RDE (which uses command line tooling), create a targeted deployment config pipeline in Cloud Manager, as referenced by [this section](/help/operations/config-pipeline.md#creating-and-managing); note that Full Stack pipelines and Web Tier pipelines do not deploy the configuration file.

1. Deploy the configuration.

Tokens in the configuration (such as `${{SPLUNK_TOKEN}}`) represent secrets, which should not be stored in Git. Instead, declare them as Cloud Manager [Secret Environment Variables](/help/operations/config-pipeline.md#secret-env-vars). Make sure to select **All** as the dropdown value for the Service Applied field, so logs can be forwarded to author, publish, and preview tiers.

It is possible to set different values between CDN logs and AEM logs (including Apache/Dispatcher), by including an additional **cdn** and/or **aem** block after the **default** block, where properties can override those defined in the **default** block; only the enabled property is required. A possible use case could be to use a different Splunk index for CDN logs, as the example below illustrates.

   ```yaml
      kind: "LogForwarding"
      version: "1"
      data:
        splunk:
          default:
            enabled: true
            host: "splunk-host.example.com"
            token: "${{SPLUNK_TOKEN}}"
            index: "AEMaaCS"
          cdn:
            enabled: true
            token: "${{SPLUNK_TOKEN_CDN}}"
            index: "AEMaaCS_CDN"
   ```

>[!NOTE]
>
>For Amazon S3, Dynatrace, and New Relic, CDN logs are in beta. They are forwarded only when your program has access to the beta and the `cdn` block sets `enabled: true`. See [CDN logs for Amazon S3, Dynatrace, and New Relic (beta)](#cdn-opt-in).

   Another scenario is to disable either forwarding of the CDN logs or AEM logs (including Apache/Dispatcher). For example, to only forward the CDN logs, one can configure the following:

   ```yaml
      kind: "LogForwarding"
      version: "1"
      data:
        splunk:
          default:
            enabled: true
            host: "splunk-host.example.com"
            token: "${{SPLUNK_TOKEN}}"
            index: "AEMaaCS"
          aem:
            enabled: false
   ```

## Transport & Advanced Networking {#transport-advancednetworking}

Some organizations choose to restrict which traffic can be received by the logging destinations, others may require to use ports other than HTTPS (443).  If so [Advanced Networking](/help/security/configuring-advanced-networking.md) will need to be configured before deploying log forwarding configuration.

Use the table below to see what the requirements are for Advanced Networking and Logging configuration based on whether you are using port 443 or not, and whether or not you need your logs to appear from a fixed IP address. The table applies to AEM logs (including Apache/Dispatcher). For CDN logs, see [CDN logs and IP allow lists](#cdn-ip-allowlist).

<table>
  <tbody>
    <tr>
      <th>Destination Port</th>
      <th>Requirement for Logs to appear from Fixed IP?</th>
      <th>Advanced Networking Needed</th>
      <th>LogForwarding.yaml Port Definition Needed</th>
    </tr>
    <tr>
      <td rowspan="2"ro>HTTPS (443)</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>Yes, <a href="/help/security/configuring-advanced-networking.md#dedicated-egress-ip-address-dedicated-egress-ip-address">Dedicated Egress</a></td>
      <td>No</td>
    <tr>
    <tr>
      <td rowspan="2">Non standard port (e.g 8088)</td>
      <td>No</td>
      <td>Yes, <a href="/help/security/configuring-advanced-networking.md#flexible-port-egress-flexible-port-egress">Flexible Egress</a></td>
      <td>Yes</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>Yes, <a href="/help/security/configuring-advanced-networking.md#dedicated-egress-ip-address-dedicated-egress-ip-address">Dedicated Egress</a></td>
      <td>Yes</td>
  </tbody>
</table>

>[!NOTE]
>Whether your logs appear from a single IP address is determined by your choice of Advanced Networking configuration.  Dedicated Egress must be used to facilitate this.
>
> Advanced Networking configuration is a [two-step process](/help/security/configuring-advanced-networking.md#configuring-and-enabling-advanced-networking-configuring-enabling) requiring enablement at program and environment level.
>
> Per note below it is not possible to use Log Forwarding with Advanced Networking VPN connections.

For AEM logs (including Apache/Dispatcher), if you have configured [Advanced Networking](/help/security/configuring-advanced-networking.md), you can use the `aem.advancedNetworking` property to forward them from a Dedicated Egress IP address.

The example below shows how to configure logging on a standard HTTPS port with Advanced Networking.

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     splunk:
       default:
         enabled: true
         host: "splunk-host.example.com"
         port: 443
         token: "${{SPLUNK_TOKEN}}"
         index: "aemaacs"
       aem:
         advancedNetworking: true
   ```

### CDN logs and IP allow lists {#cdn-ip-allowlist}

CDN logs are sent directly from the CDN (Fastly), not from AEM as a Cloud Service. This applies to every logging destination:

* CDN logs are sent from Fastly's shared IP address ranges, published at [https://api.fastly.com/public-ip-list](https://api.fastly.com/public-ip-list). They are never sent from your Dedicated Egress IP address.
* The `advancedNetworking` property applies only to AEM logs (including Apache/Dispatcher). It has no effect on CDN logs. If `advancedNetworking` is set and CDN log forwarding is enabled for the same destination, the configuration is deployed with a warning as a reminder.
* If your logging destination only accepts traffic from specific IP addresses, add **all** of Fastly's published IPv4 and IPv6 ranges to its allow list, in addition to your Dedicated Egress IP address for AEM logs. A destination that only allows your Dedicated Egress IP address receives no CDN logs.
* Fastly's IP address ranges change over time, sometimes within weeks. Review the published list regularly and keep your allow lists up to date.
* Amazon S3 has additional considerations for CDN logs. See [Amazon S3 CDN logs](#amazons3-cdn).

If the list of shared IP addresses is too large to allow-list, consider sending CDN logs to an https server or (non-Adobe) Azure Blob Store where logic can be written to send the logs out of a known IP to their ultimate destination.

>[!NOTE]
>
>It is not possible for CDN logs to appear from the same IP address that your AEM logs appear from, this is because logs are sent directly from Fastly and not AEM Cloud Service.
>
>For this reason it is not possible to use Log Forwarding with Advanced Networking VPN configurations.

## Mutual TLS (mTLS) authentication (beta) {#mtls}

>[!NOTE]
>
>mTLS for Log Forwarding is a beta feature. To use it, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID and environment IDs.

Splunk, Elasticsearch/OpenSearch, and HTTPS destinations support mutual TLS (mTLS). With mTLS, AEM as a Cloud Service presents a client certificate when it connects to your logging destination, so the destination can verify that the logs come from your environment. mTLS applies to AEM logs (including Apache/Dispatcher) and to CDN logs.

mTLS works alongside the destination's existing authentication. Keep the destination's existing authentication properties, such as `token` (Splunk) or `user` and `password` (Elasticsearch/OpenSearch). For HTTPS destinations that forward CDN logs, `authHeaderName` and `authHeaderValue` are required.

### Configuration {#mtls-configuration}

Add an `mtls` block alongside the destination's other properties:

* `cert` - required. The client certificate, in PEM format. It can be followed by intermediate CA certificates, with the client certificate first.
* `key` - required. The private key for the client certificate, in PEM format. RSA and EC keys are supported, unencrypted or encrypted. See [Supported key formats](#mtls-key-formats).
* `ca` - optional. The CA certificate, in PEM format, used to verify your destination's server certificate. It can contain more than one certificate, such as a certificate chain. Set it when the server certificate is issued by a private CA.
* `keyPasswd` - optional. The password for the private key. Set it only if the key is encrypted.

The following example forwards AEM and CDN logs to Splunk using mTLS:

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     splunk:
       default:
         enabled: true
         host: "splunk-host.example.com"
         token: "${{SPLUNK_TOKEN}}"
         index: "aemaacs"
         mtls:
           cert: "${{SPLUNK_MTLS_CERT}}"
           key: "${{SPLUNK_MTLS_KEY}}"
           ca: "${{SPLUNK_MTLS_CA}}"
   ```

The following rules apply:

* `cert` and `key` must be provided together. An `mtls` block that contains only `ca` or `keyPasswd` is rejected.
* Each `mtls` property must be a secret reference, such as `${{SPLUNK_MTLS_CERT}}`, and nothing else. Certificate or key text placed directly in the file is rejected.
* Declare each secret as a Cloud Manager [Secret Environment Variable](/help/operations/config-pipeline.md#secret-env-vars), as described in [Setup](#setup). Paste the complete PEM text, including the `-----BEGIN` and `-----END` lines. If the line breaks are removed when you paste the value into Cloud Manager, they are restored automatically. To provide more than one certificate, paste them one after another in the same secret.
* The client certificate is checked when you deploy. It must be valid PEM and within its validity period. If `cert` contains more than one certificate, the client certificate must come first and the certificates must form a valid chain. If a check fails, the deployment fails.

#### Supported key formats {#mtls-key-formats}

The first line of the key's PEM text shows its format:

| Key format | First line of the PEM text |
|---|---|
| RSA, PKCS#1 | `-----BEGIN RSA PRIVATE KEY-----` |
| EC, SEC1 | `-----BEGIN EC PRIVATE KEY-----` |
| PKCS#8 (RSA or EC) | `-----BEGIN PRIVATE KEY-----` |
| Encrypted PKCS#8 (RSA or EC) | `-----BEGIN ENCRYPTED PRIVATE KEY-----` |
| Encrypted, older format (RSA or EC), with AES or Triple DES (`DES-EDE3-CBC`) | `-----BEGIN RSA PRIVATE KEY-----` or `-----BEGIN EC PRIVATE KEY-----`, followed by `Proc-Type: 4,ENCRYPTED` and `DEK-Info` lines |

For an encrypted key, also set `keyPasswd` to its password.

Encrypted PKCS#8 is recommended for encrypted keys. To convert a key in the older format, use the following command, which asks for the current password and then for the password of the new key:

```shell
openssl pkcs8 -topk8 -v2 aes-256-cbc -in client.key -out client-pkcs8.key
```

Store the content of `client-pkcs8.key` in the secret referenced by `key`, and its password in the secret referenced by `keyPasswd`.

#### CDN logs {#mtls-cdn}

Like other properties, an `mtls` block under `default` applies to both AEM logs and CDN logs. To use a different certificate for CDN logs, set the `mtls` properties in a `cdn` block. To use mTLS for only AEM logs or only CDN logs, place the `mtls` block in the `aem` or `cdn` block instead of `default`.

After you deploy a configuration that enables CDN log forwarding to a destination, it can take several minutes before the first CDN logs arrive. For HTTPS destinations, CDN log delivery also starts only after your server completes the one-time challenge described in [HTTPS](#https). The challenge request is sent with the same client certificate, so your server must accept that certificate on the challenge path too.

### Certificate rotation and expiry {#mtls-rotation}

To rotate a certificate, update the Cloud Manager secret environment variables that hold the certificate (and the key, if it changed), then re-run the config pipeline. If the log forwarding configuration file itself is unchanged, also make a change to it so that the configuration is applied again. For example, store the new values in new secret environment variables and reference those names in the `mtls` block.

You may also receive a proactive [Actions Center](/help/operations/actions-center.md) notification about 21 days before a client certificate expires. Track certificate expiry dates yourself rather than relying on this notification.

## Logging Destination Configuration {#logging-destinations}

Configurations for the supported logging destinations are listed below, along with any specific considerations.

### Amazon S3 {#amazons3}

CDN logs to Amazon S3 are in beta. To request access, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID. See [CDN logs for Amazon S3, Dynatrace, and New Relic (beta)](#cdn-opt-in) for how to enable them, and [Amazon S3 CDN logs](#amazons3-cdn) for the file layout and considerations.

>[!NOTE]
>
>AEM logs (including Apache/Dispatcher) are uploaded to S3 for each log file type when 100 MB of logs has been collected or after 10 minutes, whichever comes first. This may result in an initial delay for logs being written to S3 once the feature is toggled. [Further information on this behavior](https://docs.fluentbit.io/manual/pipeline/outputs/s3#differences-between-s3-and-other-fluent-bit-outputs). CDN logs are written differently; see [Amazon S3 CDN logs](#amazons3-cdn).

  ```yaml
  kind: "LogForwarding"
  version: "1"
  data:
    awsS3:
      default:
        enabled: true
        region: "your-bucket-region"
        bucket: "your-bucket-name"
        accessKey: "${{AWS_S3_ACCESS_KEY}}"
        secretAccessKey: "${{AWS_S3_SECRET_ACCESS_KEY}}"
  ```

To forward both AEM logs and CDN logs (CDN logs in beta):

  ```yaml
  kind: "LogForwarding"
  version: "1"
  data:
    awsS3:
      default:
        enabled: true
        region: "us-east-1"
        bucket: "your-bucket-name"
        accessKey: "${{AWS_S3_ACCESS_KEY}}"
        secretAccessKey: "${{AWS_S3_SECRET_ACCESS_KEY}}"
      cdn:
        enabled: true
  ```

To forward only CDN logs (in beta):

  ```yaml
  kind: "LogForwarding"
  version: "1"
  data:
    awsS3:
      default:
        enabled: true
        region: "us-east-1"
        bucket: "your-bucket-name"
        accessKey: "${{AWS_S3_ACCESS_KEY}}"
        secretAccessKey: "${{AWS_S3_SECRET_ACCESS_KEY}}"
      aem:
        enabled: false
      cdn:
        enabled: true
  ```

In order to use the S3 Log Forwarder, you will need to preconfigure an AWS IAM user with appropriate policy for accessing your S3 bucket.  See [AWS IAM User Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for how to create IAM user credentials.

The IAM policy should allow the user to use `s3:PutObject`. To forward CDN logs (in beta), also allow `s3:AbortMultipartUpload`. No other permissions are needed: the user doesn't need to read or list the bucket. For example:

```json
{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Action": [
            "s3:PutObject",
            "s3:AbortMultipartUpload"
        ],
        "Resource": "arn:aws:s3:::your-bucket-name/*"
    }]
}
```

If the bucket only receives CDN logs, you can limit `Resource` to `arn:aws:s3:::your-bucket-name/aemcdn/*`.

See [AWS Bucket Policy Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html) for more information on how to implement.

#### Amazon S3 CDN logs (beta) {#amazons3-cdn}

CDN logs to Amazon S3 are in beta. They need access for your program and `cdn.enabled: true`. See [CDN logs for Amazon S3, Dynatrace, and New Relic (beta)](#cdn-opt-in).

CDN logs are written below the `aemcdn/` folder of your bucket. The filename format is `YYYY-MM-DDThh:mm:ss.000-<uniqueid>.log.gz`. For example:

```text
aemcdn/
   2026-03-04T10:00:00.000-WnFWYN9BpOUs2aOVn4ee.log.gz
   2026-03-04T10:00:00.000-0pX8ub2yQcAmLs7rT1kd.log.gz
   2026-03-04T10:05:00.000-h3JkVv9ZqN2wE5sXyR0a.log.gz
```

* Files are gzip-compressed. Each file contains multiple log entries, one JSON object per line. The entries have the same properties as CDN logs written to Azure Blob Storage. The log entry format is described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md#cdn-log), and each entry also includes the additional properties mentioned in the [Log Entry Formats](#log-formats) section below.
* A new set of files is written every 5 minutes. The CDN has many servers, and each server that handled your traffic writes its own file, so expect many files for each 5-minute period, even with little traffic. For example, a low-traffic test environment produced about 50 files every 5 minutes.
* Log entries usually appear in the bucket 1 to 6 minutes after the request.
* The time in the filename is not an exact time window, and files overlap. For example, a file named `…T16:00:00.000-….log.gz` can hold entries from 15:55 to 16:04. Use the `timestamp` property of each entry to find when a request happened.
* Files are not changed after they are written.

Customers are responsible for processing and managing these files, for example with an S3 lifecycle rule on the `aemcdn/` prefix.

Considerations for CDN logs (beta):

* Authentication uses the access key of an IAM user. IAM roles are not supported.
* The IAM user only needs `s3:PutObject` and `s3:AbortMultipartUpload`. It doesn't need permission to read or list the bucket.
* Default bucket encryption with Amazon S3 managed keys (SSE-S3) is supported, and CDN log files are then encrypted at rest.
* Only buckets in standard AWS commercial regions are supported. AWS GovCloud (US) and AWS China regions are not supported. The `region` property must be the region of the bucket.
* **Rejected uploads are not retried.** If the bucket policy or the IAM user's permissions reject an upload of CDN logs, the log entries in that upload are lost without warning. This is different from AEM logs, where failed uploads are retried. Make sure that changes to your bucket policy or IAM user don't block uploads from the CDN.
* We recommend an IAM user that is only allowed `s3:PutObject` and `s3:AbortMultipartUpload` on the bucket (or only on the `aemcdn/` prefix, if the bucket receives only CDN logs), and a bucket policy without IP address conditions.
* If your bucket policy restricts access by IP address, add all of Fastly's published IPv4 and IPv6 ranges to the `aws:SourceIp` condition, and keep them up to date. See [CDN logs and IP allow lists](#cdn-ip-allowlist).
* Buckets that only accept requests through a VPC endpoint (for example, a bucket policy with an `aws:SourceVpce` condition) cannot receive CDN logs.
* To detect lost CDN logs, consider:
  * AWS CloudTrail data events or S3 server access logs. They record rejected `PutObject` requests (HTTP status 403) from Fastly's IP addresses.
  * An alarm that fires when no new objects have arrived under `aemcdn/` for longer than you expect. Files are written every 5 minutes.

### Azure Blob Storage {#azureblob}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     azureBlob:
       default:
         enabled: true
         storageAccountName: "example_acc"
         container: "aem_logs"
         sasToken: "${{AZURE_BLOB_SAS_TOKEN}}

   ```

A SAS token should be used for authentication. It should be created from the Shared access signature page, rather than on the Shared access token page, and should be configured with these settings:

* Allowed services: Blob must be selected.
* Allowed resources: Object and container must be selected.
* Allowed permissions: Read, Write, Add, List, Create must be selected.
* A valid Start and Expiry date/time.

Here is a screenshot of a sample SAS token configuration:

![Azure Blob SAS token configuration](/help/implementing/developing/introduction/assets/azureblob-sas-token-config.png)

If logs have stopped being delivered after previously functioning correctly, check whether the SAS token you configured is still valid, as it may have expired.

#### Azure Blob Storage CDN logs {#azureblob-cdn}

Each of the globally distributed logging servers will produce a new file every few seconds, under the `aemcdn` folder. Once created, the file will no longer be appended to. The filename format is YYYY-MM-DDThh:mm:ss.sss-uniqueid.log. E.g., 2024-03-04T10:00:00.000-WnFWYN9BpOUs2aOVn4ee.log.

As an example, at some point in time:

```text
aemcdn/
   2024-03-04T10:00:00.000-abc.log
   2024-03-04T10:00:00.000-def.log

```

And then 30 seconds later:

```text
aemcdn/
   2024-03-04T10:00:00.000-abc.log
   2024-03-04T10:00:00.000-def.log
   2024-03-04T10:00:30.000-ghi.log
   2024-03-04T10:00:30.000-jkl.log
   2024-03-04T10:00:30.000-mno.log

```

Each file contains multiple json log entries, each on a separate line. The log entry formats are described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md), and each log entry also includes the additional properties mentioned in the [Log Entry Formats](#log-formats) section below.

#### Azure Blob Storage AEM logs {#azureblob-aem}

AEM logs (including Apache/Dispatcher) appear below a folder with the following naming convention:

* aemaccess
* aemerror
* aemrequest
* aemdispatcher
* aemhttpdaccess
* aemhttpderror

Under each folder, a single file will be created and appended to. Customers are responsible for processing and managing this file so it does not grow too large.

See the log entry formats under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md). The log entries will also include the additional properties mentioned in the [Log Entry Formats](#log-formats) section below.

### Datadog {#datadog}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     datadog:
       default:
         enabled: true
         host: "http-intake.logs.datadoghq.eu"
         token: "${{DATADOG_API_KEY}}"
         tags:
            tag1: value1
            tag2: value2

   ```

#### Considerations

* Create an API Key, without any integration with a specific cloud provider.
* The tags property is optional
* For AEM logs, the Datadog source tag is set to one of `aemaccess`, `aemerror`, `aemrequest`, `aemdispatcher`, `aemhttpdaccess`, or `aemhttpderror`
* For CDN logs, the Datadog source tag is set to `aemcdn`
* The Datadog service tag is set to `adobeaemcloud`, but you can overwrite it in the tags section
* If your ingestion pipeline uses Datadog tags to determine the appropriate index for forwarding logs, verify that these tags are correctly configured in the Log Forwarding YAML file. Missing tags may prevent successful log ingestion if the pipeline depends on them.

### Elasticsearch and OpenSearch {#elastic}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     elasticsearch:
       default:
         enabled: true
         host: "example.com"
         user: "${{ELASTICSEARCH_USER}}"
         password: "${{ELASTICSEARCH_PASSWORD}}"
         pipeline: "ingest pipeline name"

   ```

#### Considerations

* by default, the port is 443. It can optionally be overridden with a property named `port`
* For credentials, make sure to use use deployment credentials, rather than account credentials. These are the credentials that are generated in a screen that may resemble this image:

![Elastic deployment credentials](/help/implementing/developing/introduction/assets/ec-creds.png)

* For AEM logs, `index` is set to one of `aemaccess`, `aemerror`, `aemrequest`, `aemdispatcher`, `aemhttpdaccess`, or `aemhttpderror`
* The optional pipeline property should be set to the name of the Elasticsearch or OpenSearch ingest pipeline, which can be configured to route the log entry to the appropriate index. The pipeline's Processor type must be set to *script* and the script language should be set to *painless*. Here is a sample script snippet to route log entries into an index such as aemaccess_dev_26_06_2024:

```text
def envType = ctx.aem_env_type != null ? ctx.aem_env_type : 'unknown';
def sourceType = ctx._index;
def date = new SimpleDateFormat('dd_MM_yyyy').format(new Date());
ctx._index = sourceType + "_" + envType + "_" + date;

```

### HTTPS {#https}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     https:
       default:
         enabled: true
         url: "https://example.com/aem_logs/aem"
         authHeaderName: "X-AEMaaCS-Log-Forwarding-Token"
         authHeaderValue: "${{HTTPS_LOG_FORWARDING_TOKEN}}"

   ```

#### Considerations

* The url string must include **https://** or validation will fail.
* The url may include a port. For example, `https://example.com:8443/aem_logs/aem`. If no port is included in the url string, port 443 (the default HTTPS port) is assumed.

#### HTTPS CDN logs {#https-cdn}

Web requests (POSTs) will be sent continuously, with a json payload that is an array of log entries, with the log entry format described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md#cdn-log). Additional properties are mentioned in the [Log Entry Formats](#log-formats) section below.

There is also be a property named `sourcetype`, which is set to the value `aemcdn`.

>[!NOTE]
>
> Before the first CDN log entry is sent, your HTTP server must successfully complete a one-time challenge: a request sent to the path ``/.well-known/fastly/logging/challenge`` must respond with an asterisk ``*`` in the body and 200 status code.

#### HTTPS AEM logs {#https-aem}

For AEM logs (including apache/dispacher), web requests (POSTs) will be sent continuously, with a json payload that is an array of log entries, with the various log entry formats as described under [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md). Additional properties are mentioned in the [Log Entry Formats](#log-formats) section below.

There is also be a property named `Source-Type`, which is set to one of these values:

* aemaccess
* aemerror
* aemrequest
* aemdispatcher
* aemhttpdaccess
* aemhttpderror

### New Relic Log API {#newrelic-https}

Log Forwarding to New Relic leverages the New Relic HTTPS Log API for ingestion. CDN logs to New Relic are in beta. To request access, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID. See [CDN logs for Amazon S3, Dynatrace, and New Relic (beta)](#cdn-opt-in) for how to enable them.

  ```yaml
    kind: "LogForwarding"
    version: "1"
    data:
      newRelic:
        default:
          enabled: true
          uri: "https://log-api.newrelic.com/log/v1"
          apiKey: "${{NR_API_KEY}}"
  ```

To forward both AEM logs and CDN logs (CDN logs in beta):

  ```yaml
    kind: "LogForwarding"
    version: "1"
    data:
      newRelic:
        default:
          enabled: true
          uri: "https://log-api.newrelic.com/log/v1"
          apiKey: "${{NR_API_KEY}}"
        cdn:
          enabled: true
  ```

To forward only CDN logs (in beta):

  ```yaml
    kind: "LogForwarding"
    version: "1"
    data:
      newRelic:
        default:
          enabled: true
          uri: "https://log-api.newrelic.com/log/v1"
          apiKey: "${{NR_API_KEY}}"
        aem:
          enabled: false
        cdn:
          enabled: true
  ```

>[!NOTE]
>
>Log forwarding to New Relic is only available to customer owned New Relic accounts.

#### Considerations

* New Relic provides region specific endpoints based on where your New Relic account is provisioned. Set `uri` to the Log API endpoint for your account's region, for example `https://log-api.newrelic.com/log/v1` for accounts in the US region. See [New Relic documentation](https://docs.newrelic.com/docs/logs/log-api/introduction-log-api/#endpoint) for further information.
* For `apiKey`, use a New Relic license key (key type **INGEST - LICENSE**) from the account that receives the logs. The same key is used for AEM logs and CDN logs.
* For AEM logs, the `source` attribute is set to one of `aemaccess`, `aemerror`, `aemrequest`, `aemdispatcher`, `aemhttpdaccess`, or `aemhttpderror`. For CDN logs (beta), `source` is set to `aemcdn`, and each record carries all CDN log properties. For example, to query CDN logs: `FROM Log SELECT * WHERE source = 'aemcdn' SINCE 1 hour ago`.
* In CDN log entries (beta) sent to New Relic, `timestamp` is a number: the request start time in milliseconds since the Unix epoch. Other logging destinations receive `timestamp` as an ISO 8601 string.
* CDN logs (beta) can add significant volume to your New Relic ingestion. See [CDN logs for Amazon S3, Dynatrace, and New Relic (beta)](#cdn-opt-in).

### Dynatrace Log API {#dynatrace-https}

Log Forwarding to Dynatrace leverages the Dynatrace HTTPS API for ingestion. CDN logs to Dynatrace are in beta. To request access, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID. See [CDN logs for Amazon S3, Dynatrace, and New Relic (beta)](#cdn-opt-in) for how to enable them.

The token requires the **Ingest logs** (`logs.ingest`) scope. The same token is used for AEM logs and CDN logs.

  ```yaml
    kind: "LogForwarding"
    version: "1"
    data:
      dynatrace:
        default:
          enabled: true
          environmentId: "${{DYNATRACE_ENVID}}"
          token: "${{DYNATRACE_TOKEN}}"
  ```

To forward both AEM logs and CDN logs (CDN logs in beta):

  ```yaml
    kind: "LogForwarding"
    version: "1"
    data:
      dynatrace:
        default:
          enabled: true
          environmentId: "${{DYNATRACE_ENVID}}"
          token: "${{DYNATRACE_TOKEN}}"
        cdn:
          enabled: true
  ```

To forward only CDN logs (in beta):

  ```yaml
    kind: "LogForwarding"
    version: "1"
    data:
      dynatrace:
        default:
          enabled: true
          environmentId: "${{DYNATRACE_ENVID}}"
          token: "${{DYNATRACE_TOKEN}}"
        aem:
          enabled: false
        cdn:
          enabled: true
  ```

#### Considerations

* Only Dynatrace SaaS environments are supported. `environmentId` is the ID in your environment URL, `https://<environmentId>.live.dynatrace.com`. Use the ID only, not a URL or a host name: for CDN logs it can't contain dots. Dynatrace Managed and ActiveGate endpoints are not supported.
* Each log entry includes a `source` property. For AEM logs it is one of `aemaccess`, `aemerror`, `aemrequest`, `aemdispatcher`, `aemhttpdaccess`, or `aemhttpderror`. For CDN logs (beta) it is `aemcdn`.
* CDN logs (beta) can add significant volume to your Dynatrace ingestion. See [CDN logs for Amazon S3, Dynatrace, and New Relic (beta)](#cdn-opt-in).

#### Finding CDN logs in Dynatrace (beta) {#dynatrace-cdn}

Dynatrace stores each CDN log entry, as JSON text, in the `content` of a log record, and uses the entry's `timestamp` as the record time. The CDN log properties, such as `source`, `url`, and `status`, are not separate log attributes. The same applies to AEM logs forwarded to Dynatrace. As a result:

* Filters in the simple mode of the classic log viewer don't work on these properties. A filter on an attribute that doesn't exist is ignored, so all logs are returned.
* The log `status` of these records shows `NONE`, because the CDN `status` property is the HTTP status code, not a log level.

Use advanced mode (DQL) instead. To find CDN logs from the last hour:

```text
fetch logs, from: now() - 1h
| filter matchesPhrase(content, "aemcdn")
```

To parse the CDN log properties and show some of them:

```text
fetch logs, from: now() - 1h
| parse content, "JSON:cdn"
| filter cdn[source] == "aemcdn"
| fields timestamp, cdn[url], cdn[status], cdn[pop], cdn[cache], cdn[aem_tier]
```

### Splunk {#splunk}

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     splunk:
       default:
         enabled: true
         host: "splunk-host.example.com"
         token: "${{SPLUNK_TOKEN}}"
         index: "aemaacs"
   ```

#### Considerations

* By default, the port is 443. It can optionally be overridden with a property named `port`.
* The sourcetype field will have one of the following values, depending on the specific log: *aemaccess*, *aemerror*,
*aemrequest*, *aemdispatcher*, *aemhttpdaccess*, *aemhttpderror*, *aemcdn*
* If the required IPs have been allowlisted and logs are still not being delivered, verify that there are no firewall rules enforcing Splunk token validation. Fastly performs an initial validation step where an invalid Splunk token is intentionally sent. If your firewall is set to terminate connections with invalid Splunk tokens, the validation process will fail, preventing Fastly from delivering logs to your Splunk instance.

>[!NOTE]
>
> [If migrating](#legacy-migration) from legacy Log Forwarding to this self-serve model, the `sourcetype` field's values sent to your Splunk index may have changed, so adjust accordingly.

### Sumo Logic {#sumologic}

When configuring Sumo Logic for data ingestion you will be presented with an "HTTP Source Address" which provides the host, receiverURI and the private key in a single string.  For example:

`https://collectors.de.sumologic.com/receiver/v1/http/ZaVnC...`

You will need to copy the last section of the URL (without the preceeding `/`) and add that as a [CloudManager Secret Environment Variable](/help/operations/config-pipeline.md#secret-env-vars) as described in the [Setup](#setup) section above, then reference that variable in your configuration.  An example is provided below.

  ```yaml
  kind: "LogForwarding"
  version: "1"
  data:
    sumoLogic:
      default:
        enabled: true
        collectorURL: "https://collectors.de.sumologic.com/receiver/v1/http"
        privateKey: "${{SUMOLOGIC_PRIVATE_KEY}}"
        index: "aem-logs"
  ```

>[!NOTE]
>The `index` field behavior depends on the log type:
>
>* **AEM logs (including Apache/Dispatcher)**: routed to the partition specified by `index`, provided you have a Sumo Logic Enterprise subscription. Non-Enterprise subscriptions route to the `sumologic_default` partition instead.
>* **CDN logs**: the `index` field is ignored, as indexing is not technically supported for CDN logs forwarded to Sumo Logic. CDN logs are always routed to the `sumologic_default` partition.
>
>See the [Sumo Logic Partitioning Documentation](https://help.sumologic.com/docs/search/optimize-search-partitions/) for more information.

## CDN logs for Amazon S3, Dynatrace, and New Relic (beta) {#cdn-opt-in}

CDN log forwarding to Amazon S3, Dynatrace, and New Relic is in beta. Forwarding AEM logs (including Apache/Dispatcher) to these destinations is not affected and doesn't need a request.

To forward CDN logs to one of these destinations, complete both steps:

1. **Request access for your program.** Email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com) with your program ID and the destinations you want to use. Adobe replies when access is enabled for your program.
1. **Enable CDN logs for each destination.** After access is enabled, set `enabled: true` in the `cdn` block of the destination in your Log Forwarding configuration, and run the config pipeline. See the example below.

Both steps are needed:

* Access alone doesn't forward any CDN logs. For most logging destinations, an enabled `default` block forwards both AEM logs and CDN logs. For Amazon S3 (`awsS3`), Dynatrace (`dynatrace`), and New Relic (`newRelic`), CDN logs are forwarded **only** when the `cdn` block explicitly sets `enabled: true`.
* If you set `cdn.enabled: true` before access is enabled for your program, the configuration deploys without errors, but no CDN logs are forwarded to these destinations.

The `cdn` block inherits all other properties from the `default` block, including the credentials, so `enabled: true` is the only property you need to add:

   ```yaml
   kind: "LogForwarding"
   version: "1"
   data:
     newRelic:
       default:
         enabled: true
         uri: "https://log-api.newrelic.com/log/v1"
         apiKey: "${{NR_API_KEY}}"
       cdn:
         enabled: true
   ```

For a program with access, the configuration works as follows:

| Configuration | AEM logs | CDN logs to Amazon S3, Dynatrace, New Relic | CDN logs to other destinations |
|---|---|---|---|
| `default.enabled: true` only | Forwarded | **Not forwarded** (until 26 January 2027) | Forwarded |
| `default.enabled: true` and `cdn.enabled: true` | Forwarded | Forwarded | Forwarded |
| `default.enabled: true` and `cdn.enabled: false` | Forwarded | Not forwarded | Not forwarded |
| `default.enabled: true`, `aem.enabled: false` and `cdn.enabled: true` | Not forwarded | Forwarded | Forwarded |

As with other destinations, properties set in the `cdn` block override the values from `default`. To forward only CDN logs, set `aem.enabled: false`, as in the last row.

To stop forwarding CDN logs, set `cdn.enabled: false` and run the config pipeline. CDN log forwarding to that destination stops when the configuration is deployed. AEM logs are not affected.

>[!NOTE]
>
>**Why CDN logs are opt-in for these destinations**
>
>Many organizations configured Amazon S3, Dynatrace, or New Relic for AEM logs before CDN log forwarding was available for them. CDN logs contain an entry for every request handled by the CDN, including requests served from the CDN cache, so they are usually much larger than AEM logs. They are also sent from different IP addresses than AEM logs (see [Transport & Advanced Networking](#transport-advancednetworking)). Requiring `cdn.enabled: true` for now means existing configurations keep forwarding only AEM logs, with no unexpected ingestion costs or traffic, and gives you time to decide.

>[!IMPORTANT]
>
>**The access request and the opt-in are temporary.** From Tuesday, 26 January 2027, no access request is needed, and Amazon S3, Dynatrace, and New Relic follow the same rule as other destinations: an enabled `default` block forwards CDN logs as well. To keep forwarding only AEM logs to one of these destinations, set `cdn.enabled: false` for it. You can set it now; it has the same effect before and after that date.

Before you enable CDN logs, estimate the additional volume. Logging vendors that bill by ingested volume, such as Dynatrace and New Relic, charge for CDN logs in the same way as for AEM logs.

To give feedback on the beta, email [aemcs-logforwarding-beta@adobe.com](mailto:aemcs-logforwarding-beta@adobe.com).

## Log Entry Formats {#log-formats}

See [Logging for AEM as a Cloud Service](/help/implementing/developing/introduction/logging.md) for the format of each respective log type (CDN logs, and AEM logs including Apache/Dispatcher). Some logging destinations add or change properties in CDN log entries, for example the format of `timestamp` for New Relic. See [CDN log entries by logging destination](/help/implementing/developing/introduction/logging.md#cdn-log-destinations).

Since logs from multiple programs and environments may be forwarded to the same logging destination, in addition to the output described in the logging article, the following properties will be included in each log entry:

* aem_env_id
* aem_env_type
* aem_program_id
* aem_tier

As an example, the properties could have the following values:

```text
aem_env_id: 1242
aem_env_type: dev
aem_program_id: 12314
aem_tier: author

```

## Migrating from Legacy Log Forwarding {#legacy-migration}

Before Log Forwarding configuration was achieved through a self-serve model, customers were requested to open support tickets, where Adobe would initiate the integration.

Customers who had been setup in that manner by Adobe are welcome to adapt to the self-serve model at their convenience. There are several reason to make this transition:

* A new environment (e.g., a new dev env or RDE) has been provisioned.
* Changes to your existing Splunk endpoint or credentials.
* Adobe had setup your log forwarding before CDN logs were available and you would like to receive CDN logs.
* A conscious decision to proactively adapt to the self-serve model so your organization has the knowledge even before a time-sensitive change is necessary.

When ready to migrate, simply configure the YAML file as described in the preceding sections. Use the Cloud Manager config pipeline to deploy to each of the environments where the configuration should be applied.

It is recommended, but not required, that a configuration is deployed to all environments so they are all under self-serve control. If not, you may forget which environments have been configured by Adobe versus those configured in a self-serve way.

>[!NOTE]
>
>The `sourcetype` field's values sent to your Splunk index may have changed, so adjust accordingly.
>
>When Log Forwarding is deployed to an environment previously configured by Adobe support, you may receive duplicate logs for up to a few hours. This will eventually auto-resolve.

