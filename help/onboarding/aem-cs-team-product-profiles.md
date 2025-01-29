---
title: AEM as a Cloud Service Team and Product Profiles
description: Learn how AEM as a Cloud Service team and product profiles can grant and limit access to your licensed Adobe solutions.
exl-id: 7b1474c9-aca0-4354-8798-1abdcda2f6dd
feature: Onboarding
role: Admin, User, Developer
---

# AEM as a Cloud Service Team and Product Profiles {#product-profiles}

Learn how AEM as a Cloud Service team and product profiles can grant and limit access to your licensed Adobe solutions.

## Product Profiles {#profiles}

When granting a user access to a specific Adobe solution, you do not necessarily want to give them full access. Product profiles enable each solution to have its own set of user permissions. These are available and accessible via the [Admin Console](/help/journey-onboarding/admin-console.md).

The Adobe Admin Console has a structured hierarchy of product, product instances, and product profiles where an organization's internal users can be assigned membership, giving them access to the solutions and features that have been licensed. 

<!-- Alexandru: Drafting for now 

Your AEM as a Cloud Service team members are added and assigned to one or more of the following product profiles via the Admin Console during onboarding.

* **AEM Administrators**: An AEM administrator is typically assigned to developers, in particular developers who need access to, for example, the development environments. The AEM administrator's product profile is used to grant administrator privileges in the associated AEM instance.

* **AEM Users**: AEM users are the users in your organization who use AEM as a Cloud Service generally to create content. These users need to access AEM to do their tasks. The AEM users product profile is typically assigned to an AEM content author who creates and reviews the content. This content can be of many types such as pages, assets, publications, and so on. The AEM users product profile shown below is assigned to these members.

![Product profiles](/help/onboarding/assets/admin-console-profiles.png) -->

## AEM as a Cloud Service Product Profiles {#aem-product-profiles}

AEM as a Cloud Service is a fully cloud-native offering that delivers AEM as a service. It delivers AEM in a cloud native manner, with new attributes like always on, always current, always secure, and always at scale. At the same time, it retains the main value proposition that AEM provides as a customizable platform to customers and allows enterprise grade teams to integrate in their development and delivery procedure. See [Introduction to Adobe Experience Manager as a Cloud Service](/help/overview/introduction.md) to learn more about AEM as a Cloud Service.

### Organization Level Product Instances {#org-level-product-instances}

>[!NOTE]
>
> Some of the Product Instances and Product Profiles described in this article may only appear for newly created environments. A future mechanism will allow existing environments to be updated as well.

When Adobe processes the licensing of an AEM solution for the first time, two Product Instances will appear in Adobe Admin Console, under the Adobe Experience Manager as a Cloud Service Product:

* **AEM Org-Level** - contains one or more Product Profile that represent access to features that are scoped to all AEM environments, rather than just to a single one
* **Cloud Manager** - contains Product Profiles corresponding to different levels of access to Cloud Manager features.

<!--
>[!NOTE]
>
>For existing programs, the AEM Org-Level Product Instance is created upon selecting the **Update product** profiles action for a given environment.
-->

![Org Level Product Instances](/help/onboarding/assets/orglevel.png)

Inside the AEM Org-Level Product Instance is a Product Profile named AEM Org-Level Reporters, which is not used at this time, but may be in the future to represent access to retrieving information about AEM product licenses.

When a Forms Communication Solution is licensed, a corresponding product profile will appear under the AEM Org-level Product Instance as well. 

![Reporters Product Profile](/help/onboarding/assets/org-level-reporters.png)

### Environment and Tier Level Product Instances {#environment-and-tier-level-product-instances}

Upon provisioning new programs with one or more AEM environments, two Product Instances will appear per environment, containing Product Profiles for author and publish, respectively.

![Environment Product Instances](/help/onboarding/assets/env-productinstances.png)

Below are the Product Profiles in an author Product Instance, for an organization that has provisioned an environment in a program containing AEM Sites:

![Sites Product Instances](/help/onboarding/assets/sites-product-instances.png)

The following table describes a list of the possible Product Profiles below an environment-tier-specific Product Instance.

<table style="table-layout:auto">
    <tr>
        <th>Product Instance</th>
        <th>Naming Convention</th>
        <th>Default Service</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>AEM Author</td>
        <td>AEM Sites Content Managers - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Sites Content Managers</td>
        <td>
            <ul>
                <li>Intended for controlled access to AEM Sites author features on this environment. Users in this Product Profile will be members of the AEM Sites content author AEM group, that is automatically created in AEM. The AEM group permissions should be configured in AEM with the desired access level.</li><br>
                <li>If the default service remains selected
                    <ul>
                        <li>users in this product profile will also be members of the "AEM Sites Content Managers - Service" AEM group.</li>
                      <!--  <li>users in this product profile will have access to AEM Sites Content Management API.</li>
                        <li>an Adobe Developer Console API OAuth S2S project containing AEM Sites Content Management API can optionally be scoped to this environment.</li>-->
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td></td>
        <td>AEM Administrators - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Administrators</td>
        <td>
            <ul>
                <li>Intended for unrestricted access to AEM author and publish environment features. Users in this product profile will be members of the AEM Administrators author AEM group automatically created in AEM.</li><br>
                <li>If the default service remains selected
                    <ul>
                        <li>users in this product profile will also be members of the "AEM Administrators - Service" AEM group</li>
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td></td>
        <td>AEM Users - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Users</td>
        <td>
            <ul>
                <li>Intended for very limited access to AEM author environment features. Users in this product profile will be members of the "Contributors" AEM group automatically created in AEM</li><br>
                <li>If the default service remains selected
                    <ul>
                        <li>users in this product profile will also be members of the "AEM Users - Service" AEM group</li>
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td></td>
        <td>AEM Reporters - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Reporters</td>
        <td>
            <ul>
                <li>Not currently used, but in the future may provide access to reporting information about the author tier  for this environment.</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td></td>
        <td>AEM Assets Collaborator - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Assets Collaborator Users</td>
        <td>
        <ul>
                <li>Intended for read-only access to the DAM. Users in this product profile will be members of the "Contributors" AEM group automatically created in AEM.
                </li>
                <li>
                Also, it provides the Adobe Express entitlements to create asset variations.
                </li>
          <ul>
    </tr>
    <tr>
        <td></td>
        <td>AEM Assets Power User - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Assets Power Users</td>
<td>
        <ul>
                <li>Intended for read-only access to the DAM. Users in this product profile will be members of the "Contributors" AEM group automatically created in AEM.
                </li>
                <li>
                Also, it provides the Adobe Express entitlements to create asset variations.
                </li>
          <ul>
</td>
    </tr>
    <tr>
        <td></td>
        <td>AEM Forms Content Managers - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Forms Content Managers</td>
        <td>
            <ul>
                <li>Intended for controlled access to AEM Forms author features on this environment. Users in this Product Profile will be members of the AEM Forms forms-users AEM group, that is automatically created in AEM.</li><br>
                <li>If the default service remains selected
                    <ul>
                        <li>users in this product profile will also be members of the "AEM Forms Content Managers - Service" AEM group.</li>
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td></td>
        <td>AEM Forms Developers - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Forms Developers</td>
        <td>
            <ul>
                <li>Intended for controlled access to AEM Forms author features on this environment. Users in this Product Profile will be members of the AEM Forms forms-power-users AEM group, that is automatically created in AEM. These users have the rights to upload XDPs and author Form Data Models also in addition to normal form authoring tasks.</li><br>
                <li>If the default service remains selected
                    <ul>
                        <li>users in this product profile will also be members of the "AEM Forms Developers - Service" AEM group.</li>
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td></td>
        <td>AEM Forms Communications Service Users - author - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Forms Communications Service Users</td>
        <td>
            <ul>
                <li>Intended for controlled access to AEM Forms Communications Services features on this environment. Users in this Product Profile will be members of the AEM Forms forms-users AEM group, that is automatically created in AEM.</li><br>
                <li>If the default service remains selected
                    <ul>
                        <li>users in this product profile will also be members of the "AEM Forms Communications Service Users - Service" AEM group.</li>
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>AEM Publish</td>
        <td>AEM Users - publish - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Users</td>
        <td>
            <ul>
                <li>Intended for very limited access to AEM author environment features. Users in this product profile will be members of the "contrib" AEM group automatically created in AEM</li><br>
                <li>If the default service remains selected
                    <ul>
                        <li>users in this product profile will also be members of the "AEM Users - Service" AEM group.</li>
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
    <tr>
        <td></td>
        <td>AEM Reporters - publish - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Reporters</td>
        <td>
            <ul>
                <li>Not currently used, but in the future may provide access to reporting information about the publish tier for this environment.</li>
            </ul>
        </td>
    </tr>
   <tr>
        <td></td>
        <td>AEM Forms Communications Service Users - publish - Program <code>id</code> - Environment <code>id</code></td>
        <td>AEM Forms Communications Service Users</td>
        <td>
            <ul>
                <li>Intended for controlled access to AEM Forms Communications Services features on this environment. Users in this Product Profile will be members of the AEM Forms forms-users AEM group, that is automatically created in AEM.</li><br>
                <li>If the default service remains selected
                    <ul>
                        <li>users in this product profile will also be members of the "AEM Forms Communications Service Users - Service" AEM group.</li>
                    </ul>
                </li>
            </ul>
        </td>
    </tr>
</table>

Note that each Product Profile has an associated Product Profile Service enabled by default. Unless you have complex access requirements, it is recommended to keep just the Default Service selected. A corresponding AEM group will be created in AEM with the naming convention `<Product Profile Prefix> - Service` (for example, **AEM Sites Content Managers - Service**), and the users in the parent product profiles will automatically become members of that corresponding AEM group.

The AEM group in AEM associated with the service will have the aggregated set of users that exist in all the associated Product Profiles of that service for that environment-tier combination.

![Services](/help/onboarding/assets/services.png)

The following image represents the AEM groups reflecting the AEM Sites Content Managers author tier Product Profile and service.

![AEM Group to Service mapping](/help/onboarding/assets/profile-to-service-mapping.png)

>[!NOTE]
>
>Every user assigned to an AEM as a Cloud Service product profile has read-only access to Cloud Manager via the **Cloud Manager User** role.
>
>Users with only the **Cloud Manager User** role can log into Cloud Manager and navigate to the AEM author environments (if they exist) by using the **Programs** menu options. The **Cloud Manager User** role is not sufficient to access program details. If such access is needed, users must be granted additional roles by their system administrator.

>[!WARNING]
>
>The **AEM Administrators** product profile name must not be changed. Changing the name of the **AEM Administrators** product profile will remove administrator rights from all users assigned to that profile.

>[!TIP]
>
>* To learn more about AEM product profiles, see [Assigning AEM Product Profiles](/help/journey-onboarding/assign-profiles-aem.md).
>* For more information on the onboarding process, see [onboarding journey](/help/journey-onboarding/overview.md).

### Adding Product Profiles for Existing Environments {#adding-product-profiles-for-existing-environments}

Environments created before early November 2024 may be missing the Org-Level product instance described in sections above, as well as certain product profiles. Existing product profiles will also be missing the service toggles. It is recommended to update those product profiles, which is a prerequisite for accessing some future APIs. 

If one or more environments in a program needs its product profiles updated, Cloud Manager will show the notice below. Note that an environment must be on the latest AEM version before its product profiles can be updated.

![Modernize Product Profiles](/help/onboarding/assets/modernize-product-profiles.png)

Clicking the **Add Product Profiles** button will open a menu that displays options to add new product profiles to all environments available in the program or individual environments.

![Replace Environments](/help/onboarding/assets/choose-env-r.png)

Click **All Environments** to add the new product profiles to all environments in the program. Alternatively, click **Individual Environments** to add the new product profiles to selected environments; this navigates the user to an Environments listing page, where an **Add Product Profiles** action can be selected from the **More Options** icon.

![Individual Environments](/help/onboarding/assets/individual-environments.png)
            
You can also add product profiles to selected environments by navigating to the Program Overview page's Environments section, clicking the More Options icon corresponding to an environment, and selecting Add Product Profiles.

The status of the environment displays Adding Product Profiles while the new product profiles are being added and subsequently displays Running when the process is complete.


## Cloud Manager Product Profiles {#cloud-manager-product-profiles}

Cloud Manager has pre-configured product profiles which can be thought of as role-based permissions. Your system administrator is responsible for setting up your Cloud Manager team by assigning them to these product profiles.

>[!TIP]
>
>See [Role Based Permissions in Cloud Manager](/help/onboarding/cloud-manager-introduction.md#role-based-permissions) for more details.

Each of the product profiles have specific permissions associated with them. 

* **Business Owner**
  * In this role you have the permission to add a new program or edit a program, add or update an environment, deploy code to AEM environment, or execute code quality checks.
  * This user is responsible for defining KPIs, approving production deployments, and overriding important 3-tier failures when necessary.
* **Deployment Manager**
  * In this role, you have the permission to add or update an environment, run any pipeline, and deploy code to AEM environment, or execute code quality checks.
  * This user manages deployment operations and uses Cloud Manager to execute staging/production deployments, edit CI/CD pipelines, approve important 3-tier failures when necessary, and can access the git repository.
* **Developer**
  * In this role, you have the permission to generate personal access tokens to access git.
  * This user develops and tests custom application code and primarily uses Cloud Manager to view deployment status and can access the git repository for code commits.
* **Program Manager**
  * In this role, you have the permission to schedule pipelines, override the 3-tier quality gates, and provide production approval.
  * This user uses Cloud Manager to perform team setup, review status, view KPIs, and can approve important 3-tier failures when necessary.

A user can be assigned to multiple product profiles. For example, assigning both **Business Owner** and **Deployment Manage**r roles to a user gives them the sum of these permissions. 

Your Cloud Manager team will include at least:

* One **Business Owner**,  who is typically also the system administrator, and must be the first person to login and access Cloud Manager 
* One **Deployment Manager**
* One **Developer**

>[!NOTE]
>
>To be granted access to AEM as a Cloud Service, users must belong to one of two product profiles: `AEM Users` or `AEM Administrators`. Permissions to administer Cloud Manager will not suffice.

>[!TIP]
>
>* To learn more about Cloud Manager product profiles, see [Assigning Team Members to Cloud Manager Product Profiles](/help/journey-onboarding/assign-profiles-cloud-manager.md).
>* For more information on the onboarding process, see [onboarding journey](/help/journey-onboarding/overview.md).
