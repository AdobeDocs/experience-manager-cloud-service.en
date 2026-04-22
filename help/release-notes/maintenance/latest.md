---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 25520 {#25520}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on April 23, 2026. The previous maintenance release was release 25194.

The 2026.4.0 feature activation provides the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.


### Enhancements {#enhancements-25520}

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
* SITES-39116: Content Fragment GET endpoint now includes metadata schema information.
* SITES-41449: New dedicated GET endpoint for retrieving Content Fragment metadata.
* SITES-39434: Content Fragments and folders can now be linked to metadata schemas for structured metadata management.
* SITES-39567: Content Fragment metadata is now validated and stored according to the linked metadata schema.
* SITES-40006: Content Fragments can now be searched and filtered using metadata field values.
* SITES-41391: Single Content Fragment retrieval API now includes check-in/check-out status information
* SITES-42214: Improved reliability and performance of Content Fragment move operations
* SITES-41351: Improved the display format of metadata in Content Fragments for better readability.
* SITES-42458: Default metadata can now be added without strict schema validation for greater flexibility.
* SITES-35508: Edge Delivery with Universal Editor: Add support for images in RTE.
* SITES-37078: Edge Delivery with Universal Editor: Remove Universal Editor instrumentations when pages are read-only.
* SITES-40206: Edge Delivery with Universal Editor: Add name validation to page creation wizard.
* SITES-40255: Edge Delivery with Universal Editor: Prevent publishing of spreadsheets as `/config.json`.
* SITES-40757: Edge Delivery with Universal Editor: Ensure uniqueness of Edge Delivery Configurations in Site Creation wizard.
* SITES-41134: Edge Delivery with Universal Editor: Fail publishing of file-based configuration.

### Fixed Issues {#fixed-issues-25520}

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
* SITES-42118: Skip rewrite rules for `/graphql/execute.json`.
* SITES-40095: Fix local reference list in the metadata editor.
* SITES-42191: Fix GraphQL JSON omits embedded image references when DAM filenames contain spaces / non-ASCII characters.
* SITES-22336: Unlocalized "Content Fragment Models" string in Assets > Create > Content Fragment.
* SITES-19796: Unlocalized string "Invalid name provided" is displayed on adding invalid character while creating content fragment under Assets.
* SITES-42531: Tooltip is unlocalized when lock-in "Content Fragment" in "Assets" page..
* SITES-42532: Unlocalized "Later" string on publishing CF to AEM in Assets.
* SITES-39250: Localized characters are incorrectly displayed in link in Assets > Content Fragment Editor.
* SITES-41117: Unlocalized 'The selected value needs to be a valid Model Type inside `{}` or a global model.' string in Content Fragment Model Editor.
* SITES-41431: Reduced verbosity of screen reader feedback for the lock button to provide clearer, more concise announcements.
* SITES-40819: Fixed keyboard focus not returning to the triggering element after an interaction, ensuring a predictable focus order.
* SITES-40751: Added visible labels on keyboard focus for toolbar items so keyboard users can clearly identify actions.
* SITES-25524: Corrected the use of aria-pressed on device buttons so assistive technologies receive accurate state information.
* SITES-25321: Updated text colors to meet minimum contrast requirements and improve readability for low-vision users.
* SITES-25304: Prevented the collapsed Demographic toolbar from incorrectly receiving focus, maintaining a logical focus sequence.
* SITES-25292: Clarified screen reader announcements for the rotate device button to better describe its purpose and state.
* SITES-25290: Added a visible pressed state for the desktop toggle button to make its selection status obvious to users.
* SITES-25287: Improved ruler measurement context when editing layout, giving screen reader users understandable measurement information.
* SITES-25284: Fixed truncation of the "iPhone 8 Plus" button label in the unchecked state so the full device name is announced and visible.
* SITES-25251: Introduced feedback for screen reader users when the "Insert New Component" list is filtered, indicating that results have changed.
* SITES-25221: Increased the touch target size of the Edit button in the Asset Side Rail to meet minimum target size guidelines.
* SITES-25220: Added warning/indication that the Edit button in the Assets Left Rail opens a new tab, improving predictability for assistive tech users.
* SITES-24993: Updated the Editor Canvas header title to use a proper heading role, improving document structure for screen readers.
* SITES-24954: Corrected the focus order for the emulator button so it follows a natural and logical navigation sequence.
* SITES-41586: Fix for Copy-Pasting of Content Fragment component inside editor loosing a reference to content fragment.
* SITES-42195: Fix `CommerceLinksTransformerFactory` not respecting sling mappings on publish instance.
* SITES-41238: Fix error in ThumbnailServlet causing log flood.
* SITES-41041: Fix CIF components not rendered in Version Preview / Compare.
* SITES-40756: Fix Unlocalized date format in Live Copy Overview > Relationship Status.
* SITES-40219: Fix CatalogPageNotFoundFilter not being called for specific product or category pages.
* SITES-40218: Fix SpecificPageFilterFactory missing v3 page resource type registration.
* SITES-40347: Break the inheritance for the title when creating a live copy with a new title set.
* SITES-41544: Content Fragment ETag calculations now exclude metadata.
* SITES-42734: Fixed issue where GET metadata endpoint returned empty fields when using the default schema.
* SITES-37955: Edge Delivery with Universal Editor: Ensure publication prerequisites are checked consistently.
* SITES-40877: Edge Delivery with Universal Editor: Fix publishing failures for pages containing non-ascii special characters.
* SITES-42092: Edge Delivery with Universal Editor: Fix deep un-publishing for paths ending in `-s`.
* SITES-24650: iframe does not have a title.

### Known Issues {#known-issues-25520}

None.

### Deprecated Features and APIs {#deprecated-25520}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-25520}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 24 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-25520}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.90.0|[Oak 1.90.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.90.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
