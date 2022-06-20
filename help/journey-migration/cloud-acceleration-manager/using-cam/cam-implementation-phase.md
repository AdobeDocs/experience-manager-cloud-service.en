---
title: Implementation Phase in Cloud Acceleration Manager
description: This page provides an overview on the implementation phase in Cloud Acceleration Manager.
exl-id: e6ac88f0-4b3f-43a1-98bc-8c6608713784
---
# Implementation Phase in Cloud Acceleration Manager {#implementation-phase-cam}

The Implementation Phase includes:

* [Local Development](#local-development)
* [Code Refactoring](#code-refactoring)
* [AEM as a Cloud Service Deployment](#aem-as-a-cloud-service-deployment)
* [Content Transfer](#content-transfer)


Click on your project card to open the project landing page and navigate to the **Implementation** section, as shown in the figure below.

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/implementation-1.png)

   >[!NOTE]
   >Refer to [Creating and Managing a Project in Cloud Acceleration Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-acceleration-manager/using-cam/getting-started-cam.html?lang=en#create-project) to learn more.


## Using Local Development Card {#local-development}

The Local Development card provides all the relevant content that will help you setup your local AEM development environment as you start the Implementation phase of your migration journey.

Follow this section to explore the Local Development activity card:

1. Click on the **View** button from the **Local Development** card.

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/implementation-2.png)

1. A content carousel displays the relevant information for this phase of the migration journey.

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/implementation-3.png)


## Using Code Refactoring Card {#code-refactoring}

The Code Refactoring activity card provides all the relevant information and highlights the code refactoring areas you need to review and resolve when moving to AEM as a Cloud Service.

Follow this section to explore the Code Refactoring activity card:

1. Click on the **Review** button from the **Code Refactoring** activity card.

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/implementation-4.png)

1. The page displays the list of code refactoring activities organized by the severity level. You can learn more by clicking on the two highlighted icons. 

   The page displays the code refactoring considerations in three different tabs: 

   * Overview
   * Dispatcher
   * Testing

  >[!NOTE]
  >Please review the content in these tabs to understand some additional areas that are not covered by the Best Practices Analyzer.
   
   The **Dispatcher** tab provides information on how to structure the AEM as a Cloud Service Apache and Dispatcher configurations, as well as how to validate and run it locally before deploying to Cloud environments. It also describes debugging in Cloud environments.
   
   ![image](/help/journey-migration/cloud-acceleration-manager/assets/coderefactoring-2.png)

   The **Testing** tab provides information on functional, Experience Audit, and UI testing.
   
   ![image](/help/journey-migration/cloud-acceleration-manager/assets/coderefactoring-3.png)

   
## Using AEM as a Cloud Service Deployment Card {#aem-as-a-cloud-service-deployment}

AEM as a Cloud Service Deployment card provides all the relevant content that will help you deploy your code to AEM as a Cloud Service.

Follow this section to explore AEM as a Cloud Service Deployment Card activity card:

1. Click on the **View** button from the **AEM as a Cloud Service Deployment** activity card.

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/implementation-6.png)

1. A content carousel displays the relevant information for this phase of the migration journey.

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/aem-deployment-card.png)


## Using Content Transfer Card {#content-transfer}

The Content Transfer card allows you to start and manage content transfer from your current AEM instance to AEM as a Cloud Service. 

Follow this section to explore the Content Transfer activity card:

1. Click on the **Review** button from the **Content Transfer** activity card.

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/contenttransfer-1.png)

1. To start a content transfer you will need to create a Migration set. Click on **Create migration set**. A migration set allows content to be transferred to AEM as a Cloud Service. 

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/contenttransfer-2.png)

   >[!NOTE]
   >Please review the [prerequisites](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/prerequisites-content-transfer-tool.html?lang=en) and the [best practices and guidelines](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html?lang=en) before using the Content Transfer Tool.

1. You will need to download and install the Content Transfer Tool to populate the migration set and complete the Extraction phase of content transfer. Review [Getting Started with Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/getting-started-content-transfer-tool.html?lang=en) to learn how to use the Content Transfer Tool.

1. To ingest content from the Migration set into an environment on AEM as a Cloud Service, you will need to start an ingestion. Navigate to **Ingestion Jobs** and click on **New ingestion**. Review [Ingesting Content into Target](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/ingesting-content.html?lang=en) to learn how to complete the Ingestion phase of content transfer.

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/contenttransfer-3.png)

### Estimating Content Transfer Time {#calculating}

A Content Transfer Tool calculator has been provided to estimate how long it could take to complete the content transfer activity. You can use the content repository size slider to select the size that applies to your project. The transfer times vary for the extraction and ingestion phases. 

   ![image](/help/journey-migration/cloud-acceleration-manager/assets/contenttransfer-4.png)

   >[!NOTE]
   >These times are estimates only. Factor such as network speeds and time to scale up instances have not been accounted for in these estimates.

To estimate the size of the AEM Repository, you can run the Disk Usage report under `http://HOST:PORT/etc/reports/diskusage.html`. 

You can also estimate the size of specific repository paths by using the `path` parameter, for example, `http://HOST:PORT/etc/reports/diskusage.html?path=/content/dam`.

## What's Next {#whats-next}

Once you have learnt how to log into Cloud Acceleration Manager and how utilize the Implementation phase, you are now ready to move on to reviewing the next step in the [Go Live Phase](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-acceleration-manager/using-cam/cam-golive-phase.html?lang=en).
