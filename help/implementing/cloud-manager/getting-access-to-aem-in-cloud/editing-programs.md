---
title: Editing Programs
description: Learn how to edit your production and sandbox programs to adjust their options after you have created them.
exl-id: 819e4a6e-f77a-4594-a402-a300dcbdf510
---

# Managing and Editing Programs {#editing-programs}

The **My Programs** page provides an overview of all programs to which you have access. When selecting an individual program, the **Program Overview** page provides details of the program at a glance. 

From the **Program Overview**, users with the requisite permissions can edit [production programs created in your organization](creating-production-programs.md) and [sandbox programs created in your organization.](creating-sandbox-programs.md) By editing a program, you can:

* Add Sites solution to an existing program with Assets and conversely.
* Remove Sites or Assets from an existing program with both Sites and Assets.
* Add a second, unused solution entitlement, to either an existing program or as a new Program.
* Delete sandbox programs.

## Permissions {#permissions}

You must be a member of the **Business Owner** role to edit programs or delete sandbox programs as well as to access the License Dashboard.

## My Programs {#my-programs}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. The **My Programs** page shows a list of all programs to which you have access as tiles.

![My Programs page](/help/implementing/cloud-manager/assets/my-programs.png)

### Call-to-Action {#cta}

At the top of the page is a call-to-action relevant to the status of your organization. For example, if you have successfully set up your programs, statistics of your activities over the past 90 days might show, including:

* Number of [deployments](/help/implementing/cloud-manager/deploy-code.md)
* Number of [code quality issues](/help/implementing/cloud-manager/code-quality-testing.md) identified
* Number of builds

Or if you are just beginning the setup of your org, there might be tips on next steps or documentation resources.

### Programs Tab {#programs-tab}

The **Programs** tab lists cards representing each program to which you have access. Tap or click on a card to access the **Program Overview** page of the program for details about the program.

Use the sorting options to better find the program you need.

![Sorting options](/help/implementing/cloud-manager/assets/my-programs-sorting.png)

* Sort by
  * Date Created (default)
  * Program Name
  * Status
* Ascending (default) / Descending
* Grid View (default)
* List View

### License Tab {#license-tab}

The **License** tab gives you quick access to the [License Dashboard.](/help/implementing/cloud-manager/license-dashboard.md)

## Program Overview {#program-overview}

Once you have selected a program from the **[My Programs](#my-programs)** page, Cloud Manager opens the **Program Overview** page for the selected program.

![Program Overview page](/help/implementing/cloud-manager/assets/program-overview.png)

Tap or click the program name at the top-left corner of the page to quickly switch to another program or back to the **[My Programs](#my-programs)** page. You can also [edit the selected program](#editing) or [add a program.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md)

![Program switcher](/help/implementing/cloud-manager/assets/program-switcher.png)

The call-to-action at the top will give you helpful information depending on the status of your program. For a new program you may see next steps offered as well as a reminder of a go-live date, [set during program creation.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md)

![Call-to-action for a new program](/help/implementing/cloud-manager/assets/info-banner-new-program.png)

For a live program, the status of your last deployment with links for details and starting a new deployment.

![Call-to-action](/help/implementing/cloud-manager/assets/info-banner.png)

**Environments** and **Pipelines** cards give a quick overview of both within the selected program.

![Cards](/help/implementing/cloud-manager/assets/environments-pipelines.png)

The **Performance** card gives an overview of the **[CDN Dashboard.](/help/implementing/cloud-manager/cdn-performance.md)**

![Performance card](/help/implementing/cloud-manager/assets/cdn-performance-dashboard.png)

## Editing a Program {#editing}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](#my-programs)** page, click the program that you want to edit to show its details.

1. Click your program's name in the upper-left of the page and select **Edit program**.

   ![Edit program option](assets/edit-program-overview.png)

1. The **Edit Program** page opens to the **General** tab.

   ![General tab](assets/edit-program-prod1.png)

1. The options available for editing the program are the same as those when creating the program.
   * Please see the documents [Creating Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md) and [Creating Sandbox Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md) for details on the individual options. 
   * [Additional options](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#options) may be available for your production program depending on the entitlements of your organization.

1. Click **Update** to save your changes to the program.

The changes to the program are saved.

>[!NOTE]
>
>Anytime a program is edited, including adding or removing a solution or add-on, those changes take effect following the next deployment.

## Deleting Sandbox Programs {#delete-sandbox-program}

Deleting a sandbox program removes all environments and pipelines associated with it.

>[!TIP]
>
>Users with the **Business Owner** or **Deployment Manager** roles can alternatively delete their production and stage environments instead of the entire sandbox program. 

To delete a sandbox program, do the following.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](#my-programs)** page, click the program that you want to edit to show its details.

1. Click your program's name in the upper-left of the page and select **Delete Program**.

   ![Delete program option](assets/delete-sandbox1.png)

Alternatively you can click the ellipsis button on your program's card from the Cloud Manager overview page and select **Delete Program**.

![Delete sandbox from program card](assets/delete-sandbox2.png)

>[!NOTE]
>
>Only sandbox programs can be deleted. Production programs cannot be deleted.
