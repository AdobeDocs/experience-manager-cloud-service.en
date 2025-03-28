---
title: Overlays for Adobe Experience Manager as a Cloud Service
description: AEM as a Cloud Service uses the principle of overlays to allow you to extend and customize the consoles and other functionality
exl-id: 24bdb1a9-6d77-43c7-a75e-28e6e0fd7608
feature: Developing
role: Admin, Architect, Developer
---
# Overlays in AEM as a Cloud Service {#overlays-in-aem}

Adobe Experience Manager as a Cloud Service uses the principle of overlays to allow you to extend and customize the consoles and other functionality (for example, page authoring).

Overlay is a term that can be used in many contexts. In this context, extending AEM as a Cloud Service, an overlay means to take the predefined functionality and impose your own definitions over it to customize the standard functionality.

In a standard instance, the predefined functionality is held under `/libs` and it is recommended practice to define your overlay (customizations) under the `/apps` branch (using a [search path](#search-paths) to resolve the resources). 

* The touch-enabled user interface uses [Granite](https://developer.adobe.com/experience-manager/reference-materials/6-5/granite-ui/api/jcr_root/libs/granite/ui/index.html)-related overlays:

    * Method

        * Reconstruct the appropriate `/libs` structure under `/apps`.

          This restructure does not require a 1:1 copy because the [Sling Resource Merger](/help/implementing/developing/introduction/sling-resource-merger.md) is used to cross-reference the original definitions that are required. The Sling Resource Merger provides services to access and merge resources with diff (differencing) mechanisms.

        * Under `/apps`, make changes.

    * Advantages

        * More robust to changes under `/libs`.
        * Only redefine what is required.

>[!CAUTION]
>
>The [Sling Resource Merger](/help/implementing/developing/introduction/sling-resource-merger.md) and the related methods can only be used with [Granite](https://developer.adobe.com/experience-manager/reference-materials/6-5/granite-ui/api/jcr_root/libs/granite/ui/index.html). This rule means that creating an overlay with a skeleton structure is only appropriate for the standard, touch-enabled user interface.

Overlays are the recommended method for many changes. For example, configuring your consoles, or creating your selection category to the asset browser in the side panel (used when authoring pages). They are required as:

* **In the `/libs` branch, *do not* make changes**
  Any changes you do make may be lost, because this branch is liable to changes whenever upgrades are applied to your instance.

* They concentrate your changes in one location, making it easier for you to track, migrate, back up, or debug your changes as necessary.

## Search Paths {#search-paths}

AEM uses a search path to find a resource, searching first &ndash; by default &ndash; the `/apps` branch and then the `/libs` branch. This mechanism means that your overlay in `/apps` (and the customizations defined there) has priority.

For overlays the resource delivered is an aggregate of the resources and properties retrieved, depending on search paths defined in the OSGi configuration.
