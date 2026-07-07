---
title: Content Fragments - Cloud Configurations
description: Learn how to use Content Fragment Cloud Configurations to customize your Content Fragment environment.
feature: Content Fragments
role: User, Developer
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
solution: Experience Manager Sites
---
# Content Fragments - Cloud Configurations {#content-fragments-setup}

With a Content Fragment Cloud Configuration you can customize various aspects of your Content Fragment environment, including certain actions and the [new Content Fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md). 

After [creating](#create-a-content-fragment-cloud-configuration) and defining the configuration you also [apply the Cloud Configuration to your individual Assets folders](#apply-the-configuration-to-your-folder), so that it is applied to all the Content Fragments in that folder.

>[!NOTE]
>
>The Content Fragment Cloud Configurations do not impact the original Content Fragment editor.

## Create a Content Fragment Cloud Configuration  {#create-a-content-fragment-cloud-configuration}

To create a configuration for customizing the new Content Fragment editor:

1. Navigate to **Tools**, **Cloud Services**, then open the **Content Fragment Cloud Configuration**.
1. In the left panel select the name of the configuration you created in the Configuration Browser; for example `CFModels-Conf`.
1. Select **Create** from the top right toolbar.
1. Select **Configuration** from the dropdown menu.
1. A new configuration name **Content Fragment Cloud Configuration** is created.
   You can select the configuration to edit the properties, publish, unpublish or delete.

   >[!NOTE]
   >
   >For each configuration only one Cloud Configuration can be created.

## Disable Publishing {#disable-publishing}

Use this option to disable publishing for all Content Fragments in a folder.

1. Navigate to your Content Fragment Cloud Configuration.
1. Select and open the **Properties**.
1. Select the **Capabilities** tab.
1. Select, or deselect, **Disable Publish.**.
1. **Save and Close**.
1. [Apply the Cloud Configuration to your folder](#apply-the-configuration-to-your-folder).

## Configure the Editor - RTE{#configure-the-editor-rte}

Use this option to configure the RTE in the new Content Fragment editor, for all Content Fragments in a folder.

1. Navigate to your Content Fragment Cloud Configuration.
1. Select and open the **Properties**.
1. Select the **Filter** tab.
1. Select the **RTE** tab.


## Configure the Editor - Content Reference Selector{#configure-the-editor-content-reference-selector}

Use this option to configure the Asset Selector in the new Content Fragment editor, for all Content Fragments in a folder.

1. Navigate to your Content Fragment Cloud Configuration.
1. Select and open the **Properties**.
1. Select the **Filter** tab.
1. Select the **Assets** tab.


## Apply the Configuration to your Folder {#apply-the-configuration-to-your-folder}

When the configuration **global** is enabled for Content Fragment functionality, it then applies to any Assets folder - accessible through the **Assets** console.

To use other configurations (therefore excluding global) with a comparable Assets folder, you have to define the connection. Do this by selecting the appropriate **Configuration** in the **Cloud Services** tab of the **Folder Properties** of the appropriate folder.

![Apply configuration](/help/sites-cloud/administering/content-fragments/assets/cf-setup-apply-conf.png)