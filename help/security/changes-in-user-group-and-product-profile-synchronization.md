---
title: Changes in User Group and Product Profile Synchronization
description: Learning about the changes in user group and product profile synchronization coming to AEM as a Cloud Service
feature: Security
role: Admin
hide: yes
hidefromtoc: yes
---

# Changes in User Group and Product Profile Synchronization {#changes-in-user-group-and-product-profile-synchronization}

Whenever a user logs into AEM as a Cloud Service or an access token is used, Adobe Admin Console user groups, product profiles, and product profile services are synchronized into the AEM repository as groups.

On January 28th, in order to reduce UI clutter and to optimize performance, there will be some changes to the synchronization behavior, resulting in fewer groups appearing in AEM. Two categories of AEM groups will be removed:

1. AEM Groups with Suffix `GROUP_NAME_SUFFIX`. These groups do not appear in the Adobe Developer Console, but appear in the AEM Group Management screen, as shown below. In the unlikely case that your AEM application references these groups, make sure to use Adobe Admin Console user groups instead.

   ![Removed groups 1](/help/security/assets/removed-groups-1.png)

1. AEM groups associated with Adobe Admin Console product profiles unrelated to the specific AEM tier or environment combination (for example, `author` or `e4535`). This may include product profiles that are:

   * related to other Adobe products
   * related to other AEM programs
   * related to other AEM environments in the same AEM program
   * related to a different tier (for example, `author` vs `publish`) in the same AEM environment
   * related to Cloud Manager (for example, `Business Owner - Cloud Service`)

   For example, in the image below, there are many rows with the pattern `AEM Administrators-<suffix>` or `AEM Users-<suffix>` where the suffix is not related to the current environment.

   ![Removed groups 2](/help/security/assets/removed-groups-2.png)

You can check which suffix is related to the current environment by selecting Manage **Access - Author Profiles** (or **Publish Profiles**) in the environment's action menu in Cloud Manager. 

![Check suffixes](/help/security/assets/suffix-check.png)

This will navigate to the Adobe Admin Console, as depicted in the screenshot below. Note that the `<suffix>` may be either a random set of characters or rather the tier, and program and environment ids (for example, `author - Program 12345 - Environment 45678`).

![Suffixes in the Admin Console](/help/security/assets/admin-console-profile-suffixes.png)

In the unlikely case that your AEM application references these groups, make sure to use Adobe Admin Console user groups instead. 

>[!NOTE]
>
>In particular, watch out for these potential pitfalls: 
>
>1. Your AEM application relies on an AEM group that was synchronized from a Cloud Manager product profile
>1. Your AEM application's publish tier relies on an AEM group that was synchronized from an author tier product profile. This is also true for the inverse scenario (author tier relying on publish tier). 