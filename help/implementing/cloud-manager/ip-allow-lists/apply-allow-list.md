---
title: Apply and Unapply IP Allow Lists
description: Learn how to apply and unapply IP Allow Lists to Cloud Manager environments.
exl-id: 7158496c-b0c4-4228-a306-71dc51003c57
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

# Apply and unapply IP Allow Lists {#apply-allow-list}

When applying IP Allow Lists, all IP ranges included in the list's definition are associated with an author or publish service within an environment. Unapplying a list is the inverse to this process. 

{{add-cm-allowlist-frontend-pipeline}}
{{ip-allow-lists-ue}}

## Apply IP Allow Lists {#applying}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to apply an IP Allow List.

**To apply IP Allow Lists:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/).
1. Select the appropriate organization.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. From the **Overview** page, navigate to the **Environments** screen.
1. On the **Environments** screen, navigate to the specific environment details page.
1. Navigate to the **IP Allow List** table.
1. Use the input fields at the top of the table so you can select the IP Allow List and the Author, Publish, or Preview service to which you to apply it. 
    The IP Allow List must already exist in Cloud Manager to apply it. See [Add IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md).
1. Click ![Add icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Add_18_N.svg) **Apply** and confirm your submission.

## Unapply IP Allow Lists {#un-applying}

A user in the **Business Owner** or **Deployment Manager** role can follow these steps to unapply an IP Allow List.

**To unapply IP Allow Lists:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/).
1. Select the appropriate organization.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. From the **Overview** page, navigate to the **Environments** page.
1. Navigate to the specific environment details page.
1. From the General tab, scroll to the **IP Allow List** table.
1. Identify the row of the IP Allow List that you want to unapply.
1. On the right side of the identified row, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg).
1. Click **Unapply**.
1. In the **Unapply IP Allow List** dialog box, click **Unapply**.
