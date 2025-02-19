---
title: One Click Edge Delivery Site Creation in Cloud Manager
description: Learn how to quickly create an Edge Delivery Site in Cloud Manager with the click of a button.

feature: Cloud Manager, Developing
role: Admin, Architect, Developer

---

# About One click Edge Delivery site creation in Cloud Manager {#about-one-click-edge-delivery-site}

The one click Edge Delivery site feature is designed to help you automate the onboarding and deployment of Edge Delivery sites within Cloud Manager. It greatly simplifies the process by having you click a single button. That single click provisions the required infrastructure, integrates with GitHub for version control, and configures your document and asset storage in Google Drive.

This automation helps reduce the manual effort that is required to set up your initial site. It ensures seamless workflows, scalability, and improves the performance of your teams when it comes to managing content at the edge.

## Key concepts {#key-concepts}

Key concepts when you use one click to create an Edge Delivery site.

| Key concept | Description |
| --- | --- |
| Automated Edge deployment | <ul><li>Users can create and configure Edge Delivery sites instantly.</li><li>It reduces or eliminates the need for manual onboarding processes by using Cloud Manager's integration with CI/CD workflow.</li><li>Integrated with Cloud Manager for seamless CI/CD workflows.</li></ul> |
| Integration with Cloud Manager | <ul><li>Uses Cloud Manager's user interface to trigger the One Click Edge Delivery process.</li><li>Provides access to automated repository creation and deployment.</li></ul> |
| GitHub-based version control | <ul><li>Creates a GitHub repository within an organization using pre-defined boilerplate templates to standardize deployments.</li><li>Links with AEM Bot for content updates.</li></ul> |
| Document and asset storage integration | <ul><li>Generates a Google Drive folder for storage.<li>Installs the AEM Code Sync application on the repository, ensuring seamless synchronization and deployment.</li></li><li>Allows multiple collaborators to manage documents easily.</li></ul> |
| Security and scalability | <ul><li>Ensures compliance with enterprise security standards.</li><li>Supports multiple Edge Delivery Sites under different Cloud Manager tenants.</li></ul> |

<!-- >
## Practical use cases {#use-cases}

| Use case | Description |
| --- | --- |
| Website and application deployment | <ul><li>Automate the hosting and delivery of static or dynamic sites.</li><li>Ensure fast performance through edge caching. </li></ul> |
| API gateway and content delivery | <ul><li>Optimize API responses by caching data at the edge.</li><li>Reduce backend load and improved response times. </li></ul> |
| Real-time content updates | <ul><li>Instant deployment of new content across edge locations.</li><li>Support integration with automated content pipelines. </li></ul> |
| Edge computing workloads | <ul><li>Support serverless computing to process workloads closer to users.</li><li>Reduce latency and enhance performance. </li></ul> |
| Security and governance | <ul><li>Security is provided with integrated DDoS (Distributed Denial of Service) protection and WAF (Web Application Firewall) integration.</li><li>Ensure that content is delivered securely through TLS (Transport Security Layer) encryption. </li></ul> |
-->

## Create an Edge Delivery site in Cloud Manager with one click {#one-click-edge-delivery-site}

To create an Adobe Edge Delivery site with one click, your organization must have an available Edge Delivery Services license. This license is part of Adobe Experience Manager (AEM) and is necessary for creating Edge Delivery Services within Cloud Manager.

In terms of permissions, you must be a member of the Business Owner role or have been granted the appropriate permissions to add or edit programs in Cloud Manager. This access level lets you manage the integration of Edge Delivery Services into your programs.

See also [Introduction to Edge Delivery Services in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/introduction-to-edge-delivery-services.md).

<!-- PROPER AEM BOT CONFIGURATIONS MUST BE IN PLACE FIRST FOR AUTOMATIC CONTENT UPDATES? TRUE or FALSE? -->

**To create an Edge Delivery site in Cloud Manager with one click:**

1. Log into Cloud Manager at [`https://my.cloudmanager.adobe.com`](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the left side menu.
1. In the left side menu, under the **Program** heading, click **Overview**.
1. On the **Program Overview** page, click the **Edge Delivery** tab.
1. On the Edge Delivery page, In the **Edge Delivery to-do list** dialog box, in the **Complete prerequisites** group box, click **Provision**.
1. In the **Provision Edge Delivery site** dialog box, in the **Project Name** text field, enter the name of your site, then click **Provision**.

    A toast appears near the top-center of the screen letting you know that Edge Delivery site provisioning has started.

  When provisioning is complete and your site is validated by Cloud Manager, the **Site name** (the project name you entered earlier) appears in the **Edge Delivery sites** list box on the Edge Delivery page. Also, a green check mark appears to the left of the repository URL.


### Explore an Edge Delivery site created with one click {#explore-one-click-ed-site}

1. Log into Cloud Manager at [`https://my.cloudmanager.adobe.com`](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the left side menu.
1. In the left side menu, under the **Program** heading, click **Overview**.
1. On the **Program Overview** page, click the **Edge Delivery** tab.
1. On the Edge Delivery page, do any one of the following:

    | What to explore | Steps |
    | --- | --- |
    | GitHub repository of a site | <ul><li>In the **Edge Delivery sites** list box, under the **Repository** column heading, click the URL of the site you just created.</li> |
    | Publish a site | <ul><li> In the **Edge Delivery sites** list box, to the far right of your site's name, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) to open the drop-down menu.</li><li>Click ![Bell icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Bell_18_N.svg) **Publish site** in the drop-down menu.<br>A toast message appears letting you know that publishing of the site was successfully started.</li></ul> |
    | Preview a published site | <ul><li>In the **Edge Delivery sites** list box, under the **Site name** column heading, click the URL of the site you just created and published.<br>In the URL Address bar of your browser, note that the site's URL ends with `.page` indicating that you are seeing a preview of the site.</li><li>To see the site live, manually change `.page` to `.live` in the URL Address bar.</li></ul> | 
    | Add a collaborator to your site | <ul><li> In the **Edge Delivery sites** list box, to the far right of your site's name, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) to open the drop-down menu.</li><li>Click ![Add Circle icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_AddCircle_18_N.svg) **Gain access** in the drop-down menu.</li><li>In the **Add a collaborator to your site** dialog box, enter the email address of a contributor, then click **Add collaborator**.<br>A toast message appears letting you know that the collaborator was successfully added to the site.<br>The collaborator receives an email invitation to contribute to a shared Google drive folder by clicking **Open** in the email; there is no need to log in. They can edit and update files in the shared folder, then click **Publish site** in Cloud Manager, as described above. They can also preview the changes made, as described above.</li></ul> |
