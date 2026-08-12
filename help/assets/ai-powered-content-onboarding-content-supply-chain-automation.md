---
title: AI-powered content onboarding and content supply chain automation
description: Learn how to automate one-time content migrations and content supply chain automation between Adobe and supported third-party repositories.
role: Admin
hide: true
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
---

# AI-powered content onboarding and content supply chain automation {#ai-powered-content-onboarding-content-supply-chain-automation}

Organizations often store digital assets and metadata across multiple repositories, such as digital asset management (DAM) systems, cloud storage services, and content platforms. Migrating content to a new system or keeping multiple repositories synchronized typically requires manual effort or custom integrations that can be difficult to build and maintain.

This capability helps you automate one-time content migrations and recurring synchronization between supported repositories. An AI-powered agent guides you through configuring content transfers by proposing repository connections, metadata mappings, and transfer settings, reducing the effort required to move and synchronize content across systems.

For information on how to get it enabled for your deployment, see [Assets as a Cloud Service release notes](/help/release-notes/release-notes-cloud/release-notes-current.md#ai-powered-content-onboarding-content-supply-chain-automation).

## Benefits {#benefits-ai-powered-content-onboarding-content-supply-chain-automation}

Automating content onboarding and synchronization provides the following benefits:

- Accelerate onboarding by reducing the time required to migrate existing assets and metadata into a new repository.
- Simplify recurring synchronization by automating scheduled content transfers between systems of record.
- Reduce maintenance overhead by replacing custom integrations with configurable connections.
- Support content transfers between Adobe and third-party repositories.
- Validate transfer settings before moving content by using dry runs.

## How content transfers work? {#how-content-transfer-work}

The AI-powered agent helps configure a content transfer between a source repository and a destination repository.

During configuration, the agent:

- Collects the information required to connect to each repository.
- Proposes mappings between metadata fields and taxonomies.
- Allows you to review and validate the proposed mappings before transferring content.
- Supports dry runs so you can verify the configuration before moving production content.
- Configures one-time or recurring transfer schedules.

Each configured transfer is called a **connection**. A connection uses **gateways** to communicate with the source and destination repositories. Each execution of a connection is called a **run**.

Runs are stateful. They track previously transferred assets and metadata so that subsequent runs transfer only new or modified content instead of processing the entire repository again.

## Key capabilities {#key-capabilities-ai-powered-content-onboarding-content-supply-chain-automation}

- **Identity mapping**: Maintains the relationship between assets in the source and destination repositories across multiple runs.

- **Change detection**: Transfers only assets and metadata that have changed since the previous run, reducing unnecessary processing and improving efficiency.

- **Metadata mapping**: Maps metadata fields and taxonomies between repositories as part of the content transfer process.

- **Dry runs**: Validates mappings and transfer settings before moving content into the destination repository.

- **Scheduled synchronization**: Runs transfers on a recurring schedule, such as hourly, daily, or weekly.

- **Custom transformations**: Supports additional transformation logic when required, including JavaScript, regular expressions, webhooks, and content hashing.

## Supported repositories {#supported-repositories}

Content can be transferred between Adobe and third-party repositories through supported source and destination gateways.

Examples of supported repositories include:

- Adobe Experience Manager Assets
- Adobe Content Platform
- Adobe Commerce
- Amazon S3
- Azure Blob Storage
- Box
- Dropbox
- Google Drive
- OneDrive
- WordPress
- Workfront
- FTP and SFTP servers
- SMB file shares

Additional repositories are planned for future releases.

## Example use cases {#example-use-cases}

### Migrate content into a new repository

Configure a one-time migration from a legacy DAM or cloud storage repository into a new system of record. Review metadata mappings with a dry run before transferring production content.

### Synchronize repositories

Keep content synchronized between cloud storage and a DAM by configuring a recurring transfer that processes only newly added or modified assets.

### Streamline your content supply chain

Reduce manual content movement by automating transfers between repositories used throughout your organization's content lifecycle.

## When to use this capability {#when-to-use-ai-powered-content-onboarding-content-supply-chain-automation}

This capability is well suited for:

- One-time content migrations.
- Onboarding new systems of record.
- Recurring synchronization between repositories.
- Metadata and taxonomy mapping during content transfers.
- Automating content movement across multiple repositories.

## When not to use this capability {#when-not-to-use-ai-powered-content-onboarding-content-supply-chain-automation}

This capability is not intended for:

- General workflow or business process automation.
- Analytics or customer data ETL pipelines.
- Real-time event-driven propagation.
- Continuous byte-streaming between repositories.




