---
title: Viewing Logs for a Migration Set in Content Transfer Tool (Legacy)
description: Viewing Logs for a Migration Set in Content Transfer Tool
hide: yes
hidefromtoc: yes
exl-id: 01c8afd3-c594-4a41-b905-8c3a2d74db6f
---
# Viewing Logs for a Migration Set (Legacy) {#view-logs-content-transfer-tool}

Upon completion of each step (extraction and ingestion) check the logs and look for errors.  Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe support.

## Steps for Viewing Logs {#viewing-logs}

You can view logs for an existing migration set from the *Overview* page.
Follow the steps below:

1. Navigate to the *Overview* page and select the migration set that you want to delete and click **View Log** from the action bar.

   ![image](/help/journey-migration/content-transfer-tool/assets/view-log1.png)

1. The **Logs** dialog box displays. Click **Extraction Logs** to view the logs in a new tab.

   ![image](/help/journey-migration/content-transfer-tool/assets/view-log2.png)
Or,

   You can also view logs for your migration set from the *Overview* screen. Select the migration set and click the status under **EXTRACTION** field. In this case, click  **FINISHED** to view logs in a new tab.

   ![image](/help/journey-migration/content-transfer-tool/assets/view-log3.png)

1. To tail the logs without using the user interface, you can SSH into your source AEM environment and tail the `crx-quickstart/cloud-migration/extraction-XXXXX/output.log file`.
