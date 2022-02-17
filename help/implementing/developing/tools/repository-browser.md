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

### Launching the Repository Browser {#launching-the-repository-browser}

The repository browser can be launched by following the steps below.

1. In Cloud Manager, click the three dots next to the environment of your choice, and select **Developer Console**

   ![repobrowser1](/assets/repobrowser1.png)

1. Next, click the **Repository Browser** tab   
1. Choose a pod corresponding to either author, publish, or preview by clicking on the **Pod** dropdown list.

   ![repobrowser2](/assets/repobrowser2.png)

1. Launch the repository browser by clicking on the **Open Repository Browser** link further down. This will launch the browser corresponding to a representative instance (pod) for the chosen environment.

## Features {#features}

### Navigate the Hierarchy {#navigate-the-hierarchy}

You can use the left hand navigation pane to nagivate through the content hierarchy. Clicking on each folder or node will reveal its children.

![repobrowser3](/assets/repobrowser3.png)

### View JCR Properties {#view-jcr-properties}

Clicking on a node will reveal its JCR properties in the right hand pane of the navigation browser. Below is an example for the `experience-fragments` node.

![repobrowser4](/assets/repobrowser41.png)

### View Content {#view-content}

You can use the repository browser to view content.

### Download Content {#download-content}

You can also use the repository browser to download content.