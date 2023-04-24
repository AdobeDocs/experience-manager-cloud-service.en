---
title: Fetch JSON content with JavaScript
description: Explore fetching JSON content from your trial environment with a CodePen app and the AEM Headless Client for JavaScript.
hidefromtoc: yes
index: no
exl-id: b7dc70f2-74a2-49f7-ae7e-776eab9845ae
---
# Fetch JSON content with JavaScript {#fetch-json}

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_fetch_json_with_javascript"
>title="Fetch JSON content with JavaScript"
>abstract="Explore fetching JSON content from your trial environment with a CodePen app and the AEM Headless Client for JavaScript."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_fetch_json_with_javascript_guide"
>title="Launch the sample CodePen app"
>abstract="We've put together a minimal CodePen app to introduce fetching JSON data from your trial environment using GraphQL persisted queries.<br><br>Launch the CodePen example by clicking below, then follow this guide to learn more."

>[!CONTEXTUALHELP]
>id="aemcloud_sites_trial_fetch_json_with_javascript_guide_footer"
>title="In this module, you learned how to use the AEM Headless Client for JavaScript to fetch JSON data from your trial environment using GraphQL persisted queries.<br><br>Now you understand how you can use this client to consume data from within your own web application."
>abstract=""

## Introduction {#intro}

You begin in the CodePen app, which serves as a minimal example of fetching JSON data using the [AEM Headless Client for JavaScript](https://github.com/adobe/aem-headless-client-js). The sample app is designed to render any JSON content which is returned, regardless of the structure of the underlying content fragment model. The CodePen app tries to be verbose with any errors that are encountered, so you may see the following error message printed to the bottom pane of the app:

```
{
  "status": "Failed to fetch persisted query: your-project/USE-YOUR-QUERY-HERE from publishHost: https://publish-p00000-e12345.adobeaemcloud.com",
  "message": "[AEMHeadless:REQUEST_ERROR] General Request error: Failed to fetch."
}
```

This error is expected, as the app is not yet configured to use the persisted query that you saved and published in a previous module. You will configure the app to fetch data from your specific query in the following steps.

## CodePen walkthrough {#code-walkthrough}

The JS (Javascript) pane on CodePen contains the brains of the example app. Beginning on line 2, we import the AEM Headless Client for JavaScript from the Skypack CDN. Skypack is used to facilitate development without a build step, but you can also use the AEM Headless Client with NPM or Yarn in your own projects. Check out the usage instructions in the [README](https://github.com/adobe/aem-headless-client-js#aem-headless-client-for-javascript) for further detail.

```
import AdobeAemHeadlessClientJs from 'https://cdn.skypack.dev/@adobe/aem-headless-client-js@v3.2.0';
```

On line 6 we read your publish host details from the `publishHost` query parameter. This is the host that the AEM Headless Client will fetch data from. This would typically be coded into your app, but we are using a query parameter to make it easier for the CodePen app to work with different environments.

We configure the AEM Headless Client on line 12 to use a proxy Adobe IO Runtime function to avoid CORS issues. This is not required for your own projects, but is required for the CodePen app to work with your trial environment. The proxy function is configured to use the `publishHost` value that was provided in the query parameter.

```
const aemHeadlessClient = new AdobeAemHeadlessClientJs({
  // Use a proxy to avoid CORS issues
  serviceURL: 'https://102588-505tanocelot.adobeioruntime.net/api/v1/web/aem/proxy',
  headers: {
    'aem-url': publishHost
  }
});
```

Finally, the function `fetchJsonFromGraphQL()` is used to perform the fetch request using the AEM Headless Client. It is called each time the code is changed, or can be triggered by pressing the "Refetch" link. The actual `aemHeadlessClient.runPersistedQuery(..)` call occurs on line 34. A bit later we'll make a change to the way this JSON data is rendered, but for now we'll just print it to the `#output` div using the `resultToPreTag(queryResult)` function.

## Fetch data from your persisted query {#use-persisted-query}

On line 25 we indicate which GraphQL persisted query the app should fetch data from. The persisted query name is a combination of the name of the project (ie. `your-project`), followed by a forward slash, and then the name of the query. 

Update the `persistedQueryName` variable to use the persisted query you created in the previous module. If you followed the naming suggestion exactly you would have created a persisted query named `adventures` in the `your-project` project, and you would set the `persistedQueryName` variable to `your-project/adventures`:

```
//
// TODO: Use your persisted query here
//
persistedQueryName = 'your-project/adventures';
```

Once this change is made the app should automatically refresh, and print the raw JSON response from your persisted query to the `#output` div. If you see an error message, check the console for additional details.

Does this JSON contain the exact properties your app needs? If not, head back to your AEM Author environment, Tools, GraphQL Query Editor (or navigate to the `/aem/graphiql.html` path) and make changes to your persisted query. Don't forget to save and publish the query once you are done.

## Change the JSON rendering {#change-rendering}

Currently, the JSON is being rendered as-is into a `pre` tag, which is not very creative. We can switch our CodePen to use the `resultToDom()` function instead to illustrate how the JSON response can be iterated over to create a more interesting result.

To make this change, comment out line 37 and remove the comment from line 40: 

```
// Output the results to a pre tag
//resultToPreTag(queryResult);

// Alternatively, build a colorful div structure with the JSON results and render images inline
resultToDom(queryResult);
```

This function will also render any images that are included in the JSON response as an `img` tag. If the "Adventure" content fragments you created do not include any images, you can try switching to use the `aem-demo-assets/adventures-all` persisted query by modifying line 25:

```
persistedQueryName = 'aem-demo-assets/adventures-all';
```

This query will yield a JSON response that includes images, and the `resultToDom()` function will render them inline.

![Result of the adventures-all query and the resultToDom rendering function](assets/do-not-localize/adventures-all-query-result.png)
