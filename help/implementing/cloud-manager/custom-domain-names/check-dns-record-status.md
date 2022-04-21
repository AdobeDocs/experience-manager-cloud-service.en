---
title: Checking DNS Record Status
description: Learn how to determine whether your DNS settings are properly resolving by using Cloud Manager.
exl-id: 76ca1584-e21d-4e3a-a08a-82b2779167cf
---
# Checking DNS Record Status {#check-dns-record-status}

Within Cloud Manager you can determine whether your domain name is properly resolving to your AEM as a Cloud Service website.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. Click on **Domain Settings** in the left navigation panel.

1. Click the **Status** icon for the domain name.

Cloud Manager performs a DNS lookup for your domain name and displays one of the following status messages.

* **DNS status not detected** - DNS status will not be detected until your custom domain name has been successfully verified and deployed.

  * This status is also observed when your Custom Domain name is in the process of deletion.

* **DNS Resolves Incorrectly** - This indicates that either the DNS records configuration has not resolved or is erroneous.

   * Refer to the document [Configuring DNS Settings](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md) to learn more.
   * When ready, you must select the **Resolve Again** icon next to the status.

* **DNS Resolution In Progress** - The resolution is in progress.

  * This status is typically seen after you select the **Resolve Again** icon next to the status.

* **DNS Resolves Correctly** - Your DNS settings are properly configured.

  * Your site is serving visitors.

Cloud Manager will automatically trigger a DNS lookup when your custom domain name is first successfully verified and deployed. For subsequent attempts, you must actively select the **Resolve Again** icon next to the status.
