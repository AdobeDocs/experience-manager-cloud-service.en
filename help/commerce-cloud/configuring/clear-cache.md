---
title: Component & GraphQL Clear Cache
description: Learn how to enable and verify the clear-cache feature in AEM CIF.
feature: Commerce Integration Framework
role: Admin
---

# Component & GraphQL Clear Cache {#clear-cache}

This document provides a comprehensive guide on enabling and verifying the clear-cache feature in AEM CIF.

## Enabling Clear Cache Feature in CIF Configuration {#enable-clear-cache}

By default, the clear-cache feature will be disabled in CIF configuration. To enable it, you need to add the following to your corresponding projects:

* Enable the servlet `/bin/cif/invalidate-cache` which helps you triggering the clear-cache API with their corresponding requests by adding the `com.adobe.cq.cif.cacheinvalidation.internal.InvalidateCacheNotificationImpl.cfg.json` configuration in your project as shown [here](https://github.com/adobe/aem-cif-guides-venia/blob/main/ui.config/src/main/content/jcr_root/apps/venia/osgiconfig/config.author/com.adobe.cq.cif.cacheinvalidation.internal.InvalidateCacheNotificationImpl.cfg.json).
   >[!NOTE]
   >
   > Configuration needs to be enabled only for the author instances.
* Enable the listener in order to clear cache from each instance of AEM (publish and author) by adding the `com.adobe.cq.commerce.core.cacheinvalidation.internal.InvalidateCacheSupport.cfg.json` configuration in your project as shown [here](https://github.com/adobe/aem-cif-guides-venia/blob/main/ui.config/src/main/content/jcr_root/apps/venia/osgiconfig/config/com.adobe.cq.commerce.core.cacheinvalidation.internal.InvalidateCacheSupport.cfg.json).
  * Configuration should be enabled for both author and publish instances.
  * Enable the Dispatcher cache (Optional): you can enable the dispatcher clear cache setting by setting the `enableDispatcherCacheInvalidation` property to true in the above configuration. This provides functionality to clear cache from the dispatcher.
   >[!NOTE]
   >
   > This will only works with publish instances.
  * Also, make sure to give the corresponding pattern which suits your product, category and cms page needs to be added to the above configuration file in order to remove it from dispatcher cache. 
* In order to improve the sql queries performance for finding the corresponding page related with product and category, add the corresponding index in your project (recommended). Fore more information, see [cifCacheInvalidationSupport/](link https://github.com/adobe/aem-cif-guides-venia/blob/main/ui.apps/src/main/content/jcr_root/_oak_index/cifCacheInvalidationSupport/.content.xml).

## Verifying Clear Cache Feature {#verify-clear-cache}

To verify that everything is set up properly:

* Trigger the corresponding servlet to the Author Instance AEM, for example [http://localhost:4502/bin/cif/invalidate-cache](http://localhost:4502/bin/cif/invalidate-cache) and you should get a 200 HTTP response.
* Verify that a node has been created under the following path in author instances: `/var/cif/cacheinvalidation`. The node name will follow this pattern: `cmd_{{timestamp}}`.
* Verify the same node has been created in each publish instances too.

Now, to check whether the caches are getting cleared properly:
1. Navigate to the corresponding PLP and PDP pages.
2. Update a product or category name in the commerce engine. The changes will not be reflected in AEM immediately based on cache configurations.
3. Trigger the servlet API as shown here:
   ```
   curl --location '{Author AEM Instance Url}/bin/cif/invalidate-cache' \
   --header 'Content-Type: application/json' \
   --header 'Authorization: ••••••' \ // Mandatory
   --header 'Cookie: private_content_version=0299c5e4368a1577a6f454a61370317b' \
   --data '{
       "productSkus": ["Sku1", "Sku2"], // Optional: Pass the corresponding sku which got updated
       "categoryUids":["CategoryUid"], // Optional : Pass the corresponding category-uid which got updated.
       "storePath": "/content/venia/us/en", // Mandatory : Needs to given in order to know for which site we are removing the clear cache
   }'
   ```
If everything goes well, the new changes will be reflected in every instance. If changes are not reflected for the publish instance, please check in the private window for corresponding PLP and PDP pages.

>[!NOTE]
>
> Publish instances can have multiple level of cache layers. The feature is only responsible for clear cache from AEM internal memory and dispatcher. 

## Clear Cache Invalidation API {#clear-cache-api}

This is the API which clients needs to trigger whenever they wanted to clear cache of commerce related data from AEM.

Request Type: `POST`

### Headers

| Parameter| Value| Required/Mandatory| Comment |
|------------------------------|-------------------|---|---|
| `Content-Type`                           | `application/json`            | Required | |
| `Authorization`                      | Corresponding Author's User credentials (Auth Type: Basic Auth)  | Required | Add the corresponding username and password |


>[!NOTE]
>
> Below are existing attributes which the feature is giving out of the Box.



### Payload

This InvalidateType needs to be given in combination of Mandatory attribute (i.e storePath)

## Extensibility {#clear-cache-extensibility}

This feature not only delivers its core functionality but also offers extensibility, allowing developers to build upon and customize it further as needed.

### Extending the Existing Attribute {#existing-attribute}

In cases where the cache needs to be cleared that are not currently covered by the existing attribute-based functionality (such as `categoryUids`), you can refer to [this reference file](https://github.com/adobe/aem-cif-guides-venia/blob/main/core/src/main/java/com/venia/core/models/commerce/services/cacheinvalidation/ExtendedCategoryUidInvalidation.java
) to add new patterns and define additional `invalidatePaths` that should be cleared from the cache beyond what the current implementation handles.

### Adding New Custom Attribute {#new-custom-attribute}

If for example you don't want to use the existing attribute for clearing the cache, then you have the flexibility to create your own attribute and define its corresponding functionality.

* If you only need to clear cache from the internal memory of AEM (the graphql response), then you need to follow [this reference](https://github.com/adobe/aem-cif-guides-venia/blob/main/core/src/main/java/com/venia/core/models/commerce/services/cacheinvalidation/CustomInvalidation.java).
* If you need to clear cache from the internal memory and the dispatcher cache, then you need to follow [this reference](https://github.com/adobe/aem-cif-guides-venia/blob/main/core/src/main/java/com/venia/core/models/commerce/services/cacheinvalidation/CustomDispatcherInvalidation.java).
   >[!NOTE]
   >
   > You can ignore the internal clear cache by returning `null` for the `getPatterns()` method.
