---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 25194 {#25194}

Summarized below are the continuous improvements for maintenance release 25194, which was publicly released on April 1, 2026. The previous maintenance release was release 24678.

The 2026.4.0 feature activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

>[!NOTE]
>
>Release 24893 has been made private. 

### Enhancements {#enhancements-25194}

* ASSETS-65127: Event custom metadata: improved handling of metadata names.
* ASSETS-63313: Auto-create related links for exported assets and parents based on C2PA manifests.
* ASSETS-10995: Limit number of assets in a download zip.
* FORMS-24388: Added a local development environment for the Interactive Communication (IC) Editor that enables developers to build and test configurations without relying on shared servers. This enhancement helps enterprise customers iterate faster, reduce environment dependencies, and improve overall development productivity. 
* FORMS-24014: Enhanced the Rule Editor for file attachment components to support combining conditions using "AND" logic—for example, allowing rules like "If the file attachment is changed and the panel is valid, then do this." Previously, it was not possible to use additional conditions with file attachments; this update enables more complex rule definitions to support advanced workflows.
* FORMS-23571: Enhanced the existing simplified grammar view for trigger event rules by adding support for out-of-the-box (OOTB) events in addition to custom events. Previously, users could only use the simplified grammar for custom events and had to switch between "WHEN" and "ON TRIGGER EVENT" rules to configure OOTB and custom events separately. With this update, both OOTB and custom events can be used in the same simplified grammar, streamlining rule configuration and reducing the need to switch contexts.
* FORMS-24462: Added support for the Scribble Signature component in React Vanilla components for Headless Adaptive Forms (AF). This enhancement enables users to capture handwritten signatures directly within React-based forms, supporting digital signing workflows and planned go-live timelines for enterprise customers. 
* FORMS-24343: Added optimized handling for `custom:setProperty` in the form model JavaScript Object Notation (JSON), enabling faster processing of dynamic property updates. This enhancement improves performance for complex Adaptive Forms (AF) that rely on frequent runtime changes, resulting in smoother user interactions and reduced load times. 
* FORMS-24358: Added support for using the `items` property in the model JavaScript Object Notation (JSON) structure instead of `:items` and `:itemsOrder`. This enhancement enables developers to work with a cleaner, more intuitive data model that aligns better with common JSON conventions and simplifies integration with external systems. 
* FORMS-24087: Added support for defining rules and events directly on fragment containers in Adaptive Forms (AF). This enhancement enables authors to apply conditional logic and interactions at the container level, improving reuse and reducing the need to duplicate rules across individual fragment fields. 
* FORMS-24440: Added a new "Remove Field" action in the THEN dropdown of the Rule Editor for Interactive Communication editor that enables users to completely remove a selected component from the form when a rule condition is met. This enhancement supports workflows that require dynamically restructuring forms instead of only hiding fields, while still triggering the appropriate `forms_ready` script for consistent behavior. 
* FORMS-23898: Added support for defining variables using `@` notation in the Interactive Communication (IC) Editor, enabling users to configure dynamic tables more intuitively. This enhancement simplifies setup of variable-driven table content and improves clarity when managing dynamic data in the authoring experience. 
* FORMS-23702: Added certificate-based authentication for SharePoint List (SPList) connections that enables more secure, certificate-driven access to SharePoint data. This enhancement helps enterprise customers meet stricter security and compliance requirements while reducing reliance on password-based authentication. 
* FORMS-23800: Added support for overriding reCAPTCHA secret keys in sling configurations, enabling enterprise customers to align with their own security and compliance requirements. This enhancement allows environment-specific secret key management so administrators can safely integrate reCAPTCHA without code changes. 

### Fixed Issues {#fixed-issues-25194}

* ASSETS-62882: Admin view: info tooltip breaks when multiple invalid filenames are uploaded.
* ASSETS-63642: Share link fails to render asset on some dev environments (SLA3).
* ASSETS-59267: NPE when loading application metadata for delivery payload.
* ASSETS-59227: Metadata export: unselected properties no longer included due to regex matching.
* ASSETS-65187: CSV preview in Cloud when column data contains escaped commas.
* ASSETS-63441: Ensure all users have permissions to read Assets Omnisearch configuration.
* SITES-40095: Metadata editor: local content fragment references beyond 10 entries.
* FORMS-24811: Users experienced issues managing form logic rules. When they tried to modify rules that had been created earlier, the rule editor did not allow changes, forcing users to recreate rules from scratch and slowing down form maintenance. 
* FORMS-24720: Users experienced issues when configuring newly created variables in Adaptive Forms (AF). When they added rules to data-bound or unbound variables, the rules did not save as expected, forcing users to recreate their logic and slowing down form authoring workflows. 
* FORMS-24195: Users experienced inconsistent behavior when resetting dropdown fields in Adaptive Forms (AF). When a dropdown had a placeholder configured and the form or component was reset, the field became blank instead of returning to the placeholder value, causing confusion about required selections. 
* FORMS-24718: Users experienced navigation issues in the Interactive Communication (IC) editor when selecting the Home button. Instead of returning to the main Adobe Experience Manager (AEM) interface, the button did not redirect as expected, disrupting users’ workflow when moving between IC editing and the AEM home screen. 
* FORMS-24810: Users experienced intermittent failures when loading the Adaptive User Interface (AUI) for forms on the first attempt. In some sessions, the initial page did not render correctly, forcing users to refresh or retry before they could begin filling out their forms. 
* FORMS-24520: Users experienced missing page numbers in the agent user interface (UI) print preview for forms using the Adaptive User Interface (AUI). When agents opened the print preview, the page number field sometimes appeared empty, making it harder to reference specific pages while reviewing or sharing printed copies. 
* FORMS-24532: Users experienced failures when using Form Data Model (FDM) prefill with SharePoint `/teams` list configurations. Government organizations relying on these lists saw forms load without expected prefilled data, disrupting data collection workflows and increasing manual entry effort. 
* FORMS-24516: Users experienced missing scribble signature data in the Document of Record (DoR) after an SDK upgrade in AEM Forms as a Cloud Service. When forms were signed using the scribble option, the generated DoR did not display the captured signature, causing confusion and incomplete records for enterprise customers. 
* FORMS-18631: Users experienced accessibility issues with grid layouts on desktop, Responsive Web Design (RWD) tablet, and RWD mobile views. When using Chrome on Windows 11 with the NVDA (NonVisual Desktop Access) screen reader, grids were missing appropriate roles and attributes, making it difficult for assistive technologies to interpret and navigate the content correctly. 
* FORMS-24798: Users experienced inconsistent behavior when using `else` conditions in Adaptive Forms (AF) rules within the AEM Forms User Interface (UI). When the primary rule condition was not met, the associated `else` actions did not run, causing form logic and field visibility to behave differently from what authors configured. 
* FORMS-24334: Users experienced prefill failures and JavaScript Object Notation (JSON) merge issues when working with an embedded Adaptive Form (AF) on Adobe Experience Manager (AEM) Forms as a Cloud Service. When loading migrated forms, expected prefilled data did not appear and merged JSON content was incomplete or incorrect. This blocked migration from on-premise AEM 6.5 to AEM Forms as a Cloud Service for impacted environments. 
* FORMS-24441: Users experienced issues with the Document of Record (DoR) template configuration in Adobe Experience Manager (AEM) Forms as a Cloud Service. When they saved a customized DoR template in the rapid development environment, the template reverted to the default version, preventing them from retaining their intended layout and settings. 
* FORMS-24393: Users experienced confusion when older templates continued to appear as “Untitled” instead of showing meaningful names. This made it difficult to distinguish and reuse existing templates during daily authoring work. 
* FORMS-24163: Users experienced issues when previewing Version 2 forms that contained fragments. In preview mode, the form content did not render as expected, preventing users from validating the layout and behavior before publishing. 
* FORMS-24328: Users experienced form submissions not completing when using Invisible reCAPTCHA v2 with the "Validate CAPTCHA on a user action" option. Enterprise customers saw that forms on affected environments did not submit as expected, disrupting contact and request-for-proposal workflows. 

#### AEM Guides {#guides-25194}

* GUIDES-38412 : When editing a Schematron `(*.sch)` file and using the find and replace feature, the find and replace panel appears partially off-screen at the bottom, preventing access to its input fields and controls.
* GUIDES-37806: When the same topic is reused across multiple maps with different conditional presets, publishing the latest map to Salesforce overwrites the topic content, resulting in incorrect data being displayed to users of previously published maps.
* GUIDES-39394: When an image initially managed as a language‑specific asset with a specific version (for example, under `/en/`) is moved out to a global folder with an updated version and baseline export is performed, the new baseline continues to reference outdated language‑specific versions of that image, leading to a failed baseline export.
* GUIDES-39054: When creating a dynamic baseline, the Editor sometimes becomes unresponsive due to multiple concurrent API requests, causing all the other operations to halt.
* GUIDES-37781: When assigning a user to a review task, the dropdown lists all users instead of only those associated with the selected projects, resulting in invalid user options.
* GUIDES-39385: While opening a Report for a map, there is a delay in the loading of the Filters panel.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-25194}

None.

### Deprecated Features and APIs {#deprecated-25194}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-25194}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 9 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-25194}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.90.0|[Oak 1.90.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.90.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
