---
title: Creating Visualization Templates for Content Fragments
description: Preview and publish Content Fragments with Visualization Templates. Learn how you can create and customize the templates.
feature: Developing, Content Fragments
role: Admin, Developer
---
# Content Fragments - Visualization Templates {#content-fragments-visualization-templates}

Visualization Templates can be used to preview Content Fragments. These HTML templates are developed with Handlebars, 

This page explains how to create custom Handlebars templates for rendering Adobe Experience Manager (AEM) Content Fragments. Templates allow you to control exactly how your content fragments are displayed in preview mode.

## What you will learn {#what-you-will-learn}

In particular, this page covers:

* Handlebars - the necessary basics of the syntax
* How to access Content Fragment data
* Working with nested Content Fragments
* Handling multi-valued fields
* Creating loops and conditional logic
* Best practices of template design for Content Fragments

## Prerequisites {#prerequisites}

To understand and work with the technologies covered here you should have:

* Basic understanding of HTML
* Familiarity with AEM Content Fragments and Content Fragment Models
* Understanding of your Content Fragment models

## Handlebars - the (very) basics {#handlebars-the-very-basics}

Handlebars is a simple templating language that uses double curly braces (brackets) `{{ }}` to insert dynamic content into HTML.

### Basic syntax

```handlebars
<!-- Output a variable (HTML-escaped) -->
{{variableName}}

<!-- Output raw HTML (unescaped) -->
{{{htmlContent}}}

<!-- Comment (not rendered) -->
{{! This is a comment }}
```

### Key concepts

| Syntax | Description | When to use |
|--- |--- |--- |
| `{{ }}` | Escapes HTML special characters | Metadata, labels, booleans |
| `{{{ }}}` | Outputs raw HTML (unescaped) | Field values and asset output |
| `{{! }}` | Handlebars-only comment | Template documentation |

> **Important**  
> Use triple braces (`{{{ }}}`) for field values because values are pre-rendered HTML.

## Template context reference

When your template is rendered, it receives a context object containing all the data about your content fragment.

### Main content fragment variables

| Variable | Type | Description |
|--- |--- |--- |
| `properties` | Map | Fragment metadata |
| `fields` | Map | Direct access to field values by name |
| `allFields` | List | Array of `{name, value}` for iteration |
| `hasFields` | Boolean | `true` if the fragment has fields |

### Properties structure (main and referenced CFs)

| Property | Type | Description |
|--- |--- |--- |
| `id` | String | UUID of fragment |
| `title` | String | Fragment title |
| `description` | String | Fragment description |
| `path` | String | JCR path |
| `hasDescription` | Boolean | Description availability flag |
| `createdDate` | String | ISO-8601 created date |
| `modifiedDate` | String | ISO-8601 modified date |
| `publishedDate` | String | ISO-8601 published date |
| `status` | String | Fragment status (for example `DRAFT`) |
| `model` | Map | Model metadata (id, path, name, technicalName, description) |
| `validationStatus` | List | Entries like `{property, message}` |
| `previewReplicationStatus` | String | Preview replication status |
| `tags` | List | Tag metadata |
| `fieldTags` | List | Field-level tag metadata |

Template access examples:

```handlebars
{{properties.title}}
{{properties.description}}
{{{fields.description}}}
```

### Referenced content fragments

| Variable | Type | Description |
|--- |--- |--- |
| `hasReferencedFragments` | Boolean | `true` when references exist |
| `referencedFragments` | List | Array of referenced fragment objects |
| `referencesError` | Boolean | `true` if loading references failed |
| `referencesErrorMessage` | String | Error details |

Each referenced fragment object includes:

* `anchorId`
* `properties`
* `hasFields`
* `fields`
* `allFields`

## Basic field access

### Direct field access (recommended)

```handlebars
<!DOCTYPE html>
<html>
<head>
  <title>{{main_cf_title}}</title>
</head>
<body>
  <article>
    <h1>{{{fields.title}}}</h1>
    <p class="subtitle">{{{fields.subtitle}}}</p>
    <div class="content">{{{fields.description}}}</div>
    <div class="image">{{{fields.primaryImage}}}</div>
  </article>
</body>
</html>
```

### Iterate through all fields

```handlebars
<table>
  <thead>
    <tr>
      <th>Field Name</th>
      <th>Field Value</th>
    </tr>
  </thead>
  <tbody>
    {{#each allFields}}
    <tr>
      <td>{{name}}</td>
      <td>{{{value}}}</td>
    </tr>
    {{/each}}
  </tbody>
</table>
```

## Nested content fragments

### Single-level nesting

```handlebars
<p>Name: {{{fields.author.name}}}</p>
<p>Email: {{{fields.author.email}}}</p>
<p>Bio: {{{fields.author.bio}}}</p>
```

Pattern: `fields.referenceFieldName.nestedFieldName`

### Multi-level nesting

```handlebars
<p>Organization: {{{fields.author.organization.name}}}</p>
<p>Website: {{{fields.author.organization.website}}}</p>
<p>City: {{{fields.author.organization.address.city}}}</p>
```

Pattern: `fields.level1.level2.level3.fieldName` (unlimited depth).

### API requirement: hydration

To resolve nested references, include hydration in the preview call:

```http
GET /adobe/sites/cf/fragments/{id}/preview?hydration=%7B%22enabled%22%3Atrue%2C%22maxDepth%22%3A2%7D
```

| `maxDepth` | Loaded data |
|--- |--- |
| `1` | Main fragment + direct references |
| `2` | Main fragment + direct references + their references |
| `3+` | Continue up to 10 levels |

## Multi-valued fields

### Multi-valued text fields

```handlebars
{{#each fields.tags}}
<span class="tag">{{{this}}}</span>
{{/each}}
```

For index access, use dot-bracket syntax:

```handlebars
{{{fields.tags.[0]}}}
```

### Multi-valued content fragment references

```handlebars
{{#each fields.authors}}
<div class="author">
  <h4>{{{this.name}}}</h4>
  <p>Email: {{{this.email}}}</p>
  {{#if this.bio}}<p>{{{this.bio}}}</p>{{/if}}
</div>
{{/each}}
```

### Multi-valued assets

```handlebars
{{#each fields.gallery}}
<div class="image">{{{this}}}</div>
{{/each}}
```

## Loops and iteration

### `each` examples

```handlebars
{{#each fields.tags}}
<span class="tag">{{{this}}}</span>
{{else}}
<p>No tags available.</p>
{{/each}}
```

### Special loop variables

```handlebars
{{#each fields.items}}
  {{@index}}   {{@number}}   {{@first}}   {{@last}}   {{{this}}}
{{/each}}
```

## Conditional rendering

```handlebars
{{#if fields.author}}
  <p>By {{{fields.author.name}}}</p>
{{/if}}

{{#unless fields.hideAuthor}}
  <div class="author">{{{fields.author.name}}}</div>
{{/unless}}
```

Error handling pattern:

```handlebars
{{#if referencesError}}
<div class="error-message">
  <strong>Error Loading Referenced Fragments</strong>
  {{#if referencesErrorMessage}}
  <p>{{referencesErrorMessage}}</p>
  {{/if}}
</div>
{{/if}}
```

## Built-in Handlebars helpers

| Helper | Description |
|--- |--- |
| `{{#if condition}}` | Renders when condition is truthy |
| `{{#unless condition}}` | Renders when condition is falsy |
| `{{#each array}}` | Iterates array/object values |
| `{{#with object}}` | Creates a nested scope |
| `{{lookup this "key"}}` | Dynamic property lookup |

## Custom template helpers

The system provides custom helpers:

1. `asset` (builds `<img>` with custom attributes)
1. `text` (builds `<span>` with custom attributes)

### `asset` helper

Syntax:

```handlebars
{{{asset fieldValue attribute1="value1" attribute2="value2"}}}
```

Examples:

```handlebars
{{{asset fields.heroImage class="hero-image"}}}
{{{asset fields.logo class="brand-logo" id="main-logo"}}}
{{{asset fields.thumbnail class="thumb" data-category="product"}}}
```

### `text` helper

Syntax:

```handlebars
{{{text fieldValue attribute1="value1" attribute2="value2"}}}
```

Examples:

```handlebars
{{{text fields.title class="article-title"}}}
{{{text fields.price class="price-tag" id="product-price"}}}
```

### Attribute validation notes

Valid attribute names:

* Start with a letter
* Can contain letters, digits, hyphens, underscores
* Case-insensitive

Invalid names are skipped and logged.

## Best practices

1. Always use triple braces for field and helper output.
1. Guard nested references with `#if` checks.
1. Prefer direct field access (`fields.title`) over generic loops when possible.
1. Use semantic HTML (`article`, `header`, `main`, `time`, `address`).
1. Include fallbacks for missing optional data.
1. Test with full, partial, empty, and deeply nested data.

## Troubleshooting

| Problem | Symptom | Solution |
|--- |--- |--- |
| Field shows HTML tags as text | `<p>...</p>` appears literally | Use triple braces: `{{{fields.description}}}` |
| Nested field appears empty | `{{{fields.author.name}}}` blank | Enable hydration and verify `maxDepth` and field names |
| Array index fails | `{{{fields.tags[0]}}}` empty | Use `{{{fields.tags.[0]}}}` |
| References missing | `hasReferencedFragments` false | Enable `hydration` and check `referencesError` |
| Empty output | Blank render | Verify block closures and add temporary debug values |
| Parent value unavailable in nested loop | Undefined parent variable | Use `../` or `../../` scope notation |

## Additional resources

* [Handlebars documentation](https://handlebarsjs.com/)
* [Handlebars built-in helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
* [AEM Content Fragments documentation](/help/sites-cloud/administering/content-fragments/overview.md)

## Quick reference

### Context variables

```handlebars
{{main_cf_title}}
{{main_cf_description}}
{{main_cf_path}}
{{hasMainDescription}}
{{hasFields}}
{{hasReferencedFragments}}
{{referencesError}}
{{referencesErrorMessage}}
```

### Field access

```handlebars
{{{fields.fieldName}}}
{{{fields.author.name}}}
{{{fields.author.org.address.city}}}
{{{fields.tags.[0]}}}
{{#each fields.tags}}...{{/each}}
{{{fields.authors.[0].name}}}
```

### Control flow

```handlebars
{{#if condition}}...{{/if}}
{{#if condition}}...{{else}}...{{/if}}
{{#unless condition}}...{{/unless}}
{{#each array}}...{{/each}}
{{#each array}}...{{else}}...{{/each}}
{{#with object}}...{{/with}}
```

### Loop variables

```handlebars
{{@index}}
{{@number}}
{{@first}}
{{@last}}
{{@key}}
{{this}}
{{../parent}}
```

### Triple braces requirement

Use triple braces for:

* `{{{fields.description}}}`
* `{{{fields.heroImage}}}`
* `{{{asset fields.image class="x"}}}`
* `{{{text fields.title class="x"}}}`

Use double braces for:

* `{{main_cf_title}}`
* `{{hasFields}}`
* `{{name}}`
* `{{@index}}`
