---
title: Experience Modernization Agent Capabilities and Add-ons
description: Reference the built-in workflows and optional add-ons for migration, design, development, and project guidance.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: f2d27a5f-0d67-4d85-8a24-86a8d8a3574b
    internal-label: Developer tools
  - id: ac5ecfc1-cc78-4ecc-a90a-0362685062ce
    internal-label: AI Tools
subfeature_v2:
  - id: f88183b7-5ea5-436c-ac46-96b53f0281ea
    internal-label: Edge Delivery Services
  - id: f1710108-e0d1-47e5-9952-1888729a03da
    internal-label: Agentic AI
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Capabilities and Add-ons {#capabilities}

The Experience Modernization Agent chooses a workflow, which it calls a skill, from the task that you describe. This reference groups its capabilities by the work they support, from migration to continued development.

An entry marked "Built in" needs no add-on. For optional entries, the table gives the add-on ID used in the project's configuration. To turn one on or save the choice for your team, see [Optional Capabilities](console.md#optional-capabilities).

## Plan and Migrate {#migration}

Use these workflows to understand a source site, import its content and design, and check the result.

| Capability | What it does | Add-on |
|---|---|---|
| Site catalog and planning | Discovers pages and groups them into templates and block variants, with screenshots and a report that you refine in the **Planning** view. See [Plan a Migration with the Site Catalog](site-catalog.md). | Built in |
| Page and design migration | Imports pages into default content and blocks, extracts design tokens and global styles, and rebuilds the shared header, navigation, and footer. See [Migrate a Production Site](production-migration.md). | Built in |
| Bulk import | Runs each template's generated import script on its other pages, then corrects the script for pages that differ from their source. See [How the Agent Migrates at Scale](production-migration.md#migration-at-scale). | Built in |
| Visual critique | Compares a block, a page, or the whole site with the source, then fixes content, structure, and styling differences. See [Critique the Site](prompting-guide.md#site-critique). | Built in |
| Protected source pages | Imports content from sources with sign-in requirements. See [Protected Site Authentication](console.md#protected-site-authentication) for supported methods and setup. | Built in |
| Experience Manager authoring models | Creates the block models that the Universal Editor uses when content is stored on an author instance. See [Getting Started with Experience Manager Authoring](getting-started-aem-authoring.md). | Built in |
| Forms migration | Migrates source forms to the form block of Edge Delivery Services for Adobe Experience Manager Forms, for organizations that license Experience Manager Forms. See [What the Forms Add-on Does](block-development.md#forms-add-on). | `forms-excat@excat-extended` |
| Commerce pages | Detects product detail and listing pages and imports them as pages whose commerce blocks load product data from the catalog. It is built for Adobe Commerce storefronts in document-based projects. See [Commerce Pages](block-development.md#commerce-pages). | `excat-commerce@excat-extended` |

## Design and Develop {#development}

Use these capabilities during a migration or on an existing site. The same block and styling work continues after go-live.

| Capability | What it does | Add-on |
|---|---|---|
| Restyling | Applies a new design from reference pages, screenshots, or specifications. See [Restyle Sites](restyling.md). | Built in |
| Block development and integrations | Creates, updates, and refactors blocks from real content, reuses suitable blocks, and writes connections to other systems. See [Create, Update, and Refactor Blocks](block-development.md). | Built in |
| Figma import | Migrates blocks and creates pages from Figma components and frames. See [Create a Block from Figma](prompting-guide.md#figma-block-migration) and [Work from a Figma Design](visual-changes.md#figma). | `excat-figma@excat-extended` |
| Guided redesign (Stardust) | Redesigns several pages towards a new design direction, step by step, with checks along the way. See [Guided Redesign](restyling.md#guided-redesign). | `stardust@excat-extended` |
| Design craft | Applies frontend design-quality guidance for typography, spacing, and visual hierarchy. Guided redesign turns it on automatically; it can also be used on its own. | `impeccable@excat-extended` |
| Block library setup | Sets up the library where authors find and insert the project's blocks. See [What the Agent Provides With a Block](block-development.md#block-deliverables). | `excat-block-library@excat-extended` |
| Modern web guidance | Applies current web-platform practices for fonts, loading performance, accessibility, and layout when writing CSS and JavaScript. | `modern-web-guidance@excat-extended` |

## Document and Troubleshoot {#project-guidance}

Use these capabilities to understand the console, hand over the project, or investigate site problems.

| Capability | What it does | Add-on |
|---|---|---|
| Console tour | Explains views and actions when you ask "Give me a tour of the console." See [Experience Modernization Console](console.md). | Built in |
| Project documentation | Generates PDF guides for authors, developers, and administrators from the project's code and configuration. See [Generate Project Documentation](project-documentation.md). | `project-management@excat-extended` |
| Edge Delivery Services troubleshooting | Diagnoses problems on demand, such as blocks that don't render or changes that don't appear. See [Debug a Problem](prompting-guide.md#debugging). | `excat-support@excat-extended` |

The add-ons on offer can change between releases. If the agent says that it can't do something, ask whether an add-on covers it.
