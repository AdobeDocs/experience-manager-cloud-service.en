---
title: Managing SSL Certificates
description: Learn how to use Cloud Manager to check the status of your SSL certificates and how to edit, replace, update, and delete them.
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

## Pre-Existing CDN Configurations {#pre-existing-cdn}

If you have a pre-existing CDN configuration for your SSL certificate, there will be an informative message on the the **SSL Certificates** page, encouraging you to add these configurations via the UI so they are visible and configurable in Cloud Manager.

The message disappears once all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

Please refer to the document [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) for more details.

A similar message is also provided on the **IP Allow List** and the **Environments** pages for environments that have pre-existing CDN configurations for IP allow lists or custom domain names.

## Updating an SSL Certificate {#update-ssl-certificate}

When a certificate expires any domains that are in use with the expired certificate will no longer work. Updating your certificates through the following steps ensures that your domain continues to work as desired.

1. Navigate to the SSL Certificates screen from the **Environments** page.
1. You will see a table with a row for each SSL certificate that has been successfully installed in your program.
1. The menu options for each row may be accessed by selecting the three buttons at the far right end of the row of interest. 
1. Select **View & Update**. The certificate details can be viewed from here.

>[!NOTE]
>
>A user must be a member of the **Business Owner** or **Deployment Manager** role in order to update an SSL certificate in Cloud Manager.

## Replacing an SSL Certificate {#replace-ssl-certificate}

Follow these steps to replace an SSL certificate.

1. Navigate to the SSL Certificates screen from the **Environments** page.
1. You will see a table with a row for each SSL certificate that has been successfully installed in your program.
1. The menu options for each row may be accessed by selecting the three buttons at the far right end of the row of interest. 
1. Select **View & Update**.
1. In order to replace the certificate, paste the new content into the appropriate input fields and click on **Save**. You will need to address any errors that may arise. 

## Deleting an SSL Certificate {#deleting-an-ssl-certificate}

Removing certificates from Cloud Manager is a permanent action that cannot be undone. Adobe recommends as a best practice to save SSL files locally before deleting them in Cloud Manager.

Cloud Manager will not allow you to delete an SSL certificate that has one or more domains associated with it. All associated domains must be deleted before deleting the SSL certificate. Please refer to the document [Deleting a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/delete-custom-domain-name.md) to learn more.

Follow these steps to delete an SSL certificate.

1. Navigate to the **SSL Certificates** screen from the **Environments** page.
   ![](/help/implementing/cloud-manager/assets/ssl/ssl-cert-3.png)
1. Identify the row where the SSL certificate name you wish to delete is listed.
1. Select the **...** menu from the far right end of the row.
1. Select **Delete**.
    ![](/help/implementing/cloud-manager/assets/ssl/ssl-cert-delete01.png)
1. Confirm your submission from **Delete SSL Certificate** dialog box.

>[!NOTE]
>
>A user must be a member of the **Business Owner** or **Deployment Manager** role in order to delete an SSL certificate in Cloud Manager.