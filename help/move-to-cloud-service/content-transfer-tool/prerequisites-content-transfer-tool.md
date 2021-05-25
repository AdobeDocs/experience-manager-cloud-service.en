---
title: Prerequisites for Content Transfer Tool
description: Prerequisites for Content Transfer Tool
---
# Prerequisites for Content Transfer Tool {#prerequisites}

The following table summarizes the prerequisites before using Content Transfer Tool. Please review all the considerations listed below:

|Considerations|What is Currently Supported|
|--- |--- |
|AEM Version|Content Transfer Tool can be run on AEM 6.3 or higher versions only. To be able to use Content Transfer Tool with AEM 6.2 or older versions, an in-place upgrade of the content repository to AEM 6.5 is required. It is not required to upgrade the code to AEM 6.5 for this.|
|Size of Segment Store|Content Transfer Tool currently supports up to 83 GB on *Author* and 31 GB on *Publish*.|
|Total Size of Content Repository (content store + data store)|Content Transfer Tool is designed to transfer content up to 10 TB. Anything higher than 10 TB is not currently supported. Create a support ticket with Adobe Customer Care to discuss options for content larger than 10 TB.|
|Content in Immutable Paths|Content Transfer Tool does not work for migrating the content in immutable paths such as `“/etc”`. Refer to [Common Repository Restructuring](https://experienceleague.adobe.com/docs/experience-manager-64/deploying/restructuring/all-repository-restructuring-in-aem-6-4.html?lang=en#restructuring) to learn more about repository restructuring and workflow models.| 