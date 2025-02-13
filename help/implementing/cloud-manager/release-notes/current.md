---
title: Release Notes for Cloud Manager 2025.2.0 in Adobe Experience Manager as a Cloud Service
description: Learn about the release of Cloud Manager 2025.2.0 in AEM as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2025.2.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/pages/viewpage.action?pageId=3389843928 -->

Learn about the release of Cloud Manager 2025.2.0 in AEM (Adobe Experience Manager) as a Cloud Service.


See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.2.0 in AEM as a Cloud Service is Thursday, February 13, 2025. 

The next planned release is Thursday, March 13, 2025.
 
## What's new {#what-is-new}

* **Update to code quality rules.** 
    Starting Thursday, February 13, 2025, the Cloud Manager code quality step now uses an upgraded SonarQube version 9.9.5.90363.

    The updated rules, available for Cloud Manager on AEM as a Cloud Service at [this link](/help/implementing/cloud-manager/code-quality-testing.md#understanding-code-quality-rules), determine security scores and code quality for Cloud Manager pipelines. This update may impact your quality gates, potentially blocking deployments.

* **Java 17 and Java 21 build support.** 

    Customers can now build with Java 17 or Java 21, gaining access to performance enhancements and new language features. For configuration steps, including updating your Maven project and library versions, see [Build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md). When the build version is set to Java 17 or Java 21, the runtime deployed is Java 21.

    * **Feature enablement**
        * This feature will be enabled for all customers on Thursday, February 13, 2025, coinciding with the default rollout of the new SonarQube version.
        * Customers can enable it *immediately* by setting the two variable configurations described above for upgrading the SonarQube 9.9 version.

    * **Java 21 runtime deployment**
        * The Java 21 runtime is deployed when building with Java 17 or Java 21.
        * Gradual rollout to all Cloud Manager environments begins in February for sandboxes and development environments and extends to production environments in April.
        * Customers building with Java 11 who wish to adopt the Java 21 runtime *earlier* can contact Adobe at [aemcs-java-adopter@adobe.com](mailto:aemcs-java-adopter@adobe.com).

* **99.99% uptime reporting for Edge Delivery Services.**
    High-availability 99.99% uptime reporting is now available for qualifying Edge Delivery Services programs. To enable this feature, customers must successfully onboard their Edge Delivery Services sites and apply their 99.99% Service Level Agreement (SLA) within Cloud Manager.

    See also [SLA](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#sla).

* **Improved user invitation experience for Edge Delivery Services.**
    Improvements were made to the experience with inviting users to the content repository associated with Edge Delivery Services. <!-- CMGR-65331 -->

* **Automatic creation of Admin profiles on publish instances.**
    Previously, Cloud Manager allowed for the manual creation of admin profiles on publish instances but did not support automatic creation by default. With this update, admin profiles are now automatically created on publish instances, improving usability and reducing setup time for customers.
    
    For more details, see [Custom Permissions](/help/implementing/cloud-manager/custom-permissions.md).

    ![Pipeline activities filtering](/help/implementing/cloud-manager/release-notes/assets/product-profiles.png)

* **Transition to OAuth for Cloud Service environments.**
    New Cloud Service environments now use OAuth-based service-to-service authentication for Adobe Developer Console integration projects instead of the previously used JWT authentication method. JWT authentication is deprecated and is planned for end-of-life in June 2025.

* **Support for EC (Elliptic Curve) Private Keys (secp384r1).**
    Cloud Manager now supports `secp384r1` Elliptic Curve (EC) private keys, providing improved security and compliance for customer-managed OV/EV SSL certificates. 
    For more details, see [Requirements for customer-managed OV/EV SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md). <!-- CMGR-63636 -->

<!--
## Early adoption program {#early-adoption}

Be a part of Cloud Manager's early adoption program and have a chance to test upcoming features. -->


## Bug fixes

* **(UI) Fixed an issue preventing CDN configuration for domains in Cloud Manager.**
    Customers attempting to add a CDN configuration in Cloud Manager encountered a screen error when they selected a domain from the drop-down menu. This user interface bug prevented domain mapping in production environments, blocking the configuration process.

    Additionally, some domains remained inaccessible in the backend, despite being removed from the user interface. This issue led to conflicts with existing CDN configurations. 
    
    With this fix, you can now successfully select a domain from the drop-down without encountering an error. Backend inconsistencies that prevented domain reconfiguration have been addressed. And finally, improved validation now ensures that conflicting domains are properly removed before re-adding them.<!-- CMGR-64888 -->
* **(Backend) Fixed an issue causing SSL expiry notifications to be sent multiple times.**
    A bug was identified where the SSL expiry notification scheduler, which is designed to run once daily at midnight, was incorrectly triggering twice per day-once at midnight and again at 12:30 AM. This issue resulted in multiple redundant notifications being sent regarding expiring SSL certificates.

    The notification scheduler now correctly runs only once per day as intended. And, you no longer receive duplicate SSL expiry notifications. <!-- CMGR-64748 -->




<!-- ## Known issues {#known-issues} -->
