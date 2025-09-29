---
title: Supported HTML markup tags in Document of Record
description: Reference guide for HTML markup tags now supported in Document of Record generation, including rendering behavior and accessibility considerations
feature: Adaptive Forms
role: Developer, User
exl-id: 8481b0dc-aae7-4bd2-acfe-1f1b6d747683
---

# Supported HTML markup tags in Document of Record

## What this reference covers?

AEM Forms now supports HTML markup tags in rich text fields when generating Document of Record (DoR) PDFs. This guide explains which HTML markup tags you can safely use in Adaptive Forms and how they render in the generated documents.

If you add rich text content (such as bold formatting, lists, or links) to your forms, it's important to understand which tags are supported and any limitations they may have. This reference helps you choose the appropriate tags to ensure your content displays correctly and remains accessible in the Document of Record.

## Before you start

### Prerequisites

You should be familiar with:

- Basic HTML markup syntax
- [Document of Record fundamentals](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md)
- Accessibility principles and WCAG guidelines
- PDF accessibility requirements
- Adaptive Form components that accept HTML markup

### Considerations

The Document of Record (DoR) can be a tagged PDF, which helps ensure accessibility and proper structure for assistive technologies. To enable tagged PDF output, [set the XCI property `config/present/pdf/tagged` to `true`](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md#use-a-custom-xci-file). After generating your PDF, it's important to verify that accessibility tags are correctly applied. You can use [Adobe Acrobat to check accessibility tags](https://helpx.adobe.com/in/acrobat/using/create-verify-pdf-accessibility.html) and ensure your document meets accessibility standards.

### What's new

Rich text support in Document of Record is a recent enhancement. Previously, rich text content appeared as plain text in generated documents. This new capability allows formatted content to render properly in PDF outputs.

## HTML tag support reference

### Fully supported tags

These tags are fully supported with proper accessibility node creation:

| HTML Tag | Description | Document of Record Support | Accessibility | Example |
|----------|-------------|-------------|---------------|---------|
| `<p>` | Paragraph |  Yes |  Fully Supported - Correct `<P>` node | `<p>This is a paragraph.</p>` |
| `<br/>` | Line break |  Yes | Fully Supported - within `<P>` node | `<p>Line 1<br/>Line 2</p>` |
| `<b>` | Bold text |  Yes |  Fully Supported - within `<P>` node | `<b>bold text</b>` |
| `<i>` | Italic text |  Yes |  Fully Supported - within `<P>` node | `<i>italic text</i>` |
| `<span>` | Generic inline container |  Yes |  within block elements | `<span>styled text</span>` |
| `<sub>` | Subscript |  Yes | Fully Supported - within block elements  | `H<sub>2</sub>O` |
| `<sup>` | Superscript |  Yes | Fully Supported - Within block elements| `E=mc<sup>2</sup>` |
| `<a>` | Hyperlink |  Yes | Limited support - needs proper nesting | `<a href="url">link text</a>` |


#### List accessibility issue

Current list rendering creates `<P>` nodes instead of proper list structure:

```
Current: <P>1. First item
Current: <P>2. Second item

Expected: <L>
Expected:   <LI>
Expected:     <LBL>1.
Expected:     <LBody>First item
```

### Unsupported tags

These tags are not supported and will not render properly:

| HTML Tag | Description | Alternative Solution |
|----------|-------------|---------------------|
| `<h1>` - `<h6>` | Heading tags | Use styled `<p>` tags or design-level headers |
| `<img>` | Images | Use separate image fields or design templates |
| `<code>` | Code blocks | Use monospace fonts with `<span>` styling |
| `<blockquote>` | Block quotations | Use styled `<p>` tags with indentation |
| `<table>` | Tables | Use Adaptive Form table components |

## Code examples

### Basic text formatting

```html
<!--  Supported - renders correctly -->
<p>This paragraph contains <b>bold text</b> and <i>italic text</i>.</p>

<!--  Supported - combined formatting -->
<p>This text is <i><b>bold and italic</b></i>.</p>

<!--  Unsupported - headings don't work -->
<h1>This won't render as a heading</h1>
```

### Lists

```html
<!-- ⚠️ Partially supported - renders but not accessible -->
<ol>
  <li>First numbered item</li>
  <li>Second numbered item</li>
</ol>

<ul>
  <li>First bullet point</li>
  <li>Second bullet point</li>
</ul>
```

### Links

```html
<!--  Supported - but must be within block elements -->
<p>Visit our <a href="https://example.com">website</a> for more information.</p>

<!--  Incorrect - link not properly nested -->
<a href="https://example.com">Standalone link</a>
```

### Scientific notation

```html
<!--  Supported - but limited accessibility -->
<p>Water formula: H<sub>2</sub>O</p>
<p>Einstein's equation: E=mc<sup>2</sup></p>
```

## Related Content


- [Generate Document of Record for Adaptive Forms](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md)
- [Generate Document of Record for Core Components](/help/forms/generate-document-of-record-core-components.md)
- [Document of Record template customization](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md#customize-the-branding-information-in-document-of-record)

