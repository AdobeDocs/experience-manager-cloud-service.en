---
title: Page Properties
description: Learn about the different properties a page can have and how they control the behavior of the page and how it is managed.
exl-id: 27521a6d-c6e9-4f43-9ddf-9165b0316084
solution: Experience Manager Sites
feature: Authoring
role: User
mini-toc-levels: 2
---

# Page Properties {#page-properties}

Learn about the different properties a page can have and how they control the behavior of the page and how it is managed.

>[!TIP]
>
>For details on how you can edit and change the properties of a page, please see the document [Editing Page Properties.](/help/sites-cloud/authoring/sites-console/edit-page-properties.md)

## Overview and Property Availability {#overview}

Page properties can control many aspects of a page from the page's title and branding to its permissions. The properties are distributed across several tabs, some of which may be hidden depending on the type of page. Like most properties in AEM, [page properties can be inherited.](/help/sites-cloud/authoring/sites-console/edit-page-properties.md#inheritance)

>[!NOTE]
>
>This document describes all possible page properties. Depending on the type of page, not all properties will be available.

## Basic Tab {#basic}

### Title &amp; Tags {#title-tags}

* **Title** - Defines the page meta title for SEO purposes as well as the title displayed in the page content (unless overridden)
  * The title of the page is shown in various locations in the AEM UI including the **Sites** card/list views in the [Sites Console.](/help/sites-cloud/authoring/sites-console/introduction.md)
  * This is a mandatory field.
* **Tags** - Defines the page meta tags for SEO purposes
  * You can add or remove tags from the page by updating the list in the selection box.
   * Use the drop-down to select from existing tags.
   * After selecting a tag is it listed below the selection box. You can remove a tag from this list using the x.
  * A completely new tag can be entered by typing the name in an empty selection box.
    * The new tag is created when you press enter.
    * The new tag will then be shown with a small star on the right indicating that it is a new tag.
  * An x appears when you mouse-over a tag entry in the selection box, which can be used to remove that tag for this page.
  * For more information about tags, see [Using Tag.](/help/sites-cloud/authoring/sites-console/tags.md)
* **Hide in Navigation** - Indicates whether the page is shown or hidden in the page navigation of the resulting site

### Branding {#branding}

Apply a consistent brand identity across pages by appending a brand slug to each page title. This functionality requires use of the Page Component from release 2.14.0 or later of the [Core Components.](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html)

* **Brand Slug** 
  * **Override** - Check to define the brand slug on this page.
    * The value is inherited by any child pages unless they also have their **Override** values set.
  * **Override value** - The text of the brand slug to be appended to the page title.
    * The value is appended to the page title after a pipe character such as `Cycling Tuscany | Always ready for the WKND`

### HTML ID {#html-id}

* **ID** - HTML ID to apply to the component.

### More Titles and Description {#more-titles}

* **Page Title** - A title to be used on the page
  * This is typically used by title components.
  * If empty, the **Title** is used.
* **Navigation Title** - You can specify a separate title for use in the navigation (for example, if you want something more concise).
  * If empty, the **Page Title** is used.
* **Subtitle** - A subtitle for use on the page
* **Description** - Your description of the page, its purpose, or any other details you want to add

### On/Off Time {#on-off-time}

* **On Time** - The date and time at which the published page is made visible (rendered) on the publish environment. The page must be published, either manually or by pre-configured auto-replication.

  * If already [published (manually)](/help/sites-cloud/authoring/sites-console/publishing-pages.md) this page is kept dormant (hidden) until rendering at the specified time.
  * If not published, and configured for auto-replication, the page is automatically published, then rendered, at the ecified time.
  * If not published, and not configured for auto-replication, the page is not automatically published, so a 404 is seen when an attempt to access the page is made.
  
* **Off Time** - Similar to and often used in combination with **On Time**, this defines the time at which the published page is hidden on the publish environment.

Leave these fields (**On Time** and **Off Time**) empty for pages you want to publish immediately and have available on the publish environment until they are deactivated (the normal scenario).

>[!NOTE]
>
> See [On and Off Times - Trigger Configuration](/help/operations/replication.md#on-and-off-times-trigger-configuration) for details of how to configure the related automatic replication.

>[!NOTE]
>If either the **On Time** or **Off Time** is in the past, and automatic replication is configured, then the relevant action is triggered immediately.

### Vanity URL {#vanity-url}

This property lets you enter a vanity URL for this page, which can allow you to have a shorter and/or more expressive URL. For example, if the Vanity URL is set to `welcome` to the page identified by the path `/v1.0/startpage` for the website `http://example.com`, then `http://example.com/welcome` would be the vanity URL of `http://example.com/content/v1.0/startpage`
  
>[!CAUTION]
>
>Vanity URLs:
>
>* Must be unique.
>* Do not support regex patterns.
>* Should not be set to an existing page.

* **Add** - Select to show a field to define a vanity URL for the page.
  * Select again to add multiple.
  * Select the **Remove** icon to delete the vanity URL.
* **Redirect Vanity URL** - Indicates whether you want the page to use the vanity URL or redirect to the page's actual URL

## Advanced {#advanced}

### Settings {#settings}

* **Language** - The page language
* **Language Root** - Must be checked if the page is the root of a language copy
* **Redirect** - Indicates the page to which this page should automatically redirect with an HTML `302 Found` status
  * **Permanent Redirect** - When checked, the page redirects to the target path provided along with an HTML `301 Moved Permanently` status.
* **Design**
* **Alias** - Specifies an alias to be used with this page
  * For example, if you define an alias of `private` for the page `/content/wknd/us/en/magazine/members-only`, then this page can also be accessed via `/content/wknd/us/en/magazine/private`
  * Creating an alias sets the `sling:alias` property on the page node, which only impacts the resource, not the repository path.
  * Pages accessed by aliases in the editor cannot be published. [Publish options](/help/sites-cloud/authoring/sites-console/publishing-pages.md) in the editor are only available for pages accessed via their actual paths. 
  * See [Localized page names under SEO and URL Management Best Practices](/help/overview/seo-and-url-management.md#localized-page-names) for more information.

### Configuration {#configuration}

* **Inherited from &lt;path&gt;** - Enable/disable inheritance of the **Cloud Configuration** for the page
  * Toggles availability of **Cloud Configuration** for editing

* **Cloud Configuration** - The path to the selected configuration

### Template Settings {#template-settings}

* **Allowed Templates** - [Defines the list of templates that are available](/help/sites-cloud/authoring/page-editor/templates.md#enabling-and-allowing-a-template-template-author) within this sub-branch
  * Each value must be an absolute path to a template.
  * Use `/.*` to allow all templates below this path.
* **Use Page as Template** - [Create a new template based on the current page.](/help/sites-cloud/authoring/universal-editor/templates.md)
  * Only applies to pages created for use with the Universal Editor leveraging Edge Delivery Services.

### Authentication Requirement {#authentication}

* **Enable** - Enables use of authentication to access the page

>[!NOTE]
>
>Closed user groups for the page are defined on the **[Permissions](#permissions)** tab.

* **Login Page** - The page to be used for login

### Export {#export}

* **Export Configuration** - Specifies an export configuration

## SEO {#seo}

* **Canonical Url** - Used to overwrite the page's canonical URL
  * If left blank the page's URL is its canonical URL.

* **Robots Tags** - Use the dropdown to select the robots tags to control the behavior of search engine crawlers
  * Some options conflict with each other, in which case the more permissive option take precedence.

* **Generate Sitemap** - When selected, a `sitemap.xml` is generated for this page, and its descendants.

## Images {#images}

### Featured Image {#featured-image}

Select, and configure, the image to be featured. This is used in components referencing the page; for example, teasers, page lists, and so on.

* **Image**

  You can **Pick** an Asset, or browse for a file to upload, then **Edit**, or **Clear**.

* **Alternative Text** - a text used to represent the meaning and/or function of the image; for example, for use by screen readers.

* **Inherit - Value taken from the DAM asset** - when checked this will populate the alternative text with the value of the `dc:description`metadata in DAM

### Thumbnail {#thumbnail}

Configure the page thumbnail

* **Generate Preview** - Generate a preview of the page to use as thumbnail
* **Upload Image** - Upload an image to use as thumbnail
* **Select Image** - Select an existing Asset to use as the thumbnail
* **Revert** - This option becomes available after you have made a change to the thumbnail. If you do not want to keep your change, you can revert that change before saving.

## Cloud Services {#cloud-services}

* **Cloud Service Configurations** - Define properties for cloud services

## Personalization {#personalization}

### ContextHub Configurations {#contexthub-config}

* **Inherited from &lt;path&gt;** - enable/disable inheritance; toggles availability of **ContextHub Pathn** and **Segments Path** for selection

* **ContextHub Path** - Define the [ContextHub configuration](/help/sites-cloud/authoring/personalization/contexthub.md)
* **Segments Path** - Define the [Segments path](/help/sites-cloud/authoring/personalization/contexthub-segmentation.md)
  
### Targeting Configuration {#targeting-config}

* **Brand** - Defines a [Brand to specify a scope for Targeting](/help/sites-cloud/authoring/personalization/targeted-content.md).

>[!NOTE]
>This option requires the user account to be in the `Target Administrators`group.

## Permissions {#permissions}

* **Permissions**

  * **Add Permissions**
  * **Edit Closed User Group**
  * View the **Effective Permissions**
    
## Blueprint {#blueprint}

This tab is only visible for pages that serve as blueprints. Blueprints serve as the basis for Live Copies, and are part of [Multi Site Management](/help/sites-cloud/administering/msm/overview.md).

* **Current Live Copies** - Lists pages that are based on (that is, are Live Copies of) this blueprint page

* **Rollout Configs** - Controls the circumstances under which modifications are propagated to the Live Copy

## Live Copy {#live-copy}

This tab is only visible for pages that are configured as live copies. As with Blueprints, Live Copies are part of [Multi Site Management](/help/sites-cloud/administering/msm/overview.md).

* **Synchronize** - Synchronize Live Copy with Blueprint, keeping local modifications
* **Reset** - Reset Live Copy to state of Blueprint, removing local modifications
* **Suspend** - Suspend Live Copy from further rollout modifications
* **Detach** - Detach Live Copy from Blueprint

### Source {#source}

* Displays the path of the blueprint for this Live Copy

### Status {#status}

* Lists current Live Copy status of the page

### Configuration {#live-copy-config}

* **Live Copy Inheritance** - If checked, Live Copy configuration is effective on all children
* **Inherit Rollout Configs from Parent** - If checked, the rollout configuration is inherited from the parent of the page
* **Choose Rollout Config** - Defines the circumstances under which modifications are propagated from the Blueprint and only available when **Inherit Rollout Configs from Parent** is not selected

## Preview {#preview}

When a Preview environment is enabled you see the following:

* Preview URL - the URL used for accessing the content on the Preview environment

## Progressive Web App {#progressive-web-app}

Through a simple configuration, a content author can now enable progressive web app (PWA) features for experiences created in AEM Sites.

>[!NOTE]
>
>See [Enabling Progressive Web App Features](/help/sites-cloud/authoring/sites-console/enable-pwa.md) for more details.

{{pwa-deprecation}}

### Configure installable experience {#config-pwa}

* **Enable PWA** - enable/disable the feature; allows users to install the site as a PWA
* **StartupURL** - the preferred startup Url
* **Display Mode** - how the browser should be hidden or otherwise presented to the user on the local device
* **Screen orientation** - how the PWA will handle device orientations
* **Theme color** - the color of the app that affects how the local user's operating system displays the native UI toolbar and navigation controls
* **Background color** - the background color of the app, which is shown as the app loads
* **Icon** - the icon that represents the app on the user's device

### Cache management (Advanced) {#cache-management}

* **Caching strategy and frequency of content refresh** - defines the caching model for your PWA
* **Files to cache for offline use**
  * **File pre-caching (technical preview)** - files hosted on AEM are saved to the local browser cache when the service worker is installing and before it is used
  * **Client-side Libraries** - client-side libraries to cache for offline experience
  * **Path inclusions** - network requests for the defined paths are intercepted and cached content is returned in accordance with the configured Caching strategy and frequency of content refresh
  * **Path exclusions** - these files will never be cached regardless of the settings under File pre-caching and Path inclusions
