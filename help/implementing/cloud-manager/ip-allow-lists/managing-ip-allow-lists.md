---
title: Managing IP Allow Lists
description: Learn how to view, edit, delete, and check the status of your IP allow lists in Cloud Manager.
exl-id: 6efabe53-3f45-47d4-ac1f-979cae0ab33e
---
# Managing IP Allow Lists {#manage-ip-allow-lists}

Learn how to view, edit, delete, and check the status of your IP allow lists in Cloud Manager.

## Viewing and Updating IP Allow Lists {#update-ip-allow-lists}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to view and update an IP allow list. 

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. Navigate to **Environments** screen from the **Overview** page.
1. Navigate to the **IP Allow Lists** page from the **Environments** screen.
1. Identify the row for the IP allow lists that you wish to view or update.
1. Click the ellipsis button at the right end of the row.
1. Select the **View & Update** option.
1. The **View &amp; Update** wizard will display the name, IP addresses (or ranges) that define the rule along with the environments and service to which the rule is applied.
1. Make changes to the name or IP addresses and confirm your submission.

Adding or removing a new IP range to an IP allow list will automatically apply/un-apply it to all corresponding environment/services to which it was previously applied.

Updates can not be made to an IP allow list while a prior update is in progress and has not completed.

## Checking the Status of IP Allow Lists {#check-allow-list-status}

Follow these steps to check the status of IP allow lists.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to **Environments** screen from the **Overview** page.

1. Click the **Status** icon for the IP allow list from the table on the **Environments** screen and select the **IP Allow Lists** page.

1. Cloud Manager will display the status of the allow list as described [in the following section.](#status)

### Status of an IP Allow List {#status}

[When checking the status of IP allow lists,](#check-allow-list-status) they can have one of the following values.

* **Applied** - The IP allow list is successfully applied to one or more environments.

* **Updating** - An update to the IP allow list is in progress, which may include one or more application or un-application of the list.

  * Each application/un-application is listed along with its own status of **Not Started**, **In Progress**, **Complete**, or **Failed**.

* **Failed** - One or more application or un-application process of an update failed.
  * Each application and un-application is listed along with its status.
    * The status is **Failed** if one application/un-application in the update fails. 
    * The status will remain as **Failed** until all failures are cleared.
      * You must select the **Retry** icon next to the status to clear the failure.
    * You can not update or delete an IP allow list with a **Failed** status.

* **Deleting** - A deletion of an IP allow list is in progress.
  * Deletion involves un-applying the list from all services.
  * Each un-application is listed along with its own status of **Not Started**, **In Progress**, **Complete**, or **Failed**.
  * Once the delete operation is completed, the IP allow list will:
    * No longer appear in the IP allow list table.
    * No longer be applied on any service in the program in Cloud Manager.

* **Delete Failed** - One or more un-applications failed during a delete operation.

  * Each un-application is listed along with the status **Complete** or **Failed**.
  * The status will be **Delete Failed** if one un-application fails. 
  * The status will remain as **Delete Failed** until all failures are cleared.
    * You must select **Delete** from the ellipsis menu at the far right of the row in the table to clear any failure.
  * You can not update an IP allow list while the status is **Failed**.

## Deleting an IP Allow List {#delete-allow-list}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to view and update an IP allow list. 

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. Navigate to **Environments** screen from the **Overview** page.
1. Navigate to the **IP Allow Lists** page from the **Environments** screen.
1. Identify the row of the IP allow list that you wish to delete.
1. Select the ellipsis menu at the far right end of the row.
1. Click **Delete**.
1. Confirm your submission.

Deleting an IP allow list automatically un-applies it from all services and deletes it from the table.

## Pre-Existing CDN Configurations {#pre-existing-cdn}

If you have a pre-existing CDN configuration for your IP allow lists, there will be an informative message on the the **IP Allow List** page, encouraging you to add these configurations via the UI so they are visible and configurable in Cloud Manager.

The message disappears once all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

Please refer to the document [Adding an IP allow list](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md) for more details.

A similar message is also provided on the **SSL Certificates** and the **Environments** pages for environments that have pre-existing CDN configurations for SSL certificates or custom domain names.
