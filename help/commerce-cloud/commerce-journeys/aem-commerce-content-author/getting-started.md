---
title: Getting Started with CIF Authoring
description: Getting Started with CIF Authoring.
exl-id: 0bef4d8c-0ad3-4ec8-ab08-8c83203b3b68
feature: Commerce Integration Framework
role: Admin
---
# Getting Started with AEM CIF Authoring {#getting-started}

Get to know about Adobe Experience Manager (AEM) CIF Authoring.

## The Story So Far {#story-so-far}

In the previous document of this AEM Content and Commerce journey, [Learn about AEM Content and Commerce](/help/commerce-cloud/introduction.md), you learned the basic theory and concepts of headless CMS and AEM Content and Commerce.

This article builds on those fundamentals.

## Objective {#objective}

This document helps you understand how to use CIF for Content and Commerce specific authoring. After reading, you should:

* Understand the concepts of CIF authoring using Page Editor in AEM
* How to access product catalog data in AEM using product and category pickers
* How to access content and commerce data using the product cockpit and AEM Omnisearch

## CIF Authoring in AEM Page Editor {#cif-authoring}

CIF extends the Page Editor in AEM with capabilities to access the real-time product data without leaving the context:

Open the side panel and select 'Products' from the drop-down list.
![Select product type](assets/asset-finder-overview.png)

You can  browse the product catalog or use the full-text search field to find products.
![product type](assets/asset-finder-search.png)

Products can be dropped on components that support product drops (example product teaser, product carousel) on directly on the page which automatically creates a product teaser component.

## Product and Category Pickers {#pickers}

If product and category data is required in commerce components or AEM back-office dialogs, AEM authors can use pickers which are UI elements to comfortably search and select product catalog data.

### Product Picker

Clicking the folder icon opens the picker modal UI (for example, product teaser)
![product picker](assets/product-picker-open.png)

Products can be found either by browsing through the catalog structure on the left or search. Full-text search respects the selected category and limits the search results to this category.
![product picker folder](assets/product-picker-folders.png)

Products with variations are marked with a folder icon that can be clicked to show all variations.
![product picker variants](assets/product-picker-variants.png)
![product picker variants open](assets/product-picker-variants-open.png)

### Category Picker

Works like a product picker. Clicking the folder icon opens the picker modal UI (for example, category carousel)
![category picker](assets/category-picker-open.png)

Browse the catalog structure on the left and select the category.
![category picker](assets/category-picker-folders.png)

## Product Cockpit {#cockpit}

The product cockpit is a central place to quickly access the product catalog with all its enriched content. You learn in one of the next modules how to enrich product data with content. For now, let's focus on accessing product data.

From the main menu, click commerce to see a list of all attached product catalogs.
![commerce menu item](assets/commerce-menu-item.png)

This shows a list of all connected product catalogs.
![cockpit integrated catalogs](assets/cockpit-Integrated-catalogs.png)

The product catalog shows per default all first-level categories with all products. Clicking a category opens that category with all related products and subcategories, including their products.
![cockpit product catalog](assets/cockpit-product-catalog.png)

You can open the product properties by clicking the property icon. The icon appears by hovering over a product tile.
![cockpit product properties](assets/cockpit-properties.png)

All the product properties are read-only because the data gets loaded in real time from the connected backend. Changing product properties must be done in the backend system which is the system of record. The tab **Variants** only appear if the product has variations. Clicking the tab displays all variations with its attributes.
![cockpit product variants](assets/cockpit-properties-variants.png)

The remaining tabs show all AEM content that is associated with the product. These tabs are discussed in one of the next modules.

## AEM Omnisearch {#omnisearch}

Using Omnisearch is an easy way to find AEM content using full-text search. CIF extends Omnisearch with full-text search of product catalogs with its associated AEM content.
![commerce menu item](assets/omnisearch.png)

Omnisearch runs a full-text search in the commerce backend to find all related products. The result is listed under **View All Products**. Omnisearch also searches AEM for content that is associated to the searched product. The results are listed under the respective AEM categories. In this example, one Content Fragment is related to the product.

## What's Next {#what-is-next}

Now that you have completed this part of the journey you should:

* Understand the concepts of CIF authoring using the Page Editor
* How to access product catalog in AEM using product & category pickers
* How to access content and commerce data using the product cockpit and AEM Omnisearch

Build on this knowledge and continue your journey by next reviewing the document [Manage Product Catalog Pages and Templates](catalog-templates.md), where you learn how to build and customize your first product catalog experience.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the journey&ndash;[Manage Product Catalog Pages and Templates](catalog-templates.md)&ndash;the following are some optional resources that do a deeper dive on some concepts mentioned here. However, these optional resources are not required to continue on the journey.

* [Configuring Stores and Catalogs](/help/commerce-cloud/getting-started.md#catalog)
