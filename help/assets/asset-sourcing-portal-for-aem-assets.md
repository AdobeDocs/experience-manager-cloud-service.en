---
title: Asset Sourcing portal for AEM Assets
description: Learn how to create  Assets Sourcing Portal that provides a secure, self-service experience for collecting assets from external contributors without granting them access to Adobe Experience Manager Assets.
role: Admin
hide: true
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
---

# Asset Sourcing portal for AEM Assets {#asset-sourcing-portal-aem-assets}

Organizations often rely on photographers, creative agencies, and other external contributors to provide digital assets. Collecting these assets through email, shared drives, or file-sharing services can lead to inconsistent metadata, manual processing, and additional administrative effort. Providing external contributors with direct access to a digital asset management (DAM) system may also require additional licenses and expose internal content.

The Assets Sourcing Portal provides a secure, self-service experience for collecting assets from external contributors without granting them access to Adobe Experience Manager Assets. Contributors can upload assets, provide the required metadata, and submit content directly to a designated intake location while administrators maintain control over asset organization and governance.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

## Benefits {#benefits-asset-sourcing-aem-assets}

Using the Assets Sourcing Portal provides the following benefits:

- Allow external contributors to upload assets without requiring an AEM Assets license.
- Simplify asset intake through a dedicated upload experience.
- Reduce manual processing by automatically applying metadata and ingestion policies.
- Improve governance by controlling where uploaded assets are stored and what metadata contributors provide.
- Scale onboarding for multiple contributors without creating custom upload solutions.

## How asset sourcing works? {#how-asset-sourcing-works-in-aem-assets}

An administrator configures a sourcing portal for an external contributor by defining:

- The destination intake location for uploaded assets.
- The metadata fields contributors must complete.
- Optional ingestion policies, such as naming conventions and notifications.

Contributors receive a dedicated upload experience where they can:

- Upload one or more assets.
- Complete the required metadata fields.
- Submit assets for ingestion into Adobe Experience Manager Assets.

During ingestion, uploaded assets are processed according to the configured policies before they are stored in the designated intake location.

## Upload methods {#upload-methods-asset-sourcing-aem-assets}

The Assets Sourcing Portal supports multiple upload methods so contributors can work within their preferred workflows.

- **Browser portal:** Provides a web-based upload experience where contributors can drag and drop files and complete the required metadata before submitting assets.

- **REST API:** Allows organizations to integrate asset uploads into existing production systems or automated workflows.

- **Vendor MCP:** Enables contributors working in AI-assisted environments to upload assets through supported conversational workflows.

All upload methods provide the same core asset ingestion capabilities.

## Key capabilities {#key-capabilities-asset-sourcing-aem-assets}

- **Secure contributor access:** External contributors can upload assets without accessing the DAM, browsing repositories, or viewing other assets.

- **Configurable metadata collection:** Administrators select metadata fields from the AEM Assets metadata schema. The portal automatically generates the contributor's submission form based on the selected fields.

- **Automated asset ingestion:** Uploaded assets are routed to a designated intake location with configured metadata applied during ingestion.

- **Configurable ingestion policies:** Administrators can define ingestion rules for each contributor, including required and optional metadata fields, prepopulated values, batch identifiers, asset naming conventions, destination paths, minimum asset dimensions, and administrator notifications.

- **Scalable contributor onboarding:** Configure multiple contributors with different upload destinations, metadata requirements, and ingestion policies without developing custom upload applications.

## Example use cases {#example-use-cases-asset-sourcing}

- **Collect assets from creative agencies:** Allow agencies to submit campaign assets through a dedicated upload portal without granting access to the organization's DAM.

- **Receive photography submissions:** Provide photographers with a simple upload experience that automatically captures required metadata and stores assets in the appropriate intake location.

- **Integrate external production systems:** Use the REST API to automatically submit assets from third-party production or content creation systems.

## When to use this capability {#when-to-use-this-capability}

Use the Assets Sourcing Portal when you need to:

- Collect assets from photographers, agencies, and external vendors.
- Standardize metadata collection during asset intake.
- Secure asset submissions without providing DAM access.
- Automate asset ingestion into designated intake locations.
- Support large numbers of external contributors.

## When not to use this capability {#when-not-to-use-this-capability}

The Assets Sourcing Portal is not intended for:

- Managing assets within the DAM after ingestion.
- Providing contributors with access to browse, search, or download DAM assets.
- Internal collaboration workflows that require full DAM functionality.