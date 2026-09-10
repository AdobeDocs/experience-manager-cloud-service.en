---
title: AI-powered content onboarding and content supply chain automation
description: Learn how the Content Supply Chain Agent helps blueprint your content lifecycle and configure governed content and metadata movement between Adobe and third-party systems.
role: Admin
hide: true
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
---

# AI-powered content onboarding and content supply chain automation {#ai-powered-content-onboarding-content-supply-chain-automation}

Organizations often store digital assets and metadata across multiple repositories, such as digital asset management (DAM) systems, cloud storage services, and content platforms. Migrating content to a new system or keeping multiple repositories synchronized typically requires manual effort or custom integrations that can be difficult to build and maintain.

The Content Supply Chain Agent provides two cooperating AI-powered agents:

- **CSC Blueprint Agent** maps your end-to-end content supply chain, identifies gaps and anti-patterns, and helps define an agreed future state and prioritized action plan.
- **CSC Integration Agent** implements governed content and metadata movement between systems through configured connections, supporting both one-time migrations and recurring synchronization.

Together, the agents help you plan improvements across the content lifecycle and implement transfers between Adobe and third-party systems.

For information on how to get it enabled for your deployment, see [Assets as a Cloud Service release notes](/help/release-notes/release-notes-cloud/release-notes-current.md#ai-powered-content-onboarding-content-supply-chain-automation).

## Benefits {#benefits-ai-powered-content-onboarding-content-supply-chain-automation}

The Content Supply Chain Agent provides the following benefits:

- Establish a shared view of your current and future content supply chain.
- Accelerate onboarding by reducing the time required to migrate existing assets and metadata into a new repository.
- Simplify recurring synchronization by automating scheduled content transfers between systems of record.
- Reduce maintenance overhead by replacing custom integrations with configurable connections.
- Support governed content and metadata movement between Adobe and third-party systems.
- Validate transfer settings before moving content by using dry runs.

## Blueprint your content supply chain {#blueprint-content-supply-chain}

Use the CSC Blueprint Agent when you need to understand and improve the complete content lifecycle rather than configure a single transfer. It maps your systems, processes, and handoffs across the six phases of the content supply chain, then produces confirmed current-state and future-state diagrams and a prioritized action plan.

The Blueprint Agent may recommend Adobe product capabilities, native integrations, CSC Integration Agent connections, or customer-owned implementation work. Its recommendations are not limited to systems with an available gateway.

Where the agreed action plan includes governed content or metadata movement, the Blueprint Agent can move approved connection work into CSC Integration Agent setup.

## Configure content transfers with the CSC Integration Agent {#how-content-transfer-work}

The AI-powered agent helps configure governed content and metadata movement between source and destination systems or endpoints.

During configuration, the agent:

- Collects the information required to connect to each system or endpoint.
- Proposes mappings between metadata fields, including taxonomy or classification fields exposed by a gateway.
- Allows you to review and validate the proposed mappings before transferring content.
- Supports dry runs so you can verify the configuration before moving production content.
- Configures one-time or recurring transfer schedules.

Each configured transfer is called a **connection**. A connection uses **gateways** to communicate with source and destination systems or endpoints. Each execution of a connection is called a **run**.

Successful non-dry runs preserve identity and change-detection state. Later runs use this state to reduce unnecessary destination updates while processing additions, modifications, and eligible deletions. Source enumeration and content retransmission depend on gateway capabilities and destination requirements.

## Key Integration Agent capabilities {#key-capabilities-ai-powered-content-onboarding-content-supply-chain-automation}

- **Identity mapping**: Maintains the relationship between assets in source and destination systems across multiple runs.

- **Change detection**: Uses persisted state to reduce unnecessary destination updates while processing additions, modifications, and eligible deletions.

- **Metadata mapping**: Maps metadata fields, including taxonomy or classification fields exposed by a gateway, between source and destination systems.

- **Dry runs**: Validates mappings and transfer settings before moving content into the destination repository.

- **Scheduled synchronization**: Runs transfers on a recurring schedule, such as hourly, daily, or weekly.

- **Custom transformations**: Supports additional transformation logic when required, including JavaScript, regular expressions, webhooks, and content hashing.

## Available gateways {#supported-repositories}

Content and metadata can be transferred between Adobe and third-party systems through source and destination gateways.

**Gateways ready now for co-innovation or Limited Availability:** AEM Assets as a Cloud Service, AEM Assets (Managed Services / On-Prem 6.5), Adobe Commerce, Adobe Content Platform, Document Cloud, Adobe Dynamic Media Classic, Adobe Lightroom, Adobe Stock, Adobe Workfront, [!DNL AWS S3], [!DNL Azure Blob Storage], [!DNL Box], [!DNL Dropbox], [!DNL Drupal], FTP (Classic), [!DNL Google Drive], HTTP Basic (Apache Directory Index) Source, [!DNL OneDrive] and [!DNL SharePoint], OpTEL Media Source, SFTP / SSH File Server, SMB / Samba / CIFS File Share, [!DNL Synology] NAS (File Station), TFTP (UDP), Web Crawl Media Source, WebDAV File Server, [!DNL WordPress].

**Gateways in development:** CSV Gateway, [!DNL Google Cloud Storage], [!DNL LucidLink], [!DNL VNTANA], [!DNL Cloudinary], [!DNL Nasuni], Adobe Marketo Engage, [!DNL Syndigo], [!DNL Aprimo] DAM, [!DNL Veeva Vault], [!DNL WebDAM], [!DNL Bynder], [!DNL Figma], Frame.io (V4 API), Frame.io (V2/V3 API), [!DNL Canva], [!DNL Iconik], [!DNL Acquia] DAM, [!DNL OpenText] Media Management, [!DNL Canto], [!DNL Frontify], [!DNL Brandfolder], [!DNL Orange Logic] DAM, [!DNL MediaValet], [!DNL inriver] PIM, [!DNL FADEL] Rights Cloud, [!DNL Overcast HQ], [!DNL NetX], [!DNL ImageBank X], [!DNL ImageKit], [!DNL Hyland Nuxeo], [!DNL Sitecore] Content Hub, [!DNL Fotoware], [!DNL Wedia], [!DNL CELUM], [!DNL ResourceSpace], [!DNL PastView], [!DNL Smint.io], [!DNL Storyteq], [!DNL PhotoShelter], [!DNL Air], [!DNL Sharedien], [!DNL Blue Lucy] (formerly [!DNL BLAM]), [!DNL Terentia], [!DNL FileSpin], [!DNL Tenovos], [!DNL WoodWing] Assets, [!DNL Pimberly].

> **Trademark notice:** All third-party trademarks are the property of their respective owners. Their inclusion does not imply affiliation with or endorsement by Adobe.

## Example use cases {#example-use-cases}

### Plan and improve an end-to-end content supply chain

Map the systems, processes, and handoffs used throughout the content lifecycle, identify improvement opportunities, and prioritize integrations before configuring individual connections.

### Migrate content into a new repository

Configure a one-time migration from a legacy DAM or cloud storage repository into a new system of record. Review metadata mappings with a dry run before transferring production content.

### Synchronize repositories

Keep content synchronized between cloud storage and a DAM with a recurring transfer that processes additions, modifications, and eligible deletions while reducing unnecessary destination updates.

### Streamline your content supply chain

Reduce manual content movement by automating transfers between repositories used throughout your organization's content lifecycle.

## When to use this capability {#when-to-use-ai-powered-content-onboarding-content-supply-chain-automation}

This capability is well suited for:

- Mapping the current and future state of an end-to-end content supply chain.
- Identifying gaps, anti-patterns, and opportunities for improvement.
- Producing a prioritized implementation action plan.
- One-time content migrations.
- Onboarding new systems of record.
- Recurring synchronization between repositories.
- Metadata mapping, including supported taxonomy or classification fields.
- Automating content movement across multiple systems.

## When not to use this capability {#when-not-to-use-ai-powered-content-onboarding-content-supply-chain-automation}

This capability is not intended for:

- General workflow or business process automation.
- Analytics or customer data ETL pipelines.
- Real-time event-driven propagation.
- Continuous byte-streaming between repositories.
