---
title: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.2.0
description: Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.2.0
feature: Release Information
exl-id: b1cd871d-c71e-4902-a97e-2c859f6a4da4
---
# Release Notes for Migration Tools in AEM as a Cloud Service Release 2022.2.0 {#release-notes}

This page outlines the Release Notes for Migration Tools in AEM as a Cloud Service 2022.2.0.

## Best Practices Analyzer {#bpa-release}

### Release Date {#release-date-bpa}

The Release Date for Best Practices Analyzer v2.1.24 is February 01, 2022.

### What's New {#what-is-new-bpa}

* Ability to detect and report on the number of assets with and without Smart Tags.
* Ability to detect and report on the version of Core Component used.
* Ability to detect and report on the type of source tier (Author or Publish) where BPA was executed.

### Bug Fixes {#bug-fixes-bpa}

* BPA sizing logic was made faster and more efficient.
* In some scenarios, BPA did not increment analyzed count when it was run. This has been fixed.

## Content Transfer Tool {#ctt-release}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.8.6 is February 03, 2022.

### What's New {#what-is-new-ctt}

* Content Validation - Users have the ability to reliably determine if all of the content that was extracted by the Content Transfer Tool was successfully ingested into the target instance. To use this feature, you will need to enable it in the `System Console` of the source AEM environment. Refer to [Validating Content Transfers - Getting Started](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/validating-content-transfers.html?lang=en#getting-started) for more details.

### Bug Fixes {#bug-fixes-ctt}

* Some users were not mapped because User Mapping was case sensitive. This has been fixed. User Mapping is no longer case sensitive.
