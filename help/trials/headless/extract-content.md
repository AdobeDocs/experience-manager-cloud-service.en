---
title: Extract Content via the GraphQL API
description: Learn how to use Content Fragments and the GraphQL API as a headless content management system.
hidefromtoc: yes
index: no
exl-id: f5e379c8-e63e-41b3-a9fe-1e89d373dc6b
---

# Extract Content via the GraphQL API {#extract-content}

So far in AEM Trials for headless, you have [created your own Content Fragment models](content-structure.md) as well created your own headless content as [Content Fragments.](create-content.md) Now you can learn how to use Content Fragments and the GraphQL API as a headless content management system to deliver your content.

GraphQL provides a query-based API allowing external client applications to query AEM for only the content it needs using a single API call. 

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_graphql"
>title="Extract content using the GraphQL API"
>abstract="In this module you'll learn how you can use Content Fragments and the GraphQL API as a Headless Content Management System."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_graphql_guide"
>title="Launch the GraphQL Explorer"
>abstract="GraphQL provides a query-based API allowing external client applications to query AEM for only the content it needs, using a single API call. Follow this module to learn how to run two different types of queries. Then you will learn how to retrieve the content from the Content Fragment you created in a previous module.<br><br>Launch this module in a new tab by clicking below."
>additional-url="https://video.tv.adobe.com/v/328618" text="Placeholder for the intro video"

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_graphql_guide_footer"
>title="Launch the GraphQL Explorer"
>abstract="Great job! You've authored a Content Fragment and now understand how content teams can create and manage content for apps and websites independent of development cycles."


## Query for a List of Sample Content {#list-query}

Clicking the **Launch the GraphQL Explorer** button above opens the GraphQL Explorer in a new tab.

![The GraphQL Query Editor](assets/extract-content/query-editor.png)

Using the GraphQL Explorer you can build and validate queries against your headless content before using them to power the content in your app or website.

1. AEM Trials come with an endpoint preloaded with Content Fragments from which you can extract content for testing purposes. Select the **AEM Demo Assets** endpoint from the **Endpoint** drop-down menu at the top-right corner of the editor.

   ![Select endpoint](assets/extract-content/select-endpoint.png)

1. Copy the following code snippet for a list query of the preloaded **AEM Demo Assets** endpoint. A list query returns a list of all content that uses a specific Content Fragment model. Inventory and category pages typically use this query format.

   ```text
   {
       adventureList {
         items {
            _path
            adventureTitle
            adventurePrice
            adventureTripLength
            adventurePrimaryImage {
              ... on ImageRef {
               _path
               mimeType
               width
               height
             }
           }
         }
      }
    }
   ```

1. Then replace the existing content in the query editor by pasting the copied code.

    ![List query](assets/extract-content/list-query.png)

1. Once pasted, click the **Play** button at the top left of the query editor to execute the query.

1. The results are displayed in the right panel, next to the query editor. Should the query be incorrect, an error would appear in the right panel.

   ![List query results](assets/extract-content/list-query-results.png)

You've just validated a list query for a full list of all Content Fragments. This process helps to ensure that the response is what your app expects, with results that illustrate how your apps and websites will retrieve the content created in AEM. 

## Query for a Specific Piece of Sample Content {#bypath-query}

Running a byPath query allows you to retrieve content for a specific Content Fragment. Product detail pages and pages that focus on a specific set of content typically require this type of query.

1. Copy the following code snippet for a byPath query of the preloaded **AEM Demo Assets** endpoint.

   ```text
    {
     adventureByPath(
       _path: "/content/dam/aem-demo-assets/en/adventures/bali-surf-camp/bali-surf-camp"
     ) {
       item {
         _path
         adventureTitle
         adventureDescription {
           json
         }
         adventurePrimaryImage {
           ... on ImageRef {
             _path
             width
             height
           }
         }
       }
     }
   }
   ```

1. Then replace the existing content in the query editor by pasting the copied code.

   ![byPath query](assets/extract-content/bypath-query.png)

1. Once pasted, click the **Play** button at the top left of the query editor to execute the query.

1. The results are displayed in the right panel, next to the query editor. Should the query be incorrect, an error would appear in the right panel.

   ![byPath query results](assets/extract-content/bypath-query-results.png)

You've just validated a byPath query to retrieve a specific Content Fragment identified by the path of that fragment.

## Query Your Own Content {#own-queries}

Now that you have run the two primary types of queries, you are ready to query your own content.

1. To run queries against your own Content Fragments, change the endpoint from the **AEM Demo Assets** folder to the **Your Project** folder.

   ![Select your own endpoint](assets/extract-content/select-endpoint.png)

1. Delete all existing content in the query editor. Then type open bracket `{` and press Ctrl+Space or Option+Space for an auto-complete list of the models that were defined in your endpoint. Select the model that you created that ends in `List` from the options.

   ![Auto complete models in query editor](assets/extract-content/auto-complete-models.png)

1. Define the items that the query should contain for the Content Fragment model you selected. Again, type open bracket `{`, then press Ctrl+Space or Option+Space for an auto-complete list. Select `items` from the options.

   ![Auto complete items in query editor](assets/extract-content/auto-complete-items.png)

1. Define the fields that the query should contain for the content fragment model you selected. Again, type open bracket `{`, then press Ctrl+Space or Option+Space for an auto-complete list of available fields in the Content Fragment model. Select fields that you wish from your model from the list.

   ![Auto complete fields in query editor](assets/extract-content/auto-complete-fields.png)

1. Delimit multiple fields with a comma (`,`) or space and press Ctrl+Space or Option+Space again to select additional fields.

1. As you work, you can tap or click the **Prettify** button to automatically format your code so that it is easier to read.

   ![Prettify](assets/extract-content/prettify.png)

1. Once complete, tap or click the **Play** button at the top left of the editor to run the query.

   ![Results of your own query](assets/extract-content/custom-query-results.png)

1. The results are displayed in the right panel, next to the query editor.

This is how your content can be delivered to omnichannel digital experiences

## You've learned how to query content! {#conclusion}

Nice work! You've learned about the two basic types of queries and how to query your own content. You now understand how to use the AEM GraphQL API to create efficient queries that deliver content in a format that you app expects.
