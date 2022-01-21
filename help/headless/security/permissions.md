---
title: Permission considerations for headless content 
description: Learn about different permission and ACL considerations for a headless implementation with Adobe Experience Manager. Understand the different personas and potential permission levels needed for both Author and Publish environments.
feature: Content Fragments,GraphQL API
---

# Permission considerations for headless content

With a headless implementation there are several areas of security and permissions that should be addressed. Permissions and personas can be broadly be considered based on the AEM environment **Author** or **Publish**. Each environment will contain different personas and with different needs.

## Author Service Considerations

The Author service is where internal users create, manage, and publish content. Permissions revolve around the different personas who will be managing content.

### Manage permissions at the Group level

As a best practice, permissions should be set on Groups in AEM. Also known as local groups, these groups can be managed within the AEM author environment. 

The easiest way to manage group membership is to use Adobe Identity Management System (IMS) groups and assign [IMS groups to local AEM groups](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/security/ims-support.html?lang=en#managing-permissions-in-aem). 

![Admin console permission flow](assets/admin-console-aem-group-permissions.png)

At a high level the process is:

1. Add IMS Users to a new or existing IMS User group using the [Admin Console](https://adminconsole.adobe.com/)
1. IMS Groups will be synced with AEM when users login.
1. Assign IMS groups to AEM Groups.
1. Set permissions on AEM Groups. 
1. When users login to AEM and are authenticated via IMS they will inherit the permissions of the AEM group.

>[!TIP]
>
> A detailed video walkthrough of managing IMS and AEM users and groups can be found [here](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/overview.html).

To manage **groups** in AEM navigate to **Tools** > **Security** > **Groups**.

![Navigate to Group console](assets/group-console.png)

To manage permissions of groups in AEM navigate to **Tools** > **Security** > **Permissions**.

### DAM Users

"DAM", in this context, stands for Digital Asset Management. The **DAM Users** is an out of the box group in AEM that can be used for "everyday" users that will be managing digital assets and Content Fragments. This group provides permissions to **view**, **add**, **update**, **delete**, and **publish** Content Fragments and all other files in AEM Assets.

![Adding an IMS Group to DAM User group](assets/add-ims-group-dam-users.png)

If using IMS for group membership you would add the appropriate IMS Group(s) as a member of the **DAM Users** group. Members of the IMS group will then inherit the permissions of the DAM Users group when logging into the AEM environment.

#### Customizing DAM Users Group

It is best not to modify permissions of an out of the box group directly. Instead, you can also create your own group(s) modeled after the **DAM Users** group permissions and further restrict access to different **folders** within AEM Assets.

This would be done by navigating to the **Permissions** console in AEM and updating the path from `/content/dam` to a more specific path, i.e `/content/dam/mycontentfragments`.

![Permissions console dam users](assets/permission-screen-dam-users.png)

It may be desirable to give this group of users permissions to create and edit content fragments but not **delete**. Follow this guide to [assign the appropriate permissions to edit but not delete](/help/assets/content-fragments/content-fragments-delete.md).

### Model editors

The ability to modify **Content Fragment Models** should be left to administrators or a **small group** of users with elevated permissions. Modifying the Content Fragment Model has many downstream effects. 

>[!CAUTION]
>
>Modifications to the Content Fragment Model changes the underlying GraphQL API that headless applications rely on.

If you wish you to create a group that has the ability to manage Content Fragment Models but *not* full administrator access you can create a group with the following access control entries:

| Path | Permission | Privileges|
|-----| -------------| ---------|
|`/conf`| **allow**    | `jcr:read` |
| `/conf/<config-name>/settings/dam/cfm` | **allow** | `rep:write`, `crx:replicate` |

For example below a group named **model-editors** is given permission to modify the WKND Content Fragment Models:

![Sample model Editor group](assets/sample-model-editor-group.png)

## Publish Service Permissions

The Publish service is considered the “Live” environment and is typically what end users interact with. Content, after being edited and approved on the Author service, is distributed to the Publish service. The most common deployment pattern with AEM headless applications is to have the production version of the application connect to an AEM Publish service.