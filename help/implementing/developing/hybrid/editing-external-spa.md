---
title: Editing an External SPA within AEM
description: This document describes the recommended steps to upload a standalone SPA to an AEM instance, add editable sections of content, and enable authoring.
---
# Editing and External SPA within AEM {#external-spa-within-aem}

When deciding [what level of integration](/help/implementing/developing/headful-headless.md) you would like to have between your external SPA and AEM, it is often clear that you need to be able to view and edit the SPA within AEM.

## Overview {#overview}

This document describes the recommended steps to upload a standalone SPA to an AEM instance, add editable sections of content, and enable authoring.

## Prerequisites {#prerequisites}

The prerequisites are simple.

* Ensure an instance of AEM is running locally.
  * For the examples in this document, it is assumed that the 
* Create a base AEM SPA project using [the AEM Project Archetype.](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html?lang=en#available-properties)
  * This will form the basis of the AEM project which will be updated to include the external SPA.
  * For the samples in this document, we are using the starting point of [the WKND SPA project.](https://experienceleague.adobe.com/docs/experience-manager-learn/sites/spa-editor/spa-editor-framework-feature-video-use.html?lang=en#spa-editor)
* A working, external React SPA

## Upload SPA to AEM Project {#upload-spa-to-aem-project}

1. Replace `src` in the `/ui.frontend` project folder with your React application's `src` folder.
1. Include any additional dependencies in the app's `package.json` in the `/ui.frontend/package.json` file. Ensure the SPA SDK dependencies are of [recommended versions.](/help/implementing/developing/hybrid/getting-started-react.md#dependencies)
1. Include any customizations in the `/public` folder.
1. Include any inline scripts or styles added in the `/public/index.html` file.

## Configure the Remote SPA {#configure-remote-spa}

### Include Adobe SPA SDK Packages {#include-spa-sdk-packages}

To take advantage of AEM SPA features, there are dependencies on the following three packages.

* [`@adobe/aem-react-editable-components`](https://github.com/adobe/aem-react-editable-components)
* [`@adobe/aem-spa-component-mapping`](https://www.npmjs.com/package/@adobe/aem-spa-component-mapping)
* [`@adobe/aem-spa-page-model-manager`](https://www.npmjs.com/package/@adobe/aem-spa-model-manager)

`@adobe/aem-spa-page-model-manager` provides the API for initializing a Model Manager and retrieving the model from the AEM instance. This model can then be used to render AEM components using APIs from `@adobe/aem-react-editable-components` and `@adobe/aem-spa-component-mapping`.

#### Installation {#installation}

Run the following npm command to install.

```shell
npm install --save @adobe/aem-spa-component-mapping @adobe/aem-spa-page-model-manager @adobe/aem-react-editable-components
```

### ModelManager Initialization {#model-manager-initialization}

Before the app renders, the [`ModelManager`](/help/implementing/developing/hybrid/blueprint.md#pagemodelmanager) needs to be initialized to handle the creation of the AEM `ModelStore`.

This needs to be done within the `src/index.js` file of your application or wherever the rendering of application to root node is done.

For this, we can use `initializationAsync` API provided by the `ModelManager`.

The following screenshot shows enabling initialization of the `ModelManager` in a simple React application. The only constraint is that `initializationAsync` needs to be called before `ReactDOM.render()`.

![Initialize ModelManager](assets/external-spa-initialize-modelmanager.png)

In this example, the `ModelManager` is initialized and an empty `ModelStore` is created.

`initializationAsync` can optionally accept an `options` object as a parameter:

* `path` - On initialization, the model at the defined path is fetched and stored in the `ModelStore`. This can be used to fetch the `rootModel` at initialization if needed.
* `modelClient` - Allows providing a custom client responsible for fetching the model.
* `model` - A `model` object passed as a parameter typically populated when [using SSR.](/help/implementing/developing/hybrid/ssr.md)

### AEM Authorable Leaf Components {#authorable-leaf-components}

1. Create/identify an AEM component for which an authorable React component will be created. In this example, we are using the WKND project's text component.

   ![WKND text component](assets/external-spa-text-component.png)

1. Create a simple React text component in the SPA. In this example, a new file `Text.js` has been created with the following content.

   ![Text.js](assets/external-spa-textjs.png)

1. Create a config object to specify the attributes required for enabling AEM editing.

   ![Create config object](assets/external-spa-config-object.png)

   * `resourceType` is mandatory to map the React component to the AEM component and enable editing when opening in the AEM editor.

1. Use the wrapper function `withMappable`.

   ![Use withMappable](assets/external-spa-withmappable.png)

   This wrapper function maps the React component to the AEM `resourceType` specified in the config and enables editing capabilities when opened in the AEM editor. For standalone components, it will also fetch the model content for the specific node.

   >[!NOTE]
   >
   >In this example there are separate versions of the component - AEM wrapped and unwrapped React components. The wrapped version needs to be used when explicitly using the component. When the component is part of a page, you can continue using the default component as done currently in the SPA editor.

1. Render content in the component.

   The JCR properties of the text component appear as follows in AEM.

   ![Text component properties](assets/external-spa-text-properties.png)

   These values are passed as properties to the newly-created `AEMText` React component and can be used to render the content.

   ```javascript
   import React from 'react';
   import { withMappable } from '@adobe/aem-react-editable-components';

   export const TextEditConfig = {
       // Empty component placeholder label
       emptyLabel:'Text', 
       isEmpty:function(props) {
          return !props || !props.text || props.text.trim().length < 1;
       },
       // resourcetype of the AEM counterpart component
       resourceType:'wknd-spa-react/components/text'
   };

   const Text = ({ text }) => (<div>{text}</div>);

   export default Text;

   export const AEMText = withMappable(Text, TextEditConfig);
   ```

   This is how the component will appears when the AEM configurations are complete.

   ```javascript
   const Text = ({ cqPath, richText, text }) => {
      const richTextContent = () => (
         <div className="aem_text" id={cqPath.substr(cqPath.lastIndexOf('/') + 1)} data-rte-editelement dangerouslySetInnerHTML={{__html: text}}/>
      );
      return richText ? richTextContent() : (<div className="aem_text">{text}</div>);
   };
   ```

   >[!NOTE]
   >
   >In this example, we have made further customizations to the rendered component to match the existing text component. This, however, is not related to AEM authoring.

#### Add Authorable Components to the Page {#add-authorable-component-to-page}

Once the authorable React components are created, we can use them throughout the application.

Let's take an example page where we need to add a text from the WKND SPA project. For this example, we want to display the text "Hello World!" on `/content/wknd-spa-react/us/en/home.html`.

1. Determine the path of the node to be displayed.

   * `pagePath`: The page which contains the node, i.e. `/content/wknd-spa-react/us/en/home`
   * `itemPath`: Path to the node within the page, i.e. `root/responsivegrid/text`
     * This consists of the names of the containing items on the page.

   ![Path of the node](assets/external-spa-path.png)

1. Add component at required position in the page.

   ![Add component to the page](assets/external-spa-add-component.png)

   The `AEMText` component can be added at the required position within the page with `pagePath` and `itemPath` values set as properties. `pagePath` is a mandatory property.

#### Verify Editing of Text Content on AEM {#verify-text-edit}

We can now test the component on the running AEM instance.

