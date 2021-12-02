---
title: Backup and Restore in AEM as a Cloud Service
description: Backup and Restore in AEM as a Cloud Service
exl-id: 469fb1a1-7426-4379-9fe3-f5b0ebf64d74
---
# Backup and Restore in AEM as a Cloud Service {#backup-aemaacs}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_backuprestore"
>title="Backup & Restore"
>abstract="AEM as a Cloud Service can restore a customer's full application (code and content) to specific, predetermined times in the last seven days, replacing what was on production. This feature should be used only when there are serious issues with either code or content. The recent data between the time of the restored backup and the present will be lost. Staging will also be restored to the old version."

Should content or data corruption occur, AEM as a Cloud Service can restore a customer's full application (code and content) to specific, predetermined times in the last seven days, replacing what was on production.
If a customer's deployment, meaning the deployed application code is either broken or buggy, it is preferable to fix it and roll forward to a new release rather than restoring it from backup. Backup is performed in a manner that has no impact on the runtime performance of an application.

>[!CAUTION]
>
>This feature should be used only when there are serious issues with either code or content. The recent data between the time of the restored backup and the present will be lost. Staging will also be restored to the old version.

## How to Use {#how to use}

Customers should file a support ticket, describing the issue being experienced. This will lead to an investigation by Adobe support who will determine if a restore is necessary.

AEM as a Cloud Service supports:

* 24 hour point in time recovery, meaning that the system can be restored to any point in the last 24 hours.
* Restore from a specific, Adobe-defined timestamp taken twice a day for the last 7 days.  Any replication messages (deletes, updates, creates) will be preserved.

In all cases, the custom code version will be the taken from the last successful deployment before the restore point.

The Recovery Time Objective (RTO) will vary based on the size of the repository, but as a general guideline, the recovery sequence should take anywhere from 30 minutes to several hours.

Following a restore, the AEM version will be updated to the most recent.

>[!CAUTION]
>
>Data from deleted environments is permanently lost and cannot be recovered.

## Offsite Backup {#offsite-backup}

While regular backups cover the risk of accidental deletions or technical failures within AEM Cloud Services, the risks that can arise from the failure of a region must also be covered. In addition to availability, the greatest risk in such data region outages is primarily a loss of data.
AEM as a Cloud Service covers this risk as standard for all AEM production environments by continuously copying the entire AEM content to a remote region and making it available for recovery for a period of 3 months. We call this capability Offsite Backup.
The restoration of AEM Cloud Services for stage and production environments is carried out by AEM Service Reliability Engineering in the event of data region outages.
