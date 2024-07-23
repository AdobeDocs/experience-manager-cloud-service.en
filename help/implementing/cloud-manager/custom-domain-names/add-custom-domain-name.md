---
title: Adding a Custom Domain Name
description: Learn how to add a custom domain name using Cloud Manager.
exl-id: 0fc427b9-560f-4f6e-ac57-32cdf09ec623
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Adding a Custom Domain Name {#adding-cdn}

You can add a custom domain name from two locations in Cloud Manager:

* [From the Domain Settings page](#adding-cdn-settings)
* [From the Environments page](#adding-cdn-environments)

>[!NOTE]
>
>A user must have the **Business Owner** or **Deployment Manager** role to add a custom domain name in Cloud Manager, and you must be using the Fastly CDN.

## Prerequisite {#prerequisite}

You must add a domain SSL certificate for the domain you wish to add before adding a custom domain name. See the document [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) for more information.

## Adding a Custom Domain Name from the Domain Settings Page {#adding-cdn-settings}

When adding a custom domain name, the domain will be served using the most specific, valid certificate. If multiple certificates have the same domain, then the most recently updated is chosen. Adobe recommends that you manage certificates such that there are no overlapping domains.

Follow these steps to add a custom domain name from the **Domain Settings** page. These steps are based on Fastly. If you use a different CDN, you must configure your domain with the CDN you have chosen to use.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. Navigate to the select the **Domain Settings** tab in the left navigation panel.

   ![The Domain Settings window](/help/implementing/cloud-manager/assets/cdn/cdn-create.png)

1. Click the **Add Domain** button at the top-right to open the **Add Domain Name** dialog.

   ![Add Domain dialog](/help/implementing/cloud-manager/assets/cdn/add-cdn1.png)

1. On the **Domain Name** tab, enter the custom domain name in the **Domain Name** field. 

   >[!NOTE] 
   >
   >Do not include `http://`, `https://`, or spaces when entering in your domain. 

1. Select the **Environment** whose service is associated with the domain name.

1. Select either the **Publish** or **Preview** service.

1. Select the **Domain SSL Certificate** associated with the domain name from the drop-down and select **Continue**.

1. The **Verification** tab appears. appears and will take you to  Click **Create**.

   ![Domain name verification](/help/implementing/cloud-manager/assets/cdn/cdn-create6.png)

   * The **Verification** tab describes the domain name verification process of creating a necessary TXT record. Follow the instructions provided to prove domain ownership for your environment.
   * See the document [Adding a TXT Record](/help/implementing/cloud-manager/custom-domain-names/add-text-record.md) for more information.

1. Tap or click **Create** to save the custom domain name in Cloud Manager.

You can save the custom domain name without preforming the verification and TXT entry. However the name will not be active until those steps are complete. See [Adding a TXT Record](/help/implementing/cloud-manager/custom-domain-names/add-text-record.md) to learn more about TXT records.

Successful TXT verification is indicated by the status **Verified and Deployed**.

See [Checking Custom Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) to learn more about various statuses and how to address potential issues.

>[!TIP]
>
>Review the following article about the need to [Add a CNAME or A Record next](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md) to avoid doubling effort when adding DNS-records to your custom-domain. The TXT entry and the CNAME or A Record can be set simultaneously on the governing DNS Server.

>[!NOTE]
>
>DNS verification can take a few hours to process because of DNS propagation delays.
>
>Cloud Manager will verify ownership and update the status which can be seen in the Domain Settings Table. See [Checking Custom Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) for more details.

## Adding a Custom Domain Name from the Environments Page {#adding-cdn-environments}

The steps for adding a custom domain name from the **Environments** page are the same as when [adding a custom domain name from the Domain Settings page,](#adding-cdn-settings) but the entry point differs. Follow these steps to add a custom domain name from the **Environments** page.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to **Environments Detail** page for the environment of interest.

   ![Entering domain name on the Environment Details page](/help/implementing/cloud-manager/assets/cdn/cdn-create4.png)

1. Use the **Domain Names** table to submit the custom domain name.

   1. Enter the custom domain name.
   1. Select the SSL certificate associated with this name from the drop-down list.
   1. Click **+Add**.

   ![Add Custom Domain Name](/help/implementing/cloud-manager/assets/cdn/cdn-create3.png)

1. The **Add Domain Name** dialog box opens to the **Domain Name** tab. Continue as you would for [adding a custom domain name from the Domain Settings page.](#adding-cdn-settings)
