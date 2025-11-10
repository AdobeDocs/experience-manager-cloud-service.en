---
title: Configuring the RTE for the Universal Editor
description: Understand how you can configure the rich text editor (RTE) in the Universal Editor.
feature: Developing
role: Admin, Developer
exl-id: 350eab0a-f5bc-49c0-8e4d-4a36a12030a1
---
# Configuring the RTE for the Universal Editor {#configure-rte}

Understand how you can configure the rich text editor (RTE) in the Universal Editor.

>[!NOTE]
>
>This documentation applies to the new RTE for the Universal Editor, which is available as an early adopter feature. If you are interested in testing this new feature, [please see the release notes for details.](/help/release-notes/universal-editor/current.md#new-rte)

## Overview {#overview}

The Universal Editor provides a rich text editor (RTE) both in place and in the properties panel to allow authors to apply formatting changes as they edit their text.

This RTE is configurable using [component filters.](/help/implementing/universal-editor/filtering.md) This document describes what configuration options are available along with examples.

## Configuration Structure {#structure}

RTE configuration consists of two parts:

* [`toolbar`](#toolbar): The toolbar configuration controls which editing options are available in the UI and how they're organized.
* [`actions`](#actions): The actions configuration allows you to customize the behavior and appearance of individual editing actions.

These configurations can be defined as part of a [component filter](/help/implementing/universal-editor/filtering.md) with the property `rte`.

```json
[
  {
    "id": "richtext",
    "rte": {
      "toolbar": {
        // Toolbar configuration
      },
      "actions": {
        // Action-specific configurations
      }
    },
    "components": [
      "richtext"
    ]
  }
]
```

## Toolbar Configuration {#toolbar}

The toolbar configuration controls which editing options are available in the UI and how they're organized. These are the available sections

```json
{
  "toolbar": {
    // Text formatting options
    "format": ["bold", "italic", "underline", "strike"],
    // Text alignment options
    "alignment": ["left", "center", "right", "justify"],
    // Text direction options, right-to-left or left-to-right
    "direction": ["rtl", "ltr"],
    // Indentation controls
    "indentation": ["indent", "outdent"],
    // Block-level elements
    "blocks": ["paragraph", "h1", "h2", "h3", "h4", "h5", "h6", "code_block"],
    // List options
    "list": ["bullet_list", "ordered_list"],
    // Content insertion
    "insert": ["link", "unlink", "image"],
    // Superscript/subscript
    "sr_script": ["superscript", "subscript"],
    // Editor utilities
    "editor": ["removeformat"],
    // Section ordering (optional)
    "sections": ["format", "alignment", "list"]
  }
}
```

## Actions Configuration {#actions}

The actions configuration allows you to customize the behavior and appearance of individual editing actions. These are the available sections.

### Format Actions {#format}

Format actions are used to apply formatting and support HTML tag switching to choose between semantic variants. The following sections are available.

```json
{
  "actions": {
    "bold": {
      "tag": "strong",      // Use <strong> instead of <b>
      "shortcut": "Mod-B",  // Custom keyboard shortcut
      "label": "Make Bold"  // Custom button label 
    },
    "italic": {
      "tag": "em",          // Use <em> instead of <i>
      "shortcut": "Mod-I",
      "label": "Italicize"
    },
    "strike": {
      "tag": "del"          // Use <del> instead of <s>
    }
  }
}
```

### List Actions {#list}

List actions support content wrapping to control HTML structure. The following sections are available.

```json
{
  "actions": {
    "bullet_list": {
      "wrapInParagraphs": true,    // <ul><li><p>content</p></li></ul>
      "shortcut": "Mod-Shift-8",   // Custom shortcut
      "label": "Bullet List"       // Custom label
    },
    "ordered_list": {
      "wrapInParagraphs": false,   // <ol><li>content</li></ol> (default)
      "shortcut": "Mod-Shift-9"
    }
  }
}
```

### Link Actions {#link}

Link actions support target attribute control to manage link behavior. The following sections are available.

```json
{
  "actions": {
    "link": {
      "hideTarget": false,       // Show target attribute options (default)
      "shortcut": "Mod-K",       // Custom keyboard shortcut
      "label": "Insert Link"     // Custom button label
    },
    "unlink": {
      "shortcut": "Mod-Shift-K", // Custom keyboard shortcut
      "label": "Remove Link"     // Custom button label
    }
  }
}
```

#### Link Configuration Options {#link-options}

* `hideTarget`: `false` (default) - Include target attribute in links, allowing `_self`, `_blank`, etc.
* `hideTarget`: `true` - Exclude target attribute from links entirely

The `unlink` action only appears when the cursor is positioned within an existing link. It removes the link formatting while preserving the text content.

### Image Actions {#image}

Image actions support picture element wrapping to generate responsive image markup. The following sections are available.

```json
{
  "actions": {
    "image": {
      "wrapInPicture": false,     // Use <img> tag (default)
      "shortcut": "Mod-Shift-I",  // Custom keyboard shortcut
      "label": "Insert Image"     // Custom button label
    }
  }
}
```

#### Image Configuration Options {#image-options}

* `wrapInPicture`: `false` (default) - Generate simple `<img>` elements
* `wrapInPicture`: `true` - Wrap images in `<picture>` elements for responsive design

### Other Actions {#other}

All other actions support basic customization. The following sections are available.

```json
{
  "actions": {
    "h1": {
      "shortcut": "Mod-Alt-1",
      "label": "Large Heading"
    },
    "paragraph": {
      "shortcut": "Mod-Alt-0",
      "label": "Normal Text"
    },
    "link": {
      "shortcut": "Mod-K",
      "label": "Insert Link",
      "hideTarget": false    // Show target attribute options (default: false)
    }
  }
}
```

## Complete Example {#example}

The following is an example of a complete configuration.

```json
[
  {
    "id": "richtext",
    "rte": {
      // Configure which tools appear in toolbar
      "toolbar": {
        "format": [
          "bold",
          "italic"
        ],
        "blocks": [
          "paragraph",
          "h1",
          "h2"
        ],
        "list": [
          "bullet_list",
          "ordered_list"
        ],
        "insert": [
          "link",
          "unlink"
        ],
        "sections": [
          "format",
          "blocks",
          "list",
          "insert"
        ]
      },
      // Customize individual action behavior
      "actions": {
        // Format actions with HTML tag choices
        "bold": {
          "tag": "strong",
          "shortcut": "Mod-B",
          "label": "Bold"
        },
        "italic": {
          "tag": "em",
          "shortcut": "Mod-I"
        },
        // List actions with content wrapping
        "bullet_list": {
          "wrapInParagraphs": true,
          "label": "Bullet List"
        },
        "ordered_list": {
          "wrapInParagraphs": false
        },
        // Link actions with target control
        "link": {
          "hideTarget": false,
          "shortcut": "Mod-K",
          "label": "Add Link"
        },
        "unlink": {
          "label": "Remove Link"
        },
        // Other actions with basic customization
        "h1": {
          "shortcut": "Mod-Alt-1",
          "label": "Main Heading"
        }
      }
    },
    "components": [
      "richtext"
    ]
  }
]
```

## Action Option Details {#action-details}

Several options have additional details that are important to keep in mind.

### `wrapInParagraphs` {#wrapInParagraphs}

The `wrapInParagraphs` option for lists controls the HTML structure.

#### `wrapInParagraphs: false` (default) {#wrapInParagraphs-false}

```html
<ul>
  <li>Simple text content</li>
  <li>Another item</li>
</ul>
```

#### `wrapInParagraphs: true` {#wrapInParagraphs-true}

```html
<ul>
  <li><p>Text wrapped in paragraphs</p></li>
  <li><p>Supports rich formatting within items</p></li>
</ul>
```

Use `wrapInParagraphs: true` when you need:

* Rich formatting within list items
* Multiple paragraphs per list item
* Consistent block-level styling

### Link Target Options {#link-target}

The `hideTarget` option for links controls whether the `target` attribute is included in generated links and whether the dialog for link creation includes a field for target selection.

#### `hideTarget: false` (default) {#hideTarget-false}

```html
<a href="https://example.com" target="_self">Link text</a>
<a href="https://example.com" target="_blank">External link</a>
```

### `hideTarget: true` {#hideTarget-true}

```html
<a href="https://example.com">Link text</a>
```

### Tag Options {#tag}

Format actions allow switching between HTML variants.

|Action|Default Tag|Alternative Tags|Use Case|
|---|---|---|---|
|`bold`|`<strong>`|`<b>`|Semantic vs. visual emphasis|
|`italic`|`<em>`|`<i>`|Semantic vs. visual styling|
|`strike`|`<del>`|`<s>`|Visual vs. semantic deletion|

Choose semantic tags (`<strong>`, `<em>`, `<del>`) for better accessibility and SEO.

### Keyboard Shortcuts {#keyboard-shortcuts}

Shortcuts use the format `Mod-Key`(s) where:

* `Mod` = `Cmd` on Mac, `Ctrl` on Windows/Linux
* Examples: `Mod-B`, `Mod-Shift-8`, `Mod-Alt-1`
