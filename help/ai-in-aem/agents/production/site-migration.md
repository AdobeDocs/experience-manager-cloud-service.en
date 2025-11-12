---
title: Site Migration Skill
description: Learn how the Production Agent’s Site Migration skill onboards existing sites and designs into Edge Delivery Services.
feature: Edge Delivery Services
role: Admin, Architect, Developer
---

# Site Migration Skill {#site-migration}

Use the Site Migration skill to onboard websites into Edge Delivery Services (EDS) with the help of AI and Adobe Forward Deployed Engineers (FDEs). The skill automates content and style migration and prepares an author-ready EDS implementation that you can evolve in code and through AEM authoring.

## Overview {#overview}

The Site Migration skill transforms an existing site or design into an Edge Delivery Services project:

* **Sources**: an existing website (AEM 6.5/AMS/Cloud Service or another CMS), a design system, or mocks such as **Figma**.
* **Outputs**: an EDS repository with blocks and styles applied, migrated content, and an authoring setup that supports **document-based authoring** and **visual authoring with the Universal Editor**.
* **Operating model**: delivered by Adobe **Forward Deployed Engineers** (FDEs) who operate the agent and guide the migration to ensure quality and governance.

> NOTE  
> While the agent automates the heavy lifting, your developers retain full control of the repository and deployments through normal code review and approval workflows.

## What the skill does {#capabilities}

The Site Migration skill performs the following high-level tasks:

1. **Discovery and scoping**  
   Analyze the source website or design, inventory pages and assets, and confirm the target EDS block library and governance rules.

2. **Project bootstrap**  
   Create or update the EDS project, repositories, environments, and CI/CD configuration required for authoring and preview.

3. **Content migration**  
   Convert pages and assets into EDS-friendly content using default EDS structures and **blocks** aligned to your selected block library. Content is imported and organized to match agreed information architecture.

4. **Style application**  
   Apply styles in one of the following ways:
   * **As-is style migration** from the current site.
   * **Redesign** using provided mocks (for example, Figma).
   * **Adopt existing EDS block designs** from your design system.
   * **Block consolidation** to reduce the number of blocks/variants while preserving required layouts.

5. **Authoring enablement**  
   Configure **document-based authoring** and **visual authoring with the Universal Editor**, so authors can edit content using the method that fits each workspace.

6. **Quality and compliance checks**  
   Validate accessibility, performance targets, and guardrails defined for your project; open pull requests for review; iterate until acceptance.

7. **Handover**  
   Deliver documentation, PR history, and next-step guidance so your teams can maintain and extend the implementation.

## Supported sources and targets {#sources-targets}

* **Sources**  
  * AEM (6.5, AMS, or Cloud Service) sites  
  * Non-AEM CMS sites  
  * Static sites  
  * Design mocks (for example, Figma)  
* **Target**  
  * An **Edge Delivery Services** implementation ready for ongoing authoring and development.

> TIP  
> If you are new to EDS or the Universal Editor, review the AEM documentation on authoring methods and the Universal Editor before you begin.

## Authoring options after migration {#authoring}

The migrated site is configured for:

* **Document-based authoring** for fast editing of content and blocks.  
* **Visual authoring with the Universal Editor** for in-context changes to content and components.

You can use one or both approaches per project or per section, depending on team preferences.

## What’s not included (current limitations) {#limitations}

The Site Migration skill focuses on content and style. The following are **out of scope** and require additional implementation:

* Custom **integrations** (for example, commerce, CRM, search connectors).  
* **Dynamically rendered client applications** (for example, complex single-page apps or bespoke JavaScript frameworks) beyond standard EDS patterns.  
* Net-new feature development unrelated to the migrated experience.

If you require these capabilities, Adobe Consulting Services (ACS) or your implementation partner can extend the delivered EDS project.

## Roles and responsibilities {#roles}

* **Adobe Forward Deployed Engineers (FDEs)** operate the agent, manage the migration plan, and ensure quality.  
* **Your developers** review pull requests, own the repository long term, and implement optional integrations.  
* **Your authors** validate migrated content and styles and adopt the chosen authoring method(s).  
* **Stakeholders** approve scopes, timelines, and acceptance criteria.

## Prerequisites {#prerequisites}

* An AEM as a Cloud Service organization with EDS enabled (or planned).  
* Access and legal rights to migrate the source site or design assets.  
* A designated code repository and environments for preview and testing.  
* Named contacts for development, authoring, and governance sign-off.

## Engagement model and availability {#engagement}

The Site Migration skill is currently available **through an FDE-operated engagement**. Each project begins with a scoping exercise based on source complexity, design goals, and governance requirements. To explore a migration:

* **Contact your Adobe representative** or account team to initiate scoping and scheduling.  
* Adobe will confirm eligibility, estimate the engagement, and propose a migration plan.

## Deliverables {#deliverables}

Typical deliverables include:

* EDS repository (blocks, styles, configuration) and CI/CD setup  
* Migrated content and assets (prioritized by scope)  
* Authoring configuration (document-based and/or Universal Editor)  
* PRs documenting changes and review history  
* Handover notes and recommended next steps

## Best practices and guidance {#best-practices}

* **Decide your block strategy early**: consolidate where possible to reduce maintenance.  
* **Use design tokens** when applying styles to support brand evolution.  
* **Keep authors in the loop**: validate early page exemplars before bulk migration.  
* **Plan integrations separately** to avoid blocking content onboarding.  
* **Adopt governance**: use branch protections and PR reviews to keep quality high.

## Related documentation {#related}

* [AEM Sites and Edge Delivery Services](/en/docs/experience-manager-cloud-service/content/sites/sites-and-edge)  
* [Methods to Author Content in AEM](/en/docs/experience-manager-cloud-service/content/sites/authoring/authoring-methods)  
* [Universal Editor Introduction](/en/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/introduction)
