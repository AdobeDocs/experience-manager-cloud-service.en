---
title: AOE Delivery of the Experience Modernization Agent
description: Learn about Adobe Agentic Outcome Engineers (AOEs) and how they can help you succeed with the Experience Modernization Agent.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 75f73bb8-4d97-4c8f-b364-374a2a026b19
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

# AOE Delivery of the Experience Modernization Agent {#aoe-delivery}

Learn about Adobe Agentic Outcome Engineers (AOEs) and how they can help you succeed with the Experience Modernization Agent.

## The Agentic Outcome Engineer (AOE) {#aoe}

AOEs are Adobe engineers who operate the Experience Modernization Agent (EMA) on your behalf. AOE delivery is an optional engagement model, not a separate tier of agent capabilities. The team works with you to:

* Translate AI-assisted automation into production-ready customer outcomes.
* Resolve migration and implementation issues within the agreed engagement.
* Transfer project knowledge to the team that will maintain the site.

## AOE-Led Delivery {#aoe-led}

AOEs combine EMA automation with engineering work and customer review. Agree scope, responsibilities, acceptance criteria, and support arrangements with your Adobe account team before work begins. Do not infer a delivery guarantee, price, or entitlement from the availability of the console.

## Engagement Process {#engagement-process}

AOE engagement is a structured process.

### 1. Scoping {#scoping}

Contact your Adobe account team with your migration requirements and scope. The AOE team reviews eligibility and proposes an approach, estimate, and schedule.

* **Inputs:** Authorized source URLs, CMS platform, content inventory, design references, timeline, authoring target, integrations, access constraints, and acceptance needs
* **Outputs:** Eligibility confirmation, effort estimate, migration approach, engagement structure

### 2. Planning {#planning}

A kickoff meeting is held, along with a source site analysis, content audit, design alignment, component library review, and authoring tool selection.

* **You** provide all necessary assets and guidelines.
* **Adobe** proposes the migration plan, timeline, roles, and checkpoints for agreement.
* **Together**, confirm content/code destinations, release authority, exceptions, and the recovery approach.

### 3. Execution {#execution}

* **AOE activities:** Operate the Experience Modernization Console, review AI outputs, apply brand guidelines, refine as needed
* **Your activities:** Review deliverables, validate content and designs, test authoring

Checkpoints are implemented to ensure content accuracy, including component mapping, design review, authoring workflow, and pre-launch validation.

### 4. Handoff {#handoff}

* **Deliverables:** Agreed website code, migrated content, documentation, validation reports, and a record of acceptance and remaining exceptions
* **Activities:** Knowledge transfer, authoring training, developer onboarding

### 5. Post-Migration {#post-migration}

Confirm who owns ongoing content, code, integrations, and operations. Follow the support arrangements agreed for the engagement and your Adobe support entitlement; do not assume ongoing AOE implementation work is included after handoff.

## AOE Delivery Scope {#scope}

The engagement defines which automated and manual work is included. The sections below describe the areas to agree, not a promise that every project requirement is included.

### Source Platforms {#source-platforms}

Sources can include WordPress, Drupal, Sitecore, legacy AEM, SharePoint, or custom sites where authorized content can be extracted. The standard source scope described for this service is publicly accessible static HTML. Have the AOE team explicitly assess protected, interaction-dependent, or private-network sources rather than assume they are included.

This service-scoping boundary is not a blanket product limitation: some EMA workflows can capture client-rendered content or use supported source authentication. It is also not a limit on the complexity of sites EDS can deliver. Agree source access and extraction for the actual engagement.

### Included in AOE Scope {#included}

#### Target Platform {#target-platform}

* **Edge Delivery Services:** All migrations target Edge Delivery Services (EDS), Adobe's high-performance web delivery platform.
* **Authoring target:** Agree document-based persistence, edited visually in Experience Workspace, or AEM authoring with JCR persistence and the Universal Editor. Adobe strongly recommends document-based persistence with Experience Workspace for new implementations. See [Where Content Is Stored and How Authors Edit It](overview.md#content-storage). Confirm the setup and handover for the selected target.

#### Migration Work Performed {#migration-work}

* **Migration approach:** Agree faithful migration, redesign, or an incremental phased migration.
* **Static content import:** Automated extraction of static HTML content from source websites and automated mapping to EDS [default content and blocks](overview.md#eds-basics)
* **Design system:** Extraction of brand tokens (colors, typography, spacing) and application to the new site
* **Design references:** Agree the source site, Figma, or other supplied references and what fidelity means for acceptance. Do not assume every design format has a dedicated automated importer.
* **Responsive design:** Mobile and desktop layouts handled appropriately

#### Resulting System {#resulting-system}

The resulting site uses EDS. Agree and measure the required performance, accessibility, SEO, functional, and authoring outcomes on representative real pages. Architecture or automated scores alone do not guarantee load times, search ranking, accessibility compliance, or production readiness.

Use the [production acceptance checklist](production-migration.md#acceptance). In particular, reconcile the in-scope inventory, test integrations, and verify that authors can edit, save, reopen, and preview content in the selected authoring environment.

## Limitations {#limitations}

Review the [product boundaries](overview.md#limitations) separately from the engagement scope. Integrations, custom business logic, analytics, commerce, search, source-system inheritance, and regulated requirements need an explicit inclusion/exclusion decision and owner. Automated page import does not recreate them by itself.

Before handoff, record unresolved work, accepted exceptions, code/content destinations, validation results, recovery steps, and support ownership in the [project handover](project-documentation.md#portable-handoff). Code rollback and content/asset recovery are separate operations.
