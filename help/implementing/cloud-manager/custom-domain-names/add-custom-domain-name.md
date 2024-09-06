---
title: Add a Custom Domain Name
description: Learn how to add a custom domain name using Cloud Manager.
exl-id: 0fc427b9-560f-4f6e-ac57-32cdf09ec623
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add a custom domain name {#adding-cdn}

Learn how to add a custom domain name using Cloud Manager.

## Requirements {#requirements}

Fulfill these requirements before adding a custom domain name in Cloud Manager.

* You must have added a domain SSL certificate for the domain you wish to add before adding a custom domain name as described in the document [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md).
* You must have the **Business Owner** or **Deployment Manager** role to add a custom domain name in Cloud Manager.
* Be using the Fastly CDN.

## Where to add custom domain names {#where}

You can add a custom domain name from two locations in Cloud Manager:

* [From the Domain Settings page](#adding-cdn-settings)
* [From the Environments page](#adding-cdn-environments)

When adding a custom domain name, the domain is served using the most specific, valid certificate. If multiple certificates have the same domain, then the most recently updated is chosen. Adobe recommends that you manage certificates such that there are no overlapping domains.

The steps described in this document are based on Fastly. If you used a different CDN, configure your domain with the CDN you have chosen to use.

## Add a custom domain name from the Domain Settings page {#adding-cdn-settings}

Follow these steps to add a custom domain name from the **Domain Settings** page. 

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. Navigate to the select the **Domain Settings** tab in the left navigation panel.

   ![The Domain Settings window](/help/implementing/cloud-manager/assets/cdn/cdn-create.png)

1. Click the **Add Domain** button at the top-right to open the **Add Domain Name** dialog.

   ![Add Domain dialog box](/help/implementing/cloud-manager/assets/cdn/add-cdn1.png)

1. On the **Domain Name** tab, enter the custom domain name in the **Domain Name** field. 

   >[!NOTE] 
   >
   >Do not include `http://`, `https://`, or spaces when entering in your domain. 

1. Select the **Environment** whose service is associated with the domain name.

1. Select either the **Publish** or **Preview** service.

1. Select the **Domain SSL Certificate** associated with the domain name from the drop-down and select **Continue**.

1. The **Verification** tab appears.

   ![Domain name verification](/help/implementing/cloud-manager/assets/cdn/cdn-create6.png)

   * The **Verification** tab describes the next steps to configure your custom domain name, which is creating a necessary TXT record.
   * You can do this step immediately (before clicking **Create** in the dialog box) or after you click **Create** in the dialog box.
   * Options and next steps are described below.

1. Click **Create** to save the custom domain name in Cloud Manager.

When you select **Create** in the **Add Custom Domain** wizard, Cloud Manager triggers a TXT verification. Create the TXT record when you set up the custom domain name in Cloud Manager. However, this step is not required. For subsequent verifications, you must actively select the **Verify again** icon next to the status. 

The name is not active until Cloud Manager verifies that the TXT entry is added and verified. The status of **Verified and Deployed** indicates a successful TXT verification.

* See [Add a TXT record](/help/implementing/cloud-manager/custom-domain-names/add-text-record.md) to learn more about TXT records. 
* See [Check domain name status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) for more details on how Cloud Manager verifies the custom domain name and its TXT entry.

## Next steps {#next-steps}

After you create your custom domain name in Cloud Manager, add a TXT entry to verify ownership of the domain. Proceed to the document [Adding a TXT Record](/help/implementing/cloud-manager/custom-domain-names/add-text-record.md) to continue setting up your custom domain name.

## Add a custom domain name from the Environments page {#adding-cdn-environments}

The steps for adding a custom domain name from the **Environments** page are the same as when [adding a custom domain name from the Domain Settings page](#adding-cdn-settings), but the entry point differs. Follow these steps to add a custom domain name from the **Environments** page.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments Detail** page for the environment of interest.

   ![Entering domain name on the Environment Details page](/help/implementing/cloud-manager/assets/cdn/cdn-create4.png)

1. Use the **Domain Names** table to submit the custom domain name.

   1. Enter the custom domain name.
   1. Select the SSL certificate associated with this name from the drop-down list.
   1. Click **+Add**.

   ![Add a custom domain name](/help/implementing/cloud-manager/assets/cdn/cdn-create3.png)

1. The **Add domain name** dialog box opens to the **Domain Name** tab. Continue as you would for [adding a custom domain name from the Domain Settings page](#adding-cdn-settings).
