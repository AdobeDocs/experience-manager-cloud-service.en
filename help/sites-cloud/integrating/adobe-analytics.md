---
title: Integrating with Adobe Analytics
seo-title: Integrating with Adobe Analytics
description: Integrating with Adobe Analytics 
seo-description: Integrating with Adobe Analytics 
---

# Integrating with Adobe Analytics{#integrating-with-adobe-analytics}

Integrating Adobe Analytics and AEM as a Cloud Service allows you to track your web page activity:

* An Adobe Analytics configuration enables AEM to authenticate with Adobe Analytics.
* A framework identifies the data that is sent to your Adobe Analytics report suite.

The data includes page and user data, for example:

* data that AEM components collect
* link clicks
* video usage information
* the number of page visits from Adobe Analytics

The pages listed below can help you configure the integration. To be noted that Launch by Adobe is the defacto tool for instrumenting an AEM site with Analytics capabilities (JS libraries). Therefore, integrating AEM as a Cloud Service with Launch and Adobe Analytics goes hand-in-hand.

* [Integrate Launch by Adobe](https://docs.adobe.com/content/help/en/experience-manager-learn/sites/integrations/adobe-launch-integration-tutorial-understand.html)
* [Integrate AEM with Adobe Launch Via Adobe I/O](https://helpx.adobe.com/experience-manager/using/aem_launch_adobeio_integration.html)
* [Understanding AEM Integration with Launch By Adobe, Analytics and Target](https://helpx.adobe.com/experience-manager/kt/integration/using/aem-launch-integration-tutorial-understand.html)
* [Configuring Link Tracking for Adobe Analytics](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-link.html)
* [Mapping Component Data with Adobe Analytics Properties](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-mapping.html)
* [Configuring Video Tracking for Adobe Analytics](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-video.html)
* [Adobe Classifications](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-classifications.html)



>[!NOTE]
>
>The IMS configuration (technical accounts) for Launch by Adobe is preconfigured in AEM as a Cloud Service. Users do not have to create this configuration.

## Further Information {#further-information}

See:

* [Extending the Adobe Analytics Integration](https://docs.adobe.com/content/help/en/experience-manager-65/developing/extending-aem/extending-analytics/extending-analytics.html) for information about developing components that collect user data and customizing the Adobe Analytics framework.
* The knowledge base article, [Adobe Analytics integration - troubleshooting issues](https://helpx.adobe.com/experience-manager/kb/sitecatalystintegrationtroubleshooting.html), for information about troubleshooting your Adobe Analytics integration.


>[!NOTE]
>
>If you are using Adobe Analytics with a custom proxy configuration, you need to [configure two OSGi bundles](https://docs.adobe.com/content/help/en/experience-manager-65/deploying/configuring/configuring-osgi.html) (for example, with the Web console) required for the **Apache HTTP Client** proxy configurations. Both are required as some functionalities of AEM use the 3.x APIs, while others use the 4.x APIs. Configure:
>
>* **Day Commons HTTP Client 3.1** to configure the 3.x API;
>  for example, [https://localhost:4502/system/console/configMgr/com.day.commons.httpclient](https://localhost:4502/system/console/configMgr/com.day.commons.httpclient)
>
>* **Apache HTTP Components Proxy Configuration** to configure the 4.x API;
>  for example, [https://localhost:4502/system/console/configMgr/org.apache.http.proxyconfigurator](https://localhost:4502/system/console/configMgr/org.apache.http.proxyconfigurator)
>

