---
title: Asset Selector for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]
description: Use Asset selector to search, find, and retrieve assets' metadata and renditions within your application.
contentOwner: KK
role: Admin,User
exl-id: b968f63d-99df-4ec6-a9c9-ddb77610e258
---

# Micro-Frontend Asset Selector {#Overview}

Micro-Frontend Asset Selector provides a user interface that easily integrates with the [!DNL Experience Manager Assets] repository so that you can browse or search digital assets available in the repository and use them in your application authoring experience.

The Micro-Frontend user interface is made available in your application experience using the Asset Selector package. Any updates to the package are automatically imported and the latest deployed Asset Selector loads automatically within your application.

![Overview](assets/overview.png)

Asset Selector provides many benefits, such as:

* Ease of integration with any of the [Adobe](#asset-selector-ims) or [non-Adobe](#asset-selector-non-ims) applications using Vanilla JavaScript library.
* Easy to maintain as updates to the Assets Selector package are automatically deployed to the Asset Selector available for your application. There are no updates required within your application to load the latest modifications.
* Ease of customization as there are properties available that control the Asset Selector display within your application.
* Full-text search, out-of-the-box, and customized filters to quickly navigate to assets for use within the authoring experience.
* Ability to switch repositories within an IMS organization for asset selection.
* Ability to sort assets by name, dimensions, and size and view them in List, Grid, Gallery, or  Waterfall view.

Perform the following tasks to integrate and use Asset Selector with your [!DNL Experience Manager Assets] repository:

1. [Install Asset Selector](#installation)
2. [Integrate Asset Selector using Vanilla JS](#integration-using-vanilla-js)
3. [Use Asset Selector](#using-asset-selector)

<!--
Once the Asset Selector is integrated with [!DNL Adobe] or non-Adobe application, you can login using various means:
**Login flow for [!DNL Adobe] application:**
When Asset Selector is integrated with an [!DNL Adobe] application, you are taken directly to the Asset Selector environment where you can login using your IMS credentials.

**Login flow for non-Adobe application:**
You need a web browser, unified shell, and an app container to access Asset Selector with a non-Adobe (or third party) application. Once these are provided, you are taken to the Asset Selector environment where you can login using your IMS credentials.
-->

## Prerequisites {#prerequisites}

<!--
If your application requires user based authentication, out-of-the-box Asset Selector also supports a flow for authentication to the [!DNL Experience Manager Assets] repository using Identity Management System (IMS.)

You can use properties such as `imsScope` or `imsClientID` to retrieve `imsToken` automatically. You can use SUSI (Sign Up Sign In) flow and IMS properties. Also, you can obtain your own imsToken and pass it to Asset Selector by integrating within [!DNL Adobe] application on Unified Shell or if you already have an imsToken obtained via other methods (for example, using technical account). Accessing [!DNL Experience Manager Assets] repository without defining IMS properties (For example, `imsScope` and `imsClientID`) is referred to as a non-SUSI flow.
-->

Define the prerequisites in the `index.html` file or a similar file within your application implementation to define the authentication details to access the [!DNL Experience Manager Assets] repository.

Use the following prerequisites if you are integrating Asset Selector with an [!DNL Adobe] application:

* imsOrg
* imsToken
* apikey

Use the following prerequisites if you are integrating Asset Selector with a non-Adobe application:

* imsClientId
* imsScope
* redirectUrl
* imsOrg
* apikey

## Installation {#installation}

Asset Selector is available via both ESM CDN (For example, [esm.sh](https://esm.sh/)/[skypack](https://www.skypack.dev/)) and [UMD](https://github.com/umdjs/umd) version.

In browsers using **UMD version** (recommended):

```
<script src="https://experience.adobe.com/solutions/CQ-assets-selectors/static-assets/resources/assets-selectors.js"></script>

<script>
  const { renderAssetSelector } = PureJSSelectors;
</script>

```

In browsers with `import maps` support using **ESM CDN version**:

```
<script type="module">
  import { AssetSelector } from 'https://experience.adobe.com/solutions/CQ-assets-selectors/static-assets/resources/@assets/selectors/index.js'
</script>

```

In Deno/Webpack Module Federation using **ESM CDN version**:

```
import { AssetSelector } from 'https://experience.adobe.com/solutions/CQ-assets-selectors/static-assets/resources/@assets/selectors/index.js'

```

## Integrate Asset Selector using Vanilla JS {#integration-using-vanilla-js}

You can integrate any [!DNL Adobe] or non-Adobe application with [!DNL Experience Manager Assets] repository and select assets from within the application. 

The integration is done by importing the Asset Selector package and connecting to the Assets as a Cloud Service using the Vanilla JavaScript library. You need to edit an `index.html` or any appropriate file within your application to:

* Define the authentication details
* Access the Assets as a Cloud Service repository
* Configure the Asset Selector display properties

## Asset Selector properties {#asset-selector-properties}

You can use the Asset Selector properties to customize the way the Asset Selector is rendered. The following table lists the properties that you can use to customize and use the Asset Selector.

| Property | Type | Required | Default |Description |
|---|---|---|---|---|
| *rail*| boolean | No | false | If marked `true`, Asset Selector is rendered in a left rail view. If it is marked `false`, the Asset Selector is rendered in modal view. |
| *imsOrg*| string | Yes | | Adobe Identity Management System (IMS) ID that is assigned while provisioning [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] for your organization. The `imsOrg` key is required to authenticate whether the organization you are accessing is under Adobe IMS or not. |
| *imsToken* | string | No | | IMS bearer token used for authentication. `imsToken` is required if you are using an [!DNL Adobe] application for the integration. |
| *apiKey* | string | No | | API key used for accessing the AEM Discovery service. `apiKey` is required if you are using an [!DNL Adobe] application integration.|
| *rootPath* | string | No | /content/dam/ | Folder path from which Asset Selector displays your assets. `rootPath` can also be used in the form of encapsulation. For example, given the following path, `/content/dam/marketing/subfolder/`, Asset Selector does not allow you to traverse through any parent folder, but only displays the children folders. |
| *path* | string | No | | Path that is used to navigate to a specific directory of assets when the Asset Selector is rendered. |
| *filterSchema* | array | No | | Model that is used to configure filter properties. This is useful when you want to limit certain filter options in Asset Selector.|
| *filterFormProps*| Object | No | | Specify the filter properties that you need to use to refine your search. For example, MIME type JPG, PNG, GIF. |
| *selectedAssets* | Array `<Object>` | No       |                 | Specify selected Assets when the Asset Selector is rendered. An array of objects is required that contains an id property of the assets. For example, `[{id: 'urn:234}, {id: 'urn:555'}]` An asset must be available in the current directory. If you need to use a different directory, provide a value for the `path` property as well. |
| *acvConfig* | Object | No | | Asset Collection View property that contains object containing custom configuration to override defaults. |
| *i18nSymbols*            | `Object<{ id?: string, defaultMessage?: string, description?: string}>` | No       |                 | If the OOTB translations are insufficient for your application's needs, you can expose an interface through which you can pass your own custom localized values through the `i18nSymbols` prop. Passing a value through this interface overrides the default translations provided and instead use your own.  To perform the override, you must pass a valid [Message Descriptor](https://formatjs.io/docs/react-intl/api/#message-descriptor) object to the key of `i18nSymbols` that you want to override. |
| *intl* | Object | No  | | Asset Selector provides default, OOTB translations. You can select the translation language by providing a valid locale string through the `intl.locale` prop. For example: `intl={{ locale: "es-es" }}` </br></br> The locale strings supported follow the [ISO 639 - Codes](https://www.iso.org/iso-639-language-codes.html) for the representation of names of languages standards. </br></br> List of supported locales: English - 'en-us' (default) Spanish - 'es-es' German - 'de-de' French - 'fr-fr' Italian - 'it-it' Japanese - 'ja-jp' Korean - 'ko-kr' Portuguese - 'pt-br' Chinese (Traditional) - 'zh-cn' Chinese (Taiwan) - 'zh-tw' |
| *repositoryId* | string | No | ''| Repository from where the Asset Selector loads the content. |
| *additionalAemSolutions* | `Array<string>` | No | [ ] | It lets you add a list of additional AEM repositories. If no information is provided in this property, then only media library or AEM Assets repositories are considered.|
| *hideTreeNav*| boolean | No |  | Specifies whether to show or hide assets tree navigation sidebar. It is used in modal view only and hence there is no effect of this property in rail view. |
| *onDrop* | Function | No | | The property allows the drop functionality of an asset. |
| *dropOptions* | `{allowList?: Object}` | No | | Configures drop options using 'allowList'.  |
| *colorScheme* | string | No | | Configure theme (`light` or `dark`) for the Asset Selector. |
| *handleSelection* | Function | No | | Invoked with array of Asset items when assets are selected and the `Select` button on the modal is clicked. This function is only invoked in modal view. For rail view, use the `handleAssetSelection` or `onDrop` functions. Example: <pre>handleSelection=(assets: Asset[])=> {...}</pre> See [Selected Asset Type](#selected-asset-type) for details.|
| *handleAssetSelection*| Function | No | | Invoked with array of items as the assets are being selected or unselected. This is useful when you want to listen for assets as user selects them. Example: <pre>handleSelection=(assets: Asset[])=> {...}</pre> See [Selected Asset Type](#selected-asset-type) for details. |
| *onClose* | Function | No | | Invoked when `Close` button in modal view is pressed. This is only called in `modal` view and disregarded in `rail` view. |
| *onFilterSubmit* | Function | No | | Invoked with filter items as user changes different filter criteria. |
| *selectionType* | string | No | single | Configuration for `single` or `multiple` selection of assets at a time. |
| *dragOptions.allowList* | boolean | No | | The property is used to allow or deny the dragging of assets that are not selectable. |
| *aemTierType* | string | No | | It allows you to select whether you want to show assets from delivery tier, author tier, or both. |

## Examples to use Asset Selector properties {#usage-examples}

You can define the Asset Selector [properties](#asset-selector-properties) in the `index.html` file to customize the Asset Selector display within your application.

### Example 1: Asset Selector in rail view

   ![rail-view-example](assets/rail-view-example-vanilla.png)

If the value of the AssetSelector `rail` is set to `false` or is not mentioned in the properties, Asset Selector displays in the Modal view by default.

<!--
### Example 2: Use selectedAssets property in addition to the path property

Use the `path` property to define the folder name that displays automatically when the Asset Selector is rendered. In addition, use the `selectedAssets` property to define the IDs for the assets that you need to select within the folder. Moreover, when you want to display assets that are pre-defined within the folder, you can use selectedAssets property.

   ![selected-assets-example](assets/selected-assets-example-vanilla.png)
-->

### Example 2: Metadata popover

Use various properties to define metadata of an asset that you want to view using an info icon. The info popover provides the collection of information about asset or the folder including title, dimensions, date of modification, location, and description of an asset. In the example below, various properties are used to display metadata of an asset, for example, `repo:path` property specifies the location of an asset. <!--`repo` represents the repository from where the asset is showing, whereas, `path` represents the route from where the asset or folder is rendered.-->
    
   ![metadata-popover-example](assets/metadata-popover.png)

### Example 3: Custom filter property in rail view

In addition to the faceted search, Assets Selector lets you customize various attributes to refine your search from [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application. You need to add the following code to add customized search filters in your application. In the example below, the `Type Filter` search that filters the asset type among Images, Documents, or Videos or the filter type that you have added for the search.

![custom-filter-example-vanilla](assets/custom-filter-example-vanilla.png)

<!--

## Customization after integrating Asset Selector 

### Custom metadata

Assets display panel shows the out of the box metadata that can be displayed in the info of the asset. In addition to this, [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application allows configuration of the asset selector by adding custom metadata that is shown in info panel of the asset.
-->

## Using Asset Selector {#using-asset-selector}

Once the Asset Selector is set up and you are authenticated to use Asset Selector with your [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application, you can select assets or perform various other operations to search for your assets within the repository.

   ![using-asset-selector](assets/using-asset-selector.png)

* **A**: [Hide/Show panel](#hide-show-panel)
* **B**: [Repository switcher](#repository-switcher)
* **C**: [Assets](#repository)
* **D**: [Filters](#filters)
* **E**: [Search bar](#search-bar)
* **F**: [Sorting](#sorting)
* **G**: [Sorting in ascending or descending order](#sorting)
* **H**: [View](#types-of-view)

### Hide/Show panel {#hide-show-panel}

To hide folders in the left navigation, click **[!UICONTROL Hide folders]** icon. To undo the changes, click the **[!UICONTROL Hide folders]** icon again.

### Repository switcher {#repository-switcher}

Asset Selector also lets you switch repositories for asset selection. You can select the repository of your choice from the drop-down available in the left panel. The repository options available in the drop-down list are based on the `repositoryId` property defined in the `index.html` file. It is based on the environments from the selected IMS org that is accessed by the logged in user. Consumers can pass a preferred `repositoryID` and in that case the Asset Selector stops rendering the repo switcher and render assets from the given repository only.
<!--
It is based on the `imsOrg` that is provided in the application. If you want to see the list of repositories, then `repositoryId` is required to view those specific repositories in your application.
-->

### Assets repository

It is a collection of assets folders that you can use to perform operations. 

### Out-of-the-box filters {#filters}

Asset Selector also provides out-of-the-box filter options to refine your search results. The following filters are available:

* `File type`: includes folder, file, images, documents, or video
* `MIME type`: includes JPG, GIF, PPTX, PNG, MP4, DOCX, TIFF, PDF, XLSX
* `Image Size`: includes minimum/maximum width, minimum/maximum height of image

   ![rail-view-example](assets/filters-asset-selector.png) 

### Custom search

Apart from the full-text search, Asset Selector lets you search assets within files using customized search. You can use custom search filters in both Modal view and Rail view modes.

![custom-search](assets/custom-search.png)

You can also create default search filter to save the fields that you frequently search for and use them later. To create custom search for your assets, you can use `filterSchema` property.

### Search bar {#search-bar}

Asset Selector lets you perform full text search of assets within the selected repository. For example, if you type the keyword `wave` in the search bar, all the assets with the `wave` keyword mentioned in any of the metadata properties are displayed.

### Sorting {#sorting}

You can sort assets in Asset Selector by name, dimensions, or size of an asset. You can also sort the assets in ascending or descending order.

### Types of view {#types-of-view}

Asset Selector lets you view the asset in four different views:

* **![list view](assets/do-not-localize/list-view.png) [!UICONTROL List View]**: The list view displays scrollable files and folders in a single column.
* **![grid view](assets/do-not-localize/grid-view.png) [!UICONTROL Grid View]**: The grid view displays scrollable files and folders in a grid of rows and columns.
* **![gallery view](assets/do-not-localize/gallery-view.png) [!UICONTROL Gallery View]**: The gallery view displays files or folders in a center-locked horizontal list.
* **![waterfall view](assets/do-not-localize/waterfall-view.png) [!UICONTROL Waterfall View]**: The waterfall view displays files or folders in the form of a Bridge.

<!--
### Modes to view Asset Selector

Asset Selector supports two types of out of the box views:

**  Modal view or Inline view:** The modal view or inline view is the default view of Asset Selector that represents Assets folders in the front area. The modal view allows users to view assets in a full screen to ease the selection of multiple assets for import. Use `<AssetSelector rail={false}>` to enable modal view.

    ![modal-view](assets/modal-view.png)

**  Rail view:** The rail view represents Assets folders in a left panel. The drag and drop of assets can be performed in this view. Use `<AssetSelector rail={true}>` to enable rail view.

    ![rail-view](assets/rail-view.png)
-->
<!--

### Application Integration

Asset Selector is flexible and can be integrated within your existing [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application. It is accessible and localized to add, search, and select assets in your application. With Asset Selector you can:
*   **Configure** You can configure the files/folders that you want to show at the upfront. The assets that are chosen to view can be of any supported formats, for example, JPEG. It lets you control the display of various text or symbols as per your choice.
*   **Perfect fit** Asset selector easily fits in your existing [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application and choose the way you want to view. The mode of view can be inline, rail, or modal view.
*   **Accessible** With Asset Selector, you can reach the desired asset in an easy manner.
*   **Localize** Assets can be availed for the various locales available as per Adobe's localization standards.
-->
<!--

### Support for multiple instances

The micro front-end design supports the display of multiple instances of Asset Selector on a single screen.

![multiple-instance](assets/multiple-instance.png)
-->

<!--

### Controlled selection with multi-select

You can make default multi-selection of assets by specifying the assets to the component using `selectedAssets` property. You should specify an array of asset IDs. For example, `[{id: 'urn:234}, {id: 'urn:555'}].`
-->
<!--

### Action buttons

When you customize your application with Asset Selector based on ReactJS, you are provided with the following action buttons to perform various actions:
*   **Open in media library** Lets you open the asset in media library.
*   **Upload** Lets you upload an asset directly.
*   **Download** Downloads the asset in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service].
-->
<!--

### Status of an asset

Asset Selector lets you know the status of your uploaded assets. The status can be `Approved`, `Rejected`, or `Expired` of the asset. 
-->
<!--

### Localization

The integration of Asset Selector with [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] allows localized content appear in your application.
-->
