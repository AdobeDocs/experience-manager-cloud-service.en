---
title: Checking Domain Name Status
description: Learn how to determine whether your custom domain name has been verified successfully by Cloud Manager.
exl-id: 8fdc8dda-7dbf-46b6-9fc6-d304ed377197
---

# Checking Domain Name Status {#check-status}

You can determine status of your custom domain name within Cloud Manager.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. Click on **Domain Settings** in the left navigation panel.

1. Click the **Status** icon for the domain name.

Cloud Manager will verify domain ownership via the TXT value and displays one of the following status messages.

* **Domain Verification Failed** - The TXT value is either missing or is detected with errors.

  * Follow the instructions provided to resolve the issue.
  * When ready, you must select the **Verify Again** icon next to the status.

* **Domain Verification In Progress** - Verification is in progress.

  * This status is typically seen after you select the **Verify Again** icon next to the status.

* **Verified, Deployment Failed** - The TXT verification was successful, but the CDN deployment failed. 

  * In such cases, please contact your Adobe representative.

* **Domain Verified & Deployed** - This status indicates that your custom domain name is ready to be used.

  * At this point, your custom domain name is ready for testing and to be pointed to the Cloud Manager domain name.
  * Please refer to the document [Configuring DNS Settings](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md) to learn more.

* **Deleting** - The deletion of a custom domain name is in progress.

* **Deletion Failed** - The deletion of custom domain name failed and must be retried.

  * Please refer to the document [Managing Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/managing-custom-domain-names.md) to learn more.

Cloud Manager will automatically trigger a TXT verification when you select **Save** on the verification step of the **Add Custom Domain** wizard. For subsequent verifications, you must actively select the verify again icon next to the status.

## Domain Name Errors {#domain-error}

The following are some common domain name errors and their typical resolutions.

### Domain Not Installed Error {#domain-not-installed}

 This error may occur during domain validation of the TXT record even after you've checked that the record has been updated appropriately.

#### Error Cause {#cause}

Fastly locks a domain to the initial account that registered it and no other account can register a subdomain without asking for permission. Furthermore, Fastly only allows you to assign an apex domain and associated subdomains to one Fastly service and account. If you have an existing Fastly account that links the same apex and subdomains used for your AEM Cloud Service domains you will see this error.

#### Error Resolution {#resolution}

The error is fixed as follows:

* Remove the apex and subdomains from the existing account before installing the domain in Cloud Manager.

* Use this option to link the apex domain and all subdomains to the AEM as a Cloud Service Fastly account. See [Working with Domains in the Fastly documentation](https://docs.fastly.com/en/guides/working-with-domains) for additional details.

* If your apex domain has multiple subdomains for AEM as a Cloud Service and non-AEM as a Cloud Service sites that you want to link to different Fastly accounts, then try to install the domain in Cloud Manager. If the domain installation fails, create a Customer Support ticket with Fastly so Adobe can followup with Fastly on your behalf.

>[!TIP]
>
>* Solving domain delegation issues with Fastly typically takes 1-2 business days. 
>* If you have used Fastly before, you should install domains well before your go live.

>[!NOTE]
>
>Do not route the DNS of your site to AEM as a Cloud Service IPs if the domain was not installed successfully.

## Pre-Existing CDN Configurations for Custom Domain Names {#pre-existing-cdn}

If you have a pre-existing CDN configuration for your custom domain names, there will be an informative message on the the **Custom Domain Names** and **Environment** pages, encouraging you to add these configurations via the UI so they are visible and configurable in Cloud Manager.

The message disappears once all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

Please refer to the document [Adding a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) for more details.
