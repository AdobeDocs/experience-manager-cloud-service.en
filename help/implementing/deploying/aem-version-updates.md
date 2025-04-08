---
title: AEM Version Updates
description: Learn how Adobe Experience Manager (AEM) as a Cloud Service uses continuous integration and delivery (CI/CD) to keep your projects on the latest version. 
feature: Deploying
exl-id: 36989913-69db-4f4d-8302-57c60f387d3d
role: Admin
---

# AEM Version Updates {#aem-version-updates}

Learn how Adobe Experience Manager (AEM) as a Cloud Service uses continuous integration and delivery (CI/CD) to keep your projects on the latest version.

## CI/CD {#ci-cd}

AEM as a Cloud Service uses continuous integration and continuous delivery (CI/CD) to ensure that your projects are on the most current AEM version. This process seamlessly updates your production, staging, and development instances without causing any disruption to your users.

>[!NOTE]
> As development instances are already automatically updated, the manual updates for development instances might not be available to _some_ of your programs. This feature is being transitioned to automatic updates.

Before your instances are automatically updated, a new AEM Maintenance release is published 3-5 days in advance. During this period, your development instance might be automatically updated or in case it is available you can optionally [trigger the update for your development instances](/help/implementing/cloud-manager/manage-environments.md#updating-dev-environment). Version updates are automatically applied to your development environments first. If the update is successful, the update process proceeds to your stage and production instances. The development and staging instances act as an automated quality gate, where your custom-written tests are run before the update is applied on your production environment.

### NIMU (Non-Intrusive Maintenance Updates) {#nimu}

Non-Intrusive Maintenance Updates are automatic updates that are applied without involving the customer pipelines. 
Through NIMU, the customer can use the pipeline at any moment, even if an AEM version update is scheduled or in progress and Maintenance Updates will no longer appear in the Customer pipeline execution history, making it easier to follow the history of code deployments.

#### Update Activities

The current AEM version can still be checked for each environment, as before, using the Cloud Manager UI Environments panel. The same quality gates that are used in the pipeline are used by Non-Intrusive Maintenance Updates, including the customer written tests.
A [Cloud Manager UI notification](/help/implementing/cloud-manager/notifications.md) will be sent whenever a Non-Intrusive Maintenance Update is applied to the environments of your program. You can configure it to be also sent to your email.

>[!NOTE]
>
> Note: Non-Intrusive Maintenance Updates will be progressively enabled for all customers in 2024.


## Type of Updates {#update-types}

There are two types of AEM version updates:

* [**AEM Maintenance Updates**](/help/release-notes/maintenance/latest.md)

  * They are mostly for maintenance purposes, including the latest bug-fixes and security updates.
  * It has minimal impact because changes are applied regularly.

* [**AEM Feature Activation**](/help/release-notes/release-notes-cloud/release-notes-current.md)

   * They are released on a predictable, monthly schedule.

>[!NOTE]
>
> Check key dates for monthly releases on the [Experience Manager releases roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html#aem-as-cloud-service) and mark your calendars to prepare yourself for the key activities to get ready for the release.

## Update Failure {#update-failure}

AEM updates go through an intense and fully automated product validation pipeline involving multiple steps, ensuring no disruption of service for any systems in production. Health checks are used to monitor the health of the application. If these checks fail during an AEM as a Cloud Service update, the release does not proceed, and Adobe investigates why the update caused this unexpected behavior. 

When you deploy a new version of custom code on your environment, [Product and Custom functional tests](/help/implementing/cloud-manager/overview-test-results.md#functional-testing) play a crucial role. They ensure that the production systems remain stable and functional even after a change is applied. These tests are also applied in the AEM Version update process.

If the update to the production environment fails, Cloud Manager automatically rolls back the staging environment. This is done automatically to make sure that after an update completes, both the staging and production environments are on the same AEM version.
Similarly, if an automated update of a development environment fails, staging and production environments are not updated.

>[!NOTE]
>
>If custom code was pushed to staging and not to production, the next AEM update removes those changes to reflect the git tag of the last successful customer release to production. Therefore, the custom code that was only available on staging must be deployed again.

## Best Practices {#best-practices}

* **Stage Environment Usage**
  * Use a different environment (not Stage) for long QA/UAT cycles.
  * After sanity testing is completed on Stage, move to verify on Production.

* **Production Pipeline**
  * Pause before deploying to Production.
  * Canceling the pipeline after a Stage deploy indicates that the code is "a throwaway" and not a valid candidate for Production, refer [Configuring a Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md).

* **Non-Production Pipeline**
  * Configure a [Non-Production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#full-stack-code).
  * Accelerate delivery speed/frequency for production pipeline failures. Identify issues in non-prod pipelines by enabling Product Functional Testing, Custom Functional Testing, and Custom UI Testing. 

* **Content Copy**
  * Use [Content Copy](/help/implementing/developing/tools/content-copy.md) to move similar content sets to a non-prod environment.

* **Automated Functional Testing**
  * Include automated testing in your pipeline so you can test critical functionality. 
  * [Customer Functional Testing](/help/implementing/cloud-manager/functional-testing.md#custom-functional-testing) and [Custom UI Testing](/help/implementing/cloud-manager/functional-testing.md#custom-ui-testing) are blocking, if they fail the AEM release does not get rolled out. 

## Regression {#regression}

If you encounter an issue related to regression, submit a support case by way of the Admin Console. If the issue is a blocker and its impacting Production, a P1 should be raised. Provide all details required to reproduce the regression issue.  

## Composite Node Store {#composite-node-store}

Usually, updates incur zero downtime, including for the authoring instance, which is a cluster of nodes. Rolling updates are possible due to [the composite node store feature in Oak](https://jackrabbit.apache.org/oak/docs/nodestore/compositens.html).

This feature allows AEM to reference multiple repositories simultaneously. In a [rolling deployment](/help/implementing/deploying/overview.md#how-rolling-deployments-work), the new AEM version contains its own `/libs` (the TarMK based immutable repository). It is distinct from the older AEM version, although both reference a shared DocumentMK based mutable repository that contains areas like `/content` , `/conf` , `/etc` and others. 

Because both the old and the new versions have their own versions of `/libs`, they can both be active during the rolling update. And, both can take on traffic until the old is fully replaced by the new.

## Further Information {#further-information}

For further details on related themes:

* [Cloud Manager CI/CD Pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md)
* [Cloud Manager UI notification](/help/implementing/cloud-manager/notifications.md)
* [the Architecture of Adobe Experience Manager as a Cloud Service](/help/overview/architecture.md)
