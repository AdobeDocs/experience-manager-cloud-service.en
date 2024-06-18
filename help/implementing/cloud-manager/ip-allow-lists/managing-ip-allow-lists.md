---
title: Managing IP Allow Lists
description: Learn how to view, edit, delete, and check the status of IP allowlists in Cloud Manager.
exl-id: 6efabe53-3f45-47d4-ac1f-979cae0ab33e
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Managing IP Allow Lists {#manage-ip-allow-lists}

Learn how to view, edit, delete, and check the status of IP allowlists in Cloud Manager.

## Viewing and Updating IP Allow Lists {#update-ip-allow-lists}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to view and update an IP allowlist. 

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. Navigate to the **Environments** screen from the **Overview** page.
1. Navigate to the **IP Allow Lists** page from the **Environments** screen.
1. Identify the row for the IP allowlists that you want to view or update.
1. Click the ellipsis button at the right end of the row.
1. Select the **View & Update** option.
1. The **View &amp; Update** wizard displays the name, IP addresses (or ranges) that define the rule along with the environments and services to which the rule is applied.
1. Change the name or IP addresses, as desired, and confirm your submission.

Adding or removing a new IP range to an IP allowlist automatically applies/unapplies it to all corresponding environment/services to which it was previously applied.

Updates cannot be made to an IP allowlist while a prior update is in progress and has not been completed.

## Checking the Status of IP Allow Lists {#check-allow-list-status}

1. Log on to Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. Click the **Status** icon for the IP allowlist from the table on the **Environments** screen and select the **IP Allow Lists** page.

1. Cloud Manager displays the status of the allowlist as described [in the following section.](#status)

### Status of an IP Allow List {#status}

[When checking the status of IP allowlists,](#check-allow-list-status) they can have one of the following values.

* **Applied** - The IP allowlist is successfully applied to one or more environments.

* **Updating** - An update to the IP allowlist is in progress, which may include one or more application or unapplication of the list.

  * Each application/un-application is listed along with its own status of **Not Started**, **In Progress**, **Complete**, or **Failed**.

* **Failed** - One or more application or unapplication process of an update failed.
  * Each application and unapplication is listed along with its status.
    * The status is **Failed** if one application/un-application in the update fails. 
    * The status remains as **Failed** until all failures are cleared.
      * Select the **Retry** icon next to the status so you can clear the failure.
    * You cannot update or delete an IP allowlist with a **Failed** status.

* **Deleting** - A deletion of an IP allowlist is in progress.
  * Deletion involves unapplying the list from all services.
  * Each unapplication is listed along with its own status of **Not Started**, **In Progress**, **Complete**, or **Failed**.
  * When the delete operation is completed:
    * The IP allowlist does not appear in the IP allowlist table.
    * The IP allowlist is not applied on any service in the program in Cloud Manager.

* **Delete Failed** - One or more unapplications failed during a delete operation.

  * Each unapplication is listed along with the status **Complete** or **Failed**.
  * The status becomes **Delete Failed** if one unapplication fails. 
  * The status remains as **Delete Failed** until all failures are cleared.
    * Select **Delete** from the ellipsis menu at the far right of the row in the table so you can clear any failure.
  * You cannot update an IP allowlist while the status is **Failed**.

## Deleting an IP Allow List {#delete-allow-list}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to view and update an IP allowlist. 

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. Navigate to the **Environments** screen from the **Overview** page.
1. Navigate to the **IP Allow Lists** page from the **Environments** screen.
1. Identify the row of the IP allowlist that you want to delete.
1. Select the ellipsis menu at the far right end of the row.
1. Click **Delete**.
1. Confirm your submission.

Deleting an IP allowlist automatically unapplies it from all services and deletes it from the table.

## Pre-Existing CDN Configurations {#pre-existing-cdn}

If you have a pre-existing CDN configuration for your IP allowlists, there is an informative message on the **IP Allow List** page. The message encourages you to add these configurations by way of the user interface so they are visible and configurable in Cloud Manager.

The message disappears once all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

See [Adding an IP Allow List](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md) for more details.

A similar message is also provided on the **SSL Certificates** and the **Environments** pages for environments that have pre-existing CDN configurations for SSL certificates or custom domain names.
