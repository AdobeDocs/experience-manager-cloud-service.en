---
title: Content Fragments - Cloud Configurations
description: Learn how to use Content Fragment Cloud Configurations to customize your Content Fragment environment.
feature: Content Fragments
role: User, Developer
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
solution: Experience Manager Sites
---
# Content Fragments - Cloud Configurations {#content-fragments-setup}

With a Content Fragment Cloud Configuration you can customize various aspects of the [new Content Fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md). 

After [creating](#create-a-content-fragment-cloud-configuration) and defining the configuration you also [apply the Cloud Configuration to your individual Assets folders](#apply-the-configuration-to-your-folder), so that it is applied to all the Content Fragments in that folder.

>[!NOTE]
>
>The Content Fragment Cloud Configurations do not impact:
>
>* the original Content Fragment editor
>* the Content Fragment console or the Assets console

>[!NOTE]
>
>For further information see also [Configurations and the Configuration Browser](/help/implementing/developing/introduction/configurations.md).

## Create a Content Fragment Cloud Configuration  {#create-a-content-fragment-cloud-configuration}

To create a configuration for customizing the new Content Fragment editor:

1. Navigate to **Tools**, **Cloud Services**, then open the **Content Fragment Cloud Configuration**.
1. In the left panel select the name of the configuration (workspace) you created in the Configuration Browser; for example `CFModels-Conf`.
1. Select **Create** from the top right toolbar.
1. Select **Configuration** from the dropdown menu.
1. A new configuration name **Content Fragment Cloud Configuration** is created.
   You can select the configuration to edit the properties, publish, unpublish or delete the configuration.

   >[!NOTE]
   >
   >For each [workspace (context aware) configuration](/help/implementing/developing/introduction/configurations.md) only one Content Fragment Cloud Configuration can be created.

## Disable Publishing {#disable-publishing}

Use this option to disable publishing from the editor:

>[!NOTE]
>
>When **Disable Publish** is activate the publish options will not be visible in the new Content Fragment editor. 
>
>Publish actions will still be available from the Content Fragments Console and the Assets Console.

1. Navigate to your Content Fragment Cloud Configuration.
1. Select and open the **Properties**.
1. Select the **Capabilities** tab.
1. Select, or deselect, **Disable Publish**. See the i icons for more information on each field.
1. **Save and Close**.
1. [Apply the Cloud Configuration to your folder](#apply-the-configuration-to-your-folder).

## Configure the Editor - RTE {#configure-the-editor-rte}

Use this option to configure the Rich Text Editor (RTE):

1. Navigate to your Content Fragment Cloud Configuration.
1. Select and open the **Properties**.
1. Select the **Filter** tab.
1. Select the **RTE** tab.
1. Select whether you want to configure the **Toolbar** or **Actions**. In both cases use the **i** icons for more information on each field:

   * **Toolbar**:
     1. Expand the **Toolbar** section.
     1. Activate, or deactivate, the options you want to see in the RTE of the new Content Fragment editor.

   * **Actions**:

     1. Expand the **Actions** section.
     1. **Add** a new action.
     1. Specify the details:

        * **Action**
        * **Label**
        * **Shortcut**
        * **Tag**

     You can also:

     * edit a specific, existing **Action** configuration: select, then update
     * delete a specific, existing **Action** configuration: select, use the trash can icon to remove the action definition

1. Select **Save and Close**.
1. [Apply the Cloud Configuration to your folder](#apply-the-configuration-to-your-folder).

>[!NOTE]
>
>RTE Toolbar:
>
>If one, or more, options are selected for a section of the RTE **Toolbar**, then *only* the selected options will be displayed. 
>
>If no options are selected for a section of the RTE **Toolbar**, then *all* the available options for that section will be displayed in the RTE toolbar.

>[!CAUTION]
>
>RTE Toolbar:
>
>If at least one option has already been enabled (and saved), and then another option is enabled, the new selection is not automatically visible in the selection list unless the user intentionally selects it.

>[!NOTE]
>
>Your development team can add features to the RTE configuration. 
>
>This works on the same basis as for the Universal Editor. Though there are two features that are not supported for a Content Fragment Cloud Configuration:
>
>* [hideInline](/help/implementing/universal-editor/configure-rte.md#action)
>
>* [Unsupported HTML](/help/implementing/universal-editor/configure-rte.md#unsupported-html)
>
>See [Configuring the RTE for the Universal Editor](/help/implementing/universal-editor/configure-rte.md) for more details. 

## Configure the Editor - Content Reference Asset Selector{#configure-the-editor-content-reference-asset-selector}

Use this option to configure the Asset Selector for Content **Reference** fields:

1. Navigate to your Content Fragment Cloud Configuration.
1. Select and open the **Properties**.
1. Select the **Filter** tab.
1. Select the **Assets** tab.
1. Configure as required. Use the **i** icons for more information on each field:

   * **Disable upload**
   * **Root Path**

     >[!NOTE]
     >
     >If a Content Fragment Model has already predefined a root path for any fragments in the folder, then this configuration will override that setting.

   * **Disable remote**
   * **Repository Names**
   * **Selection Tier**: **Author** and **Deliver**

1. Select **Save and Close**.
1. [Apply the Cloud Configuration to your folder](#apply-the-configuration-to-your-folder).

## Apply the Configuration to your Folder {#apply-the-configuration-to-your-folder}

<!--
When the configuration **global** is enabled for Content Fragment functionality, it then applies to any Assets folder - accessible through the **Assets** console.
-->

To apply your Cloud Configurations to an Assets folder, you have to define the connection. 

You can do this either when creating a new folder, or when editing the properties of an existing folder. 

Select the appropriate **Configuration** in the **Cloud Services** tab of the **Folder Properties** of the appropriate folder.

>[!NOTE]
>
>A configuration on the folder will be applied to all Content Fragments in that folder. 
>
>If no configuration is applied to a folder, then any configuration will only be inherited from the direct parent folder.

<!-- new screenshot needed -->

<!--
![Apply cloud configuration](/help/sites-cloud/administering/content-fragments/assets/cf-folder-apply-cloud-configuration.png)
-->

