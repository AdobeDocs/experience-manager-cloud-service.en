---
title: Customizing Page Authoring
description: Learn about the mechanisms that AEM as a Cloud Service provides to customize page authoring functionality.
exl-id: 98d3c7ab-46d2-4e8d-b0da-5c8a7b398135
feature: Developing
role: Admin, Architect, Developer
---
# Customizing Page Authoring {#customizing-page-authoring}

Adobe Experience Manager as a Cloud Service provides mechanisms to let you customize the page authoring functionality (and the [consoles](/help/implementing/developing/extending/consoles.md)) of your authoring instance.

## Clientlibs {#clientlibs}

Clientlibs let you extend the default implementation to enable new functionality, while reusing the standard functions, objects, and methods.

When customizing, you can create your own clientlib under `/apps.` The new clientlib must:

* Depend on the authoring clientlib `cq.authoring.editor.sites.page`.
* Be part of the appropriate `cq.authoring.editor.sites.page.hook` category.

See [Using Client-Side Libraries on AEM as a Cloud Service](/help/implementing/developing/introduction/clientlibs.md).

## Overlays {#overlays}

Overlays are based on node definitions and allow you to overlay the standard functionality in `/libs` with your own customized functionality in `/apps`.

When creating an overlay, a 1:1 copy of the original is not required, as the [sling resource merger](/help/implementing/developing/introduction/sling-resource-merger.md) allows for inheritance.

For more information, see the [JS documentation set](https://developer.adobe.com/experience-manager/reference-materials/6-5/jsdoc/ui-touch/editor-core/index.html).

For more information on overlays, see [Overlays for Adobe Experience Manager as a Cloud Service](/help/implementing/developing/introduction/overlays.md).

## Add New Layer (Mode) {#add-new-layer-mode}

When you are editing a page, there are various [modes](/help/sites-cloud/authoring/page-editor/introduction.md#page-modes) available. These modes are implemented using [layers](/help/implementing/developing/introduction/ui-structure.md#layer). These allow access to differing types of functionality for the same page content. Standard AEM modes include Edit, Layout, Developer, Timewarp, Live Copy Status, and Targeting.

### Layer Example: Live Copy Status {#layer-example-live-copy-status}

A standard AEM instance provides the MSM layer. This accesses data related to [multisite management](/help/sites-cloud/administering/msm/overview.md) and highlights it in the layer.

To see it in action, you may edit any language copy in the [WKND sample content](/help/implementing/developing/introduction/develop-wknd-tutorial.md) and select the **Live Copy Status** mode.

You can find the MSM layer definition (for reference) in:

`/libs/wcm/msm/content/touch-ui/authoring/editor/js/msm.Layer.js`

### Code Sample {#code-sample}

This is a sample package showing how to create a layer (mode) for MSM view.

You can find the code of this page on [GitHub](https://github.com/Adobe-Marketing-Cloud/aem-authoring-new-layer-mode).

## Add New Selection Category to Asset Browser {#add-new-selection-category-to-asset-browser}

The asset browser shows assets of various types/categories (for example, images and documents). The assets can also be filtered by these asset categories.

### Code Sample {#code-sample-1}

`aem-authoring-extension-assetfinder-flickr` is a sample package showing how to add a group to the asset finder. This example connects to [Flickr](https://www.flickr.com)'s public stream and shows them in the side panel.

You can find the code of this page on [GitHub](https://github.com/Adobe-Marketing-Cloud/aem-authoring-extension-assetfinder-flickr).

## Filtering Resources {#filtering-resources}

When authoring pages, the user must often select from resources in a list.

To keep the list to a reasonable size and also relevant to the use case, a filter can be implemented in the form of a custom predicate. For example, if the `pathbrowser` Granite component is used to allow the user to select the path to a particular resource, the paths presented can be filtered in the following way:

* Implement the custom predicate by implementing [`com.day.cq.commons.predicate.AbstractNodePredicate`](https://developer.adobe.com/experience-manager/reference-materials/cloud-service/javadoc/com/day/cq/commons/predicate/package-summary.html) interface.
* Specify a name for the predicate, and refer that name when using the `pathbrowser`.

For further detail on creating a custom predicate, see [this article](/help/implementing/developing/introduction/query-builder-custom-predicate.md).

## Add New Action to a Component Toolbar {#add-new-action-to-a-component-toolbar}

Each component usually has a toolbar that provides access to a range of actions that can be taken on that component.

### Code Sample {#code-sample-2}

`aem-authoring-extension-toolbar-screenshot` is a sample package showing how to create a custom toolbar action to render components.

You can find the code of this page on [GitHub](https://github.com/Adobe-Marketing-Cloud/aem-authoring-extension-toolbar-screenshot).

## Add New In-Place Editor {#add-new-in-place-editor}

### Standard In-Place Editor {#standard-in-place-editor}

In a standard AEM installation:

1. `/libs/cq/gui/components/authoring/editors/clientlibs/core/js/editors/editorExample.js` holds definitions of the various editors available.

1. There is a connection between the editor and each resource type (as in component) that can use it:

    * `cq:inplaceEditing`

      for example:

        * `/libs/foundation/components/text/cq:editConfig`
        * `/libs/foundation/components/image/cq:editConfig`

            * property: `editorType`

              Defines the type of inline editor that is used when the in-place editing is triggered for that component; for example, `text`, `textimage`, `image`, `title`.

1. Additional configuration details of the editor can be configured using a `config` node containing configurations and a `plugin` node to contain necessary plugin configuration details.


The following is an example of defining aspect ratios for the image cropping plugin of the image component.

```xml
   <cq:inplaceEditing
           jcr:primaryType="cq:InplaceEditingConfig"
           active="{Boolean}true"
           editorType="image">
           <config jcr:primaryType="nt:unstructured">
               <plugins jcr:primaryType="nt:unstructured">
                   <crop jcr:primaryType="nt:unstructured">
                       <aspectRatios jcr:primaryType="nt:unstructured">
                           <_x0031_6-10
                               jcr:primaryType="nt:unstructured"
                               name="16 : 10"
                               ratio="0.625"/>
                       </aspectRatios>
                   </crop>
               </plugins>
           </config>
   </cq:inplaceEditing>
```

>[!NOTE]
>
>AEM crop ratios, as set by the `ratio` property, are defined as **height/width**. This differs from the conventional definition of width/height and is done for legacy compatibility reasons. The authoring users will not be aware of any difference provided you define the `name` property clearly since this is what is displayed in the UI.

#### Creating a New In-Place Editor {#creating-a-new-in-place-editor}

To implement a new in-place editor (within your clientlib):

1. Implement:

    * `setUp`
    * `tearDown`

1. Register the editor (includes the constructor):

    * `editor.register`

1. Provide the connection between the editor and every resource type (as in component) that can use it.

#### Code Sample for Creating a New In-Place Editor {#code-sample-for-creating-a-new-in-place-editor}

`aem-authoring-extension-inplace-editor` is a sample package showing how to create an in-place editor in AEM.

You can find the code of this page on [GitHub](https://github.com/Adobe-Marketing-Cloud/aem-authoring-extension-inplace-editor).

## Add a New Page Action {#add-a-new-page-action}

To add a new page action to the page toolbar, for example, a **Back to Sites** (console) action.

### Code Sample {#code-sample-3}

`aem-authoring-extension-header-backtosites` is a sample package showing how to create a custom header bar action to jump back to the Sites console.

You can find the code of this page on [GitHub](https://github.com/Adobe-Marketing-Cloud/aem-authoring-extension-header-backtosites).

## Customizing the Request for Activation Workflow {#customizing-the-request-for-activation-workflow}

The out-of-the-box workflow, **Request for Activation**:

* Will automatically appear on the appropriate menu when a content author **does not have** the appropriate replication rights, but **does have** membership of DAM-Users and Authors. 

* Otherwise, nothing is displayed, as replication rights have been removed.

To have customized behavior on such activation, you can overlay the **Request for Activation** workflow:

1. In `/apps` overlay the **Sites** wizard `/libs/wcm/core/content/common/managepublicationwizard`

   * This itself, overrides the common instance of `/libs/cq/gui/content/common/managepublicationwizard`.

1. Update the workflow model and related configurations/scripts as required.
1. Remove the right to the `replicate` action from all appropriate users for all relevant pages. To have this workflow triggered as a default action when any of the users, try to publish (or replicate) a page.
