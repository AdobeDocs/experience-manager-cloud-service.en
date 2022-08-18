---
title: Repository Browser
seo-title: Repository Browser
description: The repository browser provides a read-only view into the repository for all environments on author, publish, and preview tiers.
seo-description: The repository browser provides a read-only view into the repository for all environments on author, publish, and preview tiers.
exl-id: 22473a97-8f7b-4014-b885-1233116aeda6
---
# Repository Browser {#repository-browser}

>[!NOTE]
>
>The Repository Browser is available on AEM versions 6582 and higher.

>[!INFO]
>
>You can also watch [this clip](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/repository-browser.html) for a quick video introduction on how to use the Repository Browser to debug AEM as a Cloud Service.

## Introduction {#introduction}

The repository browser is a developer tool that provides a read-only view into the repository for all environments on author, publish and preview tiers. It is designed to facilitate viewing of the content structure in order to make it easier to see or debug content.

Accessible from the Developer Console, it can be used to browse the repository of an author or publish instance for a selected environment.

### Access Prerequisites {#access-prerequisites}

These following conditions must be met in order to access the Developer Console or the Repository browser

In order to access Developer Console:

* For Production programs, users must have the **Cloud Manager - Developer Role** in the Admin Console
* For sandbox programs, it is available to any user with a product profile giving them access to AEM as a Cloud Service.

In order to access the Repository Browser:

* Users must have the **Cloud Manager - Developer** Role in the Admin Console to view Author and Publish instances.
* In addition, for author, users with the AEM Users Product Profile can view the repository browser with minimal read access; the user's permissions are respected when browsing the repository. Users with the AEM Administrators Product Profile can view the repository browser with full read access.

For more information about setting up user permissions, see the [Cloud Manager Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/requirements/setting-up-users-and-roles.html).

### Launching the Repository Browser {#launching-the-repository-browser}

The repository browser can be launched by following the steps below.

1. In Cloud Manager, click the three dots next to the environment of your choice, and select **Developer Console**

   ![repobrowser1](/help/implementing/developing/tools/assets/repobrowser1.png)

1. Next, click the **Repository Browser** tab   
1. Choose any pod corresponding to author, publish or preview by clicking on the **Pod** dropdown list.

   ![repobrowser2](/help/implementing/developing/tools/assets/repobrowser2.png)

1. Launch the repository browser by clicking on the **Open Repository Browser** link further down. This will launch the browser corresponding to a representative instance (pod) for the chosen tier. This will launch the browser corresponding to a representative instance (pod) for the chosen tier. Note that you cannot control the specific pod for that tier that is launched.

## Features {#features}

### Navigate the Hierarchy {#navigate-the-hierarchy}

You can use the left hand navigation pane to nagivate through the content hierarchy. Clicking on each folder or node will reveal its children. The folder structure reflects the Sling Resource tree, which is a super-set of the JCR Node tree.

![repobrowser3](/help/implementing/developing/tools/assets/repobrowser3.png)

Alternatively, you can navigate directly to a path by entering it in the **Path** field, as shown below. This will also expand its location in the content hierarcy view on the left.

![repobrowser14](/help/implementing/developing/tools/assets/repobrowser14.png)

Whenever you click a folder on the left, the Path field automatically populates with its location. This is useful for copying and pasting the value for later usage.

Additionally, when you click on a folder, the URL is dynamically modified to include the path to that folder. This allows for bookmarkable URLs.

For publish, by default, the Repository Browser will only show public content, thus certain folders like `/conf` or `/home` will not be visible. 

In order to make those locations visible, you need to follow the below procedure.

1. Click the three dots next to the environment of your choice and select **Manage Access**

   ![repobrowser7](/help/implementing/developing/tools/assets/repobrowser7.png)

1. Find your publish instance, then click on it

   ![repobrowser8](/help/implementing/developing/tools/assets/repobrowser8.png)

1. Create a new product profile for publish administrators. In the example below, it is called **DEV - AEM Administrators Publish**

   ![repobrowser9](/help/implementing/developing/tools/assets/repobrowser9.png)

1. Add the appropriate users, corresponding to who should be able to navigate the publish repository browser with full access, to the new product profile

   ![repobrowser10](/help/implementing/developing/tools/assets/repobrowser10.png)

1. Wait for a few minutes, then open the **AEM author** console
1. Add the group corresponding to the new product profile as a member of the administrators group. You can do this by clicking on **Tools - Security - Groups on author**, then clicking on the **administrators** group. Then, add the group as shown below

   ![repobrowser11](/help/implementing/developing/tools/assets/repobrowser11.png)

1. Activate the **administrators** and the new **DEV - AEM Administrators Publish** group so that they become available on publish

   ![repobrowser12](/help/implementing/developing/tools/assets/repobrowser12.png)

1. As a good security practice, remove the new **DEV - AEM Administrators Publish** group from the administrators group on **author** so the new group is isolated to publish 

   ![repobrowser13](/help/implementing/developing/tools/assets/repobrowser13.png)

1. Upon accessing repository browser for a publish instance, all folders are visible, including `/home` and `/conf`.

### View JCR Properties {#view-jcr-properties}

Clicking on a node will reveal its JCR properties in the right hand pane of the navigation browser. Below is an example for the `experience-fragments` node.

![repobrowser4](/help/implementing/developing/tools/assets/repobrowser41.png)

### View Content {#view-content}

You can use the repository browser to view content by clicking on a resource in the navigation pane. This will open a preview on the right hand side of the browser, under a tab named after the respective resource.

![repobrowser6](/help/implementing/developing/tools/assets/repobrowser61.png)

Preview is currently available for image types in the list below:

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
