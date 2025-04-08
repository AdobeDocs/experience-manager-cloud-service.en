---
title: Viewing Logs for a Migration Set in Content Transfer Tool
description: Viewing Logs for a Migration Set in Content Transfer Tool
exl-id: aed1ac83-a2fb-425e-aca4-39cd0bb42fd3
feature: Migration
role: Admin
---
# Viewing Logs for a Migration Set {#view-logs-content-transfer-tool}


>[!CONTEXTUALHELP]
>id="aemcloud_ctt_logs"
>title="Viewing Logs"
>abstract="Upon completion of Extraction of Ingestion, Check the logs for any error/warnings. Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe support."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html#troubleshooting" text="Troubleshooting"
>additional-url="https://helpx.adobe.com/ca/enterprise/using/support-for-experience-cloud.html" text="Contacting Adobe Support"

Upon completion of each step (extraction and ingestion) check the logs and look for errors.  Any errors should be addressed immediately either by dealing with the issues reported or by contacting Adobe support.

## Steps for Viewing Logs {#viewing-logs}

### Extraction Logs

To view the Extraction Logs, go to your source Adobe Experience Manager instance, then select the desired migration set. 

Then, follow the steps below:

1. Select a migration set and click **View Log** from the action bar. This will bring up the Logs dialog. Click **Extraction log** to view the logs in a new tab.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/logs.png) \
Or, click the **FINISHED** status to view logs in a new tab.

1. To tail the logs without using the user interface, you can SSH into your source AEM environment and tail the `crx-quickstart/cloud-migration/extraction-XXXXX/output.log file`.

### Ingestion Logs

To view Ingestion logs, go to the Ingestion Jobs list in Cloud Acceleration Manager, then find the desired migration job and click the three dots (**...**) of the job. You can then click **Download log** to download logs.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam28.png)
