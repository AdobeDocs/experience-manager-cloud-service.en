---
title: Enabling Progressive Web App Features
description: AEM Sites allows the content author to enable progressive web app capabilities to any site through simple configuration instead of coding.
---

# Enabling Progressive Web App Features {#enabling-pwa}

Through a simple configuration, a content author can now enable progressive web app (PWA) features for experiences created in AEM Sites.

>[!CAUTION]
>
>This is an advanced feature that requires:
>
>* Knowledge of PWAs
>* Knowledge of your site and content structure
>* Understanding of caching strategies
>* Support from your development team
>
>Before using this feature is is recommended that you discuss this with your development team to define the best way to leverage it for your project.

## Introduction {#introduction}

[Progressive web apps (PWAs)](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps) enable immersive app-like experiences for AEM sites by allowing them to be stored locally on a user's machine and be accessible offline. A user could browse a site while on-the-go and lose the internet connection. PWAs allow seamless experiences even if the network is lost or unstable.

Instead of requiring any re-coding of the site, a content author is able to configure PWA properties as an additional tab in the [page properties](/help/sites-cloud/authoring/fundamentals/page-properties.md) of a site.

* When saved or published, this configuration triggers an event handler that writes out the [manifest files](https://developer.mozilla.org/en-US/docs/Web/Manifest) and [service worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) that enhances the site to become a PWA.
* The manifest and service worker are stored in [context aware configuration](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/context-aware-configs.html) applicable to the site. Sling mappings are also maintained to ensure that service worker is served from the root of the application to enable proxying content allowing offline capabilities within the app.

In the end the user has a local copy of the site, giving an app-like experience even without an internet connection.

>[!NOTE]
>
>Progressive web apps are an evolving technology and support for local app installation [depends on which browser you use.](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Installable_PWAs#Summary)

## Prerequisites {#prerequisites}

To be able to use PWA features for your site, there are two requirements for your project environment.

1. Adjust your components to enable this feature
1. Adjust your dispatcher rules to expose the manifest files

These are technical steps that the author will need to coordinate with the development team. These steps are only required once per site.

### Adjust Your Components {#adjust-components}

Your components need to include the [manifest files](https://developer.mozilla.org/en-US/docs/Web/Manifest) and [service worker.](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) To do this, the developer will need to add the following link to the `customheaderlibs.html` file of your page component.

```xml
<link rel="manifest" href="/content/<projectName>/manifest.webmanifest" crossorigin="use-credentials"/>
```

The developer will also need to add the following link to the `customfooterlibs.html` file of your page component.

```xml
<script>
        // Check that service workers are supported
        if ('serviceWorker' in navigator) {
            // Use the window load event to keep the page load performant
            window.addEventListener('load', () => {
                let serviceWorker = '/<projectName>sw.js';
                navigator.serviceWorker.register(serviceWorker);
            });
        }
</script>
```

>[!NOTE]
>
>Future versions of the [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html?lang=en#core-components-introduction) will include these features automatically. However if you use custom components instead of the Core Components, these adjustments will always be required.
### Adjust Your Dispatcher {#adjust-dispatcher}

The PWA feature generates and uses `/content/<sitename>/manifest.webmanifest` files. By default, the dispatcher doesn't expose such files. To expose these files, the developer must add the following configuration to their project.

```text
File location: [project directory]/dispatcher/src/conf.dispatcher.d/filters/filters.any >
 
# Allow webmanifest files
/0102 { /type "allow" /extension "webmanifest" /path "/content/*/manifest" }
```

>[!NOTE]
>
>Future versions of the [AEM Project Archetype](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html?lang=en#developing) will include this configuration.

## Enabling PWA for Your Site {#enabling-pwa-for-your-site}

1. Log into AEM.
1. From the main menu, tap or click **Navigation** -&gt; **Sites**.
1. Select the Sites project and tap or click [**Properties**](/help/sites-cloud/authoring/fundamentals/page-properties.md) or use the hotkey `p`.
1. Select the **Progressive Web App** tab and configure the applicable properties. At a minimum you will want to:
   1. Select the option **Make this site installable as a PWA**.
   1. Define the **URL to load when user opens app**.

      ![Enable PWA](../assets/pwa-enable.png)

   1. Upload a 512x512 png icon to assets (DAM) and reference that as the icon for this app.

      ![Define PWA icon](../assets/pwa-icon.png)

   1. Configure the paths you want the service worker to take offline. Typical paths are:
      * `/content/<sitename>`
      * `/content/experiencefragements/<sitename>`
      * `/content/dam/<sitename>`
      * Any third party font references
      * `/etc/clientlibs/<sitename>`

      ![Define PWA offline paths](../assets/pwa-offline.png)

1. Tap or click **Save &amp; Close**.

Your site is now configured and you can [install it as a local app.](#using-pwa-enabled-site)

## Using Your PWA-Enabled Site {#using-pwa-enabled-site}

Now that you have configured your site to support PWA, you can experience for yourself.

1. Access the starting page in a [supported mobile browser.](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Installable_PWAs#Summary)
1. You will see a + icon on the address bar, indicating that the site can be installed as a local app.
   * Depending on the browser, it may also display a notification (such as a banner or dialog box) indicating that it's possible to install as a local app.
1. Install the app.
1. The app will be installed on the home screen of your device.
1. Open the app, browse a bit, and see that pages are available offline.

## Detailed Options {#detailed-options}

The following section provides more detail on the options available when configuring your site for PWA.

### Configure Installable Experience** {configure-installable-experience}

These settings allow your site behave like a native app by making it installable on the visitor's home screen and available offline.

* **Make this site installable as a PWA** - Main toggle to enable PWA for the site
* **URL to load when user opens app** - Content path that will open when the user loads the locally-installed app
  * This can be any path in your content structure.
  * This does not have to be the root and is usually a dedicated welcome page for the app.
* **Customize app experience** - The app is still an AEM site delivered through a browser. These options define how the browser should be hidden or otherwise presented to the user.
  * **Standalone** - The browser is completely hidden from the user and it appears like a native app. This is the default value.
  * **Browser** - The browser appears as it normally would when visiting the site.
  * **Minimal UI** - The browser is mostly hidden, like a native app, but basic navigation controls are exposed.
  * **Full Screen** - The browser is completely hidden, like a native app, but is rendered in full screen mode.
* **Screen orientation when opening the app**
  * **Any** - The app adjusts to the user's selected orientation. This is the default value.
  * **Portrait** - This forces the app to open in portrait layout regardless of the user's orientation of the device.
  * **Landscape** - This forces the app to open in landscape layout regardless of the user's orientation of the device.
* **Color of the toolbar** - This defines the color of the app toolbar.
* **Color of the splash screen** - This defines the color of the app splash screen, which is shown as the app loads.
  * Certain browsers [build a splash screen automatically](https://developer.mozilla.org/en-US/docs/Web/Manifest#Splash_screens) from the app name, background color, and icon.
  * The splash screen is not visible to the user on sufficiently fast devices.
* **Icon** - This defines the icon the represents the app on the user's device.
  * The icon must be a png file of size 512x512 pixels.
  * The icon must be [stored in DAM.](/help/assets/overview.md)

### Offline Configuration {#offline-configuration}

These settings make parts of this site available offline and available locally on your visitor's device.

* **How often does your content change?**
  * **Moderately** - This is the case for most sites and is the default value.
  * **Frequently** - This is the case for sites that need changes to be closer to real-time such as auction houses.
  * **Rarely** - This is the case for sites that are nearly static such as reference pages.
* **Files to pre-fetch** - These files will be cached immediately when the app is installed.
* **Paths to cache on first use** - These files will be cached whenever the user browsers to the page the first time in the app.
* **Cache exclusions** - These files will never be caches regardless of the settings under **Files to pre-fetch** and **Paths to cache on first use**.

## Limitations {#limitations}

* A user must browse the page at least once before it becomes cached offline.
* Pages are not automatically synched or updated if the suer is not using the app.
