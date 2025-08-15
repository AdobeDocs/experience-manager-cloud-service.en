---
title: Configure the AI Assistant in Adobe Experience Manager
description: Learn how to set up and configure the AI Assistant using the Admin console in Adobe Experience Manager.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
hide: yes
hidefromtoc: yes

---
# Configure AEM AI Assistant - Admin Setup {#aem-ai-asst-admin-setup}

An Administrator must configure access, permissions, and settings before users in their organizastion can use the features in AEM AI Assistant. This article describes how to enable the AI Assistant for your organization, set up required credentials, and save configuration changes.

**Overview of the AEM AI Assistant configuration process**

The configuration process consists of the following steps:

1. Create a new product profile in Adobe Admin Console.
1. Enable "AI Assistant Product Knowledge" permission.
1. Create or use an existing user group.
1. Add users to the user group.
1. Assign the product profile to the user group.

**Prerequisites**

Before you begin, be sure you have met the following prerequisites:

* You must have Product Administrator rights at a minimum in the Adobe Admin Console.
* You have an understanding of your organization's user management structure.

## 1 - Create a new product profile in Adobe Admin Console{#create-profile}

1. Follow the detailed instructions in [Create a new product profile in Adobe Admin Console](https://experienceleague.adobe.com/en/docs/experience-platform/access-control/ui/create-profile) found the Experience Platform documentation.

1. When creating the new product profile, use the following examples of the values you can use for the AI Assistant.

    | Text field | Suggested value |
    | --- | --- |
    | Product profile name | `AEM AI Assistant` (or your preferred descriptive name) |
    | Display name (optional) | `AI Assistant` |
    | Description (optional) | `Product profile for managing AEM AI Assistant access` |
    | Notification | Configure based on your organization's preferences |




## 2 - Enable "AI Assistant Product Knowledge" permission{#enable-permission}

The process for assigning custom permissions to product profiles follows the standard Adobe Cloud Manager custom permissions workflow.

Reference article: [Assign custom permissions to the new product profile](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/requirements/custom-permissions#assign-permissions)

1. In the Admin Console, click the name of your newly created product profile (`AEM AI Assistant`)

    ![Screenshot](/help/implementing/cloud-manager/assets/ai-assistant-console.png)

1. To view the list of editable permissions, click the **Permissions** tab.

1. In the table list, locate the `AI Assistant Product Knowledge` permission.

    ![AI Assistant Permissions tab in Admin Console](/help/implementing/cloud-manager/assets/ai-assistant-permission.png)

1. To the right of the permission name, click ![Pencil icon or Edit icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Edit_18_N.svg).

1. In the **Edit Permissions for AI Assistant** page, turn on the **AI Assistant Product Knowledge** toggle. 

    ![Edit Permissions page for the AI Assistant Product Knowledge toggle option](/help/implementing/cloud-manager/assets/ai-assistant-prod-knowledge.png)

1. In the lower-right corner of the page, click **Save**.

    Your product profile now has the AI Assistant Product Knowledge permission enabled.


## 3 - Create a user group (or use an existing user group){#create-user-group}

1. Do one of the following:

>[!BEGINTABS]

>[!TAB Create a new user group]

1. In Admin Console, click **Users** > **User groups**.

    ![User groups](/help/implementing/cloud-manager/assets/ai-assistant-user-groups.png)

1. In the **User groups** page, click **New user group**.

    ![New user group button on the User groups page](/help/implementing/cloud-manager/assets/ai-assistant-new-user-group.png)

1. In the **Create a new user group** page, provide the following information:
 
    | Option | Suggested value |
    | --- | --- |
    | User group name | `AEM AI Assistant` (or your preferred name) |
    | Description (optional) | `User group for managing AEM AI Assistant access` |

    ![Create a new user group page](/help/implementing/cloud-manager/assets/ai-assistant-create-new-user-group.png)

1. In the lower right corner of the page, click **Save**.

>[!TAB Use an exisiting user group] 

Use an existing AEM user group if it meets AI Assistant access requirements, instead of creating a new group.

>[!ENDTABS]


## 4 - Add users to the user group{#add-users}


## 5 - Assign the product profile to the user group{#assign-product-profile}


