---
title: Using Content Fragments with Adobe Journey Optimizer
description: Learn how Content Fragments can be integrated and used with Adobe Journey Optimizer.
feature: Content Fragments
role: User, Developer, Architect
solution: Experience Manager Sites
exl-id: 4090ee41-80f1-4389-8961-e4af891f01ff
---
# Content Fragments with Adobe Journey Optimizer {#content-fragments-with-journey-optimizer}

[Adobe Journey Optimizer](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/get-started/get-started) helps you deliver connected, contextual, and personalized experiences to your customers. By integrating Adobe Experience Manager (AEM) as a Cloud Service with Adobe Journey Optimizer (AJO), you can reuse AEM content in your AJO inbound channels, and your AJO outbound channels; including web, SMS, email, and others. 

For example, you can:

* seamlessly incorporate your [AEM Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md) into your [Journey Optimizer email](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/email-landing-page) content
* preview the AJO experience directly from AEM

The connection between Content Fragments and AJO simplifies the process of accessing and leveraging AEM content, enabling the creation of personalized and dynamic campaigns and journeys.

For details start with the AJO documentation:

* [Using Content Fragments in AJO](https://experienceleague.adobe.com/docs/journey-optimizer/using/integrations/aem-fragments.html#integrations)
* [Integration AJO Offers with Content Fragment](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/decisioning/offer-decisioning/managing-offers-in-the-offer-library/configure-offers/add-representations#urls)

## Dispatcher Configuration {#dispatcher-configuration}

To allow AJO to access the AEM Content Fragments through the [Content Fragment Management API](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/), you need to configure the Dispatcher:

* In `dispatcher/src/conf.dispatcher.d/filters/filters.any`:

* Add:

  ```xml
  # Allow Content Fragments API requests, required for integration with AJO 
  /200 {/type "allow" /url "/adobe/sites/cf/*" }
  ```

## Further Information {#further-information}

For further information see:

* The [AJO External References extension](/help/sites-cloud/administering/content-fragments/extension-content-fragment-ajo-external-references.md) 
