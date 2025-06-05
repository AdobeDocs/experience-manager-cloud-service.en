---
title: JSON-LD Metadata
description: Learn how to enable and verify the JSON+LD feature in AEM CIF.
feature: Commerce Integration Framework
role: Admin, Developer
exl-id: 547d3721-e094-4a42-8a7c-27e4ef97ea9c
---
# JSON-LD Metadata {#json-ld}

This guide explains how to enable and verify the JSON+LD feature in AEM CIF.

## Enabling JSON+LD in CIF Configuration {#enabling}

By default, the **Enable JSON+LD** checkbox is not visible in the CIF configuration. To enable this feature, the project must include the necessary OSGi configuration, which allows the checkbox to be displayed. This configuration enables users to toggle JSON+LD script support on product pages.
To make the **Enable JSON+LD** checkbox available in the CIF configuration, add the following OSGi configuration to your project: `
com.adobe.cq.cif.components.models.JsonLdFeatureEnable`.
For further details on adding this configuration, refer to [Adds configuration for Json-Ld](https://github.com/adobe/aem-cif-guides-venia/blob/main/ui.config/src/main/content/jcr_root/apps/venia/osgiconfig/config/com.adobe.cq.cif.components.models.JsonLdFeatureEnable.cfg.json) in the public aem-cif-guides-venia repository.

Once this configuration is added and deployed, the checkbox becomes visible in the CIF configuration settings and here are the steps to enable **JSON+LD**:

1. Navigate to CIF configuration in AEM.
1. Cancel inheritance.
1. Check the **Enable JSON+LD** checkbox.
1. Save the configuration.

## Verifying JSON+LD on a Product Detail Page (PDP) {#verify}

To illustrate the steps to verify JSON+LD,  the Venia project is used as an example, where the required JSON+LD configuration is already added to enable the feature. Here are the steps to follow:

1. Navigate to your local AEM instance and open the Product Detail Page (PDP): http://localhost:4502/editor.html/content/venia/us/en/products/product-page.html
1. Author a product on the Product Detail Page (PDP).
1. Switch to **View as Publish** mode.
1. Open the **View Page Source** in your browser.
1. Search for JSON+LD in the page source.

If configured correctly, you find the JSON+LD script associated with the product injected into the page.

## Sample JSON+LD Structure for a Product {#sample}

Below is an example **JSON+LD** structure for the Agatha Skirt, authored on the PDP page in the Venia project:

```
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "Product",
  "sku": "VSK05",
  "name": "Agatha Skirt",
  "image": "https://mcstaging.catalogservice4commerce.fun/media/catalog/product/cache/926ea6fc2ad48a7202ff4587b6c2768e/v/s/vsk05-pe_main_2.jpg",
  "description": "The Agatha Skirt has a large circumference that lends itself to all sorts of drama...",
  "@id": "product-ef4fa1dc72",
  "offers": [
    {
      "@type": "Offer",
      "sku": "VSK05-KH-S",
      "url": "/content/venia/us/en/products/product-page.html/agatha-skirt.html",
      "priceCurrency": "USD",
      "price": 78.0
    },
    {
      "@type": "Offer",
      "sku": "VSK05-RN-XS",
      "availability": "InStock",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "priceType": "https://schema.org/ListPrice",
        "price": 18.0,
        "priceCurrency": "USD"
      },
      "price": 46.0
    }
  ]
}
</script>
```

## Mapping JSON+LD Attributes to GraphQL {#mapping}

JSON+LD attributes can be mapped to GraphQL queries in AEM CIF, ensuring structured data dynamically reflects product information retrieved via GraphQL. 

### Example Product Mapping {#example}

| JSON+LD Attribute| Magento GraphQL Attribute| Required (Y/N)|
|---------------------------------|-------------------|---|
| sku                             | sku               | N |
| offers.url                      | Custom Logic      | N |
| offers.SpecialPricedate         | special_to_date   | N |
| offers.sku                      | sku               | N |
|offers.priceSpecification.priceCurrency | currency   | Y|
| offers.priceSpecification.price | regular_price     | N |
| offers.priceCurrency            | currency          | Y |
| offers.price                    | special_price     | Y |
| offers.image                    | media_gallery.url | N |
| offers.availability             | stock_status      | N |
| name                            | name              | Y |
| image                           | media_gallery.url | Y |
| description                     | description       | N |
| aggregateRating.reviewCount     | review_count      | N |
| aggregateRating.ratingValue     | rating_summary    | N |
| @id                             | id                | N |

This mapping ensures that the JSON+LD script is dynamically populated based on product data retrieved via GraphQL queries.

To test your JSON+LD structure, you can use the [Rich Results Test - Google Search Console](https://search.google.com/test/rich-results/result?id=wtU3LVIEM8H7Aaf5qqK9qw). This tool provides detailed feedback, including whether the required attributes are present or missing, and helps ensure that your structured data is correctly implemented.
