---
title: Content Fragments Console
description: Learn how to manage Content Fragments from the Content Fragments Console.
landing-page-description: Learn how to manage Content Fragments from the Content Fragments Console that is focused on high volume use of Content Fragments for Headless use-cases, but also used when page authoring.
exl-id: 0e6e3b61-a0ca-44b8-914d-336e29761579
---
# Content Fragments Console  {#content-fragments-console}

Learn how the Content Fragments console optimizes access to your Content Fragments, helping you create, search, and manage them by taking administrative actions such as publish, unpublish, copy.

The Content Fragments console is dedicated to managing, searching for, and creating Content Fragments. It has been optimized for use in a Headless context, but is also used when creating Content Fragments for use in page authoring.

>[!NOTE]
>
>This console only displays Content Fragments. It does not display other asset types such as images and videos. 

>[!NOTE]
>
>Access to your Content Fragments is currently possible via:
>
>* this **Content Fragments** console
>* the **Assets** console - see [Managing Content Fragments](/help/assets/content-fragments/content-fragments-managing.md)

>[!NOTE]
>
>A selection of [keyboard shortcuts are available for use in this console](/help/sites-cloud/administering/content-fragments/content-fragments-console-keyboard-shortcuts.md).

The Content Fragments console can be directly accessed from the top level of the Global Navigation:

![Global Navigation - Content Fragments console](assets/cfc-global-navigation.png)

Selecting **Content Fragments** will open the console in a new tab. 

![Content Fragments console - Overview](assets/cfc-console-overview.png)

Here you can see that there are three main areas:

* The top toolbar
  * Provides standard AEM functionality
  * Also shows your IMS organization
* The left panel
  * Here you can hide, or reveal, the folder tree
  * You can select a specific branch of the tree
* The main/right panel - from here you can:
  * See the list of all Content Fragments in the selected branch of the tree:
    * The location is indicated by the breadcrumbs; these can also be used to change the location
    * Content Fragments from the selected folder, and all child folders will be shown:
      * [Various fields of information](#selectuse-available-columns) about a Content Fragment provide links; depending on the field, these can:
        * Open the appropriate fragment in the editor
        * Show information about references
        * Show information about language versions of the fragment
      * You can [select one, or more, Content Fragments to show the available actions](#actions-selected-content-fragment)
    * You can select a column header to sort the table according to that column; select again to toggle between ascending and descending
  * **[Create](#creating-new-content-fragment)** a new Content Fragment
  * [Filter](#filtering-fragments) the Content Fragments according to a selection of predicates, and save the filter for future use
  * [Search](#searching-fragments) the Content Fragments 
  * [Customize the table view to show selected columns of information](#selectuse-available-columns)
  * Use **Open in Assets** to directly open the current location in the **Assets** console

    >[!NOTE]
    >
    >The **Assets** console is used to access assets, such as images, videos, etc.  This console can be accessed:
    >
    >* using the **Open in Assets** link (in the Content Fragments console)
    >* directly from the global navigation pane

## Actions for a (selected) Content Fragment {#actions-selected-content-fragment}

Selecting a specific fragment will open a toolbar focused on the actions available for that fragment. You can also select multiple fragments - the selection of actions will be adjusted accordingly.

![Content Fragments console - toolbar for a selected fragment](assets/cfc-fragment-toolbar.png)

## Select and Use the Available Columns {#select-use-available-columns}

As with other consoles you can configure the columns that are visible, and available for action:

![Content Fragments console - column configuration](assets/cfc-console-column-icon.png)

This will present a list of columns that you can hide or show:

![Content Fragments console - column configuration](assets/cfc-console-column-selection.png)

* **Name**
  * Provides a link to open the fragment in the editor.
* **Model**
  * Provides a link to open the fragment in the editor.
* **Folder**
  * Provides a link to open the folder in the console.
* **Status**
  * Information only
* **Modified**
  * Information only
* **Modified By**
  * Information only
* **Published At**
  * Information only
* **Published By**
  * Information only
* **Referenced By**
  * Provides a link that opens a dialog listing all references related to the selected fragment.
* **Language**
  * Indicates the locale of the content fragment, together with the total number of locales/language copies associated with the content fragment.

    ![Content Fragments console - Language indicator](assets/cfc-console-language-indicator.png)

    * Click/tap on the count to open a dialog that displays all the language copies. To open a specific language copy, click on the **Title** in the dialog.

      ![Content Fragments console - Language dialog](assets/cfc-console-languages-dialog.png)

## Creating a new Content Fragment {#creating-new-content-fragment}

Selecting **Create** opens the compact **New Content Fragment** dialog:

![Content Fragments console - Creating a new fragment](assets/cfc-console-create.png)

## Filtering Fragments {#filtering-fragments}

The Filter panel offers:

* a selection of predicates that can be selected and combined
* the opportunity to **Save** your configuration
* the option to retrieve a saved search filter for reuse

![Content Fragments console - Filtering](assets/cfc-console-filter.png)

## Searching Fragments {#searching-fragments}

The search box supports full-text search. Entering your search terms in the search box:

![Content Fragments console - Searching](assets/cfc-console-search-01.png)

Will provide the selected results:

![Content Fragments console - Search Results](assets/cfc-console-search-02.png)

The search box also provides quick access to **Recent Content Fragments** and **Saved Searches**:

![Content Fragments console - Recent and Saved](assets/cfc-console-search-03.png)
