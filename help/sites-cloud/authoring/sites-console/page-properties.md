---
title: Editing Page Properties
description: Learn how to define the properties required for managing a page in AEM.
exl-id: 27521a6d-c6e9-4f43-9ddf-9165b0316084
solution: Experience Manager Sites
feature: Authoring
role: User
---
# Editing Page Properties {#editing-page-properties}

You can define the required properties for a page. These can vary depending on the nature of the page. For example, some pages might be connected to a live copy while others are not and the live copy information is available as appropriate.

## Page Properties {#page-properties}

The properties are distributed across several tabs.

### Basic {#basic}

* **Title &amp; Tags**

  * **Title** - The title of the page is shown in various locations. For example, the **Websites** tab list and the **Sites** card/list views.
    * This is a mandatory field.
  * **Tags** - Here you can add, or remove tags from the page by updating the list in the selection box.
    * After selecting a tag is it listed below the selection box. You can remove a tag from this list using the x.
    * A completely new tag can be entered by typing the name in an empty selection box.
      * The new tag is created when you press enter.
      * The new tag will then be shown with a small star on the right indicating that it is a new tag.
    * With the drop-down functionality you can select from existing tags.
    * An x appears when you mouse-over a tag entry in the selection box, which can be used to remove that tag for this page.
    * For more information about tags, see [Using Tags](/help/sites-cloud/authoring/sites-console/tags.md).
  * **Hide in Navigation** - Indicates whether the page is shown or hidden in the page navigation of the resulting site.

* **Branding**

  Apply a consistent brand identity across pages by appending a brand slug to each page title. This functionality requires use of the Page Component from release 2.14.0 or later of the [Core Components.](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html)

  * **Brand Slug** 

    * **Override** - Check to define the brand slug on this page.
      * The value is inherited by any child pages unless they also have their **Override** values set.
    * **Override value** - The text of the brand slug to be appended to the page title.
      * The value is appended to the page title after a pipe character such as "Cycling Tuscany | Always ready for the WKND"

* **HTML ID**

  * **ID** - HTML ID to apply to the component.

* **More Titles and Description**

  * **Page Title** - A title to be used on the page. Typically used by title components. If empty, the **Title** is used.
  * **Navigation Title** - You can specify a separate title for use in the navigation (for example, if you want something more concise). If empty, the **Title** is used.
  * **Caption** - A subtitle for use on the page.
  * **Description** - Your description of the page, its purpose, or any other details you want to add.

* **On/Off Time**

  >[!NOTE]
  >
  > See [On and Off Times - Trigger Configuration](/help/operations/replication.md#on-and-off-times-trigger-configuration) for details of how to configure the related automatic replication.

  >[!NOTE]
  >If either the **On Time** or **Off Time** is in the past, and automatic replication is configured, then the relevant action is triggered immediately.

  * **On Time** - The date and time at which the published page is made visible (rendered) on the publish environment. The page must be published, either manually or by pre-configured auto-replication.

    * If already [published (manually)](/help/sites-cloud/authoring/sites-console/publishing-pages.md) this page is kept dormant (hidden) until rendering at the specified time.
    * If not published, and configured for auto-replication, the page is automatically published, then rendered, at the specified time.
    * If not published, and not configured for auto-replication, the page is not automatically published, so a 404 is seen when an attempt to access the page is made.
  
  * **Off Time** - Similar to and often used in combination with **On Time**, this defines the time at which the published page is hidden on the publish environment.

  * Leave these fields (**On Time** and **Off Time**) empty for pages you want to publish immediately and have available on the publish environment until they are deactivated (the normal scenario).

* **Vanity URL**

  * Lets you enter a vanity URL for this page, which can allow you to have a shorter and/or more expressive URL.
  * For example, if the Vanity URL is set to `welcome` to the page identified by the path `/v1.0/startpage` for the website `http://example.com`, then `http://example.com/welcome` would be the vanity URL of `http://example.com/content/v1.0/startpage`
  
  >[!CAUTION]
  >
  >Vanity URLs:
  >
  >* Must be unique so you should take care that the value is not already used by another page.
  >* Do not support regex patterns.
  >* Should not be set to an existing page.

  * **Add** - Select to show a field to define a vanity URL for the page.
    * Select again to add multiple.
    * Select the **Remove** icon to delete the vanity URL.
  * **Redirect Vanity URL** - Indicates whether you want the page to use the vanity URL.

### Advanced {#advanced}

* **Settings**

  * **Language** - The page language
  * **Language Root** - Must be checked if the page is the root of a language copy
  * **Redirect** - Indicates the page to which this page should automatically redirect with an HTML `302 Found` status. 
    * **Permanent Redirect** - When checked, the page redirects to the target path provided along with an HTML `301 Moved Permanently` status.
  * **Design** - Indicates whether the page is shown or hidden in the page navigation of the resulting site
  * **Alias** - Specifies an alias to be used with this page
    * For example, if you define an alias of `private` for the page `/content/wknd/us/en/magazine/members-only`, then this page can also be accessed via `/content/wknd/us/en/magazine/private`
    * Creating an alias sets the `sling:alias` property on the page node, which only impacts the resource, not the repository path.
    * Pages accessed by aliases in the editor cannot be published. [Publish options](/help/sites-cloud/authoring/sites-console/publishing-pages.md) in the editor are only available for pages accessed via their actual paths. 
    * See [Localized page names under SEO and URL Management Best Practices](/help/overview/seo-and-url-management.md#localized-page-names).

* **Configuration**

  * **Inherited from &lt;path&gt;** - enable/disable inheritance; toggles availability of **Cloud Configuration** for selection

  * **Cloud Configuration** - The path to the selected configuration

* **Template Settings**

  * **Allowed Templates** - [Defines the list of templates that are available](/help/sites-cloud/authoring/page-editor/templates.md#enabling-and-allowing-a-template-template-author) within this sub-branch

* **Authentication Requirement**

  * **Enable** - Enable use of authentication to access the page

    >[!NOTE]
    >
    >Closed user groups for the page are defined on the **[Permissions](#permissions)** tab.

  * **Login Page** - The page to be used for login

* **Export**

  * **Export Configuration** - Specifies an export configuration

* **SEO**

  * **Canonical Url** - can be used to overwrite the page's canonical Url; if left blank the page's Url is its canonical Url

  * **Robots Tags** - select the robots tags to control the behavior of search engine crawlers.

    >[!NOTE]
    >
    >Some of the options conflict with each other. In case of a conflict the more permissive option takes precedence.

  * **Generate Sitemap** - when selected, a sitemap.xml is generated for this page, and its descendants

### Images {#images}

* **Featured Image**

  Select, and configure, the image to be featured. This is used in components referencing the page; for example, teasers, page lists, and so on.

  * **Image**

    You can **Pick** an Asset, or browse for a file to upload, then **Edit**, or **Clear**.

  * **Alternative Text** - a text used to represent the meaning and/or function of the image; for example, for use by screen readers.

  * **Inherit - Value taken from the DAM asset** - when checked this will populate the alternative text with the value of the `dc:description`metadata in DAM

* **Thumbnail**

  Configure the page thumbnail

  * **Generate Preview** - Generate a preview of the page to use as thumbnail
  * **Upload Image** - Upload an image to use as thumbnail
  * **Select Image** - Select an existing Asset to use as the thumbnail
  * **Revert** - This option becomes available after you have made a change to the thumbnail. If you do not want to keep your change, you can revert that change before saving.

### Cloud Services {#cloud-services}

* **Cloud Service Configurations** - Define properties for cloud services

### Personalization {#personalization}

* **ContextHub Configurations**

  * **Inherited from &lt;path&gt;** - enable/disable inheritance; toggles availability of **ContextHub Pathn** and **Segments Path** for selection

  * **ContextHub Path** - Define the [ContextHub configuration](/help/sites-cloud/authoring/personalization/contexthub.md)
  * **Segments Path** - Define the [Segments path](/help/sites-cloud/authoring/personalization/contexthub-segmentation.md)
  
* **Targeting Configuration**

  * **Brand** - Defines a [Brand to specify a scope for Targeting](/help/sites-cloud/authoring/personalization/targeted-content.md).

  >[!NOTE]
  >This option requires the user account to be in the `Target Administrators`group.

### Permissions {#permissions}

* **Permissions**

  * **Add Permissions**
  * **Edit Closed User Group**
  * View the **Effective Permissions**
    
### Blueprint {#blueprint}

This tab is only visible for pages that serve as blueprints. Blueprints serve as the basis for Live Copies, and are part of [Multi Site Management](/help/sites-cloud/administering/msm/overview.md).

* **Current Live Copies** - Lists pages that are based on (that is, are Live Copies of) this blueprint page

* **Rollout Configs** - Controls the circumstances under which modifications are propagated to the Live Copy

### Live Copy {#live-copy}

This tab is only visible for pages that are configured as live copies. As with Blueprints, Live Copies are part of [Multi Site Management](/help/sites-cloud/administering/msm/overview.md).

* **Synchronize** - Synchronize Live Copy with Blueprint, keeping local modifications
* **Reset** - Reset Live Copy to state of Blueprint, removing local modifications
* **Suspend** - Suspend Live Copy from further rollout modifications
* **Detach** - Detach Live Copy from Blueprint

* **Source**

  * Displays the path of the blueprint for this Live Copy

* **Status**

  * Lists current Live Copy status of the page

* **Configuration**

  * **Live Copy Inheritance** - If checked, Live Copy configuration is effective on all children
  * **Inherit Rollout Configs from Parent** - If checked, the rollout configuration is inherited from the parent of the page
  * **Choose Rollout Config** - Defines the circumstances under which modifications are propagated from the Blueprint and only available when **Inherit Rollout Configs from Parent** is not selected

### Preview {#preview}

When a Preview environment is enabled you see the following:

* Preview URL - the URL used for accessing the content on the Preview environment

### Progressive Web App {#progressive-web-app}

Through a simple configuration, a content author can now enable progressive web app (PWA) features for experiences created in AEM Sites.

>[!NOTE]
>
>See [Enabling Progressive Web App Features](/help/sites-cloud/authoring/sites-console/enable-pwa.md).

* **Configure installable experience**

  * **Enable PWA** - enable/disable the feature; allows users to install the site as a PWA
  * **StartupURL** - the preferred startup Url
  * **Display Mode** - how the browser should be hidden or otherwise presented to the user on the local device
  * **Screen orientation** - how the PWA will handle device orientations
  * **Theme color** - the color of the app that affects how the local user's operating system displays the native UI toolbar and navigation controls
  * **Background color** - the background color of the app, which is shown as the app loads
  * **Icon** - the icon that represents the app on the user's device

* **Cache management (Advanced)**

  * **Caching strategy and frequency of content refresh** - defines the caching model for your PWA
  * **Files to cache for offline use**
    * **File pre-caching (technical preview)** - files hosted on AEM are saved to the local browser cache when the service worker is installing and before it is used
    * **Client-side Libraries** - client-side libraries to cache for offline experience
    * **Path inclusions** - network requests for the defined paths are intercepted and cached content is returned in accordance with the configured Caching strategy and frequency of content refresh
    * **Path exclusions** - these files will never be cached regardless of the settings under File pre-caching and Path inclusions

## Editing Page Properties {#editing-page-properties-1}

* From the **Sites** console:
  * [Creating a new page](/help/sites-cloud/authoring/sites-console/creating-pages.md#creating-a-new-page) (a subset of the properties)
  * Clicking or tapping **Properties**
    * For a single page
    * For multiple pages (only a subset of the properties are available for editing en masse)
* From the page editor:
  * Using **Page Information** (then **Open Properties**)

### From the Sites Console - Single Page {#from-the-sites-console-single-page}

Clicking or tapping **Properties** to define the page properties:

1. Using the **Sites** console, navigate to the location of the page for which you want to view and edit properties.
1. Select the **Properties** option for the required page using either:
   * [Quick actions](/help/sites-cloud/authoring/basic-handling.md#quick-actions)
   * [Selection mode](/help/sites-cloud/authoring/basic-handling.md#selecting-resources)
   * The page properties are shown using the appropriate tabs.
1. Either view or edit the properties as required.
1. Then use **Save** to save your updates followed by **Close** to return to the console.

### When Editing a Page {#when-editing-a-page}

When editing a page you can use **Page Information** to define the page properties:

1. Open the page for which you want to edit properties.
1. Select the **Page Information** icon to open the selection menu:
1. Select **Open Properties** and a dialog box opens that lets you edit the properties, sorted by the appropriate tab. The following buttons are also available at the right of the toolbar:
   * **Cancel**
   * **Save & Close**
1. Use the **Save & Close** button to save the changes.

### From the Sites Console - Multiple Pages {#from-the-sites-console-multiple-pages}

From the **Sites** console you can select several pages then use **View Properties** to view and/or edit the page properties. This is referred to as bulk editing of page properties.

You can select multiple pages for bulk editing by various methods, including:

* When browsing the **Sites** console
* After using **Search** to locate a set of pages

After selecting the pages and then clicking or tapping the **Properties option**, the bulk properties are shown:

![Bulk editing page properties](/help/sites-cloud/authoring/assets/page-properties-bulk-edit.png)

You can only bulk edit pages that:

* Share the same resource type
* Are not part of a livecopy
  * If any of the pages are in a live copy, then a message is shown when the properties are opened.

Once you have entered Bulk Editing you can:

* **View**

  * A list of the pages impacted
    * You can select/deselect if necessary
    * Tabs
      * As when viewing properties for a single page, the properties are ordered under tabs.
  * A subset of properties
    * Properties that are available on all selected pages and have been explicitly defined as available to bulk editing are visible.
    * If you reduce the page selection to one page, then all properties are visible.
  * Common properties with a common value
    * Only properties with a common value are shown in View mode.
    * When the field is multi-value (for example, Tags), values will only be shown when *all* are common. If only some are common, they will only be shown when editing.
    * When no properties with a common value exist, a message is displayed.

* **Edit**

  * You can update the values in the fields available.
    * The new values are applied to all selected pages when you select **Done**.
    * When the field is multi-value (for example, Tags), you can either append a new value or remove a common value.
  * Fields that are common, but have different values across the various pages are indicated with a special value such as the text `<Mixed Entries>`.
