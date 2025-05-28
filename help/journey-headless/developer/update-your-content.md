---
title: How to Update Your Content via AEM APIs
description: In this part of the AEM Headless Developer Journey, learn how to use the available APIs to access and update the content of your Content Fragments.
exl-id: 84120856-fd1d-40f7-8df4-73d4cdfcc43b
solution: Experience Manager
feature: Headless, Content Fragments, GraphQL API
role: Admin, Architect, Developer
---
# How to Update Your Content via AEM APIs {#update-your-content}

In this part of the [AEM Headless Developer Journey](overview.md), learn how to use the available APIs to access and update the content of your Content Fragments.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless journey, [How to Access Your Content via AEM Delivery APIs](access-your-content.md) you learned how to access your headless content in AEM via the AEM GraphQL API and you should now:

* Have a high-level understanding of GraphQL.
* Understand how the AEM GraphQL API works.
* Understand some practical sample queries.

This article builds on those fundamentals so you understand how to update your existing headless content in AEM via the available APIs.

## Objective {#objective}

* **Audience**: Advanced
* **Objective**: Learn about the APIs available to access and update the content of your Content Fragments.

## AEM APIs for use with Content Fragments {#aem-apis-for-use-with-content-fragments}

Adobe Experience Manager (AEM) as a Cloud Service offers multiple APIs for both structured content delivery from Content Fragments and Content Fragment management. See the individual pages for further details of the specific APIs.

* AEM Content Fragment Delivery with OpenAPI
  * This API creates JSON responses for delivering structured content from Content Fragments in AEM. 
  * It uses a path to a content fragment as endpoint. 
  * This API is REST based.
  * It is optimized for content delivery, including CDN integration. 
* AEM GraphQL API for Content Fragment delivery
  * This API is schema-based. API schemas are represented by Content Fragment Models, which define the content structure.
  * This API is GraphQL based.
* Content Fragments and Content Fragment Models OpenAPIs
  * These APIs are intended for structured content management. 
  * Respective GET operators are not optimized for content delivery.
  * This API is REST based. 

>[!NOTE]
>
>[Content Fragment Support in Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md) is now [deprecated](/help/release-notes/deprecated-removed-features.md). It has been replaced by replaced by [Content Fragment Delivery with OpenAPI](/help/headless/aem-content-fragment-delivery-with-openapi.md) together with [Content Fragments and Content Fragment Models Management OpenAPIs](/help/headless/content-fragment-openapis.md).

## What's Next {#whats-next}

Now that you have completed this part of the AEM Headless Developer Journey, you should:

* Understand the AEM APIs available.
* Understand how Content Fragments are supported in these APIs.

You should continue your AEM headless journey by next reviewing the document [How to Put It All Together - Your App and Your Content in AEM Headless](put-it-all-together.md) where you will get familiar with the AEM architecture basics and tools you need to use to put your application together.

## Additional Resources {#additional-resources}

* [Adobe Experience Manager as a Cloud Service APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/)
* [AEM APIs for Structured Content Delivery and Management](/help/headless/apis-headless-and-content-fragments.md)
* [AEM Content Fragment Delivery with OpenAPI](/help/headless/aem-content-fragment-delivery-with-openapi.md)
* [AEM GraphQL API for Content Fragment delivery](/help/headless/graphql-api/content-fragments.md)
* [Content Fragments and Content Fragment Models OpenAPIs](/help/headless/content-fragment-openapis.md)
* [Content Fragments Support in the AEM Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)
* [Working with Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md)
* [AEM Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html)
* [CORS/AEM explained](https://helpx.adobe.com/experience-manager/kt/platform-repository/using/cors-security-article-understand.html)
* [Video - Developing for CORS with AEM](https://helpx.adobe.com/experience-manager/kt/platform-repository/using/cors-security-technical-video-develop.html)
* [Introduction to AEM as a Headless CMS](/help/headless/introduction.md)
* [AEM Developer Portal](https://experienceleague.adobe.com/landing/experience-manager/headless/developer.html)
* [Tutorials for Headless in AEM](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/overview.html) 
