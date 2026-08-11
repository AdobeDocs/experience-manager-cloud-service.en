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
>When you start a Universal Editor project, all rich text features that your backend supports (AEM with Edge Delivery or headless implementation) are automatically active and available in [the modal editor window of the RTE.](/help/sites-cloud/authoring/universal-editor/authoring.md#modal-editor)
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
    "format": ["bold", "italic", "underline", "strike", "text_color"],
    // Text alignment options
    "alignment": ["left", "center", "right", "justify"],
    // Text direction options, right-to-left or left-to-right
    "direction": ["rtl", "ltr"],
    // Indentation controls
    "indentation": ["indent", "outdent"],
    // Block-level elements
    "blocks": ["paragraph", "h1", "h2", "h3", "h4", "h5", "h6", "code_block", "blockquote"],
    // List options
    "list": ["bullet_list", "ordered_list"],
    // Content insertion
    "insert": ["link", "unlink", "image", "special_characters"],
    // Superscript/subscript
    "sr_script": ["superscript", "subscript"],
    // Editor utilities
    "editor": ["removeformat", "clean_unsupported_tags", "paste_text", "fullscreen"],
    // Advanced items (e.g. the class picker).
    "advanced": ["classes"],
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

#### Table Configuration Options {#table-configuration-options}

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

#### Properties Dialogs {#properties-dialog}

The table plugin ships three property-editor dialogs that open from the **Table** menu when these flags are enabled:

* **Table Properties** — Edit the enclosing table's width/height, cell spacing, cell padding, alignment, border (width/style/color), and background color. Border and cell padding changes fan out to every cell in the same transaction so the visual result matches what a user would expect.
* **Row Properties** — Edit the enclosing row's row type (Header/Body/Footer), alignment, height, border (width/style/color), and background color. Row type is section-only (matching TinyMCE's default `table_header_type: "section"`): a Header row moves into `<thead>` on serialization but its cells remain `<td>`. Use **Cell Properties** -> **Header cell** for `<th>`. On serialization the rows are grouped into real `<thead>`/`<tbody>`/`<tfoot>` sections (matching TinyMCE/Word). See the storage note below. Borders fan out to the row's cells so they render under border-collapse.
* **Cell Properties** — Edit the selected cell(s) cell type (Cell/Header cell), width/height, horizontal and vertical alignment, border (width/style/color), and background color. When a `CellSelection` spans multiple cells, the patch is applied to every selected cell at once. The cell type toggles the cell between `table_cell` (`<td>`) and `table_header` (`<th>`).

All three default to disabled (opt-in), matching the rest of the RTE config surface where capabilities are off until a consumer explicitly enables them. Opt in per consumer when you want the dialogs surfaced:

```json
{
  actions: {
    table: {
      showTableProperties: true, // default false: show "Table Properties" menu item
      showRowProperties: true,   // default false: show "Row Properties" menu item
      showCellProperties: true,  // default false: show "Cell Properties" menu item
    }
  }
}
```

#### Properties Dialog Options {#properties-dialog-options}

|---|---|---|
|Option|Default|Effect|
|`showTableProperties`|`false`|Show the **Table Properties** item in the **Table** dropdown|
|`showRowProperties`|`false`|Show the **Row Properties** item in the **Row** submenu|
|`showCellProperties`|`false`|Show the **Cell Properties** item in the **Cell** submenu|

The dialogs round-trip through `htmlAttrs.style` on the respective ProseMirror node, i.e. inline CSS like TinyMCE/Word emit, not custom data attributes. Cell width also writes the schema-level `colwidth` so it survives PM's table machinery. Cell type is carried by the node tag (`<td>`/`<th>`).

The `prosemirror-tables` schema is flat (`table` -> `table_row` -> `cell`) with no `<thead>`/`<tbody>`/`<tfoot>` section nodes, so internally a row's Header/Body/Footer intent is held on the `<tr>` as a `data-row-type` marker. When a row's type changes, the rows are re-sorted in place into header -> body -> footer order within the same transaction, so the editor canvas matches the exported structure live (Header rows hoist to the top, Footer rows sink to the bottom, like TinyMCE). This in-editor reorder is skipped when any cell spans multiple rows (`rowspan > 1`), where moving a row would corrupt the grid. On the way out, `sanitizeHTML` groups the rows into real `<thead>`/`<tbody>`/`<tfoot>` sections (header rows first, footer rows last) and drops the marker, producing the same structure TinyMCE/Word emit. On the way in, a `<tr>`'s enclosing section is read back into the marker, so sectioned HTML round-trips.

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

### Full Screen {#full-screen}

The full screen action toggles the editor into and out of full screen mode:

```json
{
  actions: {
    fullscreen: {
      label: "Fullscreen"; // Custom button label
    }
  }
}
```

When full screen is active, the editor wrapper receives the class `rte-fullscreen-wrapper`. Consumer apps can target this class to apply custom styles or CSS properties (e.g. z-index, dimensions, overlay). (Not supported in the Universal Editor)

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

### Special Characters {#special-characters}

The `special_characters` insert action opens a character picker popover for inserting special characters (symbols, math operators, currency signs, punctuation, arrows, etc.) at the cursor position.

```json
{
  "toolbar": {
    "insert": ["link", "unlink", "image", "table", "special_characters"],
    "sections": ["insert"],
  },
  "actions": {
    "special_characters": {
      "label": "Special Characters"
    }
  }
}
```

A default set of 44 commonly-used characters is included out-of-the-box. The character list can be customized through two configuration options:

* `appendCharacters` - Add characters to the default set
* `characters` - Replace the default set entirely

Each character entry has `character` (the Unicode character) and `title` (tooltip / accessible name).

#### Append Characters to Defaults {#append-special-characters}

```json
{
  "actions": {
    "special_characters": {
      "appendCharacters": [
        { "character": "\u2605", "title": "Black star" },
        { "character": "\u2764", "title": "Heavy black heart" },
      ];
    }
  }
}
```

#### Replace Default Special Characters {#replace-special-characters}

```json
{
  "actions": {
    "special_characters": {
      "characters": [
        { "character": "\u00A9", "title": "Copyright sign" },
        { "character": "\u00AE", "title": "Registered sign" },
        { "character": "\u2122", "title": "Trade mark sign" },
      ];
    }
  }
}
```

#### Both Options Together {#both-special-character-options}

This example uses `characters` as the base, then appends additional characters using `appendCharacters`.

```json
{
  "actions": {
    "special_characters": {
      "characters": [
        { "character": "\u00A9", "title": "Copyright sign" },
        { "character": "\u00AE", "title": "Registered sign" }
      ],
      "appendCharacters": [
        { "character": "\u2605", "title": "Black star" }
      ]
    }
  }
}
```

### CSS Classes {#css-classes}

The `classes` action adds a dropdown that applies a configurable CSS class to RTE content. It is listed as an item in the `advanced` section. The plugin only writes/removes class names on the produced HTML. The consumer app owns the actual CSS for each class and is responsible for loading it wherever the RTE content is rendered (editor, preview, publish).

The dropdown only appears when at least one option is configured. The plugin ships with no defaults.

```json
{
  toolbar: {
    advanced: ["classes"],
    sections: ["blocks", "format", "advanced"],
  },
  actions: {
    classes: {
      label: "Add Custom Class",
      options: [
        { value: "rte-hero", label: "Hero title" },
        { value: "rte-lede", label: "Lede paragraph" },
        { value: "rte-callout", label: "Callout block" },
        { value: "rte-pill", label: "Pill (inline)" },
      ],
    },
  },
}
```

Each entry has value (the CSS class name written to the HTML) and label (the human-readable text shown in the dropdown).

The target follows the closest-to-caret-wins rule:

* **Empty selection inside a managed span:** The class is applied to that span run, not the block. Picking a different class swaps the span's class; **Remove Custom Class** clears it.
* **Empty selection elsewhere (cursor only):** The chosen class is applied to the nearest block-level ancestor of the cursor (`<p>`, `<h1>`, etc.). When the cursor is inside a list item or table cell that wraps a paragraph, the `<li>`/`<td>`/`<th>` receives the class, not the inner paragraph.
* **Real selection:** The selected text is wrapped in a `<span class="...">`. If the selection already has a span, the existing span's class is updated.
* **Remove Custom Class**: Remove the managed class from the target (span run or block, whichever the caret resolves to). If the only remaining attribute on a span was the managed class, the span itself is unwrapped. The **Remove Custom Class** option only appears when a managed class is currently active.

Existing classes that aren't part of the configured options list are preserved untouched. Only the managed classes are swapped in/out. Consumer-set classes coexist safely with the plugin.

Dropdown reflection:

* With only the cursor placed, the dropdown reflects the closest managed class: the span at the caret if there is one, otherwise the block under the cursor.
* With a selection, the dropdown reflects the managed class on the span wrapping the selection. Only when the entire selection shares the same class. Mixed selections show nothing selected.

### Block Types {#block-types}

The `blocks` toolbar section renders a dropdown that switches the current block between the configured block types. Supported values are `paragraph`, `h1`–`h6`, `code_block`, and `blockquote`.

* `blockquote` is a wrapping block (its ProseMirror `content` is `block+`), unlike `paragraph`/`h1`–`h6`/`code_block` which are text blocks. Selecting **Quote** wraps the current block in a `<blockquote>` The dropdown then shows **Quote** as selected while the caret is inside one. Selecting any other block type (e.g. **Paragraph**) while inside a quote lifts the block out of the quote first, so it also leaves the quote. This mirrors TinyMCE's blocks dropdown.
* Because it is a wrapping node, a `<blockquote>` can hold multiple paragraphs, lists, or even nested quotes. This is what lets externally-authored content round-trip losslessly: TinyMCE (legacy content) and Word (paste) both emit `<blockquote><p>…</p></blockquote>` (often multi-paragraph), and that structure is preserved on load, edit, and serialize rather than being flattened.
* As with all block types, the consumer app owns the CSS that visually styles `<blockquote>` wherever the RTE content is rendered.

```json
{
  "toolbar": {
    "blocks": ["paragraph", "h1", "h2", "h3", "code_block", "blockquote"],
    "sections": ["blocks"],
  },
  "actions": {
    "blockquote": {
      "label": "Quote", // Custom dropdown label
    },
  },
}
```

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

### Find and Replace {#find-replace}

The `find_and_replace` editor action uses [`prosemirror-search`](https://github.com/ProseMirror/prosemirror-search) (match highlights) plus a command plugin keyed by `FIND_AND_REPLACE_PLUGIN_KEY`.

* **Integration:** Add `createFindAndReplacePlugin()` to your editor's ProseMirror plugins when `toolbar.editor` includes `find_and_replace`.
* **API:** Use `FIND_AND_REPLACE_PLUGIN_KEY.getState(state)` to access `find`, `replaceNext`, `replaceAll`, and `getMatchCount`.
* **Styles:** Ensure your app loads CSS for `.ProseMirror-search-match` and `.ProseMirror-active-search-match` (from `prosemirror-search`'s style/`search.css` or your own equivalent).

```json
{
  "toolbar": {
    "editor": ["find_and_replace"],
    "sections": ["editor"],
  },
  "actions": {
    "find_and_replace": {
      "label": "Find and replace",
    },
  },
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
          "italic",
          "text_color"
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
          "unlink",
          "image",
          "special_characters"
        ],
        "editor": [
          "removeformat",
          "paste_text"
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
        // Image actions with picture wrapping
        "image": {
          "wrapInPicture": false, // Use <img> tag instead of <picture>
          "shortcut": "Mod-Shift-I",
          "label": "Insert Image",
        },
        // Special characters with custom additions
        "special_characters": {
          "label": "Special Characters",
          "appendCharacters": [{ "character": "\u2605", "title": "Black star" }],
        },
        // Other actions with basic customization
        "paste_text": {
          "shortcut": "Mod-Shift-v",
          "label": "Paste as Text",
        },
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

### Text Color {#color}

The `text_color` format option adds text coloring capabilities to the editor.

```html
<!-- With color applied -->
<span style="color: #ff0000">Colored text</span>

<!-- Color removed -->
Plain text
```

The plugin also parses legacy `<font color="...">` elements for backward compatibility.

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

### `unsupportedHtmlOptions.structuralTags` (optional) {#unsupportedhtmloptions}

Use `unsupportedHtmlOptions.structuralTags` to control which additional structural tags are treated as supported HTML.

```javascript
const rteConfig = {
  unsupportedHtml: true,
  unsupportedHtmlOptions: {
    structuralTags: ["div", "section"], // preserve configured tags as supported
  },
};
```

|Value|Behavior|
|---|---|
|Omitted/`[]`|No additional structural tags are whitelisted.|
|`["div"]`|`<div>` is treated as supported HTML and is not wrapped as unsupported.|
|`["div", "section"]`|Both `<div>` and `<section>` are treated as supported HTML and are not wrapped as unsupported.|

>[!NOTE]
>
>`unsupportedHtmlOptions` only affects behavior when `unsupportedHtml` is enabled.

When enabled, the editor renders unsupported nodes with wrapper tags (`unsupported-block`/`unsupported-inline`) and wrapper classes. Consumer apps should provide the styling for this class (e.g., border, padding, background). The tag label inside the block uses `rte-unsupported-label`, which can also be customized.

* `rte-unsupported-block`
* `rte-unsupported-inline`
* `rte-unsupported-label`

Consumer apps should provide styling for these classes (e.g. border, spacing, background, and inline alignment).

When `unsupportedHtml` is enabled, the consumer should add the unsupported nodes plugin (e.g. `createUnsupportedNodesPlugin()`) so that copying an unsupported block or inline node puts its inner text on the clipboard (plain text only) and users can paste the content elsewhere.
