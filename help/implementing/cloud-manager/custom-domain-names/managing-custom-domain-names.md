---
title: Managing Custom Domain Names
description: Learn how to use Cloud Manager to view, update, replace, and delete custom domain names.
exl-id: 6cab8cf2-22c0-4f4b-9c54-a1425e74ddd0
---
# Managing Custom Domain Names {#managing-custom-domain-names}

Cloud Manager allows you to to view, update, replace, and delete custom domain names.

## View and Update {#view-and-update}

Use the **View and Update** menu to view the details of any of your custom domain names.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. Identify the row of the custom domain name you wish to view or update.

1. Click the ellipsis button at the far right end of the row.

1. Select the **View &amp; Update** option.

## Updating Custom Domain Name’s SSL Certificate {#update-cert}

You can follow [the same steps to view and update a custom domain name](#view-and-update) to update a custom domain name's SSL certificate.

>[!NOTE]
>
>The SSL certificate must be valid, [already configured,](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md) and contain the custom domain name you are updating.

## Deleting a Custom Domain Name {#deleting}

A user with the **Business Owner** or **Deployment Manager** role can use Cloud Manager to delete a custom domain name.

### Deleting a Custom Domain Name from All Associated Environments {#delete-cdn-all}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. Navigate to the **Domain Settings** page from the **Environments** screen.

1. Identify the row of the custom domain name you wish to delete.

1. Click the ellipsis button at the far right end of the row.

1. Select **Delete**.

   ![Deleting custom domain names](/help/implementing/cloud-manager/assets/cdn/cdn-delete.png)

1. Confirm your submission.

### Deleting a Custom Domain Name from a Specific Environment {#delete-cdn-specific}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. Navigate to the **Environments** screen from the **Overview** page.
1. From the **Environments** page, navigate to details screen of the environment of interest.
1. From the domain names table, identify the row of the custom domain name you wish to delete.
1. Click the ellipsis button at the far right end of the row.
1. Select **Delete**.
1. Confirm your submission.
