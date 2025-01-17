---
title: Managing Content Fragments
description: Learn how to manage your AEM Content Fragments from the console and editor, to create content as the basis of your headless content, or for page authoring.
feature: Content Fragments
role: User, Developer, Architect
exl-id: bcaa9f06-b15d-4790-bc4c-65db6a2d5e56
solution: Experience Manager Sites
---
# Managing Content Fragments {#managing-content-fragments}

>[!IMPORTANT]
>
>Various features of the Content Fragments and Content Fragment Models are available through the Early Adopter Program.
>
>To see the status, and how to apply if you are interested, check the [Release Notes](/help/release-notes/release-notes-cloud/release-notes-current.md).

Learn how to manage your **Content Fragments** in Adobe Experience Manager (AEM) as a Cloud Service, from the dedicated [Content Fragments console](#content-fragments-console), and [Content Fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md#content-fragment-editor). These Content Fragments can be used as the basis of your headless content, or for page authoring.

>[!NOTE]
>
>Your project team can customize the console and editor if necessary. See [Customizing the Content Fragment Console and Editor](/help/implementing/developing/extending/content-fragments-console-and-editor.md) for further details.

After defining your [Content Fragment Models](#creating-a-content-model) you can use these to:

* [Create your Content Fragments](#creating-a-content-fragment). 
* Then open the [Content Fragment Editor](#opening-the-fragment-editor) to [author your content and manage your Variations](#editing-the-content-of-your-fragment).
* [Manage Tags](#manage-tags)
* [View, and edit, the Properties (Metadata)](#viewing-and-editing-properties)
* [View the Structure Tree](/help/sites-cloud/administering/content-fragments/authoring.md#structure-tree)

>[!NOTE]
>
>Content fragments can be used:
>
>* for [Headless Content Delivery using Content Fragments with GraphQL](/help/sites-cloud/administering/content-fragments/content-delivery-with-graphql.md),
>* when authoring pages; see [Page Authoring with Content Fragments](/help/sites-cloud/authoring/fragments/content-fragments.md).

>[!NOTE]
>
>Content Fragments are stored as **Assets**. They are primarily managed from the **Content Fragments** console, but can also be managed from the [Assets](/help/assets/content-fragments/content-fragments-managing.md) console.

## The Content Fragments Console {#content-fragments-console}

The Content Fragments console is dedicated to managing, searching for, and creating Content Fragments. It has been optimized for use in a Headless context, but is also used when creating Content Fragments for use in page authoring.

The Content Fragments console provides direct access to your fragments, and related tasks. The console can be directly accessed from the top level of the Global Navigation.

![Global Navigation - Content Fragments console](assets/cf-managing-global-navigation.png)

For detailed further information see:

* [Basic Structure and Handling of the Content Fragments Console](#basic-structure-handling-content-fragments-console)

* [The Information provided about your Content Fragments](#information-content-fragments)

* [Actions for a Content Fragment in the Content Fragments Console](#actions-selected-content-fragment)

* [Select columns shown in the console](#select-columns-console)

* [Search and Filter in the Content Fragments Console](#filtering-fragments)

* A selection of [keyboard shortcuts](/help/sites-cloud/administering/content-fragments/keyboard-shortcuts.md) are available for use in this console

>[!NOTE]
>
>This console only displays Content Fragments. It does not display other asset types such as images and videos. 

>[!CAUTION]
>
>This console is *only* available in the online Adobe Experience Manager (AEM) as a Cloud Service.

### Basic Structure and Handling of the Console {#basic-structure-handling-content-fragments-console}

Selecting **Content Fragments** opens the console in a new tab. 

<!-- CQDOC-21349: screenshot -->

![Content Fragments console - Overview](assets/cf-managing-console-overview.png)

Here you can see that there are three main areas:

* The top toolbar
  * Provides standard AEM functionality
  * Also shows your IMS organization
  * Provides various [actions](#actions-unselected)
* The left panel
  * Here you can hide, or reveal, the folder tree
  * You can select a specific branch of the tree
  * This can be resized to show nested folders
  * You can select between viewing Content Fragments or [Assets](/help/sites-cloud/administering/content-fragments/assets-content-fragments-console.md)
* The main/right panel - from here you can:
  * See the list of all Content Fragments in the selected branch of the tree:
    * Content Fragments from the selected folder, and all child folders will be shown:
      * The location is indicated by the breadcrumbs; these can also be used to change the location:
    * [Information is shown about each fragments](#information-content-fragments)
      * [You can select which columns to show](#select-columns-console)
    * [Various fields of information](#information-content-fragments) about a Content Fragment provide links; depending on the field, these can:
      * Open the appropriate fragment in the editor
      * Show information about references
      * Show information about language versions of the fragment
    * [Certain other fields of information](#information-content-fragments) about a Content Fragment can be used for [Fast Filtering](#fast-filtering):
      * Select a value in the column and is immediately applied as a filter
      * Fast filtering is supported for the **Model**, **Status**, **Modified By**, **Tags** and **Published By** columns.
    * By using mouse-over on the column headers a drop-down action selector, and width sliders, will be shown. These allow you to:
      * Sort - select the appropriate action for either ascending or descending
        This will sort the entire table according to that column. Sorting is only available on appropriate columns.
      * Resize the column - using either the action, or width sliders
    * Select one, or more, fragments for further [action](#actions-selected-content-fragment)
  * Use the [Search](#searching-fragments) box
  * Open the [Filter panel](#filtering-fragments)

### Actions {#actions}

Within the console there is a range of actions that you can use, either directly, or after selecting a specific fragment:

* Various actions are directly [available from the console](#actions-unselected)
* You can [select one, or more, Content Fragments to show appropriate actions](#actions-selected-content-fragment)

#### Actions (unselected) {#actions-unselected}

Certain actions are available from the console - without selecting a specific Content Fragment:

* **[Create](#creating-a-content-fragment)** a new Content Fragment
* [Filter](#filtering-fragments) the Content Fragments according to a selection of predicates, and save the filter for future use
* [Search](#searching-fragments) the Content Fragments 
* [Customize the table view to show selected columns of information](#select-columns-console)
* Use **Open in Assets** to directly open the current location in the **Assets** console

  >[!NOTE]
  >
  >The **Assets** console is used to access assets, such as images, videos, and so on.  This console can be accessed:
  >
  >* using the **Open in Assets** link (in the Content Fragments console)
  >* directly from the global **Navigation** pane

#### Actions for a (selected) Content Fragment {#actions-selected-content-fragment}

Selecting a specific fragment opens a toolbar focused on the actions available for that fragment. You can also select multiple fragments - the selection of actions will be adjusted accordingly.

<!-- CQDOC-21349: screenshot -->

![Content Fragments console - toolbar for a selected fragment](assets/cf-managing-console-fragment-toolbar.png)

* **[Open in new Editor](#editing-the-content-of-your-fragment)**
* **[Open](/help/assets/content-fragments/content-fragments-variations.md)** (in original editor)
* **[Publish](#publishing-and-previewing-a-fragment)** (and **[Unpublish](#unpublishing-a-fragment)**)
* **[Manage Tags](#manage-tags)**
* **[Copy](/help/assets/manage-digital-assets.md)**
* **[Move](/help/assets/manage-digital-assets.md)**
* **[Rename](/help/assets/manage-digital-assets.md)**
* **[Delete](#deleting-a-fragment)**
* **[Replace](#find-and-replace)**

>[!NOTE]
>
>Use **Open** to open the selected fragment in the *original* editor.

>[!NOTE]
>
>Actions such as Publish, Unpublish, Delete, Move, Rename, and Copy each trigger an asynchronous job. The progress of that job can be monitored via the AEM Async Jobs UI.

### The Information provided about your Content Fragments {#information-content-fragments}

The main/right panel (table view) of the console provides a range of information about your Content Fragments. Some items also provide direct links to further actions and/or information:

* **Name**
  * Provides a link to open the fragment in the editor.
* **Model**
  * Information only.
  * Can be used for [Fast Filtering](#fast-filtering)
* **Folder**
  * Provides a link to open the folder in the console.
    Hovering over the folder name will show the JCR path.
* **Status**
  * Information only.
  * Can be used for [Fast Filtering](#fast-filtering)
* **Preview**
  * Information only:
    * **In sync**: Content Fragment is in-sync on the **Author** and **Preview** services.
    * **Out of sync**: Content Fragment is out-of-sync on the **Author** and **Preview** services. You need to **Publish** to **Preview** to ensure that the two instances return to being in-sync.
    * blank: The Content Fragment does not exist on the **Preview** service.
* **Modified**
  * Information only.
* **Modified By**
  * Information only.
  * Can be used for [Fast Filtering](#fast-filtering).
* **Tags**
  * Information only.
  * Shows all tags related to the Content Fragment; both Main and any variations.
  * Can be used for [Fast Filtering](#fast-filtering).
* **Published At**
  * Information only.
* **Published By**
  * Information only.
  * Can be used for [Fast Filtering](#fast-filtering).
* **Referenced By**: 
  * Provides a link that opens a dialog listing all [parent references](#parent-references-fragment)  of that fragment; including referencing Content Fragments, Experience Fragments and pages. To open a specific reference, click the **Title** in the dialog.

    ![Content Fragments console - References dialog](assets/cf-managing-console-references-dialog.png)

* **Language**: indicate any [Language](#language-copies-fragment) copies

  * Indicates the locale of the content fragment, together with the total number of local/[Language](#language-copies-fragment)  copies associated with the content fragment.

    ![Content Fragments console - Language indicator](assets/cf-managing-console-language-indicator.png)

  * Select the count to open a dialog that displays all the language copies. To open a specific language copy, click the **Title** in the dialog.

    ![Content Fragments console - Language dialog](assets/cf-managing-console-languages-dialog.png)


## Creating Content Fragments {#creating-content-fragments}

Before creating your Content Fragment, the underlying Content Fragment Model must be created.

### Creating a Content Model {#creating-a-content-model}

[Content Fragment Models](/help/sites-cloud/administering/content-fragments/content-fragment-models.md) must be enabled and created, prior to creating content fragments with structured content.

### Creating a Content Fragment {#creating-a-content-fragment}

To create a content fragment:

1. From the **Content Fragments** console, select **Create** (top-right).

   >[!NOTE]
   >
   >To have the location of the new fragment predefined you can navigate to the folder where you want to create the fragment, or you can specify the location during the creation process.

1. The **New Content Fragment** dialog opens, from here you can specify the:

   * **Location** - Auto-completed with the current location, but you can select a different location if necessary.
   * **Content Fragment Model** - Select the model to be used as a basis of the fragment from the drop-down list.
   * **Auto Tag** - Select this option so that any tags assigned to the Content Fragment Model are also assigned to this Content Fragment.
   * **Title**
   * **Name** - Auto-completed based on the **Title**, but you can edit it, if necessary.
   * **Description** 

   ![New Content Fragment dialog](assets/cf-managing-new-cf-dialog.png)

1. Select **Create**, or **Create and open** to persist your definition.

## Statuses of Content Fragments {#statuses-content-fragments}

During its existence a Content Fragment can have several statuses, as shown in the [Content Fragment Console](/help/sites-cloud/administering/content-fragments/managing.md#content-fragments-console) and [Content Fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md):

* **New** (grey)
  A new Content Fragment has been created, but has no content as it has never edited, nor opened, in the Content Fragment editor.
* **Draft** (blue)
  Someone has either edited or opened the (new) Content Fragment in the Content Fragment Editor - but it has not yet been published.
* **Published** (green)
  The Content Fragment has been published.
* **Modified** (orange)
  The Content Fragment has been edited after it was published (but before publishing the modification). 
* **Unpublished** (red)
  The Content Fragment has been unpublished.

## Editing the Content of your Fragment (and Variations) {#editing-the-content-of-your-fragment}

>[!IMPORTANT]
>
>For full details, [see Authoring Content Fragments](/help/sites-cloud/administering/content-fragments/authoring.md)

To open your fragment for editing:

1. Use the **Content Fragments** console to navigate to the location of your content fragment.
1. Open the fragment for editing, by selecting the fragment, then **Open in new Editor** from the toolbar.

1. The fragment editor opens. Select your required **Variation** amd make your changes as required (they will be auto-saved):

   ![Fragment editor](assets/cf-managing-editor.png)

## View and Manage Tags {#manage-tags}

From the Content Fragments console you can view any applied tags in the **Tags** column; after ensuring that [the column is showing](#select-columns-console). 

### Manage Tags (Console) {#manage-tags-console}

To manage the tags:

1. Navigate to the Content Fragment console.
1. Select a Content Fragment.
1. Select **Manage Tags** in the toolbar.
1. Use the Tag selector to select tags to apply, or remove:

   ![Manage Tags](assets/cf-managing-manage-tags.png)

1. **Save** updates. This will return you to the console.

### Viewing, and Editing, Tags (Editor) {#viewing-and-editing-tags}

You can also view, and edit, the tags applied to a fragment using the [Properties](/help/sites-cloud/administering/content-fragments/authoring.md) tab of the editor. The information shown differs between **Main** and any **Variations**.

## Viewing, and Editing, Properties (Editor) {#viewing-and-editing-properties}

You can view, and edit, the properties (metadata) of a fragment using the [Properties](/help/sites-cloud/administering/content-fragments/authoring.md) tab of the editor. The information shown differs between **Main** and any **Variations**.

## Publishing and Previewing a Fragment {#publishing-and-previewing-a-fragment}

You can publish your Content Fragments to:

* the **[Publish Service](/help/headless/deployment/architecture.md)** - for full, public access

* the **[Preview Service](/help/headless/deployment/architecture.md)** - to preview the content prior to full availability

  >[!CAUTION]
  >
  >Publishing Content Fragments to the **Preview Service** is only available from the Content Fragments console; using the **Publish** action.

  >[!NOTE]
  >
  >For more details about the Preview environments, see [Manage Environments](/help/implementing/cloud-manager/manage-environments.md#access-preview-service).

>[!CAUTION]
>
>If your fragment is based on a model, then you should ensure that the [model has been published](/help/sites-cloud/administering/content-fragments/content-fragment-models.md#publishing-a-content-fragment-model).
>
>If you publish a content fragment for which the model has not yet been published, a selection list will indicate this and the model will be published with the fragment.

### Publishing {#publishing}

You can publish your Content Fragments using the **Publish** option from either:

* the toolbar of the [Content Fragments console](#actions-selected-content-fragment)

  * Select one, or more, fragments from the list.

* the toolbar of the [Content Fragments editor](/help/sites-cloud/administering/content-fragments/authoring.md#content-fragment-editor)

After selecting the **Publish** action:

1. Select either of the following options to open the appropriate dialog:

   * **Now** - select either the **Publish service**, or the **Preview service**; after confirmation, the fragment will be published immediately
   * **Schedule** - in addition to the required service, you can also select the date and time when the fragment will be published

1. Provide all details in the dialog. For example, for a scheduled publish request:

   ![Publish dialog](assets/cf-managing-publish-dialog.png)

   >[!NOTE]
   >
   >When necessary you will be required to specify the references to publish. By default, references also get published to the Preview service to ensure that there is no break in the content. 
  
1. Confirm the publish action.

After publication the fragment status will be updated and visible in the editor and console. If you have specified a scheduled publication, information will be shown.

>[!NOTE]
>
>In addition, when you [publish a page that uses the fragment](/help/sites-cloud/authoring/fragments/content-fragments.md#publishing); the fragment will be listed in the page references.

## Unpublishing a Fragment {#unpublishing-a-fragment}

You can unpublish Content Fragments:

* the toolbar of the [Content Fragments console](#actions-selected-content-fragment)

  * Select one, or more, fragments from the list.

* the toolbar of the [Content Fragments editor](/help/sites-cloud/administering/content-fragments/authoring.md#content-fragment-editor)

In both cases, select **Unpublish** from the toolbar, followed by either **Now** or **Scheduled**.

When the relevant dialog opens you can select the appropriate service:

![Unpublish dialog](assets/cf-managing-unpublish-dialog.png)

>[!NOTE]
>
>The **Unpublish** action will be only visible when published fragments are available.

>[!CAUTION]
>
>If the fragment is already referenced from another fragment, or from a page, you will then see a warning message and be required to confirm that you want to proceed.

## Find and Replace {#find-and-replace}

<!-- CQDOC-21349: screenshot -->

The **Replace** action is available (in the top toolbar) to find, and replace, specified text in your selected Content Fragments. 

![Find and Replace](assets/cf-managing-find-replace.png)

Before replacement, validation criteria are checked and you are informed of any conflicts, allowing you to change the replacement string or only replace the validated instances.

>[!NOTE]
>
>The find and replace action can only be performed on a maximum of 20 selected Content Fragments (at a time). 
>
>If you select more than 20 Content Fragments, you will see the message **Unable to find and replace**.

<!-- CQDOC-21349: screenshot -->

![Confirm Replace](assets/cf-managing-confirm-replace.png)

## Deleting a Fragment {#deleting-a-fragment}

To delete a fragment:

1. In the **Content Fragments** console navigate to the location of the content fragment.
1. Select the fragment.
1. Select **Delete** from the toolbar.
1. Confirm the **Delete** action.

>[!NOTE]
>
>The **Delete** is not available for fragments that are currently published, they must be unpublished first.

## Finding Parent References of your Fragment {#parent-references-fragment}

Details of parent references can be accessed from the

* **References** column of the Content Fragments Console
* the [parent references link in the top toolbar of the Content Fragments editor](/help/sites-cloud/administering/content-fragments/authoring.md#view-parent-references)

Both provide a link that opens a dialog listing all parent references of that fragment; including referencing Content Fragments, Experience Fragments and pages. To open a specific reference, click the **Title**, or the link icon, in the dialog.

For example:

![Content Fragments console - References dialog](assets/cf-managing-console-references-dialog.png)

## Finding Language Copies of your Fragment {#language-copies-fragment}

Details of Language Copies can be accessed from:

* the **Language** column of the [Content Fragments Console](#information-content-fragments)
* the [Language Copies tab of the Content Fragments editor](/help/sites-cloud/administering/content-fragments/authoring.md#view-language-copies)

The icon indicates the locale of the content fragment, together with the total number of locales/language copies associated with the content fragment. For example, from the console:

![Content Fragments console - Language indicator](assets/cfc-console-language-indicator.png)

Select the count to open a dialog that displays all the language copies. To open a specific language copy, click the **Title** in the dialog.

![Content Fragments console - Language dialog](assets/cf-managing-console-languages-dialog.png)

## Select columns shown in the console {#select-columns-console}

As with other consoles you can configure the columns that are visible, and available for action:

![Content Fragments console - column configuration](assets/cf-managing-console-column-icon.png)

This will present a list of columns that you can hide or show:

![Content Fragments console - column configuration](assets/cf-managing-console-column-selection.png)

## Filtering Fragments {#filtering-fragments}

The Filter panel offers:

* a selection of predicates; 
  * including content fragment models, localization, tags, status fields, among others
  * one, or more, predicates can be selected and combined to create the filter
* **Exclude sub-folder items**, giving you the option of excluding content fragments stored in sub-folders
* the opportunity to **Save** your configuration
* the option to retrieve a saved search filter for reuse

 Once selected, the **Filtering by** options are shown (under the Search box). They can be deselected from there. For example:

<!-- CQDOC-21349: screenshot -->

![Content Fragments console - Filtering](assets/cf-managing-console-filter.png)

### Fast Filtering {#fast-filtering}

You can also select a predicate by clicking on a specific column value in the list. You can select one, or more, values to combine predicates. 

For example, select **Published** in the **Status** column:

>[!NOTE]
>
>Fast filtering is only supported for the **Model**, **Status**, **Modified By**, **Tags**, and **Published By** columns.

![Content Fragments console - Filtering](assets/cf-managing-console-fast-filter-overview.png)

Once selected, this will be shown as a filter predicate, and the list will be filtered accordingly:

![Content Fragments console - Filtering](assets/cf-managing-console-fast-filter-criteria.png)

## Searching Fragments {#searching-fragments}

The search box supports full-text search. Entering your search terms in the search box:

<!-- CQDOC-21349: screenshot -->

![Content Fragments console - Searching](assets/cf-managing-console-search-specification.png)

Will provide the selected results:

<!-- CQDOC-21349: screenshot -->

![Content Fragments console - Search Results](assets/cf-managing-console-search-results.png)

The search box also provides quick access to **Recent Content Fragments** and **Saved Searches**:

![Content Fragments console - Recent and Saved](assets/cf-managing-console-search-saved.png)
