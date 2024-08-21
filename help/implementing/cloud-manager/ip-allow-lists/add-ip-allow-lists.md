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

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. From the **Program Overview** page, using the side panel on the left side (you may need to click the hamburger icon in the upper-left corner to see the panel), click **IP Allow Lists**.

   ![IP Allow Lists option in the side panel](/help/implementing/cloud-manager/assets/ip-allow-list/ip-allow-list-create.png)

1. Near the upper-right corner of the IP Allow Lists page, click **Add IP Allow List**.

   ![The Add IP Allow List dialog box](/help/implementing/cloud-manager/assets/ip-allow-list/ip-allow-list-create02.png)

1. In the **Add IP Allow List** dialog box, in the **IP Allow List name** field, enter a name that you want to use to reference the IP Allow List. This name is informational only. Be sure it is descriptive enough to help you identify the list.

1. In the **IP address / CIDR** field, enter an IP or IP CIDR block. Separate multiple blocks with a comma or a tab.

1. Click **Save**.

After saving, the newly created IP Allow List appears as a row in the table in the **IP Allow Lists** page.

## Add the Cloud Manager IP Allow List {#add-cm-allowlist}

The front-end pipeline requires that the following Cloud Manager IP Allow List be added beforehand.

**Cloud Manager IP Allow List**

`52.254.106.192/28,20.186.185.181,52.254.106.240/28,52.254.107.128/28,52.254.105.192/28,52.254.106.176/28,20.186.185.227,52.254.106.144/28,52.254.107.64/28,20.186.185.239,20.22.83.112,52.254.107.80/28,52.254.107.144/28,52.254.106.224/28,20.14.241.153,52.254.107.0/28,52.254.107.32/28,52.254.106.208/28,40.70.154.136/29,52.254.106.160/28,52.254.107.16/28,52.254.106.0/28,4.152.211.251`

To avoid disruption of running the front-end pipeline, ensure that this Cloud Manager IP Allow List is added and then applied to the Author service of the environment *before* you enable the pipeline.

**To add the Cloud Manager IP Allow List:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. From the **Program Overview** page, using the side panel on the left side (you may need to click the hamburger icon in the upper-left corner to see the panel), click **IP Allow Lists**.

1. Near the upper-right corner of the IP Allow Lists page, click **Add IP Allow List**.

1. In the **Add IP Allow List** dialog box, in the **IP Allow List name** field, type *`Cloud Manager`*.

1. Copy the block of Cloud Manager IP Allow List addresses above. Each address is already separated by a comma.

1. In the **Add IP Allow List** dialog box, paste the block into the **IP address / CIDR** field.

1. Place the cursor just after the first comma in the address list and press **Enter**.

1. Click **Save**.

Now, [apply the Cloud Manager IP Allow List](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) to your program environments. 



