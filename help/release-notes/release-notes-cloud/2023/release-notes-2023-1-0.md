---
title: Release Notes for 2023.1.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Release Notes for 2023.1.0 release of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: f134fdbc-224b-404c-b20f-44cae8bad681
feature: Release Information
role: Admin
---
# 2023.1.0 Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the feature release notes for the 2023.1.0 version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>
>From here, you can navigate to release notes of previous versions; for example, for those in 2021, 2022, and so on.
>
>Have a look at the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html) to learn about the upcoming feature activations for [!DNL Experience Manager] as a Cloud Service. 

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The release date of [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] 2023.1.0 feature release is February 9, 2023. The next feature release (2023.2.0) is planned for April 12, 2023.

## Release Video {#release-video}

Have a look at the January 2023 Release Overview video for a summary of the features added in the 2023.1.0 release:

>[!VIDEO](https://video.tv.adobe.com/v/3413479/?quality=12)

## [!DNL Experience Manager Sites] as a [!DNL Cloud Service] {#sites}

### New features in [!DNL Sites] prerelease {#prerelease-features-sites}

* The AEM GraphQL content delivery API now supports GraphQL [Paging](/help/headless/graphql-api/content-fragments.md#paging) and [Sorting](/help/headless/graphql-api/content-fragments.md#sorting), to make fetching and rendering large content sets more efficient. GraphQL pagination allows to improve query response time by returning results in sub-sets as opposed to all at once. GraphQL sorting allows putting content sets in a desired order, making it easier for a client appliation to process the content.  Query response time is further improved with Hybrid Filtering in the AEM GraphQL engine. Content is now read from JCR in smaller sets that correspond with query filters. 

## [!DNL Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

### New features in [!DNL Assets] {#assets-features}

* Assets Reports now includes the ability for Administrators to [generate assets download reports](/help/assets/asset-reports.md) from the Experience Manager Assets as a Cloud Service deployment. This data further empowers Admins to derive insights from key success metrics to measure the adoption of Assets within your enterprise and by customers.

   ![PDF rendition for other formats](/help/release-notes/assets/choose_report.png)

* Experience Manager Assets now [supports SAS Token](/help/assets/add-assets.md#asset-bulk-ingestor) in addition to the Access Key for authentication while connecting to Azure Blob Storage data source for ingesting assets using the Bulk Import tool.

* Improved management of CMYK images in Asset Compute, enabling you to generate Smart Crop and Smart Tags for CMYK images.

### New features in [!DNL Assets] prerelease {#prerelease-features-assets}

* Experience Manager Assets now supports [large-scale ingestion of assets from Google Cloud Platform](/help/assets/add-assets.md#asset-bulk-ingestor) using the Bulk Import tool.

## [!DNL Experience Manager Forms] as a [!DNL Cloud Service] {#forms}

### New features available in [!DNL Forms] {#new-features-available-in-channel}

* **[Workflow steps to generate non-interactive PDF documents and printable output](/help/forms/aem-forms-workflow-step-reference.md)**: Automate the creation of non-interactive PDF documents and printable output for your business processes with AEM Workflow steps, streamlining your document generation process and saving time.
* **[Use Footnotes to provide citations or extra information in Adaptive Forms](/help/forms/footnotes-richtextsupport.md)**:  Use Footnotes in an adaptive form to display the information on how to complete or use a form. You can also use it to provide parenthetical information, copyright permissions, and other helpful information.

### New features in [!DNL Forms] prerelease {#prerelease-features-forms}

* **[Use data capture core components to build Adaptive Forms](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html)**: [Use Adaptive Forms editor](/help/forms/creating-adaptive-form-core-components.md) to create forms based on standardized data capture components (Core Components). These components provide customization capabilities, reduced development time, and lower maintenance costs for your digital enrolment experiences.
* **[Frontend pipeline support for styling core component based Adaptive Forms](/help/forms/using-themes-in-core-components.md)**: Utilize easily customizable BEM-based themes for Core Components-based Adaptive Forms by deploying them with Frontend Deployment pipeline to enhance the look and feel of your forms.
* **[Generate Document of Record for core component based Adaptive Forms](/help/forms/generate-document-of-record-core-components.md)**: Create a record for core component based Adaptive Form on submission for long term archival, in print or in the document format. 

![https://www.aemcomponents.dev/](/help/forms/assets/sample-core-components-based-adaptive-form.png)

* **[Submit Adaptive Forms to Microsoft SharePoint and Microsoft OneDrive](/help/forms/configuring-submit-actions.md)**: Streamline data submission with the ability to directly send Adaptive Form data to both Microsoft SharePoint and Microsoft OneDrive. You can submit both schema-based and schema-less data. These submit actions are in addition to already available submit actions. 
* **[Efficient form-building with the Save an Adaptive Form as a template feature](/help/forms/template-editor.md#save-an-adaptive-form-as-template-saving-adaptive-form-as-template)**: Streamline your form-building process by saving an Adaptive Form as a template and reusing the templates for your next Adaptive Form. 
* **[Connect AEM Forms to JDBC-Supported databases](/help/forms/configure-data-sources.md#configure-relational-database-configure-relational-database)**: Easily connect your AEM Forms data model to databases that support JDBC, allowing you to read and write data seamlessly.
* **[Integrate with REST Endpoints Using Open API 3.0](/help/forms/configure-data-sources.md#configure-restful-services-open-api-specification-version-20-configure-restful-services-swagger-version30)**: Connect AEM Forms as a Cloud Service Form Data Models to REST endpoints that support Open API specification version 3.0, allowing you to send and receive data with ease.
* **[Share an Adaptive Form for review](/help/forms/create-reviews-forms.md)**: Use the Adaptive Forms review mechanism to allow one or more reviewers to review the form.

## [!DNL Experience Manager as a Cloud Service] Foundation {#foundation}

### What is New {#what-is-new-foundation}

* [Rapid Development Environments](/help/implementing/developing/introduction/rapid-development-environments.md) - RDEs enable developers to rapidly troubleshoot issues and deploy new features on AEM as a Cloud Service.  

  Rapid Development Environments are a new type of Cloud Environment intended as a fast, consistent, and extensible way of validating that code working locally also functions as expected in the Cloud. Using Command Line Tools, quickly "sync" content packages, bundles, content files, OSGI configuration, or dispatcher configuration to the RDE. See this in action in the video below:  
  
  >[!VIDEO](https://video.tv.adobe.com/v/3413508/?quality=12&learn=on)   
 
  After successfully validating code in the RDE, it is encouraged to deploy to a Cloud Dev Environment to exercise the Cloud Manager quality gates, before deploying via production pipeline to stage and production environments.  

  Each program includes one RDE and optionally, more can be licensed.  
    
  >[!NOTE]
  >
  >RDEs will be gradually rolled out over the next few weeks; you can send an email to aemcs-rde-support@adobe.com to skip to the front of the line.

* [Extended support for server-side API access tokens](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md) – You can now generate multiple credentials, which is useful for scenarios where APIs have different characteristics. It is also now possible to revoke credentials in a self-service manner.

## Maintenance Release Notes {#maintenance}

You can find the latest maintenance release notes [here](/help/release-notes/maintenance/latest.md).

## Cloud Manager {#cloud-manager}

You can find a complete list of Cloud Manager monthly releases [here](/help/implementing/cloud-manager/release-notes/current.md).

## Migration Tools {#migration-tools}

You can find a complete list of Migration Tools releases [here](/help/journey-migration/release-notes/release-notes-migration-tools-current.md).
