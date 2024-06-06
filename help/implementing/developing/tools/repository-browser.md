---
title: Repository Browser
seo-title: Repository Browser
description: The repository browser provides a read-only view into the repository for all environments on author, publish, and preview tiers.
seo-description: The repository browser provides a read-only view into the repository for all environments on author, publish, and preview tiers.
exl-id: 22473a97-8f7b-4014-b885-1233116aeda6
feature: Developing
role: Admin, Architect, Developer
---
# Repository Browser {#repository-browser}

>[!NOTE]
>
>The Repository Browser is available on AEM versions 6582 and higher.

>[!INFO]
>
>You can also watch [this clip](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/repository-browser.html) for a quick video introduction on how to use the Repository Browser to debug AEM as a Cloud Service.

## Introduction {#introduction}

The repository browser is a developer tool that provides a read-only view into the repository for all environments on author, publish, and preview tiers. It is designed to facilitate viewing of the content structure to make it easier to see or debug content.

Accessible from the [AEM as a Cloud Service Developer Console](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console), it can be used to browse the repository of an author or publish instance for a selected environment.

### Access Prerequisites {#access-prerequisites}

These following conditions must be met to access the AEM as a Cloud Service Developer Console or the Repository browser

To access the AEM as a Cloud Service Developer Console:

* For Production programs, users must have the **Cloud Manager - Developer Role** in the Adobe Admin Console
* For sandbox programs, it is available to any user with a product profile giving them access to AEM as a Cloud Service.

To access the Repository Browser:

* Users must have the **Cloud Manager - Developer** Role in the AEM as a Cloud Service Developer Console to view Author and Publish instances.
* In addition, for author, users with the AEM Users Product Profile can view the repository browser with minimal read access; the user's permissions are respected when browsing the repository. Users with the AEM Administrators Product Profile can view the repository browser with full read access.

For more information about setting up user permissions, see the [Cloud Manager Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/content/requirements/users-and-roles.html).

### Launching the Repository Browser {#launching-the-repository-browser}

The repository browser can be launched by following the steps below.

1. In Cloud Manager, click the three dots next to the environment of your choice, and select **Developer Console**

   ![repobrowser1](/help/implementing/developing/tools/assets/repobrowser1.png)

1. Next, click the **Repository Browser** tab   
1. Choose any pod corresponding to author, publish, or preview by clicking the **Pod** drop-down list.

   ![repobrowser2](/help/implementing/developing/tools/assets/repobrowser2.png)

1. Launch the repository browser by clicking the **Open Repository Browser** link further down. The browser corresponding to a representative instance (pod) for the chosen tier is launched. You cannot control the specific pod for that tier that is launched.

## Features {#features}

### Navigate the Hierarchy {#navigate-the-hierarchy}

You can use the left-hand navigation pane to navigate through the content hierarchy. Clicking each folder or node reveals its children. The folder structure reflects the Sling Resource tree, which is a super-set of the JCR Node tree.

![repobrowser3](/help/implementing/developing/tools/assets/repobrowser3.png)

Alternatively, you can navigate directly to a path by entering it in the **Path** field, as shown below. This path also expands its location in the content hierarchy view on the left.

![repobrowser14](/help/implementing/developing/tools/assets/repobrowser14.png)

When you click a folder on the left, the Path field automatically populates with its location. This functionality is useful for copying and pasting the value for later usage.

Also, when you click a folder, the URL is dynamically modified to include the path to that folder. This functionality allows for bookmarkable URLs.

For publish, by default, the Repository Browser only shows public content, therefore certain folders like `/conf` or `/home` are not visible. 

To make those locations visible, do the following.

1. Click the three dots next to the environment of your choice and select **Manage Access**

   ![repobrowser7](/help/implementing/developing/tools/assets/repobrowser7.png)

1. Find your publish instance, then click it

   ![repobrowser8](/help/implementing/developing/tools/assets/repobrowser8.png)

1. Create a product profile for publish administrators. In the example below, it is called **DEV - AEM Administrators Publish**

   ![repobrowser9](/help/implementing/developing/tools/assets/repobrowser9.png)

1. Add the appropriate users, corresponding to who should be able to navigate the publish repository browser with full access, to the new product profile

   ![repobrowser10](/help/implementing/developing/tools/assets/repobrowser10.png)

1. Wait for a few minutes, then open the **AEM author** console
1. Add the group corresponding to the new product profile as a member of the administrator's group by clicking **Tools - Security - Groups on author**, then clicking the **administrators** group. Then, add the group as shown below

   ![repobrowser11](/help/implementing/developing/tools/assets/repobrowser11.png)

1. Activate the **administrators** and the new **DEV - AEM Administrators Publish** group so that they become available on publish

   ![repobrowser12](/help/implementing/developing/tools/assets/repobrowser12.png)

1. As a good security practice, remove the new **DEV - AEM Administrators Publish** group from the administrator's group on **author** so the new group is isolated to publish 

   ![repobrowser13](/help/implementing/developing/tools/assets/repobrowser13.png)

1. Upon accessing repository browser for a publish instance, all folders are visible, including `/home` and `/conf`.

### View JCR Properties {#view-jcr-properties}

Clicking a node reveals its JCR properties in the right-hand pane of the navigation browser. Below is an example for the `experience-fragments` node.

![repobrowser4](/help/implementing/developing/tools/assets/repobrowser41.png)

### View Content {#view-content}

You can use the repository browser to view content. Click a resource in the navigation pane so you open a preview on the right-hand side of the browser, under a tab named after the respective resource.

![repobrowser6](/help/implementing/developing/tools/assets/repobrowser61.png)

Preview is available for the following image types:

* apng
* avif
* gif
* jpeg
* png
* svg+xml
* webp
* bmp
* x-icon
* tiff

And for the following text-based mime-types:

* `"text/*"`
* `'application/javascript'`
* `'application/json'`
* `'application/x-sh'`

### Download Content {#download-content}

You can also use the repository browser to download content. In the example below, you can press the **download** link to download the `jcr:data` associated with the selected node. This feature is available for all binary properties by navigating to the node containing the property definition.

![repobrowser5](/help/implementing/developing/tools/assets/repobrowser52.png)
