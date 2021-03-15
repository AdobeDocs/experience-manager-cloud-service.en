---
title: Checking Domain Name Status
description: Checking Domain Name Status
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


## Pre-existing CDN Configurations for IP Allowlists {#pre-existing-cdn}

Customers with environments that includes pre-existing CDN configurations for IP Allowlists (SSL certificates or Custom Domain Names) will see the following message in the the **IP Allowlist** and the **Environment** details page. 

![](/help/implementing/cloud-manager/assets/ip-allow-list-1.png)

In order to see and manage the pre-existing configurations they must be added via the UI.
![](/help/implementing/cloud-manager/assets/ip-allow-list-2.png)
