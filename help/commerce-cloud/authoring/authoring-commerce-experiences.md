---
title: Authoring commerce experiences
description: Working commerce experiences
exl-id: 2cef5d4b-45f6-4d72-a24b-67ca53d9057d
---
# Authoring commerce experiences {#authoring-commerce-experiences}

## Overview {#overview}

The CIF add-on extends AEM authoring with commerce specific capabilties. This enables authors to build and managed commerce related experiences efficiently by getting access to product data and content without leaving the context.

## Pickers {#pickers}

tbd

## Universal editor {#universal-editor}

The Universal Editor is extended with capabilities to access the real time product data and associated product content.

### Accessing product data

The 'Assets' tab in the editor's Side panel offers access to product data by selecting the type 'Products'. The data is fetched live from the configured commerce endpoint. The filter is a full-text serach on the commerce endpoint to find specific products.

![Product data side panel](assets/products-side-panel.png)

Analog to assets, products can be dnd on a page (Which creates a product teaser component as default) or components (Currently supported are product teaser and product carousel).

### Accessing associated product content

tbd

## Omnisearch {#omnisearch}

Using Omnisearch is an easy way for practioners to find AEM content and product catalog data using full-text search. Omnisearch will run full-text search in AEM and the commerce backend to find product catalog objects in the commerce backend and AEM content. AEM results also include content that was tagged with product / category data.

tbd-image

The result is grouped by type.
