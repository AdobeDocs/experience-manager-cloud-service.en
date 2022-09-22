---
title: Adding IP Allow Lists
description: Learn how to add your own IP allow list using Cloud Manager.
exl-id: 769be71f-5c11-4f98-8906-7a5667a25aee
---

# Adding an IP Allow List {#add-ip-allow-list}

Learn how to add your own IP allow list using Cloud Manager.

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to add an IP allow list.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to **Environments** screen from the **Overview** page.

1. Navigate to **IP Allow Lists** page from the **Environments** screen.

   ![IP allow lists option in the side panel](/help/implementing/cloud-manager/assets/ip-allow-list/ip-allow-list-create.png)

1. Click on **Add IP Allow List** to open the **Add IP Allow List** dialog.

   ![The Add IP Allow List dialog](/help/implementing/cloud-manager/assets/ip-allow-list/ip-allow-list-create02.png)

1. Enter a name you would like to use to reference the allow list in the **IP Allow List name** field.

   * This is informational only and should be descriptive to help you identify the list.

1. Enter an IP or IP CIDR block in the **IP address/CIDR** field.

   * Multiple blocks can be separated by a comma or a tab.

1. Click **Save** to confirm your submission.

Upon saving, the newly created IP allow list will appear as a row in the table in the **IP Allow Lists** page.
