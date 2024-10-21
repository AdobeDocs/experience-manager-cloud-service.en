---
title: Manage IP Allow Lists
description: Learn how to view, edit, delete, and check the status of IP Allow Lists in Cloud Manager.
exl-id: 6efabe53-3f45-47d4-ac1f-979cae0ab33e
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Manage IP Allow Lists {#manage-ip-allow-lists}

Learn how to view, edit, delete, and check the status of IP Allow Lists in Cloud Manager.

## View and update IP Allow Lists {#update-ip-allow-lists}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to view and update an IP Allow List. 

**To view and update IP Allow Lists:**

1. Log on to Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. From the **Overview** page, in the left side menu, under **Services**, click ![Task list icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_TaskList_18_N.svg) **IP Allow Lists**.
1. Identify the row for the IP Allow Lists that you want to view or update.
1. Click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the right end of the row.
1. From the drop-down menu, click **View & Update**.
    The **View &amp; Update IP Allow List** dialog box shows the name, IP addresses (or ranges) that define the rule along with the environments and services to which the rule is applied.
1. Change the name or IP addresses, as desired.

    Adding or removing a new IP range to an IP Allow List automatically applies/unapplies it to all corresponding environment/services to which it was previously applied.

    Updates cannot be made to an IP Allow List while a prior update is in progress and has not been completed.

1. Click **Update**.

## Check the status of IP Allow Lists {#check-allow-list-status}

1. Log on to Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. From the **Overview** page, in the left side menu, under **Services**, click ![Task list icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_TaskList_18_N.svg) **IP Allow Lists**.

1. In the **Status** column of the IP Allow Lists table, hover the mouse pointer over an IP Allow List that is green (in use) to see one or more services applied to it.

    The status values shown in the table have the following meanings:

    | Status of IP Allow List | Description |
    | --- | --- |
    | Applied  | The IP Allow List is successfully applied to one or more environments. |
    | Updating | An update to the IP Allow List is in progress, which may include one or more application or unapplication of the list. Each application/un-application is listed along with its own status of **Not Started**, **In Progress**, **Complete**, or **Failed**.  |
    | Failed | One or more application or unapplication process of an update failed.<br>&bull; Each application and unapplication is listed along with its status.<br>&bull; The status is **Failed** if one application/un-application in the update fails. The status remains as **Failed** until all failures are cleared.<br>&bull; Click the **Retry** icon next to the status so you can clear the failure.<br>&bull; You cannot update or delete an IP Allow List with a **Failed** status.   |
    | Deleting | A deletion of an IP Allow List is in progress.<br>&bull; Deleting involves unapplying the list from all services.<br>&bull; Each unapplication is listed along with its own status of **Not Started**, **In Progress**, **Complete**, or **Failed**.<br>&bull; When the delete operation is complete, the IP Allow List does not appear in the IP Allow List table. Also, the IP Allow List is not applied on any service in the program in Cloud Manager. |
    | Delete Failed  | One or more unapplications failed during a delete operation.<br>&bull; Each unapplication is listed along with the status **Complete** or **Failed**.<br>&bull; The status becomes **Delete Failed** if one unapplication fails. The status remains as **Delete Failed** until all failures are cleared. At the far right of the table row, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg), then in the drop-down menu, click **Delete** to clear any failure.<br>&bull; You cannot update an IP Allow List while the status is **Failed**.  |

## Delete an IP Allow List {#delete-allow-list}

When you delete an IP Allow List, it automatically unapplies the list from all services and deletes it from the IP Allow List table.

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to view and update an IP Allow List. 

**To delete an IP Allow List:**

1. Log on to Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. From the **Overview** page, in the left side menu, under **Services**, click ![Task list icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_TaskList_18_N.svg) **IP Allow Lists**.
1. Identify the row for the IP Allow List that you want to delete, then click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the right end of the row, then click **Delete**.
1. In the **Delete IP Allow List** dialog box, click **Delete**.

## Pre-existing CDN configurations {#pre-existing-cdn}

If you have a pre-existing CDN (Content Delivery Network) configuration for your IP Allow Lists, there is an informative message on the **IP Allow List** page. The message encourages you to add these configurations by way of the user interface so they are visible and configurable in Cloud Manager.

The message disappears once all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

See [Add an IP Allow List](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md) for more details.

A similar message is also provided on the **SSL Certificates** and the **Environments** pages for environments that have pre-existing CDN configurations for SSL certificates or custom domain names.
