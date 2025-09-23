---
title: Subform in Interactive Communication Editor
description: Subform in Interactive Communication Editor manage layouts, control object positioning, and define how content flows across pages.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
---

# Subform in Interactive Communication Editor

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

## 1. Introduction

A Subform in the Interactive Communication Editor is a container object used to group fields, objects, and components into a logical section. It helps manage layouts, control object positioning, and define how content flows across pages. Subforms are essential for creating structured, reusable, and responsive communications, especially when dealing with dynamic or repeated content.

By using subforms, authors can maintain consistency, manage pagination, and bind entire sections to structured data sources.

## 2. Properties

2.1 Form Design Layouts

- **Fixed Layout:** Objects maintain exact positions on the page. Best for static designs where precision placement is required (e.g., invoices or official letters).

- **Flowable Layout:** Objects adjust dynamically based on content length and screen size. Suitable for communications that require responsive design or varying data lengths.

2.2 Subform Positioning

- **Pagination:** Control how subforms break across pages. Options include keeping subforms together or allowing page breaks within them.

- **Position:** Specify whether the subform is placed relative to its parent container or flows naturally within the layout.

- **Appearance:** Define background, borders, and styling for the subform to visually separate content.

- **Presence:** Configure visibility settings—Visible, Hidden, or Conditional—depending on business rules or data values.

2.3 Data Binding

- Subforms can be bound directly to **Form Data Model (FDM)** nodes or arrays.

- Binding allows the subform to repeat dynamically for each record in a collection (e.g., multiple policies, transactions, or addresses).

- Supports both static and dynamic population of content based on the data structure.

## 3. Usage

Subforms are widely used for:

- Structuring documents into sections like header, body, and footer.

- Repeating content such as tables, itemized bills, or lists of policies.

- Managing pagination so grouped content stays together.

- Conditional display of sections based on rules or data values.

- Applying layout control (fixed or flowable) depending on the communication type.

Authors can drag a subform from the Object Library into the canvas and adjust its layout, positioning, and binding from the Properties Panel.

## 4. Best Practices

- **Choose layout wisely:** Use fixed layout for forms requiring exact placement, and flowable layout for dynamic, data-driven communications.

- **Bind collections carefully:** For lists or arrays, bind subforms directly to FDM collections with template rows.

- **Optimize pagination:** Prevent awkward breaks by grouping related objects in a subform.

- **Use conditional presence:** Hide or display subforms dynamically based on data values.

- **Maintain hierarchy:** Nest subforms logically to make complex layouts easier to manage.

- **Test with varied data:** Preview with short, long, and empty datasets to ensure the design adapts correctly.

By leveraging Subforms effectively, authors can achieve cleaner layouts, better control over dynamic content, and ensure communications adapt seamlessly to both data-driven and static scenarios.
