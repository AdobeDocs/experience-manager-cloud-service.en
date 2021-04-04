---
title: Viewing and Updating - IP Allow Lists in Cloud Manager
description: Viewing and Updating - IP Allow Lists in Cloud Manager
exl-id: 9f9aebcd-b6d0-497a-b262-0a24b4938b45
---
# Viewing and Updating an IP Allow List {#view-update}

You can view and update IP Allow Lists under the following scenarios:

* To View and Update menu to simply view the details of one or more IP Allow List’s. 
* To edit one or more of the following: 
   * IP ranges in the definition of the rule name
   * Friendly name of the IP Allow List rule

## Update IP Allow List {#update-ip-allow-lists}


A user in the Business Owner or Deployment Manager role must be logged in in order to be able to update an IP Allow List. 

>[!NOTE]
>The View & Update wizard will display the name, IP's or IP ranges that define the rule. In addition, it will display the environments and service on which the rule is applied.

Follow the steps below to update an IP Allow List:

1. Navigate to the **IP Allow Lists** page from the **Environments** screen.
1. Identify the row where the IP Allow List rule you wish to view/update is listed.
1. Select the **...** menu from the far right end of the row.
1. Select the **View & Update** option.
1. Make changes to the name or IP’s and confirm your submission.

## Important Considerations while Adding, Updating or Removing IP Allow Lists {#considerations} 

* Adding a new IP range to the IP Allow List will automatically Apply it to all corresponding environment- services.
* Removing an IP range from the IP Allow List will automatically Unapply it from all corresponding environment- services.
* Updates cannot be made to an IP Allow List while a prior update is in progress and has not completed.
* Updates cannot be made to an IP Allow List if any errors exist from a prior update. Any error(s) must be cleared by attempting to retry the update. 
   Refer to [Checking IP Allow List Status](/help/implementing/cloud-manager/ip-allow-lists/check-ip-allow-list-status.md) to learn more.
