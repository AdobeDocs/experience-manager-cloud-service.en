---
title: Checking Domain Name Status
description: Checking Domain Name Status
exl-id: 8fdc8dda-7dbf-46b6-9fc6-d304ed377197
---
# Checking Domain Name Status {#check-status}

You can determine whether your domain name has been verified successfully by clicking the Status icon for the domain name from the table on Environments from the Domain Settings page. 

>[!NOTE]
>Cloud Manager will automatically trigger a TXT verification when you select Save on the verification step of the Add Custom Domain wizard. For subsequent verifications, you must actively select the **verify again** icon next to the status.

Cloud Manager will verify domain ownership via the TXT value and displays one of the following status messages:

* **Domain Verification Failed** 
   TXT value is either missing or is detected with errors. Follow instructions and retry. When ready, you must select the *verify again* icon next to the status.

* **Domain Verification In Progress**
   Verification in progress. This status is typically seen after you select the *verify again* icon next to the status.

* **Verified, Deployment Failed** 
   TXT verification was successful. However, the CDN deployment failed. An Adobe representative will be notified automatically.

* **Domain Verified & Deployed**
   This status indicates that your custom domain name is ready to be used. 
   >[!NOTE]
   >At this point, your custom domain name is ready for testing and to be pointed to the Cloud Manager domain name. Refer to [Configuring DNS Settings](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md) to learn more.

* **Deleting** 
   Deletion of Custom Domain name is in process.

* **Deletion Failed** 
   Deletion of Custom Domain name failed. You must retry. Refer to [Deleting a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/delete-custom-domain-name.md) to learn more.


## Pre-existing CDN Configurations for Custom Domain Names {#pre-existing-cdn}

Customers with environments that includes pre-existing CDN configurations for IP Allow Lists, SSL Certificates or Custom Domain Names will see the following message in the the **IP Allow List** and the **Environment** details page. The message displayed on the UI will disappear once the customer has fully migrated all pre-existing environment configurations via the UI and it may take 1-2 business days for the message to disappear.

>[!NOTE]
>In order to see and manage the pre-existing configurations they must be added via the UI. Refer to [Adding a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) for more details.

![](/help/implementing/cloud-manager/assets/ip-allow-list-message1.png)

![](/help/implementing/cloud-manager/assets/ip-allow-list-message2.png)
