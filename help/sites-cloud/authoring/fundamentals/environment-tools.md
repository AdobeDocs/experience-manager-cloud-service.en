---
title: Authoring Environment and Tools
description: The authoring environment of AEM provides various mechanisms for organizing and editing your content
---

# Authoring Environment and Tools {#authoring-the-environment-and-tools}

The authoring environment of AEM provides various mechanisms for organizing and editing your content. The tools provided are accessed from the various consoles and page editors.

## Managing your Site {#managing-your-site}

The **Sites** console allows you to navigate and manage your website, using the header bar, toolbar, action icons (applicable for the selected resource), breadcrumbs, and, when selected, secondary rails (for example, timeline and references).

For example, column view:

![Column view](/help/sites-cloud/authoring/assets/column-view.png)

## Editing Page Content {#editing-page-content}

You can edit a page with the page editor. For example:

`http://<host>:<port>/editor.html/content/wknd/en/sports/la-skateparks.html`

![Page Editor](/help/sites-cloud/authoring/assets/page-editor.png)

>[!NOTE]
>
>The first time you open a page for editing, a series of slides will provide you with a tour of the features.
>
>You can skip the tour if wanted and repeat it at any time by selecting from the **Page Information** menu.

## Accessing Help {#accessing-help}

When editing a page, **Help** can be accessed from:

* The [**Page Information**](/help/sites-cloud/authoring/fundamentals/page-properties.md#page-properties) selector which shows the introductory slides (as shown the first time you access the editor)
* The [configuration](/help/sites-cloud/authoring/fundamentals/editing-content.md#component-toolbar) dialog for specific components (using the ? icon in the dialog toolbar), which shows context sensitive help

Further [help-related resources are available from consoles](/help/sites-cloud/authoring/getting-started/basic-handling.md#accessing-help).

## Components Browser {#components-browser}

Components are the building blocks of AEM content. You place multiple components on a page and configure their options in order to build your content page with AEM.

The components browser shows all components that are available for use on your current page. These can be dragged to the appropriate location, then edited to add your content.

The components browser is a tab within the side panel (together with the [assets browser](#assets-browser) and [content tree](#content-tree)). To open (or close) the side panel use the icon at the top left of the toolbar:

![Side Panel toggle](/help/sites-cloud/authoring/assets/side-panel-toggle.png)

When you open the side panel it will slide open from the left side (select the **Components** tab if necessary). When open you can browse through all the components available for your page.

The actual appearance and handling is dependent on the device type you are using:

* **Mobile device (e.g. iPad)**

  The component browser completely covers the page being edited.

  To add a component to your page touch-and-hold the required component and move it towards the right - the component browser will close to show the page again - where you can position the component.

  ![Component Browser on mobile](/help/sites-cloud/authoring/assets/component-browser-mobile.png)

* **Desktop device**

  The component browser is opened at the left side of the window.

  To add a component to your page click on the required component and drag it to the required location.

  ![Component Browser on desktop](/help/sites-cloud/authoring/assets/component-browser-desktop.png)

  Components are represented by

  * Component name
  * Component group (in gray)
  * Icon or abbreviation
    * Standard components' icons are monochrome.
    * Abbreviations are always the first two characters of the component name.

  From the top toolbar in the **Components** browser you can:

  * Filter components by name.
  * Limit the display to a specific group using the drop down selection.

  For a more detailed description of the component, you can click or tap the information icon next to the component in the **Components** browser (if available). For example, for the **Content Fragment**:

  ![Component Browser information](/help/sites-cloud/authoring/assets/component-browser-information.png)

  For even more information about the components available to you see the [Component Console](/help/sites-cloud/authoring/features/components-console.md).

>[!NOTE]
>
>A mobile device is detected when the width is less than 1024px. This can also be the case for a small desktop window.

## Assets Browser {#assets-browser}

The assets browser shows all [assets](/help/assets/home.md) that are available for direct use on your current page.

The assets browser is a tab within the side panel along with the [components browser](#components-browser) and [content tree](#content-tree). To open or close the side panel use the icon at the top left of the toolbar:

![Side Panel toggle](/help/sites-cloud/authoring/assets/side-panel-toggle.png)

When you open the side panel it will slide open from the left side. Select the **Assets** tab if necessary.

![Assets Browser button](/help/sites-cloud/authoring/assets/assets-browser-button.png)

When the assets browser is open you can browse through all the assets available for your page. Infinite scrolling is used to expand the list when required.

![Assets Browser](/help/sites-cloud/authoring/assets/assets-browser.png)

To add an asset to your page, select and drag to the required location. This can be:

* An existing component of the appropriate type.
  * For example, you can drag an asset of type image onto an Image component.
* A [placeholder](/help/sites-cloud/authoring/fundamentals/editing-content.md#component-placeholder) in the paragraph system to create a new component of the appropriate type.
  * For example, you can drag an asset of type image onto the paragraph system to create an Image component.

>[!NOTE]
>
>This is available for specific assets and component types. See [Inserting a Component using the Assets Browser](/help/sites-cloud/authoring/fundamentals/editing-content.md#inserting-a-component-using-the-assets-browser) for more details.

From the top toolbar of the assets browser you can filter the assets by:

* Name
* Path
* Asset type such as images, videos, documents, paragraphs, Content Fragments, and Experience Fragments
* Asset characteristics such as orientation and style
  * Available only for certain asset types

The actual appearance and handling is dependent on the device type you are using:

* **Mobile Device**

  The assets browser completely covers the page being edited.

  To add an asset to your page touch-and-hold the required asset, then move it towards the right - the assets browser will close to show the page again, where you can add the asset to the required component.

  ![Assets Browser on mobile](/help/sites-cloud/authoring/assets/assets-browser-mobile.png)

* **Desktop Device**

  The assets browser is opened at the left side of the window.

  To add an asset to your page click on the required asset and drag it to the required component or location.

  ![Assets Browser on desktop](/help/sites-cloud/authoring/assets/assets-browser-desktop.png)

>[!NOTE]
>
>A mobile device is detected when the width is less than 1024px; i.e. also on a small desktop window.

If you need to quickly make a change to an asset, you can start the [asset editor](/help/assets/manage-digital-assets.md) directly from the asset browser by clicking the edit icon shown next to the asset's name.

![Asset edit button](/help/sites-cloud/authoring/assets/asset-edit-button.png)

## Content Tree {#content-tree}

The **Content Tree** gives an overview of all of the components on the page in a hierarchy so you can see at a glance how the page is composed.

The Content Tree is a tab within the side panel (together with the components and assets browser). To open (or close) the side panel use the icon at the top left of the toolbar:

![Content Tree button](/help/sites-cloud/authoring/assets/content-tree-button.png)

When you open the side panel it will slide open (from the left side). Select the **Content Tree** tab if necessary. When open you can see a tree view representation of your page or template, so that it's easier to understand how its content is structured hierarchically. Additionally on a complex page, it makes it easier to jump between components of the page.

![Content Tree](/help/sites-cloud/authoring/assets/content-tree-editor.png)

A page can easily be composed of many of the same type of components, so the content (component) tree displays descriptive text (in gray) after the name of the component type (in black). The descriptive text comes from common properties of the component such as title or text.

Component types will be shown in the user language, whereas the component description text comes from the page language.

Clicking the chevron next to a component will collapse or expand that level.

![Content Tree chevron expansion](/help/sites-cloud/authoring/assets/content-tree-chevron.png)

Clicking on the component will highlight the component in the page editor. The actions available will depend on the page state:

* For example, a basic page:
  
  ![Content Tree highlighted](/help/sites-cloud/authoring/assets/content-tree-highlighted.png)

  The components of a basic page will have the usual options.
  
  If the component you click in the tree is editable a wrench icon will appear to the right of the name. Clicking on this icon will directly start the edit dialogue for the component.

  ![Content Tree edit button](/help/sites-cloud/authoring/assets/content-tree-edit.png)

* A page that is part of a [livecopy](/help/sites-cloud/administering/msm/overview.md), where components are inherited from another page.

>[!NOTE]
>
>The Content Tree is not available if you are editing a page on a mobile device (if the browser width is less than 1024px).

## Fragments - Associated Content Browser {#fragments-associated-content-browser}

If your page contains Content Fragments then you will also have access to the [browser for Associated Content](/help/sites-cloud/authoring/fundamentals/content-fragments.md#using-associated-content).

## References {#references}

**References** shows connections to the selected page:

* Blueprints
* Launches
* Live copies
* Language copies
* Incoming Links
* Use of the reference component: borrowed and lent content

Open the required console, then navigate to the required resource and open **References** using:

![References option](/help/sites-cloud/authoring/assets/references.png)

[Select your required resource](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources) to show a list of references types relevant to that resource:

![References details](/help/sites-cloud/authoring/assets/references-detail.png)

Select the appropriate reference type for more information. In certain situations further actions are available when you select a specific reference, including:

* **Incoming Links**, provides a list of pages that reference the page, together with direct access to **Edit** one of those pages when you select a specific link
* Instances of borrowed and lent content using the **Reference** component, from here you can navigate to the referencing/referenced page
* [Launches](/help/sites-cloud/authoring/launches/overview.md), provides access to related launches
* [Live Copies](/help/sites-cloud/administering/msm/overview.md) displays the paths of all live copies that are based on the selected resource.
* [Blueprint](/help/sites-cloud/administering/msm/best-practices.md), provides details and various actions
* [Languages Copies](/help/sites-cloud/administering/translation/managing-projects.md#creating-translation-projects-using-the-references-panel), provides details and various actions

## Events - Timeline {#events-timeline}

For appropriate resources (e.g. pages from the **Sites** console, or assets from the **Assets** console) the [timeline can be used to show the recent activity on any selected items](/help/sites-cloud/authoring/getting-started/basic-handling.md#timeline).

Open the required console, then navigate to the required resource and open **Timeline**, using:

![Timeline option](/help/sites-cloud/authoring/assets/timeline.png)

[Select your required resource](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources), then either **Show All** or **Activities** to list any recent actions on the selected resources:

![Timeline details](/help/sites-cloud/authoring/assets/timeline-detail.png)

## Page Information {#page-information}

The Page Information (equalizer icon) opens a menu that also provides details about the last edit and the last publication. Depending on the characteristics of the page, its site, and your instance, more or fewer options might be available:

![Page Information option](/help/sites-cloud/authoring/assets/page-information.png)

* [Open Properties](/help/sites-cloud/authoring/fundamentals/page-properties.md)
* [Rollout Page](/help/sites-cloud/administering/msm/overview.md#msm-from-the-ui)
* [Start Workflow](/help/sites-cloud/authoring/workflows/applying.md#starting-a-workflow-from-the-page-editor)
* [Lock Page](/help/sites-cloud/authoring/fundamentals/editing-content.md#locking-a-page)
* [Publish Page](/help/sites-cloud/authoring/fundamentals/publishing-pages.md#publishing-pages-1)
* [Unpublish Page](/help/sites-cloud/authoring/fundamentals/publishing-pages.md#unpublishing-pages)
* [Edit Template](/help/sites-cloud/authoring/features/templates.md)
* [View as Published](/help/sites-cloud/authoring/fundamentals/editing-content.md#view-as-published)
* [View in Admin](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources)
* [Help](/help/sites-cloud/authoring/getting-started/basic-handling.md#accessing-help)
* [Promote Launch](/help/sites-cloud/authoring/launches/promoting.md) (only if the page is a launch)

In addition, **Page Information** can provide access to analytics and recommendations, when appropriate.

## Page Modes {#page-modes}

There are various modes when editing a page allowing for different actions:

* [Edit](/help/sites-cloud/authoring/fundamentals/editing-content.md) - the mode to use when editing the page content.
* [Layout](/help/sites-cloud/authoring/features/responsive-layout.md) - allows you to create and edit your responsive layout dependent on device (if the page is based on a layout container)
* [Targeting](/help/sites-cloud/authoring/personalization/targeted-content.md) - increase content relevance through targeting and measuring across all channels.
* [Timewarp](/help/sites-cloud/authoring/features/page-versions.md#timewarp) - allows you to view a pages state at a particular point in time.
* [Live Copy Status](/help/sites-cloud/authoring/fundamentals/editing-content.md#live-copy-status) - allows a quick overview of the live copy status and which components are/are not inherited.
* [Preview](/help/sites-cloud/authoring/fundamentals/editing-content.md#previewing-pages) - used to view the page as it will be shown on the publish environment; or to navigate using links in the content.
* [Annotate](/help/sites-cloud/authoring/fundamentals/annotations.md) - used to add or view annotations on the page.

You can access these using the icons in the top right corner. The actual icon will change to reflect the mode you are currently using:

![Page modes](/help/sites-cloud/authoring/assets/page-modes.png)

>[!NOTE]
>
>* Depending on the characteristics of the page, some modes my not be available.
>* Access to some modes require the appropriate permissions/privileges.
>* Developer mode is not available on mobile devices due to space restrictions.
>* There is a [keyboard shortcut](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) ( `Ctrl-Shift-M`) to toggle between **Preview** and the currently selected mode (e.g. **Edit**, **Layout**, etc).
>

## Path Selection {#path-selection}

Often when authoring it is necessary to select another resource such as when defining a link to another page or resource or selecting an image. To easily select a path, [path fields](#path-fields) offer auto-complete and the [path browser](#path-browser) allows for more robust selection.

### Path Fields {#path-fields}

The example used here to illustrate is the image component. For more information about using and editing components see [Components for Page Authoring](/help/sites-cloud/authoring/fundamentals/components.md).

Path fields have auto-complete and look-ahead functionality now to make locating a resource easier.

Clicking the **Open Selection Dialog** button in the path field opens the [path browser](#path-browser) dialog to allow for more detailed selection options.

![Open Selection Dialog button](/help/sites-cloud/authoring/assets/open-selection-dialog-button.png)

Alternatively you can start typing in the path field and AEM will offer matching paths as you type.

![Open Selection Dialog button](/help/sites-cloud/authoring/assets/path-selection-completion.png)

### Path Browser {#path-browser}

The path browser is organized like the [column view](/help/sites-cloud/authoring/getting-started/basic-handling.md#column-view) of the sites console, allowing for more detailed selection of resources.

![Path Browser](/help/sites-cloud/authoring/assets/path-browser.png)

* Once a resource is selected, the **Select** button at the upper-right of the dialogue becomes active. Click or tap to confirm the selection or **Cancel** to abort.
* If the context allows for the selection of multiple resources, selecting a resource also activates the **Select** button, but also adds a count of the number of selected resources to the upper-right of the window. Click the **X** next to the number to deselect all.
* When you navigate through the tree, your location is reflected in the breadcrumbs at the top of the dialog. These breadcrumbs can also be used to quickly jump within the resource hierarchy.
* At any time you can use the search field at the top of the dialogue. Click the **X** in the search field to clear the search.
* To narrow your search, you can reveal the filter options and filter your results based on a certain path.

  ![Filters option](/help/sites-cloud/authoring/assets/filters-option.png)

## Keyboard Shortcuts {#keyboard-shortcuts}

Various [keyboard shortcuts](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) are available.
