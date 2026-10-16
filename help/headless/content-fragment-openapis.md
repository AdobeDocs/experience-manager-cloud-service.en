---
title: Content Fragments and Content Fragment Models OpenAPIs
description: Learn about the Content Fragments and Content Fragment Models OpenAPIs.
exl-id: 077eed73-a066-4273-b2f5-da4bf5cd900c
feature: Headless, Content Fragments,GraphQL API
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: bfd4bc52-c397-5127-8f86-8953ba9fc0a3
    internal-label: Headless
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Content Fragments and Content Fragment Models Management OpenAPIs {#content-fragments-and-content-fragment-models-management-openapis}

The modernized OpenAPI implementation of the Content Fragment Management API allows developers to programmatically perform Create, Read, Update, and Delete operations on AEM Author to manage Content Fragment Models and Content Fragments that are stored in AEM. These APIs support a number of use-cases.

For full documentation see [Content Fragment Management API](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/sites/).

>[!NOTE]
>
>The existing usage of [Assets HTTP API](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/assets/admin/mac-api-assets) for Content Fragments should be migrated to the new Content Fragment Management OpenAPI. 

>[!NOTE]
>
>Authorization is required to access the OpenAPI when you are not logged into AEM; for example when the OpenAPI is used from another product as part of an integration. 
>
>See [OpenAPI-Based APIs](/help/implementing/developing/open-api-based-apis.md) for details of authorizing your access to the OpenAPI.

>[!CAUTION]
>
>By default the Content Fragment Management OpenAPI is disabled on publish. Instead of this, for delivery-oriented use-cases, we recommend using the [Content Fragment Delivery OpenAPI](/help/headless/aem-content-fragment-delivery-with-openapi.md).

>[!NOTE]
>
>See [AEM APIs for Structured Content Delivery and Management](/help/headless/apis-headless-and-content-fragments.md) for an overview of the various APIs available and comparison of some of the concepts involved.