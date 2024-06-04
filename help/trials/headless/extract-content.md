---
title: Extract Content via the GraphQL API
description: Learn how to use Content Fragments and the GraphQL API as a headless content management system.
hidefromtoc: yes
index: no
exl-id: f5e379c8-e63e-41b3-a9fe-1e89d373dc6b
feature: Onboarding
role: "Admin, User, Developer"
---

# Extract Content via the GraphQL API {#extract-content}

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_graphql"
>title="Extract content using the GraphQL API"
>abstract="In this module you learn how you can use Content Fragments and the GraphQL API as a headless content management system."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_graphql_guide"
>title="Launch the GraphQL Explorer"
>abstract="GraphQL provides a query-based API allowing external client applications to query AEM for only the content it needs, using a single API call. Follow this module to learn how to run two different types of queries. Then learn how to retrieve the content from the Content Fragment you created in the previous module.<br><br>Launch this module in a new tab by clicking below."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_admin_content_fragments_graphql_guide_footer"
>title="Nice work! You have learned about the two basic types of queries and how to query your own content. You now understand how to use the AEM GraphQL API to create efficient queries that deliver content in a format that you app expects."
>abstract=""

## Query for a List of Sample Content {#list-query}

You start on the GraphQL Explorer in a new tab. Here you can build and validate queries against your headless content before using them to power the content in your app or website.

1. Your AEM headless trial comes with an endpoint preloaded with Content Fragments from which you can extract content for testing purposes. Make sure that the **AEM Demo Assets** endpoint is selected in the **Endpoint** drop-down menu at the top-right corner of the editor.

1. Copy the following code snippet for a list query of the preloaded **AEM Demo Assets** endpoint. A list query returns a list of all content that uses a specific Content Fragment model. Inventory and category pages typically use this query format.

   ```text
   {
    adventureList {
     items {
       _path
       title
       price
       tripLength
       primaryImage {
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

1. Replace the existing content in the query editor by pasting the copied code.

1. Once pasted, click the **Play** button at the top left of the query editor to execute the query.

1. The results are displayed in the right panel, next to the query editor. Should the query be incorrect, an error would appear in the right panel.

   ![List query](assets/do-not-localize/list-query-1-3-4-5.png)

You have just validated a list query for a full list of all Content Fragments. This process helps to ensure that the response is what your app expects, with results that illustrate how your apps and websites will retrieve the content created in AEM.

## Query for a Specific Piece of Sample Content {#bypath-query}

Running a byPath query lets you retrieve content for a specific Content Fragment. Product detail pages and pages that focus on a specific set of content typically require this type of query.

1. Copy the following code snippet for a byPath query of the preloaded **AEM Demo Assets** endpoint.

   ```text
    {
     adventureByPath(
       _path: "/content/dam/aem-demo-assets/en/adventures/bali-surf-camp/bali-surf-camp"
     ) {
       item {
         _path
         title
         description {
           json
         }
         primaryImage {
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

1. Replace the existing content in the query editor by pasting the copied code.

1. Once pasted, click the **Play** button at the top left of the query editor to execute the query.

1. The results are displayed in the right panel, next to the query editor. Should the query be incorrect, an error would appear in the right panel.

   ![byPath query results](assets/do-not-localize/bypath-query-2-3-4.png)

You have just validated a byPath query to retrieve a specific Content Fragment identified by the path of that fragment.

## Query Your Own Content {#own-queries}

Now that you have run the two primary types of queries, you are ready to query your own content.

1. To run queries against your own Content Fragments, change the endpoint from the **AEM Demo Assets** folder to the **Your Project** folder.

1. Delete all existing content in the query editor. Then type open bracket `{` and press Ctrl+Space or Option+Space for an auto-complete list of the models that were defined in your endpoint. Select the model that you created that ends in `List` from the options. If you followed the examples in the previous modules, you should find `adventureList` in the auto-complete list.

   ![Start custom query](assets/do-not-localize/custom-query-1.png)

1. Define the items that the query should contain for the Content Fragment model you selected. Again, type open bracket `{`, then press Ctrl+Space or Option+Space for an auto-complete list. Select `items` from the options.

1. Select the **Prettify** button to automatically format your code so that it is easier to read.

1. Once complete, select the **Play** button at the top left of the editor to run the query. The editor auto-complete the `items`, which are briefly highlighted in yellow, and the query runs.

1. The results are displayed in the right panel, next to the query editor.

   ![Run custom query](assets/do-not-localize/custom-query-2.png)

This is how your content can be delivered to omnichannel digital experiences.

## Persisted Queries {#persisted-queries}

Persisted queries are the preferred mechanism for exposing the GraphQL API to client applications. Once a query has been persisted, it can be requested using a GET request and cached for fast retrieval.

You will create a persisted query that includes data you would like to consume from your client application.

1. You will use the data that you created as a content fragment earlier, so make sure that the **Your Project** endpoint is selected in the **Endpoint** drop-down menu at the top-right corner of the editor.

1. Copy the following code snippet.

   ```text
      {
      adventureList {
       items {
         title
         description {
           plaintext
         }
         price
         image {
           ... on ImageRef {
             _publishUrl
             mimeType
           }
         }
       }
     }
   }
   ```

1. Replace the existing content in the query editor by pasting the copied code. 

   >[!NOTE]
   >
   >If you did not use the same field descriptions as described in the previous modules, update the field names in this query.
   >
   >Use the GraphQL autocomplete (Ctrl+Space or Option+Space) feature as described previously to help identify the available properties.

1. Once pasted, click the **Play** button at the top left of the query editor to execute the query.

1. The results are displayed in the right panel, next to the query editor. Should the query be incorrect, an error would appear in the right panel.

   ![Create own query](assets/do-not-localize/own-query.png)

1. When satisfied with your query, click the **Save As** button at the top of the query editor to persist the query.

1. In the **Query name** pop-up, give your query the name `adventure-list`.

1. Select **Save As**.

   ![Persist query](assets/do-not-localize/persist-query.png)

1. The query is persisted as confirmed by a banner message at the bottom of the screen. The query also now appears in the left panel of persisted queries in the window.

1. For the persisted query to be available publicly, it must be published, much like how your Content Fragments need to be published. Click **Publish** at the top right of the query editor to publish the query.

1. The publication is confirmed by a banner notification.

You now have a new persisted query which will contain only the specific properties and formats that you defined.
