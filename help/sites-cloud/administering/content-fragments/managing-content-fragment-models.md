---
title: Managing Content Fragment Models
description: Learn how to manage Content Fragment Models; these serve as a foundation for your Content Fragments in AEM, allowing you to create structured content for use in headless delivery, or page authoring.
feature: Content Fragments
role: User, Developer, Architect
solution: Experience Manager Sites
---
# Managing Content Fragment Models {#managing-content-fragment-models}

From the Content Fragment console you can manage your Content Fragment Models, then [open the editor](/help/sites-cloud/administering/content-fragments/content-fragment-models.md) to define the structure.

Content Fragment Models in Adobe Experience Manager (AEM) as a Cloud Service define the structure for the content of your [Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md). These fragments can then be used as a foundation for your headless content, or for page authoring. 

## The Content Fragments Console {#content-fragments-console}

The Content Fragments console is dedicated to managing, searching for, and creating [Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md), Content Fragment Models and [Assets](/help/sites-cloud/administering/content-fragments/assets-content-fragments-console.md). It has been optimized for use in a Headless context, but is also used when creating Content Fragments and Content Fragment Models for use in page authoring.

>[!NOTE]
>
>This page covers the section of the console that (only) displays Content Fragment Models. For other panels see:
>
>* [Managing Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md)
>* [Viewing and Managing Assets in the Content Fragments Console](/help/sites-cloud/administering/content-fragments/assets-content-fragments-console.md)

The Content Fragments console provides direct access to your fragment models, and related tasks. The console can be directly accessed from the top level of the Global Navigation.

![Global Navigation - Content Fragments console](assets/cf-managing-global-navigation.png)

For detailed further information see:

* [Basic Structure and Handling of Content Fragment Models in the Content Fragments Console](#basic-structure-handling-content-fragment-models-console)

* [The Information provided about your Content Fragment Models](#information-content-fragment-models)

* [Actions for a Content Fragment Model in the Content Fragments Console](#actions-selected-content-fragment-models)

* [Select columns shown in the console](#select-columns-console)

* [Search and Filter Content Fragment Models in the Content Fragments Console](#filtering-fragment-models)

* A selection of [keyboard shortcuts](/help/sites-cloud/administering/content-fragments/keyboard-shortcuts.md) are available for use in this console

>[!CAUTION]
>
>This console is *only* available in the online Adobe Experience Manager (AEM) as a Cloud Service.

## Basic Structure and Handling of Content Fragment Models in the Content Fragments Console {#basic-structure-handling-content-fragment-models-console}

![Content Fragments console - Managing Content Fragment Models](assets/cf-managing-content-fragment-models.png)

Here you can see that there are three main areas:

* The top toolbar
  * Provides standard AEM functionality
  * Also shows your IMS organization
  * Provides various [actions](#actions-unselected)
* The left panel
  * Here you can hide, or reveal, the folder tree
  * You can select a specific configuration of the tree
  * This can be resized to show sub-configurations
  * As well as Content Fragment Models, you can view [Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md) or [Assets](/help/sites-cloud/administering/content-fragments/assets-content-fragments-console.md); you can also compress, or expand, links to the panels
* The main/right panel - from here you can:
  * See the list of all Content Fragment Models held under the selected configuration:
    * Content Fragment Models from the selected configuration, and all sub-configurations will be shown:
      * The location is indicated by the breadcrumbs; these can also be used to change the location:
    * [Information is shown about each model](#information-content-fragment-models)
      * [You can select which columns to show](#select-columns-console)
    * [Various fields of information](#information-content-fragment-models) about a Content Fragment provide links; depending on the field, these can:
      * Open the appropriate model in the editor
      * Show information about the configuration
      * Show information about the status of the model
    * [Certain other fields of information](#information-content-fragments) about a Content Fragment Model can be used for [Fast Filtering](#fast-filtering):
      * Select a value in the column and it is immediately applied as a filter
      * Fast filtering is supported for the **Modified By**, **Published By** and **Status** column.s
    * By using mouse-over on the column headers a drop-down action selector, and width sliders, will be shown. These allow you to:
      * Sort - select the appropriate action for either ascending or descending
        This will sort the entire table according to that column. Sorting is only available on appropriate columns.
      * Resize the column - using either the action, or width sliders
    * Select one, or more, models for further [action](#actions-selected-content-fragment-models)
  * Open the [Filter panel](#filter-fragment-models)

## The Information provided about your Content Fragment Models {#information-content-fragment-models}

The main/right panel (table view) of the console provides a range of information about your Content Fragments. Some items also provide direct links to further actions and/or information:

* **Name**
  * Provides a link to open the fragment in the editor.
* Locked
  * When the model is locked, this is indicated with a padlock icon.
* **Configuration**
  * Provides a link to open the configuration in the console.
    Hovering over the folder name will show the JCR path.
* **Status**
  * Information only.
  * Can be used for [Fast Filtering](#fast-filtering)
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

When you select a specific model, additional information is shown, and some items can be updated is the model is not **Locked**:

![Content Fragments console - Information for a selected Content Fragment Model](assets/cf-managing-content-fragment-models-selected.png)

* **Configuration**
* **Status**
* **Title**
* **Tags**
* **Description**
* **Preview URL pattern**

## Actions for a Content Fragment Model in the Content Fragments Console {#actions-selected-content-fragment-models}

## Select columns shown in the console {#select-columns-console}

As with other consoles you can configure the columns that are visible, and available for action:

![Content Fragments console - column configuration](assets/cf-managing-console-column-icon.png)

This will present a list of columns that you can hide or show:

![Content Fragments console - column configuration](assets/cf-managing-content-fragment-models-column-selection.png)

## Filter Content Fragment Models {#filter-fragment-models}

![Content Fragments console - Filtering Content Fragment Models](assets/cf-managing-content-fragment-models-filter.png)

### Fast Filtering {#fast-filtering}