---
title: Asset Selector for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]
description: Use Asset selector to show and select assets that you can use as a copy of the original asset.
contentOwner: Adobe
feature: asset selector
role: Admin,User
exl-id: a2abc48b-5586-421c-936b-ef4f896d78b7
---

# Micro Frontend Asset Selector {#Overview}

Micro Frontend Asset Selector provides a user interface embedded within your application that interacts with the [!DNL Assets as a Cloud Service] repository. As a result, you can easily browse or search digital assets available in the repository and use them in your application experience.
The Micro Frontend user interface is made available in your application experience using the Asset Selector package. You can import the package and the latest deployed Micro Frontend loads automatically within your application.

![Overview](assets/overview.png)

Micro Frontend Asset Selector provides many benefits, such as:

*   Ease of integration with any of the Adobe or non-Adobe applications using Vanilla JavaScript library.
*   Easy to maintain as you can update the Assets Selector package to deploy and load the latest Micro Frontend on your application automatically. There are no updates required within your application to view the latest Micro Frontend modifications.
*   Ease of customization as there are properties available to customize the Asset Selector display within your application.


<!--

## Configuration {#configuration}

Asset Selector is implemented for the usage in Enterprise Service Management (ESM), Common JavaScript (CJS), and Universal Module Definition (UMD) export. It eases its integration with various JavaScript frameworks including React, Angular, Vanilla, and so on, using the provided bindings.

-->

### Integrate Micro Frontend Asset Selector using Vanilla JS {#integration-with-vanilla-js}

You can integrate any Adobe or non-Adobe application with Experience Manager Assets as a Cloud Service repository and select assets from within the application. 
The integration is done by importing the Asset Selector package and connecting to the Assets as a Cloud Service using the Vanilla JavaScript library. Edit the index.html file to define the authentication details to access the Assets as a Cloud Service repository and to configure the Asset Selector display properties.
The authentication to the Experience Manager Assets as a Cloud Service repository depends on various factors such as:
*   You are integrating an Adobe application on [Unified Shell](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/overview/aem-cloud-service-on-unified-shell.html?lang=en).
*   You already have an Identity Management System (IMS) token generated for authentication.
*   You are not integrating an Adobe application on Unified Shell and do not have an IMS token generated for authentication.
The first two scenarios are referred to as non-IMS flow in this article and the third scenario is referred to as an IMS flow.

## Prerequisites {#prerequisites}

**Non-IMS flow**

*   discoveryURL
*   imsOrg
*   imsToken
*   apikey

For more information on these properties, refer to [Asset Selector Properties](#props).

**IMS flow**

*   imsClientId
*   imsScope
*   redirectUrl
*   discoveryURL
*   imsOrg
*   apikey

For more information on these properties, refer to [Example for the IMS flow](#ims-vanilla) and [Asset Selector Properties](#props).

#### Example for the non-IMS flow {#non-ims-vanilla}

Use this example `index.html` file for authentication if you are integrating an Adobe application on Unified Shell or if you already have an IMS token generated for authentication.
Access the Asset Selector package using the `Script` tag, as shown in line 9 to line 11 of the example index.html file. Define the authentication and other Assets as a Cloud Service access related properties in the const props section, as shown in line 20 to line 27 of the `index.html` file.
The `PureJSSelectors` global variable, mentioned in line 29, is used to render the Micro Frontend Asset Selector in the web browser.
Asset Selector is rendered on the `<div>` container element, as mentioned in line 35 and line 36.

```html {line-numbers="true"}
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta charset="utf-8">
    <title>Asset Selectors</title>
    <link rel="stylesheet" href="index.css">
    <script id="asset-selectors-umd-src"
        src="https://experience-stage.adobe.com/solutions/CQ-assets-selectors/assets/resources/asset-selectors.js"></script>
    <script>

        // container element on which you want to render the AssetSelector/DestinationSelector component
        const container = document.getElementById('asset-selector');

        const otherProps = {
            // any other props supported by asset selector
        }

        const props = {
            discoveryURL: 'https://aem-discovery.adobe.io',
            apiKey: 'aem-assets-backend-nr-1',
            imsOrg: '745F37C35E4B776E0A49421B@AdobeOrg',
            imsToken: "eyJ4NXUiOiJpbXNfbmExLXN0ZzEta2V5LTEuY2VyI...",
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

#### Example for the IMS flow {#ims-vanilla}

Use this example `index.html` file for authentication if you are not integrating an Adobe application on Unified Shell or if you do not have an IMS token generated for authentication.

Access the Asset Selector package using the `Script` Tag, as shown in line 9 to line 11 of the example `index.html` file.

Line 14 to line 38 of the example describes the IMS flow properties, such as `imsClientId`, `imsScope`, and `redirectURL`. The function requires that you define at least one of the `imsClientId` and `imsScope` properties. If you do not define a value for `redirectURL`, the registered redirect URL for the client ID is used.

As you do not have an `imsToken` generated, use the `registerAssetSelectorsIms` and `renderAssetSelectorWithIms` functions, as shown in line 40 to line 50 of the example `index.html` file. Use the `registerAssetSelectorsIms` function before `renderAssetSelectorWithIms` to register the `imsToken` with the Asset Selector. Adobe recommends to call `registerAssetSelectorsIms` as soon as you instantiate the component.

Define the authentication and other Assets as a Cloud Service access related properties in the `const props` section, as shown in line 54 to line 60 of the example `index.html` file.

The `PureJSSelectors` global variable, mentioned in line 65, is used to render the Micro Frontend Asset Selector in the web browser.

Asset Selector is rendered on the `<div>` container element, as mentioned in line 74 to line 81. The example uses a dialog to display the Asset Selector.

```html {line-numbers="true"}
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta charset="utf-8">
    <title>Asset Selectors</title>
    <link rel="stylesheet" href="index.css">
    <script id="asset-selectors-umd-src"
        src="https://experience-stage.adobe.com/solutions/CQ-assets-selectors/assets/resources/asset-selectors.js"></script>
    <script>

        const imsProps = {
            imsClientId: "<obtained from IMS team>",
            imsScope: "openid, <other scopes>",
            redirectUrl: window.location.href, // redirect url to be used for ims flow, if empty it will use the registered redirect url for the client id.
            modalMode: true, // false to open in a full page reload flow
            adobeImsOptions: {
                modalSettings: {
                    allowOrigin: window.location.origin,
                },
                useLocalStorage: true,
            },
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
            const registeredTokenService = PureJSSelectors.registerAssetSelectorsIms(imsProps);
            imsInstance = registeredTokenService;
        };

        // initialize the IMS flow before attempting to render the asset selector
        load();
        

        //function that will render the asset selector
        async function renderAssetSelectorWithImsFlow() {
            const otherProps = {
            // any other props supported by asset selector
            }
            const assetSelectorProps = {
                "discoveryURL": "https://aem-discovery-stage.adobe.io",
                "imsOrg": "9D0725C05E44FE1A0A49411C@AdobeOrg",
                apiKey: "aem-assets-backend-nr-1",
                env: "",
                ...otherProps
            }
             // container element on which you want to render the AssetSelector/DestinationSelector component
            const container = document.getElementById('asset-selector');

            /// Use the PureJSSelectors in globals to render the AssetSelector/DestinationSelector component
            PureJSSelectors.renderAssetSelectorWithIms(container, assetSelectorProps, () => {
                const assetSelectorDialog = document.getElementById('asset-selector-dialog');
                assetSelectorDialog.showModal();
            });
        }
    </script>

</head>
<body class="asset-selectors">
    <div>
        <button onclick="renderAssetSelectorWithImsFlow()">Asset Selector - Select Assets with Ims Flow</button>
    </div>
        <dialog id="asset-selector-dialog">
            <div id="asset-selector" style="height: calc(100vh - 80px); width: calc(100vw - 60px); margin: -20px;">
            </div>
        </dialog>
    </div>
</body>

</html>

```

### Subscribe to I/O service

Vlad to provide inputs on this

## Use Asset Selector properties {#props}

| Property | Type | Required | Default | Description |
|---|---|---|---|---|
| *rail* | boolean | No | false | If marked `true`, it displays the Asset Selector in a left rail view. If it is marked `false`, the Asset Selector displays in modal view. |
| *discoveryURL* | string | No | | A URL that triggers the Micro Frontend Asset Selector application integrated with your [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] Assets directly in case your application has the discovery information. (For example, https://aem-discovery.adobe.io) |
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
| *hideTreeNav* | boolean | No | | Specifies whether to show or hide assets tree navigation sidebar. This is used in modal view only and hence there is no effect of this property in rail view. | 
| *onDrop* | function | No | | The property allows the drop functionality of an asset. |
| *dropOptions* | `{allowList?: object}` | No | | Configures drop options using 'allowList'. |
| *showForcedLoading* | boolean | No | false | Indicates whether to show Asset Selector on loading screen. This is useful when you are waiting for an imsToken to be available in SUSI flow. Asset Selector stops rendering assets if `showForcedLoading` is true. However, it still sends pre-flight requests to discovery. |

## Examples to use Asset Selector properties {#usage-examples}

You can define the Asset Selector [properties](#props) in the `index.html` file to customize the Asset Selector display within your application.

### Example 1: Asset Selector in rail view.

   ![rail-view-example](assets/rail-view-example-vanilla.png)

If the value of the AssetSelector `rail` is set to `false` or is not mentioned in the properties, Asset Selector displays in the Modal view by default.

### Example 2: Use selectedAssets property in addition to the path property

Use the `path` property to define the folder name that displays automatically when the Asset Selector is rendered. In addition, use the `selectedAssets` property to define the IDs for the assets that you need to select within the folder. 

   ![selected-assets-example](assets/selected-assets-example-vanilla.png)

<!--

*   **An example of Custom Filter**

    ![custom-filter-example](assets/custom-filter-example.png)

-->

<!--

## Customization after integrating Asset Selector 

### Custom metadata

Assets display panel shows the out of the box metadata that can be displayed in the info of the asset. In addition to this, [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application allows configuration of the asset selector by adding custom metadata that is shown in info panel of the asset.

<!-- Property details to be added here. Referred the ticket https://jira.corp.adobe.com/browse/ASSETS-19023-->

<!--

### Custom filter

In addition to the faceted search, Assets Selector allows you to customize various attributes to refine your search from !DNL Adobe Experience Manager] as a [!DNL Cloud Service] application.![Alt text](https://file%2B.vscode-resource.vscode-cdn.net/Users/kkour/Desktop/MDs/asset%20selector/rail-view.png)

-->

<!-- Property details to be added here -->



## Using Asset Selector {#using-asset-selector}

Once the Micro Frontend Asset Selector is set up and you are authenticated to use Asset Selector with your [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] application, you can select assets or perform various other operations to search for your assets within the repository.

### Hide/Show panel 

To hide folders in the left navigation, click **[!UICONTROL Hide folders]** icon. To undo the changes, click the **[!UICONTROL Hide folders]** icon again.

### Repository switcher

Asset selector also allows you to switch repositories for asset selection. You can select the repository of your choice from the drop-down available in the left panel. The repository options available in the drop-down list are based on the `repositoryId` property defined in the `index.html` file.

### Search bar

Asset Selector allows you to perform full text search of assets within the selected repository. For example, if you type the keyword `wave` in the search bar, all the assets with the `wave` keyword mentioned in any of the metadata properties are displayed.

### Out-of-the-box filters

Asset Selector also provids out-of-the-box filter options to refine your search results. The following filters are available:

*   `File type`: includes folder, file, images, documents, or video
*   `MIME type`: includes JPG, GIF, PPTX, PNG, MP4, DOCX, TIFF, PDF, XLSX
*   `Image Size`: includes minimum/maximum width, minimum/maximum height of image

   ![rail-view-example](assets/filters-asset-selector.png)

<!--

### Custom search

Apart from the full-text search, asset selector microfront end allows you to search assets within files using customized search. You can use custom search filters in both Modal view and Rail view modes.

![custom-search](assets/custom-search.png)

You can also create default search filter to save your most search fields and use them later. To create custom search for your assets, you can use `filterSchema` property.

-->

### Sorting

You can sort assets in Asset Selector by name, dimension, or size of an asset. You can also sort the assets in ascending or descending order.

### Types of view

Asset Selector allows you to view the asset four different views:

*   `List view`: The list view displays scrollable files and folders in a single column.
*   `Grid view`: The grid view displays scrollable files and folders in a grid of rows and columns.
*   `Gallery view`: The gallery view displays files or folders in a center-locked horizontal list.
*   `Waterfall view`: The waterfall view displays files or folders in the form of a bridge.

<!--

### Modes to view Asset Selector

Asset Selector supports two types of out of the box views:

**1.  Modal view or Inline view:** The modal view or inline view is the default view of asset selector that represents Assets folders in the front area. The modal view allows users to view assets in a full screen to ease the selection of multiple assets for import. Use `<AssetSelector rail={false}>` to enable modal view.
    ![modal-view](assets/modal-view.png)

**2.  Rail view:** The rail view represents Assets folders in a left panel. The drag and drop of assets can be performed in this view. Use `<AssetSelector rail={true}>` to enable rail view.
    ![rail-view](assets/rail-view.png)

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

The micro front-end design supports the display of multiple instances of asset selector on a single screen.

![multiple-instance](assets/multiple-instance.png)

### Controlled selection with multi-select

You can make default multi-selection of assets by specifying the assets to the component using `selectedAssets` property. You should specify an array of asset IDs. For example, `[{id: 'urn:234}, {id: 'urn:555'}].`

### Action buttons

When you customize your application with asset selector based on ReactJS, you are provided with the following action buttons to perform various actions:
*   **Open in media library** Allows you to open the asset in media library.
*   **Upload** Allows you to upload an asset directly.
*   **Download** Downloads the asset in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service].

### Status of an asset

Asset selector allows you to know the status of your uploaded assets. The status can be `Approved`, `Rejected`, or `Expired` of the asset. 

### Localization

The integration of asset selector with [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] allows localized content appear in your application.

-->