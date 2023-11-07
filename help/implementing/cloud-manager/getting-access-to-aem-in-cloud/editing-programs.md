---
title: Editing Programs
description: Learn how to edit your production and sandbox programs to adjust their options after you have created them.
exl-id: 819e4a6e-f77a-4594-a402-a300dcbdf510
---
# Editing Programs {#editing-programs}

Users with the requisite permissions can edit [production programs created in your organization](creating-production-programs.md) and [sandbox programs created in your organization.](creating-sandbox-programs.md) By editing a program, you can:

* Add Sites solution to an existing program with Assets and conversely.
* Remove Sites or Assets from an existing program with both Sites and Assets.
* Add a second, unused solution entitlement, to either an existing program or as a new Program.
* Delete sandbox programs.

## Permissions {#permissions}

You must be a member of the **Business Owner** role to edit programs or delete sandbox programs.

## Editing a Program {#editing}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click the program that you want to edit to show its details.

1. Click your program's name in the upper-left of the page and select **Edit program**.

   ![Edit program option](assets/edit-program-overview.png)

1. The **Edit Program** page opens. On the **General** tab, edit the program name and description.

   * At least one solution must be selected for a program.

   ![General tab](assets/edit-program-prod1.png)

1. On the **Solutions &amp; Add-ons** tab, modify the solutions for the program.

   ![Select solutions](assets/edit-prg.png)

1. Click the chevron before the solution name to reveal optional add-ons such as selecting the **Commerce** add-on option under **Sites**.

   ![Edit add-ons](assets/edit-program-add-on.png)

1. On the **Go live settings** tab, modify the planned go-live date for the program.

   ![Edit go-live settings](assets/edit-program-go-live.png)

   * This date is for informational use only. It triggers the Go Live widget on the program overview page. In turn, it provides in-product links to Adobe Experience Manager (AEM) as a Cloud Service best practice documentation to align with your journey, culminating in a successful Go Live experience.
   * This tab is not available for sandbox programs.

1. If the required entitlements are available for the program, the **Security** tab will show where you can modify the security options for the program.

   ![Edit security settings](assets/edit-program-security.png)

   * HIPAA can not be enabled or disabled after [program creation.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md)
      * [Learn more](https://www.adobe.com/go/hipaa-ready) about Adobe's HIPAA ready solution implementation.
   * Once activated, WAF-DDOS protection can then be configured by setting up a [non-production pipeline.](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md)
   
   {{waf-limited-release}}

1. Click **Update** to save your changes to the program.

Anytime a program is edited, including adding or removing a solution or add-on, those changes take effect following the next deployment.

## Deleting Sandbox Programs {#delete-sandbox-program}

Deleting a sandbox program removes all environments and pipelines associated with it.

>[!TIP]
>
>Users with the **Business Owner** or **Deployment Manager** roles can alternatively delete their production and stage environments instead of the entire sandbox program. 

To delete a sandbox program, do the following.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click the program that you want to edit to show its details.

1. Click your program's name in the uppper-left of the page and select **Delete Program**.

   ![Delete program option](assets/delete-sandbox1.png)

Alternatively you can click the ellipsis button on your program's card from the Cloud Manager overview page and select **Delete Program**.

![Delete sandbox from program card](assets/delete-sandbox2.png)

>[!NOTE]
>
>Only sandbox programs can be deleted. Production programs cannot be deleted.
