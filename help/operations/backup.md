---
title: Backup and Restore in AEM as a Cloud Service
description: Backup and Restore in AEM as a Cloud Service
exl-id: 469fb1a1-7426-4379-9fe3-f5b0ebf64d74
---
# Backup and Restore in AEM as a Cloud Service

Should content or data corruption occur, AEM as a Cloud Service can restore a customer's full application (code and content) to specific, predetermined times in the last seven days, replacing what was on production.
If a customer's deployment, meaning the deployed application code is either broken or buggy, it is preferable to fix it and roll forward to a new release rather than restoring it from backup. Backup is performed in a manner that has no impact on the runtime performance of an application.

>[!CAUTION]
>
>This feature should be used only when there are serious issues with either code or content. The recent data between the time of the restored backup and the present will be lost. Staging will also be restored to the old version.

## How to Use

Customers should file a support ticket, describing the issue being experienced. This will lead to an investigation by Adobe support who will determine if a restore is necessary.

AEM as a Cloud Service supports:

* 24 hour point in time recovery, meaning that the system can be restored to any point in the last 24 hours.
* Restore from a specific, Adobe-defined timestamp taken once a day for the last 7 days.  Any replication messages (deletes, updates, creates) will be preserved.

In all cases, the custom code version will be the taken from the last successful deployment before the restore point.

The Recovery Time Objective (RTO) will vary based on the size of the repository, but as a general guideline once the restore sequence begins it should take around 30 minutes.

Following a restore, the AEM version will be updated to the most recent.

**The data from deleted environments is permanently lost and cannot be recovered.**
