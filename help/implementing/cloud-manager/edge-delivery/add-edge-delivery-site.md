---
title: Add an Edge Delivery Site to Cloud Manager
description: Learn how to add an Edge Delivery site to your production program or sandbox program.

feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

## Add an Edge Delivery site to Cloud Manager {#eds-add-site}

After you add Edge Delivery Services to a production program, your Edge Delivery Services license is applied to it. 

A clickable tab called **Edge Delivery** is seen on the Overview page. Clicking the tab displays a table that lists each Edge Delivery site you have added. In the left navigation panel, under the **Services** grouping, notice the menu option named **Edge Delivery Sites**.

![Overview page showing Edge Delivery Sites in left navigation panel and Edge Delivery tab to the right of the Publish Delivery tab](/help/implementing/cloud-manager/assets/cm-overview-eds.png)

**To add an Edge Delivery site to Cloud Manager:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate program.
1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program with Edge Delivery Services configured, where you want to add an Edge Delivery site.
1. Do either one of the following:
    * From the **Program Overview** page, click the **Edge Delivery** tab. Then, near the lower-right corner of the page, click **Add Edge Delivery site**.

        ![Add Edge Delivery Site from the Edge Delivery tab](/help/implementing/cloud-manager/assets/cm-eds-add1.png)

        The **Edge Delivery to-do list**, as seen in the image above, is an optional onboarding checklist guide meant to help you get started with using Edge Delivery. See [About the Edge Delivery to-do list](#ed-todo-list).

    * In the upper-left corner of the page, click the hamburger icon to reveal the left navigation menu. Under the **Services** heading, click **Edge Delivery Sites**. Near the upper-right corner of the page, click **Add site**.

        ![Add Edge Delivery Site from the Edge Delivery Sites button](/help/implementing/cloud-manager/assets/cm-eds-add2.png)

1. In the **Add Edge Delivery site** dialog box, do the following:

    | Text field | What to do |
    | --- | --- |
    | Site Name | Enter the name of the Edge Delivery site that you are adding. The name serves as a unique identifier for the site within Cloud Manager. |
    | Repository URL | This field refers to the Git repository where your website's code is stored.<br>Enter the URL of the Git repository that contains the necessary files and resources (such as HTML, CSS, JavaScript, and other web assets) for your Edge Delivery site. This arrangement allows Cloud Manager to pull the code from that repository during the deployment process.  |
    | Site description (optional) | Enter a brief description of the Edge Delivery site that you are adding.<br>This description helps to identify and differentiate the site, making it easier to manage and recognize among other sites you have added. You may want to include details about the site's purpose, content, or any other relevant information that can help clarify its function or scope. |

1. In the lower-right corner of the dialog box, click **Add**.

1. In the **Verify repository ownership** dialog box, do each of the following:

    | Step | Description |
    | --- | --- |
    | 1 | Add a file with the location path to the `main` branch of the Git repository that is listed in the **Repository URL** field. If necessary, click the Copy icon to copy the path to the clipboard.<br> The location path is:<br>`well-known/adobe/cloudmanager-challenge.txt`.<br><br>Do *not* add a period at the start of the location path, is in:<br>`.well-known/adobe/cloudmanager-challenge.txt` |
    | 2 | Add the generated code to the file that you created in Step 1. If necessary, click the Copy icon to copy the code to the clipboard. |
    | 3 | In the Git repository, create a pull request, then merge it to commit the code. |

1. Click **Verify**. After the repository is verified, its status in the Edge Deliver Sites table changes to a green circle with a white check mark inside of it.
