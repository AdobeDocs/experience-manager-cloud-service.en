---
title: Add IP Allow Lists
description: Learn how to add your own IP Allow Lists using Cloud Manager.
exl-id: 769be71f-5c11-4f98-8906-7a5667a25aee
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add an IP Allow List {#add-ip-allow-list}

Learn how to add your own IP Allow List using Cloud Manager.

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to add an IP Allow List.

{{add-cm-allowlist-frontend-pipeline}}

{{ip-allow-lists-ue}}

**To add an IP Allow List:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. From the **Program Overview** page, using the left side menu (you may need to click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) in the upper-left corner to see the menu), click ![Task list icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_TaskList_18_N.svg) **IP Allow Lists**.

   ![IP Allow Lists option in the left side menu](/help/implementing/cloud-manager/assets/ip-allow-list/ip-allow-list-create.png)

1. Near the upper-right corner of the IP Allow Lists page, click **Add IP Allow List**.

   ![The Add IP Allow List dialog box](/help/implementing/cloud-manager/assets/ip-allow-list/ip-allow-list-create02.png)

1. In the **Add IP Allow List** dialog box, in the **IP Allow List name** field, enter a name that you want to use to reference the IP Allow List. This name is informational only. Be sure it is descriptive enough to help you identify the list.

1. In the **IP address / CIDR** field, enter an IP or IP CIDR block. Separate multiple blocks with a comma or a tab.

1. Click **Save**.

After saving, the newly created IP Allow List appears as a row in the table in the **IP Allow Lists** page.

