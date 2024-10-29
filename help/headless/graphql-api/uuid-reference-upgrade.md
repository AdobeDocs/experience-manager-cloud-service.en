---
title: Upgradng your Content Fragments for UUID References
description: Learn how to upgrade your Content Fragments for optimized UUID references in Adobe Experience Manager as a Cloud Service for headless content delivery.
feature: Headless, Content Fragments,GraphQL API
role: Admin, Developer
---
# Upgrading your Content Fragments for UUID References {#upgrading-content-fragments-for-UUID-references}

To optimize the stability of your GraphQL filters run a procedure to upgrade the content and fragment references in your Content Fragments to use universally unique identifiers (UUID).

Originally Content Fragment Models provided the data types of **Content Reference** and **Fragment Reference**. Both of these are based on a path that points to the referenced resource, and which can become outdated if the resource is moved. Although these are more than sufficient in most scenarios, Content Fragment Models have been extended to also provide references based on a UUID: **Content Reference (UUID)** and **Fragment Reference (UUID)**. 

The new reference types (supporting UUIDs) can be used in new Content Fragment Models and Fragments, and to extend existing instances. 

You can also upgrade existing Content Fragments and Models to replace any **Content Reference** and **Fragment Reference** fields with the corresponding new **Content References (UUID)** and **Fragment Reference (UUID)** fields.

## Upgrade Considerations {#upgrade-considerations}

## What will be upgraded {#what-will-be-upgraded}

The following updates are made:

* Fields of the data types:
  * **Content Reference** are converted to **Content Reference (UUID)** 
  * **Fragment Reference** are converted to **Fragment Reference (UUID)** 
* The path based reference values held in these fields are replaced by the corresponding UUIDs

## What will NOT be upgraded {#what-will-not-be-upgraded}

The following references will not be upgraded:

* Page references - UUIDs are not supported for these yet
* Any [invalid references](#what-happens-if-there-are-invalid-references-in-the-existing-data)

## When you should not upgrade {#when-you-should-not-upgrade}

You should not upgrade:

* When any of your Content Fragments use page references; as UUIDs are yet not supported for these

## What happens if there are invalid references in the existing data {#what-happens-if-there-are-invalid-references-in-the-existing-data}

Invalid references will not be upgraded, as if the Content Fragment path, or Asset path, is invalid there will not be a corresponding UUID to assign. The original reference will remain untouched.

Being invalid, they are not usable, irrespective of the upgrade.

You can run the content upgrade in `dry-run` mode to identify any invalid references, by listing them in the log files. You can then fix those, before running the actual content upgrade.

## Upgrade Planning {#upgrade-planning}

## Plan a content freeze time period {#plan-a-content-freeze-time-period}

Execution of the content upgrade should be planned during a content freeze period.

The duration of content freeze depends on volume of Content Fragments being upgraded, and accordingly can vary from few minutes till few hours, and also depends upon the parameters used for the starting the content upgrade.

## Running the content upgrade {#running-the-content-upgrade}

The content upgrade can be managed using the endpoint: `/libs/dam/cfm/maintenance.json`

>[!NOTE]
>
>Your account needs the `Administrator` role to access the endpoint. 

### Start a content upgrade {#start-a-content-upgrade}

| Endpoint | HTTP request type | Comment |
|--- |--- |--- |
| `/libs/dam/cfm/maintenance.json`| `POST`| |
| action | `start`| |
| basePath | `/conf` | Specify either:<ul><li>the root `/conf` to upgrade all the AEM configurations</li><li>a selected AEM configuration path. for which the content upgrade will be executed<br>For example: `/conf/wknd-shared` will only upgrade the single tenant `wknd-shared`</li></ul>
| dryRun | `true`, `false`| <ul><li>`false`: simulate the content upgrade, without saving any content changes</li><li>`true`: perform the content upgrade, and save content changes</li></ul> |
| interval | `10`| Interval in seconds, after which next segment of Content Fragments, or models will be upgraded. |
| jobId | `UUID`| The ID of the job that executes the content upgrade.<ul><li>This ID will be required in any subsequent calls related to this execution.</li><li>If the `mode` value is set to `replicate` execution on AEM Publish instances will also need to be under the same `jobId`.</li></ul> |
| mode | `replicate`, `noReplicate`| <ul><li>`replicate`: will replicate the same job on all AEM Publish instances</li><li>`noReplicate`: will only run the job on AEM Author instances</li></ul> |
| parameters | The content upgrade parameters | These include the initial parameters provided to start the content upgrade, and also some internal defaults.|
| **Request parameters** | **Value(s)** | |
| &nbsp; | &nbsp; | &nbsp; |
| **Response details** | **Value(s)** | | 
| segmentSize | `1000` | This is the number of Content Fragments or models that will be upgraded in one segment (batch). |
| serviceTypeId | `uuidUpgradeService` | This is a fixed service ID.

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
| **Request parameters** | **Value(s)** | |
| action | status | |
| jobId | `<UUID>` | The `jobId` that was returned from the call to start the content upgrade. |
| **Response details** | **Value(s)** | | 
| status | JSON values | Contains the detailed status of the content upgrade:<ul><li>Updated after every interval (seconds).</li><li>`uuidUpgradeService` execution has two phases:<ol><li>phase-0 to upgrade content fragment models</li><li>phase-1 to upgrade content fragments</li></ol></li><li>In each phase, statistics will will be updated after every interval.</li><li>"jobStatus": "COMPLETED" will mark the upgrade as successfully completed.</li><li>Other status values are self-explanatory.</li></ul>

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

### Abort a content upgrade {#abort-a-content-upgrade}

>[!CAUTION]
>
>Aborting a content upgrade (that is not a dry run):
>
>* will not revert any changes already made
>* might leave your content in a mixed state 
>
>Use this action with caution.

| Endpoint | HTTP request type | Comment |
|--- |--- |--- |
| `/libs/dam/cfm/maintenance.json`| `POST`| |
| **Request parameters** | **Value(s)** | |
| action | abort | |
| jobId | `<UUID>` | The `jobId` that was returned from the call to start the content upgrade. |
| **Response details** | **Value(s)** | | 
| status | JSON values | Contains the detailed status of the content upgrade:<ul><li>The status to note is "jobStatus": "ABORTED".<br>After this, any pending segments of data will not be processed.</li><li>If the jobStatus is "COMPLETED" before an abort, the call will not have any effect.</li></ul>

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
