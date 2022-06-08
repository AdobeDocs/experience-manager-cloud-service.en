---
title: Prerequisites for Content Transfer Tool
description: Prerequisites for Content Transfer Tool
exl-id: 41a9cff1-4d89-480c-b9fc-5e8efc2a0705
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
|AEM Version|Content Transfer Tool can be run on AEM 6.3 or higher versions only.|
|Size of Segment Store|An existing repository that has less than 55 million JCR nodes and up to 83 GB (online compacted size) on *Author* and 50 GB on *Publish* are currently supported. Create a support ticket with Adobe Customer Care to discuss options for segment store size above these limits.|
|Total Size of Content Repository <br>*(segment store + data store)*|Content Transfer Tool is designed to transfer content up to 20 TB for File Data Store type of data store. Anything higher than 20 TB is not currently supported. Create a support ticket with Adobe Customer Care to discuss options for content larger than 20 TB. <br>To significantly speed up the content transfer process for large repositories, an optional [pre-copy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/handling-large-content-repositories.html?lang=en#setting-up-pre-copy-step) step can be used. This applies to File Data Store, Amazon S3 and Azure Data Store types of data store. For Amazon S3 and Azure Data Store, repository sizes greater than 20TB is supported.|
|Total Lucene Index Size|Total Lucene Index size of 25GB maximum, excluding `/oak:index/lucene` and `/oak:index/damAssetLucene` is currently supported. Create a support ticket with Adobe Customer Care to discuss options for index size above this limit.|
|Node Name Length|Length of a node name must be 150 bytes or less when the node parent path is >= (equal or larger than) 350 bytes. These node names must be shortened to be <= 150 bytes in order to be supported by the Document node store in AEM as a Cloud Service. Ingestions will fail if these long node names are not fixed.|
|Content in Immutable Paths|Content Transfer Tool cannot be used to migrate content in immutable paths. To transfer content from `/etc` only certain `/etc` paths are allowed to be selected but only to support [AEM Forms to AEM Forms as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-forms-cloud-service/forms/migrate-to-forms-as-a-cloud-service.html?lang=en#paths-of-various-aem-forms-specific-assets). For all other use-cases, refer to [Common Repository Restructuring](https://experienceleague.adobe.com/docs/experience-manager-64/deploying/restructuring/all-repository-restructuring-in-aem-6-4.html?lang=en#restructuring) to learn more about repository restructuring.|
|Node property value in MongoDB| Node property values stored in MongoDB cannot exceed 16MB. This is enforced by MongoDB. Ingestions will fail if there are property values larger than this limit. Before running an extraction, run this [oak-run](https://repo1.maven.org/maven2/org/apache/jackrabbit/oak-run/1.38.0/oak-run-1.38.0.jar) script. Review all large property values and validate if they are needed. The ones that exceed 16MB will need to be converted to Binary values.|

## What's Next {#whats-next}

Once you have reviewed the prerequisites and have determined whether you can use the Content Transfer Tool in your migration project, refer to [Guidelines and Best Practices for using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html?lang=en).
