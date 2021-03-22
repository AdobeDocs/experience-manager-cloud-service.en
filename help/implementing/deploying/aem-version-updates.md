---
title: AEM Version Updates
description: AEM Version Updates 
feature: Deploying
---

# AEM Version Updates {#aem-version-updates}

## Introduction {#introduction}

AEM as a Cloud Service now uses Continuous Integration and Continuous Delivery (CI/CD) to ensure  that your projects are on the most current AEM version. This means that Production and Stage instances are updated to the latest AEM version without any interruption of service for users. 

>[!NOTE]
>If the update to production environment fails, Cloud Manager will automatically rollback the stage environment. This is done automatically to make sure that after an update completes, both stage and production environments are at on same AEM version.
 
AEM version updates are of two types:

* **AEM Push updates**

   * Can be released on a daily basis.

   * Mostly maintenance, including the latest bug-fixes and security updates.

     As changes are applied regularly the impact is incremental, reducing the impact on your service.

* **New Feature updates**

   * Released via a predictable monthly schedule.

AEM updates go through an intense and fully automated product validation pipeline involving multiple steps ensuring no disruption of service for any systems in production. Health checks are used to monitor the health of the application. If these checks fail during an AEM as a Cloud Service update, the release will not proceed and Adobe will investigate why the update caused this unexpected behavior. 

[Product tests and Customer functional tests](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/understand-test-results.html#functional-testing) which prevent product upgrades and customer code pushes from breaking production are also validated during an AEM version update.

>[!NOTE]
>
>If custom code was pushed to staging and then rejected by you, the next AEM update will remove those changes to reflect the git tag of the last successful customer release to production.

## Composite Node Store {#composite-node-store}

As mentioned above, updates in most cases will incur zero downtime, including for the author, which is a cluster of nodes. Rolling updates are possible due to the *composite node store* feature in Oak. 

This feature allows AEM to reference multiple repositories simultaneously. In a rolling deployment, the new Green AEM version contains its own `/libs` (the TarMK based immutable repository), distinct from the older Blue AEM version, although both reference a shared DocumentMK based mutable repository that contains areas like `/content` , `/conf` , `/etc` and others. Because both the Blue and the Green have their own versions of `/libs`, they can both be active during the rolling update, both taking on traffic until the blue is fully replaced by the green.
 
