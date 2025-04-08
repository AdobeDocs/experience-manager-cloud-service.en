---
title: Check DNS Record Status
description: Learn how to determine whether your DNS settings are properly resolved using Cloud Manager.
exl-id: 76ca1584-e21d-4e3a-a08a-82b2779167cf
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Check DNS record status {#check-dns-record-status}

Learn how to determine whether your DNS settings are properly resolved using Cloud Manager.

## DNS records status {#status}

A custom domain name cannot serve live traffic until the DNS resolves correctly. Within Cloud Manager, you can determine whether your domain name is properly resolving to your AEM as a Cloud Service website.

## Requirements {#requirements}

Fulfill these requirements before checking a DNS record status using Cloud Manager.

You must have already configured the DNS settings for your custom domain name as described in [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).

## Check DNS record status {#how-to}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. Click **Domain Settings** in the left side menu.

1. Click the **Status** icon for the domain name.

Cloud Manager performs a DNS lookup for your domain name and displays it [current status](#statuses).

Cloud Manager automatically triggers a DNS lookup when your custom domain name is first successfully verified and deployed. For subsequent attempts, you must actively select the **Resolve Again** icon next to the status.

## DNS statuses in Cloud Manager {#statuses}

A custom domain can have one of the following statuses in Cloud Manager.

| Status | Description |
| --- | --- |
| DNS status not detected | DNS status is not detected until your custom domain name is successfully verified and deployed. This status is also observed when your custom domain name is in the process of deletion. |
| DNS resolves incorrectly | This status indicates that either the DNS records configuration has not resolved or is erroneous. See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) to learn more.<br>When ready, you must select the **Resolve Again** icon next to the status. |
| DNS resolution in progress | The resolution is in progress. This status is typically seen after you select the **Resolve Again** icon next to the status. |
| DNS resolves correctly | Your DNS settings are properly configured. Your site is serving visitors. |

## Next steps {#next-steps}

You have successfully configured your custom domain for use with Cloud Manager. See the document [Manage custom domain names](/help/implementing/cloud-manager/custom-domain-names/managing-custom-domain-names.md) for details on how to manage your custom domain names using Cloud Manager.
