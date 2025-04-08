---
title: Creating Launches
description: You can create a launch to enable the updating of a new version of existing web pages for future activation.
exl-id: 216ccb7a-1409-4f55-8be2-2b088f91a430
solution: Experience Manager Sites
feature: Authoring, Launches
role: User
---
# Creating Launches {#creating-launches}

Create a launch to enable the updating of a new version of existing web pages for future activation. When you create a Launch, you specify a title and the source page:

* The title appears in the [References](/help/sites-cloud/authoring/sites-console/console-side-panel.md#references) rail, from where authors can access them to work on them.
* The child pages of the source page are included in the launch by default. You can use only the source page if desired.
* By default, [Live Copy](/help/sites-cloud/administering/msm/overview.md) automatically updates the launch pages as the source pages change. You can specify that a static copy is created to prevent automatic changes.

Optionally, you can specify the **Launch Date** (and time) to define when the launch pages are to be promoted and activated. However the **Launch Date** only operates in combination with the **Production Ready** flag (see [Editing a Launch Configuration](/help/sites-cloud/authoring/launches/editing.md#editing-a-launch-configuration)); for the actions to actually occur automatically, both must be set.

>[!NOTE]
>
>When you create a launch, pages higher up in the hierarchy are not copies of the source pages. They are placeholders, created with the template:
>
>* `/libs/launches/templates/outofscope`
>
>These pages cannot be edited. You see the message: 
>
>* **This page is not part of the launch. Go to production page**

## Creating a Launch {#creating-a-launch}

You can create a launch from either the Sites or Launches console:

1. Open the **Sites** or **Launches** console.

   >[!NOTE]
   >
   >When using the **Sites** console it is usual to navigate to the location of the source page, but this is not compulsory as you can navigate when selecting the **Launch Source** in the wizard.

1. Depending on the console you are using:
    * **Launches**:
        1. Select **Create Launch** from the toolbar to open the wizard.
    * **Sites**:
        1. Select **Create** from the toolbar to open the selection box.
        1. From this select **Create Launch** to open the wizard.

   >[!NOTE]
   >
   >In the **Sites** console you can also use [selection mode](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources) to select a page before selecting **Create**.
   >
   >This will use the selected page as the initial source page.

1. In the **Select Source** step you need to **Add Pages**. You can select multiple pages, specifying the path for each:
    * Navigate to the required location.
    * Select the source page(s) and confirm (check mark).

   Repeat as required.

   ![Select launch source](/help/sites-cloud/authoring/assets/launches-select-source.png)

   >[!NOTE]
   >
   >To add pages and/or branches to a launch they must be within a site; that is, below a common top-level root.
   >
   >If a site contains language roots below the top level, the pages and branches for a launch must be below a common language root.

1. For each entry you can specify whether to:

    * **Include subpages**:

        * Specify whether you want to create the launch with or without the child pages.  By default, this subpages are included.

   Proceed with **Next**.

   ![Select launch source](/help/sites-cloud/authoring/assets/launches-select-source-2.png)

1. In the **Properties** step of the wizard you can specify:

    * **Launch Title**: The name of the Launch. The name should be meaningful for authors.
    * **with existing content**: the original content is used to create the launch.
    * **use a new template to replace the page**: See [Create Launch with New Template](#create-launch-with-new-template) for more details.
    * **Inherit source page live data**: Select this option to automatically update the content of launch pages when the source pages change. This option achieves this by making the launch a [Live Copy](/help/sites-cloud/administering/msm/overview.md). By default, this option is selected.-->
    * **Launch Date**: The date and time when the launch copy is to be activated (dependent on the **Production Ready** flag; see [Launches - the Order of Events](/help/sites-cloud/authoring/launches/overview.md#launches-the-order-of-events)).

   ![Launch properties](/help/sites-cloud/authoring/assets/launches-properties.png)

1. Use **Create** to complete the process and create your new launch. The confirmation dialog will ask whether you want to open the launch immediately.

   If you return the console (with **Done**) you can see (and access) your launch from either:

    * The [**Launches** console](/help/sites-cloud/authoring/launches/overview.md#the-launches-console)
    * The [**References** in the **Sites** console](/help/sites-cloud/authoring/launches/overview.md#launches-in-references-sites-console)

### Create Launch with New Template {#create-launch-with-new-template}

When creating a launch you can select whether to use a new template:

>[!NOTE]
>
>This option is only available when creating a launch from the **Sites** console. It is not available when creating a launch from the **Launches** console.

![Creating a launch with a new template](/help/sites-cloud/authoring/assets/launches-create-new-template.png)

Selecting this will:

* Update the other options available,
* Include a new step where you can select the required template.

![Selecting a new template](/help/sites-cloud/authoring/assets/launches-select-template.png)

>[!CAUTION]
>
>As a different template is used, the new page is empty. Due to the different page structure no content is copied over.
>
>This mechanism can be used to change the template of an [existing page](/help/sites-cloud/authoring/sites-console/creating-pages.md#creating-a-new-page) - though the loss of content must be considered.

### Creating a Nested Launch {#creating-a-nested-launch}

Creating a nested launch (launch within a launch) gives you the ability to create a launch from an existing launch so that authors can take advantage of changes already made, rather than having to make the same changes multiple times for each launch.

>[!NOTE]
>
>See also [Promoting a Nested Launch](/help/sites-cloud/authoring/launches/promoting.md#promoting-a-nested-launch).

#### Creating a Nested Launch - Launches Console {#creating-a-nested-launch-launches-console}

Creating a nested launch from the **Launches** console is basically the same as creating any other form of launch, with the exception that you need to navigate to the launches branch `/content/launches`:

1. In the **Launches** console select **Create**.
1. Select **Add Pages**, then navigate to the launches branch by specifying `/content/launches` in the **Filters** rail. Select the required launch and confirm with **Select**:

   ![Creating a nested launch](/help/sites-cloud/authoring/assets/launches-create-nested.png)

1. Proceed with **Next**.

1. Complete the **Properties** as with any other launch.

1. Complete with **Create**.

#### Creating a Nested Launch - Sites Console {#creating-a-nested-launch-sites-console}

To create a nested launch from the **Sites** console - based on an existing launch:

1. Access the [Launch from References (Sites console)](/help/sites-cloud/authoring/launches/overview.md#launches-in-references-sites-console) to show the available actions.
1. Select **Create launch** to open the wizard (as the source has already been selected it will skip the **Select Source** step).
1. Enter the **Launch Title** and any other required details (as with a normal launch).
1. Use **Create** to complete the process and create your new launch. The confirmation dialog will ask whether you want to open the launch immediately.

If you select **Done**, you are returned to the **References** rail of the **Sites** console, if you select the appropriate page your new launch is shown.

### Cloning a Launch {#cloning-a-launch}

You can clone a launch from the [launches console](/help/sites-cloud/authoring/launches/overview.md#the-launches-console):

* Select the launch, by tapping/clicking on the thumbnail.
* The toolbar will appear - select Clone.
  * The clone will be created and shown in the console. 
  * The **Launch Title** will indicate that it is a clone. You can update the title by editing the [Launch Configuration](/help/sites-cloud/authoring/launches/editing.md#editing-a-launch-configuration) (**Properties**).

## Deleting a Launch {#deleting-a-launch}

You can delete a launch from the [launches console](/help/sites-cloud/authoring/launches/overview.md#the-launches-console):

* Select the launch, by tapping/clicking on the thumbnail.
* The toolbar will appear - select Delete.
* Confirm the action.

>[!CAUTION]
>
>Deleting a launch will remove the launch itself and all descendant nested launches.
