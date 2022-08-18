---
title: Your Inbox
description: Managing your tasks with the inbox
exl-id: 37d0cf43-192f-4a50-b174-42d7dced3b63
---
# Your Inbox {#your-inbox}

You can receive notifications from various areas of AEM, including workflows and projects. For example, you might receive notifications about:

* Tasks:
  * These can also be created at various points within the AEM UI, for example, under **Projects**.
  * These can be the product of a workflow **Create Task** or **Create Project Task** step.
* Workflows:
  * Work items that represent actions that you need to perform on page content
    * These are the product of workflow **Participant** steps.
  * Failure items, to allow administrators to retry the failed step

You receive these notifications in your own Inbox where you can view them and take action.

>[!NOTE]
>
>For further information about the item types see also:
>
>* [Projects](/help/sites-cloud/authoring/projects/overview.md)
>* [Projects - working with Tasks](/help/sites-cloud/authoring/projects/tasks.md)
>* [Workflows](/help/sites-cloud/authoring/workflows/overview.md)

## Inbox in the Header {#inbox-in-the-header}

From any of the consoles the current number of items in your inbox is shown in the header. The indicator can also be opened to provide either quick access to the page(s) requiring action(s) or access to the inbox:

![Inbox overview in header](/help/sites-cloud/authoring/assets/inbox-header.png)

>[!NOTE]
>
>Certain actions will also be shown in the [card view of the appropriate resource](/help/sites-cloud/authoring/getting-started/basic-handling.md#card-view).

## Opening the Inbox {#opening-the-inbox}

To open the AEM notification inbox:

1. Click/tap on the indicator in the toolbar.

1. Select **View all**. The **AEM Inbox** will open. The inbox shows items from workflows, projects and tasks.
1. The default view is [List View](#inbox-list-view), but you can also switch to [Calendar View](#inbox-calendar-view). This is done with the view selector (toolbar, top right).

   For both views you can also define [View Settings](#inbox-view-settings). The options available are dependent on the current view.

   ![Inbox view settings](/help/sites-cloud/authoring/assets/inbox-view-settings.png)

>[!NOTE]
>
>The Inbox operates as a console, so use [Global Navigation](/help/sites-cloud/authoring/getting-started/basic-handling.md#global-navigation) or [Search](/help/sites-cloud/authoring/getting-started/search.md) to navigate to another location when you are finished.

### Inbox - List View {#inbox-list-view}

This view lists all items, together with relevant information:

![Inbox list view](/help/sites-cloud/authoring/assets/inbox-list-view.png)

### Inbox - Calendar View {#inbox-calendar-view}

This view presents items according to their position in the calendar:

![Inbox calendar view](/help/sites-cloud/authoring/assets/inbox-calendar-view.png)

You can:

* Select a specific view: **Timeline**, **Column**, **List**
* Specify the tasks to display according to **Schedule**: **All**, **Planned**, **In Progress**, **Due Soon**, **Past Due**
* Drill down for more detailed information on an item
* Select a date range to focus the view:

![Inbox calendar view date range](/help/sites-cloud/authoring/assets/inbox-calendar-range.png)

### Inbox - View Settings {#inbox-view-settings}

For both views (List and Calendar) you can define settings:

* **Calendar View**

  For **Calendar View** you can configure:

  * **Group by**
  * **Schedule** or **None**
  * **Card size**

  ![Inbox calendar view settings](/help/sites-cloud/authoring/assets/inbox-calendar-settings.png)

* **List View**

  For **List View** you can configure the sort mechanism:

  * **Sort on**
  * **Sort Order**

  ![Inbox list view settings](/help/sites-cloud/authoring/assets/inbox-list-settings.png)

  You can also delegate your calendar to other uses as well as request delegation from other users and manage your delegations.

  ![Inbox list view delegation settings](/help/sites-cloud/authoring/assets/inbox-delegation.png)

## Taking Action on an Item {#taking-action-on-an-item}

>[!NOTE]
>
>Although it is possible to select more than one item, actions can only be taken on one item at a time.

1. To take an action on an item, select the thumbnail for the appropriate item. Icons for the actions that are applicable to that item will be shown in the toolbar:

   ![Select inbox item](/help/sites-cloud/authoring/assets/inbox-select-item.png)

   The actions are appropriate to the item and include:

    * **Complete** action
    * **Delegate** an item
    * **Open** an item, depending on the item type this action can:

        * Show the item properties
        * Open an appropriate dashboard or wizard for further action
        * Open related documentation

    * **Step back** to a previous step
    * View the payload for a workflow
    * Create a project from the item

   >[!NOTE]
   >
   >For further information see:
   >
   >* Workflow items - [Participating in Workflows](/help/sites-cloud/authoring/workflows/participating.md)

2. Depending on the item selected an action will be started, for example:

    * A dialog appropriate to the action will be opened
    * An action wizard will be started
    * A documentation page will be opened

   For example, **Delegate** will open a dialog:

   ![Delegate inbox task](/help/sites-cloud/authoring/assets/inbox-assign-task.png)

   Depending on whether a dialog, wizard, documentation page has been opened you can:

    * Confirm the appropriate action, e.g re-assign.
    * Cancel the action
    * Select the back arrow to return to the inbox, for example if an action wizard or documentation page has been opened, you can return to the Inbox.

## Creating a Task {#creating-a-task}

From the inbox you can create tasks:

1. Select **Create**, then **Task**.
1. Complete the necessary fields in the **Basic** and **Advanced** tabs (only the **Title** is mandatory, all others are optional):

    * **Basic**:

        * **Title**
        * **Project**
        * **Assignee**
        * **Content**, similar to Payload, this is a reference from the task to a location in the repository
        * **Description**
        * **Task Priority**
        * **Start Date**
        * **Due Date**

   ![Inbox add task](/help/sites-cloud/authoring/assets/inbox-create-task.png)

    * **Advanced**

        * **Name**:This will be used to form the URL and if blank it will be based on the **Title**.

   ![Inbox add task advanced options](/help/sites-cloud/authoring/assets/inbox-add-task-advanced.png)

1. Select **Submit**.

## Creating a Project {#creating-a-project}

For certain tasks you can create a [Project](/help/sites-cloud/authoring/projects/overview.md) based on that task:

1. Select the appropriate task, by tapping/clicking on the thumbnail.

   >[!NOTE]
   >
   >Only tasks created using the **Create** option of the **Inbox** can be used to create a project.
   >
   >Work items (from a workflow) cannot be used to create a project.

1. Select **Create Project** from the toolbar to open the wizard.
1. Select the appropriate template, then **Next**.
1. Specify the required properties:

    * **Basic**

        * **Title**
        * **Description**
        * **Start Date**
        * **Due Date**
        * **User** and role

    * **Advanced**

        * **Name**

   >[!NOTE]
   >
   >See [Creating a Project](/help/sites-cloud/authoring/projects/managing.md#creating-a-project) for full information.

1. Select **Create** to confirm the action.

## Filtering Items in the AEM Inbox {#filtering-items-in-the-aem-inbox}

You can filter the items listed:

1. Open the **AEM Inbox**.

1. Open the filter selector:

   ![Inbox search](/help/sites-cloud/authoring/assets/inbox-search.png)

1. You can filter the items listed according to a range of criteria, many of which can be refined. For example:

   ![Inbox search filter](/help/sites-cloud/authoring/assets/inbox-search-filter.png)

   >[!NOTE]
   >
   >With [View Settings](#inbox-view-settings) you can also configure the sort order when using the [List View](#inbox-list-view).
