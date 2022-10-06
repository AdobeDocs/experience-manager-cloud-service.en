---
title: Dispatcher Configurations in Screens as a Cloud Service
description: This page describes Dispatcher Configurations in Screens as a Cloud Service.
exl-id: cc04b480-9310-4975-a7c2-20682c567fa4
---
# Dispatcher Configurations in Screens as a Cloud Service {#dispatcher-configurations-screens-cloud}

This section describes the dispatcher configurations for Screens as a Cloud Service.

## Adding Filters and Cache Rules in Dispatcher for Screens as a Cloud Service deployment {#deployment}

Allow the following filters and cache rules in dispatchers for the publish instances in Screens as a Cloud Service.

### AEM Screens Filters {#filters}
 
```
## # Content Configurations
/0200 { /type "allow" /method '(GET|HEAD)' /url "/content/screens/*" }
#/0201 { /type "allow" /method '(GET|HEAD)' /url "/content/experience-fragments/*" } ## uncomment this, if you're using experience-fragments
## add any other formats required for your project here
/0202 { /type "allow" /extension '(css|eot|gif|ico|jpeg|jpg|js|gif|pdf|png|svg|swf|ttf|woff|woff2|html|mp4|mov|m4v)' /path "/content/dam/*" }
/0203 { /type "allow" /method 'GET' /url "/screens/channels.json" }
## # Enable clientlibs proxy servlet
/0210 { /type "allow" /method "GET" /url "/etc.clientlibs/*" }
```

### Cache Rules {#cache-rules}

* Add `/statfileslevel "10"` to `/cache` section in `publish_farm.any`/.

   >[!NOTE]
   >This cache rule supports caching up to 10 levels from the cache docroot and invalidates when content is published rather than invalidating everything. You can change this level based on how deep your content structure is setup.

* Add the following to `/invalidate` section in `publish_farm.any`.

   ```
   /0003 {
       /glob "*.json"
       /type "allow"
   }
   ```

* Add the following rules to `/rules` section in `/cache` in publish_farm.any or in a file that's included from `publish_farm.any`.

   ```
   ## Allow Dispatcher Cache for Screens channels
    /0002
        {
        /glob "/content/screens/*.html"
        /type "allow"
        }

   ## Allow Dispatcher Cache for Screens offline manifests

   /0003
       {
       /glob "/content/screens/*.manifest.json"
       /type "allow"
       }

   ## Allow Dispatcher Cache for Assets
   /0004
       {
       /glob "/content/dam/*"
       /type "allow"
       }

   ## Deny Screens Channels json
   /0005
       {
       /glob "/screens/channels.json"
       /type "deny"
       }
   ```
