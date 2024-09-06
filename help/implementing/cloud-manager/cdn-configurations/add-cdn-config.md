---
title: Add a CDN Configuration
description: Learn about how to add a CDN configuration for an Edge Delivery site or a Cloud Manager environment.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer

---

# Add a CDN configuration {#add-cdn}

Adding a CDN configuration must be completed to configure a domain with an SSL.

>![NOTE]
>
>For Adobe-managed CDNs, when using DV certificates, only sites with ACME validation are permitted.

**To add a CDN configuration:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click **CDN Configurations**.

1. Near the upper-right corner of the CDN Configurations page, click **Add**. 

   ![Configure CDN dialog box](/help/implementing/cloud-manager/assets/configure-cdn-dialog.png)

1. In the **Configure CDN** dialog box, provide the necessary information.

   * From the **Origin** drop-down list, do one of the following:
     * **Sites:** Select an Edge Delivery Services site.
     * **Environments:** Select a Cloud Service environment.
        * **Tier:** Select a **Publish** or **Preview** web tier for the selected environment.
   * Select your CDN type: **Adobe managed CDN** or **Other CDN provider**.
   * Select the domain.
   * Select the SSL certificate. Only required if you selected **Adobe managed CDN** as your CDN type.

1. Click **Save**.




