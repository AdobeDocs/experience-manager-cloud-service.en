---
title: Integrating with Adobe Target
description: Integrating with Adobe Target
exl-id: 2b4cf35e-2b75-4303-8d09-f6644ad99274
---
# Integrating with Adobe Target{#integrating-with-adobe-target}

As part of the Adobe Marketing Cloud, [Adobe Target](http://www.adobe.com/solutions/testing-targeting/testandtarget.html) lets you increase content relevance through targeting and measuring across all channels. Adobe Target is used by marketers to design and execute online tests, create on-the-fly audience segments (based on behavior) and automate the targeting of content and online experiences. AEM as a Cloud Service has adopted the targeting workflow that is used in Adobe Target Standard. If you use Target, you will be familiar with the targeting editing environment in AEM as a Cloud Service.

Integrate your AEM sites with Adobe Target to personalize content in your pages:

* Implement content targeting.
* Use Target audiences to create personalized experiences.
* Submit context data to Target when visitors interact with your pages.
* Track conversion rates.

>[!NOTE]
>
>Adobe Experience Manager as a Cloud Service customers who do not have an existing Target account, can request access to the Target Foundation Pack for Experience Cloud.  The Foundation Pack provides volume limited use of Target.


To integrate with Target, perform the following tasks:

* [Perform prerequisite tasks](https://experienceleague.adobe.com/docs/experience-manager-65/administering/integration/target-requirements.html): Register with Adobe Target and configure certain aspects of the AEM author instance. Your Adobe Target account must have **approver** level permissions at a minimum. In addition, you must secure the activity settings on the publish node so that it is inaccessible to users.

* Launch by Adobe is the defacto tool for instrumenting an AEM site with Target capabilities (JS libraries). Therefore, integrating AEM as a Cloud Service with Launch and Adobe Target goes hand-in-hand (see the links below).
   
  * [Integration with Adobe Target using Adobe I/O](https://experienceleague.adobe.com/docs/experience-manager-65/administering/integration/integration-ims-adobe-io.html)
  * [Integrate Launch by Adobe](https://experienceleague.adobe.com/docs/experience-manager-learn/sites/integrations/adobe-launch-integration-tutorial-understand.html)
  * [Integrate AEM with Adobe Launch Via Adobe I/O](https://helpx.adobe.com/experience-manager/using/aem_launch_adobeio_integration.html)
  * [Understanding AEM Integration with Launch By Adobe, Analytics and Target](https://helpx.adobe.com/experience-manager/kt/integration/using/aem-launch-integration-tutorial-understand.html)

>[!NOTE]
>
>The IMS configuration (technical accounts) for Launch by Adobe is preconfigured in AEM as a Cloud Service. Users do not have to create this configuration.

1. [Configure Activities](https://experienceleague.adobe.com/docs/experience-manager-65/authoring/personalization/activitylib.html): Associate your Activities with the Target cloud configuration.

>[!CAUTION]
>
>In AEM as a Cloud Service, the replication agent that synchronizes Offers and Activities from AEM to Adobe Target is disabled by default. Please contact the [Adobe Support](https://helpx.adobe.com/contact/enterprise-support.ec.html#experience-manager) team if you need to re-enable the replication agent.

>[!NOTE]
>
>If you are using Target with a custom proxy configuration, you need to configure both HTTP Client proxy configurations as some functionalities of AEM are using the 3.x APIs and some others the 4.x APIs:
>
>* 3.x is configured with [http://localhost:4502/system/console/configMgr/com.day.commons.httpclient](http://localhost:4502/system/console/configMgr/com.day.commons.httpclient)
>* 4.x is configured with [http://localhost:4502/system/console/configMgr/org.apache.http.proxyconfigurator](http://localhost:4502/system/console/configMgr/org.apache.http.proxyconfigurator)
>

>[!CAUTION]
>
>You must secure the activity settings node **cq:ActivitySettings** on the publish instance so that it is inaccessible to normal users. The activity settings node should only be accessible to the service handling the activity synchronization to Adobe Target.
>
>See [Prerequisites for Integrating with Adobe Target](https://experienceleague.adobe.com/docs/experience-manager-65/administering/integration/target-requirements.html#securing-the-activity-settings-node) for detailed information.

When the integration is complete, you can [author targeted content](https://experienceleague.adobe.com/docs/experience-manager-65/authoring/personalization/content-targeting-touch.html) that sends visitor data to Adobe Target. Note that page components require specific code to enable content targeting. (See [Developing for Targeted Content](https://experienceleague.adobe.com/docs/experience-manager-65/developing/personlization/target.html).

>[!NOTE]
>
>When you target a component in AEM author, the component makes a series of server-side calls to Adobe Target to register the campaign, set up offers, and retrieve Adobe Target segments (if configured). No server-side calls are made from AEM publish to Adobe Target.

## Background Information Sources {#background-information-sources}

Integrating AEM as a Cloud Service with Adobe Target requires knowledge of Adobe Target, AEM Activities management, and AEM Audiences management. You should be familiar with the following information:

* Adobe Target (See the [Adobe Target documentation](https://experienceleague.adobe.com/docs/target/using/target-home.html)).
* AEM Activities console (See [Managing Activities](https://experienceleague.adobe.com/docs/experience-manager-65/authoring/personalization/activitylib.html).
* AEM Audiences (See [Managing Audiences](https://experienceleague.adobe.com/docs/experience-manager-65/authoring/personalization/managing-audiences.html).

>[!NOTE]
>
>When working with Adobe Target, the following is the maximum number of artifacts allowed within a campaign:
>
>* 50 locations
>* 2,000 experiences
>* 50 metrics
>* 50 reporting segments
>
