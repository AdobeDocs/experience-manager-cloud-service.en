---
title: Running the Content Transfer Tool on a Publish Instance (Legacy)
description: Running the Content Transfer Tool on a Publish Instance
hide: yes
hidefromtoc: yes
exl-id: 0a699dc1-9977-4cf9-a1b0-7b503ea2fc69
---
# Running the Content Transfer Tool on a Publish Instance (Legacy) {#run-content-transfer-tool-publish-instance}

## Introduction {#introduction}

The Content Transfer Tool (CTT) does not perform any kind of content analysis before transferring content from the source instance to the target instance. For example, CTT does not differentiate between published and unpublished content while ingesting content into a Publish environment. Whatever content is specified in the migration set will be ingested into the chosen target instance. User has the ability to ingest a migration set into an Author instance or Publish instance or both. 

>[!NOTE]
>It is recommended that while moving content to a Production instance, Content Transfer Tool be installed on the source Author instance to move content to the target Author instance and similarly, install Content Transfer Tool on the source Publish instance to move content to the target Publish instance. See [Recommended Approach](#recommended-approach) section below for more details.

## Recommended Approach {#recommended-approach}

Follow the recommended approach as described below:

* Use the same version of the Content Transfer Tool which was used on the Author instance.

* Only a single publish node needs to be migrated. It should be removed from the load balancer prior to beginning the extraction.

* When creating the migration set, use the URL of the author AEM as a Cloud Service environment.

* During ingestion to publish, the publish tier will not be scaled down (unlike the author). 

   >[!IMPORTANT]
   >As a precaution, please avoid any user initiated write operations, such as:
   > * Content distribution from AEM as a Cloud Service Author to Publish in that environment 
   > * User Sync between publish instances
