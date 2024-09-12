---
title: Delete a CDN Configuration
description: Learn about how to delete a CDN configuration for an Edge Delivery site or a Cloud Manager environment.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Delete a CDN configuration {#delete-cdn}

When you delete an Adobe-managed or Customer-managed CDN configuration in Adobe Cloud Manager, the associated domain's routing and SSL certificate settings are removed. The domain no longer uses the CDN for traffic delivery, and any security or performance enhancements provided by the CDN is lost. You may experience service disruption until a new configuration is set up, whether re-adding the deleted CDN or adding a new one. 

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To delete a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. In the left navigation panel, under **Services**, click **CDN Configurations**.

1. In the CDN Configurations table, click the ellipsis at the end of a row whose CDN you want to remove.

    ![Deleting a CDN configuration](/help/implementing/cloud-manager/assets/cdn-config-delete.png)

1. Click **Delete**.
1. Click **Delete** again to confirm the removal of the site's CDN.