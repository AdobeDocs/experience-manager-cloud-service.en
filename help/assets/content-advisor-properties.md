---
title: Content Advisor properties
description: Use properties to customize how the Content Advisor renders when you integrate it with your application.. 
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: cd5ec1de-36b0-48a5-95c9-9bd22fac9719
---
# Content Advisor installation and properties {#content-advisor-installation-properties}

Content Advisor allows you to intergrate AEM with non-Adobe (third-party) applications, extending intelligent asset discovery beyond Adobe applications. The same rich feature set, including AI-powered search, context-aware recommendations, campaign brief–based discovery, access to Dynamic Media renditions, filters, and asset metadata, is supported in third-party integrations.

## Prerequisites{#prereqs}

You must ensure the following communication methods:

* The host application is running on HTTPS.
* You cannot run the application on `localhost`. If you want to integrate Content Advisor on your local machine, you need to create a custom domain for example `[https://<your_campany>.localhost.com:<port_number>]` and add this custom domain in the `redirectUrl list`.
* You can configure and add clientID into the AEM Cloud Service environment variable with the respective `imsClientId`.
<!--
* You can configure and add `ADOBE_PROVIDED_CLIENT_ID` into the AEM Cloud Service environment variable with the respective `imsClientId`.
![Asset Selector IMS Client id environment](assets/asset-selector-ims-client-id-env.png)
-->
* The list of IMS scopes needs to be defined in the environment configuration. 
* The URL of the application is in the IMS client's allowed list of redirect URLs.
* The IMS login flow is configured and rendered using a popup on the web browser. Therefore, popups should be enabled or allowed on the target browser.

Use the above prerequisites if you require the IMS authentication workflow of Content Advisor. Alternatively, if you are already authenticated with the IMS workflow, you can add the IMS information instead.

>[!IMPORTANT]
>
> This repository is intended to serve as a supplemental documentation describing the available APIs and usage examples for integrating Content Advisor. Before attempting to install or use Content Advisor, ensure that your organization has been provisioned the access to Content Advisor as part of the Experience Manager Assets as a Cloud Service profile. If you have not been provisioned, you cannot integrate or use these components. To request provisioning, your program admin should raise a support ticket marked as P2 from the Admin Console and include the following information:
>
>* Domain names where the integrating application is hosted.
>* After provisioning, your organization will be provided with `imsClientId`, `imsScope`, and a `redirectUrl` corresponding to the environments requested that are essential for the configuration of Content Advisor. Without those valid properties, you cannot run the installation steps.

## Installation {#content-advisor-installation}

Content Advisor is available via both ESM CDN (For example, [esm.sh](https://esm.sh/)/[skypack](https://www.skypack.dev/)) and [UMD](https://github.com/umdjs/umd) version.

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

## Content Advisor properties {#content-advisor-propertiess}

You can use the Content Advisor properties to customize the way the Content Advisor is rendered. The following table lists the properties that you can use to customize and use Content Advisor.

| Property | Type | Required | Default |Description |
|---|---|---|---|---|
| *rail*| Boolean | No | False | If marked `true`, Content Advisor is rendered in a left rail view. If it is marked `false`, the Content Advisor is rendered in modal view. |
| *imsOrg*| String | Yes | | Adobe Identity Management System (IMS) ID that is assigned while provisioning [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] for your organization. The `imsOrg` key is required to authenticate whether the organization you are accessing is under Adobe IMS or not. |
| *imsToken* | String | No | | IMS bearer token used for authentication. `imsToken` is required if you are using an [!DNL Adobe] application for the integration. |
| *apiKey* | String | No | | API key used for accessing the AEM Discovery service. `apiKey` is required if you are using an [!DNL Adobe] application integration.|
| *externalBrief* | String | No | | Allows you to upload a campaign brief document to discover relevant assets without manually entering search keywords. Content Advisor analyzes the information in the campaign brief to understand the campaign's intent and recommends relevant assets available in AEM Assets.|
| *filterSchema* | Array | No | | Model that is used to configure filter properties. This is useful when you want to limit certain filter options in Content Advisor.|
| *filterFormProps*| Object | No | | Specify the filter properties that you need to use to refine your search. For! example, MIME type JPG, PNG, GIF. |
| *selectedAssets* | Array `<Object>` | No       |                 | Specify selected Assets when the Content Advisor is rendered. An array of objects is required that contains an id property of the assets. For example, `[{id: 'urn:234}, {id: 'urn:555'}]` An asset must be available in the current directory. If you need to use a different directory, provide a value for the `path` property as well. |
| *acvConfig* | Object | No | | Asset Collection View property that contains object containing custom configuration to override defaults. Also, this property is used with `rail` property to enable rail view of assets viewer.|
| *i18nSymbols*            | `Object<{ id?: string, defaultMessage?: string, description?: string}>` | No       |                 | If the OOTB translations are insufficient for your application's needs, you can expose an interface through which you can pass your own custom-localized values through the `i18nSymbols` prop. Passing a value through this interface overrides the default translations provided and instead use your own. To perform the override, you must pass a valid [Message Descriptor](https://formatjs.io/docs/react-intl/api/#message-descriptor) object to the key of `i18nSymbols` that you want to override. |
| *intl* | Object | No  | | Content Advisor provides default OOTB translations. You can select the translation language by providing a valid locale string through the `intl.locale` prop. For example: `intl={{ locale: "es-es" }}` </br></br> The locale strings supported follow the [ISO 639 - Codes](https://www.iso.org/iso-639-language-codes.html) for the representation of names of languages standards. </br></br> List of supported locales: English - 'en-us' (default) Spanish - 'es-es' German - 'de-de' French - 'fr-fr' Italian - 'it-it' Japanese - 'ja-jp' Korean - 'ko-kr' Portuguese - 'pt-br' Chinese (Traditional) - 'zh-cn' Chinese (Taiwan) - 'zh-tw' |
| *repositoryId* | String | No | ''| Repository from where the Content Advisor loads the content. |
| *additionalAemSolutions* | `Array<string>` | No | [ ] | It lets you add a list of additional AEM repositories. If no information is provided in this property, then only media library or AEM Assets repositories are considered.|
| *hideTreeNav*| Boolean | No |  | Specifies whether to show or hide assets tree navigation sidebar. It is used in modal view only and hence there is no effect of this property in rail view. |
| *onDrop* | Function | No | | The on drop functionality is used to drag an asset and release onto a designated drop area. It allows for interactive user interfaces where assets can be moved and processed seamlessly. |
| *dropOptions* | `{allowList?: Object}` | No | | Configures drop options using 'allowList'.  |
| *theme* | String | No | Default | Apply theme to the Content Advisor application between `default` and `express`. It also supports `@react-spectrum/theme-express`. |
| *handleSelection* | Function | No | | Invoked with array of Asset items when assets are selected and the `Select` button on the modal is clicked. This function is only invoked in modal view. For rail view, use the `handleAssetSelection` or `onDrop` functions. Example: <pre>handleSelection=(assets: Asset[])=> {...}</pre> See [selection of assets](/help/assets/content-advisor-customization.md#selection-of-assets) for details.|
| *handleAssetSelection*| Function | No | | Invoked with array of items as the assets are being selected or unselected. This is useful when you want to listen for assets as user selects them. Example: <pre>handleAssetSelection=(assets: Asset[])=> {...}</pre> See [selection of assets](/help/assets/content-advisor-customization.md#selection-of-assets) for details. |
| *onClose* | Function | No | | Invoked when `Close` button in modal view is pressed. This is only called in `modal` view and disregarded in `rail` view. |
| *onFilterSubmit* | Function | No | | Invoked with filter items as user changes different filter criteria. |
| *selectionType* | String | No | Single | Configuration for `single` or `multiple` selection of assets at a time. |
| *dragOptions.allowList* | boolean | No | | The property is used to allow or deny the dragging of assets that are not selectable. See [dragOptions Property](/help/assets/content-advisor-customization.md#drag-options-property) |
| *aemTierType* | String | No |  | It allows you to select whether you want to show assets from delivery tier, author tier, or both. <br><br> Syntax: `aemTierType: "author"  "delivery"` <br><br> For example, if both `["author","delivery"]` are used, then the repository switcher displays options for both author and delivery. |
| *handleNavigateToAsset* | Function | No | | It is a Callback function to handle selection of an asset. |
| *noWrap* | Boolean | No | | The *noWrap* property prevents the Content Advisor from being wrapped in a dialog. If this property is not mentioned, it renders the *Dialog view* by default. |
| *dialogSize* | S, M, L, fullscreen, fullscreenTakeover | String | Optional | You can control the layout by specifying its size using the given options. |
| *colorScheme* | String (light, dark) | No | | This property is used to set the theme of an Content Advisor application. You can choose between light or dark theme. |
| *filterRepoList* | Function | No | | A function that receives the repository list and returns a filtered list. |
| *expiryOptions* | Function | | | You can use between the following two properties: **getExpiryStatus** which provides status of an expired asset. The function returns `EXPIRED`, `EXPIRING_SOON` or `NOT_EXPIRED` based on the expiry date of an asset that you provide. See [customize expired assets](/help/assets/content-advisor-customization.md#customize-expired-assets). Additionally, you can use **allowSelectionAndDrag** in which the value of the function can either be `true` or `false`. When the value is set to `false`, the expired asset cannot be selected or dragged on the canvas. |
| *showToast* | | No | | It allows Content Advisor to show a customized toast message for the expired asset. |
| *uploadConfig* | Object | | | It is an object that contains customized configuration for the upload. See [upload configuration](#content-advisor-customization.md#upload-config) for the usability.|
| *uploadConfig* > *metadataSchema* | Array | No | | This property is nested under `uploadConfig` property. Add an array of fields that you provide to gather metadata from the user. Using this property, you can also use hidden metadata which is assigned to an asset automatically but is not visible to the user. |
| *uploadConfig* > *onMetadataFormChange* | Callback function | No | | This property is nested under `uploadConfig` property. It consists of `property` and `value`. `Property` equals the *mapToProperty* of the field passed from the *metadataSchema* whose value is being updated. Whereas,`value` equals the new value is provided as an input. |
| *uploadConfig* > *targetUploadPath* | String |  | `"/content/dam"` | This property is nested under `uploadConfig` property. The target upload path for the files which defaults to root of the assets repository. |
| *uploadConfig* > *hideUploadButton* | Boolean | | False | It ensures if the internal upload button should be hidden or not. This property is nested under `uploadConfig` property. |
| *uploadConfig* > *onUploadStart* | Function | No |  | It is a callback function which is used to pass the upload source among Dropbox, OneDrive, or local. The syntax is `(uploadInfo: UploadInfo) => void`. This property is nested under `uploadConfig` property. |
| *uploadConfig* > *importSettings* | Function | | | It enables the support for importing assets from third party source. `sourceTypes` uses an array of the import sources that you want to enable. The supported sources are Onedrive and Dropbox. The syntax is `{ sourceTypes?: ImportSourceType[]; apiKey?: string; }`. Moreover, this property is nested under `uploadConfig` property. |
| *uploadConfig* > *onUploadComplete* | Function | No | | It is a callback function which is used to pass the file upload status among succeeded, failed, or duplicate. The syntax is `(uploadStats: UploadStats) => void`. Moreover, this property is nested under `uploadConfig` property. |
| *uploadConfig* > *onFilesChange* | Function | No | | This property is nested under `uploadConfig` property. It is a callback function which is used to show the behavior of upload when a file is changed. It passes the new array of files pending for upload and the source type of the upload. Source type can be null in case of error. The syntax is `(newFiles: File[], uploadType: UploadType) => void` |
| *uploadConfig* > *uploadingPlaceholder* | String | | | It is a placeholder image that replaces the metadata form when an upload of the asset is initiated. The syntax is `{ href: string; alt: string; }`, Moreover, this property is nested under `uploadConfig` property. |
| *featureSet* | Array | String | | The `featureSet:[ ]` property is used to enable or disable a particular functionaly in the Content Advisor application. To enable the component or a feature, you can pass a string value in the array or leave the array empty to disable added features, and just have the base functionality. For example, you want to enable upload functionality in the Content Advisor, use the syntax `featureSet:["upload"]`. Similarly, you can use `featureSet:["content-fragments"]` to enable Content Fragments in the Content Advisor. To use multiple features together, the syntax is featureSet:["upload", "content-fragments"].|

<!--
| *selectedRendition* | Object | | | This property allows users to define and control which renditions of an asset are displayed when the panel is accessed. This customization enhances user experience by filtering out unnecessary renditions and showcasing only the most relevant renditions. For example, `CopyUrlHref` allows you to use Dynamic Media renditions in your Asset Selector application (delivery URL). |
| *featureSet* | Array | String | | The `featureSet:[ ]` property is used to enable or disable a particular functionaly in the Asset Selector application. To enable the component or a feature, you can pass a string value in the array or leave the array empty to disable that component. For example, you want to enable upload functionality in the Asset Selector, use the syntax `featureSet:[0:"upload"]`. Similarly, you can use `featureSet:[0:"collections"]` to enable collections in the Asset Selector. Addidionally, use `featureSet:[0:"detail-panel"]` to enable [details panel](overview-asset-selector.md#asset-details-and-metadata) of an asset. Also, `featureSet:[0:"dm-renditions"]` to show Dynamic Media renditions of an asset.|
| *rootPath* | String | No | /content/dam/ | Folder path from which Asset Selector displays your assets. `rootPath` can also be used in the form of encapsulation. For example, given the following path, `/content/dam/marketing/subfolder/`, Asset Selector does not allow you to traverse through any parent folder, but only displays the children folders. |
| *path* | String | No | | Path that is used to navigate to a specific directory of assets when the Asset Selector is rendered. |
| *expirationDate* | Function | No | | This function is used to set the usability period of an asset. |
| *disableDefaultBehaviour* | Boolean | No | False | It is a function that is used to enable or disable the selection of an expired asset. You can customize the default behavior of an asset that is set to expire. See [customize expired assets](/help/assets/asset-selector-customization.md#customize-expired-assets). |
-->

### ImsAuthProps {#ims-auth-props}

The `ImsAuthProps` properties define the authentication information and flow that the Content Advisor uses to obtain an `imsToken`. By setting these properties, you can control how the authentication flow should behave and register listeners for various authentication events.

| Property Name | Description|
|---|---|
| `imsClientId`| A string value representing the IMS client ID used for authentication purposes. This value is provided by Adobe and is specific to your Adobe AEM CS organization.|
| `imsScope`| Describes the scopes used in authentication. The scopes determine the level of access that the application has to your organization resources. Multiple scopes can be separated by commas.|
| `redirectUrl` | Represents the URL where the user is redirected after authentication. This value is typically set to the current URL of the application. If a `redirectUrl` is not supplied, `ImsAuthService` uses the redirectUrl used to register the `imsClientId`|
| `modalMode`| A boolean indicating whether the authentication flow should be displayed in a modal (pop-up) or not. If set to `true`, the authentication flow is displayed in a pop-up. If set to `false`, the authentication flow is displayed in a full page reload. _Note:_ for better UX, you can dynamically control this value if the user has browser pop-up disabled. |
| `onImsServiceInitialized`| A callback function that is called when the Adobe IMS authentication service is initialized. This function takes one parameter, `service`, which is an object representing the Adobe IMS service. See [`ImsAuthService`](#imsauthservice-ims-auth-service) for more details.|
| `onAccessTokenReceived`| A callback function that is called when an `imsToken` is received from the Adobe IMS authentication service. This function takes one parameter, `imsToken`, which is a string representing the access token. |
| `onAccessTokenExpired`| A callback function that is called when an access token has expired. This function is typically used to trigger a new authentication flow to obtain a new access token. |
| `onErrorReceived`| A callback function that is called when an error occurs during authentication. This function takes two parameters: the error type and error message. The error type is a string representing the type of error and the error message is a string representing the error message. |

### ImsAuthService {#ims-auth-service}

`ImsAuthService` class handles the authentication flow for the Content Advisor. It is responsible for obtaining an `imsToken` from the Adobe IMS authentication service. The `imsToken` is used to authenticate the user and authorize access to the [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] Assets repository. ImsAuthService uses the `ImsAuthProps` properties to control the authentication flow and register listeners for various authentication events. You can use the convenient [`registerAssetsSelectorsAuthService`](#purejsselectorsregisterassetsselectorsauthservice) function to register the _ImsAuthService_ instance with the Content Advisor. The following functions are available on the `ImsAuthService` class. However, if you are using the _registerAssetsSelectorsAuthService_ function, you do not need to call these functions directly.

| Function Name | Description |
|---|---|
| `isSignedInUser` | Determines whether the user is currently signed in to the service and returns a boolean value accordingly.|
| `getImsToken`    | Retrieves the authentication `imsToken` for the currently signed-in user, which can be used to authenticate requests to other services such as generating asset _rendition.|
| `signIn`| Initiates the sign-in process for the user. This function uses the `ImsAuthProps` to show authentication in either a pop-up or a full page reload |
| `signOut`| Signs the user out of the service, invalidating their authentication token and requiring them to sign in again to access protected resources. Invoking this function will reload the current page.|
| `refreshToken`| Refreshes the authentication token for the currently signed-in user, preventing it from expiring and ensuring uninterrupted access to protected resources. Returns a new authentication token that can be used for subsequent requests. |

### contentFragmentSelectorProps {#content-fragment-selector-properties}

`contentFragmentSelectorProps` allows you to configure how Content Fragments are accessed and displayed within the Content Advisor. By enabling the content-fragments feature in the `featureSet` and providing the required configuration, you can seamlessly integrate Content Fragment selection alongside assets. This enables users to browse, search, and select Content Fragments within the same unified interface, ensuring a consistent content selection experience across assets and structured content.

```
const assetSelectorProps = {
     featureSet: [
       'upload',            /* Include upload or other featureSet values to ensure no missing functionality */
       'content-fragments', /* Content Fragments pill will be shown */
     ],
     contentFragmentSelectorProps: {
       /* Configures the Content Fragments Pill experience */
       /* ...props @aem-sites/content-fragment-selector MFE supports */
    }
}

<AssetSelector {...assetSelectorProps} />
```

In `contentFragmentSelectorProps`, you can mention any of the properties available at [Content Fragment Selector properties](/help/headless/content-fragment-selector/properties.md).


