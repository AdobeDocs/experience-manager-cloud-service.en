---
title: Getting Started with the Universal Editor in AEM
description: Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.
exl-id: 9091a29e-2deb-4de7-97ea-53ad29c7c44d
feature: Developing
role: Admin, Architect, Developer
---

# Getting Started with the Universal Editor in AEM {#getting-started}

Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.

>[!TIP]
>
>If you would prefer to dive right into an example, you can review the [Universal Editor Sample App on GitHub.](https://github.com/adobe/universal-editor-sample-editable-app)

Although the Universal Editor can edit content from any source, this document will use an AEM app as an example. This document will guide you through these steps.

## Instrument the Page {#instrument-page}

The Universal Editor requires a JavaScript library in order to render and edit the page in the editor.

In addition, the Universal Editor service requires a [uniform resource name (URN)](https://en.wikipedia.org/wiki/Uniform_Resource_Name) to identify and utilize the correct backend system for the content in the app being edited. Therefore, a URN schema is required to map content back to content resources.

### Include the Universal Editor CORS Library {#cors-library}

In order for the Universal Editor to connect to your app, your app must include the Universal Editor CORS library. Add the following script to your app.

```html
 <script src="https://universal-editor-service.adobe.io/cors.js" async></script>
```

### Creating Connections {#connections}

Connections which are used in the app are stored as `<meta>` tags in the page's `<head>`.

```html
<meta name="urn:adobe:aue:<category>:<referenceName>" content="<protocol>:<url>">
```

* `<category>` - This is a classification of the connection with two options.
  * `system` - For connection endpoints
  * `config` - For [defining optional configuration settings](#configuration-settings)
* `<referenceName>` - This is a short name which is reused in the document to identify the connection. E.g. `aemconnection`
* `<protocol>` - This indicates which persistence plugin of the Universal Editor Persistence Service to use. E.g. `aem`
* `<url>` - Ths is the URL to the system where the changes shall be persisted. E.g. `http://localhost:4502`

The identifier `urn:adobe:aue:system` represents the connection for the Adobe Universal Editor.

`data-aue-resource`s will use the `urn` prefix to shorten the identifier.

```html
data-aue-resource="urn:<referenceName>:<resource>"
```

* `<referenceName>` - This is the named reference mentioned in the `<meta>` tag. E.g. `aemconnection`
* `<resource>` - This is a pointer to the resource in the target system. E.g. an AEM content path such as `/content/page/jcr:content`

>[!TIP]
>
>See the document [Attributes and Types](attributes-types.md) for further details about the data attributes and types that the Universal Editor requires.

### Example Connection {#example}

```html
<meta name="urn:adobe:aue:system:<referenceName>" content="<protocol>:<url>">

<html>
<head>
    <meta name="urn:adobe:aue:system:aemconnection" content="aem:https://localhost:4502">
    <meta name="urn:adobe:aue:system:fcsconnection" content="fcs:https://example.franklin.adobe.com/345fcdd">
</head>
<body>
        <aside>
          <ul data-aue-resource="urn:aemconnection:/content/example/list" data-aue-type="container">
            <li data-aue-resource="urn:aemconnection:/content/example/listitem" data-aue-type="component">
              <p data-aue-prop="name" data-aue-type="text">Jane Doe</p>
              <p data-aue-prop="title" data-aue-type="text">Journalist</p>
              <img data-aue-prop="avatar" src="https://www.adobe.com/content/dam/cc/icons/Adobe_Corporate_Horizontal_Red_HEX.svg" data-aue-type="image" alt="avatar"/>
            </li>

...

            <li data-aue-resource="urn:fcsconnection:/documents/mytext" data-aue-type="component">
              <p data-aue-prop="name" data-aue-type="text">John Smith</p>
              <p data-aue-resource="urn:aemconnection:/content/example/another-source" data-aue-prop="title" data-aue-type="text">Photographer</p>
              <img data-aue-prop="avatar" src="https://www.adobe.com/content/dam/cc/icons/Adobe_Corporate_Horizontal_Red_HEX.svg" data-aue-type="image" alt="avatar"/>
            </li>
          </ul>
        </aside>
</body>
</html>
```

### Configuration Settings {#configuration-settings}

You can use the `config` prefix in your connection URN to set service and extension endpoints if necessary.

If you would like not to use the Universal Editor Service, which is hosted by Adobe, but your own hosted version, you can set this in a meta tag. To overwrite the default service endpoint that the Universal Editor provides, set your own service endpoint:

* Meta name - `urn:adobe:aue:config:service`
* Meta content - `content="https://adobe.com"` (example)

```html
<meta name="urn:adobe:aue:config:service" content="<url>">
```

If you only want to have certain extensions enabled for a page, you can set this in a meta tag. To fetch extensions, set the extension endpoints:

* Meta name: `urn:adobe:aue:config:extensions`
* Meta content: `content="https://adobe.com,https://anotherone.com,https://onemore.com"` (example)

```html
<meta name="urn:adobe:aue:config:extensions" content="<url>,<url>,<url>">
```

## Define for which content paths or `sling:resourceType`s the Universal Editor shall be opened. (Optional) {#content-paths}

If you have an existing AEM project using [the page editor,](/help/sites-cloud/authoring/page-editor/introduction.md) when content authors edit pages, the pages are opened automatically with the page editor. You can define which editor AEM should open based on the content paths or the `sling:resourceType`, making the experience seamless for your authors, regardless of which editor is required for the selected content.

1. Open the Configuration Manager.

   `http://<host>:<port>/system/console/configMgr`

1. Locate **Universal Editor URL Service** in the list and click **Edit the configuration values**.

1. Define for which content paths or `sling:resourceType`s the Universal Editor shall be opened.

   * In the **Universal Editor Opening Mapping** field, provide the paths for which the Universal Editor is opened.
   * In the **Sling:resourceTypes which shall be opened by Universal Editor** field, provide a list of resources which are opened directly by the Universal Editor.

1. Click **Save**.

AEM will open the Universal Editor for pages based on this configuration in the following order.

1. AEM will check the mappings under `Universal Editor Opening Mapping` and if the content is under any paths defined there, the Universal Editor is opened for it.
1. For content not under paths defined in `Universal Editor Opening Mapping`, AEM checks if the `resourceType` of the content matches those defined in **Sling:resourceTypes which shall be opened by Universal Editor** and if the content matches one of those types, the Universal Editor is opened for it at `${author}${path}.html`.
1. Otherwise AEM opens the Page Editor.

The following variables are available to define your mappings in the **Universal Editor Opening Mapping** field.

* `path`: Content path of the resource to open
* `localhost`: Externalizer entry for `localhost` without schema, e.g. `localhost:4502`
* `author`: Externalizer entry for author without schema, e.g. `localhost:4502`
* `publish`: Externalizer entry for publish without schema, e.g. `localhost:4503`
* `preview`: Externalizer entry for preview without schema, e.g. `localhost:4504`
* `env`: `prod`, `stage`, `dev` based on the defined Sling run modes
* `token`: Query token required for the `QueryTokenAuthenticationHandler`

### Example Mappings {#example-mappings}

* Open all pages under `/content/foo` on the AEM Author:

  * `/content/foo:${author}${path}.html?login-token=${token}`
  * This results in opening `https://localhost:4502/content/foo/x.html?login-token=<token>`

* Open all pages under `/content/bar` on a remote NextJS server, providing all variables as information:

  * `/content/bar:nextjs.server${path}?env=${env}&author=https://${author}&publish=https://${publish}&login-token=${token}`
  * This results in opening `https://nextjs.server/content/bar/x?env=prod&author=https://localhost:4502&publish=https://localhost:4503&login-token=<token>`

## You're Ready to Use the Universal Editor {#youre-ready}

Your app is now instrumented to use the Universal Editor!

See [Authoring Content with the Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md) to learn how easy and intuitive it is for content authors to create content using the Universal Editor.

## Additional Resources {#additional-resources}

To learn more about the Universal Editor, see these documents.

* [Universal Editor Introduction](introduction.md) - Learn how the Universal Editor enables editing any aspect of any content in any implementation so you can deliver exceptional experiences, increase content velocity, and provide a state-of-the-art developer experience.
* [Authoring Content with the Universal Editor](/help/sites-cloud/authoring/universal-editor/authoring.md) - Learn how easy and intuitive it is for content authors to create content using the Universal Editor.
* [Publishing Content with the Universal Editor](/help/sites-cloud/authoring/universal-editor/publishing.md) - Learn how the Universal Editor publishes content and how your apps can handle the published content.
* [Universal Editor Architecture](architecture.md) - Learn about the architecture of the Universal Editor and how data flows between its services and layers.
* [Attributes and Types](attributes-types.md) - Learn about the data attributes and types that the Universal Editor requires.
* [Universal Editor Authentication](authentication.md) - Learn how the Universal Editor authenticates.

