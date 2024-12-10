---
title: Upgrade your Content Fragments for UUID References
description: Learn how to upgrade your Content Fragments for optimized UUID references in Adobe Experience Manager as a Cloud Service for headless content delivery.
feature: Headless, Content Fragments,GraphQL API
role: Admin, Developer
exl-id: 004d1340-8e3a-4e9a-82dc-fa013cea45a7
---
# Upgrade your Content Fragments for UUID References {#upgrade-content-fragments-for-UUID-references}

>[!IMPORTANT]
>
>Various features of the GraphQL API for use with Content Fragments are available through the Early Adopter Program.
>
>To see the status, and how to apply if you are interested, check the [Release Notes](/help/release-notes/release-notes-cloud/release-notes-current.md).

To optimize the stability of your GraphQL filters, you can upgrade the content and fragment references in your Content Fragments so that they use universally unique identifiers (UUID).

Originally Content Fragment Models provided the data types of **Content Reference** and **Fragment Reference**. Both of these references use a path to point to the referenced resource, and this path can become outdated if the resource is moved. Although such references are more than sufficient in most scenarios, Content Fragment Models have been extended to also provide references based on a UUID:

* **Content Reference (UUID)** 
* **Fragment Reference (UUID)**. 

These new reference types can be used both in new Content Fragment Models and Fragments, and to extend existing instances. 

To upgrade existing Content Fragments and Models, you can run the procedure documented here. 

>[!CAUTION]
>
>Before running the upgrade procedure you should always [Execute a dry run](#execute-a-dry-run) to highlight any potential issues with your content.

## What is upgraded {#what-is-upgraded}

The following updates are made:

* Fields of the data types:
  * **Content Reference** are converted to **Content Reference (UUID)** 
  * **Fragment Reference** are converted to **Fragment Reference (UUID)** 
* The values of the path based references held in these fields are replaced by the corresponding UUIDs

>[!NOTE]
>
>After the upgrade both Data Types are still available in the Content Fragment Model editor. You can create new fields based on both types (though it is anticipated that you will use the UUID based types) and rerun the upgrade if required.

## What is NOT upgraded {#what-is-not-upgraded}

The following references are not upgraded:

* Page references - UUIDs are not supported yet
* Any invalid references; for example, where the target of the Content Fragment path, or Asset path, does not exist

  * Invalid references are not upgraded, as if the Content Fragment path, or Asset path, is invalid there is not a corresponding UUID to assign. The original reference remains untouched.

  * Use a [dry run](#execute-a-dry-run) to detact any invalid references.

  >[!NOTE]
  >
  >Being invalid, they are not usable, irrespective of the upgrade.

## When you should not upgrade {#when-you-should-not-upgrade}

Do not upgrade:

* When any of your Content Fragments use page references; as UUIDs are yet not supported for page references

## Limitations of UUID references {#limitations-of-uuid-references}

Currently the following limitations apply when using references based on a UUID:

* Models

  * New Content Fragment Models with either Content Fragment UUID or Content Reference UUID fields cannot be created via OpenAPI.
  * The `id` field for models has not been changed to be UUID based. It uses the base64 decoded path of the model. Models cannot be moved, therefore, this value is still stable.

* Assets

  * When creating a Content Fragment via OpenAPI,`fragment-reference` or `content-reference` field types must be used for specifying references to a fragment or an asset respectively - even when setting the value of a UUID based reference field.

## Upgrade Planning {#upgrade-planning}

There are a few preparation steps before running your upgrade.

### Execute a dry run {#execute-a-dry-run}

It is recommended that *every* time you upgrade your content, you first perform a dry run. This will create log files with entries that highlight any potential issues:

* Invalid references
* Page references

Run the content upgrade in `dryRun` mode to:

* identify any invalid references; by listing them in the log files
  You can then fix these references, before running the actual content upgrade.
* identify any page references; by listing them in the log files
  When page references are detected you [should not run the content upgrade](#when-you-should-not-upgrade).


### Enforce a content freeze {#enforce-a-content-freeze}

Execution of the content upgrade should be planned during a content freeze period.

The duration of the content freeze depends on the volume of Content Fragments being upgraded. Accordingly, the upgrade can range from a few minutes up to a few hours, and also depends upon the parameters used when starting the content upgrade.

## Running the content upgrade {#running-the-content-upgrade}

The content upgrade can be managed using the endpoint: `/libs/dam/cfm/maintenance.json`

>[!NOTE]
>
>Your account needs the `Administrator` role to access the endpoint. 

### Start a content upgrade {#start-a-content-upgrade}

| Endpoint | HTTP request type | Comment |
|--- |--- |--- |
| `/libs/dam/cfm/maintenance.json`| `POST`| |
| **Request parameters** | **Value** | |
| action | `start`| |
| serviceTypeId | `uuidUpgradeService` | The service type ID (predefined, fixed value). |
| segmentSize | `1000` | The number of Content Fragments or models that will be upgraded in one segment (batch). |
| basePath | `/conf` | Specify either:<ul><li>the root `/conf` to upgrade all the AEM configurations</li><li>a selected AEM configuration path. for which the content upgrade is executed<br>For example: `/conf/wknd-shared` only upgrades the single tenant `wknd-shared`</li></ul> |
| interval | `10`| Interval in seconds, after which the next segment of Content Fragments, or models is upgraded. |
| mode | `replicate`, `noReplicate`| <ul><li>`replicate`: replicates the same job on all AEM Publish instances</li><li>`noReplicate`: only runs the job on AEM Author instances</li></ul> |
| dryRun | `true`, `false`| <ul><li>`false`: simulate the content upgrade, without saving any content changes</li><li>`true`: perform the content upgrade, and save content changes</li></ul> |
| **Response details** | **Value** | | 
| jobId | `UUID`| The ID of the job that executes the content upgrade.<ul><li>This ID is required in any subsequent calls related to this execution.</li><li>If the `mode` value is set to `replicate`, execution on AEM Publish instances also need to be under the same `jobId`.</li></ul> |
| parameters | The content upgrade parameters | These include the initial parameters provided to start the content upgrade, and some internal defaults. |


### Example Content Upgrade Request {#example-content-upgrade-request}

+++Request

```http
POST http://localhost:4502/libs/dam/cfm/maintenance.json
Content-Type: application/json
Authorization: _REPLACE_WITH_VALID_AUTH_
Accept: application/json
 
{
    "action": "start",
    "serviceTypeId": "uuidUpgradeService",
    "segmentSize": 1000,
    "basePath": "/conf/wknd-shared",
    "interval": 10,
    "mode": "replicate",
    "dryRun": true
}
```

+++

+++Response

```http
HTTP/1.1 200 OK
Date: Wed, 16 Oct 2024 14:34:37 GMT
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Content-Type: application/json
Content-Length: 386
 
{
  "jobId": "91af43a6-63ff-45e5-ac7b-06ccf565bdfa",
  "jcr:created": 1729089277309,
  "parameters": {
    "mode": "replicate",
    "dryRun": true,
    "segmentSize": 1000,
    "serviceTypeId": "uuidUpgradeService",
    "action": "start",
    "basePath": "/conf/wknd-shared",
    "topic": "cfm/maintenance",
    "interval": 10,
    "cronSchedule": "*/10 * * * * ?"
  }
}
```

+++

### Get the status of a content upgrade {#get-the-status-of-a-content-upgrade}

| Endpoint | HTTP request type | Comment |
|--- |--- |--- |
| `/libs/dam/cfm/maintenance.json`| `GET`| |
| **Request parameters** | **Value** | |
| action | status | |
| jobId | `<UUID>` | The `jobId` that was returned from the call to start the content upgrade. |
| **Response details** | **Value** | | 
| status | JSON values | Contains the detailed status of the content upgrade:<ul><li>Updated after every interval (seconds).</li><li>`uuidUpgradeService` execution has two phases:<ol><li>phase-0 to upgrade content fragment models</li><li>phase-1 to upgrade content fragments</li></ol></li><li>In each phase, statistics are updated after every interval.</li><li>"jobStatus": "COMPLETED" marks the upgrade as successfully completed.</li><li>Other status values are self-explanatory.</li></ul> |

### Example Content Upgrade Status Request {#example-content-upgrade-status-request}

+++Request

```http
GET http://localhost:4502/libs/dam/cfm/maintenance.json?action=status&jobId=91af43a6-63ff-45e5-ac7b-06ccf565bdfa
Authorization: _REPLACE_WITH_VALID_AUTH_
Accept: application/json
```

+++

+++Response

```http
HTTP/1.1 200 OK
Date: Wed, 16 Oct 2024 14:35:51 GMT
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Content-Type: application/json
Content-Length: 1116
 
{
  "jobId": "91af43a6-63ff-45e5-ac7b-06ccf565bdfa",
  "jcr:created": 1729089277309,
  "eventProcessed": 1,
  "parameters": {
    "mode": "replicate",
    "dryRun": true,
    "segmentSize": 1000,
    "serviceTypeId": "uuidUpgradeService",
    "action": "start",
    "confPath": "/conf/wknd-shared",
    "topic": "cfm/uuid-migration",
    "interval": 10,
    "cronSchedule": "*/10 * * * * ?"
  },
  "status": {
    "jobStatus": "COMPLETED",
    "lastModified": 1729089310301,
    "currentPhaseIndex": 1,
    "phases": {
      "phase-0": {
        "bookmark": 1727183332520,
        "stats": {
          "successCount": 2,
          "skippedCount": 1,
          "errorCount": 0
        },
        "name": "modelUpgrade",
        "lastModified": 1729089290040,
        "isCompleted": true
      },
      "phase-1": {
        "bookmark": 1727183347990,
        "stats": {
          "successCount": 29,
          "skippedCount": 0,
          "errorCount": 1
        },
        "name": "cfUpgrade",
        "lastModified": 1729089310298,
        "isCompleted": true
      }
    }
  }
}
```

+++

+++Sample log files

In addition to the status of a running content upgrade obtained from the HTTP endpoint, AEM logs provide detailed information of the progress on the content level. For example:

```xml
#Successful model upgrade
com.adobe.cq.dam.cfm.impl.servicing.uuid.* Phase phase-0: resource: /conf/wknd-shared/settings/dam/cfm/models/article , status: SUCCESS, skips: [], errors: []
 
#Successful content fragment upgrade
com.adobe.cq.dam.cfm.impl.servicing.uuid.* Phase phase-1: resource: /content/dam/wknd-shared/en/magazine/san-diego-surf-spots/san-diego-surfspots , status: SUCCESS, skips: [], errors: []
 
#Unsuccessful/Skipped model upgrade
com.adobe.cq.dam.cfm.impl.servicing.uuid.* Phase phase-0: resource: /conf/wknd-shared/settings/dam/cfm/models/adventure , status: SKIPPED, skips: [Model: '/conf/wknd-shared/settings/dam/cfm/models/adventure', no upgradeable fields found], errors: []
 
#Unsuccessful content fragment upgrade
com.adobe.cq.dam.cfm.impl.servicing.uuid.* Phase phase-1: resource: /content/dam/wknd-shared/en/magazine/western-australia/western-australia-by-camper-van , status: FAILED, skips: [], errors: [Path '/content/dam/wknd-shared/en/magazine/western-australia/western-australia-by-camper-van', Variation: 'master' Field 'featuredImage', Value '/content/dam/wknd-shared/en/magazine/western-australia/adobestock_156407519.jpeg' is invalid; will not upgrade this field.] 
```

Additionally, after the processing of each segment (batch) of Content Fragments and Models, an accumulated status is logged, summarizing the progress so far. For example:

```xml
com.adobe.cq.dam.cfm.impl.servicing.PhaseChainProcessor Phase phase-x, processed a segment, stats: {successCount=29, skippedCount=0, errorCount=1}
```

+++

### Abort a content upgrade {#abort-a-content-upgrade}

>[!CAUTION]
>
>Aborting a content upgrade (that is not a dry run):
>
>* does not revert any changes already made
>* might leave your content in a mixed state 
>
>Use this action with caution.

| Endpoint | HTTP request type | Comment |
|--- |--- |--- |
| `/libs/dam/cfm/maintenance.json`| `POST`| |
| **Request parameters** | **Value** | |
| action | abort | |
| jobId | `<UUID>` | The `jobId` that was returned from the call to start the content upgrade. |
| **Response details** | **Value** | | 
| status | JSON values | Contains the detailed status of the content upgrade:<ul><li>The status to note is "jobStatus": "ABORTED".<br>After an abort action, any pending segments of data will not be processed.</li><li>If the jobStatus is "COMPLETED" before an abort, the call does not have any effect.</li></ul> |

### Example Abort a Content upgrade Request {#example-abort-content-upgrade-request}

+++Request

```http
POST http://localhost:4502/libs/dam/cfm/maintenance.json
Content-Type: application/json
Authorization: Basic YWRtaW46YWRtaW4=
Accept: application/json
 
{
    "action": "abort",
    "jobId": "b1dbf6f9-5f59-4007-b631-01b63cd17807"
    "mode": "replicate",
}
```

+++

+++Response

```http
HTTP/1.1 200 OK
Date: Wed, 16 Oct 2024 14:39:03 GMT
 
{
  "jobId": "b1dbf6f9-5f59-4007-b631-01b63cd17807",
   ...
  "eventProcessed": 2,
  "parameters": {
    ...
    "abort": true,
    ...
  },
  "status": {
     "jobStatus": "ABORTED",
    ...
  }
}
```

+++
