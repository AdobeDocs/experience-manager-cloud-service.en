---
title: Asset Selector for [!DNL Adobe Experience Manager] as a [!DNL Cloud Service]
description: Use functions to customize Asset selector within your application.
role: Admin, User
exl-id: 0fd0a9f7-8c7a-4c21-9578-7c49409df609
---
# Asset Selector customizations {#asset-selector-customization}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|
 
Asset Selector allows you to customize various components according to preferences, requirements, or functional needs. You can customize the following components [Micro-Frontend Asset Selector](#overview-asset-selector.md):

* [Customize filter panel](#customize-filter-panel)
* [Customize information in modal view](#customize-info-in-modal-view)
* [Enable or disable drag and drop mode](#enable-disable-drag-and-drop)
* [Selection of Assets](#selection-of-assets)
* [Customize expired assets](#customize-expired-assets)
* [Contextual invocation filter](#contextual-invocation-filter)

You need to define the prerequisites in the **index.html** file or a similar file within your application implementation to define the authentication details to access the [!DNL Experience Manager Assets] repository. Once done, you can add code snippets as per your requirement.

## Customize filter panel {#customize-filter-panel}

You can add the following code snippet in `assetSelectorProps` object to customize the filter panel:

```
filterSchema: [
    {
    header: 'File Type',
    groupKey: 'TopGroup',
    fields: [
    {
    element: 'checkbox',
    name: 'type',
    options: [
    {
    label: 'Images',
    value: '<comma separated mimetypes, without space, that denote all images, for e.g., image/>',
    },
    {
    label: 'Videos',
    value: '<comma separated mimetypes, without space, that denote all videos for e.g., video/,model/vnd.mts,application/mxf>'
    }
    ]
    }
    ]
    },
    {
    fields: [
    {
    element: 'checkbox',
    name: 'type',
    options: [
    { label: 'JPG', value: 'image/jpeg' },
    { label: 'PNG', value: 'image/png' },
    { label: 'TIFF', value: 'image/tiff' },
    { label: 'GIF', value: 'image/gif' },
    { label: 'MP4', value: 'video/mp4' }
    ],
    columns: 3,
    },
    ],
    header: 'Mime Types',
    groupKey: 'MimeTypeGroup',
    },
    {
    fields: [
    {
    element: 'checkbox',
    name: 'property=metadata.application.xcm:keywords.value',
    options: [
    { label: 'Fruits', value: 'fruits' },
    { label: 'Vegetables', value: 'vegetables'}
    ],
    columns: 3,
    },
    ],
    header: 'Food Category',
    groupKey: 'FoodCategoryGroup',
    }
],
```

## Customize information in modal view {#customize-info-in-modal-view}

You can customize the details view of an asset when you click the ![info icon](assets/info-icon.svg) icon. Execute the code below:

```
// Create an object infoPopoverMap and set the property `infoPopoverMap` with it in assetSelectorProps
const infoPopoverMap = (map) => {
// for example, to skip `path` from the info popover view
let defaultPopoverData = PureJSSelectors.getDefaultInfoPopoverData(map);
return defaultPopoverData.filter((i) => i.label !== 'Path')
};
assetSelectorProps.infoPopoverMap = infoPopoverMap;
```

## Enable or disable drag and drop mode {#enable-disable-drag-and-drop}

Add the following properties to `assetSelectorProp` to enable drag and drop mode. To disable drag and drop, replace the `true` parameter with `false`.

```
rail: true,
acvConfig: {
dragOptions: {
allowList: {
'*': true,
},
},
selectionType: 'multiple'
}

// the drop handler to be implemented
function drop(e) {
e.preventDefault();
// following helps you get the selected assets – an array of objects.
const data = JSON.parse(e.dataTransfer.getData('collectionviewdata'));
}
```

## Selection of Assets {#selection-of-assets}

Selected Asset Type is an array of objects that contains the asset information when using the `handleSelection`, `handleAssetSelection`, and `onDrop` functions.

Execute the following steps to configure the selection of single or multiple assets:

```
acvConfig: {
selectionType: 'multiple' // 'single' for single selection
}
// the `handleSelection` callback, always gets you the array of selected assets
```

**Schema Syntax**

```
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
        'https://ns.adobe.com/adobecloud/rel/rendition': Array<{
            href: string;
            type: string;
            'repo:size': number;
            width: number;
            height: number;
            [others: string]: any;
        }>;
    };
}
```

The following table describes some of the important properties of the Selected Asset object.

| Property | Type | Description |
|---|---|---|
| *repo:repositoryId* | string | Unique identifier for the repository where the asset is stored. |
| *repo:id*| string | Unique identifier for the asset. |
| *repo:assetClass* | string | The classification of the asset (For example, image, or video, document). |
| *repo:name*| string | The name of the asset, including the file extension. |
| *repo:size*| number| The size of the asset in bytes.|
| *repo:path*| string | The location of the asset within the repository. |
| *repo:ancestors*| `Array<string>`| An array of ancestor items for the asset in the repository. |
| *repo:state*| string | Current state of the asset in the repository (For example, active, deleted, and so on). |
| *repo:createdBy*| string | The user or system that created the asset. |
| *repo:createDate* | string | The date and time when the asset was created. |
| *repo:modifiedBy* | string | The user or system that last modified the asset. |
| *repo:modifyDate* | string| The date and time when the asset was last modified. |
| *dc:format*| string | The format of the asset, such as the file type (For example, JPEG, PNG, and so on).|
| *tiff:imageWidth* | number| The width of an asset.|
| *tiff:imageLength* | number | The height of an asset. |
| *computedMetadata* | `Record<string, any>` | An object which represents a bucket for all the asset's metadata of all kinds (repository, application, or embedded metadata). |
| *_links* | `Record<string, any>` | Hypermedia links for the associated asset. Includes links for resources such as metadata and renditions. |
| *`_links.<https://ns.adobe.com/adobecloud/rel/rendition>`* | `Array<Object>`| Array of objects containing information about renditions of the asset. |
| *`_links.<https://ns.adobe.com/adobecloud/rel/rendition[].href>`* | string | The URI to the rendition.|
| *`_links.<https://ns.adobe.com/adobecloud/rel/rendition[].type>`* | string | The MIME type of the rendition.|
| *`_links.<https://ns.adobe.com/adobecloud/rel/rendition[].repo:size>`* | number | The size of the rendition in bytes.|
| *`_links.<https://ns.adobe.com/adobecloud/rel/rendition[].width>`* | number | The rendition's width. |
| *`_links.<https://ns.adobe.com/adobecloud/rel/rendition[].height>`* | number | The rendition's height. |

### Handling selection of Assets using Object Schema {#handling-selection}

The `handleSelection` property is used to handle single or multiple selections of Assets in Assets Selector. The example below states the syntax of usage of `handleSelection`. 

![handle-selection](assets/handling-selection.png)

### Disabling selection of Assets {#disable-selection}

Disable selection is used to hide or disable the assets or folders from being selectable. It hides the select checkbox from the card or asset which refrains it from getting selected. To use this feature, you can declare the position of an asset or folder that you want to disable in an array. For example, if you want to disable the selection of a folder appearing at first position, you can add the following code:
    `disableSelection: [0]:folder`

You can provide the array with a list of mime types (such as image, folder, file, or other mime types for example, image/jpeg) that you want to disable. The mime types that you declare are mapped into `data-card-type` and `data-card-mimetype` attributes of an asset. 

Additionally, Assets with disabled selection are draggable. To disable drag and drop of a particular asset type, you can use `dragOptions.allowList` property. 

The syntax of disable selection is as follows:

```
(args)=> {
    return(
        <ASDialogWrapper
            {...args}
            disableSelection={args.disableSelection}
            handleAssetSelection={action('handleAssetSelection')}
            handleSelection={action('handleSelection')}
            selectionType={args.selectionType}
        />
    );
}
```

>[!NOTE]
>
> In case of an asset, the select checkbox is hidden, whereas, in case of a folder, the folder is unselectable but the navigation of the mentioned folder still appears.

<!--For a complete list of properties and detailed example, visit [Asset Selector Code Example](https://github.com/adobe/aem-assets-selectors-mfe-examples).-->

## Customize expired assets {#customize-expired-assets}

Asset Selector allows you to control the usage of an expired asset. You can customize the expired asset with an **Expiring soon** badge that can help you know in advance about the assets that are going to expire within 30 days from the current date. Moreover, this can be customized as per the requirement. You can also allow the selection of an expired asset on the canvas or vice versa. The customization of an expired asset can be done using some code snippets in various ways:

<!--{
    getExpiryStatus: function, // to control Expired/Expiring soon badges of the asset
    allowSelectionAndDrag: boolean, // set true to allow the selection of expired assets on canvas, set false, otherwise.
}-->

```
expiryOptions: {
    getExpiryStatus: getExpiryStatus;
}
```

### Selection of an expired asset {#selection-of-expired-asset}

You can customize the usage of an expired asset to make it either selectable or unselectable. You can customize whether you want to allow the drag and drop of an expired asset on the Asset Selector canvas or not. To do this, use the following parameters to make an asset unselectable on the canvas:

```
expiryOptions:{
    allowSelectionAndDrop: false;
}
```
<!--
Additionally, To do this, navigate to **[!UICONTROL Disable default expiry behavior]** under the [!UICONTROL Controls] tab and set the boolean value to `true` or `false` as per the requirement. If `true` is selected, you can see the select box over the expired asset, otherwise it remains unselected. You can hover to the info icon of an asset to know the details of an expired asset. 

![Disable default expiry behavior](assets/disable-default-expiry-behavior.png)-->

### Setting duration of an expired asset {#set-duration-of-expired-asset}

The following code snippet helps you set **Expiring Soon** badge for the assets that are expiring within next five days: <!--The `expirationDate` property is used to set the expiration duration of an asset. Refer to the code snippet below:-->

```
/**
  const getExpiryStatus = async (asset) => {
  if (!asset.expirationDate) {
    return null;
  }
  const currentDate = new Date();
  const millisecondsInDay = 1000 * 60 * 60 * 24;
  const fiveDaysFromNow = new Date(value: currentDate.getTime() + 5 * millisecondsInDay);
  const expirationDate = new Date(asset.expirationDate);
  if (expirationDate.getTime() < currentDate.getTime()) {
    return 'EXPIRED';
  } else if (expirationDate.getTime() < fiveDaysFromNow.getTime()) {
    return 'EXPIRING_SOON';
  } else {
    return 'NOT_EXPIRED';
  }
};
```

<!--In the above code snippet, the `getExpiryStatus` function is used to show the **Expiring soon** badge that have expiration date stored in `customExpirationDate`. Additionally, it sets the expiration date of an asset to five days from the current date. The `millisecondsInDay` helps you set expiry of an asset by specifying the time range in milliseconds. You can replace milliseconds with hours directly or customize function as per the requirement. Whereas, the `getTime()` function returns the number of milliseconds for the mentioned date. See [properties](#asset-selector-properties) to know about `expirationDate` property.--> 

Refer to the following example to understand how the property works to fetch the current date and time: 

```
const currentData = new Date();
currentData.getTime(),
```

returns `1718779013959` which is as per the date format 2024-06-19T06:36:53.959Z. 

### Customize toast message of an expired asset {#customize-toast-message}

The `showToast` property is used to customize the toast message that you want to show on an expired asset.

Syntax:

```
{
    type: 'ERROR', 'NEUTRAL', 'INFO', 'SUCCESS',
    message: '<message to be shown>',
    timeout: optional,
}
```

The default timeout is 500 milliseconds. Whereas, you can modify it as per the requirement. Additionally, passing the value `timeout: 0` keeps the toast open until you click on the cross button.

Below is an example to show a toast message when it is required to disallow selection for a folder and show a corresponding message:

```
const showToast = {
    type: 'ERROR',
    message: 'Folder cannot be selected',
    timeout: 5000,
}
```

Use the following code snippet to show toast message for the usage of an expired asset:

```
(args) => {
    const [selectedAssets, setSelectedAssets] = useState([]);
    const [showToast, setShowToast] = React.useState(false);
    const handleAssetSelection = (assets) => {
        let directorySelectedFlag = false;
        const temp = assets.filter((asset) => {
            if (asset['repo:assetClass'] === 'directory') {
                directorySelectedFlag = true;
                setShowToast(true);
            }
            return !(asset['repo:assetClass'] === 'directory');
        });
        if (!directorySelectedFlag) {
            setShowToast(false);
        }
        setSelectedAssets(temp);
    };
    return (
        <ASDialogWrapper
            {...args}
            showToast={showToast ? args.showToast : null}
            selectedAssets={selectedAssets}
            handleAssetSelection={handleAssetSelection}
        />
    );
}
```

## Contextual invocation filter{#contextual-invocation-filter}

Asset Selector allows you to add a tag picker filter. It supports a tag group which combines all the relevant tags to a particular tagging group. Additionally, it allows you to select additional tags corresponding to the asset that you are looking for. Moreover, you can also set the default tag groups under the contextual invocation filter that are mostly used by you so that they are accessible to you on the go.

>![NOTE]
>
> * You need to add contextual invocation code snippet to enable tagging filter in the search.
> * It is mandatory to use name property corresponding to the tag group type `(property=xcm:keywords.id=)`. 

Syntax:

```
const filterSchema=useMemo(() => {
    return: [
        {
            element: 'taggroup',
            name: 'property=xcm:keywords.id='
        },
    ];
}, []);
```

To add tag groups in the filters panel, it is mandatory to add at least one tag group as default. Additionally, use the below code snippet to add the default tags that are pre-selected from the tag group.

```
export const WithAssetTags = (props) = {
const [selectedTags, setSelectedTags] = useState (
new Set(['orientation', 'color', 'facebook', 'experience-fragments:', 'dam', 'monochrome'])
const handleSelectTags = (selected) => {
setSelectedTags (new Set (selected)) ;
};
const filterSchema = useMemo ((); => {
    return {
        schema: [
            ｛
                fields: [
                    {
                    element: 'checkbox', 
                    name: 'property=xcm:keywords=', 
                    defaultValue: Array. from(selectedTags), 
                    options: assetTags, 
                    orientation: 'vertical',
                    },
                ],
    header: 'Asset Tags', 
    groupkey: 'AssetTagsGroup',
        ],
    },
｝；
}, [selectedTags]);
```

![tag group filter](assets/tag-group.gif)

## Upload in Asset Selector {#upload-in-asset-selector}

You can upload files or folders to Asset Selector from your local file system. To upload files using the local file system, you generally need to use an upload  feature provided by a Asset Selector micro front-end application. Various code snippets required to invoke upload in asset selector involves:

* [Basic upload form code snippet](#basic-upload)
* [Upload with metadata](#upload-with-metadata)
* [Customized upload](#customized-upload)
* [Upload using third party sources](#upload-using-third-party-source)

### Basic upload form {#basic-upload}

```
import { AllInOneUpload } from '@assets/upload';
import { TextField, ContextualHelp } from '@adobe/react-spectrum';

const repoId = 'author-p52554-e145207-cmstg.adobeaemcloud.com'
const apiToken = 'eyJhbG....';
const targetUploadPath = '/content/dam/hydrated-assets/cq/as/cq-assets-upload-storybook-testing';

export const UploadExample = () => {
    return (
        <>
            <TextField
                marginStart="size-200"
                width="size-6000"
                isDisabled={true}
                label="Target Upload Path"
                value={targetUploadPath}
                contextualHelp={
                    <ContextualHelp>
                        <Content>Use Storybook Controls panel to change the default upload location</Content>
                    </ContextualHelp>
                }
            />
            <AllInOneUpload
                repositoryId={repoId}
                apiToken={apiToken}
                targetUploadPath={targetUploadPath}
            />
        <>
    )
}
```

### Upload with metadata {#upload-with-metadata}

```
import { AllInOneUpload } from '@assets/upload';

const repoId = 'author-p52554-e145207-cmstg.adobeaemcloud.com'
const apiToken = 'eyJhbG....';
const targetUploadPath = '/content/dam/hydrated-assets/cq/as/cq-assets-upload-storybook-testing';

/**
 * see https://git.corp.adobe.com/CQ/assets-upload/blob/main/packages/@assets/upload/stories/data/SampleMetadataSchemas.ts
 * for full schema shape used in rendered example below
 */
const metadataSchema = [
    {
        mapToProperty: 'gmo:lineofBusiness',
        label: 'Line of Business',
        placeholder: 'Select one',
        required: true,
        element: 'dropdown',
        dropdownOptions: [
            {
                id: 'corporate',
                name: 'Corporate',
            },
            {
                id: 'digital-media-dme',
                name: 'Digital Media (DMe)',
            },
            {
                id: 'digital-experience-dx',
                name: 'Digital Experience (DX)',
            },
            {
                id: 'business-solutions',
                name: 'Business Solutions',
            },
        ],
    },
    // ... see link above for full schema
    {
        mapToProperty: 'dam:assetStatus',
        value: 'approved',
        // hidden metadata element, this metadata will be applied to the asset without rendering UI for user input
        element: 'hidden',
    },
];

const handleMetadataFormChange = (event: MetadataChangeEvent) => {
    const { property, value } = event;

    console.log({ property, value });
}

const UploadExampleWithMetadataForm = () => {
    return (
        <AllInOneUpload
            repositoryId={repoId}
            apiToken={apiToken}
            targetUploadPath={targetUploadPath}
            metadataSchema={sampleMetadataSchema}
            onMetadataFormChange={handleMetadataFormChange}
        />
    )
}
```

### Customized upload {#customized-upload}

```
const MultipleAllInOneUploadExample = () => {
    const mfeRef = React.useRef<{ iframeRef: { current: HTMLIFrameElement } }>(null);

    return (
        <>
            <Button
                onPress={() => UploadCoordinator.initiateUpload(mfeRef.current?.iframeRef?.current)}
            >
                External Initiate Upload
            </Button>
            <AllInOneUpload
                {...otherProps}
                ref={mfeRef}
            />
        <>
    );
}
```

### Upload using third party sources {#upload-using-third-party-source}

```
import { useState, useRef } from 'react';
import { AllInOneUpload, UploadCoordinator } from '@assets/upload';
import { Button, Flex, Divider } from '@adobe/react-spectrum';
import { sampleMetadataSchema } from './SampleMetadataSchemas';

const repoId = 'author-p52554-e145207-cmstg.adobeaemcloud.com'
const apiToken = 'eyJhbG....';
const targetUploadPath = '/content/dam/hydrated-assets/cq/as/cq-assets-upload-storybook-testing';

const defaultFiles = [
    new File(['file-content'], 'Controlled File 1'),
    new File(['file-content-with-more'], 'Controlled File 2')
];

const ControlledUploadExample = () => {
    const [controlledFiles, setControlledFiles] = useState<File[]>(defaultFiles)
    const inputRef = React.useRef<HTMLInputElement>(null);

    const handleFileInputChange = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        if (e.target.files) {
            setMyFiles([...e.target.files]);
        }
    }, []);

    return (
        <Flex height="100%" alignItems="center" direction="column">
            <Flex direction="row" alignItems="center" justifyContent="center">
                <Button
                    variant="accent"
                    onPress={() => UploadCoordinator.initiateUpload()}
                    isDisabled={files.length < 1}
                >
                    External Initiate Upload
                </Button>
                <Button
                    variant="secondary"
                    onPress={() => {
                        inputRef.current?.click();
                    }}
                >
                    External Browse files
                </Button>
            </Flex>
            <Divider size="M" marginTop="size-200" />
            <AllInOneUpload
                repositoryId={repoId}
                apiToken={apiToken}
                targetUploadPath={targetUploadPath}
                files={controlledFiles}
                onFilesChange={setControlledFiles}
                hideUploadButton={true}
                metadataSchema={sampleMetadataSchema}
            />
            <input
                ref={inputRef}
                type="file"
                style={{ display: 'none' }}
                onChange={handleFileInputChange}
                multiple={true}
            />
        </Flex>
    )
}
```

>[!MORELIKETHIS]
>
>* [Asset Selector properties](/help/assets/asset-selector-properties.md)
>* [Integrate Asset Selector with various applications](/help/assets/integrate-asset-selector.md)
>* [Asset Selector properties](/help/assets/asset-selector-properties.md)
>* [Integrate Asset Selector with Dynamic Media with OpenAPI capabilities](/help/assets/integrate-asset-selector-dynamic-media-open-api.md)
