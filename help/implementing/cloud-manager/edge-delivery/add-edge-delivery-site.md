---
title: Add an Edge Delivery Site to Cloud Manager
description: Learn how to add an Edge Delivery site to your production program or sandbox program and the benefits it brings.

feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Add an Edge Delivery site to Cloud Manager {#eds-add-site}

Learn how to add an Edge Delivery site to your production program or sandbox program and the benefits it brings.

## Introduction {#introduction}

As part of your Edge Delivery Services project with AEM as a Cloud Service, you are encouraged to add your Edge Delivery site to Cloud Manager. Adding your Edge Delivery website to Cloud Manager brings you the following benefits.

* [Access to Adobe-managed CDN](/help/implementing/cloud-manager/cdn-configurations/add-cdn-config.md)
* [Access to SLA reports](/help/implementing/cloud-manager/sla-reporting.md)
* [Access to licensing usage reports](/help/implementing/cloud-manager/license-dashboard.md)

Please note that adding your Edge Delivery Site to Cloud Manager is required in order to [register a support ticket for your Edge Delivery project.](/help/edge/overview.md##support-ticket)

## Adding and Edge Delivery site to Cloud Manager {#adding}

1. Log into Cloud Manager at [`https://my.cloudmanager.adobe.com`](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. Do one of the following:
    * From the **Program Overview** page, click the **Edge Delivery** tab. Then, near the lower-right corner of the page, click **Add Edge Delivery site**.

        ![Add Edge Delivery Site from the Edge Delivery tab](/help/implementing/cloud-manager/assets/cm-eds-add1.png)       

    * In the upper-left corner of the page, click the hamburger icon to reveal the left navigation menu. Under the **Services** heading, click **Edge Delivery Sites**. Near the upper-right corner of the page, click **Add site**.

        ![Add Edge Delivery Site from the Edge Delivery Sites button](/help/implementing/cloud-manager/assets/cm-eds-add2.png)

1. In the **Add Edge Delivery site** dialog box, provide the following information in the required fields:

    | Text field | Data to provide |
    | --- | --- |
    | Site Name | Enter the name of the Edge Delivery site that you are adding. The name serves as a unique identifier for the site within Cloud Manager. |
    | Repository URL | This field refers to the Git repository where your website's code is stored. This field allows Cloud Manager to pull the code from that repository during the deployment process.  |
    | Site description (optional) | Enter a brief description of the Edge Delivery site that you are adding. This description helps to identify and differentiate the site, making it easier to manage and recognize among other sites you have added. |

1. In the lower-right corner of the dialog box, click **Add**.

1. The **Verify repository ownership** dialog box opens. With it open, perform the following steps:

   1. Add a file with the path and name `well-known/adobe/cloudmanager-challenge.txt` to the `main` branch of the Git repository that is listed in the **Repository URL** field.
      * If necessary, click the **Copy** icon to copy the path to the clipboard.
      * Do *not* add a period at the start of the location path.
   1. Add the code from the **Step &num; 1** field to the file that you created in the previous step.
      * If necessary, click the **Copy** icon to copy the code to the clipboard.
   1. In the Git repository, create a pull request for the changes you just created and then merge it to `main`.

1. Click **Verify**.

After the repository is verified, its status in the Edge Deliver Sites table changes to a green circle with a white check mark inside of it.

Once you add Edge Delivery Services to a production program, your Edge Delivery Services license is applied to it. 

Each Edge Delivery site has a **Edge Delivery to-do- list** to guide you through the creation of your Edge Delivery site.

![Edge Delivery to-do app](/help/implementing/cloud-manager/assets/edge-delivery-to-do-ist.png)

Please see the document [Introduction to Edge Delivery Services in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/introduction-to-edge-delivery-services.md#ed-todo-list) for details on these steps.
