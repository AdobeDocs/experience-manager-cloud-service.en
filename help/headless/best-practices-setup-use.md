---
title: Best Practices for the setup and use of AEM GraphQL with Content Fragments
description: Learn the recommended Best Practices for the setup and use of AEM GraphQL with Content Fragments.
exl-id: 4d6a5aaa-c8be-4858-ad07-085dc4fb77e7
feature: Headless
role: "Admin, Developer"
---
# Best Practices for the setup and use of AEM GraphQL with Content Fragments{#best-practices-setup-use-aem-graphql-content-fragments}

These guidelines summarize the recommended best practices for setting up, configuring and using AEM with GraphQL and Content Fragments.

## Getting Started {#getting-started}

To help get you up to speed:

* [What is Headless?](/help/headless/what-is-headless.md)
* An overview of the various environments in the AEM [Architecture](/help/headless/deployment/architecture.md) 

## Setup {#setup}

To securely setup AEM GraphQL for use with Content Fragments and your apps you need to configure various components.

### GraphQL endpoint creation (including security) {#graphql-endpoint-creation}

The endpoint is the path used to access GraphQL for AEM. These endpoints need to be created, and published, so that they can be accessed securely.

#### Details {#details-graphql-endpoint-creation}

[Manage GraphQL endpoints in AEM ](/help/headless/graphql-api/graphql-endpoint.md)

#### Environments {#environments-graphql-endpoint-creation}

Endpoints need to be configured in:

* Author
* Preview
* Publish

For:

* Development
* Testing
* Production

### AEM Dispatcher caching {#dispatcher-caching}

>[!NOTE]
>If caching in the Dispatcher is enabled then the [CORS setup](#cors-setup) is not needed, and so can be ignored.

Caching of persisted queries is not enabled by default in the Dispatcher. Default enablement is not possible as customers using CORS (Cross-Origin Resource Sharing) with multiple origins need to review, and possibly update, their Dispatcher configuration.

#### Details {#details-dispatcher-caching}

[GraphQL Persisted Queries - enabling caching in the Dispatcher](/help/headless/deployment/dispatcher-caching.md)

#### Environments {#environments-dispatcher-caching}

The Dispatcher is usually configured for:

* Publish: production

### CORS setup {#cors-setup}

>[!NOTE]
>If caching in the [AEM Dispatcher](#dispatcher-caching) is enabled then the CORS setup is not needed, and so this section can be ignored.

To access the GraphQL endpoint, a CORS policy must be configured and added to an AEM Project that is deployed to AEM via Cloud Manager. This is done by adding an appropriate OSGi CORS configuration file for the desired endpoint(s). 

#### Details {#details-cors-setup}

[Cross-Origin Resource Sharing (CORS) configuration](/help/headless/deployment/cross-origin-resource-sharing.md)

#### Environments {#environments-cors-setup}

CORS is usually configured for:

* Publish: production

### Authentication {#authentication}

A primary use case for The Adobe Experience Manager as a Cloud Service (AEM) GraphQL API for Content Fragment Delivery is to accept remote queries from third-party applications or services. These remote queries may require authenticated API access to secure headless content delivery.

#### Details {#details-authentication}

[Authentication for Remote AEM GraphQL Queries on Content Fragments](/help/headless/security/authentication.md)

#### Environments {#environments-authentication}

Authentication is usually configured for:

* Preview
* Publish

For:

* Development
* Testing
* Production

### Permissions {#permissions}

With a headless implementation, there are several areas of security and permissions that should be addressed. Permissions and personas can broadly be considered based on the AEM environment **Author** or **Publish**. Each environment contains different personas and with different needs.

#### Details {#details-permissions}

[Permission considerations for headless content](/help/headless/security/permissions.md)

#### Environments {#environments-permissions}

Permissions are usually configured for:

* Author
* Preview
* Publish

For:

* Development
* Testing
* Production

### Use a Content Delivery Network (CDN) {#cdn}

GraphQL queries and their JSON responses can be cached if targeted as `GET` requests when using a CDN. In contrast, uncached requests can be very (resource) expensive and slow to process, with the potential for further detrimental effects on the origin's resources. 

#### Details {#details-cdn}

[CDN in AEM as a Cloud Service](/help/implementing/dispatcher/cdn.md)

#### Environments {#environments-cdn}

A CDN is usually configured for:

* Publish: production

### Configure and create Content Fragments {#cconfigure-create-content-fragments}

AEM GraphQL is used to retrieve information from your Content Fragments. These need to be configured, then a structure and location defined, before you can create the content. 

#### Details {#details-content-fragments}

* [Create a Configuration](/help/headless/setup/create-configuration.md)
* [Create a Content Fragment Model](/help/headless/setup/create-content-model.md)
* [Create an Assets Folder](/help/headless/setup/create-assets-folder.md)
* [Create, and edit, your Content Fragments](/help/headless/setup/create-content-fragment.md)

#### Environments {#eenvironments-content-fragments}

Content Fragments are defined, authored, tested, published, and accessed on:

* Author
* Preview
* Publish

For:

* Development
* Testing
* Production

## Using AEM GraphQL {#use-aem-graphql}

### Optimize your GraphQL queries {#optimize-graphql-queries}

These guidelines are provided to help prevent performance issues with your GraphQL queries.

#### Details {#details-optimize-graphql-queries}

[Optimizing GraphQL Queries](/help/headless/graphql-api/graphql-optimization.md)

>[!NOTE]
>
>The optimization guidelines cover cache configuration, already covered in [Setup](#setup).

### Access GraphQL from your apps {#access-graphql-from-your-apps}

AEM headless CMS gives developers the freedom to build and deliver exceptional experiences using the languages, frameworks, and tools they're already familiar with.

#### Details {#details-your-apps}

* [Install, and use, the AEM SDK for development](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/how-to/aem-headless-sdk.html)
* [AEM Headless Developer Resources](https://experienceleague.adobe.com/landing/experience-manager/headless/developer.html)
* Examples, including [React](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/how-to/example-apps/react-app.html), [Next.js](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/how-to/example-apps/next-js.html), [Node.js](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/how-to/example-apps/server-to-server-app.html), among others

#### Environments {#environments-your-apps}

Apps are usually developed, tested, and used on:

* Preview
* Publish

For:

* Development
* Testing
* Production

### Additional Resources

For more details about AEM GraphQL and Content Fragments, see the following:

* [AEM GraphQL API for use with Content Fragments](/help/headless/graphql-api/content-fragments.md)
* [Using the GraphiQL IDE](/help/headless/graphql-api/graphiql-ide.md)
* [AEM Headless Developer Resources](https://experienceleague.adobe.com/landing/experience-manager/headless/developer.html)
