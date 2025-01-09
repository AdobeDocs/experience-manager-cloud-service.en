---
title: Component Definition
description: Understand the JSON contract between the component definition and the Universal Editor in detail.
feature: Developing
role: Admin, Architect, Developer
---

# Component Definition {#component-definition}

Understand the JSON contract between the component definition and the Universal Editor in detail.

## Overview {#overview}

The `component-definition.json` file defines the components available to your content authors for the project. This document explains in detail the purpose of this file and how the Universal Editor uses it to present your authors with page authoring components.

>[!TIP]
>
>You do not need to create your own `component-definition.json` file from scratch. The project boilerplate that you use to [bootstrap your project](/help/edge/wysiwyg-authoring/edge-dev-getting-started.md) contains a fully-functioning `component-definition.json` file that you can adapt to your needs.

## Example Component Definition {#example}

The following is a complete, but simplified `component-definition.json` file for reference.

```json
{
  "groups": [
    {
      "title": "General Components",
      "id": "general",
      "components": [
        {
          "title": "Text",
          "id": "text",
          "plugins": {
            "aem": {
              "page": {
                "resourceType": "wknd/components/text",
                "template": {
                  "text": "Default Text"
                }
              }
            },
            "aem65": {
              "page": {
                "resourceType": "wknd/components/text",
                "template": {
                  "text": "Default Text"
                }
              }
            }
          }
        },
      }
   ]
}
```

## groups {#groups}