---
title: Enabling Progressive Web App Features
description: AEM Sites allows the content author to enable progressive web app capabilities to any site through simple configuration instead of coding.
---

# Enabling Progressive Web App Features {#enabling-pwa}

Through a simple configuration, a content author can now enable progressive web app (PWA) features for experiences created in AEM Sites.

## Introduction {#introduction}

[Progressive web apps (PWAs)](https://web.dev/progressive-web-apps/) enable immersive app-like experiences for AEM sites by allowing them to be stored locally on a user's machine and be accessible offline. A user could browsing an site while on-the-go and lose the internet connection. PWAs allow seamless experiences even if the network is lost or unstable.

Instead of requiring any re-coding of the site, a content author is able to configure PWA properties as an additional tab in the [page properties](/help/sites-cloud/authoring/fundamentals/page-properties.md) of a site.

* When saved or published, this configuration riggers an event handler that writes out the manifest and service worker that enhances the site to become a PWA.
* The manifest and service worker are stored in context aware configuration applicable to the site. Sling mappings are also maintained to ensure that service worker is served from the root of the application to enable proxying content allowing offline capabilities within the app.

In the end the user has a local copy of the site, giving an app-like experience even without an internet connection.

## Enabling PWA {#enabling-pwa}

1. Log into AEM.
1. From the main menu, tap or click **Navigation** -&gt; **Sites**.
1. Select the Sites project and tap or click [**Properties**](/help/sites-cloud/authoring/fundamentals/page-properties.md) or use the hotkey `p`.
1. Select the **Progressive Web App** tab and configure the applicable properties.
   1. You will need to upload a 512x512 png icon to assets (DAM) and reference that as the icon for this app.
   1. Configure the paths you want the service worker to take offline. The usual areas are
      * `/content/<sitename>`
      * `/content/experiencefragements/<sitename>`
      * `/content/dam/<sitename>`
      * Any third party font references
      * `/etc/clientlibs/<sitename>`
1. Save and close
1. Access the starting page in your browser.
1. You should now see a + icon on the address bar allowing you to install the app.
1. Install the app, browse a bit to ensure the pages are taken offline. Enjoy.

## Limitations {#limitations}

* A user must browse the page at least once before it becomes cached offline.
* Pages are not automatically synched or updated if the suer is not using the app.
