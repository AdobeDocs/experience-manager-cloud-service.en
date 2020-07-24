---
title: AEM and Magento Integration using Commerce Integration Framework
description: AEM and Magento Integration using Commerce Integration Framework
---

# AEM and Magento Integration using Commerce Integration Framework

AEM and Magento are seamlessly integrated using the Commerce Integration Framework (CIF). CIF enables AEM to access a Magento instance and bind the catalog data via GraphQL. It also allows AEM Authors to use Product and Category Pickers and a read-only Product Console to browse through product and category data fetched on-demand from Magento. In addition, CIF provides an out-of-the-box storefront that can accelerate commerce projects.

## Architecture

The overall architecture is as follows:

![AEM Magento Architecture Overview](/help/commerce-cloud/assets/AEM_Magento_Architecture.JPG)

## AEM Venia Reference Store-front

The AEM Venia reference storefront is a modern production-ready reference storefront showcasing a basic B2C commerce journey. It can be used to kickstart commerce projects and accelerate projects using AEM, CIF, and Magento. It demonstrates best practices for integrating AEM and Magento and shows how to use the Commerce Core Components. It also provides pre-sales with a reference site to demo the integration between AEM and Magento.

The project is open source and available on [GitHub](https://github.com/adobe/aem-cif-project-archetype).

## AEM CIF Core Components and AEM Authoring

Basic components are provided, common across commerce implementations such as Product Detail, Product List, Navigation, Search, etc. They can be used as-is or be extended.

The [AEM CIF Core Components](https://github.com/adobe/aem-core-cif-components) work like the [AEM Sites Core Components](https://github.com/adobe/aem-core-wcm-components) but are dedicated to commerce specific use-cases.

These components key benefits are:

- They are easy to use in your projects.
- They can be used as-is or with very minimal modifications.
- They provide best practices for connecting with Magento via GraphQL APIs or REST APIs

Components such as Product Teaser and Product Carousel are provided to enable AEM Authors to create Experience pages in AEM, combining marketing and commerce content. These components can be easily dragged and dropped on to a content page created in AEM and linked to specific products or categories using the Product or Category Picker in AEM.

All the components are open-sourced on [GitHub](https://github.com/adobe/aem-core-cif-components).
This shows full transparency on changes made going forward and allows you to get the latest version very easily. You can also provide pull requests for improvements and bug fixes that can be incorporated.

## AEM Commerce connector for Magento and GraphQL

This connector provides integration of Magento products and categories in the AEM Commerce console as well as authoring features like product and category pickers. It also provides authoring features to display product and category information of data stored in Magento from within AEM by using Magento's [GraphQL APIs](https://devdocs.magento.com/guides/v2.3/graphql/index.html)

- The AEM Commerce console shows a hierarchal view of products stored in Magento organized by category.
- The Product Picker is an AEM Dialog field, similar to the Asset Picker, that would be used with an AEM Component to allow a user to select one or more products.
- The Category Picker is an AEM Dialog field, similar to the Asset Picker or Product Picker, that would be used with an AEM Component to allow an author to select one or more category.

The AEM Commerce connector is expected to be used to enhance the AEM authoring experience with deeper integration with Magento products and categories.

It is open source on [GitHub](https://github.com/adobe/commerce-cif-connector) and you are welcome to [contribute](https://github.com/adobe/commerce-cif-connector/blob/master/.github/CONTRIBUTING.md).

Even if you have very specific use-cases, the connector can be used a reference to build additional extensions to the AEM UI, but keep in mind that any extensions to the AEM UI can have an impact on future upgrades.

## Integration pattern

The AEM Venia Store front is a mixed page application in which AEM owns the glass and Magento powers the commerce backend in a headless way. Both server-side rendering and client-side rendering are used in the storefront. Server-side rendering is used to deliver static content and client-side rendering is used to deliver dynamic content.

Product and Catalog pages are relatively static and are rendered server-side using AEM Core Components such as Product Detail and Product List on generic templates created in AEM. These components get data from Magento via GraphQL APIs.
These pages are created dynamically, rendered on the server, cached on the AEM dispatcher and then delivered to the browser.
For more dynamic attributes such as Inventory or Price, on the other hand, client-side components are used. Client-side components or Web components fetch data directly from Magento via GraphQL APIs and the content is then rendered on the browser.

### Commerce APIs

This integration works with the latest Magento 2.3.5 release. For more information on GraphQL APIs and coverage, refer to [GraphQL API](https://devdocs.magento.com/guides/v2.3/graphql/index.html). 

### Catalog Management

From a catalog management point of view, Magento is responsible for all commerce data including categories, products, product attributes, and so on. No commerce data is imported and stored in AEM. AEM Authors can view the product catalog stored in Magento via a read-only Product Console in AEM but cannot make any edits to the product catalog. Any changes to the product catalog can be made only via the Magento Admin UI.

### Checkout

This integration uses client-side Cart component that renders the shopping cart and the checkout form to demonstrate a full experience integration pattern where you can deliver commerce experiences with Magento running in a completely headless way and AEM owning the glass. This component requires the AEM Dispatcher to be setup with GraphQL routing to enable the AEM page to access Magento's GraphQL endpoint. Additionally, it is mandatory to use abstracted payment methods. This puts the browser client in direct communication with the payment gateway provider so that neither Adobe or Magento clouds hold or pass PCI sensitive data. 

### Account Management

Account management is handled by Magento but in our integration we have developed client-side React-based components to enable AEM to render the experience for the following functionalities: Create Acct, Sign In, and Forgot Password. These components require the AEM Dispatcher to be setup with GraphQL routing to enable the AEM page to access Magento's GraphQL endpoint. 

