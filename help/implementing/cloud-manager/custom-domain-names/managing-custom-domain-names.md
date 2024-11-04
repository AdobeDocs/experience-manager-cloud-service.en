---
title: Manage Custom Domain Names
description: Learn how to use Cloud Manager to view, update, replace, and delete custom domain names.
exl-id: 6cab8cf2-22c0-4f4b-9c54-a1425e74ddd0
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Manage custom domain names {#managing-custom-domain-names}

Cloud Manager lets you edit, update, replace, verify, and delete custom domain names.

## Edit a custom domain name configuration {#view-and-update}

In Adobe Cloud Manager, you might want to edit a custom domain name configuration for the following reasons:

* **Switching environments**: To apply the correct configuration depending on whether you are serving content to end users (Publish) or internal users (Author).
* **Security updates**: To upgrade to a newer SSL certificate for enhanced security or compliance purposes.
* **Changing deployment strategy**: To ensure that the correct SSL certificate is applied to a specific environment for proper encryption and site access.

**To edit a custom domain name configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the left side menu.

1. Under the **Services** heading, click **CDN Configurations**.

1. On the **CDN Configurations** page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose CDN you want to edit. 

1. Click **Edit**.

1. In the **Edit CDN configuration** dialog box, do the following:

    * In the **Tier** drop-down list, select the tier (Publish or Preview) you want to use.
    * In the **SSL certificate** drop-down list, select the SSL certificate that you want to use.

1. Click **Update**.


## Update a custom domain name's SSL certificate {#update-cert}

Follow the same steps above to update a custom domain name's SSL certificate.

>[!NOTE]
>
>The SSL certificate must be valid, [already configured](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md), and contain the custom domain name you are updating.


## Verify a custom domain name {#verify-custom-domain-name}

See also [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Domain Settings** page from the **Overview** screen.

1. Identify the row of the custom domain name that you want to verify.

1. Click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the far right end of the row.

1. In the drop-down menu, click **Verify**.

1. In the **Verify domain** dialog box, in the **What certificate type do you plan on using with this domain?** drop-down list, select one of the following options:

   | Certificate type option | Description |
   | --- | --- |
   | Adobe managed (DV) SSL certificate | Select this certificate type if you want to use a DV (Domain Validation) certificate. This option is ideal for most cases, providing basic domain validation. Adobe manages and renews the certificate automatically. |
   | Customer managed (OV/EV) SSL certificate | Select this certificate type if you intend to use an EV/OV SSL certificate to secure the domain. This option offers enhanced security with OV (Organization Validation) or EV (Extended Validation). Use if stricter verification, higher trust levels, or custom control over the certificates is required. |

1. In the **Verify domain** dialog box, based on the certificate type you selected, do one of the following:

   | If you selected the certificate type | Description |
   | --- | ---  |
   | Adobe managed certificate |a. Complete the [Adobe managed certificate steps](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md#adobe-managed-cert-steps). When you complete the steps in the **Verify domain** dialog box, click **Verify**.<ul><li>DNS verification can take a few hours to process because of DNS propagation delays.</li><li>Cloud Manager eventually verifies domain name ownership and updates the status in the **Domain Settings** table. See [Check custom domain name status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) for more details.</li>![Verify domain status](/help/implementing/cloud-manager/assets/domain-settings-verified.png)</li></ul>b. You are now ready to [add an Adobe managed (DV) SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md#add-adobe-managed-ssl-cert).</li></ul> |
   | Customer managed certificate | a. Click **OK**.<br>b. You are now ready to [add a customer managed (OV/EV) SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md#add-customer-managed-ssl-cert).<br>After you add the certificate, your domain name is marked as verified in the **Domain Settings** table. See [Check custom domain name status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) for more details.</li></ul><br>![Verify domain for a customer managed EV/OV certificate](/help/implementing/cloud-manager/assets/verify-domain-customer-managed-step.png) |


## Delete a custom domain name from all associated environments {#deleting}

A user with the **Business Owner** or **Deployment Manager** role can use Cloud Manager to delete a custom domain name.

### Delete a custom domain name from all associated environments {#delete-cdn-all}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Domain Settings** page from the **Overview** screen.

1. Identify the row of the custom domain name that you want to delete.

1. Click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the far right end of the row.

1. Select **Delete**.

1. Confirm your submission.


### Delete a custom domain name from a specific environment {#delete-cdn-specific}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. From the **Environments** page, navigate to a details screen of the environment of interest.

1. From the domain names table, identify the row of the custom domain name you want to delete.

1. Click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the far right end of the row.

1. Select **Delete**.

1. Confirm your submission.
