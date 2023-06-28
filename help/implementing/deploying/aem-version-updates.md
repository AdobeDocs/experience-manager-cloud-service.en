---
title: AEM Version Updates
description: Learn how AEM as a Cloud Service uses continuous integration and delivery (CI/CD) to keep your projects on the latest version. 
feature: Deploying
exl-id: 36989913-69db-4f4d-8302-57c60f387d3d
---

# AEM Version Updates {#aem-version-updates}

Learn how AEM as a Cloud Service uses continuous integration and delivery (CI/CD) to keep your projects on the latest version.

## CI/CD {#ci-cd}

AEM as a Cloud Service uses continuous integration and continuous delivery (CI/CD) to ensure that your projects are on the most current AEM version. This means that production and staging instances are updated to the latest AEM version without any interruption of service for users.

Version updates are applied automatically to production and staging instances only. [AEM updates must be applied manually to all other instances](/help/implementing/cloud-manager/manage-environments.md#updating-dev-environment).

## Type of Updates {#update-types}

There are two types of AEM version updates:

* **AEM Maintenance Updates**

  * Can be released on a daily basis.
  * Are mostly for maintenance purposes, including the latest bug-fixes and security updates.
  * Have minimal impact since changes are applied regularly.

* **New Feature Updates**

   * Are released on a [predictable, monthly schedule.](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html)

## Update Failure {#update-failure}

AEM updates go through an intense and fully automated product validation pipeline involving multiple steps, ensuring no disruption of service for any systems in production. Health checks are used to monitor the health of the application. If these checks fail during an AEM as a Cloud Service update, the release will not proceed and Adobe will investigate why the update caused this unexpected behavior. 

[Product tests and Customer functional tests,](/help/implementing/cloud-manager/overview-test-results.md#functional-testing) which prevent product upgrades and customer code pushes from breaking production systems, are also validated during an AEM version update.

If the update to production environment fails, Cloud Manager will automatically roll back the staging environment. This is done automatically to make sure that after an update completes, both the staging and production environments are on same AEM version.

>[!NOTE]
>
>If custom code was pushed to staging and not to production, the next AEM update will remove those changes to reflect the git tag of the last successful customer release to production. Therefore, the custom code that was only available on staging will have to be deployed again.

## Composite Node Store {#composite-node-store}

In most cases, updates will incur zero downtime, including for the authoring instance, which is a cluster of nodes. Rolling updates are possible due to [the composite node store feature in Oak.](https://jackrabbit.apache.org/oak/docs/nodestore/compositens.html)

This feature allows AEM to reference multiple repositories simultaneously. In a [rolling deployment,](/help/implementing/deploying/overview.md#how-rolling-deployments-work) the new AEM version contains its own `/libs` (the TarMK based immutable repository), distinct from the older AEM version, although both reference a shared DocumentMK based mutable repository that contains areas like `/content` , `/conf` , `/etc` and others. 

Because both the old and the new versions have their own versions of `/libs`, they can both be active during the rolling update, and both can take on traffic until the old is fully replaced by the new.
