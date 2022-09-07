---
title: Troubleshooting caching performance  
seo-title: Troubleshooting caching performance  
description: Troubleshooting caching performance  
seo-description: Troubleshooting caching performance  
contentOwner: khsingh
exl-id: eae44a6f-25b4-46e9-b38b-5cec57b6772c
---
# Caching performance {#caching-performance}

You can encounter some of the following issues while configuring or using Adaptive Forms cache in a Cloud Service environment:

## Some Adaptive Forms containing images or videos are not automatically invalidated from Dispatcher cache {#images-videos-not-invalidated}

You can select and add images or videos from asset browser to an Adaptive Form. When these images are edited in Assets editor, the cached version of an Adaptive Form containing such images is not invalidated. The Adaptive Form continues showing older images. 

To resolve the issue, after publishing the images and video, explicitly unpublish and publish the Adaptive Forms that reference these assets.

## Some Adaptive Forms containing content fragment or Experience Fragments are not automatically invalidated from Dispatcher cache {#content-fragments-experience-fragments-not-invalidated}

You can add a content fragment or an Experience Fragment to an Adaptive Form. When these fragments are independently edited and published, the cached version of an Adaptive Form containing such fragments not invalidated. The Adaptive Form continues showing older fragments. 

To resolve the issue, after publishing updated content fragment or Experience Fragment, explicitly unpublish and publish the Adaptive Forms that use these assets.

## Only first instance of Adaptive Forms is cached {#only-first-instance-cached}

When the Adaptive Form URL does not contain any localization information, and the Use Browser Locale option in configuration manager is enabled, a localized version of the Adaptive Form is served and an instance of the Adaptive Form, based on the first request (browser locale requested), is cached and delivered to every subsequent user.

Perform the following steps to resolve the issue:

1. Open your Experience Manager project.
1. Open the `dispatcher/scr/conf.d/rewrites/rewrite.rules` for editing.
1. Open the `conf.d/httpd-dispatcher.conf` or any other configuration file configured to load at runtime.
1. Add the following code to your file and save it. It is a sample code modify it to suit your environment.

```shellscript

    # Handle actual URL convention (just pass through)
    RewriteRule "^/content/forms/af/(.*)[.](.*).html$" "/content/forms/af/$1.$2.html" [PT]
    
    # Handle selector-based redirection based on browser language
    <VirtualHost *:80>
            # Handle actual URL convention (just pass through)
    RewriteRule "^/content/forms/af/(.*)[.](.*).html$" "/content/forms/af/$1.$2.html" [PT]

    # Handle selector based redirection basded on browser language
    # The Rewrite Condition is looking for the Accept-Language header and if found takes the first two character which most likely will be the desired language selector.
    RewriteCond %{HTTP:Accept-Language} ^(..).*$ [NC]
    RewriteRule "^/content/forms/af/(.*).html$" "/content/forms/af/$1.%1.html" [R]
    RewriteRule "^/content/forms/af/(.*).html$" "/content/forms/af/$1.%1.html" [R]

```

## CDN caching stops working after 300 seconds {#cdn-caching-stops-working-after-300-seconds}

CDN caching stops working after 300 seconds and all the requests to cache on CDN are redirected to Dispatcher.

To resolve the issue, set the age header to 0:

1. Create a file at `src\conf.d\available_vhosts`

1. Add the following to file to set the age header

    ```shellscript
        <IfModule mod_headers.c>
                Header add X-Vhost "publish"
                Header set age 0
        </IfModule>
    ```

1. Save and close the file.
1. Modify the soft link for `src\conf.d\enabled_vhosts\default.vhost` to point to new file.
