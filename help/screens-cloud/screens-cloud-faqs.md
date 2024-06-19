---
title: Screens as a Cloud Service FAQs
description: This page describes Screens as a Cloud Service frequently asked questions.
exl-id: 93f2144c-0e64-4012-88c6-86972d8cad9f
feature: Administering Screens
role: "Admin, Developer, User"
---
# Screens as a Cloud Service FAQs {#screens-cloud-faqs}

The following section provides answers to Frequently Asked Questions (FAQs) related to Screens as a Cloud Service project.

## What should I do if AEM Screens Player pointing to Screens as a Cloud Service does not pick the custom clientlibs with /etc.clientlibs/xxx/clientlibs/clientlib-site.lc-813643788974b0f89d686d9591526d63-lc.min.css format?

AEM as a Cloud Service changes the long cache keys with every deployment. AEM Screens generates the offline caches when the content is modified, rather than when the Cloud Manager runs the deployment. These long cache keys in the manifests are invalid, so the player fails to download the *clientlibs*. 

Using `longCacheKey="none"` in your `clientlib` folder removes the long cache keys altogether for the *clientlibs*.


## What should I do if offline manifest does not include all resources as intended? {#offline-manifest}

Offline caches are generated using **bulk-offline-update-screens-service** service user. Certain paths, not accessible by `bulk-offline-update-screens-service`, lead to missing content in offline manifests. 

In your code, that is, `ui.config or ui.apps`, create an OSGi configuration in configuration folder, with the following content, and title the file name as `org.apache.sling.jcr.repoinit.RepositoryInitializer-serviceusersandacls-content.config`

```
scripts=[
        "
        set principal ACL for bulk-offline-update-screens-service
                allow jcr:read on /content/mysite
                allow jcr:read on /apps/my-resources
        end
        "] 
```

## What image formats are recommended for seamless rendition of images in an AEM Screens as a Cloud Service channel?{#screens-cloud-image-format}

Adobe recommends using images in the format `.png` and `.jpeg` in an AEM Screens as a Cloud Service channel, for the best digital signage experience.
The images in the format `*.tif` (Tag Image File format) are not supported in AEM Screens as a Cloud Service. If a channel has this format of image, on the player side, the image is not rendered.

## What should I do if a Channel in Developer mode (online) is not rendering on AEM Screens Player?{#screens-cloud-online-channel-blank-iframe}

Adobe recommends that you use AEM Screens caching capabilities. However, if you must run your Channel in Developer mode and the AEM Screens Player shows a blank screen, check your Player's developer tools and look for `X-Frame-Options` or `frame-ancestors` errors. The resolution is to configure the Dispatcher to allow content running in iFrames. Usually, the following configuration works:

```
Header set Content-Security-Policy "frame-ancestors 'self' file: localhost:*;"
```

## What is the use of the Registration Code Limit?

As a best practice, you can limit the registration code usage. If a registration code is compromised, but has a limit of 100 registrations, then the attacker can register only up to that number, but not more. You can always update the usage limit after the registration code is created and some of the customer's players have already been registered. If the customer observes unusual registration activity for a specific registration code, they can lower the limit in real time while they investigate. They can increase the number back if it was a false alarm, without impacting the already registered players.
