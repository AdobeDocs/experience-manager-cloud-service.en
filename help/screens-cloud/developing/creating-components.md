---
title: Creating Components
description: AEM components are used to hold, format, and render the content made available on your webpages. Follow this page to learn about authoring channels and rendering components.
exl-id: a81e812e-29ed-45de-b2d0-1fb0a8c5ce1a
---
# Creating Components {#creating-components}

AEM components are used to hold, format, and render the content made available on your webpages.

## Authoring Channels {#authoring-channels}

The channel is the central object of content delivered to a set of displays. Therefore, a content author would typically open a channel in the editor to add or modify content. Since the Channel is a ***cq:Page*** it will follow the same traditional UX pattern to add and change components on the channel.

However, since components within a channel are typically rendered full screen, the authoring experience will suffer when trying to edit single components or compose new orders. Therefore the channel will rely on selectors to render different views of the components. The authoring environment will leverage the edit selector to activate the custom channel rendering.

For example, `http://localhost:4502/editor.html/content/screens/we-retail/channels/idle.edit.html](http://localhost:4502/editor.html/content/screens/we-retail/channels/idle.edit.html`

The user does not have to take care of adding the selector to the URL while editing. A client side logic is listening to the layer switch event and adds the selector if a the channel has the dedicated resource type *screens/core/components/channel.*

## Rendering Components {#rendering-components}

To enable proper authoring, components need to provide the following two renderings:

| **Component** |**Renditions** |
|---|---|
| *my-component/my-component.html* |production rendering |
| *my-component/edit.html* |editing rendering in a smaller view |

The built-in components leverage the following client library categories:

| **Component** |**Client Library** |
|---|---|
| *cq.screens.components.edit* |CSS and JS which has to be loaded during authoring |
| *cq.screens.components.production* |CSS and JS which has to be loaded when the channel is running |
| *cq.screens.components* |shared CSS and JS |

>[!NOTE]
>
>To develop custom components, use the ***[AEM Screens sample component template](https://github.com/Adobe-Marketing-Cloud/aem-screens-component-template)***.
