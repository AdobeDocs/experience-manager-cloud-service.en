---
title: Checking DNS Record Status
description: Checking DNS Record Status
exl-id: 76ca1584-e21d-4e3a-a08a-82b2779167cf
---
# Checking DNS Record Status {#check-dns-record-status}

You can determine whether your domain name is properly resolving to your AEM as a Cloud Service website by clicking the Status icon for the DNS record from the table on the Environments from the Domain Settings page. 

Cloud Manager will automatically trigger a DNS lookup when your Custom Domain Name is first successfully verified and deployed. For subsequent attempts, you must actively select the **resolve again** icon next to the status.

Cloud Manager performs a DNS lookup for your domain name and displays one of the following status messages:

* **DNS status not detected**
   DNS status will not be detected until your custom domain name has been successfully verified and deployed. This status is also observed when your Custom Domain name is in the process of deletion.

* **DNS Resolves Incorrectly** 
   This indicates that either DNS records configuration has not resolved/pointed over yet or is erroneous. An Adobe representative will be notified automatically.

   >[!NOTE]
   >You must configure either a `CNAME` or `A-record` by following the corresponding instructions. Refer to Configuring DNS Settings to learn more. When ready, you must select the **resolve again** icon next to the status.

* **DNS Resolution In Progress**
   Resolution is in progress. This status is typically seen after you select the ‘resolve again’ icon next to the status.

* **DNS Resolves Correctly**
   Your DNS settings are properly configured. Your site is serving visitors.
