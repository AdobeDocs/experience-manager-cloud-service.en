---
title: Search assets in Content Hub
description: Learn how to search assets in [!DNL Content Hub]
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 8578d7d0-32b9-4e5c-80ef-3827e358ac6c
---
# Search Assets in [!DNL Content Hub] {#search-assets}

When you have a large number of assets in your repository, searching for the right asset is time-consuming. [!DNL The Content Hub] search provides you with the capability to look for the approved assets so that you can perform additional actions on them, such as download, share, or create collections. You can utilize various capabilities to narrow down your search results, such as performing text-based search, using filters, performing tags or smart tags-specific search, searching for a particular file format, and so on.

## Prerequisites {#prerequisites}

[Content Hub users](deploy-content-hub.md#onboard-content-hub-users) can perform actions mentioned in this article.

## What you can search for  {#what-you-can-search}

The [!DNL Content Hub] search provides results based on: 

* **Matching text:** The [!DNL Content Hub] search allows you to search for an asset using its name or description. You can perform keyword-based search, which compares the keyword to the text available in the properties of an asset. 

* **Matching context:** [!DNL Content Hub] search results list contains proximate results of assets that you get based on the matching context. For example, if you type `cool` in the search bar, the assets related to `winter`, `snow`, `cold surroundings`, display in the search list. 

* **Asset information (title, tags, or smart tags):** [!DNL Content Hub] uses smart search algorithm to rank search results accurately and as relevant as possible. [Metadata](#asset-properties.md) is the collection of all the data available for an asset, but it may not necessarily be contained in that asset. [It helps you further categorize assets and is helpful as the amount of digital information grows](/help/assets/configure-content-hub-ui-options.md##configure-metadata-search-content-hub). 

* **Last modified date:** The assets that were modified recently appear on the top of search results list. You can also filter the date range as per your requirement. 

* **Usage:** The commonly used assets appear on the top of the search list.

* **Search history:** Click inside the search box without typing a character to get your search history. You can also remove any particular keyword from history. The search history is saved in the cache memory of a web browser, which means, if you access the [!DNL Content Hub] search in a different browser or clear cache memory of the browser, you cannot view the search history anymore.

* **Search while you type:** The [!DNL Content Hub] search enhances your search experience by providing autocomplete suggestions as you start typing.

## Basic search {#basic-search}

To perform basic search on [!DNL the Content Hub], navigate to the search bar and specify the keyword that you need to search. Navigate to filters available in the left pane and apply them to narrow down your search results. 

For example, search for all the **[!UICONTROL JPEG]** images with keyword `architect` in it, which is modified within the last year. To execute this scenario, execute the following steps: 

1. Specify `architect` as the search keyword.

1. Navigate to filters panel > **[!UICONTROL Format]** > select **[!UICONTROL JPEG]**. 

1. Navigate to **[!UICONTROL Modified]** > specify the date range. 

   ![Basic search](assets/basic-search.png)

## Narrow your search results using filters {#narrow-down-search-results}

Use the Filters panel to search for assets based on metadata. You can filter search results based on various search predicates. You can select all the appropriate predicates to minimize or narrow down your search results. You can choose more than 10 predicates while filtering your search results. When you select multiple options within a filter, Content Hub displays the assets that match any of the options selected within a filter. However, when you select multiple options across filters, Content Hub only displays the assets that match all options selected across filters to narrow down your search results. 

The default filters include file format, approved by, date approved, expired and not expired assets, and expiration date. Administrators can also configure the filters that display in the list of filters. For more information, see [Configure Content Hub user interface](configure-content-hub-ui-options.md#configure-filters-content-hub).

## AI Search in Content Hub {#ai-search-aem-assets-content-hub}

AI Search in AEM Assets Content Hub is an advanced search capability that understands the meaning and intent behind a user's query rather than relying on exact keyword matches. It uses artificial intelligence (AI) and machine learning to deliver more accurate and contextually relevant results.

Unlike traditional keyword-based search, which looks for exact terms, AI Search interprets relationships between words, concepts, and user intent. This ensures that users find what they are looking for—even if their query is phrased differently, contains typos, or is in another language.

Some if its key benefits include:

* **Multilingual support**: Search across multiple languages without requiring exact translations. Users can find relevant content regardless of their query language.

* **Handles misspellings**: Interprets typos and spelling errors, ensuring accurate results even with imperfect input.

* **Understands synonyms**: Delivers results for related terms and phrases, so users do not need to guess the right keyword.

* **Contextually relevant search**: Recognizes the intent behind a query, not just the exact words.

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

AI Search is available for Content Hub environments that use the latest search stack. Adobe is rolling out the latest search stack to Content Hub customers in phases. 

To verify if you are using the latest search stack, navigate to your user profile icon and click **Configurations** on the Content Hub User Interface. Select the **Search** tab. If you can see options to select **AI Search** or **Keyword**, AI Search is available and you are using the latest search stack.

![AI Search in Content Hub](/help/assets/assets/ai-search-content-hub.png)

If AI Search is not yet available and you want to enable it, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

### Examples for AI Search in Content Hub {#examples-ai-search-aem-assets-content-hub}

**Example Prompt**: *Woman drinking coffee*

The traditional keyword-based search looks for exact matches of asset metadata, such as `Woman`, `drinking`, `Coffee`, and returns assets that include all these terms in the metadata.

However, AI Search matches similar words such as `Girl`, `Lady` in the case of `Woman` and `Cappuccino` and `Latte` in the case of `Coffee`.

Similarly, you can specify this prompt in Spanish or misspell `Woman` as `Wman` and still get the same results.


### Enable or disable AI Search in Content Hub {#enable-disable-ai-search-content-hub}

The steps to enable or disable AI Search in Content Hub are the same that you use to verify if you are using the latest search stack for Content Hub.

Execute the following steps to enable or disable AI Search in Content Hub:

1. Navigate to your user profile icon and click **[!UICONTROL Configurations]**.

1. In the **[!UICONTROL Search]** tab, select **[!UICONTROL AI Search]** to enable AI Search for Content Hub or **[!UICONTROL Keyword]** to disable it.

   ![AI Search in Content Hub](/help/assets/assets/ai-search-content-hub.png)

1. Click **[!UICONTROL Save]**.

<!--

<table>
    <tbody>
     <tr>
      <th><strong>Search Predicate</strong></th>
      <th><strong>Description</strong></th>
      <th><strong>Properties</strong></th>
     </tr>
     <tr>
      <td> Campaigns </td>
      <td> Allows you to search using planned activity performed to take any particular action. For example, advertisement campaign run on Ferrari to know the understand the interests of people using number of clicks people perform.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Channels </td>
      <td> Helps you to understand the path from where the asset is coming from. For example, web, social media, books, catalog, etc.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Region </td>
      <td> Helps you to understand the location where the asset is created. For example, Japan, EMEA, Worldwide, etc.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Keywords </td>
      <td> Keyword helps you search using terms or the words that you enter based on the topic. For example, images, low-resolution, etc.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Timeframe </td>
      <td> Helps you search assets using timeline. For example, search by year 2024, Q3 2023, etc.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td>File format</td>
      <td>Composition of an asset. The supported assets include image, document, video, printable media, and so on.</td>
      <td>
        <ul>
            <li>[!UICONTROL JPEG]</li> 
            <li>[!UICONTROL Quicktime]</li> 
            <li>[!UICONTROL PNG]</li> 
            <li>[!UICONTROL WebP]</li> 
            <li>[!UICONTROL MP4]</li> 
            <li>[!UICONTROL Plain]</li> 
            <li>[!UICONTROL PDF]</li>
            <li>[!UICONTROL SVG + XML]</li>
        </ul>
      </td>
     </tr>
     <tr>
      <td>Tags</td>
      <td>Tags help you categorize assets that can be browsed and searched more efficiently based on hierarchical taxonomies.</td>
      <td>
        <ul>
            <li>Field label</li>
            <li>Property name</li>
            <li>Path</li>
            <li>Description</li>
        </ul>
      </td>
     </tr>
     <tr>
      <td>Subject</td>
      <td>Classification of assets based on their theme. For example, colorful, hiking, outdoors.</td>
      <td>NA</td>
     </tr>
          <tr>
      <td>Last modified</td>
      <td>Search assets based on their last modification. Specify the date range using the Start date and End date fields.</td>
      <td>
        <ul>
            <li>Range text (From)</li> 
            <li>Range text (To) </li>
        </ul>
      </td>
     </tr>    
     <tr>
      <td>Asset ID</td>
      <td>Unique number that identifies the asset.</td>
      <td>NA</td>
     </tr>
     <tr>
      <td> Colors </td>
      <td> Helps you search assets using colors that are automatically identified in an asset using Adobe's AI capabilities.</td>
      <td>NA</td>
     </tr>  
    </tbody>
   </table>

-->

## Bulk search {#bulk-search}

Bulk Search of assets allows you to look up multiple assets simultaneously by entering a list of identifiers (such as names, file formats, colors, tags, and more). Instead of searching assets one by one, [!DNL Content Hub] Bulk Search makes it faster to discover the assets you need. With this capability, you can enter multiple values for any filter property—separated by a delimiter (for example, multiple SKU IDs)—and instantly retrieve all matching assets with a single search.

To search for multiple assets at once, enter multiple values in a single query by separating them with delimiters ` [ , | \t | \r | \n | \r\n ]`. You can also add more delimiters depending upon your use case. See [Configure Bulk Search](configure-content-hub-ui-options.md#bulk-search-configuration).

To perform Bulk Search in the [!DNL Content Hub], execute the following steps:

1. Once Bulk Search is [configured](configure-content-hub-ui-options.md#bulk-search-configuration), you can see Bulk Search toggle on the [!DNL Content Hub] filter properties which you configured. You can enable or disable it as per the requirement.

1. Add a search query containing delimiters that are specified in the configuration. The search query should contain a string accompanied by multiple comma-separated values.

  ![Bulk Search UI](assets/bulk-search-ui.png)

## Configure sorting in Content Hub {#configure-sorting-aem-assets-content-hub}

Content Hub provides out-of-the-box sorting options to help users organize asset search results. Administrators can also enable custom metadata fields as sorting options so that users can sort assets based on business-specific metadata, such as Channel, Region, SKU, or Campaign.

### Default sorting options {#default-sorting-options}

By default, Content Hub includes the following sorting options on the Content Hub home page:

* Size

* Modified

* Name

* Relevance

>[!IMPORTANT]
>
>This feature is available as Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

### Add custom metadata fields as sorting options {#add-custom-metadata-fields-for-sorting}

Administrators can configure additional metadata fields to appear in the sorting menu.

To enable a metadata field for sorting:

1. Click the user profile icon and select **Configurations**.
1. Navigate to the **Filters** tab.
1. Locate the metadata field that you want to enable for sorting.
1. Click the edit icon available for that particular metadata field.
1. In the Edit Filter dialog, enable the **Sorting** option.
1. Click **Confirm** and save the configuration. The updates take effect when the **Status** field value for the metadata field is displayed as `Active`.

For example, enabling sorting for the Channel metadata field allows users to sort asset results using the Channel value.

![Basic search](assets/enable-filters-sorting.png)

### Use custom sorting options on the Content Hub home page {#use-custom-sorting-options}

After you enable sorting for a metadata field:

* The field appears in the sorting menu on the Content Hub home page.
* Custom sorting fields are displayed below a separator line in the sorting menu.
* The separator visually differentiates administrator-configured custom fields from the default out-of-the-box sorting options.

For example, if the Channel metadata field is enabled for sorting, the sorting menu displays:

* Default fields such as Size, Modified, Name, and Relevance
* A separator line
* The custom field Channel

This distinction helps users quickly identify standard sorting options versus organization-specific metadata-based sorting options.

![Basic search](assets/custom-sorting-options.png)

Custom Sorting feature is available for Content Hub environments that use the latest search stack. Adobe is rolling out the latest search stack to Content Hub customers in phases. 

To verify if you are using the latest search stack, navigate to your user profile icon and click **Configurations** on the Content Hub User Interface. Select the **Search** tab. If you can see options to select **AI Search** or **Keyword**, AI Search is available and you are using the latest search stack.

![AI Search in Content Hub](/help/assets/assets/ai-search-content-hub.png)

If AI Search is not yet available and you want to enable it, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

## Do more with search {#do-more-with-search}

[!DNL The Content Hub] is not limited to search, instead it allows you to perform additional actions, such as [download](download-assets-content-hub.md), [share](share-assets-content-hub.md), and [add assets to collection](collections-content-hub.md), right from the search or preview interface. Select the assets on the search results page to view these options.

Learn more about [configuring assets in the [!DNL Content Hub]](configure-content-hub-ui-options.md).

## Frequently asked questions {#faqs-deploy-content-hub}

### How can I narrow down my search results in AEM Assets Content Hub?

You can narrow down search results in AEM Assets Content Hub by using text-based search, applying various filters (such as file format, approval status, modification date, etc.), searching by tags or smart tags, and using the filters panel. Combining multiple predicates or filter options helps you precisely target the assets you need.

### Can I perform a bulk search in AEM Assets Content Hub for multiple assets at once?

Yes, you can perform a Bulk Search in AEM Assets Content Hub by entering multiple values (such as names, file formats, tags) separated by specified delimiters. The Bulk Search feature allows you to quickly find several assets in a single query, making it more efficient than searching assets one by one.


### Can administrators customize the filters available in AEM Assets Content Hub search?

Yes, administrators can use the AEM Assets Content Hub Configuration User Interface to configure which filters are available in search interface. While default filters include file format, approval status, expiration date, and more, administrators can tailor these options to fit organizational needs.

### Do you need the ability to filter on custom date fields or use Tags as filters?

If you need the ability to filter on custom date fields or use Tags as filters, you must get [AI Search](#ai-search-aem-assets-content-hub) enabled for your deployment. [Create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable AI Search.


**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

