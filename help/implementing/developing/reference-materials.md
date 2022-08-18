---
title: API Reference Materials
description: AEM has extensive and powerful APIs that you can leverage for your digital experience project.
exl-id: d4ef3040-5a0a-4149-9e99-09eda9605038
---
# API Reference Materials {#api-reference-materials}

Adobe Experience Manager (AEM) provides many APIs for developing applications and extending AEM. AEM is built on top of a number of open-source technologies, which can also be leveraged.

## AEM Core APIs {#core-aem-apis}

The following APIs are core to AEM.

|API|Description|
|---|---|
|[Adobe Experience Manager as a Cloud Service](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/index.html)|Product abstractions such as pages, assets, workflows, etc.|
|[Granite UI](https://helpx.adobe.com/experience-manager/6-5/sites/developing/using/reference-materials/granite-ui/api/jcr_root/libs/granite/ui/index.html#)|Adobe’s Open Web stack, providing various essential components (Note that the 6.5 Granite materials apply to AEMaaCS)|
|[Coral UI](https://opensource.adobe.com/coral-spectrum/documentation/)|Adobe’s visual style for cloud UIs, designed to provide consistency in the user experience|

<!---
|Editor core JavaScript API reference|Provides all the base objects and concepts to support authoring of content resources|
--->

## Additional Frameworks {#additional-apis}

AEM relies on a number of additional open-source APIs.

|API|Description|
|---|---|
|[Apache Sling](https://sling.apache.org/apidocs/sling11/)|Web framework that uses a Java Content Repository (JCR) to store and manage content|
|[Apache Jackrabbit Oak](http://jackrabbit.apache.org/oak/docs/oak_api/overview.html)|Implementation a scalable and high-performance hierarchical Java Content Repository (JCR) for use as the foundation of modern world-class web sites|
|[Java Content Repository](https://www.adobe.io/experience-manager/reference-materials/spec/javax.jcr/javadocs/jcr-2.0/index.html)|Specification for the JCR Version 2.0|
|[Apache Felix](https://felix.apache.org)|Implementation of the Open Services Gateway initiative (OSGi) framework and service platform|

## API Preference Guidelines {#guidelines}

AEM is built on the following four primary Java API sets in descending order of preference.

|Priority|API|Description|
|---|---|---|
|1|[Adobe Experience Manager as a Cloud Service](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/index.html)|Product abstractions such as pages, assets, workflows, etc.|
|2|[Apache Sling](https://sling.apache.org/apidocs/sling11/)|REST and resource-based abstractions such as resources, value maps, and HTTP requests.|
|3|[Apache Jackrabbit Oak](http://jackrabbit.apache.org/oak/docs/oak_api/overview.html)|Data and content abstractions such as node, properties and sessions.|
|4|[Apache Felix](https://felix.apache.org/)|OSGi application container abstractions such as services and (OSGi) components.|

If an API is provided by AEM, prefer it over Sling, JCR, and OSGi. If AEM doesn’t provide an API, then prefer Sling over JCR and OSGi.

>[!TIP]
>
>For details of these guidelines, see the document [Understand Java API Best Practices.](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/development/understand-java-api-best-practices.html)

## AEM Delivery and Content Management Services and APIs {#delivery-apis}

AEM offers customizable components and content delivery options.

|Feature|Description|
|---|---|
|[The Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html)|Standardized Web Content Management (WCM) components for AEM to speed up development time and reduce maintenance cost of your websites|
|[JSON Exporter](/help/implementing/developing/components/json-exporter.md)|Deliver the contents of any AEM page in JSON data model format|
|[Enabling JSON Export for a Component](/help/implementing/developing/components/enabling-json-exporter.md)|Generate JSON export of component content based on a modeler framework|
|[Assets API](/help/assets/mac-api-assets.md)|Allows for create-read-update-delete (CRUD) operations on assets, including binary, metadata, renditions, and comments. See AEM Assets HTTP API|
|[Content Fragments HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)|Access Content Fragment content directly over the HTTP API via CRUD operations|
|[Content Fragment GraphQL API](/help/headless/graphql-api/content-fragments.md)|Enable the efficient delivery of Content Fragments to JavaScript clients in headless CMS implementations|
|[Content Fragments Assets HTTP API](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/admin/mac-api-assets.html)|Eexact format of supported HTTP asset requests|

## SPA-Specific APIs {#spa-apis}

AEM Single-Page Application (SPA) Editor SDK framework provides specific JavaScript API references.

|API|Description|
|---|---|
|[Component Mapping](https://www.npmjs.com/package/@adobe/aem-spa-component-mapping)|Provides a way for the Single Page Application to map front-end components to Adobe Experience Manager resource types (AEM Components)|
|[Page Model Manager](https://www.npmjs.com/package/@adobe/aem-spa-page-model-manager)|An interpreter between Adobe Experience Manager Editor and the Adobe Experience Manager Single Page Application (SPA) Editor|
|[React Editable Components](https://www.npmjs.com/package/@adobe/aem-react-editable-components)|Provides the React components and integration layer to get you started with the Adobe Experience Manager Site Editor|
|[Angular Editable Components](https://www.npmjs.com/package/@adobe/aem-angular-editable-components)|Provides the Angular components and integration layer to get you started with the Adobe Experience Manager Site Editor|

>[!TIP]
>
>Check out the [SPA Introduction and Walkthrough](/help/implementing/developing/hybrid/introduction.md) for more information on single-page applications.
