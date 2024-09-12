---
title: Edit a CDN Configuration
description: Learn about how to edit and update a CDN configuration for an Edge Delivery site or a Cloud Manager environment.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer


---

# Edit a CDN configuration {#edit-cdn}

When editing a CDN configuration, you can adjust settings like the environment's tier (Publish or Preview), or SSL certificates, without fully removing the existing configuration. Changes apply to the selected environment&ndash;for example, staging or production&ndash;and can affect how content is delivered and secured. 

A user must be a member of the **Business Owner** or **Deployment Manager** role to complete this task.

**To edit a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. In the left navigation panel, under **Services**, click **CDN Configurations**.

1. In the **CDN Configurations** table, click the ellipsis at the end of a row whose CDN you want to update.

    ![Editing a CDN configuration](/help/implementing/cloud-manager/assets/cdn-config-edit.png)

1. Click **Edit**.

1. In the **Edit CDN** dialog box, set one or more of the options in the respective drop-down list.

    The options you see in the dialog box vary depending on if you are using an Adobe-managed CDN or a Customer-managed CDN. 

1. Click **Update**.

    The status of the edited CDN is updated in the **CDN Configurations** table to reflect the changes you made.
