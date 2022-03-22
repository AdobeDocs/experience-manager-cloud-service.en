---
title: Product Cockpit
description: Working with Product Cockpit
exl-id: 6dbf039c-e040-48f1-88f3-ebbd70cdf94d
---
# Product Cockpit {#product-cockpit}

## Overview {#overview}

The Product Cockpit provides a unified overview of linked product catalogs and associated content. All associated content has links to quickly access it from the cockpit. 

Staged product data includes any mutation in the future such as new categories, products, or updated properties.

>[!NOTE]
>
>The term product catalog is interchangeable with commerce store, store view, and similar expressions.

## Configuration {#configuration}

Product catalogs need to be configured in AEM. See [configuring store and catalogs](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content-and-commerce/storefront/getting-started.html?#catalog) for more information.

Enabling staged catalog features require authentication. See [Getting Started](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content-and-commerce/storefront/getting-started.html) for more information.

>[!NOTE]
>
>Staged catalog features are only available with Adobe Commerce and 3rd party connectors that support token-based authentication.

## Opening the Product Cockpit {#opening-product-cockpit}

Easiest way to access the Product Cockpit is via the 'Commerce' menu in AEM's main menu. It is also possible to use Omnisearch (search for Commerce) or opening `https://<yourAEMInstance>/commerce.html`.

![AEM menu](../assets/aem-menu.png)

## Browsing Product Catalogs {#browsing-product-catalogs}

The Product Cockpit is organized in a hierarchical way following the product catalog structure. The first level shows the catalog root level of all configured product catalogs including meta information of the commerce backend.

![Configured catalogs](../assets/catalog-overview.png)

Clicking on a category will load the children of the clicked category.

![Category children](../assets/catalog-category-children.png)

Clicking on a product will load product variations if available.

![Product variations](../assets/catalog-product-variation.png)

>[!NOTE]
>
>Product catalog data in AEM is data that is retrieved in real time via the configured commerce endpoint. No product catalog data is store in AEM.

## Searching Product Catalogs {#searching-product-catalog}

A full-text search over the full product catalog is provided in the left filter tab to quickly find products.

![search](../assets/search-cockpit.png)

## Browsing Staged Product Catalog {#staged-product-catalogs}

By default, the product cockpit shows live product catalog data. Using the "STAGED CATALOG" in the left filter tab will load the product catalog for any selected date.

![staged catalog](../assets/staged-cockpit.png)

## Product Catalog Properties {#catalog-properties}

Clicking on the properties icon of a product or category will open the property view of the selected object. Open properties of a product variant is equal to open the main product properties.

### Commerce Tabs {#tabs}

The general and variant tabs show pre-defined commerce properties that come from the commerce backend. This data (incl. variants) is read-only data in AEM as the system of record is the commerce backend. The variant tab only appears for products with variants and shows a list of all variants.

![catalog properties](../assets/catalog-properties.png)

### AEM Content Tabs {#content-tabs}

These tabs, grouped by AEM content types (Experience Fragments, Content Fragments, Associated Assets), show AEM content that is associated with the commerce object. The action 'View Details' opens a new browser tab with the selected content.

![content properties](../assets/content-properties.png)
