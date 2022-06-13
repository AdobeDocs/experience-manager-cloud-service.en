---
title: Content Restore in AEM as a Cloud Service
description: Learn how to restore your AEM as a Cloud Service content from backup using Cloud Manager.
exl-id: 469fb1a1-7426-4379-9fe3-f5b0ebf64d74
---

# Content Restore in AEM as a Cloud Service {#content-restore}

>[!CONTEXTUALHELP]
>id="aemcloud_golive_backuprestore"
>title="Backup & Restore"
>abstract="Learn how to restore your AEM as a Cloud Service content from backup using Cloud Manager."

Learn how to restore your AEM as a Cloud Service content from backup using Cloud Manager.

## Overview {#overview}

Cloud Manager's self-service restore process copies data from Adobe system backups and restores it to its original environment. A restore is performed to return data that has been lost, damaged, or accidentally deleted to its original condition.

The restore process only affects content, leaving your code and version of AEM unchanged. You can initiate a restore operation of individual environments at any time.

Cloud Manager provides two types of backups from which you may restore content.

* **Point In Time (PIT):** This type restores from system backups from the last 24 hours from the current time.
* **Last week:** This type restores from system backups in the last seven days excluding the previous 24 hours.

In both cases, the version of your custom code and AEM version remain unchanged.

>[!TIP]
>
>It is also possible to restore backups [using the public API.](https://developer.adobe.com/experience-cloud/cloud-manager/reference/api/)

## Limitations {#limitations}

Usage of the self-service restore mechanism is subject to the following limitations.

* Restore operations are limited to seven days, meaning it is not possible to restore a snapshot older than seven days.
* A maximum of ten successful restores are allowed across all environments in a program per calendar month.
* After environment creation, it takes six hours before the first backup snapshot is created. Until this snapshot is created, no restore can be performed on the environment.
* A restore operation will not initiate if there is a full stack or web tier config pipeline currently running for the environment.
* A restore can not be initiated if another restore is already running on the same environment.
* In rare cases, because of the 24 hour/seven day limit on backups, the selected backup may become unavailable due to a delay between when it was selected and when the restore is initiated.
* Data from deleted environments is permanently lost and cannot be recovered.

## Restoring Content {#restoring-content}

First determine the the time frame of the content that you wish to restore. Then to restore your environment's content from a backup perform these steps.

>[!NOTE]
>
>A user with the **Business Owner** or **Deployment Manager** role must be logged in, in order to initiate a restore operation.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click on the program for which you want to initiate a restore.

1. From the **Program Overview** page, in the **Environments** card, click on the ellipsis button next to the environment for which you want to initiate a restore and select **Restore Content**.

   ![Restore option](assets/backup-option.png)

   * Alternatively you can navigate directly to the **Restore Content** tab of the environment details page of a specific environment.

1. On the **Restore Content** tab of the environment details page, first select the time frame of the restore under the **Time to restore** dropdown.

   1. If you select **Last 24 hours** the neighboring **Time** field allows you to specify the exact time within the last 24 hours to restore.

      ![Last 24 hours](assets/backup-time.png)
   
   1. If you select **Last week** the neighboring **Day** field allows you to select a date within the past seven days, excluding the previous 24 hours.
   
      ![Last week](assets/backup-date.png)

1. Once you select a date or specify a time, the **Backups available** section below shows a list of available backups that can be restored

   ![Backups available](assets/backup-available.png)

1. Find the backup you wish to restore by using the information icon to view information regarding the version of the code and AEM release included in that backup and consider the implications of a restore when [choosing the backup.](#choosing-the-right-backup)

   ![Backup info](assets/backup-info.png)

   * Note that the time stamp displayed for the restore options are all based on the user's computer's time zone.

1. Click the **Restore** icon at the right end of the row representing the backup you wish to restore to start the restore process.

1. Review the details on the **Restore Content** dialog before confirming your request by clicking on **Restore**.

   ![Confirm restore](assets/backup-restore.png)

The backup process is initiated and you can view its status in the **[Restore Activity](#restore-activity)** table. The time required for a restore operation to complete depends on the size and profile of the content being restored.

When the restore successfully completes the environment will:

* Run the same code and AEM release as at the time of initiating the restore operation.
* Have the same content that was available at the timestamp of the chosen snapshot, with the indexes rebuilt to match the current code.

## Choosing the Right Backup {#choosing-backup}

Restores only restore content to AEM. For this reason, you must carefully consider code changes that were made between your desired restore point and the current time by reviewing the commit history between the your current commit ID and the one being restored to.

There are several scenarios.

* The custom code on the environment and the restore are on the same repository and same branch.
* The custom code on the environment and the restore are on the same repository but a different branch with a common commit.
* The custom code on the environment and the restore are on different repositories.
  * In this case, a commit ID will not be displayed.
  * It is strongly recommended that you clone both repositories and use a diff tool to compare the branches.

Additionally, keep in mind that a restore might cause your production and staging environments to fall out of sync. You are responsible for the consequences of restoring content.

## Restore Activity {#restore-activity}

The **Restore Activity** table shows the status of the ten most recent restore requests including any active restore operations.

![Restore activity](assets/backup-activity.png)

By clicking on the information icon for a backup you can download logs for that backup as well as inspect the code details including the differences between the snapshot and data at the moment the restore was initiated.

## Offsite Backup {#offsite-backup}

Regular backups cover the risk of accidental deletions or technical failures within AEM Cloud Services, but additional risks can arise from the failure of a region. In addition to availability, the greatest risk in such region outages is a loss of data.

AEM as a Cloud Service mitigates this risk for all AEM production environments by continuously copying all AEM content to a remote region and making it available for recovery for a period of three months. This capability is referred to as offsite backup.

The restoration of AEM Cloud Services for staging and production environments from offsite backup is carried out by AEM Service Reliability Engineering in the event of data region outages.
