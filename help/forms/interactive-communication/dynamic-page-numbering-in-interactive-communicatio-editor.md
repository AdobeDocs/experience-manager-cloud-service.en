---
title: Dynamic Page Numbering in Interactive Communication Editor
description: Dynamic Page Numbering in Interactive Communication Editor allows authors to automatically display page numbers in their PDF output.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
hide: yes
index: no
hidefromtoc: yes
---

# Dynamic Page Numbering in Interactive Communication Editor

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

## Introduction

The Dynamic Page Numbering feature in Interactive Communication (IC) allows authors to automatically display page numbers in their PDF output. Page numbering can be enabled at the master page level, ensuring consistent numbering across all associated design pages. This helps maintain clear page tracking and a professional layout throughout multipage communications.

## Key Capabilities

- **Master Page Configuration:**
Page numbering can be enabled at the master page level. Once activated, it automatically applies to all associated design pages linked to that master page.

- **Automatic Placement:**
A page numbering component appears at the bottom center of each page with the format:
"**Page # of ##**"

    - The first **#** represents the current page number.

    - The second **##** represents the total number of pages in the communication.

- **Dynamic Display on PDF Preview:**
The page numbers dynamically render during PDF preview, displaying accurate page numbering in the final output.

### Example

When previewing a 5-page Interactive Communication, each page will display:

Page 1 of 5

Page 2 of 5

… and so on, dynamically updating during PDF generation.

## Key Benefits

- Enhances document readability and professionalism.

- Automates page numbering without manual intervention.

- Maintains consistency across all pages linked to a master page.
