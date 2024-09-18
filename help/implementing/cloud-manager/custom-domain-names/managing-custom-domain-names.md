---
title: Manage Custom Domain Names
description: Learn how to use Cloud Manager to view, update, replace, and delete custom domain names.
exl-id: 6cab8cf2-22c0-4f4b-9c54-a1425e74ddd0
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Manage custom domain names {#managing-custom-domain-names}

Cloud Manager lets you edit, update, replace, and delete custom domain names.

## Edit a custom domain name configuration {#view-and-update}

In Adobe Cloud Manager, you might want to edit a custom domain name configuation for the following reasons:

* **Switching environments**: To apply the correct configuration depending on whether you are serving content to end users (Publish) or internal users (Author).
* **Security updates**: To upgrade to a newer SSL certificate for enhanced security or compliance purposes.
* **Changing deployment strategy**: To ensure the correct SSL certificate is applied to a specific environment for proper encryption and site access.

**To edit a custom domain name configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. In the upper-left corner of the page, click the hamburger icon to reveal the left navigation menu. 
1. Under the **Services** heading, click **CDN Configurations**.
1. On the **CDN Configurations** page, click the ellipsis at the end of a row whose CDN you want to edit. 
1. Click **Edit**.
1. In the **Edit CDN configuation** dialog box, do the following:
    * In the **Tier** drop-down list, select the tier (Author or Publish) you want to use.
    * In the **SSL certificate** drop-down list, select the SSL certificat you want to use.
1. Click **Update**.


## Update a custom domain name's SSL certificate {#update-cert}

You can follow [the same steps to view and update a custom domain name](#view-and-update) to update a custom domain name's SSL certificate.

>[!NOTE]
>
>The SSL certificate must be valid, [already configured](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md), and contain the custom domain name you are updating.


## Delete a custom domain name {#deleting}

A user with the **Business Owner** or **Deployment Manager** role can use Cloud Manager to delete a custom domain name.

### Delete a custom domain name from all associated environments {#delete-cdn-all}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Domain Settings** page from the **Overview** screen.

1. Identify the row of the custom domain name that you want to delete.

1. Click the ellipsis button at the far right end of the row.

1. Select **Delete**.

1. Confirm your submission.


### Delete a custom domain name from a specific environment {#delete-cdn-specific}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. Navigate to the **Environments** screen from the **Overview** page.
1. From the **Environments** page, navigate to a details screen of the environment of interest.
1. From the domain names table, identify the row of the custom domain name you want to delete.
1. Click the ellipsis button at the far right end of the row.
1. Select **Delete**.
1. Confirm your submission.
