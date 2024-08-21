---
title: Apply and Unpply IP Allow Lists 
description: Learn how to apply and unapply IP Allow Lists to Cloud Manager environments.
exl-id: 7158496c-b0c4-4228-a306-71dc51003c57
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Apply and unapply IP Allow Lists {#apply-allow-list}

When applying IP Allow Lists, all IP ranges included in the list's definition are associated with an author or publish service within an environment. Unapplying a list is the inverse to this process.

>[!IMPORTANT]
>
>To avoid disruption of running the front-end pipeline, ensure that the [Cloud Manager IP Allow List is added](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md), and then applied to the Author service of the environment *before* you [enable the pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md##enabling).

## Apply IP Allow Lists {#applying}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to apply an IP Allow List.

**To apply IP Allow Lists:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/).
1. Select the appropriate organization.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. From the **Overview** page, navigate to the **Environments** screen.
1. On the **Environments** screen, navigate to the specific environment details page.
1. Navigate to the **IP Allow List** table.
1. Use the input fields at the top of the table so you can select the IP Allow List and the Author or publish service to which you to apply it. 
The IP Allow List must already exist in Cloud Manager to apply it. See [Add IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md).
1. Click **Apply** and confirm your submission.

## Unapply IP Allow Lists {#un-applying}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to unapply an IP Allow List.

**To unapply IP Allow Lists:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/).
1. Select the appropriate organization.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. Navigate to the **Environments** screen from the **Overview** page.
1. Navigate to the specific environment details page on the **Environments** screen.1. Navigate to the **IP Allow List** table.
1. Identify the row of the IP Allow List that you want to unapply.
1. On the right side of the identified row, click the ellipsis button, then select **Unapply**.
1. Confirm your submission.
