---
title: Deleting an SSL Certificate - Managing SSL Certificates
description: Deleting an SSL Certificate - Managing SSL Certificates
exl-id: 43f66871-cca4-4709-95d0-68aa715c0da2
---
# Deleting an SSL Certificate {#deleting-an-ssl-certificate}

>[!IMPORTANT]
>Removing certificates from Cloud Manager is a permanent action that cannot be undone. Best practice is to save any necessary SSL files locally before deleting them in the Cloud Manager user interface.

A user must be in the Business Owner or Deployment Manager role in order to delete an SSL certificate in Cloud Manager. Cloud Manager will not allow you to delete an SSL certificate that has one or more domains associated with it.  All associated domains must be deleted before deleting the SSL certificate. Refer to [Deleting a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/delete-custom-domain-name.md) to learn more.

Follow the steps below to delete an SSL Certificate:

1. Navigate to the **SSL Certificates** screen from the **Environments** page.
   ![](/help/implementing/cloud-manager/assets/ssl/ssl-cert-3.png)
1. Identify the row where the SSL certificate name you wish to delete is listed.
1. Select the **...** menu from the far right end of the row.
1. Select **Delete**.
    ![](/help/implementing/cloud-manager/assets/ssl/ssl-cert-delete01.png)
1. Confirm your submission from **Delete SSL Certificate** dialog box.
