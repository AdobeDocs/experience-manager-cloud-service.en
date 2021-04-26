---
title: Search
description: Find your content faster with comprehensive search
exl-id: 8a799e9a-1461-4e79-ae90-1978af6cf0ed
---
# Search {#search-feature}

The author environment of AEM provides various mechanisms for searching for content, dependent on the resource type.

## Search Basics {#search-basics}

Search is available from the top toolbar:

![Search icon](/help/sites-cloud/authoring/assets/search-icon.png)

With the search rail you can:

* Search for a specific keyword, path or tag
* Filter according to resource specific criteria, such as modified dates, page status, file size, etc.
* Define and use a [saved search](#saved-searches) - based on the above criteria

>[!NOTE]
>
>Search can also be invoked by using the hotkey `/` (forward slash) whenever the search rail is visible.

## Search and Filter {#search-and-filter}

To search and filter your resources:

1. Open **Search** (with the magnifying glass in the toolbar) and enter your search term. Suggestions will be made and can be selected:

   ![Search term](/help/sites-cloud/authoring/assets/search-term.png)

   By default the search results will be limited to your current location (i.e. console and related resource type):

   ![Search location](/help/sites-cloud/authoring/assets/search-term-location.png)

1. If required, you can remove the location filter (select **X** on the filter you want removed) to search across all consoles/resource types.
1. The results will be shown, grouped according to console and related resource type.

   You can either select a specific resource (for further action), or drill down by selecting the required resource type; for example **View All Sites**:

   ![Search results](/help/sites-cloud/authoring/assets/search-results.png)

1. If you want to drill down further, select the Rail symbol (top left) to open the side panel **Filters & Options**.

   ![Rail button](/help/sites-cloud/authoring/assets/rail-button.png)

   According to the resource type Search will show a predefined selection of search/filter criteria.

   The side panel allows you to select:

    * Saved Searches
    * Search Directory
    * Tags
    * Search Criteria, for example Modified Dates, Publish Status, LiveCopy Status

   >[!NOTE]
   >
   >The search criteria can vary:
   >
   >* Depending on the resource type you have selected; for example, the Assets and Communities criteria are understandably specialized.
   >* Your instance as the Search Forms can be customized (appropriate to the location within AEM).
   
  <!--
  >* Your instance as the [Search Forms](/help/sites-administering/search-forms.md) can be customized (appropriate to the location within AEM).
  -->

   ![Search side panel](/help/sites-cloud/authoring/assets/search-side-panel.png)

1. You can also add additional search terms.

1. Close **Search** with the **X** (top right).

>[!NOTE]
>
>Search criteria are persisted when selecting an item in the search results.
>
>When you select an item on the search results page, when returning to the search page after using the browser back button, the search criteria remain.

## Saved Searches {#saved-searches}

As well as searching by a wide range of facets you can also save a particular search configuration for retrieval and use at a later stage:

1. Define your search criteria and select **Save**.

   ![Saving a search](/help/sites-cloud/authoring/assets/search-side-panel.png)

1. Assign a name, then use **Save** to confirm:

   ![Saving a search with a name](/help/sites-cloud/authoring/assets/search-save-name.png)

1. Your saved search will be available from the selector the next time you access the search panel:

   ![Saved searches](/help/sites-cloud/authoring/assets/saved-searches.png)

1. Once saved you can:

    * Use **x** (against the name of the saved search) to start a new query (the saved search itself will not be deleted).
    * **Edit Saved Search**, change the search conditions, then **Save** again.

Saved searches can be modified by selecting the saved search and clicking **Edit Saved Search** at the bottom of the search panel.

![Modifying a saved search](/help/sites-cloud/authoring/assets/saved-searches-modify.png)
