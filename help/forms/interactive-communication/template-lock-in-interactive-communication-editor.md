---
title: Template Lock in Interactive Communication Editor
description: Template Lock in Interactive Communication Editor provides the ability to the template authors to lock the layout or content for the document authors.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
hide: yes
index: no
hidefromtoc: yes
---

# Template Lock in Interactive Communication Editor

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

## 1. Introduction

The Template Lock feature in the Interactive Communication (IC) Editor allows template authors to restrict modifications to specific elements of a communication template. This ensures design consistency, protects critical content, and enforces governance across teams that reuse templates to create personalized communications.

When applied, locked components appear visually distinct and cannot be modified by downstream authors or contributors, depending on the lock type set. This feature helps maintain brand standards, data integrity, and layout uniformity across all derived communications.

## 2. Lock Types

Template authors can apply Content and Layout Locks, individually or together to control content and layout changes in Interactive Communication templates:

### 2.1 Content Lock

A Content Lock restricts any modification to the content or properties of the selected element. This type of lock ensures that essential data, text, or design properties remain unchanged, even when reused across multiple communications.

When applied, authors cannot modify:

- Text content or captions

- Appearance settings (font, color, background, borders, etc.)

- Data binding configurations

- Constituent elements within a container component (such as subforms)

### 2.2 Layout Lock

A Layout Lock restricts changes related to the position and size of an element. This ensures that visual alignment and design hierarchy remain consistent with brand or document standards.

When applied, authors cannot:

- Move the element to a new position on the page

- Resize the element's width or height

## 3. Behavior in Derived Communications

- When a communication is created from a locked template, the locked elements appear as read-only in the IC Editor for communication authors.

- Components with content lock cannot have their inner properties or bindings changed.

- Components with layout lock cannot be moved or resized.

This allows template creators to maintain control over design and structure while enabling other users to focus on variable content and data-driven customization.

## 4. Best Practices

- **Lock critical Components early:** Apply locks to headers, footers, legal disclaimers, and logos to preserve compliance and brand identity.

- **Use content locks for accuracy:** Protect fields bound to core data models or regulatory text.

- **Use layout locks for consistency:** Prevent misalignment or visual distortion in frequently reused templates.

- **Communicate lock usage:** Ensure downstream users are aware of which sections are intentionally restricted to avoid confusion.
