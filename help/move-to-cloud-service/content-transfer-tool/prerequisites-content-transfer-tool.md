---
title: Prerequisites for Content Transfer Tool
description: Prerequisites for Content Transfer Tool
---
# Prerequisites for Content Transfer Tool {#prerequisites}

The following table summarizes the prerequisites for using Content Transfer Tool. 

Please review all the considerations listed below:

|Considerations|What is Currently Supported|
|--- |--- |
|AEM Version|Content Transfer Tool can be run on AEM 6.3 or higher versions only. To be able to use Content Transfer Tool with AEM 6.2 or older versions, an in-place upgrade of the content repository to AEM 6.5 is required. It is not required to upgrade the code to AEM 6.5 for this.|
|Size of Segment Store|Content Transfer Tool currently supports up to 83 GB on *Author* and 31 GB on *Publish*.|
|Total Size of Content Repository <br>*(segment store + data store)*|Content Transfer Tool is designed to transfer content up to 10 TB. Anything higher than 10 TB is not currently supported. Create a support ticket with Adobe Customer Care to discuss options for content larger than 10 TB.|
|Content in Immutable Paths|Content Transfer Tool cannot be used to migrate content in immutable paths such as `“/etc”`. There are certain `"/etc"` paths allowed to be selected but only to support [AEM Forms to AEM Forms as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/migrate-to-forms-as-a-cloud-service.html?lang=en#paths-of-various-aem-forms-specific-assets). For all other use-cases, refer to [Common Repository Restructuring](https://experienceleague.adobe.com/docs/experience-manager-64/deploying/restructuring/all-repository-restructuring-in-aem-6-4.html?lang=en#restructuring) to learn more about repository restructuring.| 

## What's Next {#whats-next}

Once you have reviewed the prerequisites and have determined whether you can use the Content Transfer Tool in your migration project, please refer to [Additional best practices and considerations](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md) while using the Content Transfer Tool.
