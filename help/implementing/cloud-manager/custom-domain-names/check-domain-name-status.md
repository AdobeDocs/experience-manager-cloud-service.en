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

## Pre-existing CDN Configurations for Custom Domain Names {#pre-existing-cdn}

If you have a pre-existing CDN configuration for your custom domain names, there will be an informative message on the the **Custom Domain Names** and **Environment** pages, encouraging you to add these configurations via the UI so they are visible and configurable in Cloud Manager.

The message disappears once all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

Please refer to the document [Adding a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) for more details.
