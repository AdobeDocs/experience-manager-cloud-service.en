---
title: Architecture of the Commerce Integration Framework on AEM as a Cloud Service
description: Architecture of the Commerce Integration Framework on AEM as a Cloud Service
---

# Architecture of the Commerce Integration Framework on AEM as a Cloud Service {#commerce-architecture}



## AEM and Magento Integration using Commerce Integration Framework

AEM and Magento are seamlessly integrated using the Commerce Integration Framework (CIF). CIF enables AEM to access a Magento instance and bind the catalog data via GraphQL. It also allows AEM Authors to use Product and Category Pickers and a read-only Product Console to browse through product and category data fetched on-demand from Magento. In addition, CIF provides an out-of-the-box storefront that can accelerate commerce projects.

### Architecture

The overall architecture is as follows:

![AEM Magento Architecture Overview](assets/AEM_Magento_Architecture.JPG)

#### Commerce APIs

This integration works with the latest Magento 2.3.5 release. For more information on GraphQL APIs and coverage, refer to [GraphQL API](https://devdocs.magento.com/guides/v2.3/graphql/index.html). 

#### Catalog Management

From a catalog management point of view, Magento is responsible for all commerce data including categories, products, product attributes, and so on. No commerce data is imported and stored in AEM. AEM Authors can view the product catalog stored in Magento via a read-only Product Console in AEM but cannot make any edits to the product catalog. Any changes to the product catalog can be made only via the Magento Admin UI.

