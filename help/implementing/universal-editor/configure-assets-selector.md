---
title: Configuring the Assets Selector for the Universal Editor
description: Understand how you can configure the assets selector for use with the Universal Editor.
feature: Developing
role: Admin, Developer
---

# Configuring the Assets Selector for the Universal Editor {#configure-assets-selector}

Understand how you can configure the assets selector for use with the Universal Editor.

## Overview {#overview}

The Universal Editor uses [the assets selector](/help/assets/overview-asset-selector.md#using-asset-selector) to allow authors to browse and select assets for insertion into their content.

The assets selector is configurable within the Universal Editor by using [component filters.](/help/implementing/universal-editor/filtering.md) This document describes what configuration options are available.

>[!NOTE]
>
>When you start a Universal Editor project, there are no filters in place for the assets selector. Authors will have access to all assets that their user permissions normally allow.

## Filter Definition {#filter-definition}

The filter definition for the assets selector has a simple structure.

```json
[
  {
    "id": "assets-filter",
    "assets": {...}
   }
]
```

## Filter Options {#filter-options}

The `assets` filter can have the following options.

* `deliveryTier?`: - Defines which of the following delivery tiers to use:
   * `dm`: Dynamic Media (preferred) with fallback to `publish` if necessary
   * `publish`: AEM publish instance
* `repoNames?`: String - List of AEM repositories which can be used to select images.
   * Default: all delivery repos
* `selectionTier?`: String - AEM tiers to select assets from
   * Default: `["author", "delivery"]`
* `disableRemote?`: Boolean - Disable remote repository support
* `preselectedTypes?`: String - Preselected file types to be applied as default filter in Asset Selector
* `minMaxDimensions?`: Object - Provides minimum and/or maximum dimensions (in pixels) to be applied as default filter in the asset selector
  * `widthMin?`: Number - Minimum width
  * `widthMax?`: Number - Maximum width
  * `heightMin?`: Number - Minimum height
  * `heightMax?`: Number - Maximum height
* `minMaxFileSize?`: Object - Provide minimum and/or maximum file size (in bytes) to be applied as default filter in the asset selector
  * `min?`: Number - Minimum file size
  * `max?`: number - Maximum file size
* `customFileTypeFilters?`: Object - Provides custom file type filters to be shown in the asset selector
  * `label`: String - Label to be shown in the asset select UI
  * `value`: String - Value of the file type to be filtered
* `displayFilters?`: Boolean - Used to disable the filters UI in the asset selector; true by default

## Example {#example}

The following example contains most options for illustration purposes.

```json
[
  {
    "id": "assets-filter",
    "assets": {
      "deliveryTier": "dm",
      "repoNames": ["thisRepo", "thatRepo"],
      "selectionTier": ["author", "delivery"],
      "disableRemote": true,
      "preselectedTypes": ["png", "svg", "jpg", "gif"],
      "minMaxDimensions": {
        "widthMin": 640,
        "widthMax": 640,
        "heightMin": 480,
        "heightMax": 480
      },
      "minMaxFileSize": {
        "min": 1024,
        "max": 1024
      }
    }
   }
]
```

## Additional Resources {#additional-resources}

For details on the assets selector, please see the document [Micro-Frontend Asset Selector](/help/assets/overview-asset-selector.md#using-asset-selector) in the assets documentation.
