---
title: Universal Editor Calls
description: Learn about the different types of calls made by the Universal Editor to your app to help you when debugging.
---

# Universal Editor Calls {#calls}

Learn about the different types of calls made by the Universal Editor to your app to help you when debugging.

## Overview {#overview}

The Universal Editor communicates with your instrumented app through a series of defined calls. This is transparent to and has no affect on the end user experience.

For the developer, however, understanding these calls and what they do can be valuable when debugging your application when using the Universal Editor. If you have instrumented your app and it is not behaving as anticipated, it can be very helpful to open the **Network** tab of the developer tools in your browser and inspect the calls as you edit content in your app.

![Example of a details call on the Network tab of the developer tools of the browser](assets/calls-network-tab.png)

The following is a list of the types of calls that the Universal Editor makes to your app.

## Update {#update}

An `update` call occurs when you edit content in your app using the Universal Editor to persist the changes.

Its payload includes details of what to write back to the JCR.

itemid: The JCR path to be updated
itemprop: The JCR property that is being updated
itemtype: The JCR value type of the property being updated
value: The update in the form of a JSON patch

Payload
```json
{
  "op": "patch",
  "connections": {
    "aem": "aem:https://localhost:8443"
  },
  "path": {
    "itemid": "urn:aem:/content/wknd/language-masters/en/jcr:content/root/container/carousel/item_1571954853062",
    "itemtype": "text",
    "itemprop": "jcr:title"
  },
  "value": "\nTiny Toon Adventures\n    "
}
```

Preview
```json
{
  "updates": [
    {
      "itemid": "urn:aem:/content/wknd/language-masters/en/jcr:content/root/container/carousel/item_1571954853062",
      "itemprop": "jcr:title",
      "itemtype": "text"
    }
  ]
}
```

## Details {#details}

A `details` call occurs when loading your app in the Universal Editor to retrieve the app's content.

Its payload includes the details of what the values represent so they can be rendered in the Universal Editor.

For a component, the Universal Editor will only retrieve a `data` object, since the schema of the data is defined in the app.

For Content Fragments, the Universal Editor will also retrieve a `schema` object since the Content Fragment Model is defined in the JCR.

Payload
```json
{
  "op": "patch",
  "connections": {
    "aem": "aem:https://localhost:8443"
  },
  "path": {
    "itemid": "urn:aem:/content/wknd/language-masters/en/jcr:content/root/container/carousel/item_1571954853062",
    "itemtype": "component",
    "itemprop": ""
  }
}
```

Data
```json
{
  "data": {
    "jcr:primaryType": "nt:unstructured",
    "jcr:title": "Tiny Toon Adventures!",
    "fileReference": "/content/dam/wknd-shared/en/adventures/riverside-camping-australia/adobestock-216674449.jpeg",
    "cq:panelTitle": "WKND Adventures",
    "actionsEnabled": "true",
    "jcr:lastModifiedBy": "admin",
    "titleFromPage": "false",
    "jcr:description": "<p>With WKND Adventures, you don't just see the world you experinece it.</p>",
    "jcr:lastModified": "Wed Jan 03 2024 09:06:05 GMT+0100",
    "descriptionFromPage": "true",
    "sling:resourceType": "wknd/components/teaser",
    "textIsRich": "true",
    "cq:styleIds": [
      "1555543212672"
    ],
    "actions": {
      "jcr:primaryType": "nt:unstructured",
      "item0": {
        "jcr:primaryType": "nt:unstructured",
        "link": "/content/wknd/language-masters/en/adventures",
        "text": "View Trips"
      }
    }
  }
}
```

## Add {#add}

An `add` call occurs when you place new content in your app using the Universal Editor.

Its payload includes a `path` object containing where the content should be added. It also includes a `content` object with additional objects for endpoint-specific details of the content to be stored [for each plugin.](/help/implementing/universal-editor/architecture.md) For example if your app is based on content from AEM and Magento, the payload would contain a data object for each system.

## Move {#move}

A `move` call occurs when you move a component within your app using the Universal Editor.

Its payload includes a `from` object defining where the component was and a `to` object defining where it was moved.

## Remove {#remove}

A `remove` call occurs when you delete a component within your app using the Universal Editor.

Its payload includes the path of the object that is removed.

## Patch {#patch}

A `patch` call occurs when you update content in a dialog within your app. This updates the content within the page of the app as a JSON patch to the existing content.

Its payload includes the path of the content on the page as well as the JSON patch of the change to be made.

## Publish {#publish}

A `publish` call occurs when you click the **Publish** button in the Universal Editor to publish the content that you have edited.

The response of all objects includes a list of items that need to be updated in the editor. For a move, the whole page must be updated since the content was reordered.