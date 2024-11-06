---
title: Manage Edge Delivery Sites in Cloud Manager
description: Learn how to add a CDN configuration to an Edge Delivery site or delete an Edge Delivery site.
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
exl-id: 960aa3c6-27b9-44b1-81ea-ad8c5bbc99a5
---
# Manage Edge Delivery site in Cloud Manager {#manage-edge-delivery-sites}

Learn how to manage Edge Delivery sites in Cloud Manager by adding a CDN configuration to an existing site. Or, delete an Edge Delivery site.

## Add a CDN configuration to an existing Edge Delivery site {#add-cdn-to-edge-delivery-site}

See [Add a CDN configuration](/help/implementing/cloud-manager/cdn-configurations/add-cdn-config.md).

## Rename an Edge Delivery Site (#rename-edge-delivery-site)

In Adobe Cloud Manager, you may want to rename an Edge Delivery site for several reasons:

* **Clarity and organization**: To describe the site's purpose better or its associated environment (for example, production, staging).
* **Avoiding confusion**: If multiple sites are in use, renaming can help easily differentiate between them, reducing the chance of applying configurations or updates to the wrong site.
* **Standardization**: To follow a consistent naming convention that aligns with your organization's guidelines for easier management and auditing.

**To rename an Edge Delivery site:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program with Edge Delivery Services configured, where you want to add an Edge Delivery site.
1. Do either one of the following:

    * From the **Program Overview** page, click the **Edge Delivery** tab. In the Edge Delivery site table, click the ellipsis at the end of a row whose site you want to rename. 
    Click **Rename**.
    * In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the left side menu. Under the **Services** heading, click ![Web pages icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_WebPages_18_N.svg) **Edge Delivery Sites**. 
    In the Edge Delivery site table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose site you want to rename. Click **Rename**.

1. In the **Edit Edge Delivery Site** dialog box, in the **Site Name** text field, enter the new name of the site.

1. Click **Edit**.

## Delete an Edge Delivery site {#delete-edge-delivery-site}

If you delete an Edge Delivery Services site, any associated CDN configurations are removed as well. This action breaks the connection between custom domains and the site. For more details, see CDN configurations. <!-- https://wiki.corp.adobe.com/display/DMSArchitecture/%5BKT%5D+Cloud+Manager+2024.9.0+Release -->

**To delete an Edge Delivery site:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program with Edge Delivery Services configured, where you want to add an Edge Delivery site.
1. Do either one of the following:

    * From the **Program Overview** page, click the **Edge Delivery** tab. In the Edge Delivery site table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose site you want to remove. 
    Click ![Delete Edge Delivery site](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Delete_18_N.svg) **Delete**, then click **Delete** again to confirm the site's removal.

        ![Add Edge Delivery Site from the Edge Delivery tab](/help/implementing/cloud-manager/assets/cm-eds-delete1.png)

    * In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg ) to reveal the left side menu. Under the **Services** heading, click ![Web page for Edge Delivery sites](https://spectrum.adobe.com/static/icons/workflow_18/Smock_WebPages_18_N.svg) **Edge Delivery Sites**. 
    In the Edge Delivery site table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose site you want to remove. Click ![Delete Edge Delivery site](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Delete_18_N.svg) **Delete**, then click **Delete** again to confirm the site's removal.

        ![Add Edge Delivery Site from the Edge Delivery Sites button](/help/implementing/cloud-manager/assets/cm-eds-delete2.png)

## Log a support ticket {#eds-support-ticket}

{{support-ticket}}
