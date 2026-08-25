---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release X {#release-X}

Summarized below are the continuous improvements for maintenance release X, which was publicly released on August 26, 2026. The previous maintenance release was release 27673.

The 2026.9.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

### Enhancements {#enhancements-X}

* FORMS-27178: Font sizes are now rounded to the nearest integer point during PDF generation for more consistent output.

### Fixed Issues {#fixed-issues-X}

* FORMS-25184: In the Data Sources panel, the binding-indicator dots were missing for Core Components-based Adaptive Forms.
* FORMS-26236: The `fd-service` user was missing `jcr:versionManagement` permissions on `/conf`.
* FORMS-26250: Switching fields in the Rule Editor while rules were still loading applied or saved the wrong field's rules, due to a race condition.
* FORMS-26476: The Content Tree did not load in the Adaptive Forms editor.
* FORMS-26500: Uploading multiple files with the same name to a foundation Adaptive Forms file-attachment field saved only one binary on the server.
* FORMS-26627: Concurrent read and update calls in the Rule Editor could overlap and corrupt rule state; a blocking loader now prevents this.
* FORMS-26633: A Forms script misidentified non-Forms dialogs, which broke any component that has an "Advanced" tab.
* FORMS-26813: The File Attachment component ignored the custom "unsupported file type" message (`acceptMessage`).
* FORMS-26824: In the Rule Editor, dragging a form object across an existing target cleared that target and reverted it to "Drop here."
* FORMS-26864: Forms Manager did not download or publish fragments that were bound to variables.
* FORMS-26878: On French Adaptive Forms, the Date Picker validation message was not localized and appeared in English.
* FORMS-26910: Objects went missing after syncing when a template was used as a reference.
* FORMS-26974: The Dropdown component's PDF preview showed the default value instead of the bound value when both were set.
* FORMS-26986: Fragments present in an Interactive Communications (IC) Document disappeared when the document was synced with its template.
* FORMS-27224: In Interactive Communications (IC), pagination and binding properties overridden in an IC Document were not preserved after a template sync.
* FORMS-27506: When a template was used as a reference, legacy document-author overrides were dropped during the template sync.

### Known Issues {#known-issues-X}

None.

### Deprecated Features and APIs {#deprecated-X}

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-X}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses X identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-X}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 2.4.0 | [Oak 2.4.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/2.4.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.67 | [Apache Httpd 2.4.67](https://apache.googlesource.com/httpd/+/refs/tags/2.4.67/CHANGES)|
|Dispatcher|2.0.274||
|AEM Core Components| 2.32.4|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
|Java 21|21.0.11|[JDK 21.0.11](https://www.oracle.com/java/technologies/javase/21-0-11-relnotes.html)|
