---
title: Manage SSL certificates
description: Learn how to use Cloud Manager to check the status of your SSL certificates and how to edit, replace, update, and delete them.
exl-id: ad6170f4-93bd-4bac-9c54-63c35a0d4f06
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Manage SSL certificates {#managing-ssl-certificates}

Learn how to use Cloud Manager to check the status of your Adobe managed and customer managed SSL certificates and how to delete them. For customer managed certificates, you can also edit and update (replace) them.

## Check the status of SSL certificates {#checking-status-an-ssl-certificate}

The status of your SSL certificates can be understood at a glance from the **SSL Certificates** page.

| Status of SSL certificate | Description |
| --- | --- |
| Green  | The certificate is valid for at least 14 days from the current date.  |
| Orange  | The certificate is due to expire in less than 14 days.<br>&bull; Ensure that you have a plan to renew your certificate and replace it by way of the Cloud Manager user interface to avoid possible site access or outages.<br>&bull; Cloud Manager sends regular notifications in the UI to alert you of an impending certificate expiration. |
| Red | The SSL certificate is expired.<br>See [Update an expired, customer managed SSL certificate](#update-ssl-certificate) or [Delete an SSL certificate](#deleting-an-ssl-certificate). |

## Update an expired, customer managed SSL certificate {#update-ssl-certificate}

When a customer managed certificate expires any domains that are in use with the expired certificate no longer work. Updating your certificates ensures that your domain continues to work as desired.

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To update an expired, customer managed SSL certificate:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.
1. From the **Overview** page, navigate to the **Environments** screen.
1. From the **Environments** screen, navigate to the **SSL Certificates** screen.
1. In the row of the expired customer managed certificate that you want to update, click the ellipsis button at the far right, then select **View and Update**.

   ![Update an expired, customer managed SSL certification](/help/implementing/cloud-manager/assets/ssl/ssl-cert-update.png)

1. In the **View & Update SSL Certificate** dialog box, do the following:

    * (Optional) In the **Certificate name** field, type a new name. 
    * In the **Certificate** field, paste the new certificate contents key.
    * In the **Private key** field, update this field only if you made changes to the certificate.
    * In the **Certificate chain** field (or chain of trust), paste the certificate chain.

1. Click **Update** to save your changes and have them applied automatically.

## Replace an expired, customer managed SSL certificate {#replace-ssl-certificate}

Follow the same steps that are described in [Update an expired SSL Certificate](#update-ssl-certificate) to replace an expired, customer managed SSL certificate.

## Delete an SSL certificate {#deleting-an-ssl-certificate}

Deleting Adobe managed or customer managed SSL certificates from Cloud Manager is a permanent action that cannot be undone. As a best practice, Adobe recommends that you save SSL files locally before deleting them in Cloud Manager.

>[!NOTE]
>
>You cannot delete an Adobe managed SSL certificate that has one or more active domains associated with it. All associated active domains must be deleted before deleting the SSL certificate. See [Manage custom domain names](/help/implementing/cloud-manager/custom-domain-names/managing-custom-domain-names.md) to learn more.

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To delete an SSL certificate:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. From the **Overview** page, navigate to the **Environments** screen.
1. From the **Environments** screen, navigate to the **SSL Certificates** screen.
1. In the row of the certificate you want to delete, click the ellipsis button at the far right, then select **Delete**.
If the Delete button has an information icon as seen in the following image, see the Note above.

   ![Delete button with Information icon](/help/implementing/cloud-manager/assets/ssl/ssl-cert-delete-infoicon.png)

1. In the **Delete SSL Certificate** dialog box, click **Delete** to confirm the deletion.
1. Run the pipeline to undeploy the deleted certificate.

## Pre-existing CDN configurations {#pre-existing-cdn}

If you already have a CDN configuration for your SSL certificate, the **SSL Certificates** page displays an informative message. It encourages you to add these configurations through the UI so they are visible and manageable in Cloud Manager.

The message disappears after all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

See [Add an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) for more details.

A similar message is also provided on the **IP Allow List** and the **Environments** pages for environments that have pre-existing CDN configurations for IP allow lists or custom domain names.
