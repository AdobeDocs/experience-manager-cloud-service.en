---
title: Customizing the UI
description: Learn about the different extension points that allow you to customize the UI of the Universal Editor to support the needs of your content authors.
exl-id: 8d6523c8-b266-4341-b301-316d5ec224d7
---
# Customizing the UI {#customizing-ui}

Learn about the different extension points that allow you to customize the UI of the Universal Editor to support the needs of your content authors.

## Disabling Publishing {#disable-publish}

Certain authoring workflows require content to be reviewed before it is published. In such situations, the option to publish should not be available to any authors.

The **Publish** button can therefore be suppressed enitrely in an app by adding the following metadata.

```html
<meta name="urn:adobe:aue:config:disable" content="publish"/>
```
