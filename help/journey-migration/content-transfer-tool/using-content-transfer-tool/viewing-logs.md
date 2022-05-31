---
title: Viewing Logs for a Migration Set in Content Transfer Tool
description: Viewing Logs for a Migration Set in Content Transfer Tool
exl-id: aed1ac83-a2fb-425e-aca4-39cd0bb42fd3
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

To view the Extraction Logs, go to your source Adobe Experience Manager instance, then select the desired migration set. 

Then, follow the steps below:

1. Select a migration set and click **View Log** from the action bar. This will bring up the Logs dialog. Click **Extraction log** to view the logs in a new tab.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam25.png) \
Or, click the **FINISHED** status to view logs in a new tab.

1. To tail the logs without using the user interface, you can SSH into your source AEM environment and tail the `crx-quickstart/cloud-migration/extraction-XXXXX/output.log file`.

1. To view Ingestion logs, go to the Ingestion Jobs list in Cloud Acceleration Manager and click on the three dots (**...**). You can then click on **View log**. This will open the logs in a separate tab. You can also download logs by click on **Download log**.

   ![image](/help/journey-migration/content-transfer-tool/assets-ctt/cttcam26.png)

>[!IMPORTANT]
>
>If you click on **View log** while an ingestion is running, the logs displayed in a separate tab do not get automatically refreshed or updated to display the latest. You will need to click on View log each time to view the most recent logs during an ongoing ingestion.
