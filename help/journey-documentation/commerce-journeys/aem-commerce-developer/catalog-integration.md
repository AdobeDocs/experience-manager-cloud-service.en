---
title: Integration of Product Catalog
description: Get to know how to integrate a product catalog.
index: no
hide: yes
hidefromtoc: yes
---
# Integration of Product Catalog {#product-catalog}

Get to know how to integrate a product catalog.

## The Story So Far {#story-so-far}

In the previous document of the AEM Content and Commerce developer journey, [Path to your first storefront](first-storefront.md), you learned how to have a functioning storefront.

This article builds on those fundamentals.

## Objective {#objective}

This document helps you understand how to integrate a catalog in your storefront.

## Configuring stores and catalogs {#catalog}

The CIF add-on and the [CIF Core Components](https://github.com/adobe/aem-core-cif-components) can be used on multiple AEM site structures connected to different commerce stores (or store views, etc) .By default, the CIF add-on is deployed with a default config connecting to Adobe Commerce's default store and catalog (Magento).

This configuration can be adjusted for the project via the CIF Cloud Service config following these steps:

1. In AEM go to Tools -> Cloud Services -> CIF Configuration

2. Select the commerce configuration you want to change

3. Open the configuration properties via the action bar

![CIF Cloud Services Configuration](/help/commerce-cloud/assets/cif-cloud-service-config.png)

The following properties can be configured:

* GraphQL Client - select the configured GraphQL client for commerce backend communication. This should typically stay at default.
* Store View - the (Magento) store view identifier. If empty, the default store view will be used.
* GraphQL Proxy Path - the URL path GraphQL Proxy in AEM use to proxy requests to the commerce backend GraphQL endpoint.
    >[!NOTE]
    >
    > In most setups the default value `/api/graphql` must not be changed. Only advanced setup not using the provided GraphQL proxy should change this setting.
* Enable Catalog UID Support - enable support for UID instead of ID in the commerce backend GraphQL calls.
    >[!NOTE]
    >
    > Support for UIDs got introduced in Adobe Commerce (Magento) 2.4.2. Only enable this if your commerce backend supports a GraphQL schema of version 2.4.2 or later.
* Catalog Root Category Identifier - the identifier (UID or ID) of the store catalog root
    >[!CAUTION]
    >
    > Starting with CIF Core Components version 2.0.0 the support for `id` was removed and replaced with `uid`. If your project uses CIF Core Components version 2.0.0 you must enable Catalog UID Support and use a valid category UID as "Catalog Root Category Identifier".

The configuration shown above is for reference. Projects should provide thier own configurations.

## What's Next {#what-is-next}

Now that you have completed this part of the journey you should:

* have integrated a catalog in your storefront.

Build on this knowledge and continue your  journey by next reviewing the document [Extending the storefront](extending-storefront.md), where you will learn how extend your storefront.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the journey by reviewing the document [Extending the storefront](extending-storefront.md), the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the headless journey.

* [Migration guide for the Experience Manager Cloud Service](/help/commerce-cloud/migration.md) - How to migrate to the AEM Commerce Integration Framework (CIF) add-on from an old version
