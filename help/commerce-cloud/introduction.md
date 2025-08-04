---
title: Introduction and overview
description: Overview of the different storefront options
thumbnail: introducing-aem-commerce.jpg
exl-id: 29410f76-a63f-4b0a-b817-2ed724ad1a3c
feature: Commerce Integration Framework
role: Admin
---

# Content and Commerce {#content-commerce}

As customer expectations for intent-based and high-performing commerce experiences grow, brands are under pressure to deliver more content, more quickly—without sacrificing quality. With Adobe Experience Manager, brands can scale and innovate faster to create immersive commerce experiences and capture more traffic and growing online spend. 

Adobe Experience Manager offers powerful tools to create and manage content-rich, personalized customer experiences. By integrating AEM with a commerce solution—such as Adobe Commerce, Salesforce Commerce, SAP Commerce Cloud, or any other solution - brands can unify content and commerce to deliver seamless shopping journeys across channels.

## Overview storefront approaches
There are different ways how AEM can support you based on your situation and preferences. Use the following guidance to pick the right approach for you:
 
### Use Edge Delivery Services (Recommended)
If your business wants the fastest and AI-friendliest storefront on the web and your developers a state-of-the-art developer experience, use [Edge Delivery Services](../edge/overview.md) that meets all of today's and tomorrow's requirements. Depending on our backend and solution, you have different options:

**1. Integration with Adobe Commerce as a Cloud Service**
Perfect, you are case Edge Delivery and the [Adobe Commerce Storefront](https://experienceleague.adobe.com/developer/commerce/storefront/) as your starting point. The storefront comes with a boilerplate that is pre-integrated with Adobe Commerce services, APIs, and offers a variety of Commerce drop-in components to rapidly build a storefront.

Good fit: Typical storefront experience with Adobe Commerce as a Cloud Service

**2. Integration with Adobe Commerce Optimizer (for any 3rd party solution)**
If you want to integrate your existing commerce solution and boost your catalog performance, our recommendation is to use [Adobe Commerce Optimizer](https://experienceleague.adobe.com/en/docs/commerce-learn/tutorials/adobe-commerce-optimizer/overview) as the modern integration layer. Commerce Optimizer enhances your commerce solution with high-performance SaaS services for catalog and merchandizing. As with Adobe Commerce as a Cloud Service, [Adobe Commerce Storefront](https://experienceleague.adobe.com/developer/commerce/storefront/) works out-of-the-box with it.

Integrations to commercial commerce solutions such as Salesforce Commerce are avaialble. Please talk to your Adobe rep.

Good fit: Typical storefront experience with an existing commerce solution 

**3. Custom integration**
We also recommend using Edge Delivery Services if you want to build a custom integration. You can either start from scratch or re-use existing JS-framework commerce components (e.g. for the transactional part) in your Edge Delivery storefront. That way, your customers will get a blazing-fast shopping experience which is agentic-friendly, while you can re-use your existing investments to increase TTV. Your starting point is the default [Edge Delivery Boilerplate](https://www.aem.live/developer/tutorial).

Good fit: Low value from the Edge Deliery storefront.

### Use your own storefront (Headless AEM integration)
You have an existing storefront (e.g. built with React JS) and want to use Adobe Experience Manager for manage & delivery content (Content Fragments), assets, plus in-context editing (Universal Editor). Your starting point for an integration is [Introduction to Adobe Experience Manager as a Headless CMS](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/headless/introduction) and the [CIF add-on](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/content-and-commerce/storefront/authoring/enrich-product-associated-content). The CIF add-on allows a seamless integration of your product data into AEM (Search, browse, and find products within the AEM UI) that you can use to build commerce-specific experiences.

### AEM CIF storefront
Our recommendation and reference architecture is to use Edge Delivery Services. The CIF storefront with its AEM CIF Core Components are now in maintenance mode and should not be used in new projects anymore. For reference, the [CIF documentation](./cif-introduction.md).

>[!NOTE]
>Existing customers who want to leverage new AEM / Commerce functionality should move their website to Edge Delivery. A common pattern is to start by moving only a subset of pages to Edge Delivery and running Edge Deliery and CIF pages in a side-by-side fashion. It is also possible to replace AEM CIF components with the new [Commerce drop-in components](https://experienceleague.adobe.com/developer/commerce/storefront/dropins/all/introduction/) to leverage new Commerce capabilities.
