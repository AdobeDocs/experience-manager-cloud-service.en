---
title: Prerequisites for Content Transfer Tool
description: Prerequisites for Content Transfer Tool
exl-id: ef6d0e1a-0ed2-4485-adab-df6e0cf3ac4d
---
# Prerequisites for Content Transfer Tool {#prerequisites}

>[!CONTEXTUALHELP]
>id="aemcloud_ctt_prereqs"
>title="Important Considerations for using Content Transfer Tool"
>abstract="Review important considerations to use the Content Transfer tool including Java and AEM verions, supported Datastore types, user groups considerations and more."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html?lang=en#pre-reqs" text="Important Considerations for Using Content Transfer Tool"
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html?lang=en#best-practices" text="Best Practices and Guidelines"

The following table summarizes the prerequisites for using Content Transfer Tool. 

Please review all the considerations listed below:

|Considerations|What is Currently Supported|
|--- |--- |
|AEM Version|Content Transfer Tool can be run on AEM 6.3 or higher versions only. To be able to use Content Transfer Tool with AEM 6.2 or older versions, an in-place upgrade of the content repository to AEM 6.5 is required. It is not required to upgrade the code to AEM 6.5 for this.|
|Size of Segment Store|An existing repository that has less than 55 million JCR nodes and up to 83 GB (online compacted size) on *Author* and 31 GB on *Publish* are currently supported. Create a support ticket with Adobe Customer Care to discuss options for segment store size above these limits.|
|Total Size of Content Repository <br>*(segment store + data store)*|Content Transfer Tool is designed to transfer content up to 10 TB for File Data Store type of data store. Anything higher than 10 TB is not currently supported. Create a support ticket with Adobe Customer Care to discuss options for content larger than 10 TB. <br>For Amazon S3 and Azure Data Store types of data store, an optional [pre-copy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en#setting-up-pre-copy-step) step can be used to significantly speed up the content transfer process and supports greater than 10TB size of data store.|
|Total Index Size|Total index size of 25GB maximum is currently supported. Create a support ticket with Adobe Customer Care to discuss options for index size above this limit.|
|Node Name Length|Length of a node name must be 150 bytes or less. Node names longer than 150 bytes must be shortened to be <= 150 bytes in order to be supported by the Document node store in AEM as a Cloud Service. Ingestions will fail if these long node names are not fixed.|
|Content in Immutable Paths|Content Transfer Tool cannot be used to migrate content in immutable paths. To transfer content from `/etc` only certain `/etc` paths are allowed to be selected but only to support [AEM Forms to AEM Forms as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/migrate-to-forms-as-a-cloud-service.html?lang=en#paths-of-various-aem-forms-specific-assets). For all other use-cases, refer to [Common Repository Restructuring](https://experienceleague.adobe.com/docs/experience-manager-64/deploying/restructuring/all-repository-restructuring-in-aem-6-4.html?lang=en#restructuring) to learn more about repository restructuring.| 

## What's Next {#whats-next}

Once you have reviewed the prerequisites and have determined whether you can use the Content Transfer Tool in your migration project, refer to [Additional best practices and considerations](/help/move-to-cloud-service/content-transfer-tool/using-content-transfer-tool.md) while using the Content Transfer Tool.
