---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: a2d56721-502c-4f4e-9b72-5ca790df75c5
mini-toc-levels: 1
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions; for example, for those in 2020, 2021, and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] current feature release (2023.1.0) is February 9, 2023. The next feature release (2023.2.0) is planned for February 23, 2023.

## Release Video {#release-video}

Have a look at the January 2023 Release Overview video for a summary of the features added in the 2023.1.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3413479/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Sites] prerelease {#prerelease-features-sites}

* The AEM GraphQL content delivery API now supports GraphQL [Paging](/help/headless/graphql-api/content-fragments.md#paging) and [Sorting](/help/headless/graphql-api/content-fragments.md#sorting), to make fetching and rendering large content sets more efficient. GraphQL pagination allows to improve query response time by returning results in sub-sets as opposed to all at once. GraphQL sorting allows putting content sets in a desired order, making it easier for a client appliation to process the content.  Query response time is further improved with Hybrid Filtering in the AEM GraphQL engine. Content is now read from JCR in smaller sets that correspond with query filters. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* Assets Reports now includes the ability for Administrators to [generate assets download reports](/help/assets/asset-reports.md) from the Experience Manager Assets as a Cloud Service deployment. This data further empowers Admins to derive insights from key success metrics in order to measure the adoption of Assets within your enterprise and by customers.

   ![PDF rendition for other formats](/help/release-notes/assets/choose_report.png)

* Experience Manager Assets now [supports SAS Token](/help/assets/add-assets.md#asset-bulk-ingestor) in addition to the Access Key for authentication while connecting to Azure Blob Storage data source for ingesting assets using the Bulk Import tool.

* Improved management of CMYK images in Asset Compute, enabling you to generate Smart Crop and Smart Tags for CMYK images.

### New features in [!DNL Assets] prerelease {#prerelease-features-assets}

* Experience Manager Assets now supports [large-scale ingestion of assets from Google Cloud Platform](/help/assets/add-assets.md#asset-bulk-ingestor) using the Bulk Import tool.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] {#new-features-available-in-channel}

* **Data capture core components to build Adaptive Forms**: Use Adaptive Forms editor to create forms based on standardized data capture components (Core Components). These components provide customization capabilities, reduced development time, and lower maintenance costs for your digital enrolment experiences.
* **Frontend pipeline support for styling core component based Adaptive Forms**: Utilize easily customizable BEM-based themes for Core Components-based Adaptive Forms by deploying them with Frontend Deployment pipeline to enhance the look and feel of your forms.
* **Submit Adaptive Forms to Microsoft SharePoint and Microsoft OneDrive**: Streamline data submission with the ability to directly send Adaptive Form data to both Microsoft SharePoint and Microsoft OneDrive. You can submit both schema-based and schema-less data. These submit actions are in addition to already available submit actions. 
* **Efficient form-building with the Save an Adaptive Form as a template feature**: Streamline your form-building process by saving an Adaptive Form as a template and reusing the templates for your next Adaptive Form. 
* **Workflow steps to generate non-interactive PDF documents and printable output**: Automate the creation of non-interactive PDF documents and printable output for your business processes with AEM Workflow steps, streamlining your document generation process and saving time.
* **Quicky deploy forms with Rapid Development environment**: Use Rapid Development environment to swiftly develop and deploy forms. This minimizes the amount of time needed for testing, as features are already proven to work in a local development environment. The result is a streamlined and efficient development process that saves time and resources.

## [!DNL Experience Manager as a Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* Rapid Development Environments - Increase your team's development productivity through quicker cloud validation and debugging sessions! RDE is a new type of Cloud Environment intended for swiftly validating that code working locally also behaves as expected in the Cloud. Using Command Line Tools, developers quickly synchronize content packages, bundles, content files, OSGI configuration, or dispatcher configuration to the RDE. After successfully validating code in the RDE, customers are encouraged to deploy to a Cloud Dev Environment to exercise the Cloud Manager quality gates, before deploying via production pipeline to stage and production environments. Each program includes one RDE and optionally, more can be licensed. This feature will be gradually rolled out over the next few weeks; you can send an email to aemcs-rdesupport@adobe.com to skip to the front of the line!

* [Extended support for server-side API access tokens](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md) – You can now generate multiple credentials, which is useful for scenarios where APIs have different characteristics. It is also now possible to revoke credentials in a self-service manner.

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes-cloud-manager/release-notes-cm-current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
