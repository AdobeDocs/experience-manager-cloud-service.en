---
title: Viewing Updating and Replacing an SSL Certificate - Managing SSL 
description: Viewing Updating and Replacing an SSL Certificate - Managing SSL Certificates
exl-id: 662494b1-a710-4822-97ef-057043ef89ba
---
# Viewing & Updating & Replacing an SSL Certificate  {#view-update-replace-ssl-certificate}

## Viewing and Updating an SSL Certificate {#view-update}

When to use these options in the Cloud Manager UI:

* An existing certificate is about to expire. User has renewed the certificate with the certificate vendor and wishes to replace the existing one that is about to expire. Note Only user with the appropriate permissions can make updates.
* Use the **View & Update** menu to simply view the SSL certificate details.
* Alternatively, you can change the name that has been used to reference a certificate from this screen. 
* Only user with the appropriate permissions can make updates.


## Updating an SSL Certificate about to Expire {#update-ssl-certificate}

When a certificate expires any domains that are in use with the expired certificate will no longer work. To update an expired certificate, one must follow the steps listed below. This will ensure that your domain continues to work as desired. Adding a new certificate will necessitate updating the custom domain name with the new Certificate before the domains will work as desired. Refer to [Viewing & Updating & Replacing a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/view-update-replace-custom-domain-name.md) for more details.

Follow the steps below to update an SSL Certificate:

>[!NOTE]
>A user must be in the Business Owner or Deployment Manager role in order to update an SSL certificate in Cloud Manager.

1. Navigate to the SSL Certificates screen from the **Environments** page.
1. You will see a table with a row for each SSL certificate that has been successfully installed in your program.
1. The menu options for each row may be accessed by selecting the three buttons at the far right end of the row of interest. 
1. Select **View & Update**. The certificate details can be viewed from here.

## Replacing an SSL Certificate {#replace-ssl-certificate}

Follow the steps below to replace an SSL Certificate:

1. Navigate to the SSL Certificates screen from the **Environments** page.
1. You will see a table with a row for each SSL certificate that has been successfully installed in your program.
1. The menu options for each row may be accessed by selecting the three buttons at the far right end of the row of interest. 
1. Select **View & Update**.
1. In order to replace the certificate, paste the new content into the appropriate input fields and click on **Save**. You will need to address any errors that may arise. 

   Refer to [Certificate Errors](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md#certificate-error) to work through commonly encountered issues.
