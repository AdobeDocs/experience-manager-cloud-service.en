---
title: Repository Browser
seo-title: Repository Browser
description: The repository browser provides a read-only view into the repository for all environments on author, publish, and preview tiers.
seo-description: The repository browser provides a read-only view into the repository for all environments on author, publish, and preview tiers.
---

# Repository Browser {#repository-browser}

## Introduction {#introduction}

The repository browser is a developer tool that provides a read-only view into the repository for all environments on author, publish and preview tiers. It is designed to facilitate viewing of the content structure in order to make it easier to see or debug content.

Accessible from the Developer Console, it can be used to browse the repository of any instance or pod for a selected environment.

### Access Prerequisites {#access-prerequisites}

These following conditions must be met in order to access the Developer Console or the Repository browser

In order to access Developer Console:

* For Production programs, users must have the **Cloud Manager - Developer Role** in the Admin Console
* For sandbox programs, it is available to any user with a product profile giving them access to AEM as a Cloud Service.

In order to access the Repository Browser:

* Users must have the **Cloud Manager - Developer** Role in the Admin Console
* Users must also be defined in the AEM Users or AEM Administrators Product Profile on both the author and publish services

For more information about setting up user permissions, see the [Cloud Manager Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/requirements/setting-up-users-and-roles.html).

### Launching the Repository Browser {#launching-the-repository-browser}

The repository browser can be launched by following the steps below.

1. In Cloud Manager, click the three dots next to the tier of your choice, and select **Developer Console**

   ![repobrowser1](/help/implementing/developing/tools/assets/repobrowser1.png)

1. Next, click the **Repository Browser** tab   
1. Choose any pod corresponding to author, publish or preview by clicking on the **Pod** dropdown list.

   ![repobrowser2](/help/implementing/developing/tools/assets/repobrowser2.png)

1. Launch the repository browser by clicking on the **Open Repository Browser** link further down. This will launch the browser corresponding to a representative instance (pod) for the chosen tier. This will launch the browser corresponding to a representative instance (pod) for the chosen tier. Note that you cannot control the specific pod for that tier that is launched.

## Features {#features}

### Navigate the Hierarchy {#navigate-the-hierarchy}

You can use the left hand navigation pane to nagivate through the content hierarchy. Clicking on each folder or node will reveal its children.

![repobrowser3](/help/implementing/developing/tools/assets/repobrowser3.png)

### View JCR Properties {#view-jcr-properties}

Clicking on a node will reveal its JCR properties in the right hand pane of the navigation browser. Below is an example for the `experience-fragments` node.

![repobrowser4](/help/implementing/developing/tools/assets/repobrowser41.png)

### View Content {#view-content}

You can use the repository browser to view content.

### Download Content {#download-content}

You can also use the repository browser to download content.