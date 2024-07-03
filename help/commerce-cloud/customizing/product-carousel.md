---
title: Custom Attributes to CIF Product Carousel
description: Learn how to extend the AEM CIF Product Carousel component by updating the Sling Model and customizing the markup.
feature: Commerce Integration Framework
role: Admin, Developer
---
# Custom Attributes to CIF Product Carousel {#product-carousel}

## Introduction {#intro}

The Product Carousel component is extended throughout this tutorial. As a first step, add an instance of the Product Carousel to the Home page to understand the baseline functionality:

1. Navigate to the Home Page of the site, for example [http://localhost:4502/editor.html/content/acme/us/en.html](http://localhost:4502/editor.html/content/acme/us/en.html)
1. Insert a new Product Carousel component into the main layout container on the page.
    ![Product Carousel component](/help/commerce-cloud/assets/product-carousel-component.png)
1. Expand the Side Panel (if not already toggled) and switch the asset finder dropdown to **Products**.
     ![Carousel Products](/help/commerce-cloud/assets/carousel-products.png)    
1. This should display a list of available products from a connected Adobe Commerce instance.
    ![Connected Instance](/help/commerce-cloud/assets/connected-instance.png)
1. Products will be shown like below with default properties:
    ![Product Shown with Properties](/help/commerce-cloud/assets/discount.png)
    
## Update the Sling Model {#update-sling-model}

You can extend the business logic of the Product Carousel by implementing a Sling Model:

1. In your IDE, navigate under the core module to `core/src/main/java/com/venia/core/models/commerce` and create a CustomCarousel Interface that extends the CIF ProductCarousel interface:
    
    ```
    package com.venia.core.models.commerce;
    import com.adobe.cq.commerce.core.components.models.productcarousel.ProductCarousel;
    public interface CustomCarousel extends ProductCarousel {
    }
    ```
1. Next, create an implementation class `CustomCarouselImpl.java` at `core/src/main/java/com/venia/core/models/commerce/CustomCarouselImpl.java`.
   The delegation pattern for Sling Models allows `CustomCarouselImpl` to reference `ProductCarousel` model via the `sling:resourceSuperType` property:

    ```
    @Self
    @Via(type = ResourceSuperType.class)
    private ProductCarousel productCarousel;
    ```

1. The @PostConstruct annotation ensures that this method is called when the Sling Model is initialized. The product GraphQL query has already been extended using the extendProductQueryWith method to retrieve attributes. Update the GraphQL query to include the  attribute in the partial query:

    ```
    @PostConstruct
    private void initModel() {
    productsRetriever = productCarousel.getProductsRetriever();
    
    if(productCarousel.getProductsRetriever() != null)
    productCarousel.getProductsRetriever().extendProductQueryWith(p -> p
    .createdAt()
    .addCustomSimpleField("accessory_gemstone_addon")
    );
    }
    ```
    
    In the above code, the `addCustomSimpleField` is used to retrieve the `accessory_gemstone_addon` attribute.

## Customizing the Markup {#customize-markup}

To further customize the markup:

1. Create a copy of `productcard.html` from `/apps/core/cif/components/commerce/productcarousel/v1/productcarousel` (the core component crxde path) to ui.apps module `ui.apps/src/main/content/jcr_root/apps/venia/components/commerce/productcarousel/productcard.html`. 

1. Edit `productcard.html` to call the custom attribute, which is mentioned in the implementation class:


    ```
    
    data-product-sku="${product.commerceIdentifier.value}"
    data-product-base-sku="${product.combinedSku.baseSku}"
    id="${product.id}"
    data-cmp-data-layer="${product.data.json}"
    class="card product__card">
    <span>${product.product.responseData['accessory_gemstone_addon']}</span>
    <a href="${product.URL}"
    target="${productCarousel.linkTarget}"
    
    ```

1. Save the changes and deploy the updates to AEM using your Maven command, from a command-line terminal. You will be able to see the custom attribute `accessory_gemstone_addon` value for the selected products on the page.
