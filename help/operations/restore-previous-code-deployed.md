---
title: Restore the Previous Source Code Deployed
description: Learn how to restore an environment to its last successful build &ndash; no pipeline run required.
feature: Operations
role: Admin
exl-id: 8f804f55-a66d-47ad-a48d-61b861cef4f7
---
# Restore the previous source code deployed in AEM as a Cloud Service {#restore-previous-code-deployed}

<!-- BETA BADGE REMOVED FOR NOVEMBER 2025 CM RELEASE badge: label="Beta" type="Positive" url="/help/implementing/cloud-manager/release-notes/current.md#gitlab-bitbucket"

>[!NOTE]
>
>The feature described in this article is only available through the beta program. To sign up for the beta, see [One-click rollback for pipeline deployments](/help/implementing/cloud-manager/release-notes/current.md##one-click-rollback). -->

Use **Restore previous code deployed** to roll an environment back instantly to its last successful build—no pipeline run required.

You simply open the selected environment's ![More icon or ellipsis menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) menu and choose **Restore** > **Previous code deployed** to roll back the most recently deployed source code in seconds.

See also [Restore Content in AEM as a Cloud Service](/help/operations/restore.md).

>[!TIP]
>
>You can view the active source-code version in use in the environment's details view, under the **General** tab. See [View details of an environment](/help/implementing/cloud-manager/manage-environments.md#viewing-environment).
>
>![Source code version in use](/help/operations/assets/environments-view-details-sourcecodeversion.png) 

**Restore previous code deployed** becomes available only when the following conditions are met:

* Only one restore is allowed per successful pipeline execution; to restore again, complete another successful pipeline run.
* You hold **Environment Restore Create** permissions. For details on managing permissions, see [Custom Permissions](/help/implementing/cloud-manager/custom-permissions.md).
* The feature flag guarding this feature is enabled (on).
* The program runs on AEM as a Cloud Service.
* The last pipeline for that environment finished successfully and ran **fewer than 30 days** ago.
* The environment status is *Running* and no pipeline is in progress.

**Restore previous code deployed** works in `Production` environment, in addition to `Development` environment, `Stage` environment, and `Specialized Testing Environment`. After you confirm, Cloud Manager starts the restore and sends a push notification at start and on successful completion. 

>[!IMPORTANT]
>
>For first-time use, Adobe highly recommends validating the procedure in `Stage` *before* using it in `Production` to reduce risk and ensure stability.


If any check fails, Cloud Manager opens the following dialog box that lists one or more unmet conditions and disables **Confirm**, preventing the restore.

![Restore previous code deployed failure dialog box](/help/operations/assets/restore-previous-code-deployment-not-allowed.png).

If you just want to restore data, which has been lost, damaged, or accidentally deleted, to its original condition, you can use [Restore Content in AEM as a Cloud Service](/help/operations/restore.md). This restore process only affects content, leaving your source code and version of AEM unchanged.

**To restore the previous code deployed:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click the program for which you want to initiate a restore.

1. List all environments for the program by doing one of the following:

   * From the left side menu, under **Services**, click ![Data icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Data_18_N.svg) **Environments**.

      ![Environments tab](assets/environments-1.png)

   * From the left side menu, under **Program**, click **Overview**, then from the **Environments** card, click ![Workflow icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Workflow_18_N.svg) **Show All**.

     ![Show all option](assets/environments-2.png)

      >[!NOTE]
      >
      >The **Environments** card lists three environments only. Click **Show All** in the card to see *all* environments of the program.

1. In the Environments table, to the right of an environment whose source code you want to restore, click ![More icon or ellipsis menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg), then click **Restore** > **Previous code deployed**.

   ![Restore previous code deployed option from the ellipsis menu](/help/operations/assets/restore-previous-code-deployed-menu.png)

1. In the **Restore previous code deployed** dialog box, review the currently deployed version and the version you want to restore, then click **Confirm**.

    ![Restore previous code deployed dialog box](/help/operations/assets/restore-previous-code-deployed-dialogbox.png) 

1. Cloud Manager rolls the environment back to the earlier build, keeps content and configuration intact, and marks the environment **Restoring** on the Environments page until deployment completes.

    ![Restoring activation](/help/operations/assets/restore-previous-code-deployed-restoring.png)

1. Near the upper-right corner of page, click ![Bell icon or Notifications icon ](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Bell_18_N.svg) **Notifications** to find out when your restore starts and ends.

    ![Restore previous code notifications when starting restore and when restore is completed](/help/operations/assets/restore-previous-code-notifications.png) 
    *Notifications for a restore previous code job.*
