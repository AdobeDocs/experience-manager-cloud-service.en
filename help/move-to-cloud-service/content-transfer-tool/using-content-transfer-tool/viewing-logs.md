---
title: Viewing Logs for a Migration Set in Content Transfer Tool
description: Viewing Logs for a Migration Set in Content Transfer Tool
---

# Viewing Logs for a Migration Set {#view-logs-content-transfer-tool}


>[!CONTEXTUALHELP]
>id="aemcloud_ctt_logs"
>title="Viewing Logs"
>abstract="Upon completion of Extraction of Ingestion, Check the logs for any error/warnings. Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe support."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#troubleshooting" text="Troubleshooting"
>additional-url="https://helpx.adobe.com/ca/enterprise/admin-guide.html/ca/enterprise/using/support-for-experience-cloud.ug.html" text="Contacting Adobe Support"

Upon completion of each step (extraction and ingestion) check the logs and look for errors.  Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe support.

## Steps for Viewing Logs {#viewing-logs}

You can view logs for an existing migration set from the *Overview* page.
Follow the steps below:

1. Navigate to the *Overview* page and select the migration set that you want to delete and click **View Log** from the action bar.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/view-log1.png)

1. The **Logs** dialog box displays. Click **Extraction Logs** to view the logs in a new tab.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/view-log2.png)
Or,

   You can also view logs for your migration set from the *Overview* screen. Select the migration set and click the status under **EXTRACTION** field. In this case, click  **FINISHED** to view logs in a new tab.

   ![image](/help/move-to-cloud-service/content-transfer-tool/assets/view-log3.png)

1. To tail the logs without using the user interface, you can SSH into your source AEM environment and tail the `crx-quickstart/cloud-migration/extraction-XXXXX/output.log file`.
