---
title: Creating Visualization Templates for Content Fragments
description: Preview and publish Content Fragments with Visualization Templates. Learn how you can create and customize the templates.
feature: Developing, Content Fragments
role: Admin, Developer
---
# Visual Content Fragments - Templates {#visual-content-fragments-templates}

In Adobe Experience Manager (AEM) as a Cloud Service, HTML templates can be used to preview, and deliver, Content Fragments. 

You can create HTML templates in your code editor of choice, then upload and assign them to Content Fragment Models in AEM. HTML templates allow you to control exactly how your Content Fragments are displayed. Once assigned, a template is available to be used with any Content Fragment based on the model, by mapping the HTML template to the Content Model and Fragment with Handlebars.js syntax as content placeholders. Combined into a Visual Content Fragment, this allows visual preview of the fragment, or delivery of the modular  experience in HTML format to any channel; for example, browser, email, mobile application, or others. 

This article explains how to create custom HTML templates with Handlebars syntax for rendering Visual Content Fragments.

After creating your templates you can then:

* [Use your templates in AEM](#using-a-template-in-aem)

* Use the [Publish URL of your Visual Content Fragments](#using-the-publish-url)

>[!NOTE]
>
>See [Visual Content Fragments](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md) for uploading, assigning and using your template in AEM.

## What you will learn {#what-you-will-learn}

After providing a (very quick) introduction to: 

* How to use your templates in AEM 
* Using the Publish URL

This page covers (in more detail):

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

## Using a template {#using-a-template}

### Using a template in AEM {#using-a-template-in-aem}

For details of how to use your template in AEM see:

* [Visual Content Fragments - uploading and assigning your templates](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md)
* [Preview action for a selected fragment - from the console](/help/sites-cloud/administering/content-fragments/managing.md#actions-selected-content-fragment)
* [Preview your fragment - from the fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md#preview-content-fragment)

### Using the Publish URL {#using-the-publish-url}

Once you have created visual Content Fragments using the template you can then use the [Publish URL of your Visual Content Fragments](/help/implementing/developing/extending/content-fragments-visualization-publish-url.md).

## Handlebars - the (very) basics {#handlebars-the-very-basics}

Handlebars is a simple templating language that uses double curly braces (brackets) `{{ }}` to insert dynamic content into HTML.

### Basic syntax {#basic-syntax}

An example of basic Handlebars syntax:

```handlebars
<!-- Output a variable (HTML-escaped) -->
{{variableName}}

<!-- Output raw HTML (unescaped) -->
{{{htmlContent}}}

<!-- Comment (not rendered) -->
{{! This is a comment }}
```

### Key concepts {#key-concepts}

The key concepts of Handlebars:

| Syntax | Description | When to use |
|--- |--- |--- |
| `{{ }}` | Escapes HTML special characters | Metadata, labels, booleans |
| `{{{ }}}` | Outputs raw HTML (unescaped) | Rich text and asset output |
| `{{! }}` | Handlebars-only comment | Template documentation |

>[!IMPORTANT]
>
> Use triple braces (`{{{ }}}`) for field values because values are pre-rendered HTML.

## Template context reference {#template-context-reference}

When your template is rendered, it receives a context object containing all the data about your Content Fragment. This will cover:

* the fragment that you have selected
* all further fragments referenced from that selected fragment

  >[!NOTE]
  >
  >Fragments can be referenced:
  >
  >* in the UI: to the default depth of 5
  >* via the API: the depth is configurable, up to the maximum depth of 10

### Content Fragment {#content-fragment}

The structure of the context object for the (selected) Content Fragment:

| Variable | Type | Description |
|--- |--- |--- |
| `properties` | Map | Fragment metadata (see [Properties structure](#properties-structure-main-and-referenced-fragments)) |
| `fields` | Map | Direct access to field values by name |
| `allFields` | List | Array of `{name, value}` for iteration |
| `hasFields` | Boolean | `true` if the fragment has fields |

### Properties structure {#properties-structure}

The `properties` object has the same structure for the selected fragment and for each referenced fragment.

| Property | Type | Description | Example |
|--- |--- |--- |--- |
| `id` | String | UUID of fragment | |
| `title` | String | Title of the fragment | Cycling Southern Utah |
| `description` | String | Description of the fragment | An adventure... |
| `path` | String | JCR path to the fragment | `/content/dam/...` |
| `hasDescription` | Boolean | True if description is not blank | `true` |
| `createdDate` | String | ISO-8601 created date | |
| `modifiedDate` | String | ISO-8601 modified date | |
| `publishedDate` | String | ISO-8601 published date | |
| `status` | String | Replication status for Publish tier | `DRAFT` |
| `model` | Map | Contains: `id`, `path`, `name`, `technicalName`, `description` | |
| `validationStatus` | List | Entries like `{property, message}` | |
| `previewReplicationStatus` | String | Replication status for Preview tier | |
| `tags` | List | Fragment level tags. Each item: `id`, `title`, `titlePath`, `name`, `path`, `description` | |
| `fieldTags` | List | Field level tags. Same structure as `tags`. | |

Examples: Template access

For the (selected) Content Fragment:

```handlebars
{{properties.title}}, {{properties.description}}, {{{fields.field_name}}} 
```

### Referenced Content Fragments {#referenced-content-fragments}

The structure of the context object for any referenced fragments:

| Variable | Type | Description |
|--- |--- |--- |
| `hasReferencedFragments` | Boolean | `true` when references exist |
| `referencedFragments` | List | Array of referenced fragment objects |
| `referencesError` | Boolean | `true` if an error occurred when loading references |
| `referencesErrorMessage` | String | Error message when `referencesError` is `true` |

### Referenced Fragment Structure {#referenced-fragment-structure}

Each item in `referencedFragments` contains:

| Property | Type | Description |
|--- |--- |--- |
| `anchorId` | String | HTML-safe anchor ID (at fragment level; not a CF property) |
| `properties` | Map | Fragment metadata (same structure as above) |
| `hasFields` | Boolean | True if the fragment has fields |
| `fields` | Map | Direct access to fields within this fragment |
| `allFields` | List | Array of `{name, value}` for iteration |

Examples: Template access for the first referenced Content Fragment (first item in the 0-indexed list):

```handlebars
{{referencedFragments.[0].anchorId}}, {{referencedFragments.[0].properties.title}}, {{referencedFragments.[0].properties.description}}
```

Or from the fields map: 

```handlebars
{{{ fields.referenced_cf_field_name.properties.description }}}
```

## Basic field access {#basic-field-access}

Direct field access is recommended, when necessary you can iterate through all fields.

### Direct field access (recommended) {#direct-field-access-recommended}

Access fields directly by name using the fields map:

```handlebars
<!DOCTYPE html>
<html>
<head>
  <title>{{properties.title}}</title>
</head>
<body>
  <article>
    <h1>{{{fields.title}}}</h1>
    <p class="subtitle">{{{fields.subtitle}}}</p>
    <div class="content">
      {{{fields.description}}}
    </div>
    <div class="image">
      {{{fields.primaryImage}}}
    </div>
  </article>
</body>
</html>
```

Remember:

* Use triple braces `{{{ }}}` for field values if they contain pre-rendered HTML (rich text)
* Field names (title, subtitle, description, primaryImage) **must** match your Content Fragment Model **exactly**
* Missing fields are not rendered - no errors are thrown and the Handlebars syntax remains present (and visible) in the rendered HTML Fragment

### Iterate through all fields {#iterate-through-all-fields}

Use `allFields` when you do not know the field names in advance:

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

Remember:

* `{{name}}` uses double braces (plain text label)
* `{{{value}}}` uses triple braces (pre-rendered HTML value)

## Nested Content Fragments {#nested-content-fragments}

When a Content Fragment field references another Content Fragment, you can use dot notation to directly access fields in the referenced fragment.

### Single-level nesting {#single-level-nesting}

An example for single-level nesting:

```handlebars
<article>
  <h1>{{{fields.title}}}</h1>

  <!-- Access author (a referenced Content Fragment) -->
  <div class="author-info">
    <h3>Author</h3>
    <p>Name: {{{fields.author.name}}}</p>
    <p>Email: {{{fields.author.email}}}</p>
    <p>Bio: {{{fields.author.bio}}}</p>
  </div>

  <div class="content">
    {{{fields.content}}}
  </div>
</article>
```

Pattern: `fields.referenceFieldName.nestedFieldName`

### Multi-level nesting {#multi-level-nesting}

The system supports unlimited nesting depth:

```handlebars
<article>
  <h1>{{{fields.title}}}</h1>

  <div class="author-details">
    <!-- Level 1: Author -->
    <p>Author: {{{fields.author.name}}}</p>

    <!-- Level 2: Author's Organization -->
    <p>Organization: {{{fields.author.organization.name}}}</p>
    <p>Website: {{{fields.author.organization.website}}}</p>

    <!-- Level 3: Organization's Address -->
    <p>Located in: {{{fields.author.organization.address.city}}},
    {{{fields.author.organization.address.country}}}</p>
  </div>

  <div class="content">
    {{{fields.content}}}
  </div>
</article>
```

Pattern: `fields.level1.level2.level3.fieldName` (limited depth; default is 5, can be extended to 10 by using the API)

### API parameter requirement: hydration {#api-parameter-requirements}

To enable nested Content Fragment access, you must include the `hydration` query parameter in your API call:

To enable Hydration:

```http
# Enable hydration with depth=2 for 2 levels of nesting
GET /adobe/sites/cf/fragments/{id}/preview?hydration=%7B%22enabled%22%3Atrue%2C%22maxDepth%22%3A2%7D
```

| `maxDepth` | What is loaded |
|--- |--- |
| `1` | Main fragment + direct references |
| `2` | Main fragment + direct references + their references |
| `3+` | Continue up to 10 levels |

## Multi-valued fields {#multi-valued-fields}

There are several types of multi-valued fields.

### Multi-valued text fields {#multi-valued-text-fields}

Text, [number](#multi-valued-number-fields), date, and other simple fields become arrays when multi-valued:

```handlebars
<article>
  <h1>{{{fields.title}}}</h1>

  <!-- Access individual items by index (use dot before bracket) -->
  <div class="tags">
    <span class="tag">{{{fields.tags.[0]}}}</span>
    <span class="tag">{{{fields.tags.[1]}}}</span>
  </div>

  <!-- Better: Iterate through all tags -->
  <div class="tags">
    {{#each fields.tags}}
    <span class="tag">{{{this}}}</span>
    {{/each}}
  </div>
</article>
```

Remember, when accessing array items by index in Handlebars:

* Use: 
  * `.[0]` (dot before bracket)
* Not: 
  * `[0]`

### Multi-valued number fields {#multi-valued-number-fields}

Numbers are converted to [strings](#multi-valued-text-fields) for rendering:

```handlebars
<div class="pricing">
  <h3>Available Prices:</h3>
  {{#each fields.prices}}
  <span class="price">${{{this}}}</span>
  {{/each}}
</div>
```

### Multi-valued Content Fragment references {#multi-valued-content-fragment-references}

When a field references multiple Content Fragments:

```handlebars
<div class="authors">
  <h3>Authors:</h3>
  {{#each fields.authors}}
  <div class="author">
    <h4>{{{this.name}}}</h4>
    <p>Email: {{{this.email}}}</p>
    {{#if this.bio}}
    <p class="bio">{{{this.bio}}}</p>
    {{/if}}
  </div>
  {{/each}}
</div>
```

### Multi-valued Asset references {#multi-valued-asset-references}

[Content Reference](/help/sites-cloud/administering/content-fragments/content-fragment-models.md#content-reference) fields configured for content types that are assets (for example, images and documents) are pre-rendered as HTML. Multi-valued assets become arrays:

```handlebars
<!-- Single asset -->
<div class="hero-image">
  {{{fields.heroImage}}}
</div>

<!-- Multi-valued: iterate through all images -->
<div class="gallery">
  {{#each fields.gallery}}
  <div class="image">{{{this}}}</div>
  {{/each}}
</div>
```

### Nested multi-valued references {#nested-multi-valued-references}

Multi-valued references can contain multi-valued references at any depth:

```handlebars
{{#each fields.chapters}}
<div class="chapter">
  <h3>Chapter: {{{this.title}}}</h3>

  {{#each this.authors}}
  <p>Author: {{{this.name}}}</p>

  {{#each this.publications}}
  <p>Publication: {{{this.title}}}</p>
  {{/each}}
  {{/each}}
</div>
{{/each}}
```

## Loops and iteration {#loops-and-iteration}

Handlebars provides the `{{#each}}` helper for iterating over arrays and objects.

### Iterating over arrays {#iterating-over-arrays}

An example of iterating over arrays:

```handlebars
<!-- Simple array iteration -->
{{#each fields.tags}}
<span class="tag">{{{this}}}</span>
{{/each}}

<!-- Array of objects -->
{{#each fields.authors}}
<div class="author">
  <h4>{{{this.name}}}</h4>
  <p>{{{this.email}}}</p>
</div>
{{/each}}

<!-- With empty-state fallback -->
{{#each fields.tags}}
<span class="tag">{{{this}}}</span>
{{else}}
<p>No tags available.</p>
{{/each}}
```

### Special variables in loops {#special-variables-in-loops}

Inside `{{#each}}` blocks, Handlebars provides special variables:

```handlebars
{{#each fields.items}}
<div class="item">
  <p>Index: {{@index}}</p>     <!-- 0-based index -->
  <p>Number: {{@number}}</p>   <!-- 1-based index -->
  <p>First: {{@first}}</p>     <!-- true for first item -->
  <p>Last: {{@last}}</p>       <!-- true for last item -->
  <p>Value: {{{this}}}</p>     <!-- current item -->
</div>
{{/each}}

<!-- Example: numbered steps with first/last CSS classes -->
<ul>
  {{#each fields.steps}}
  <li class="{{#if @first}}first{{/if}} {{#if @last}}last{{/if}}">
    Step {{@number}}: {{{this}}}
  </li>
  {{/each}}
</ul>
```

### Iterating over referenced fragments {#iterating-over-referenced-fragments}

An example of iterating over referenced fragments:

```handlebars
{{#if hasReferencedFragments}}
<section class="references">
  <h2>Related Content</h2>
  {{#each referencedFragments}}
  <article id="{{anchorId}}">
    <h3>{{title}}</h3>
    {{#if hasDescription}}
    <p>{{description}}</p>
    {{/if}}
    {{#if hasFields}}
    <ul>
      {{#each allFields}}
      <li><strong>{{name}}:</strong> {{{value}}}</li>
      {{/each}}
    </ul>
    {{/if}}
  </article>
  {{/each}}
</section>
{{/if}}
```

### Nested loops {#nested-loops}

An example of nested loops:

```handlebars
{{#each fields.categories}}
<section class="category">
  <h2>{{{this.name}}}</h2>

  {{#each this.products}}
  <article class="product">
    <h3>{{{this.name}}}</h3>
    <p>{{{this.description}}}</p>
  </article>
  {{/each}}
</section>
{{/each}}
```

## Conditional rendering {#conditional-rendering}

Use conditionals to show or hide content based on data availability.

### Basic If/Else {#basic-if-else}

An example of a basic if-else construct:

```handlebars
{{#if hasMainDescription}}
<p class="description">{{properties.description}}</p>
{{else}}
<p class="no-description">No description available.</p>
{{/if}}

<!-- Check field existence before rendering -->
{{#if fields.author}}
<div class="author">
  <p>By {{{fields.author.name}}}</p>
</div>
{{/if}}

{{#if fields.publishDate}}
<time>{{{fields.publishDate}}}</time>
{{/if}}
```

### Unless (negative conditional) {#unless-negative-conditional}

An `unless` helper:

```handlebars
<!-- Show author unless explicitly hidden -->
{{#unless fields.hideAuthor}}
<div class="author">{{{fields.author.name}}}</div>
{{/unless}}
```

### Nested Conditionals {#nested-conditials}

An example of nested conditional:

```handlebars
{{#if fields.author}}
<div class="author">
  <h3>{{{fields.author.name}}}</h3>

  {{#if fields.author.bio}}
  <p class="bio">{{{fields.author.bio}}}</p>
  {{/if}}

  {{#if fields.author.website}}
  <a href="{{{fields.author.website}}}">Visit Website</a>
  {{/if}}
</div>
{{/if}}
```

## Built-in Handlebars helpers {#built-in-handlebars-helpers}

Handlebars includes several built-in helpers, beyond `{{#if}}` and `{{#each}}`.

| Helper | Description |
|--- |--- |
| `{{#if condition}}` | Renders content if condition is truthy. Falsy values: `false`, `undefined`, `null`, `0`, `""`, `[]` |
| `{{#unless condition}}` | Renders content if condition is falsy (inverse of `#if`) |
| `{{#each array}}` | Repeats content for each item; supports `{{else}}` for empty arrays |
| `{{#with object}}` | Creates a new scope for a nested object, reducing path repetition |
| `{{lookup this "key"}}` | Dynamically looks up a property by name |

### With Helper {#with-helper}

Creates a new scope for nested objects to reduce repetitive path prefixes:

```handlebars
{{#with fields.author}}
<div class="author">
  <h3>{{{name}}}</h3>     <!-- same as fields.author.name -->
  <p>{{{email}}}</p>      <!-- same as fields.author.email -->
  <p>{{{bio}}}</p>        <!-- same as fields.author.bio -->
</div>
{{/with}}

<!-- Useful for deeply nested objects -->
{{#with fields.author.organization}}
<div class="organization">
  <h4>{{{name}}}</h4>
  <p>{{{website}}}</p>
  {{#with address}}
  <address>
    {{{street}}}<br/>
    {{{city}}}, {{{country}}}
  </address>
  {{/with}}
</div>
{{/with}}
```

## Advance Patterns {#advanced-patterns}

Some examples of advanced patterns follow.

### Accessing Parent Context in Nested Loops {#accessing-parent-context-in-nested-loops}

Use `../` to access the parent scope from within a nested loop:

```handlebars
<h1>{{{fields.title}}}</h1>

{{#each fields.chapters}}
<section class="chapter">
  <h2>Chapter {{@number}}: {{{this.title}}}</h2>

  {{#each this.sections}}
  <article>
    <!-- Access parent chapter via ../ -->
    <p>Chapter: {{{../title}}}</p>

    <!-- Access root context via ../../ -->
    <p>Book: {{{../../fields.title}}}</p>

    <h3>{{{this.title}}}</h3>
    <div>{{{this.content}}}</div>
  </article>
  {{/each}}
</section>
{{/each}}
``` 

### Dynamic CSS Classes {#dynamic-css-classes}

An example of dynamic CSS classes:

```handlebars
<article class="content-fragment {{#if hasMainDescription}}with-description{{/if}} {{#if hasReferencedFragments}}has-refs{{/if}}">
  <h1>{{main_cf_title}}</h1>
</article>

<ul class="tag-list">
  {{#each fields.tags}}
  <li class="tag {{#if @first}}first{{/if}} {{#if @last}}last{{/if}}">
    {{{this}}}
  </li>
  {{/each}}
</ul>
``` 

## Complete Examples {#complete-examples}

Several complete examples are provided for reference.

### Blog post with author

A blog post with author details:

```handlebars
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{main_cf_title}}</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; }
    .author-card { background: #f5f5f5; padding: 20px; border-radius: 8px; }
    .tags { display: flex; gap: 10px; }
    .tag { background: #007bff; color: white; padding: 5px 10px; border-radius: 4px; }
  </style>
</head>
<body>
  <article>
    <header>
      <h1>{{{fields.title}}}</h1>
      {{#if fields.publishDate}}
      <time datetime="{{{fields.publishDate}}}">{{{fields.publishDate}}}</time>
      {{/if}}
      {{#if fields.tags}}
      <div class="tags">
        {{#each fields.tags}}
        <span class="tag">{{{this}}}</span>
        {{/each}}
      </div>
      {{/if}}
    </header>

    {{#if fields.heroImage}}
    <figure>
      {{{fields.heroImage}}}
      {{#if fields.imageCaption}}
      <figcaption>{{{fields.imageCaption}}}</figcaption>
      {{/if}}
    </figure>
    {{/if}}

    <div class="content">
      {{{fields.content}}}
    </div>

    {{#if fields.author}}
    <aside class="author-card">
      <h3>About the Author</h3>
      <h4>{{{fields.author.name}}}</h4>
      {{#if fields.author.profilePicture}}
      <div class="author-image">{{{fields.author.profilePicture}}}</div>
      {{/if}}
      {{#if fields.author.bio}}
      <p>{{{fields.author.bio}}}</p>
      {{/if}}
      {{#if fields.author.email}}
      <p>Contact: <a href="mailto:{{{fields.author.email}}}">{{{fields.author.email}}}</a></p>
      {{/if}}
    </aside>
    {{/if}}
  </article>
</body>
</html>
``` 

Required API call:

```http
GET /adobe/sites/cf/fragments/{id}/preview?hydration=%7B%22enabled%22%3Atrue%2C%22maxDepth%22%3A1%7D
```

### Generic table view (no prior knowledge of fields) {#generic-table-view-no-prior-knowledge-of-fields}

A generic table view, without an inherent knowledge of fields. The is similar to the **Generic Template**:

```handlebars
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{{main_cf_title}}</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; }
    table { width: 100%; border-collapse: collapse; margin: 20px 0; }
    th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
    th { background-color: #f4f4f4; font-weight: bold; }
    .ref-section { background: #f9f9f9; padding: 20px; margin: 20px 0; border-radius: 8px; }
  </style>
</head>
<body>
  <header>
    <h1>{{properties.title}}</h1>
    {{#if properties.description}}<p>{{properties.description}}</p>{{/if}}
    <p><small>Path: {{main_cf_path}}</small></p>
  </header>

  {{#if hasFields}}
  <section>
    <h2>Fields</h2>
    <table>
      <thead>
        <tr><th>Field Name</th><th>Field Value</th></tr>
      </thead>
      <tbody>
        {{#each allFields}}
        <tr>
          <td><strong>{{name}}</strong></td>
          <td>{{{value}}}</td>
        </tr>
        {{/each}}
      </tbody>
    </table>
  </section>
  {{/if}}

  {{#if hasReferencedFragments}}
  <section class="ref-section">
    <h2>Referenced Content Fragments</h2>
    {{#each referencedFragments}}
    <article id="{{anchorId}}" style="margin-bottom: 30px;">
      <h3>{{title}}</h3>
      {{#if hasDescription}}<p>{{description}}</p>{{/if}}
      <p><small>Path: {{path}}</small></p>
      {{#if hasFields}}
      <table>
        <thead>
          <tr><th>Field Name</th><th>Field Value</th></tr>
        </thead>
        <tbody>
          {{#each allFields}}
          <tr>
            <td><strong>{{name}}</strong></td>
            <td>{{{value}}}</td>
          </tr>
          {{/each}}
        </tbody>
      </table>
      {{/if}}
    </article>
    {{/each}}
  </section>
  {{/if}}
</body>
</html>
``` 

## Best practices {#best-practices}

Best practices include:

1. Always use triple braces for field values that contain HTML markup content. 

   * Field values are pre-rendered HTML. 

     >[!NOTE]
     >
     >Double braces show raw HTML tags as plain text.

   ```handlebars
   <!-- CORRECT -->
   {{{fields.description}}}
   
   <!-- WRONG - displays HTML tags as text -->
   {{fields.description}}
   ``` 

1. Check for existence before accessing nested fields.

   ```handlebars
   <!-- GOOD: check before accessing nested fields -->
   {{#if fields.author}}
   <p>By {{{fields.author.name}}}</p>
   {{/if}}
   
   <!-- RISKY: may render empty if author is not set -->
   <p>By {{{fields.author.name}}}</p>
   ``` 

1. Use direct field access when possible. 

   * It is more readable, and maintainable, than iterating `allFields` and matching by name.

1. Structure templates with section comments.

   ```handlebars
   {{! ===== HEADER SECTION ===== }}
   <header>
     <h1>{{properties.title}}</h1>
   </header>

   {{! ===== MAIN CONTENT ===== }}
   <main>
     {{#if hasFields}}
     <!-- fields rendering -->
     {{/if}}
   </main>

   {{! ===== REFERENCES ===== }}
   {{#if hasReferencedFragments}}
   <!-- references rendering -->
   {{/if}}
   ``` 

1. Handle missing data gracefully with fallbacks.

   ```handlebars
   {{#if fields.title}}
   <h1>{{{fields.title}}}</h1>
   {{else}}
   <h1>Untitled</h1>
   {{/if}}
   ```

1. Always use a proper HTML document structure.

   ```handlebars
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <title>{{properties.title}}</title>
   </head>
   <body>
     <!-- your content here -->
   </body>
   </html>
   ```

1. Test with a variety of content scenarios:

   * All fields fully populated
   * Optional fields missing
   * Empty multi-valued fields
   * Deep nesting (multiple levels)
   * References that fail to load

1. Use semantic HTML elements:

   * For better accessibility use `<article>`, `<header>`, `<main>`, `<footer>`, `<time>`, `<address>`, or similar.

1. Keep styles in CSS. 

   * Use `<style>` tags or external stylesheets.
   * Avoid inline styles where possible.

1. Document complex logic:

   * Use Handlebars comments `({{! }})`.
   * Do not use HTML comments, which appear in rendered output.

## Troubleshooting {#troubleshooting}

Some troubleshooting hints include:

| Problem | Symptom | Solution |
|--- |--- |--- |
| Field shows HTML tags as text | `<p>Hello World</p>` displayed literally | Use triple braces: `{{{fields.description}}}` |
| Nested CF fields are empty or show [object Object] | `{{{fields.author.name}}}` is blank | Enable hydration in the API call; verify field name spelling; check that `maxDepth` is deep enough |
| Multi-valued field shows only the first item | Array with five items renders only one | Use `{{#each fields.tags}}` to iterate all items |
| Array index access not working | `{{{fields.tags[0]}}}` renders empty | Use dot-bracket syntax: `{{{fields.tags.[0]}}}` |
| Referenced fragments not appearing | `hasReferencedFragments` is always false | Enable hydration: `?hydration=%7B%22enabled%22%3Atrue%7D;` also check `{{#if referencesError}}` |
| Template renders nothing | Empty page or blank output | Check for unclosed `{{#if}}` or `{{#each}}` blocks; add diagnostic output: `<pre>hasFields: {{hasFields}}`&#124;`title: {{main_cf_title}}</pre>` |
| Comments appear in the rendered page | HTML comment text visible to end users | Use Handlebars comments `{{! comment }}` instead of HTML `<!-- comment -->` |
| Conditional always evaluates to true | `{{#if fields.enabled}}` is always truthy | Note: the string `"false"` is truthy in Handlebars. Only actual `false`, `null`, `undefined`, `0`, `""`, and `[]` are falsy. |
| Special characters rendering as entities | `&lt;`, `&amp;` shown instead of `<`, `&` | Use triple braces for pre-rendered HTML content: `{{{fields.content}}}` |
| Cannot access outer loop variable from inner loop | Variable from parent `#each` is undefined | Use `../` for parent scope: `{{{../name}}}`; use `../../` for grandparent |
| Empty list not showing fallback message | Multi-valued field with zero items shows nothing | Use `{{else}}` inside `{{#each}}`: `{{#each fields.tags}}...{{else}}<p>No tags</p>{{/each}}` |

### Working with Assets {#working-with-assets}

Assets referenced from Content Fragments are pre-rendered as HTML by AEM. Therefore, triple braces are mandatory for all asset references.

| Asset type | Rendered as |
|--- |--- |
| Images | `<img src="..." alt="...">` |
| Videos | `<video>` element |
| Documents | `<a href="...">` link |

Remember:

* Always use triple braces for asset fields. 
  Using double braces will escape the generated HTML tag and display it as raw text rather than rendering the image, video, or link.

### Asset field usage {#asset-field-usage}

An example of asset field usage:

```handlebars
<!-- CORRECT - triple braces render the image -->
{{{fields.heroImage}}}
<!-- Output: <img src="path/to/image.jpg" alt="Hero"> -->

<!-- WRONG - double braces escape the tag, showing it as text -->
{{fields.heroImage}}
<!-- Output: &lt;img src="path/to/image.jpg" alt="Hero"&gt; -->
``` 

## Custom template helpers {#customer-template-helpers}

The system provides custom Handlebars helpers for generating HTML elements with custom HTML attributes. These helpers give you control over the generated markup, while handling the complexity of extracting source URLs from pre-rendered content.

Available helpers:

1. `asset` - Generates `<img>` tags with custom attributes
1. `text` - Generates `<span>` tags wrapping text content with custom attributes

### `asset` helper {#asset-helper}

Syntax:

```handlebars
{{{asset fieldValue attribute1="value1" attribute2="value2"}}}
```

Remember:

* Use triple braces `{{{ }}}` with the asset helper, not double braces!

#### Four basic examples {#four-basic-examples}

Four basic examples are:

```handlebars
<!-- Add a CSS class to an image -->
{{{asset fields.heroImage class="hero-image"}}}
<!-- Output: <img src="..." alt="..." class="hero-image"> -->

<!-- Add multiple CSS classes -->
{{{asset fields.productImage class="product-img responsive shadow"}}}

<!-- Add id and class -->
{{{asset fields.logo class="brand-logo" id="main-logo"}}}

<!-- Add data attributes -->
{{{asset fields.thumbnail class="thumb" data-category="product" data-id="123"}}}
```

#### Supported Attributes {#supported-attributes}

You can add any valid HTML attribute:

| Attribute | Example |
|--- |--- |
| `class` | `class="my-class another-class"` |
| `id` | `id="unique-id"` |
| `alt` | `alt="Custom alt text" (overrides existing alt)` |
| `data-*` | `data-index="1" data-type="hero"` |
| `aria-*` | `aria-label="Description" aria-hidden="true"` |
| `width` | `width="300"` |
| `height` | `height="200"` |
| `loading` | `loading="lazy"` |
| `style` | `style="border-radius: 8px;"` |

#### Override Alt Text {#override-alt-text}

The `alt` attribute from the original image can be overridden:

```handlebars
{{{asset fields.photo alt="Custom description for accessibility"}}}
```

#### Complex example {#complex-example}

A complex example is:

```handlebars
<article class="blog-post">
<header>
{{{asset fields.featuredImage 
class="featured-image responsive" 
id="post-hero"
loading="lazy"
data-post-id="12345"}}}
</header>
</article>
```

#### Using with loops {#using-with-loops}

Asset helper in loops:

```handlebars
{{#each fields.galleryImages}}
{{{asset this class="gallery-item" data-index=@index}}}
{{/each}}
```

### `text` helper {#text-helper}

The text helper generates a `<span>` tag wrapping text content with custom CSS classes and HTML attributes. Useful for styling individual text fields.

Syntax:

```handlebars
{{{text fieldValue attribute1="value1" attribute2="value2"}}}
```

Remember:

* Use triple braces `{{{ }}}` with the text helper, not double braces!

#### Three Basic examples {#three-basic-examples}

Three basic examples are:

```handlebars
<!-- Add a CSS class to text -->
{{{text fields.title class="article-title"}}}
<!-- Output: <span class="article-title">The Title Text</span> -->

<!-- Add multiple attributes -->
{{{text fields.price class="price-tag" id="product-price" data-currency="USD"}}}

<!-- Style inline text -->
{{{text fields.highlightedText class="highlighted" style="background: yellow;"}}}
```

#### Common Use Cases {#common-use-cases}

Some common use cases include:

```handlebars
<!-- Styling article metadata -->
<article>
<header>
{{{text fields.category class="category-badge"}}}
<h1>{{{fields.title}}}</h1>
{{{text fields.author class="byline"}}}
{{{text fields.publishDate class="date"}}}
</header>
</article>

<!-- Creating styled labels -->
<div class="product-card">
{{{text fields.productName class="product-name"}}}
{{{text fields.brand class="brand-label" data-brand-id="abc"}}}
{{{text fields.price class="price" id="main-price"}}}
</div>

<!-- Accessibility enhancements -->
{{{text fields.importantNote class="alert" role="alert" aria-live="polite"}}}
```

#### With loops {#with-loops}

A common use case with loops includes:

```handlebars
{{#each fields.tags}}
{{{text this class="tag-badge"}}}
{{/each}}
```

### Helpers - Attribute validation {#helpers-attribute-validation}

Both helpers validate attribute names before including them in the output.

Valid attribute names:

* Must start with a letter (a-z, A-Z)
* Can only contain letters, digits, hyphens, and underscores; see the [Naming Conventions](/help/implementing/developing/introduction/naming-conventions.md)
* Case-insensitive
* For example:
  * Valid:
    * `class`, `id`, `data-value`, `aria-label`, `my_attr`, `dataIndex1`
  * Invalid:
    * `123-attr`, `-class`, `@special`, `$money`

Invalid attribute names are silently skipped with a warning in the logs:

```handlebars
{{{asset fields.image class="valid" 123-invalid="skipped" id="also-valid"}}}
<!-- Output: <img src="..." alt="..." class="valid" id="also-valid"> -->
<!-- 123-invalid is skipped because it starts with a number -->
```

Remember:

* Check server logs for "Blocked invalid attribute name format" warnings.

## Comparing direct output to helpers {#comparing-direct-output-to-helpers}

When to ise direct output `{{{fields.xxx}}}`:

* You do not need custom styling
* You want the default output as-is
* The field contains complex HTML that you do not want to modify

When to use helpers:

* You need to add CSS classes for styling
* You need to add custom HTML attributes (`data-*`, `aria-*`, and others)
* You want consistent, controlled HTML structure

Comparison:

```handlebars
<!-- Direct output - uses whatever HTML the system generates -->
{{{fields.heroImage}}}
<!-- Output: <img src="/path/image.jpg" alt="Hero Image"> -->

<!-- With asset helper - full control over attributes -->
{{{asset fields.heroImage class="hero responsive" id="main-hero" loading="lazy"}}}
<!-- Output: <img src="/path/image.jpg" alt="Hero Image" class="hero responsive" id="main-hero" loading="lazy"> -->
```

## Quick reference {#quick-reference}

Some quick reference information is provided for reference.

### Context variables {#context-variables}

The context variables:

```handlebars
{{properties}}                <!-- Main fragment metadata -->
{{fields}}                    <!-- Map keyed by field name to rendered values (such as strings, lists, nested maps for CF refs, commerce maps, HTML, and others) -->
{{allFields}}                 <!-- List of { name, value } maps (uniform iteration) -->
{{hasFields}}.                <!-- Boolean -->
{{hasReferencedFragments}}.   <!-- Boolean -->
{{referencedFragments}}       <!-- List of referenced-fragment maps -->

```

### Field access {#field-access}

How to access fields:

```handlebars
{{{fields.fieldName}}}                    <!-- Direct field -->
{{{fields.author.name}}}                  <!-- Nested CF field -->
{{{fields.author.org.address.city}}}      <!-- Multi-level nesting -->
{{{fields.tags.[0]}}}                     <!-- Array by index -->
{{#each fields.tags}}...{{/each}}         <!-- Array iteration -->
{{{fields.authors.[0].name}}}             <!-- Multi-valued CF reference -->
```

### Control flow {#control-flow}

The control flow:

```handlebars
{{#if condition}}...{{/if}}               <!-- Conditional -->
{{#if condition}}...{{else}}...{{/if}}    <!-- If/else -->
{{#unless condition}}...{{/unless}}       <!-- Negative conditional -->
{{#each array}}...{{/each}}               <!-- Iteration -->
{{#each array}}...{{else}}...{{/each}}    <!-- Iteration with fallback -->
{{#with object}}...{{/with}}              <!-- Change scope -->
```

### Loop variables {#loop-variables}

The loop variables:

```handlebars
{{@index}}        <!-- 0-based index -->
{{@number}}       <!-- 1-based index -->
{{@first}}        <!-- true for first item -->
{{@last}}         <!-- true for last item -->
{{@key}}          <!-- Object property name -->
{{this}}          <!-- Current item -->
{{../parent}}     <!-- Access parent scope -->
```

### Custom template helpers {#custom-template-helpers}

The custom template helpers:

```handlebars
{{{asset fields.image class="css-class"}}}                <!-- Image with class -->
{{{asset fields.image class="c1" id="my-id"}}}            <!-- Image with multiple attrs -->
{{{asset fields.image alt="Custom alt text"}}}            <!-- Override alt text -->
{{{asset fields.image loading="lazy" data-x="val"}}}      <!-- Custom attributes -->

{{{text fields.title class="title-class"}}}               <!-- Span with class -->
{{{text fields.price class="price" id="p1"}}}             <!-- Span with multiple attrs -->
{{{text this class="item" data-index=@index}}}            <!-- In loops -->
```

## Additional resources {#additional-resources}

Additional resources are available:

* [Handlebars documentation](https://handlebarsjs.com/)
* [Handlebars built-in helpers](https://handlebarsjs.com/guide/builtin-helpers.html)
* [AEM Content Fragments documentation](/help/sites-cloud/administering/content-fragments/overview.md)

