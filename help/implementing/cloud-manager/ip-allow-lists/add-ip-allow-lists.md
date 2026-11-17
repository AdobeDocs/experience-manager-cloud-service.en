---
title: Add IP Allow Lists
description: Learn how to add your own IP Allow Lists using Cloud Manager.
exl-id: 769be71f-5c11-4f98-8906-7a5667a25aee
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: a01bfd36-4ab8-4bf8-9dc0-5b45b890552e
    internal-label: APIs
subfeature_v2:
  - id: d9eb3b3e-9447-4ed4-bf4a-96c7b245cb27
    internal-label: Cloud Manager APIs
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Add an IP Allow List {#add-ip-allow-list}

Configure your IP Allow List using Cloud Manager.

To add an IP Allow List, a user in the **Business Owner** or **Deployment Manager** role can follow these steps.

{{add-cm-allowlist-frontend-pipeline}}
{{ip-allow-lists-ue}}

**To add an IP Allow List:**

{{sign-in-to-cloud-manager}}

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select a program.

1. From the **Program Overview** page, using the left navigation menu (if necessary, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) in the upper-left corner to see the menu), click ![Task list icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_TaskList_18_N.svg) **IP Allow Lists**.

   ![IP Allow Lists option in the left side menu](/help/implementing/cloud-manager/assets/ip-allow-list/ip-allow-list-create.png)

1. Near the upper-right corner of the IP Allow Lists page, click **Add IP Allow List**.

   ![The Add IP Allow List dialog box](/help/implementing/cloud-manager/assets/ip-allow-list/ip-allow-list-create02.png)

1. In the **Add IP Allow List** dialog box, in the **IP Allow List name** field, enter a name that you want to use to reference the IP Allow List. This name is informational only. Ensure it is descriptive enough to help you identify the list.

1. In the **IP address / CIDR** field, enter up to 50 IP addresses or CIDR blocks. You can add them in either of the following ways:

   * One at a time: Type an address, then press `Enter`. Repeat for each additional address.
   * Multiple simultaneously: Type addresses separated by commas (,) or tabs, then press `Enter` to process each address.

1. After you enter the last IP address or CIDR block, press `Enter` to confirm the input. The entry is acknowledged only after you press `Enter`, and the **Save** button becomes active.

1. Click **Save**.

After saving, the newly created IP Allow List appears as a row in the **IP Allow Lists** page table.

