---
title: Manage Domain Mappings
description: Learn about how to use Cloud Manager to edit and update, or delete CDN configurations for an Edge Delivery site or a Cloud Manager environment.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
exl-id: 2ec16c91-0195-4732-a26d-ac223e10afb9
---
# Manage Domain Mappings {#manage-domain-mappings}

Learn about how to use Cloud Manager to edit or delete CDN configurations for an Edge Delivery site or a Cloud Manager environment.

## Edit a CDN configuration from the Domain Mappings page {#edit-domain-mapping}

In Adobe Cloud Manager, you may want to edit a CDN (Content Delivery Network) configuration, including the environment tier (Publish or Preview) and SSL certificate, for several reasons.

* **Environment changes**: Adjusting the tier helps match the CDN settings with the correct environment, whether for live production (Publish) or testing (Preview).
* **Security enhancements**: Selecting a different SSL certificate may be necessary when updating certificates or addressing compliance and security needs.
* **Optimizing performance**: Editing the configuration ensures the correct CDN settings for delivering content based on changing operational needs.

You can edit a configuration without fully removing the existing configuration. Changes apply to the selected environment&ndash;for example, staging or production&ndash;and can affect how content is delivered and secured.

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To edit a CDN configuration from the Domain Mappings page:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. In the left side menu, under **Services**, click ![Social network icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_SocialNetwork_18_N.svg) **Domain Mappings**.
1. In the **Domain Mappings** table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose CDN configuration you want to update.

1. From the drop-down menu, click **Edit**.

1. In the **Edit CDN configuration** dialog box, set one or more of the options in the respective drop-down list.

    The options displayed in the dialog box depend on whether you are using an **Adobe managed CDN** or an **Other CDN provider** (customer managed CDN).

1. Click **Update**.

    The status of the edited CDN is updated in the **Domain Mappings** table to reflect the changes you made.


## Edit a CDN configuration from the Environments page
    
The steps for editing a CDN configuration from the **Environments** page are nearly the same as when [editing a CDN configuration from the Domain Mappings page](#edit-cdn), but the entry point differs. 

**To edit a CDN configuration from the Environments page:**
    
1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
    
1. In the left side menu, click ![Data icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Data_18_N.svg) **Environments**.

1. On the **Environments** page, select an environment of interest.

1. On the environment details page, in the Domain Mappings grouping, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) that corresponds to the CDN configuration you want to edit.  
    
1. In the pop-up menu, click **Edit**.

1. In the **Edit Domain Mapping** dialog box, set one or more of the options in the respective drop-down list.

    The options displayed in the dialog box depend on whether you are using an **Adobe managed CDN** or an **Other CDN provider** (customer managed CDN).

1. Click **Update**.

 
## Go live readiness: Configure DNS settings for a custom domain {#go-live-readiness} 

Before a custom domain can serve traffic, you must complete DNS configuration with your DNS provider. After deploying a domain mapping, and clicking **Go live**, Cloud Manager displays a dialog box that guides you through the DNS record setup process. You have the option to go live by adding either a CNAME record type or an A record type.

<!-- See also [APEX record](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md#adobe-managed-cert-cname-record#adobe-managed-cert-apex-record) and [CNAME record](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md#adobe-managed-cert-cname-record). -->

**To configure Go live readiness:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. In the left side menu, under **Services**, click ![Social network icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_SocialNetwork_18_N.svg) **Domain Mappings**.
1. In the Domain Mappings table, click **Go live** near the end of a row that corresponds to a CDN whose go live readiness you want to configure.

    ![Go live readiness dialog box](/help/implementing/cloud-manager/assets/domain-mappings-go-live-readiness.png)

1. In the **Go live readiness** dialog box, do one of the following:

    | Option  | Steps |
    | --- | --- |
    | Configure A RECORD | Recommended for root domains like `example.com`<br><ol><li>Log in to your DNS service provider's portal.<li>Go to the DNS Records section.<li>Create an A record to point to all the listed IP addresses.</li></ol> |
    | Configure CNAME | Recommended for custom domains like `www.example.com`<br><ol><li>Log in to your DMS service provider's portal.<li>Go to the DNS Records section.<li>Map `cdn.adobeaemcloud.com` (CNAME record) in the DNS record of the DNS service provider (your custom domain). This mapping ensures that requests received at the custom domain are redirected to Adobe's CDN.</li></ol> |

1. In the **Go live readiness** dialog box, click **OK** to save the record. 

    Wait for DNS propagation; it may take several minutes to a few hours. 

    When the **[!UICONTROL Status]** column in the Domain Mappings table updates to **[!UICONTROL Verified]**, the custom domain is ready to use. You may need to click ![Refresh icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Refresh_18_N.svg) to update the status.

## Delete a CDN configuration {#delete-cdn}

When you delete an Adobe managed or customer managed CDN configuration in Cloud Manager, the associated domain's routing and SSL certificate settings are removed. The domain no longer uses the CDN for traffic delivery, and any security or performance enhancements provided by the CDN is lost. You may experience service disruption until a new configuration is set up, whether re-adding the deleted CDN or adding a new one. 

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To delete a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. In the left side menu, under **Services**, click ![Social network icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_SocialNetwork_18_N.svg) **Domain Mappings**.

1. In the Domain Mappings table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row that corresponds to a CDN you want to remove, then click **Delete**.

1. In the **Delete Domain Mapping** dialog box, click **Delete**.

1. Click **Delete** again to confirm the removal of the site's CDN.


## Delete a CDN configuration from the Environments page
    
The steps for deleting a CDN configuration from the **Environments** page are nearly the same as when [deleting a CDN configuration from the Domain Mappings page](#edit-cdn), but the entry point differs. 

**To delete a CDN configuration from the Environments page:**
    
1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
    
1. In the left side menu, click ![Data icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Data_18_N.svg) **Environments**.

1. On the **Environments** page, select an environment of interest.

1. On the environment details page, in the **Domain Mappings** grouping, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) that corresponds to the CDN configuration you want to remove, then click **Delete**.  
    
1. In the **Delete Domain Mapping** dialog box, click **Delete**.

1. Click **Delete** again to confirm the removal of the site's CDN.
