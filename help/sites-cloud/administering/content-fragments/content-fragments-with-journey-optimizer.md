---
title: Using Content Fragments with Adobe Journey Optimizer
description: Learn how Content Fragments can be integrated and used with Adobe Journey Optimizer.
feature: Content Fragments
role: User, Developer
solution: Experience Manager Sites
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
exl-id: 4090ee41-80f1-4389-8961-e4af891f01ff
product_v2:
  - id: c45915cf-e157-4af7-a80d-97b905bcb3a5
    internal-label: Experience Manager Sites
feature_v2:
  - id: a642c50e-80eb-4fc1-a5d2-f3762d1f841d
    internal-label: Administration
subfeature_v2:
  - id: e9db7c79-8f65-4281-a439-c9049296d903
    internal-label: Content Fragments
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Content Fragments with Adobe Journey Optimizer {#content-fragments-with-journey-optimizer}

[Adobe Journey Optimizer](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/get-started/get-started) helps you deliver connected, contextual, and personalized experiences to your customers. By integrating Adobe Experience Manager (AEM) as a Cloud Service with Adobe Journey Optimizer (AJO), you can reuse AEM content in your AJO inbound channels, and your AJO outbound channels; including web, SMS, email, and others. 

For example, you can:

* seamlessly incorporate your [AEM Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md) into your [Journey Optimizer email](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/channels/email/email-landing-page) content
* preview the AJO experience directly from AEM

The connection between Content Fragments and AJO simplifies the process of accessing and leveraging AEM content, enabling the creation of personalized and dynamic campaigns and journeys.

For details start with the AJO documentation:

* [Using Content Fragments in AJO](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/content-management/combine/aem/aem-fragments)
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
