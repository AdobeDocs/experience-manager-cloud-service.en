---
title: Manage CDN Configurations
description: Learn about how to use Cloud Manager to edit and update, or delete CDN configurations for an Edge Delivery site or a Cloud Manager environment.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Manage CDN configurations {#manage-cdn-configurations}

Learn about how to use Cloud Manager to edit and update, or delete CDN configurations for an Edge Delivery site or a Cloud Manager environment.

## Edit a CDN configuration {#edit-cdn}

In Adobe Cloud Manager, you may want to edit a CDN configuration, including the environment tier (Publish or Preview) and SSL certificate, for several reasons.

* **Environment changes**: Adjusting the tier helps match the CDN settings with the correct environment, whether for live production (Publish) or testing (Preview).
* **Security enhancements**: Selecting a different SSL certificate may be necessary when updating certificates or addressing compliance and security needs.
* **Optimizing performance**: Editing the configuration ensures the correct CDN settings for delivering content based on changing operational needs.

You can edit a configuration without fully removing the existing configuration. Changes apply to the selected environment&ndash;for example, staging or production&ndash;and can affect how content is delivered and secured.

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To edit a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.
1. In the left navigation panel, under **Services**, click **CDN Configurations**.
1. In the **CDN Configurations** table, click the ellipsis at the end of a row whose CDN configuration you want to edit.

    ![Editing a CDN configuration](/help/implementing/cloud-manager/assets/cdn-config-edit.png)

1. Click **Edit**.
1. In the **Edit CDN configuration** dialog box, set one or more of the options in the respective drop-down list.

    The options that you see in the dialog box may vary depending on if you are using an Adobe-managed CDN or a Customer-managed CDN. 

1. Click **Update**.

    The status of the edited CDN is updated in the **CDN Configurations** table to reflect the changes you made.

## Delete a CDN configuration {#delete-cdn}

When you delete an Adobe-managed or Customer-managed CDN configuration in Adobe Cloud Manager, the associated domain's routing and SSL certificate settings are removed. The domain no longer uses the CDN for traffic delivery, and any security or performance enhancements provided by the CDN is lost. You may experience service disruption until a new configuration is set up, whether re-adding the deleted CDN or adding a new one. 

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To delete a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. In the left navigation panel, under **Services**, click **CDN Configurations**.

1. In the CDN Configurations table, click the ellipsis at the end of a row whose CDN you want to remove.

    ![Deleting a CDN configuration](/help/implementing/cloud-manager/assets/cdn-config-delete.png)

1. Click **Delete**.
1. Click **Delete** again to confirm the removal of the site's CDN.


