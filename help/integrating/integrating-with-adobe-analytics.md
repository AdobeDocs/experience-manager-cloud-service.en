---
title: Integrating with Adobe Analytics
seo-title: Integrating with Adobe Analytics
description: Integrating with Adobe Analytics 
seo-description: Integrating with Adobe Analytics 
---

# Integrating with Adobe Analytics{#integrating-with-adobe-analytics}

Integrating Adobe Analytics and AEM allows you to track your web page activity:

* An Adobe Analytics configuration enables AEM to authenticate with Adobe Analytics.
* A framework identifies the data that is sent to your Adobe Analytics report suite.

The data includes page and user data; for example:

* data that AEM components collect
* link clicks
* video usage information
* the number of page visits from Adobe Analytics

The following pages help you configure the integration:

* [Connecting to Adobe Analytics and Creating Frameworks](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-connect.html)
* [Configuring Link Tracking for Adobe Analytics](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-link.html)
* [Mapping Component Data with Adobe Analytics Properties](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-mapping.html)
* [Configuring Video Tracking for Adobe Analytics](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-video.html)
* [Adobe Classifications](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/adobeanalytics-classifications.html)

You can also use the [Opt-in wizard](https://docs.adobe.com/content/help/en/experience-manager-65/administering/integration/opt-in.html) to easily perform the integration.

>[!NOTE]
>
>See also the how-to article: [Integrating AEM with Adobe Target and Adobe Analytics using DTM](https://helpx.adobe.com/experience-manager/using/integrate-digital-marketing-solutions.html).

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

