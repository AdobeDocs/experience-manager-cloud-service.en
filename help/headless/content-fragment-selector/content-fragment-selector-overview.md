---
title: The Micro-Frontend Content Fragment Selector for Adobe Experience Manager as a Cloud Service
description: Use the Micro-Frontend Content Fragment Selector to search, find, and retrieve content fragments from your application.
role: Admin, User
---

# Micro-Frontend Content Fragment Selector {#micro-frontend-content-fragment-selector}

The Micro-Frontend Content Fragment Selector provides a user interface that easily integrates with the Adobe Experience Manager (AEM) as a Cloud Service repository. The interface allows you to browse or search Content Fragments in the repository, and use them in your application.

The Micro-Frontend user interface is made available in your application using the Content Fragment Selector package. Any updates to the package are automatically imported and loaded into your application.

![Micro-Frontend Content Fragment Selector - Overview](/help/headless/assets/content-fragment-selector-overview.png)

The Content Fragment Selector provides many benefits, such as:

* Ease of integration, with any of the Adobe, or non-Adobe, applications using the Vanilla JavaScript library.
* Easy to maintain, as updates to the Content Fragment Selector package are automatically deployed to the Content Fragment Selector available to your application. This means that your application does not need to take action to load the latest modifications.
* Ease of customization, using properties that control the Content Fragment Selector display within your application.
* Full-text search, together with customizable filters, allow the quick navigation of Content Fragments within the authoring experience.
* Ability to switch repositories within an IMS organization for Content Fragment selection.
* Ability to sort Content Fragments, and view them in List, Grid, Gallery, or Waterfall view.

<!--Perform the following tasks to integrate and use Asset Selector with your [!DNL Experience Manager Assets] repository:

1. [Install Asset Selector](#installation)
2. [Integrate Asset Selector using Vanilla JS](#integration-using-vanilla-js)
3. [Use Asset Selector](#using-asset-selector)
-->

<!--
## Setting up Asset Selector {#asset-selector-setup}

![Asset Selector set up](assets/asset-selector-prereqs.png)
-->

## Prerequisites {#prerequisites}

### IMS Authentication {#ims-authentication}

If you require the IMS authentication workflow you must ensure that:

* The application is running on `HTTPS`.
* The URL of the application is in the list of allowed redirect URLs for the IMS client.
* The IMS login flow is configured and rendered using a popup on the web browser. Therefore, popups should be enabled or allowed on the target browser.

Alternatively, if your application is already authenticated with the IMS workflow, you can add the appropriate IMS information instead. 

<!--
For further information see:

* [Integrate the Content Fragment Selector with an Adobe app](/help/assets/integrate-asset-selector-adobe-app.md)
* [Integrate the Content Fragment Selector with a non-Adobe app](/help/assets/integrate-asset-selector-non-adobe-app.md)
-->

### Provisioning {#provisioning}

Before attempting to install or use the Content Fragment Selector, you must ensure that your organization has been provisioned for access to the Content Fragment Selector as part of the Experience Manager as a Cloud Service profile. 

If your organization has not been provisioned, you cannot integrate or use these components. 

>[!NOTE] 
>
>To request provisioning, your program administrator should raise a support ticket marked as `P2` from the Admin Console and include the following information:
>
>* Domain names: where the integrating application is hosted.

After provisioning, your organization will be provided with the following properties for your environment:

* `imsClientId`
* `imsScope`
* `redirectUrl` 

>[!IMPORTANT]
>
>Without these properties, you cannot run the installation steps.

<!-- -->

## Installation {#installation}

The Content Fragment Selector is available via both:

* [UMD](https://github.com/umdjs/umd) version (recommended)
* ESM CDN; for example, [esm.sh](https://esm.sh/) and [skypack](https://www.skypack.dev/) 

For example:

* In browsers using **UMD version** (recommended):

  ```html
  <script src="https://experience.adobe.com/solutions/CQ-content-fragments-selectors/static-content-fragments/resources/content-fragments-selectors.js"></script>

  <script>
    const { renderContentFragmentSelector } = PureJSSelectors;
  </script>
  ```

* In browsers with `import maps` support using **ESM CDN version**:

  ```html
  <script type="module">
    import { ContentFragmentSelector } from 'https://experience.adobe.com/solutions/CQ-content-fragments-selectors/static-content-fragments/resources/@content-fragments/selectors/index.js'
  </script>
  ```

* In Deno/Webpack Module Federation using **ESM CDN version**:

  ```html
  import { ContentFragmentSelector } from 'https://experience.adobe.com/solutions/CQ-content-fragments-selectors/static-content-fragments/resources/@content-fragments/selectors/index.js'
  ```

## Using the Content Fragment Selector {#using-the-Content-Fragment-selector}

Once the Content Fragment Selector is set up and authenticated to use the Content Fragment Selector with your AEM as a Cloud Service application, you can select Content Fragments or perform various other operations to search for your fragments in the repository.

<!-- SCREENSHOT -->

   ![using-content-fragment-selector](assets/using-content-fragment-selector.png)

* **1**: [Hide/Show panel](#hide-show-panel)
* **2**: [Repository switcher](#repository-switcher)
* **3**: [Content Fragments](#content-fragments-repository)
* **4**: [Filters](#out-of-the-box-filters)
* **5**: [Search bar](#custom-search)
* **6**: [Search bar](#search-bar)
* **7**: [Sorting](#sorting)
* **8**: [Sorting in ascending or descending order](#sorting)
* **9**: [View](#types-of-view)

### Hide/Show panel {#hide-show-panel}

To hide folders in the left navigation, click the **Hide folders** icon. To undo the changes, click the **Hide folders** icon again.

### Repository switcher {#repository-switcher}

The Content Fragment Selector lets you select a repository for fragment selection. 

You can select the repository of your choice from the drop-down available in the left panel. The repository options available in the drop-down list are based on the `repositoryId` property defined in the `index.html` file. This property is based on the environment from the selected IMS org accessed by the user currently logged in. 

Consumers can pass a preferred `repositoryID` to render fragments from a specific repository, and stop rendering the repository switcher.

### Content Fragments repository {#content-fragments-repository}

The Content Fragments repository is a collection of Content Fragment folders that you can use to perform operations. 

### Out-of-the-box filters {#out-of-the-box-filters}

The Content Fragment Selector also provides out-of-the-box filter options to refine your search results. The following filters are available:

* **Status**: the current state of the fragment; `all`, `published`, `unpublished`, or `no status`

<!-- SCREENSHOT -->

![rail-view-example](assets/filters-asset-selector.png) 

### Custom search {#custom-search}

In addition to the full-text search, the Content Fragment Selector lets you search the content within fragments using customized search. You can use custom search filters in both Modal view and Rail view modes.

<!-- SCREENSHOT -->

![custom-search](assets/custom-search1.png)

You can also create a default search filter to save the for future use. To create custom search filtersfor your Content Fragments, you can use `filterSchema` property.

### Search bar {#search-bar}

The Content Fragment Selector lets you perform a full text search of fragments within the selected repository. For example, if you type the keyword `wave` in the search bar, all the fragments with the `wave` keyword mentioned in any of the metadata properties are displayed.

### Sorting {#sorting}

You can sort fragments in the Content Fragment Selector by various properties. You can also sort the fragments in ascending or descending order.

### Types of view {#types-of-view}

Content Fragment Selector lets you view the fragment in four different views:

* ![list view](/help/headless/assets/list-view.png) **List View** The list view displays scrollable files and folders in a single column.
* ![grid view](/help/headless/assets/grid-view.png) **Grid View** The grid view displays scrollable files and folders in a grid of rows and columns.
* ![gallery view](/help/headless/assets/gallery-view.png) **Gallery View** The gallery view displays files or folders in a center-locked horizontal list.
* ![waterfall view](/help/headless/assets/waterfall-view.png) **Waterfall** View The waterfall view displays files or folders in the form of a Bridge.
