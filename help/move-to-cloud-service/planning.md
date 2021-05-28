---
title: Planning Phase
description: Planning Phase
exl-id: 987cb929-7871-4fec-8ef5-4d2f5f2f2186
---
# Planning {#planning-phase}

>[!CONTEXTUALHELP]
>id="aemcloud_cam_planning"
>title="Planning your Transition"
>abstract="Before beginning your transition journey to Cloud Service, you should familiarize yourself with AEM as a Cloud Service and review the notable changes that have been made to it and also review the features that have been replaced or deprecated."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html" text="Best Practices Analyzer"

Before beginning your transition journey to Cloud Service, you should familiarize yourself with AEM as a Cloud Service and review the notable changes that have been made to it and also review the features that have been replaced or deprecated.

## Notable Changes {#notable-changes}

AEM as a Cloud Service brings many new features and possibilities for managing your AEM projects.

However, there are a number of differences between AEM On-premise or in Adobe Managed Services as compared to AEM as a Cloud Service.

Refer to [Notable Changes to AEM Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/aem-cloud-changes.html) to understand the important differences.

## Deprecated Features {#deprecated-features}

Adobe constantly evaluates product capabilities, to over time reinvent or replace older features with more modern alternatives to improve overall customer value, always under careful consideration of backward compatibility. 

Refer to [Deprecated Features](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/deprecated-removed-features.html#deprecated-features) to learn more about features and capabilities that have been marked as deprecated in Experience Manager as a Cloud Service.

## Understanding the Planning Phase {#introduction}

The following figure showcases key steps involved during the Planning phase:

![image](/help/move-to-cloud-service/assets/planning-phaseimg1.png)

### Assessing Cloud Service Readiness {#access-cloud-readiness}

The first step in the Planning phase is to assess your readiness to move from your existing AEM version to Cloud Service and determine areas that will require refactoring to be compatible with AEM as a Cloud Service. 

You will need to do a comprehensive assessment of your current AEM source code against the notable changes and deprecated features to determine the level of effort expected in the transition journey.

You can accelerate the assessment step by running the Best Practices Analyzer on your current AEM version. For more details refer to [Best Practices Analyzer](/help/move-to-cloud-service/best-practices-analyzer/overview-best-practices-analyzer.md).

>[!NOTE]
>If you already have access to Cloud Manager and a Cloud Service environment, it is recommended to run your current code in a Cloud Manager code quality pipeline to assess the required code changes to be compatible with Cloud Service.

### Reviewing Resource Planning {#review-resource-planning}

Once you have estimated the level of effort that will be required to move to Cloud Service, you should identify resources, create a team, and map out roles and responsibilities for the transition process. 

### Establishing KPIs {#establish-kpis}

If you have not established Key Performance Indicators (KPIs) previously, it is recommended to establish KPIs for your Adobe Experience Manager (AEM) implementation to help your team focus on what matters the most. 

Refer to [Developing KPIs](https://guided.adobe.com/welcome/aem/part6.html) to learn how to choose the right KPIs for your business objectives.
