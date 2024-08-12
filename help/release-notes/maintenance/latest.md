---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 17349 {#release-17349}

Summarized below are the continuous improvements for maintenance release 17349, which was publicly released on August 13, 2024. The previous maintenance release was release 17258.

The 2024.8.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-17349}

* FORMS-15436 - Gracefully handle exception in Adobe Sign Status scheduler.
* FORMS-15362 - Add configuration for forms-foundation in aemds to enable login.
* FORMS-15261 - SPA does not render in Forms editor.
* FORMS-15138 - Handling for Double data backward compatability due to sling commons json upgrade.
* FORMS-15113 - Changing Key name to sid from vistorId for RUM tracking.
* FORMS-15103 - Assets attached in a form are not getting published in edge delivery.
* FORMS-15082 - JSON schema to map to custom adaptive form components.
* FORMS-15002 - Template type registration of v1 fragments.
* FORMS-14845 - Support for xdpRef in core component bases form via forms manager.
* FORMS-14840 - Forms Prefill Service Errors.
* FORMS-14836 - Improve forms manager UI, to list AF1 fragment templates.
* FORMS-14834 - Template support for fragments in AF1.
* FORMS-14275 - Overriding Thank you page and Thank you Message in Embed Container.
* FORMS-13623 - Enable auto save time based functionality for V2.
* FORMS-8651 - Warning dialog on changing data model configuration on form properties page.
* SITES-23310 - Content Fragments REST API: Prevent Circular Dependencies in Nested References for Content Fragments.
* SITES-23285 - Content Fragments REST API: Create endpoint to list all available Languages.
* SITES-22857 - Content Fragments REST API: Checkbox enumeration fields should not allow multiple property set to false.
* SITES-22813 - Content Fragments REST API: Define min/max properties for enumeration fields.
* SITES-22031 - Content Fragments REST API: Get allowed content fragment models for a Fragment's folder.
* SITES-17640 - Content Fragments REST API: Content Fragment Publish operation validation.
* SITES-22677 - Content Fragments REST API: Retrieve a flat list of descendent references
* SITES-22207 - Model duplicated on Content Fragment creation.
* SITES-23093 - Eventing: add tags to payloads for Content Fragment Model events.
* SITES-23092 - Eventing: add tags to payloads for Content Fragment events.
* SITES-22447 - Add Experience Fragment properties inheritance support to the Basic properties tab.
* SITES-12209 - Improve Policy Editor performance by adding cq:policy to index.

### Fixed Issues {#fixed-issues-17349}

* CQ-4358028 - Failed to create project if thumbnail is uploaded.
* CQ-4357891 - Sequence Issue of Exported XLIFF.
* CQ-4357059 - Translation Job takes hours to complete causing 503 timeout in AEMaaCS.
* FORMS-15320 - Email submission is not working in core component based form.
* FORMS-15272 - AEM Forms - Checkbox group only sending 1 value.
* FORMS-15269 - Facing product related issues after maintenance release 16461.
* FORMS-15174 - JsonSchemaParser isValid issue.
* FORMS-15095 - Multiline Textbox Can Be Stretched Beyond Containing Panels in AEM Forms.
* FORMS-15057 - FDM Sharepoint list throwing attachment error for submission > 999.
* FORMS-15011 - Core Editor is causing console error while opening a Form in editor.
* FORMS-14809 - SDK folder not getting created automatically inside shared temp directory.
* FORMS-14327 - Forms Service APIs : Extract data:- gives 500 response code when a non-interactive pdf is provided in input.
* FORMS-7475 - Sorting is not working on Adaptive Form creation page.
* FORMS-3309 - If multiple options are selected when submitting a form, then in a generated DoR only one option is displaying.
* SITES-23646 - GraphQL models endpoint fails for models created with OpenAPI if fields contain unique.
* SITES-23637 - Content Fragments REST API: OpenAPI doesn't use the correct value type for enums.
* SITES-23573 - Content Fragments REST API: Live relationships are not respected on GET Content Fragments by uuid.
* SITES-23535 - Content Fragments REST API: Content Fragment Model enumeration multi-fields have empty values.
* SITES-23534 - Content Fragments REST API: Content Fragment Validation ClassCastException.
* SITES-23524 - Adapt GraphQL BFF models endpoint to support multi-field enumeration fields.
* SITES-23467 - Content Fragments REST API: Search Models fails due to cursor issue.
* SITES-23327 - ArrayIndexOutOfBoundsException in AuditLogTimelineEventProvider during Timeline Event Processing Description.
* SITES-23277 - Content Fragments REST API: Content Fragment Field live relationship check should only be done for live copies.
* SITES-23232 - Custom validation does not work in new CF Editor UI.
* SITES-23090 - Content Fragments REST API: Cannot update title of a locked Content Fragment.
* SITES-22981 - Promoting a nested launch which is not deep is not publishing.
* SITES-22870 - PathAttributesHandler.processSrcAttr ArrayIndexOutOfBoundsException.
* SITES-22814 - Content Fragments REST API: Checkbox Enumeration fragment fields values should be ordered by the keys defined in the model.
* SITES-22716 - Issue with OOTB components live usage List.
* SITES-22457 - Promoting a launch which is not deep is not updating source content.
* SITES-22449 - Unable to save changes in content fragments after AEM P20 upgrade.
* SITES-22279 - Content Fragments REST API: Content Fragment is missing the unique attribute for Enumeration types.
* SITES-22203 - Content Fragments REST API: Align Management APIs to respond the same for the same situation.
* SITES-21973 - Content Fragments REST API: Model is missing the unique attribute for Enumeration types.
* SITES-20364 - 302 Redirects Not Working with Selector in URL.
* SITES-21198 - VersionPreviewServlet: Cleanup runs concurrently on all cluster nodes causing merge conflicts and blocks commits
* GRANITE-53094 - Repository-based JS Use objects cannot be located when using relative paths.

### Known Issues {#known-issues-17349}

None.

### Change Notice {#change-notice-17349}

* Starting in September 2024, AEM as a Cloud Service will disable the serialization of Resource Resolvers via the Sling Model Exporter framework. See [the documentation](/help/implementing/developing/hybrid/disallow-the-serialization-of-resourceresolvers-via-sling-model-exporter.md) for more details.

### Deprecated Features and APIs {#deprecated-17349}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Embedded Technologies {#embedded-tech-17349}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.66.0|[Oak API 1.66.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.66.0/index.html)| 
|AEM SLING API | 2.27.2 |[Apache Sling API 2.27.2 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.24-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|AEM Core Components| 2.25.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
