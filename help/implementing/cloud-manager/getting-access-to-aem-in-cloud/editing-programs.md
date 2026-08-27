---
title: Edit Programs
description: Learn how to edit your production and sandbox programs to adjust their options after you have created them.
exl-id: 819e4a6e-f77a-4594-a402-a300dcbdf510
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
---

# Edit programs {#editing-programs}

To manage and edit programs, start at the [**My Programs** console](/help/implementing/cloud-manager/navigation.md). The **My Programs** page provides an overview of all programs to which you have access. When selecting an individual program, the **Program Overview** page provides an overview of the program details. 

From the **Program Overview**, users with the requisite permissions can edit [production programs created in your organization](creating-production-programs.md) and [sandbox programs created in your organization](creating-sandbox-programs.md). By editing a program, you can do the following:


* Enable or disable **WAF-DDOS Protection** on the **Security** tab.
* Add the Sites solution to an existing program that includes Assets, and add Assets to an existing program that includes Sites.
* Remove Sites or Assets from an existing program that has both Sites and Assets.
* Add an unused solution entitlement to an existing program or create a new program.
* Mark production programs for deletion.
* Delete sandbox programs.

## Permissions {#permissions}

You must have the **Business Owner** role to edit programs, delete sandbox programs, mark production programs for deletion, and access the License Dashboard.

## Edit a program {#editing}

When a program is edited, including adding or removing a solution or add-on, those changes take effect following the next deployment. 

**To edit a program:**

{{sign-in-to-cloud-manager}}

1. On the **My Programs** page, click the program that you want to edit.
1. Near the upper-left corner of the page, click the program's name, then select **Edit program**.

   ![Edit program option on the Program's drop-down menu](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/edit-program.png)

1. In the **Edit Program** dialog box, use the tabs to set the various options you want.

   ![General tab](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/edit-program-dialog-box.png)

   The options available for editing the program are the same as the options for program creation.

   * You can configure whether a publish tier is provisioned for new environments (Beta). See [Flexible Publish Tier (Beta)](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#flexible-publish-tier).
   * See [Create Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md) and [Create Sandbox Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md) for details on the individual options.
   * To enable or disable the Web Application Firewall (WAF) at any time, select the **Security** tab, then check or uncheck the **WAF-DDOS Protection** check box. Checking this box activates the feature, but beyond some automatic Common Vulnerabilities and Exposures (CVE) protection, you must deploy the WAF rules through Cloud Manager for full protection. If WAF rules are licensed but this check box is not checked, the feature is not active. For more information, see [Traffic Filter Rules including WAF Rules](/help/security/traffic-filter-rules-including-waf.md).

      >[!NOTE]
      >To confirm the feature is active, inspect the [CDN logs](//help/security/traffic-filter-rules-including-waf.md#cdn-logs) once traffic is flowing to the site. Look for log entries that include a `rules` property containing a `waf` attribute. For example,
      >
      >`"rules": "*waf=*"`
      >
      >This attribute appears once WAF is active, even before any WAF rules are deployed.

      ![Edit Program dialog box showing Security tab options](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/cmk-edit-programs.png)

   * On the same **Security** tab, you can enable **Customer Managed Keys** for an existing program.

      CMK cannot be disabled after activation. After enabling CMK, configure your encryption keys in Experience Hub. See [Configure CMK in Experience Hub](#configure-cmk-experience-hub).
 
   * [Additional options](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#options) are available for your production program depending on the entitlements of your organization.
   
1. Click **Update** to save your changes.

## Configure CMK in Experience Hub {#configure-cmk-experience-hub}

After CMK is enabled for a program, Cloud Manager provides a direct link to the CMK configuration page in Experience Hub so you can configure your
encryption keys while remaining in your program.

Once CMK has been successfully configured for an environment, the Environment details page displays a **CMK configuration** status badge. If CMK is enabled for the program but has not yet been configured for a specific environment, the badge does not appear on that environment's details page.

**To configure CMK in Experience Hub:**

1. On the **My Programs** page, locate the program card with CMK enabled.
2. Click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg), then click **Configure CMK**.

      ![Program card showing CMK icon to indicate enabled, then the Configure CMK option from the ellipsis menu](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/cmk-configure-edit-program-dlg.png)

   Experience Hub opens the CMK configuration page where you can supply your Azure Key Vault details and encryption key information.

   For full configuration steps, see [Customer Managed Keys Setup for AEM as a Cloud Service](/help/security/customer-managed-keys.md).

## Mark a production program for deletion {#delete-production-program}

Deleting a production program is a two-phase process. A Business Owner marks the program for deletion, which triggers a validation and removal period. The program is then permanently removed after the takedown period has elapsed.

When a production program is marked for deletion, the following occurs:

* The credit associated with the production program is returned to the customer.
* All environments belonging to the production program are removed.

Before marking for deletion is initiated, the system validates whether the production program is eligible for deletion. If the marking fails, the production program moves to a `Failed to mark for deletion` state instead.

>[!NOTE]
>
>Sandbox programs are unaffected by this process. To delete a sandbox program, see [Delete a sandbox program](#delete-sandbox-program).

**To mark a production program for deletion:**

{{sign-in-to-cloud-manager}}

1. On the **My Programs** page, for the production program that you want to mark for deletion, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg), then click **Delete program**.

   ![Selecting Delete Program from the drop-down list of a production program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/production-program-markfordelete1.png)*Example production program seen above is for illustration purposes only.*

1. In the **Mark production program for deletion** dialog box, review the warning that lists the resources connected to your program, including production, stage, and development environments.

   ![Delete Production Program dialog box](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/production-program-markfordelete2.png)


   >[!NOTE]
   >
   >If the production program has blocking resources, such as environments that are currently updating, the **Mark for deletion** button is disabled. Wait until all program resources are unlocked before you can mark the program for deletion.
   >
   >![The Mark production program for deletion dialog box showing that the program cannot be deleted because it has blocking resources](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/production-program-markfordelete2b.png)


1. To confirm, type the program name as displayed in the dialog box, then click **Mark for deletion**.

   After confirmation, the production program shows a **Marking for deletion** status while the process runs.

   ![Marking for deletion status](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/production-program-markfordelete3.png)

   When complete, the production program card updates to **Marked for deletion** with an associated Alert badge.

   ![Marked for deletion status with associated Alert badge](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/production-program-markfordelete4.png)  

1. Click the Alert badge on the production program card to display the scheduled permanent removal date.

   ![Display of the scheduled permanent removal date of the production program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/production-program-markfordelete5.png)

   After the removal period has elapsed, the program is permanently removed and cannot be restored.

### Cancel the deletion of a production program {#unmark-from-deletion}

You can restore a production program that has been *marked* for deletion as long as the permanent removal has not yet occurred. 

>[!IMPORTANT]
>
>Restoring a production program that was marked for deletion requires that the customer has available credits.

**To cancel the deletion of a production program:**

1. On the **My Programs** page, locate the production program card that shows **Marked for deletion**.

1. On the production program card, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg), then click **Unmark for deletion**.

   ![Unmarking the scheduled permanent removal date of the production program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/assets/production-program-unmarkfordelete6.png) 

   The production program deletion is canceled.

## Delete a sandbox program {#delete-sandbox-program}

Deleting a sandbox program removes all environments and pipelines associated with it.

>[!TIP]
>
>Users with the **Business Owner** or **Deployment Manager** roles can delete their production and stage environments instead of the entire sandbox program. 

**To delete a sandbox program:**

{{sign-in-to-cloud-manager}}

1. On the **[My Programs](#my-programs)** page, click the sandbox program that you want to delete to show its details.

1. Click your sandbox program's name in the upper-left of the page and select **Delete Program**.

   ![Delete program option](assets/delete-sandbox1.png)

Alternatively, you can click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) on your sandbox program's card from the Cloud Manager overview page and select **Delete Program**.

   ![Delete sandbox from program card](assets/delete-sandbox2.png)
