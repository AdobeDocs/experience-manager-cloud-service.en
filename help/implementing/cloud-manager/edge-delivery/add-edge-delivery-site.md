---
title: Add an Edge Delivery Site to Cloud Manager
description: Learn how to add an Edge Delivery site to your production program or sandbox program.
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
exl-id: 17e842c9-599a-4877-9834-1e7220f508a8
---
# Add an Edge Delivery site to Cloud Manager {#adding}

After you add an Edge Delivery site to your production program, your Edge Delivery Services license is applied to it.

Adding an Edge Delivery site to Cloud Manager is required to [register a support ticket for your Edge Delivery project](/help/edge/overview.md##support-ticket).

See also [Introduction to Edge Delivery Services in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/introduction-to-edge-delivery-services.md).

**To add an Edge Delivery site to Cloud Manager:**

1. Log into Cloud Manager at [`https://my.cloudmanager.adobe.com`](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. Do one of the following:

    * From the **Program Overview** page, click the **Edge Delivery** tab. Then, near the lower-right corner of the page, click **Add Edge Delivery site**.

        ![Add Edge Delivery site from the Edge Delivery tab](/help/implementing/cloud-manager/assets/cm-eds-add1.png)       

    * In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the left side menu.
    Under the **Services** heading, click ![Web page icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_WebPages_18_N.svg) **Edge Delivery Sites**.
    Near the upper-right corner of the page, click **Add site**.

        ![Add Edge Delivery site from the Edge Delivery Sites button](/help/implementing/cloud-manager/assets/cm-eds-add2.png)

1. In the **Add Edge Delivery site** dialog box, provide the following information in the required fields:

    | Text field | Description |
    | - | --- |
    | Site Name | Enter the name of the Edge Delivery site that you are adding.<br>The name serves as a unique identifier for the site within Cloud Manager. |
    | Repository URL | Enter the Git repository where your website's code is stored.<br>This field allows Cloud Manager to pull the code from that repository during the deployment process.  |
    | Site description (optional) | Enter a brief description of the Edge Delivery site that you are adding.<br>A description helps to identify and differentiate the site, making it easier to manage and recognize among other sites you have added. |

1. In the lower-right corner of the dialog box, click **Add**.

1. In the **Verify repository ownership** dialog box, verify the ownership of your repository by doing the following steps:

    | Step number | Description |
    | - | - |
    | **1** | Add a file with the path and name `well-known/adobe/cloudmanager-challenge.txt` to the `main` branch of the Git repository that is listed in the **Repository URL** field. Do *not* add a period at the start of the location path.<br>If necessary, click ![Copy](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Copy_18_N.svg) to copy the path to the clipboard. |
    | **2** | Add the code seen in the text field in Step 2 to the file that you just created in Step 1.<br>If necessary, click ![Copy](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Copy_18_N.svg) to copy the code to the clipboard. |
    | **3** | Create a pull request in the Git repository for the changes you just created, then merge it to `main` to commit the code. |

1. Click **Verify**.

When the repository is verified, its status in the Edge Delivery sites table gets updated. A green circle with a white check mark inside indicates the status.

In the same table, click ![Information about Edge Delivery site](https://spectrum.adobe.com/static/icons/workflow_18/Smock_InfoOutline_18_N.svg) to view site details. This information includes the verified Repository URL, along with the Preview and Production website URLs.
