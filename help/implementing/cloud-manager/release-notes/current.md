---
title: Release Notes for Cloud Manager 2025.1.0 in Adobe Experience Manager as a Cloud Service
description: Learn about the release of Cloud Manager 2025.1.0 in AEM as a Cloud Service.
feature: Release Information
role: Admin

---
# Release notes for Cloud Manager 2025.1.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

Learn about the release of Cloud Manager 2025.1.0 in AEM (Adobe Experience Manager) as a Cloud Service.

>[!NOTE]
>
>See the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.1.0 in AEM as a Cloud Service is Thursday, January 23, 2025. 

The next planned release is Thursday, February 13, 2025.
 

## What's new {#what-is-new}

* **SonarQube enablement approach:** 

* **Java 17 and Java 21 build support:** Customers can now build with Java 17 or Java 21, gaining access to performance enhancements and new language features. For configuration steps, including updating your Maven project and library versions, see [Build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md). When the build version is set to Java 17 or Java 21, the runtime deployed is Java 21.

    * **Feature enablement**
        * This feature will be enabled for all customers on Thursday, February 13, 2025, coinciding with the default rollout of the new SonarQube version.
        * Customers can enable it *immediately* by manually upgrading the SonarQube version as described in the documentation.

    * **Java 21 runtime deployment**
        * The Java 21 runtime is deployed when building with Java 17 or Java 21.
        * Gradual rollout to all Cloud Manager environments begins in February for sandboxes and development environments and extends to production environments in April.
        * Customers who want to adopt the Java 21 runtime *earlier* can contact Adobe at [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com).


<!-- ## Early adoption program {#early-adoption}

Be a part of Cloud Manager's early adoption program and have a chance to test upcoming features. -->

<!-- ## Bug fixes -->




<!-- ## Known issues {#known-issues} -->
