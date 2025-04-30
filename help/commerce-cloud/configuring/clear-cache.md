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
  * Configuration Should be enabled for both Author & Publish instances.
Enable the Dispatcher cache (Optional): Clients can enable the dispatcher clear cache setting by adding  the following property in the above configuration  i.e "enableDispatcherCacheInvalidation" to true. This provides functionality to clear cache from the dispatcher. Note: This will only works with Publish Instances.
Also, make sure to give the corresponding pattern which suits your product, category & cms page needs to be added to the above configuration file in order to remove it from dispatcher cache. 
Add corresponding index in your project(Recommended):  In order to improve the sql queries performance for finding the corresponding page related with product & category. Please refer the following link https://github.com/adobe/aem-cif-guides-venia/blob/main/ui.apps/src/main/content/jcr_root/_oak_index/cifCacheInvalidationSupport/.content.xml.

## Verifying Clear Cache Feature {#verify-clear-cache}

## Clear Cache Invalidation API {#clear-cache-api}

## Extensibility {#clear-cache-extensibility}
