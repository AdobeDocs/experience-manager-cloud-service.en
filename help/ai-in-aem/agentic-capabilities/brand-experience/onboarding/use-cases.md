---
title: Onboarding Agentic Capabilities Overview
description: Learn how the Onboarding Agentic Capabilities in AEM help you configure Adobe Experience Manager Assets using natural language, coordinating the full onboarding lifecycle, from environment provisioning through content structure, metadata, migration, and search.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Onboarding Agentic Capabilities {#development-agentic-capabilities}

The Onboarding Agentic Capability of Adobe Experience Manager (AEM) as a Cloud Service collaborates with [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview) to help you configure Adobe Experience Manager Assets using natural language, coordinating the full onboarding lifecycle, from environment provisioning through content structure, metadata, migration, and search.

The Onboarding Agentic Capability brings onboarding guidance and execution into a single experience, helping teams move from their requirements to a configured DAM in a structured and controlled manner. It recommends appropriate approaches based on the user's context and requires confirmation before making changes, allowing teams to establish their AEM Assets foundation with greater consistency and confidence.

Some of the key benefits include:

- **Conversational onboarding**: Set up and configure AEM Assets using natural language, without navigating complex configuration workflows.
- **Faster time-to-value**: Accelerate onboarding through guided planning and automated execution of setup tasks.
- **Unified onboarding experience**: Coordinate onboarding activities across AEM applications and workflows from a single conversational interface.
- **Built-in best practices**: Get recommendations that help establish consistent, scalable, and well-structured DAM foundations.
- **Controlled execution**: Review and confirm changes before write operations are performed..

## Skills {#skills-aem-onboarding-agentic-capability}

The AEM Onboarding Agentic Capability provides the following skills:

* **End-to-end onboarding**: Orchestrates the overall AEM onboarding journey and routes requests to the appropriate skills for environment setup, access, content architecture, metadata, migration, and search configuration.

* **Environment and access setup**: Provisions AEM Cloud Service environments and configures user access through Adobe Cloud Manager and Adobe Admin Console, including programs, environments, user groups, and product profiles.

* **Content architecture**: Designs and creates folder hierarchies under `/content/dam` and controlled tag taxonomies under `/content/cq:tags`, including support for CSV-based definitions and batch operations.

* **Metadata management**: Provides guidance on metadata architecture and creates and assigns custom metadata forms. The metadata advisory capability is read-only and helps define fields, namespaces, asset-type structures, and migration approaches.

* **Asset and metadata migration**: Runs and monitors existing bulk asset import jobs and supports bulk metadata imports for existing assets from CSV files.

* **Search configuration**: Makes custom `dam:Asset` properties searchable and configures indexed properties as filters in the AEM Assets search interface.

These skills provide a unified onboarding experience while allowing users to work at the level of the business task rather than needing to know the underlying AEM configuration or implementation details.


## How to Access {#access}

You can access the AEM Onboarding Agentic Capability via the [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview).

## Common use cases and sample prompts {#common-use-cases-sample-prompts}

### Getting started

| Use Case | Description | Skills | Application | Sample Prompts |
|---|---|---|---|---|
| Guided end-to-end onboarding | Orchestrates the full onboarding lifecycle and delegates to the folder, tag, metadata, import, and search skills for users who do not yet know which task they need. | `aem-assets-onboarding-workflow` | AEM Assets | "Onboard our team to AEM Assets"<br>"Walk me through AEM DAM onboarding" |

### Environment & access

| Use Case | Description | Skills | Application | Sample Prompts |
|---|---|---|---|---|
| Provision AEM environments | Sets up the Cloud Manager resources for a new AEM Cloud Service instance, including tenant discovery, program creation or reuse, and Stage and Production environments as a sequential, progress-tracked workflow. | `aem-assets-environment-provisioning` | Adobe Cloud Manager | "Set up a new AEM Cloud Service program"<br>"Provision Stage and Production environments" |
| Provision users & access | Adds users to the Adobe Admin Console organization, creates user groups, and attaches product profiles to groups. | `aem-assets-user-provisioning` | Adobe Admin Console | "Add these users to the org and give them AEM access"<br>"Create a user group and assign product profiles"<br>"Provision users from this CSV" |

### Content architecture

| Use Case | Description | Skills | Application | Sample Prompts |
|---|---|---|---|---|
| Design & create folder hierarchies | Recommends and creates folder structures under `/content/dam`, including building a hierarchy from a CSV definition. | `aem-assets-folder-onboarding` | AEM Assets | "Recommend a folder hierarchy for our brand assets"<br>"Build a folder structure under /content/dam from this CSV" |
| Design & create tag taxonomies | Designs and creates controlled tag vocabularies under `/content/cq:tags`, including namespaces, hierarchical tags, and batch tag operations. | `aem-assets-tag-onboarding` | AEM Assets | "Design a tag taxonomy with namespaces for our product categories"<br>"Create these hierarchical tags in AEM" |

### Metadata

| Use Case | Description | Skills | Application | Sample Prompts |
|---|---|---|---|---|
| Metadata schema advisory | Provides read-only expert guidance on metadata architecture, including fields to capture, namespace conventions, organization by asset type, and migration from an existing DAM. Makes no changes in AEM. | `aem-assets-metadata-advisory` | AEM Assets (advisory) | "What metadata should I capture for campaign assets?"<br>"Which namespace should I use for these fields?"<br>"Advise on migrating metadata from our old DAM" |
| Create & assign metadata forms | Designs and creates custom metadata forms—the authoring UI content authors use—from a CSV, table, requirements document, or description, then optionally assigns them to folders. | `aem-assets-metadata-form-onboarding` | AEM Assets | "Create a metadata form from this list of fields"<br>"Assign this form to the campaigns folder" |

### Asset & metadata migration

| Use Case | Description | Skills | Application | Sample Prompts |
|---|---|---|---|---|
| Run & monitor bulk asset import | Manages existing bulk import jobs—list, run, schedule, stop, dry-run, and monitor progress. Creating new import configurations is done in the AEM Assets UI. | `aem-assets-bulk-import` | AEM Assets | "Run my bulk import job"<br>"Do a dry run first, then check import progress"<br>"Show me my bulk import configurations" |
| Bulk metadata import from CSV | Populates metadata for existing assets in bulk from a CSV file and monitors the import job status. | `aem-assets-metadata-import` | AEM Assets | "Import metadata from this CSV for existing assets"<br>"Check the status of my metadata import" |

### Search configuration

| Use Case | Description | Skills | Application | Sample Prompts |
|---|---|---|---|---|
| Index custom properties for search | Adds custom `dam:Asset` properties to the search index using a simplified configuration approach, deployed through Adobe Cloud Manager Git change and pipeline. | `aem-assets-search-indexing` | AEM Assets + Cloud Manager | "Make this custom property searchable"<br>"My custom field isn't showing in search — add it to the index" |
| Add search filters to the UI | Adds indexed properties as filter fields in the AEM Assets search panel for files, folders, or collections. Requires the property to be indexed first. | `aem-assets-search-filter-onboarding` | AEM Assets | "Add this field as a filter in the search panel"<br>"Customize the AEM Assets search form" |

<!--

## Metadata form field type reference

| Element Type | Description | Example Properties |
|---|---|---|
| `text` | Single-line text input | `dc:title`, `dc:creator` |
| `dropdown` | Select from predefined options | `dam:assetStatus`, `dc:language` |
| `datepicker` | Date/time picker | `xmp:CreateDate`, `photoshop:DateCreated` |
| `number` | Numeric input | `xmp:Rating` |
| `tag_picker` | Tag selection widget linked to AEM taxonomy | `cq:tags`, `xcm:keywords` |
| `smart_tags` | AI-generated tags — read-only | `xcm:machineKeywords` |
| `multi_val` | Multiple free-form values | `dc:subject`, `dc:contributor` |

-->

