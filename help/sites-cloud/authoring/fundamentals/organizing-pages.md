---
title: Creating and Organizing Pages
description: How to create and organize pages with AEM
---

# Creating and Organizing Pages {#creating-and-organizing-pages}

This document describes how to create and manage pages with Adobe Experience Manager Cloud Service so that you can then [create content](/help/sites-cloud/authoring/fundamentals/editing-content.md) on those pages.

>[!NOTE]
>
>Your account needs the appropriate access rights and permissions to take action on pages such as create, copy, move, edit, and delete.
>
>If you encounter any problems we suggest you contact your system administrator.

<!--
>Your account needs the [appropriate access rights](/help/sites-administering/security.md) and [permissions](/help/sites-administering/security.md#permissions) to take action on pages such as create, copy, move, edit, and delete.
-->

>[!TIP]
>
>There are a number of [keyboard shortcuts](/help/sites-cloud/authoring/getting-started/keyboard-shortcuts.md) that you can use from the websites console that make organizing your pages more efficient.

## Organizing your Website {#organizing-your-website}

As an author you will need to organize your website within AEM. This involves creating and naming your content pages so that:

* You can easily find them on the author environment
* Visitors to your site can easily browse them on the publish environment

You can also use [folders](#creating-a-new-folder) to help organize your content.

The structure of a website can be thought of as a tree that holds your content pages. The names of these content pages are used to form the URLs, whereas the titles are shown when the page content is viewed.

The following shows an example from the [WKND Tutorial](https://docs.adobe.com/content/help/en/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html) site, where an article about skateparks ( `la-skateparks`) is accessed:

`http://<host>:<port>/editor.html/content/wknd/en/sports/la-skateparks.html`

```xml
 /content
 /wknd
  /en
   /music
    /...
   /sports
    /la-skateparks
    /five-gyms-la
    /mountain-bike-routes
   /shopping
    /...
   /art
    /...
   /...
```

This structure can be viewed From the **Sites** console, where you can [navigate through the pages of your website](/help/sites-cloud/authoring/getting-started/basic-handling.md#selecting-resources) and perform actions on the pages. You can also create new sites and [new pages](#creating-a-new-page).

From any point, you can see the upward branch from breadcrumbs in the header bar:

![Using breadcrumbs to navigate](/help/sites-cloud/authoring/assets/organizing-breadcrumbs.png)

### Page Naming Conventions {#page-naming-conventions}

When creating a new page there are two keys fields:

* **[Title](#title)**:

  * This is displayed to the user in the console and shown at the top of the page content when editing.
  * This field is mandatory.

* **[Name](#name)**:

  * This is used to generate the URI.
  * User input for this field is optional. If not specified, the name is derived from the title. See the following section [Page Name Restrictions and Best Practices](#page-name-restrictions-and-best-practices) for details.

#### Page Name Restrictions and Best Practices {#page-name-restrictions-and-best-practices}

The page **Title** and **Name** can be created separately but are related:

* When creating a page, only the **Title** field is required. If no **Name** is provided at page creation, AEM will generate a name from the first 64 characters of the title (observing the validation set out below). Only the first 64 characters are used in order to support the best practice of short page names.
* If a page name is manually specified by the author, the 64 character limit does not apply, however other technical limitations on the page name length may.

>[!TIP]
>
>When defining a page name, a good rule-of-thumb is to keep the page name as brief but as expressive and memorable as possible to make it easy to understand for the reader. See the [W3C style guide](https://www.w3.org/Provider/Style/TITLE.html) for the `title` element for more information.
>
>Also keep in mind that some browsers (e.g. older versions of IE) can only accept URLs up to a certain length, so there is also technical reason to keep page names short.

When creating a new page, AEM will [validate the page name according to the conventions](/help/implementing/developing/introduction/naming-conventions.md) imposed by AEM and the JCR.

The minimum allowed characters are:

* `a` through `z`
* `A` through `Z`
* `0` through `9`
* `_` (underscore)
* `-` (hyphen/minus)

Full details of all characters allowed can be found in [the naming conventions](/help/implementing/developing/introduction/naming-conventions.md).

>[!NOTE]
>
>Page names are limited to 150 characters.

#### Title {#title}

If you supply only a page **Title** when creating a new page, AEM will derive the page **Name** from this string and [validate the name according to the conventions](/help/implementing/developing/introduction/naming-conventions.md) imposed by AEM and JCR.

A **Title** field containing invalid characters will be accepted, but the name derived will have the invalid characters substituted. For example:

| Title |Derived Name |
|---|---|
|Schön|`schoen.html`|
|SC%&&#42;ç+|`sc---c-.html` |

#### Name {#name}

When you supply a page **Name** when creating a new page, AEM will [validate the name according to the conventions](/help/implementing/developing/introduction/naming-conventions.md) imposed by AEM and JCR. You cannot submit invalid characters in the **Name** field. When AEM detects invalid characters the field will be highlighted with an explanatory message.

![Example of entering an invalid page name](/help/sites-cloud/authoring/assets/organizing-invalid-name.png)

>[!TIP]
>
>You should avoid using a two-letter code as defined by ISO-639-1 as a page name, unless it is a language root.
>
>See [Preparing Content for Translation](/help/sites-cloud/administering/translation/preparation.md) for more information.

### Templates {#templates}

In AEM, a template specifies a specialized type of page. A template will be used as the basis for any new page being created.

The template defines the structure of a page including a thumbnail image and other properties. For example, you may have separate templates for product pages, sitemaps, and contact information. Templates are comprised of [components](#components).

AEM comes with several templates provided out-of-the-box. The templates available depend on the individual website. The key fields are:

* **Title**
  The title displayed on the resulting web-page.

* **Name**
  Used when naming the page.

* **Template**
  A list of templates available for use when generating the new page.

>[!TIP]
>
>If configured on your instance, [template authors can create templates with the Template Editor](/help/sites-cloud/authoring/features/templates.md).

### Components {#components}

Components are the elements provided by AEM so that you can add specific types of content. AEM comes with a range of out-of-the-box components that provide comprehensive functionality. These include:

* Text
* Image
* Title
* Carousel
* And many more

Once you have created and opened a page you can [add content using the components](/help/sites-cloud/authoring/fundamentals/editing-content.md#inserting-a-component), which are available from the [component browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#components-browser).

>[!TIP]
>
>The [Components Console](/help/sites-cloud/authoring/features/components-console.md) give an overview of the components on your instance.

## Managing Pages {#managing-pages}

### Creating a New Page {#creating-a-new-page}

Unless all pages have been created for you in advance, you must create a page before you can start creating content:

1. Open the Sites console (for example, `https://<host>:<port>/sites.html/content`.
1. Navigate to the location where you want to create the new page.
1. Open the drop down selector using **Create** in the toolbar, then select **Page** from the list:

   ![Creating a page](/help/sites-cloud/authoring/assets/organizing-create-page.png)

1. From the first stage of the wizard you can either:

    * Select the template you want used to create the new page, then click/tap **Next** to proceed.

    * **Cancel** to abort the process.

   ![Selecting a template for a new page](/help/sites-cloud/authoring/assets/organizing-create-page-template.png)

1. From the final stage of the wizard you can either:

    * Use the three tabs to enter the [page properties](/help/sites-cloud/authoring/fundamentals/page-properties.md) you want assigned to the new page, then click/tap **Create** to actually create the page.

    * Use **Back** to return to template selection.

   Key fields are:

    * **Title**:

        * This is displayed to the user and is mandatory.

    * **Name**:

        * This is used to generate the URI. If not specified, the name is derived from the title.
        * If you supply a page **Name** when creating a new page, AEM will [validate the name according to the conventions](/help/implementing/developing/introduction/naming-conventions.md) imposed by AEM and JCR.
        * You **cannot submit invalid characters** in the **Name** field. When AEM detects invalid characters the field will be highlighted and an explanatory message shown to indicate the characters that need removing/replacing.

   >[!TIP]
   >
   >See [Page Naming Conventions](#page-naming-conventions).

   The minimum information required to create a new page is the **Title**.

   ![Providing page title](/help/sites-cloud/authoring/assets/organizing-create-page-title.png)

1. Use **Create** to complete the process and create your new page. The confirmation dialog will ask whether you want to **Open** the page immediately or return to the console (**Done**):

   ![Page creation success](/help/sites-cloud/authoring/assets/organizing-create-page-success.png)

   >[!NOTE]
   >
   >If you create a page using a name that already exists at that location, the system will automatically generate a variation of the name by appending a number. For example if `beach` already exists a new page will become `beach1`.

1. If you return to the console you will see your new page:

   ![Resulting new page](/help/sites-cloud/authoring/assets/organizing-create-page-result.png)

>[!CAUTION]
>
>Once a page has been created its template cannot be changed - unless you [create a launch with a new template](/help/sites-cloud/authoring/launches/creating.md#create-launch-with-new-template), though this will lose any existing content.

### Opening a Page For Editing {#opening-a-page-for-editing}

After creating a page, or navigating to an existing page (in the console), you can open it for editing:

1. Open the **Sites** console.
1. Navigate until you find the page that you want to edit.
1. Select your page by using either:

    * [Quick actions](/help/sites-cloud/authoring/getting-started/basic-handling.md#quick-actions)
    * [Selection mode](/help/sites-cloud/authoring/getting-started/basic-handling.md#selecting-resources) and the toolbar

   And then select the **Edit** icon:

   ![Edit button](/help/sites-cloud/authoring/assets/edit.png)

1. The page will be opened and you can [edit the page](/help/sites-cloud/authoring/fundamentals/editing-content.md) as required.

>[!NOTE]
>
>Navigating to other pages from the page editor is only possible in Preview mode since links are not active in the Edit mode..

### Copying and Pasting a Page {#copying-and-pasting-a-page}

You can copy a page and all of its sub-pages to a new location:

1. In the **Sites** console, navigate until you find the page that you want to copy.
1. Select your page using either:

    * [Quick actions](/help/sites-cloud/authoring/getting-started/basic-handling.md#quick-actions)
    * [Selection mode](/help/sites-cloud/authoring/getting-started/basic-handling.md#selecting-resources) and the toolbar

   And then the **Copy** page icon:

   ![Copy](/help/sites-cloud/authoring/assets/copy.png)

   >[!NOTE]
   >
   >If you are in selection mode this is exited automatically as soon as the page is copied.

1. Navigate to the location for the new copy of the page.
1. The **Paste** icon is available with a drop down arrow directly to the right:

   ![Paste](/help/sites-cloud/authoring/assets/paste.png)

   You can either:

     1. Select the **Paste** page icon itself: A copy of the original page and any child-pages will be created at this location.
     1. Select the drop down arrow to reveal the **Paste without children** option. A copy of the original page will be created at this location; child-pages will not be copied.

   >[!NOTE]
   >
   >If you copy the page to a location where a page with the same name as the original already exists, the system will automatically generate a variation of the name by appending a number. For example if `beach` already exists a new page with the name `beach` will become `beach1`.

### Moving or Renaming a Page {#moving-or-renaming-a-page}

The procedure to move or rename a page is basically the same and is handled by the same wizard. With this wizard you can:

* Rename a page without moving it
* Move the page without renaming it
* Move and rename at the same time

AEM offers you the functionality to update any internal links that refer to the page being renamed/moved. This can be done on a page-by-page basis to provide full flexibility.

1. Navigate until you find the page that you want to move.
1. Select your page using either:

    * [Quick actions](/help/sites-cloud/authoring/getting-started/basic-handling.md#quick-actions)
    * [Selection mode](/help/sites-cloud/authoring/getting-started/basic-handling.md#selecting-resources) and the toolbar

   And then select the **Move** page icon:

   ![Move button](/help/sites-cloud/authoring/assets/move.png)

   This will open the move page wizard.

1. From the **Rename** stage of the wizard you can either:

    * Specify the name you want the page to have after it is moved, then click/tap **Next** to proceed.
    * **Cancel** to abort the process.

   ![Move and rename page](/help/sites-cloud/authoring/assets/move-page-rename.png)

   The page name can remain the same if you are only moving the page.

   >[!NOTE]
   >
   >If you move a page to a location where a page with the same name already exists, the system will automatically generate a variation of the name by appending a number. For example if `beach` already exists a new page with the name `beach` will become `beach1`.

1. From the **Select Destination** stage of the wizard you can either:

    * Use the [column view](/help/sites-cloud/authoring/getting-started/basic-handling.md#column-view) to navigate to the new location for the page:

        * Select the destination it by clicking the destination's thumbnail.
        * Click **Next** to continue.

    * Use **Back** to return to page name specification.

   >[!NOTE]
   >
   >By default the parent of the page you are moving/renaming will be selected as the destination.

   ![Select page move destination](/help/sites-cloud/authoring/assets/move-page-destination.png)

   >[!NOTE]
   >
   >If you move a page to a location where a page with the same name already exists, the system will automatically generate a variation of the name by appending a number. For example if `winter` already exists `winter` will become `winter1`.

1. If the page is linked to or referenced, or has been published, then the details will be listed in the **Adjust/Republish** step.

   You can indicate which should be adjusted and/or republished as appropriate.

   >[!NOTE]
   >
   >If the page is neither linked to nor referenced, then this step will not be available.

   ![Republish page on move](/help/sites-cloud/authoring/assets/move-page-republish.png)

1. Selecting **Move** will complete the process and move/rename your page as appropriate.

>[!NOTE]
>
>If the page was already published, moving the page will automatically unpublish it. By default, it will be republished when the move is complete, but this can changed by un-checking the **Republish** field in the **Adjust/Republish** step.

>[!NOTE]
>
>If the page is not referenced in any way, then the **Adjust/Republish** step will be skipped.

>[!NOTE]
>
>Renaming a page is also subject to the [Page Naming Conventions](#page-naming-conventions) when specifying the new page name.

>[!NOTE]
>
>A page can only be moved to a location where the template upon which the page is based is allowed. See [Template Availability](/help/implementing/developing/components/templates.md#template-availability) for more information.

#### Asynchronous Actions {#asynchronous-actions}

Normally a page move or rename action is carried out immediately. This is considered synchronous processing and further action in the UI is blocked until the action is complete.

However, if the number of pages impacted is above a defined limit, the action will be processed asynchronously, allowing the user to continue authoring in the UI unimpeded by the page move or rename action.

* When clicking **Move** in the last step above, AEM checks the configured limit.
* If the number of pages impacted is below the limit, it performs a synchronous operation.
* If the number of pages impacted is above the limit, it performs an asynchronous operation.
  * The user must define when the asynchronous operation should be performed
    * **Now** begins the execution of the asynchronous job immediately.
    * **Later** allows the user to define when the asynchronous job will start.

      ![Asynchronous page move](/help/sites-cloud/authoring/assets/asynchronous-page-move.png)

The status of asynchronous jobs can be checked in the [**Async Jobs Status** dashboard](/help/operations/asynchronous-jobs.md#monitor-the-status-of-asynchronous-operations) at **Global Navigation** -&gt; **Tools** -&gt; **Operations** -&gt; **Jobs**

>[!NOTE]
>
>For further information about asynchronous job processing and how to configure the limit for page move/rename actions, please see the [Asynchronous Jobs](/help/operations/asynchronous-jobs.md) document in the Operations user guide.

### Deleting a Page {#deleting-a-page}

1. Navigate until you can see the page you want to delete.
1. Use [selection mode](/help/sites-cloud/authoring/getting-started/basic-handling.md#viewing-and-selecting-resources) to select the required page, then use **Delete** from the toolbar:

   ![Delete button](/help/sites-cloud/authoring/assets/delete.png)

   >[!NOTE]
   >
   >As a security precaution, **the Delete** page icon is not available as a quick action.

1. A dialog will ask for confirmation.

   ![Delete dialog](/help/sites-cloud/authoring/assets/delete-page.png)

    * **Do you want to archive pages before deletion?** - If checked, versions of the pages selected for deletion will be created upon deletion.
      * [Versions can be restored at a later date.](/help/sites-cloud/authoring/features/page-versions.md)
      * Pages deleted without previous versions can not be restored.
    * **Cancel** to abort the action
    * **Delete** to confirm the action:

      * If the page has no references, the page will be deleted.
      * If the page has references, a message box will inform you that **One or more pages are referenced.** You can select **Force Delete** or **Cancel**.

>[!NOTE]
>
>If a page is already published, it will automatically be un-published before deletion.

### Locking a Page {#locking-a-page}

You can [lock/unlock a page](/help/sites-cloud/authoring/fundamentals/editing-content.md#locking-a-page) from either a console or when editing an individual page. Information about whether a page is locked is also shown in both locations.

![Lock button](/help/sites-cloud/authoring/assets/lock.png)
![Unlock button](/help/sites-cloud/authoring/assets/unlock.png)

### Creating a New Folder {#creating-a-new-folder}

You can create folders to help organize your files and pages.

1. Open the **Sites** console and navigate to the required location.
1. To open the option list, select **Create** from the toolbar
1. Select **Folder** to open the dialog. Here you can enter the **Name** and **Title**:

   ![Create folder](/help/sites-cloud/authoring/assets/organizing-create-folder.png)

1. Select **Create** to create the folder.

>[!NOTE]
>
>Folders are also subject to the [Page Naming Conventions](#page-naming-conventions) when specifying the new folder name.

>[!CAUTION]
>
>* Folders can only be created directly under **Sites** or under other folders. They cannot be created under a page.
>* The standard actions move, copy, paste, delete, publish, unpublish, and view/edit properties can be performed on a folder.
>* Folders are not available for selection within a live copy.
