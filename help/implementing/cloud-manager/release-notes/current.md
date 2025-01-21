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

The release date for Cloud Manager 2025.1.0 in AEM as a Cloud Service is Wednesday, January 22, 2025. 

The next planned release is Thursday, February 13, 2025.
 

## What's new {#what-is-new}

* **Code quality rules:** Cloud Manager Code Quality step will start using SonarQube Server 9.9 with Cloud Manager 2025.2.0 release, scheduled for Thursday, February 13, 2025. 

To prepare, updated SonarQube rules are now available at [Code Quality Rules](/help/implementing/cloud-manager/code-quality-testing.md#understanding-code-quality-rules).

You can "early check" the new rules by setting the following pipeline text variable: 

`CM_BUILD_IMAGE_OVERRIDE` = `self-service-build:sonar-99-upgrade-java17or21`

Additionally, set the following variable to ensure the code quality step runs for the same commit (normally skipped for the same `commitId`): 

`CM_DISABLE_BUILD_REUSE` = `true`

![Variables Configuration page](/help/implementing/cloud-manager/release-notes/assets/variables-config.png)

>[!NOTE]
>
>Adobe recommends creating a new CI/CD Code Quality pipeline, configured to the same branch as your main production pipeline. Set the appropriate variables *before* the February 13, 2025 release to validate that the new enforced rules do not introduce blockers.

* **Java 17 and Java 21 build support:** Customers can now build with Java 17 or Java 21, gaining access to performance enhancements and new language features. For configuration steps, including updating your Maven project and library versions, see [Build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md). When the build version is set to Java 17 or Java 21, the runtime deployed is Java 21.

    * **Feature enablement**
        * This feature will be enabled for all customers on Thursday, February 13, 2025, coinciding with the default rollout of the new SonarQube version.
        * Customers can enable it *immediately* by setting the two variable configurations describe above for upgrading the SonarQube 9.9 version.

    * **Java 21 runtime deployment**
        * The Java 21 runtime is deployed when building with Java 17 or Java 21.
        * Gradual rollout to all Cloud Manager environments begins in February for sandboxes and development environments and extends to production environments in April.
        * Customers who want to adopt the Java 21 runtime *earlier* can contact Adobe at [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com).


<!-- ## Early adoption program {#early-adoption}

Be a part of Cloud Manager's early adoption program and have a chance to test upcoming features. -->

<!-- ## Bug fixes -->




<!-- ## Known issues {#known-issues} -->
