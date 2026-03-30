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

### Basic Syntax {#basic-syntax}

The basic syntax that you will need is:

```html
<!-- Output a variable (HTML-escaped) -->
{{variableName}}

<!-- Output raw HTML (unescaped) -->
{{{htmlContent}}}

<!-- Comment (not rendered) -->
{{! This is a comment }}
```

### Key Concepts {#key-concepts}

| Basic Syntax | Description | When to use |
|--- |--- |--- |
| `{{ }}` | Escapes HTML special characters — safe for plain text | Properties, titles, metadata values |
| `{{! }}` | Handlebars comment — not rendered in output | Template documentation and section labels |
| `{{{ }}}` | Outputs raw HTML (unescaped) | All field values (they contain pre-rendered HTML) |

>[!IMPORTANT]
>
>Use triple braces `{{{ }}}` for all field values as they contain pre-rendered HTML. Using double braces displays raw HTML tags as text.

## The Generic Template {#the-generic-template}

The **Generic Template**:

* displays the fields of your fragment in table form; name and content
* shows the content of referenced fragments in separate tables, with the same format

![Preview Fragment with Generic HTML Template](/help/sites-cloud/administering/content-fragments/assets/cf-preview-html-template-referenced-fragment.png)

The **Generic Template** has no knowledge of the fragment, it simply loops through all fields, and all referenced fragments to display the contents.

```html
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
    <h1>{{main_cf_title}}</h1>
    {{#if hasMainDescription}}<p>{{main_cf_description}}</p>{{/if}}
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

  {{#if referencesError}}
  <div style="background: #ffebee; border-left: 4px solid #f44336; padding: 15px; margin: 20px 0;">
    <strong>Error Loading Referenced Fragments</strong>
    {{#if referencesErrorMessage}}<p>{{referencesErrorMessage}}</p>{{/if}}
  </div>
  {{/if}}
</body>
</html>
```
