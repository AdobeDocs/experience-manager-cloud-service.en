---
title: AOE Delivery of the Experience Modernization Agent
description: Have Adobe engineers migrate your site with the Experience Modernization Agent, and learn what to agree before an engagement starts.
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

Adobe's Agentic Outcome Engineers (AOEs) can migrate your site for you with the Experience Modernization Agent. AOE delivery is an optional engagement, not a separate tier of the agent: the same agent, operated by Adobe engineers who add engineering work and review to its automation.

## The Agentic Outcome Engineer (AOE) {#aoe}

The AOE team works with you to:

* Take the agent's output to a site that is ready for production.
* Resolve migration and implementation issues within the agreed engagement.
* Transfer project knowledge to the team that will maintain the site.

## AOE-Led Delivery {#aoe-led}

Agree scope, responsibilities, how the result is signed off, and support with your Adobe account team before work begins. Access to the console doesn't include an AOE engagement, a delivery guarantee, or a price.

## Engagement Process {#engagement-process}

### 1. Scoping {#scoping}

Contact your Adobe account team with your migration requirements and scope. The AOE team reviews eligibility and proposes an approach, estimate, and schedule.

* **Inputs:** Authorized source URLs, CMS platform, content inventory, design references, timeline, where content will be stored, integrations, access constraints, and how you'll sign off the result
* **Outputs:** Eligibility confirmation, effort estimate, migration approach, engagement structure

### 2. Planning {#planning}

A kickoff meeting is held, along with a source site analysis, content audit, design alignment, component library review, and authoring tool selection.

* **You** provide all necessary assets and guidelines.
* **Adobe** proposes the migration plan, timeline, roles, and checkpoints for agreement.
* **Together**, confirm where code and content go, who approves releases, exceptions, and how to recover from a mistake.

### 3. Execution {#execution}

* **AOE activities:** Operate the Experience Modernization Console, review AI outputs, apply brand guidelines, refine as needed
* **Your activities:** Review deliverables, check content and designs, test authoring

Checkpoints for component mapping, design review, the authoring workflow, and pre-launch checks keep the content accurate.

### 4. Handoff {#handoff}

* **Deliverables:** Agreed website code, migrated content, documentation, check reports, and a record of what was signed off and what remains open
* **Activities:** Knowledge transfer, authoring training, developer onboarding

### 5. Post-Migration {#post-migration}

Confirm who owns ongoing content, code, integrations, and operations. Follow the support arrangements agreed for the engagement and your Adobe support entitlement; do not assume ongoing AOE implementation work is included after handoff.

## AOE Delivery Scope {#scope}

The engagement defines which automated and manual work is included. The sections below describe the areas to agree.

### Source Platforms {#source-platforms}

Sources can include WordPress, Drupal, Sitecore, existing Adobe Experience Manager sites, SharePoint, or custom sites where authorized content can be extracted. The standard source scope described for this service is publicly accessible static HTML. Have the AOE team explicitly assess protected, interaction-dependent, or private-network sources rather than assume they are included.

This is the scope of the service, not a limit of the product or of Edge Delivery Services. The agent itself reads pages as a browser renders them, including content that scripts insert, and reads pages behind supported sign-in methods. See [Limitations](overview.md#limitations). Agree source access and extraction for the actual engagement.

### Included in AOE Scope {#included}

#### Target Platform {#target-platform}

* **Platform:** Every migration goes to Edge Delivery Services.
* **Where content is stored:** Agree [where content is stored and how authors edit it](overview.md#content-storage), and confirm the setup and handover for the option you choose.

#### Migration Work Performed {#migration-work}

* **Migration approach:** Agree faithful migration, redesign, or an incremental phased migration.
* **Content import:** Automated extraction of page content from source websites and automated mapping to [default content and blocks](production-migration.md#content-structure)
* **Design system:** Extraction of brand tokens (colors, typography, spacing) and application to the new site
* **Design references:** The agent imports designs from the source site and from Figma, and works from attached screenshots and documents otherwise. Agree which references apply and how close to them the result must be.
* **Responsive design:** Layouts for mobile and desktop widths in the project's CSS

#### Resulting System {#resulting-system}

The resulting site runs on Edge Delivery Services. A new project from the AEM boilerplate scores 100 in Lighthouse; what a project adds, such as third-party scripts, large images, or heavy block code, can lower that score. Accessibility and search results depend on the content and code. Agree and measure the required performance, accessibility, SEO, functional, and authoring outcomes on real pages of each template.

Use the checklist in [Check and Sign Off](production-migration.md#acceptance). In particular, reconcile the in-scope inventory, test integrations, and verify that authors can edit, save, reopen, and preview content in their editor.

## Limitations {#limitations}

Review the [product boundaries](overview.md#limitations) separately from the engagement scope. Integrations, custom business logic, analytics, commerce, search, source-system inheritance, and regulated requirements each need a decision on whether they're included, and an owner. They run on the source's servers or in its scripts, which page import doesn't carry over.

Before handoff, record unresolved work, accepted exceptions, where code and content went, check results, recovery steps, and support ownership in the [project handover](project-documentation.md#portable-handoff).
