---
title: Managing SSL Certificates
description: Learn how to use Cloud Manager to check the status of your SSL certificates and how to edit, replace, update, and delete them.
exl-id: ad6170f4-93bd-4bac-9c54-63c35a0d4f06
---
# Managing SSL Certificates {#managing-ssl-certificates}

Learn how to use Cloud Manager to check the status of your SSL certificates and how to edit, replace, update, and delete them.

## Checking the Status of SSL Certificates {#checking-status-an-ssl-certificate}

The status of your SSL certificates can be understood at a glance from the SSL certificate page.

* **Green** - This status indicates that your certificate is valid for at least 60 days from the current date.

* **Orange** - This status indicates that your certificate is due to expire in less than 60 days.
  * It is time to ensure you have a plan to renew your certificate and replace it via Cloud Manager UI in order to avoid possible site access or outages.
  * Cloud Manager will send regular notifications in the UI to alert you of an impending certificate expiration.

* **Red** - This status indicates that the SSL certificate has expired.

## Updating an SSL Certificate {#update-ssl-certificate}

When a certificate expires any domains that are in use with the expired certificate will no longer work. Updating your certificates through the following steps ensures that your domain continues to work as desired.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. Navigate to **Environments** screen from the **Overview** page.
1. Navigate to the **SSL Certificates** screen from the **Environments** screen.
1. You will see a table with a row for each SSL certificate that has been successfully installed in your program. Click on the ellipsis button at the far right in the row of the certificate you wish to update and select **View &amp; Update**.
1. The certificate details are displayed and can be updated.

>[!NOTE]
>
>A user must be a member of the **Business Owner** or **Deployment Manager** role in order to update an SSL certificate in Cloud Manager.

## Replacing an SSL Certificate {#replace-ssl-certificate}

An SSL certificate can be replaced by following the same steps as described in the section [Updating an SSL Certificate.](#update-ssl-certificate)

## Deleting an SSL Certificate {#deleting-an-ssl-certificate}

Removing certificates from Cloud Manager is a permanent action that can not be undone. As a best practice, Adobe recommends to save SSL files locally before deleting them in Cloud Manager.

Cloud Manager will not allow you to delete an SSL certificate that has one or more domains associated with it. All associated domains must be deleted before deleting the SSL certificate. Please refer to the document [Managing Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/managing-custom-domain-names.md) to learn more.

Follow these steps to delete an SSL certificate.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. Navigate to **Environments** screen from the **Overview** page.
1. Navigate to the **SSL Certificates** screen from the **Environments** screen.
1. You will see a table with a row for each SSL certificate that has been successfully installed in your program. Click on the ellipsis button at the far right in the row of the certificate you wish to delete and select **Delete**.
1. Confirm the deletion in the **Delete SSL Certificate** dialog.

>[!NOTE]
>
>A user must be a member of the **Business Owner** or **Deployment Manager** role in order to delete an SSL certificate in Cloud Manager.

## Pre-Existing CDN Configurations {#pre-existing-cdn}

If you have a pre-existing CDN configuration for your SSL certificate, there will be an informative message on the the **SSL Certificates** page, encouraging you to add these configurations via the UI so they are visible and configurable in Cloud Manager.

The message disappears once all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

Please refer to the document [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) for more details.

A similar message is also provided on the **IP Allow List** and the **Environments** pages for environments that have pre-existing CDN configurations for IP allow lists or custom domain names.
