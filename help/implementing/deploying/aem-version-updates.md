---
title: AEM Version Updates
description: AEM Version Updates 
feature: Deploying
exl-id: 36989913-69db-4f4d-8302-57c60f387d3d
---

# AEM Version Updates {#aem-version-updates}

## Introduction {#introduction}

AEM as a Cloud Service now uses continuous integration and continuous delivery (CI/CD) to ensure that your projects are on the most current AEM version. This means that production and stageing instances are updated to the latest AEM version without any interruption of service for users. 

>[!NOTE]
>
>If the update to production environment fails, Cloud Manager will automatically roll back the staging environment. This is done automatically to make sure that after an update completes, both the staging and production environments are on same AEM version.
 
There are two types of AEM version updates:

* **AEM Maintenance Updates**

  * Can be released on a daily basis.
  * Are mostly for maintenance purposes, including the latest bug-fixes and security updates.
  * Have minimal impact since changes are applied regularly.

* **New Feature Updates**

   * Are released via a predictable monthly schedule.

AEM updates go through an intense and fully automated product validation pipeline involving multiple steps, ensuring no disruption of service for any systems in production. Health checks are used to monitor the health of the application. If these checks fail during an AEM as a Cloud Service update, the release will not proceed and Adobe will investigate why the update caused this unexpected behavior. 

[Product tests and Customer functional tests,](/help/implementing/cloud-manager/overview-test-results.md#functional-testing) which prevent product upgrades and customer code pushes from breaking production systems, are also validated during an AEM version update.

>[!NOTE]
>
>If custom code was pushed to staging and then rejected by you, the next AEM update will remove those changes to reflect the git tag of the last successful customer release to production.

## Composite Node Store {#composite-node-store}

Updates in most cases will incur zero downtime, including for the authoring instance, which is a cluster of nodes. Rolling updates are possible due to the composite node store feature in Oak. 

This feature allows AEM to reference multiple repositories simultaneously. In a rolling deployment, the new green AEM version contains its own `/libs` (the TarMK based immutable repository), distinct from the older blue AEM version, although both reference a shared DocumentMK based mutable repository that contains areas like `/content` , `/conf` , `/etc` and others. Because both the blue and the green have their own versions of `/libs`, they can both be active during the rolling update, both taking on traffic until the blue is fully replaced by the green.
