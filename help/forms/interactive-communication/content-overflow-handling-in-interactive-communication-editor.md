---
title: Content Overflow Handling in Interactive Communication Editor
description: Content Overflow Handling in Interactive Communication Editor enhances how text behaves within Flowed and Positioned layouts.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
hide: yes
index: no
hidefromtoc: yes
---

# Content Overflow Handling in Interactive Communication Editor

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

## Introduction

The Content Overflow Handling feature in the Interactive Communication Editor enhances how text behaves within Flowed and Positioned layouts.
It ensures smooth content continuity for flowed layouts and provides visual alerts for positioned layouts, giving authors better control and flexibility when designing communications.

## Key Capabilities

### Flowed Layout

- **New Option:**
Adds a property **allow page breaks** within content to control overflow behavior. This option is visible only when the parent subform is set to Flowed and it's **Allow page breaks** property is enabled.

- **Automatic Page Continuation:**
When content exceeds the available space, a new page is automatically created, and editing continues seamlessly.

- **Copy-Paste Support:**
Large text pasted into the editor automatically flows across pages, maintaining layout consistency.

### Positioned Layout

- **Overflow Indicator:**
When content exceeds the container (subform or page), the text editor expands for editing, but the element height stays fixed.

- **Visual Alert:**
A red border appears at the bottom of the container to indicate overflow.

- **Manual Adjustment:**
Authors manually resize the container to fit additional content.

>[!NOTE]
>
> This feature requires the entire parent hierarchy (such as subforms) to be set to Flowed. If any parent subform in the hierarchy is Positioned, the **Allow page breaks** within content option will not work as expected.

## Benefits

- Improves content authoring efficiency and control.

- Maintains consistent layout and readability across pages.

- Helps identify overflow quickly through visual indicators.

- Enhances communication design flexibility for both layout types.
