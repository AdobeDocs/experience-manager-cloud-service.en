---
title: Asset Selector for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]
description: Use Asset selector to search, find, and retrieve assets' metadata and renditions within your application.
role: Admin, User
exl-id: cd5ec1de-36b0-48a5-95c9-9bd22fac9719
---
# Asset Selector properties {#asset-selector-properties}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

You can use the Asset Selector properties to customize the way the Asset Selector is rendered. The following table lists the properties that you can use to customize and use the Asset Selector.

| Property | Type | Required | Default |Description |
|---|---|---|---|---|
| *rail*| Boolean | No | False | If marked `true`, Asset Selector is rendered in a left rail view. If it is marked `false`, the Asset Selector is rendered in modal view. |
| *imsOrg*| String | Yes | | Adobe Identity Management System (IMS) ID that is assigned while provisioning [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] for your organization. The `imsOrg` key is required to authenticate whether the organization you are accessing is under Adobe IMS or not. |
| *imsToken* | String | No | | IMS bearer token used for authentication. `imsToken` is required if you are using an [!DNL Adobe] application for the integration. |
| *apiKey* | String | No | | API key used for accessing the AEM Discovery service. `apiKey` is required if you are using an [!DNL Adobe] application integration.|
| *filterSchema* | Array | No | | Model that is used to configure filter properties. This is useful when you want to limit certain filter options in Asset Selector.|
| *filterFormProps*| Object | No | | Specify the filter properties that you need to use to refine your search. For! example, MIME type JPG, PNG, GIF. |
| *selectedAssets* | Array `<Object>` | No       |                 | Specify selected Assets when the Asset Selector is rendered. An array of objects is required that contains an id property of the assets. For example, `[{id: 'urn:234}, {id: 'urn:555'}]` An asset must be available in the current directory. If you need to use a different directory, provide a value for the `path` property as well. |
| *acvConfig* | Object | No | | Asset Collection View property that contains object containing custom configuration to override defaults. Also, this property is used with `rail` property to enable rail view of assets viewer.|
| *i18nSymbols*            | `Object<{ id?: string, defaultMessage?: string, description?: string}>` | No       |                 | If the OOTB translations are insufficient for your application's needs, you can expose an interface through which you can pass your own custom-localized values through the `i18nSymbols` prop. Passing a value through this interface overrides the default translations provided and instead use your own. To perform the override, you must pass a valid [Message Descriptor](https://formatjs.io/docs/react-intl/api/#message-descriptor) object to the key of `i18nSymbols` that you want to override. |
| *intl* | Object | No  | | Asset Selector provides default OOTB translations. You can select the translation language by providing a valid locale string through the `intl.locale` prop. For example: `intl={{ locale: "es-es" }}` </br></br> The locale strings supported follow the [ISO 639 - Codes](https://www.iso.org/iso-639-language-codes.html) for the representation of names of languages standards. </br></br> List of supported locales: English - 'en-us' (default) Spanish - 'es-es' German - 'de-de' French - 'fr-fr' Italian - 'it-it' Japanese - 'ja-jp' Korean - 'ko-kr' Portuguese - 'pt-br' Chinese (Traditional) - 'zh-cn' Chinese (Taiwan) - 'zh-tw' |
| *repositoryId* | String | No | ''| Repository from where the Asset Selector loads the content. |
| *additionalAemSolutions* | `Array<string>` | No | [ ] | It lets you add a list of additional AEM repositories. If no information is provided in this property, then only media library or AEM Assets repositories are considered.|
| *hideTreeNav*| Boolean | No |  | Specifies whether to show or hide assets tree navigation sidebar. It is used in modal view only and hence there is no effect of this property in rail view. |
| *onDrop* | Function | No | | The property allows the drop functionality of an asset. |
| *dropOptions* | `{allowList?: Object}` | No | | Configures drop options using 'allowList'.  |
| *colorScheme* | String | No | | Configure theme (`light` or `dark`) for the Asset Selector. |
| *Theme* | String | No | Default | Apply theme to the Asset Selector application between `default` and `express`. It also supports `@react-spectrum/theme-express`. |
| *handleSelection* | Function | No | | Invoked with array of Asset items when assets are selected and the `Select` button on the modal is clicked. This function is only invoked in modal view. For rail view, use the `handleAssetSelection` or `onDrop` functions. Example: <pre>handleSelection=(assets: Asset[])=> {...}</pre> See [selection of assets](/help/assets/asset-selector-customization.md#selection-of-assets) for details.|
| *handleAssetSelection*| Function | No | | Invoked with array of items as the assets are being selected or unselected. This is useful when you want to listen for assets as user selects them. Example: <pre>handleSelection=(assets: Asset[])=> {...}</pre> See [selection of assets](/help/assets/asset-selector-customization.md#selection-of-assets) for details. |
| *onClose* | Function | No | | Invoked when `Close` button in modal view is pressed. This is only called in `modal` view and disregarded in `rail` view. |
| *onFilterSubmit* | Function | No | | Invoked with filter items as user changes different filter criteria. |
| *selectionType* | String | No | Single | Configuration for `single` or `multiple` selection of assets at a time. |
| *dragOptions.allowList* | boolean | No | | The property is used to allow or deny the dragging of assets that are not selectable. |
| *aemTierType* | String | No |  | It allows you to select whether you want to show assets from delivery tier, author tier, or both. <br><br> Syntax: `aemTierType:[0]: "author" 1: "delivery"` <br><br> For example, if both `["author","delivery"]` are used, then the repository switcher displays options for both author and delivery. |
| *handleNavigateToAsset* | Function | No | | It is a Callback function to handle selection of an asset. |
| *noWrap* | Boolean | No | | The *noWrap* property helps rendering Asset Selector in the side rail panel. If this property is not mentioned, it renders the *Dialog view* by default. | 
| *dialogSize* | small, medium, large, fullscreen, or fullscreen takeover | String | Optional | You can control the layout by specifying its size using the given options. |
| *colorScheme* | Light or dark | No | | This property is used to set the theme of an Asset Selector application. You can choose between light or dark theme. |
| *filterRepoList* | Function | No |  | You can use `filterRepoList` callback function that calls Experience Manager repository and returns a filtered list of repositories. |
| *expiryOptions* | Function | | | You can use between the following two properties: **getExpiryStatus** which provides status of an expired asset. The function returns `EXPIRED`, `EXPIRING_SOON` or `NOT_EXPIRED` based on the expiry date of an asset that you provide. See [customize expired assets](/help/assets/asset-selector-customization.md#customize-expired-assets). Additionally, you can use **allowSelectionAndDrag** in which the value of the function can either be `true` or `false`. When the value is set to `false`, the expired asset cannot be selected or dragged on the canvas. | 
| *showToast* | | No | | It allows Asset Selector to show a customized toast message for the expired asset. |
| *metadataSchema* | Array | No | | Add an array of fields that you provide to gather metadata from the user. Using this property, you can also use hidden metadata which is assigned to an asset automatically but is not visible to the user. |
| *onMetadataFormChange* | Callback function | No | | It consists of `property` and `value`. `Property` equals the *mapToProperty* of the field passed from the *metadataSchema* whose value is being updated. Whereas,`value` equals the new value is provided as an input. |
| *targetUploadPath* | String |  | `"/content/dam"` | The target upload path for the files which defaults to root of the assets repository. |
| *hideUploadButton* | Boolean | | False | It ensures if the internal upload button should be hidden or not. |
| *onUploadStart* | Function | No |  | It is a callback function which is used to pass the upload source among Dropbox, OneDrive, or local. The syntax is `(uploadInfo: UploadInfo) => void` |
| *importSettings* | Function | | | It enables the support for importing assets from third party source. `sourceTypes` uses an array of the import sources that you want to enable. The supported sources are Onedrive and Dropbox. The syntax is `{ sourceTypes?: ImportSourceType[]; apiKey?: string; }` |
| *onUploadComplete* | Function | No | | It is a callback function which is used to pass the file upload status among succeeded, failed, or duplicate. The syntax is `(uploadStats: UploadStats) => void` |
| *onFilesChange* | Function | No | | It is a callback function which is used to show the behavior of upload when a file is changed. It passes the new array of files pending for upload and the source type of the upload. Source type can be null in case of error. The syntax is `(newFiles: File[], uploadType: UploadType) => void` |
| *uploadingPlaceholder* | String | | | It is a placeholder image that replaces the metadata form when an upload of the asset is initiated. The syntax is `{ href: string; alt: string; } `|
| *uploadConfig* | Object | | | It is an object that contains customized configuration for the upload. |
| *featureSet* | Array | String | | The `featureSet:[ ]` property is used to enable or disable a particular functionaly in the Asset Selector application. To enable the component or a feature, you can pass a string value in the array or leave the array empty to disable that component. For example, you want to enable upload functionality in the Asset Selector, use the syntax `featureSet:[0:"upload"]`. |

<!--
| *rootPath* | String | No | /content/dam/ | Folder path from which Asset Selector displays your assets. `rootPath` can also be used in the form of encapsulation. For example, given the following path, `/content/dam/marketing/subfolder/`, Asset Selector does not allow you to traverse through any parent folder, but only displays the children folders. |
| *path* | String | No | | Path that is used to navigate to a specific directory of assets when the Asset Selector is rendered. |
| *expirationDate* | Function | No | | This function is used to set the usability period of an asset. |
| *disableDefaultBehaviour* | Boolean | No | False | It is a function that is used to enable or disable the selection of an expired asset. You can customize the default behavior of an asset that is set to expire. See [customize expired assets](/help/assets/asset-selector-customization.md#customize-expired-assets). |
-->
