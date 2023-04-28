---
title: Asset Selector for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]
description: Use Asset selector to show and select assets that you can use as a copy of the original asset.
contentOwner: Adobe
feature: asset selector
role: Admin,User
exl-id: a2abc48b-5586-421c-936b-ef4f896d78b7
---

# Micro-Frontend Asset Selector {#Overview}

Micro-Frontend Asset Selector provides a user interface that easily integrates with the [!DNL Experience Manager Assets as a Cloud Service] repository so that you can browse or search digital assets available in the repository and use them in your application authoring experience.

The Micro-Frontend user interface is made available in your application experience using the Asset Selector package. Any updates to the package are automatically imported and the latest deployed Asset Selector loads automatically within your application.

![Overview](assets/overview.png)

Asset Selector provides many benefits, such as:

*   Ease of integration with any of the Adobe or non-Adobe applications using Vanilla JavaScript library.
*   Easy to maintain as updates to the Assets Selector package are automatically deployed to the Asset Selector available for your application. There are no updates required within your application to load the latest modifications.
*   Ease of customization as there are properties available that control the Asset Selector display within your application.

* Full-text search, out-of-the-box, and customized filters to quickly navigate to assets for use within the authoring experience.

* Ability to switch repositories within an IMS organization for asset selection.

* Ability to sort assets by name, dimensions, and size and view them in List, Grid, Gallery, or  Waterfall view.

Perform the following tasks to integrate and use Asset Selector with your [!DNL Experience Manager Assets as a Cloud Service] repository:

* [Integrate Asset Selector using Vanilla JS](#integration-with-vanilla-js)

* [Define Asset Selector display properties](#asset-selector-properties)
* [Use Asset Selector](#using-asset-selector)

## Integrate Asset Selector using Vanilla JS {#integration-with-vanilla-js}

You can integrate any [!DNL Adobe] or non-Adobe application with [!DNL Experience Manager Assets] as a [!DNL Cloud Service] repository and select assets from within the application. 

The integration is done by importing the Asset Selector package and connecting to the Assets as a Cloud Service using the Vanilla JavaScript library. Edit the `index.html` file or a similar file within your application implementation to define the authentication details to access the Assets as a Cloud Service repository and to configure the Asset Selector display properties.
<!--
Asset Selector supports authentication to the [!DNL Experience Manager Assets] as a [!DNL Cloud Service] repository using Identity Management System (IMS) properties such as `imsScope` or `imsClientID`. Authentication using these IMS properties is referred to as SUSI (Sign Up Sign In) flow in this article.

You can perform authentication without defining some of the IMS properties, such as `imsScope` or `imsClientID`, if:

*   You are integrating an [!DNL Adobe] application on [Unified Shell](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/aem-cloud-service-on-unified-shell.html?lang=en).
*   You already have an IMS token generated for authentication.

Accessing [!DNL Experience Manager Assets] as a [!DNL Cloud Service] repository without defining `imsScope` or `imsClientID` IMS properties is referred to as a non-SUSI flow in this article.
-->

You can perform authentication without defining some of the IMS properties, if:

*   You are integrating an [!DNL Adobe] application on [Unified Shell](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/aem-cloud-service-on-unified-shell.html?lang=en).
*   You already have an IMS token generated for authentication.

## Prerequisites {#prerequisites}

Define the prerequisites in the `index.html` file or a similar file within your application implementation to define the authentication details to access the [!DNL Experience Manager Assets] as a [!DNL Cloud Service] repository. The prerequisites include:
*   imsOrg
*   imsToken
*   apikey

<!-- The prerequisites vary if you are authenticating using a SUSI flow or a non-SUSI flow.

**Non-SUSI flow**

*   imsOrg
*   imsToken
*   apikey

For more information on these properties, refer to [Asset Selector Properties](#asset-selector-properties).

**SUSI flow**

*   imsClientId
*   imsScope
*   redirectUrl
*   imsOrg
*   apikey

For more information on these properties, refer to [Example for the SUSI flow](#susi-vanilla) and [Asset Selector Properties](#asset-selector-properties).
-->

### Example for the non-SUSI flow {#non-susi-vanilla}

Use this example `index.html` file for authentication if you are integrating an [!DNL Adobe] application on Unified Shell or if you already have an IMS token generated for authentication.
Access the Asset Selector package using the `Script` tag, as shown in *line 9* to *line 11* of the example `index.html` file. Define the authentication and other Assets as a Cloud Service access-related properties in the const props section, as shown in *line 20* to *line 27* of the `index.html` file.
The `PureJSSelectors` global variable, mentioned in *line 29*, is used to render the Asset Selector in the web browser.
Asset Selector is rendered on the `<div>` container element, as mentioned in *line 35* and *line 36*.

```html {line-numbers="true"}
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta charset="utf-8">
    <title>Asset Selectors</title>
    <link rel="stylesheet" href="index.css">
    <script id="asset-selector"
        src="https://experience.adobe.com/solutions/CQ-assets-selectors/assets/resources/asset-selectors.js"></script>
    <script>

        // container element on which you want to render the AssetSelector/DestinationSelector component
        const container = document.getElementById('asset-selector');

        const otherProps = {
            // any other props supported by asset selector
        }

        const props = {
            discoveryURL: 'https://aem-discovery.adobe.io/',
            apiKey: 'apikey',
            imsOrg: 'imsorg',
            imsToken: "imstoken",
            rail: true,
            ...otherProps
        };
        // Use the PureJSSelectors in globals to render the AssetSelector/DestinationSelector component
        PureJSSelectors.renderAssetSelector(container, props);
    </script>

</head>

<body class="asset-selectors">
    <div id="asset-selector" style="height: calc(100vh - 80px); width: calc(100vw - 60px); margin: -20px;">
    </div>
</body>

</html>

```
<!--
### Example for the SUSI flow {#susi-vanilla}

Use this example `index.html` file for authentication if you are integrating your application using SUSI flow.

Access the Asset Selector package using the `Script` Tag, as shown in *line 9* to *line 11* of the example `index.html` file.

*Line 14* to *line 38* of the example describes the IMS flow properties, such as `imsClientId`, `imsScope`, and `redirectURL`. The function requires that you define at least one of the `imsClientId` and `imsScope` properties. If you do not define a value for `redirectURL`, the registered redirect URL for the client ID is used.

As you do not have an `imsToken` generated, use the `registerAssetsSelectorsAuthService` and `renderAssetSelectorWithAuthFlow` functions, as shown in line 40 to line 50 of the example `index.html` file. Use the `registerAssetsSelectorsAuthService` function before `renderAssetSelectorWithAuthFlow` to register the `imsToken` with the Asset Selector. [!DNL Adobe] recommends to call `registerAssetsSelectorsAuthService` when you instantiate the component.

Define the authentication and other Assets as a Cloud Service access-related properties in the `const props` section, as shown in *line 54* to *line 60* of the example `index.html` file.

The `PureJSSelectors` global variable, mentioned in *line 65*, is used to render the Asset Selector in the web browser.

Asset Selector is rendered on the `<div>` container element, as mentioned in *line 74* to *line 81*. The example uses a dialog to display the Asset Selector.

```html {line-numbers="true"}
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta charset="utf-8">
    <title>Asset Selectors</title>
    <link rel="stylesheet" href="index.css">
    <script id="asset-selector"
        src="https://experience.adobe.com/solutions/CQ-assets-selectors/assets/resources/asset-selectors.js"></script>
    <script>

        const imsProps = {
            imsClientId: "<obtained from IMS team>",
            imsScope: "openid, <other scopes>",
            redirectUrl: window.location.href,
            modalMode: true, // false to open in a full page reload flow
            onImsServiceInitialized: (service) => {
                // invoked when the ims service is initialized and is ready
                console.log("onImsServiceInitialized", service);
            },
            onAccessTokenReceived: (token) => {
                console.log("onAccessTokenReceived", token);
            },
            onAccessTokenExpired: () => {
                console.log("onAccessTokenError");
                // re-trigger sign-in flow
            },
            onErrorReceived: (type, msg) => {
                console.log("onErrorReceived", type, msg);
            },
        }

        function load() {
            const registeredTokenService = PureJSSelectors.registerAssetsSelectorsAuthService(imsProps);
            imsInstance = registeredTokenService;
        };

        // initialize the IMS flow before attempting to render the asset selector
        load();
        

        //function that will render the asset selector
            const otherProps = {
            // any other props supported by asset selector
            }
            const assetSelectorProps = {
                "imsOrg": "imsorg",
                ...otherProps
            }
             // container element on which you want to render the AssetSelector/DestinationSelector component
            const container = document.getElementById('asset-selector');

            /// Use the PureJSSelectors in globals to render the AssetSelector/DestinationSelector component
            PureJSSelectors.renderAssetSelectorWithAuthFlow(container, assetSelectorProps, () => {
                const assetSelectorDialog = document.getElementById('asset-selector-dialog');
                assetSelectorDialog.showModal();
            });
        }
    </script>

</head>
<body class="asset-selectors">
    <div>
        <button onclick="renderAssetSelectorWithAuthFlowFlow()">Asset Selector - Select Assets with Ims Flow</button>
    </div>
        <dialog id="asset-selector-dialog">
            <div id="asset-selector" style="height: calc(100vh - 80px); width: calc(100vw - 60px); margin: -20px;">
            </div>
        </dialog>
    </div>
</body>

</html>

```
-->

## Use Asset Selector properties {#asset-selector-properties}

| Property | Type | Required | Default | Description |
|---|---|---|---|---|
| *rail* | boolean | No | false | If marked `true`, it displays the Asset Selector in a left rail view. If it is marked `false`, the Asset Selector displays in modal view. |
| *discoveryURL* | string | No | Optional | URL to the Experience Manager as a Cloud Service Discovery Service. You can specify the Experience Manager as a Cloud Service URL directly if your application already called the Discovery Service. For example, https://aem-discovery.adobe.io. |
| *imsOrg* | string | No | | Adobe Identification Management System (IMS) ID that is assigned while provisioning [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] for your organization. The imsORG key authenticates whether the org is under Adobe IMS or not.|
| *imsToken* | string | No | | IMS bearer token used for authentication |
| *apiKey* | string | No | | API key used for accessing the AEM Discovery service.|
| *rootPath* | string | No | AEM_ROOT_PATH | Folder name from which you can select your assets. For example, /content/dam/marketing/subfolder. You cannot access and select assets from any other folder.  |
| *path* | string | No | | Path that is used to navigate to a specific directory of assets when the Asset Selector is rendered. |
| *filterSchema* | array | No | | Model that is used to configure properties that you need to specify for the filter. |
| *filterFormProps* | object | No | | Specify the filter properties that you need to use to refine your search. For example, MIME type JPG, PNG, GIF. |
| *selectedAssets* | Array `<object>` | No | | Specify selected Assets when the Asset Selector is rendered. An array of objects is required that contains an id property of the assets. For example, [{id: 'urn:234}, {id: 'urn:555'}]. An asset must be available in current directory. If you need to use a different directory, provide a value for the `path` property as well. |
| *acvConfig* | object | No | | Asset Collection View property that contains object containing custom configuration to override defaults. |
| *i18nSymbols* | `Object<{ id?: string, defaultMessage?: string, description?: string}>` | No | | If the OOTB translations are insufficient for your application needs, you can use this property to specify your own custom-localized values. Adding these values overrides the default translations so that you can use the custom ones. You should pass a valid object (message descriptor) to the key of i18nSymbols that you need to override. |
| *intl* | object | No | | Format text or date and time in localized format. |
| *repositoryId* | string | No | '' | Repository from where the Asset Selector loads the content. |
| *additionalAemSolutions* | `Array<string>` | No | [ ] | It allows you to add a list of additional AEM repositories. If no information is provided in this property, then only media library or AEM Assets repositories are considered. |
| *hideTreeNav* | boolean | No | | Specifies whether to show or hide assets tree navigation sidebar. It is used in modal view only and hence there is no effect of this property in rail view. | 
| *onDrop* | function | No | | The property allows the drop functionality of an asset. |
| *dropOptions* | `{allowList?: object}` | No | | Configures drop options using 'allowList'. |

## Examples to use Asset Selector properties {#usage-examples}

You can define the Asset Selector [properties](#props) in the `index.html` file to customize the Asset Selector display within your application.

### Example 1: Asset Selector in rail view

   ![rail-view-example](assets/rail-view-example-vanilla.png)

If the value of the AssetSelector `rail` is set to `false` or is not mentioned in the properties, Asset Selector displays in the Modal view by default.

<!--
### Example 2: Use selectedAssets property in addition to the path property

Use the `path` property to define the folder name that displays automatically when the Asset Selector is rendered. In addition, use the `selectedAssets` property to define the IDs for the assets that you need to select within the folder. Moreover, when you want to display assets that are pre-defined within the folder, you can use selectedAssets property.

   ![selected-assets-example](assets/selected-assets-example-vanilla.png)
-->

### Example 2: Metadata popover

Use various properties to define metadata of an asset that you want to view using an info icon. The info popover provides the collection of information about asset or the folder including title, dimensions, date of modification, location, and description of an asset. In the example below, various properties are used to display metadata of an asset, for example, `repo:path` property specifies the location of an asset. `repo` represents the repository from where the asset is showing, whereas, `path` represents the route from where the asset or folder is rendered.
    
   ![metadata-popover-example](assets/metadata-popover.png)


### Example 3: Custom filter property in rail view

In addition to the faceted search, Assets Selector allows you to customize various attributes to refine your search from [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application. You need to add the following code to add customized search filters in your application. In the example below, the `Type Filter` search that filters the asset type among Images, Documents, or Videos or the filter type that you have added for the search.

![custom-filter-example-vanilla](assets/custom-filter-example-vanilla.png)

<!--

## Customization after integrating Asset Selector 

### Custom metadata

Assets display panel shows the out of the box metadata that can be displayed in the info of the asset. In addition to this, [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application allows configuration of the asset selector by adding custom metadata that is shown in info panel of the asset.

<!-- Property details to be added here. Referred the ticket https://jira.corp.adobe.com/browse/ASSETS-19023-->

## Asset Selector Object Schema {#object-schema}

Schema describes the object properties associated with an asset selected using Asset Selector. It uses the combination of data types and their values to validate the object describing the selected Asset using an Asset Selector.

**Schema Syntax**
````
interface SelectedAsset {
    'repo:id': string;
    'repo:name': string;
    'repo:path': string;
    'repo:size': number;
    'repo:createdBy': string;
    'repo:createDate': string;
    'repo:modifiedBy': string; 
    'repo:modifyDate': string; 
    'dc:format': string; 
    'tiff:imageWidth': number;
    'tiff:imageLength': number;
    'repo:state': string;
    computedMetadata: Record<string, any>;
    _links: {
        'http://ns.adobe.com/adobecloud/rel/rendition': Array<{
            href: string;
            type: string;
            'repo:size': number;
            width: number;
            height: number;
            [others: string]: any;
        }>;
    };
}
````

**Query Parameters**

| Parameter | Type | Description |
|---|---|---|
| repo:id | string | ID of an Asset |
| repo:name | string | The name of an Asset |
| repo:path | string | The path of an Asset |
| repo:size | number | Size of an Asset (in bytes) |
| repo:createdBy | string | ID of a user who created an Asset |
| repo: createdDate | string | The timestamp when an asset was created |
| repo:modifiedBy | string | ID of a user who modified the asset recently |
| repo:modifyDate | string | The timestamp when the asset was last modified |
| dc:format | string | MIME type of an Asset |
| tiff:imageWidth | number | The width of an image type of Asset |
| tiff:imageLength | number | The height of an image type of Asset |
| repo:state | string | The `Approved`, `Rejected`, or `Expired`state of an Asset |
| computedMetadata | string | It is an object that represents a bucket for all the Asset's metadata of all kinds (repository, application or embedded metadata) |
| _links | string | It represents the collection of links used in the Asset Selector. The links are represented in the form of an array. The parameters of an array include: `href`, `type`, `repo:size`, `width`, `height`, etc.  |

For the detailed example of Object Schema, click 

## Handling selection of Assets using Object Schema {#handling-selection}

The `handleSelection` property is used to handle single or multiple selection of Assets in Assets Selector. The example below states the syntax of usage of `handleSelection`. 

![handle-selection](assets/handling-selection.png)

## Using Asset Selector {#using-asset-selector}

Once the Asset Selector is set up and you are authenticated to use Asset Selector with your [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application, you can select assets or perform various other operations to search for your assets within the repository.

   ![using-asset-selector](assets/using-asset-selector.png)

*   **A**: [Hide/Show panel](#hide-show-panel)
*   **B**: [Repository switcher](#repository-switcher)
*   **C**: [Assets](#repository)
*   **D**: [Filters](#filters)
*   **E**: [Search bar](#search-bar)
*   **F**: [Sorting](#sorting)
*   **G**: [Sorting in ascending or descending order](#sorting)
*   **H**: [View](#types-of-view)

### Hide/Show panel {#hide-show-panel}

To hide folders in the left navigation, click **[!UICONTROL Hide folders]** icon. To undo the changes, click the **[!UICONTROL Hide folders]** icon again.

### Repository switcher {#repository-switcher}

Asset Selector also allows you to switch repositories for asset selection. You can select the repository of your choice from the drop-down available in the left panel. The repository options available in the drop-down list are based on the `repositoryId` property defined in the `index.html` file. It is based on the environments from the selected IMS org that is accessed by the logged in user. Consumers can pass a preferred `repositoryID` and in that case the Asset Selector stops rendering the repo switcher and render assets from the given repository only.
<!--
It is based on the `imsOrg` that is provided in the application. If you want to see the list of repositories, then `repositoryId` is required to view those specific repositories in your application.
-->

### Assets repository

It is a collection of assets folders that you can use to perform operations. 

### Out-of-the-box filters {#filters}

Asset Selector also provides out-of-the-box filter options to refine your search results. The following filters are available:

*   `File type`: includes folder, file, images, documents, or video
*   `MIME type`: includes JPG, GIF, PPTX, PNG, MP4, DOCX, TIFF, PDF, XLSX
*   `Image Size`: includes minimum/maximum width, minimum/maximum height of image

   ![rail-view-example](assets/filters-asset-selector.png) 

### Custom search

Apart from the full-text search, Asset Selector allows you to search assets within files using customized search. You can use custom search filters in both Modal view and Rail view modes.

![custom-search](assets/custom-search.png)

You can also create default search filter to save the fields that you frequently search for and use them later. To create custom search for your assets, you can use `filterSchema` property.

### Search bar {#search-bar}

Asset Selector allows you to perform full text search of assets within the selected repository. For example, if you type the keyword `wave` in the search bar, all the assets with the `wave` keyword mentioned in any of the metadata properties are displayed.

### Sorting {#sorting}

You can sort assets in Asset Selector by name, dimensions, or size of an asset. You can also sort the assets in ascending or descending order.

### Types of view {#types-of-view}

Asset Selector allows you to view the asset in four different views:

*   **![list view](assets/do-not-localize/list-view.png) [!UICONTROL List View]**: The list view displays scrollable files and folders in a single column.
*   **![grid view](assets/do-not-localize/grid-view.png) [!UICONTROL Grid View]**: The grid view displays scrollable files and folders in a grid of rows and columns.
*  **![gallery view](assets/do-not-localize/gallery-view.png) [!UICONTROL Gallery View]**: The gallery view displays files or folders in a center-locked horizontal list.
*   **![waterfall view](assets/do-not-localize/waterfall-view.png) [!UICONTROL Waterfall View]**: The waterfall view displays files or folders in the form of a bridge.

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
*   **Configure** You can configure the files/folders that you want to show at the upfront. The assets that are chosen to view can be of any supported formats, for example, JPEG. It allows you to control the display of various text or symbols as per your choice.
*   **Perfect fit** Asset selector easily fits in your existing [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application and choose the way you want to view. The mode of view can be inline, rail, or modal view.
*   **Accessible** With Asset Selector, you can reach the desired asset in an easy manner.
*   **Localize** Assets can be availed for the various locales available as per Adobe's localization standards.
-->

<!--
### Support for multiple instances

The micro front-end design supports the display of multiple instances of Asset Selector on a single screen.

![multiple-instance](assets/multiple-instance.png)

### Controlled selection with multi-select

You can make default multi-selection of assets by specifying the assets to the component using `selectedAssets` property. You should specify an array of asset IDs. For example, `[{id: 'urn:234}, {id: 'urn:555'}].`

### Action buttons

When you customize your application with Asset Selector based on ReactJS, you are provided with the following action buttons to perform various actions:
*   **Open in media library** Allows you to open the asset in media library.
*   **Upload** Allows you to upload an asset directly.
*   **Download** Downloads the asset in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service].

### Status of an asset

Asset Selector allows you to know the status of your uploaded assets. The status can be `Approved`, `Rejected`, or `Expired` of the asset. 

### Localization

The integration of Asset Selector with [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] allows localized content appear in your application.
-->