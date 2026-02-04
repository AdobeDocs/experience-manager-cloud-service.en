---
title: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Maintenance Release Notes of [!DNL Adobe Experience Manager] as a Cloud Service.
exl-id: eee42b4d-9206-4ebf-b88d-d8df14c46094
feature: Release Information
role: Admin
---

# Maintenance Release Notes {#maintenance-release-notes}

The following section outlines the technical release notes for the current maintenance release of Experience Manager as a Cloud Service.

## Release 24222 {#24222}

Summarized below are the continuous improvements for maintenance release 24222, which was publicly released on February 4, 2026. The previous maintenance release was release 23963.

The 2026.2.0 feature activation will provide the full feature set for this maintenance release. See the [Experience Manager Releases Roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap) for more information.

>[!NOTE]
>
>Release 24222 has been made private. 

### Enhancements {#enhancements-24222}

* CNTBF-604: Create new contentbackflow bundle release.
* CQ-4361592: Add TypeHint support for project creation and update.
* CQ-4362198: Latest AEM and Granite package translations.
* GRANITE-36205: Update internal Oak release version to latest.
* GRANITE-59211: OPTEL: Added nonce support and self-service configuration.
* GRANITE-62166: Update migration bundle to reuse migration states from migration tool.
* GRANITE-62598: Remove redundant property exclude from content package filter.
* GRANITE-62684: Make client socket timeout configurable through skyline-ops.
* GRANITE-62702: Replace sling discovery with standalone implementation for online migration.
* GRANITE-62763: Update Guava deprecation exception list based on ASSETS rotary.
* GRANITE-62771: Fail Quickstart builds when new deprecated Commons-Lang dependencies are introduced.
* GRANITE-62987: Update Felix webconsole to version 5.0.18.
* GRANITE-63339: Improve lease mechanism for Azure migration-state blob.
* GRANITE-63343: Add support for the latest version of the Sling API bundle in workflow.core.
* GRANITE-63799: Bump OIDC Authentication Bundle version.
* GRANITE-63821: Update Quickstart to filevault release fixing JCRVLT-831/JCRVLT-839.
* GRANITE-63827: Update Quickstart to the latest public release of Oak (1.90.0).
* GRANITE-63888: Update Quickstart to Jackrabbit 2.22.3.
* GRANITE-64030: Add keywords and patterns to the allowed list for Expression Language Validator.
* GRANITE-64050: Allow for hidden conf folders to hide external product functionality.
* SITES-30452: Content API with ASO - Title and Description Suggestions.
* SITES-38099: Update `testing-model.txt` to use higher version of sanity checks.
* SKYOPS-43616: Migrate Jenkins credentials to Vault in dispatcher repositories.
* SKYOPS-108584: Bump FACT tool from 0.6.0 to 0.6.10.
* SKYOPS-115691: Upgrade CORS filter bundle to add Vary Origin header on preflight requests.
* SKYOPS-123094: Update Apache HTTP components in Quickstart.
* SKYOPS-123236: Include `rep:cugPolicy` in the replication package.
* SKYOPS-123240: Update CRXDE dependencies in Quickstart.
* SKYOPS-123247: Update Sling XSS bundle in Quickstart.
* SKYOPS-123250: Update Sling security bundle in Quickstart.
* SKYOPS-123327: Require Java 21 for the AEM-CS SDK.
* SKYOPS-125574: Update netcentric AC Tool bundles in Quickstart.
* SKYOPS-126150: Improve top command for thread dumps generator script.

### Fixed Issues {#fixed-issues-24222}

* FORMS-23687: Fix SSV validation failure when contains rule is used without default value.
* GRANITE-48472: Localize error when changing password in the Edit User Settings tab.
* GRANITE-50286: Fix layout issue in the status column of User Management modal.
* GRANITE-52301: Localize Unable to commit changes to session string in Security Groups.
* GRANITE-52920: Localize error when creating user in Security Create New User.
* GRANITE-54654: Localize string in Security Adobe IMS Configurations Check dialog.
* GRANITE-56371: Fix incorrect data format in Security Trust Store.
* GRANITE-62717: Upgrade crypto keystore for JSafe password handling with non-ASCII characters.
* GRANITE-62789: Update messaging-client to support no retries mode on content distribution.
* GRANITE-62824: Fix `NullPointerException` when accessing Groups tab in User Editor.
* GRANITE-63080: Make import of `org.slf4j.spi` compatible with `slf4j 2.x`.
* GRANITE-63210: Update distribution core to fix dispatcher invalidation on publish startup.
* GRANITE-63293: Fix mandatory pathfield losing the required asterisk after first authoring.
* GRANITE-63360: Fix wrong information shown when multiple paths are selected.
* SITES-36242: Narrow down GraphQL execute regex to fix dispatcher filter bypass.
* SITES-40122: Fix of Edge Delivery integration with content-distribution ImsService.
* SKYOPS-84379: Use the latest FACT tool for proper feature toggle pickup by RDEs.
* SKYOPS-121216: Revert update to Jackson 2.20.0 libraries.

#### AEM Guides {#guides-24222}

* GUIDES-38198 : When updating an inline MathML equation using the Edit MathML option from the context menu, the updated value is not reflected until the page is refreshed.
* GUIDES-38276: Unable to remove Version labels from Version history panel in Assets UI.
* GUIDES-36641: When generating AEM Sites output, the map titles containing keywords and topic titles with `<ph>` element are not getting included in the published output.
* GUIDES-37837: When attempting to save a topic or map, the operation may intermittently fail with a Failed to save file error, particularly during intensive asset processing tasks or translation workflows running in the background.
* GUIDES-27774: The Broken list report is incorrectly including external links, valid `keyrefs` and keywords that are properly resolved within scope of current map.

For more information about the new and enhanced features and issues fixed in the release, view the [Experience Manager Guides release roadmap](https://experienceleague.adobe.com/en/docs/experience-manager-guides/using/release-info/aem-guides-releases-roadmap). 

### Known Issues {#known-issues-24222}

None.

### Deprecated Features and APIs {#deprecated-24222}

* AEMSRE-2896: Fix customized logmanager configuration handling.
* GRANITE-62802: Remove deprecated `commons-lang` dependency from `granite.auth.saml`.
* GRANITE-62805: Remove deprecated `commons-lang` dependency from `granite.httpcache.core`.
* GRANITE-62864: Remove deprecated `commons-lang` dependency from `granite.jobs.async`.
* GRANITE-62865: Remove deprecated `commons-lang` dependency from `granite.replication.core`.
* GRANITE-62868: Remove deprecated `commons-lang` dependency from `granite.rest.api`.
* GRANITE-62895: Remove deprecated `commons-lang` dependency from `translation.connector.msft.core`.
* GRANITE-63069: Deprecate `com.adobe.granite.httpcache.core`.
* GRANITE-63179: Remove deprecated `commons-lang` dependency from `cq-workflow-impl`.
* GRANITE-63180: Remove deprecated `commons.lang` export from `cq-mailer` bundle.
* SKYOPS-123329: Drop Java 11 support for AEM Ethos deployments and update `commons-lang3`.
* SKYOPS-124983: Remove deprecated `nashorn.args` from AEM startup scripts.

Deprecated and removed features and APIs in AEM as a Cloud Service are detailed in the [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md) document.

### Security Fixes {#security-24222}

AEM as a Cloud Service is dedicated to optimizing your platform's security and performance. This maintenance release addresses 10 identified vulnerabilities, reinforcing our commitment to robust system protection.

### Embedded Technologies {#embedded-tech-24222}

|Technology|Version|Link|
|---|---|---|
|AEM Oak | 1.90.0|[Oak 1.90.0 API](https://www.javadoc.io/doc/org.apache.jackrabbit/oak-api/1.90.0/index.html)|
|AEM SLING API | 2.27.6 |[Apache Sling API 2.27.6 API](https://www.javadoc.io/doc/org.apache.sling/org.apache.sling.api/latest/index.html)|
|AEM HTL| 1.4.28-1.4.0 |[HTML Template Language Specification](https://github.com/adobe/htl-spec)|
|Apache HTTP Server| 2.4.65 | [Apache Httpd 2.4.65](https://apache.googlesource.com/httpd/+/refs/tags/2.4.65/CHANGES)|
|AEM Core Components| 2.30.2|[AEM WCM Core Components](https://github.com/adobe/aem-core-wcm-components)|
|Node.js|14 (default)|[Supported Node.js versions](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developing/developing-with-front-end-pipelines#node-versions)|
