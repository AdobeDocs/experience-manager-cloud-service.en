---
title: Manage CDN Configurations
description: Learn about how to use Cloud Manager to edit and update, or delete CDN configurations for an Edge Delivery site or a Cloud Manager environment.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
exl-id: 2ec16c91-0195-4732-a26d-ac223e10afb9
---
# Manage CDN configurations {#manage-cdn-configurations}

Learn about how to use Cloud Manager to edit or delete CDN configurations for an Edge Delivery site or a Cloud Manager environment.

## Edit a CDN configuration from the CDN Configurations page {#edit-cdn}

In Adobe Cloud Manager, you may want to edit a CDN (Content Delivery Network) configuration, including the environment tier (Publish or Preview) and SSL certificate, for several reasons.

* **Environment changes**: Adjusting the tier helps match the CDN settings with the correct environment, whether for live production (Publish) or testing (Preview).
* **Security enhancements**: Selecting a different SSL certificate may be necessary when updating certificates or addressing compliance and security needs.
* **Optimizing performance**: Editing the configuration ensures the correct CDN settings for delivering content based on changing operational needs.

You can edit a configuration without fully removing the existing configuration. Changes apply to the selected environment&ndash;for example, staging or production&ndash;and can affect how content is delivered and secured.

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To edit a CDN configuration from the CDN Configurations page:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. In the left side menu, under **Services**, click ![Social network icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_SocialNetwork_18_N.svg) **CDN Configurations**.
1. In the **CDN Configurations** table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose CDN configuration you want to update.

1. From the drop-down menu, click **Edit**.

1. In the **Edit CDN configuration** dialog box, set one or more of the options in the respective drop-down list.

    The options displayed in the dialog box depend on whether you are using an **Adobe managed CDN** or an **Other CDN provider** (customer managed CDN).

1. Click **Update**.

    The status of the edited CDN is updated in the **CDN Configurations** table to reflect the changes you made.


## Edit a CDN configuration from the Environments page
    
The steps for editing a CDN configuration from the **Environments** page are nearly the same as when [editing a CDN configuration from the CDN Configurations page](#edit-cdn), but the entry point differs. 

**To edit a CDN configuration from the Environments page:**
    
1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
    
1. In the left side menu, click **Environments**.

1. On the **Environments** page, select an environment of interest.

1. On the environment details page, in the CDN Configurations grouping, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) that corresponds to the CDN configuration you want to edit.  
    
1. In the pop-up menu, click **Edit**.

1. In the **Edit CDN Configuration** dialog box, set one or more of the options in the respective drop-down list.

    The options displayed in the dialog box depend on whether you are using an **Adobe managed CDN** or an **Other CDN provider** (customer managed CDN).

1. Click **Update**.


<!-- ## Go live readiness {#go-live-readiness} 

1. ADD STEPS -->


## Delete a CDN configuration {#delete-cdn}

When you delete an Adobe managed or customer managed CDN configuration in Cloud Manager, the associated domain's routing and SSL certificate settings are removed. The domain no longer uses the CDN for traffic delivery, and any security or performance enhancements provided by the CDN is lost. You may experience service disruption until a new configuration is set up, whether re-adding the deleted CDN or adding a new one. 

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To delete a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. In the left side menu, under **Services**, click **CDN Configurations**.

1. In the CDN Configurations table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row that corresponds to a CDN you want to remove, then click **Delete**.

1. In the **Delete CDN Configuration** dialog box, click **Delete**.

1. Click **Delete** again to confirm the removal of the site's CDN.


## Delete a CDN configuration from the Environments page
    
The steps for deleting a CDN configuration from the **Environments** page are nearly the same as when [deleting a CDN configuration from the CDN Configurations page](#edit-cdn), but the entry point differs. 

**To delete a CDN configuration from the Environments page:**
    
1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
    
1. In the left side menu, click **Environments**.

1. On the **Environments** page, select an environment of interest.

1. On the environment details page, in the **CDN Configurations** grouping, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) that corresponds to the CDN configuration you want to remove, then click **Delete**.  
    
1. In the **Delete CDN Configuration** dialog box, click **Delete**.

1. Click **Delete** again to confirm the removal of the site's CDN.
