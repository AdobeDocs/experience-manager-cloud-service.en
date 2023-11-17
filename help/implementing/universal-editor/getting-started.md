---
title: Getting Started with the Universal Editor in AEM
description: Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.
exl-id: 9091a29e-2deb-4de7-97ea-53ad29c7c44d
---

# Getting Started with the Universal Editor in AEM {#getting-started}

Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.

>[!TIP]
>
>If you would prefer to dive right into an example, you can review the [Universal Editor Sample App on GitHub.](https://github.com/adobe/universal-editor-sample-editable-app)

## Onboarding Steps {#onboarding}

Although the Universal Editor can edit content from any source, this document will use an AEM app as an example.

There are several steps to onboarding your AEM app and instrumenting it to use the Universal Editor.

1. [Request access to the Universal Editor.](#request-access)
1. [Include the Universal Editor core library.](#core-library)
1. [Add the necessary OSGi configuration.](#osgi-configurations)
1. [Instrument the page.](#instrument-page)

This document will guide you through these steps.

## Request Access to the Universal Editor {#request-access}

You first need to request access to the Universal Editor. See [https://experience.adobe.com/#/aem/editor](https://experience.adobe.com/#/aem/editor), sign in, and validate if you have access to the Universal Editor.

In case you do not have access, it can be requested via a form linked on the same page.

![Request access to the Universal Editor](assets/request-access.png)

Click **Request access** and fill out the form as directed to request access. An Adobe representative will review your request and reach out to discuss your use case.

## Include the Universal Editor Core Library {#core-library}

Before your app can be instrumented for use with the Universal Editor, it must include following dependency.

```javascript
@adobe/universal-editor-cors
```

To activate the instrumentation, the following import must be added to your `index.js`.

```javascript
import "@adobe/universal-editor-cors";
```

### Alternative for Non-React Apps {#alternative}

If you are not implementing a React app and/or require server-side rendering an alternative method is to include the following to the document body.

```html
<script src="https://cdn.jsdelivr.net/gh/adobe/universal-editor-cors/dist/universal-editor-embedded.js" async></script>
```

## Add the Necessary OSGi Configurations {#osgi-configurations}

To be able to edit AEM content with your app using the Universal Editor, CORS and cookie settings must be done within AEM.

The following [OSGi configurations have to be set on the AEM authoring instance.](/help/implementing/deploying/configuring-osgi.md)

* `SameSite Cookies = None` in `com.day.crx.security.token.impl.impl.TokenAuthenticationHandler`
* Remove X-FRAME-OPTIONS: SAMEORIGIN Header in `org.apache.sling.engine.impl.SlingMainServlet`

### com.day.crx.security.token.impl.impl.TokenAuthenticationHandler {#samesite-cookies}

The login token cookie must be sent to AEM as a third-party domain. Therefore the same-site cookie must be set explicitly to `None`.

This property must be set in the `com.day.crx.security.token.impl.impl.TokenAuthenticationHandler` OSGi configuration.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jcr:root xmlns:sling="http://sling.apache.org/jcr/sling/1.0"
          xmlns:jcr="http://www.jcp.org/jcr/1.0" jcr:primaryType="sling:OsgiConfig"
          token.samesite.cookie.attr="None" />
```

### org.apache.sling.engine.impl.SlingMainServlet {#sameorigin}

X-Frame-Options: SAMEORIGIN prevents rendering AEM pages within an iframe. Removing the header allows the pages to be loaded.

This property must be set in the `org.apache.sling.engine.impl.SlingMainServlet` OSGi configuration.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<jcr:root xmlns:sling="http://sling.apache.org/jcr/sling/1.0"
          xmlns:jcr="http://www.jcp.org/jcr/1.0"
          jcr:primaryType="sling:OsgiConfig"
          sling.additional.response.headers="[X-Content-Type-Options=nosniff]"/>
```

## Instrument the Page {#instrument-page}

The Universal Editor service requires a [uniform resource name (URN)](https://en.wikipedia.org/wiki/Uniform_Resource_Name) to identify and utilize the correct backend system for the content in the app being edited. Therefore, a URN schema is required to map content back to content resources.

The instrumentation attributes added to the page consist mostly of [HTML Microdata,](https://developer.mozilla.org/en-US/docs/Web/HTML/Microdata) an industry-standard that can also be used to make HTML more semantic, make HTML documents indexable, and so on.

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

`itemid`s will use the `urn` prefix to shorten the identifier.

```html
itemid="urn:<referenceName>:<resource>"
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
          <ul itemscope itemid="urn:aemconnection:/content/example/list" itemtype="container">
            <li itemscope itemid="urn:aemconnection/content/example/listitem" itemtype="component">
              <p itemprop="name" itemtype="text">Jane Doe</p>
              <p itemprop="title" itemtype="text">Journalist</p>
              <img itemprop="avatar" src="https://www.adobe.com/content/dam/cc/icons/Adobe_Corporate_Horizontal_Red_HEX.svg" itemtype="image" alt="avatar"/>
            </li>

...

            <li itemscope itemid="urn:fcsconnection:/documents/mytext" itemtype="component">
              <p itemprop="name" itemtype="text">John Smith</p>
              <p itemid="urn:aemconnection/content/example/another-source" itemprop="title" itemtype="text">Photographer</p>
              <img itemprop="avatar" src="https://www.adobe.com/content/dam/cc/icons/Adobe_Corporate_Horizontal_Red_HEX.svg" itemtype="image" alt="avatar"/>
            </li>
          </ul>
        </aside>
</body>
</html>
```

### Configuration Settings {#configuration-settings}

You can use the `config` prefix in your connection URN to set service and extension endpoints if required.

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

## You're Ready to Use the Universal Editor {#youre-ready}

Your app is now instrumented to use the Universal Editor!

See [Authoring Content with the Universal Editor](authoring.md) to learn how easy and intuitive it is for content authors to create content using the Universal Editor.

## Additional Resources {#additional-resources}

To learn more about the Universal Editor, see these documents.

* [Universal Editor Introduction](introduction.md) - Learn how the Universal Editor enables editing any aspect of any content in any implementation so you can deliver exceptional experiences, increase content velocity, and provide a state-of-the-art developer experience.
* [Authoring Content with the Universal Editor](authoring.md) - Learn how easy and intuitive it is for content authors to create content using the Universal Editor.
* [Publishing Content with the Universal Editor](publishing.md) - Learn how the Universal Editor publishes content and how your apps can handle the published content.
* [Universal Editor Architecture](architecture.md) - Learn about the architecture of the Universal Editor and how data flows between its services and layers.
* [Attributes and Types](attributes-types.md) - Learn about the data attributes and types that the Universal Editor requires.
* [Universal Editor Authentication](authentication.md) - Learn how the Universal Editor authenticates.
