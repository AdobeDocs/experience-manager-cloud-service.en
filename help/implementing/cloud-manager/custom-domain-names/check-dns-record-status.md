---
title: Checking DNS Record Status
description: Learn how to determine whether your DNS settings are properly resolving by using Cloud Manager.
exl-id: 76ca1584-e21d-4e3a-a08a-82b2779167cf
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Checking DNS Record Status {#check-dns-record-status}

Learn how to determine whether your DNS settings are properly resolving by using Cloud Manager.

## DNS Records Status {#status}

A custom domain name can not serve live traffic until the DNS resolves correctly. Within Cloud Manager you can determine whether your domain name is properly resolving to your AEM as a Cloud Service website.

## Requirements {#requirements}

You must fulfill these requirements before checking a DNS record status using Cloud Manager.

* You must have already configured the DNS settings for your custom domain name as described in the document [Configuring DNS Settings.](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md)

## How to Check DNS Record Status {#how-to}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. Click **Domain Settings** in the left navigation panel.

1. Click the **Status** icon for the domain name.

Cloud Manager performs a DNS lookup for your domain name and displays it [current status.](#statuses)

Cloud Manager will automatically trigger a DNS lookup when your custom domain name is first successfully verified and deployed. For subsequent attempts, you must actively select the **Resolve Again** icon next to the status.

## DNS Statuses in Cloud Manager {#statuses}

A custom domain can have one of the following statuses in Cloud Manager.

* **DNS status not detected** - DNS status will not be detected until your custom domain name has been successfully verified and deployed.

  * This status is also observed when your custom domain name is in the process of deletion.

* **DNS Resolves Incorrectly** - This indicates that either the DNS records configuration has not resolved or is erroneous.

   * See [Configuring DNS Settings](/help/implementing/cloud-manager/custom-domain-names/configure-dns-settings.md) to learn more.
   * When ready, you must select the **Resolve Again** icon next to the status.

* **DNS Resolution In Progress** - The resolution is in progress.

  * This status is typically seen after you select the **Resolve Again** icon next to the status.

* **DNS Resolves Correctly** - Your DNS settings are properly configured.

  * Your site is serving visitors.
