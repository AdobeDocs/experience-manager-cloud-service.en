---
title: Configuring the RTE for the Universal Editor
description: Understand how you can configure the rich text editor (RTE) in the Universal Editor.
feature: Developing
role: Admin, Developer
exl-id: 350eab0a-f5bc-49c0-8e4d-4a36a12030a1
---
# Configuring the RTE for the Universal Editor {#configure-rte}

Understand how you can configure the rich text editor (RTE) in the Universal Editor.

## Overview {#overview}

The Universal Editor provides a rich text editor (RTE) both in place and in the properties panel to allow authors to apply formatting changes as they edit their text.

This RTE is configurable using [component filters.](/help/implementing/universal-editor/filtering.md) This document describes what configuration options are available along with examples.

>[!NOTE]
>
>When you start a Universal Editor project, all rich text features that your backend supports (AEM with Edge Delivery or headless implementation) are automatically active.
>
>* You can deactivate those options you do not need.
>* Activating options that are not compatible with your project type is not supported.

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

## Action Configuration {#action}

The actions configuration allows you to customize the behavior and appearance of individual editing actions. These are the available sections.

### Common Action Options {#common-action-options}

Most actions support the following common options:

* `shortcut?`: string - Overrides the default keyboard shortcut for the action (if any)
* `label?`: string - Overrides the label used for the action in UI
* `hideInline?`: boolean - When `true`, hides this action from the in-context (inline) RTE editor toolbar

```json
{
  "actions": {
    "bold": {
      "label": "Bold",
      "shortcut": "Mod-B",
      "hideInline": true
    }
  }
}
```

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

### Table Actions {#table-actions}

Table actions support content wrapping to control HTML structure in table cells:

```json
{
  "actions": {
    "table": {
      "wrapInParagraphs": false, // <td>content</td> (default)
      "shortcut": "Mod-Alt-T",   // Custom shortcut
      "label": "Insert Table"    // Custom label
    }
  }
}
```

#### Table Configuration Options {#table-configuration-options}

* `wrapInParagraphs`: `false` (default) - Table cells contain unwrapped text content
* `wrapInParagraphs`: `true` - Table cells wrap content in paragraph tags

Samples:

When `wrapInParagraphs`: `false`:

```html
<!-- Single line -->
<td>Cell content</td>

<!-- Multiple paragraphs get <br> separation -->
<td>Line 1<br />Line 2</td>
```

When `wrapInParagraphs`: `true`:

```html
<!-- Single paragraph -->
<td><p>Cell content</p></td>

<!-- Multiple paragraphs preserved -->
<td>
  <p>Line 1</p>
  <p>Line 2</p>
</td>
```

>[!NOTE]
>
>When unwrapping paragraphs (`wrapInParagraphs`: `false`), the sanitizer automatically inserts `<br>` tags between multiple paragraphs to preserve visual line breaks. This follows HTML standards and common practice across major rich text editors.

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

### Indentation Configuration {#indentation}

Indentation has a feature-level configuration that controls the scope of indentation behavior, plus individual action configs for shortcuts and labels.

```json
{
  "actions": {
    // Feature-level configuration
    "indentation": {
      "scope": "all"  // Controls what content can be indented (default: "all")
    },

    // Individual action configurations
    "indent": {
      "shortcut": "Tab",           // Custom keyboard shortcut
      "label": "Increase Indent"   // Custom button label
    },
    "outdent": {
      "shortcut": "Shift-Tab",     // Custom keyboard shortcut
      "label": "Decrease Indent"   // Custom button label
    }
  }
}
```

#### Indentation Scope Options {#indentation-options}

* `scope`: `all` (default) - Indent/outdent applies to all content:
  * Lists: Nest/unnest list items
  * Paragraphs and headings: Increase/decrease general indentation level
* `scope`: `lists` - Indent/outdent only applies to list items:
  * Lists: Nest/unnest list items
  * Paragraphs and headings: No indentation (buttons disabled for these)

>[!NOTE]
>
>List nesting via Tab/Shift+Tab keys works independently of general indentation settings.

### Paste as Text {#paste-as-text}

The `paste_text` editor action enables a standard paste-as-plain-text workflow.

* **Default shortcut:** Mod-Shift-v (Cmd+Shift+V on macOS, Ctrl+Shift+V on Windows/Linux)
* **Behavior:** Pastes from text/plain (source formatting is ignored)
  * In lists, newlines create new list items.

```json
{
  "toolbar": {
    "editor": ["removeformat", "paste_text"]
  },
  "actions": {
    "paste_text": {
      "shortcut": "Mod-Shift-v",
      "label": "Paste as Text"
    }
  }
}
```

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
    }
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

### `wrapInPicture`{#wrapinpicture}

The `wrapInPicture` option for images controls the HTML structure generated for image content.

#### wrapInPicture: false (default) {#wrapinpicture-false}

```html
<img src="image.jpg" alt="Description" />
```

#### wrapInPicture: true {#wrapinpicture-true}

```html
<picture>
  <img src="image.jpg" alt="Description" />
</picture>
```

Use `wrapInPicture: true` when you need:

* Responsive image support with `<source>` elements.
* Art direction capabilities.
* Future-proofing for advanced image features.
* Consistent picture element structure.

>[!NOTE]
>
>When `wrapInPicture: true` is enabled, images can be enhanced with additional `<source>` elements for different media queries and formats, making them more flexible for responsive design.

### Link Target Options {#link-target}

The `hideTarget` option for links controls whether the `target` attribute is included in generated links and whether the dialog for link creation includes a field for target selection.

#### `hideTarget: false` (default) {#hideTarget-false}

```html
<a href="https://example.com" target="_self">Link text</a>
<a href="https://example.com" target="_blank">External link</a>
```

#### `hideTarget: true` {#hideTarget-true}

```html
<a href="https://example.com">Link text</a>
```

### Disabling Links on Images {#disableforimages}

The `disableForImages` option for links controls whether users can create links on images and picture elements. This applies to both inline `<img>` elements and block-level `<picture>` elements.

#### `disableForImages: false` (default) {#disableforimages-false}

Users can select images and wrap them in links.

```html
<!-- Inline image with link -->
<a href="https://example.com">
  <img src="image.jpg" alt="Description" />
</a>

<!-- Block-level picture with link -->
<a href="https://example.com">
  <picture>
    <img src="image.jpg" alt="Description" />
  </picture>
</a>
```

#### disableForImages: true {#disableforimages-true}

The link button is disabled when an image or picture is selected. Users can only create links on text content.

```html
<!-- Images remain standalone without links -->
<img src="image.jpg" alt="Description" />

<picture>
  <img src="image.jpg" alt="Description" />
</picture>

<!-- Links work normally on text -->
<a href="https://example.com">Link text</a>
```

Use `disableForImages: true` when you want to:

* Maintain visual consistency by preventing linked images.
* Simplify content structure by separating images from navigation.
* Enforce content policies that restrict image linking.
* Reduce accessibility complexity in your content.

>[!NOTE]
>
>This setting only affects the ability to create new links on images. It does not remove existing links from images in the content.

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

## Unsupported HTML {#unsupported-html}

By default, unknown HTML tags are stripped when parsed by the editor. To preserve them, opt in via the `unsupportedHtml` configuration option:

```javascript
const rteConfig = {
  unsupportedHtml: true, // preserve unknown HTML tags (default: false)
};
```

|Value|Behavior|
|---|---|
|`false` (default)|Unknown HTML tags are dropped during parsing.|
|`true`|Unknown HTML tags are wrapped in a custom unsupported-block node so content can round-trip safely.|

When enabled, the editor renders unsupported nodes with a `rte-unsupported-block` class. Consumer apps should provide the styling for this class (e.g., border, padding, background). The tag label inside the block uses `rte-unsupported-label`, which can also be customized.
