---
title: Getting Started with the Universal Editor in AEM
description: Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.
feature: Page Editor
hide: yes
hidefromtoc: yes
index: no
---

# Getting Started with the Universal Editor in AEM {#getting-started}

Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.

## Onboarding Steps {#onboarding}

Although the Universal Editor can edit content from any source, this document will use an AEM app as an example.

There are a number of steps to onboarding your AEM app and instrumenting it to use the Universal Editor.

1. [Request access to the Universal Editor.](#request-access)
1. [Include the Universal Editor core library.](#core-library)
1. [Add the necessary OSGi configuration.](#osgi-configurations)
1. [Instrument the page.](#instrument-page)

This document will guide you through these steps.

## Request Access to the Universal Editor {#request-access}

You first need to request access to the Universal Editor. Please go to [https://experience.adobe.com/#/aem/editor](https://experience.adobe.com/#/aem/editor) and validate if you have access to the Universal Editor.

In case you do not have access, it can be requested via a form linked on the same page.

## Include the Universal Editor Core Library {#core-library}

Before your app can be instrumented for use with the Universal Editor, it needs to include following dependency.

```javascript
@aem-sites/universal-editor-cors
```

To activate the instrumentation, the following import needs to be added to your `index.js`.

```javascript
import "@aem-sites/universal-editor-cors";
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

The instrumentation attributes added to the page consist mostly of [HTML Microdata,](https://developer.mozilla.org/en-US/docs/Web/HTML/Microdata) an industry-standard that can also be used to make HTML more semantic, make HTML documents indexable, etc.

### Creating Connections {#connections}

Connections which are used in the app are stored as `<meta>` tags in the page's `<head>`.

```html
<meta name="urn:auecon:<referenceName>" content="<protocol>:<url>">
```

* `<referenceName>` - This is a short name which is reused in the document to identify the connection. E.g. `aemconnection`
* `<protocol>` - This indicates which persistence plugin of the Universal Editor Persistence Service to use. E.g. `aem`
* `<url>` - Ths is the URL to the system where the changes shall be persisted. E.g. `http://localhost:4502`

The short identifier `auecon` stands for Adobe Universal Editor Connection.

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
<html>
<head>
    <meta name="urn:auecon:aemconnection" content="aem:https://localhost:4502">
    <meta name="urn:auecon:fcsconnection" content="fcs:https://example.franklin.adobe.com/345fcdd">
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

### Universal Editor Translation Service {#translation}

The Universal Editor performs translation based on the instrumentation metadata.

#### Basic Translation Principle {#principle}

Consider the following selection from the previous example.

```html
<meta name="urn:auecon:aemconnection" content="aem:https://localhost:4502">
<ul itemscope itemid="urn:aemconnection:/content/example/list" itemtype="urn:fcs:type/list">
```

The editor will perform replacements and internally the `itemid` will be re-written to the following.

```html
itemid="urn:aem:https://localhost:4502/content/example/list"
```

This results in the term `aemconnection` being replaced by the content of the `<meta>` tag.

#### Query Selector {#query-selector}

This replacement will result into following query string for John Smith.

```html
<ul itemscope itemid="urn:aemconnection:/content/example/list" itemtype="urn:fcs:type/list">
  <li itemscope itemid="urn:fcsconnection:/documents/mytext" itemtype="urn:fcs:type/fragment">.  
    <p itemprop="name" itemtype="text">John Smith</p>
    <p itemid="urn:aemconnection/content/example/another-source" itemprop="title" itemtype="text">Photographer</p>
    <img itemprop="avatar" src="urn:fcs:missing" itemtype="image" alt="avatar"/>
  </li>
```

`[itemid="urn:fcs:https://example.franklin.adobe.com/345fcdd/content/example/list][itemprop="name"]`

If you want to alter the tile of John Smith, the selector will be the following.

`[itemid="urn:aem:https://localhost:4502/content/example/another-source"][itemprop="title"]`

Instead of inheritance of `itemid`s and resources, the Universal Editor works with scopes. A scope can be defined on a node level and be inherited by the entire sub-structure.

In case a different scope is required for a sub-structure within the structure or a defined leave, another `itemid` can be defined.

## You're Ready to Use the Universal Editor {#youre-ready}

Your app is now instrumented to use the Universal Editor!

Please refer to the document [Authoring Content with the Universal Editor](authoring.md) to learn how easy and intuitive it is for content authors to create content using the Universal Editor.

## Additional Resources {#additional-resources}

To learn more about the Universal Editor, see these documents.

* [Universal Editor Introduction](introduction.md) - Learn how the Universal Editor enables editing any aspect of any content in any implementation in order to deliver exceptional experiences, increase content velocity, and provide a state-of-the-art developer experience.
* [Authoring Content with the Universal Editor](authoring.md) - Learn how easy and intuitive it is for content authors to create content using the Universal Editor.
* [Universal Editor Architecture](architecture.md) - Learn about the architecture of the Universal Editor and how data flows between its services and layers.
* [Attributes and Types](attributes-types.md) - Learn about the data attributes and types that the Universal Editor requires.
* [Universal Editor Authentication](authentication.md) - Learn how the Universal Editor authenticates.
