---
title: AEM Technical Foundations
description: An overview of the technical foundations of AEM including how AEM is structured and fundamental technologies like JCR, Sling, and OSGi.
exl-id: ab6e7fe9-a25d-4351-a005-f4466cc0f40e
feature: Developing
role: Admin, Architect, Developer
---
# AEM Technical Foundations {#aem-technical-foundations}

AEM is a robust platform built upon proven, scalable, and flexible technologies. This document gives a detailed overview of the various parts that make up AEM and is intended as a technical appendix for a full-stack AEM developer. It is not intended as a getting-started guide. If you are new to AEM development, see [Getting Started Developing AEM Sites - WKND Tutorial](develop-wknd-tutorial.md) as a first step.

>[!TIP]
>
>Before diving into the core technologies of AEM, Adobe recommends completing the [Getting Started Developing AEM Sites - WKND Tutorial](develop-wknd-tutorial.md).

## Fundamentals {#fundamentals}

As a modern content management system, AEM relies on standard web technologies:

* The request-response (XMLHttpRequest / XMLHttpResponse) cycle
* HTML
* CSS
* JavaScript

The underlying content repository and business logic layers are built around Java&trade; technologies:

* JCR
* Sling
* OSGi

## Java&trade; Content Repository {#java-content-repository}

The Java&trade; Content Repository (JCR) standard, [JSR 283](https://developer.adobe.com/experience-manager/reference-materials/spec/jcr/2.0/index.html), specifies a vendor-independent and implementation-independent way to access content bi-directionally on a granular level within a content repository. The specification lead is held by Adobe Research (Switzerland) AG.

The [JCR API 2.0](https://developer.adobe.com/experience-manager/reference-materials/spec/javax.jcr/javadocs/jcr-2.0/index.html) package, `javax.jcr.*` is used for the direct access and manipulation of repository content.

AEM is built upon a JCR.

## Apache Jackrabbit Oak {#jackrabbit-oak}

[Apache Jackrabbit Oak](https://jackrabbit.apache.org/oak/docs/) is an implementation of a scalable and high-performance hierarchical content repository for use as the foundation of modern world-class web sites and other demanding content applications, conforming to the JCR standard.

Jackrabbit Oak (also referred to simply as Oak), is the implementation of the JCR standard upon which AEM is built.

## Sling Request Processing {#sling-request-processing}

AEM is built using [Sling](https://sling.apache.org/index.html), a Web application framework based on REST principles that provides easy development of content-oriented applications. Sling uses a JCR repository, like Apache Jackrabbit Oak, as its data store. Sling has been contributed to the Apache Software Foundation - further information can be found at Apache.

### Introduction to Sling {#introduction-to-sling}

Using Sling, the type of content to be rendered is not the first processing consideration. Instead, the main consideration is whether the URL resolves to a content object for which a script can then be found to perform the rendering. This process provides excellent support for web content authors to build pages which are easily customized to their requirements.

The advantages of this flexibility are apparent in applications with a wide range of different content elements, or when you need pages that can be easily customized. In particular, when implementing a Web Content Management system such as AEM.

See [Discover Sling in 15 minutes](https://sling.apache.org/documentation/getting-started/discover-sling-in-15-minutes.html) for the first steps for developing with Sling.

The following diagram explains Sling script resolution. It shows how to get from HTTP request to content node, from content node to resource type, from resource type to script and what scripting variables are available.

![Understanding Apache Sling script resolution](assets/sling-cheatsheet-01.png)
 
The following diagram explains the hidden, but powerful, request parameters that you can use with `SlingPostServlet`, the default handler for all POST requests. The handler gives you endless options for creating, modifying, deleting, copying, and moving nodes in the repository.

![Using the SlingPostServlet](assets/sling-cheatsheet-02.png)

### Sling is Content Centric {#sling-is-content-centric}

Sling is *content-centric*. It means that processing is focused on the content as each (HTTP) request is mapped onto content in the form of a JCR resource (a repository node):

* The first target is the resource (JCR node) holding the content
* Second, the representation, or script, is located from the resource properties with certain parts of the request (for example, selectors and/or the extension)

### RESTful Sling {#restful-sling}

Due to its content-centric philosophy, Sling implements a REST-oriented server and thus features a new concept in web application frameworks. The advantages are:

* RESTful, not just on the surface; resources and representations are correctly modeled inside the server
* Removes one or more data models
  * Other content management frameworks might require URL structure, business objects, DB schema to access a resource.
  * Using Sling reduces it to: URL = resource = JCR structure

### URL Decomposition {#url-decomposition}

In Sling, processing is driven by the URL of the user request. It defines the content to display by the appropriate scripts and information is extracted from the URL.

Analyzing the following URL:

```text
https://myhost/tools/spy.printable.a4.html/a/b?x=12
```

You can break it down into its composite parts:

| protocol |host ||content path |selectors |extension |  |suffix |  |params  |
|---|---|---|---|---|---|---|---|---|---|
| `https://` |`myhost` |`/`|`tools/spy` |`.printable.a4.` |`html` |`/`| `a/b` |`?` |`x=12` |

* **protocol** - HTTPS
* **host** - Domain of the site
* **content path** - Path specifying the content to be rendered and is used with the extension. In this example, it translates to `tools/spy.html`
* **selectors** - Used for alternative methods of rendering the content; in this example a printer-friendly version in A4 format
* **extension** - Content format; also specifies the script to be used for rendering
* **suffix** - Can be used to specify additional information
* **params** - Any parameters required for dynamic content

#### From URL to Content and Scripts {#from-url-to-content-and-scripts}

Using the principles of URL decomposition:

* The mapping uses the content path extracted from the request to locate the resource.
* When the appropriate resource is located, the sling resource type is extracted, and used to locate the script to be used for rendering the content.

The following figure illustrates the mechanism used, which is discussed in more detail in the following sections.

![URL mapping mechanism](assets/url-mapping.png)

With Sling, you specify which script renders a certain entity (by setting the `sling:resourceType` property in the JCR node). This mechanism offers more freedom than one in which the script accesses the data entities (as an SQL statement in a PHP script would do) as a resource can have several renditions.

#### Mapping Requests to Resources {#mapping-requests-to-resources}

The request is broken down and the necessary information extracted. The repository is searched for the requested resource (content node):

* First Sling checks whether a node exists at the location specified in the request; for example, `../content/corporate/jobs/developer.html`
* If no node is found, the extension is dropped and the search repeated; for example, `../content/corporate/jobs/developer`
* If no node is found, then Sling returns the http code 404 (Not Found).

Sling also allows things other than JCR nodes to be resources, but this functionality is an advanced feature.

### Locating the Script {#locating-the-script}

When the appropriate resource (content node) is located, the **sling resource type** is extracted. This path locates the script to use for rendering the content.

The path specified by the `sling:resourceType` can be either:

* Absolute
* Relative to a configuration parameter

>[!TIP]
>
>Relative paths are recommended by Adobe as they increase portability.

All Sling scripts are stored in subfolders of either `/apps` (mutable, user scripts) or `/libs` (immutable, system scripts), which is searched in this order.

A few other points to note are:

* When the method (GET, POST) is required, it is specified in uppercase as according to the HTTP specification for example, `jobs.POST.esp`
* Various script engines are supported, but the common, recommended scripts are HTL and JavaScript.

The list of script engines supported by the given instance of AEM are listed on the Felix Management Console ( `http://<host>:<port>/system/console/slingscripting`).

Using the previous example, if the `sling:resourceType` is `hr/jobs` then for:

* GET/HEAD requests and URLs ending in `.html` (default request types, default format)
  * The script is `/apps/hr/jobs/jobs.esp`; the last section of the `sling:resourceType` forms the file name.
* POST requests (all request types excluding GET/HEAD, the method name must be uppercase)
  * POST is used in the script name.
  * The script is `/apps/hr/jobs/jobs.POST.esp`.
* URLs in other formats, not ending with `.html`
  * For example, `../content/corporate/jobs/developer.pdf`
  * The script is `/apps/hr/jobs/jobs.pdf.esp`; the suffix is added to the script name.
* URLs with selectors
  * Selectors can be used to display the same content in an alternative format. For example, a printer-friendly version, an rss feed or a summary.
  * If you look at a printer-friendly version where the selector could be `print`; as in `../content/corporate/jobs/developer.print.html`
  * The script is `/apps/hr/jobs/jobs.print.esp`; the selector is added to the script name.
* If no, `sling:resourceType` is defined then:
  * The content path is used to search for an appropriate script (if the path-based `ResourceTypeProvider` is active).
  * For example, the script for `../content/corporate/jobs/developer.html` would generate a search in `/apps/content/corporate/jobs/`.
  * The primary node type is used.
* If no script is found at all, then the default script is used.
  * The default rendition is supported as plain text (`.txt`), HTML (`.html`), and JSON (`.json`), all of which lists the node's properties (suitably formatted). The default rendition for the extension `.res`, or requests without a request extension, is to spool the resource (where possible).
* For http error handling (codes 403 or 404), Sling looks for a script at either:
  * The location `/apps/sling/servlet/errorhandler` for customized scripts
  * Or the location of the standard script `/libs/sling/servlet/errorhandler/404.jsp`

If multiple scripts apply for a given request, the script with the best match is selected. The more specific a match is, the better it is; in other words, the more selector matches the better, regardless of any request extension or method name match.

For example, consider a request to access the resource

* `/content/corporate/jobs/developer.print.a4.html`

Of type

* `sling:resourceType="hr/jobs"`

Assuming you have the following list of scripts in the correct location:

1. `GET.esp`
1. `jobs.esp`
1. `html.esp`
1. `print.esp`
1. `print.html.esp`
1. `print/a4.esp`
1. `print/a4/html.esp`
1. `print/a4.html.esp`

Then the order of preference would be (8) - (7) - (6) - (5) - (4) - (3) - (2) - (1).

In addition to the resource types (primarily defined by the `sling:resourceType` property), there is also the resource super type. This type is indicated by the `sling:resourceSuperType` property. These super types are also considered when trying to find a script. The advantage of resource super types is that they may form a hierarchy of resources where the default resource type `sling/servlet/default` (used by the default servlets) is effectively the root.

The resource super type of a resource may be defined in two ways:

* by the `sling:resourceSuperType` property of the resource.
* by the `sling:resourceSuperType` property of the node to which the `sling:resourceType` points.

For example:

* `/`
  * `a`
  * `b`
    * `sling:resourceSuperType = a`
  * `c`
    * `sling:resourceSuperType = b`
  * `x`
    * `sling:resourceType = c`
  * `y`
    * `sling:resourceType = c`
    * `sling:resourceSuperType = a`

The type hierarchy of:

* `/x`
  * Is `[ c, b, a, <default>]`
* While for `/y`
  * The hierarchy is `[ c, a, <default>]`

The reason is because `/y` has the `sling:resourceSuperType` property, whereas `/x` does not and therefore its supertype is taken from its resource type.

#### Sling Scripts Cannot be Called Directly {#sling-scripts-cannot-be-called-directly}

Within Sling, scripts cannot be called directly because it would break the strict concept of a REST server; you would mix resources and representations.

If you call the representation (the script) directly you hide the resource inside your script, so the framework (Sling) no longer knows about it. Thus you lose certain features:

* Automatic handling of http methods other than GET, including:
  * POST, PUT, DELETE which is handled with a sling default implementation
  * The `POST.jsp` script in your `sling:resourceType` location
* Your code architecture is no longer as clean nor as clearly structured as it should be; of prime importance for large-scale development

### Sling API {#sling-api}

Uses the Sling API package, `org.apache.sling.*`, and tag libraries.

### Referencing existing elements using sling:include {#referencing-existing-elements-using-sling-include}

A final consideration is the need to reference existing elements within the scripts.

More complex scripts (aggregating scripts) access multiple resources (for example, navigation, sidebar, footer, elements of a list), and do so by including the *resource*.

In this case, you can use the `sling:include("/<path>/<resource>")` command. It effectively includes the definition of the referenced resource.

## OSGi {#osgi}

OSGi (Open Services Gateway Initiative) defines an architecture for developing and deploying modular applications and libraries (it is also known as the Dynamic Module System for Java&trade;). OSGi containers allow you to break your application into individual modules (are jar files with additional meta information and called bundles in OSGi terminology) and manage the cross-dependencies between them with:

* Services implemented within the container
* A contract between the container and your application

These services and contracts provide an architecture which enables individual elements to dynamically discover each other for collaboration.

An OSGi framework then offers you dynamic loading/unloading, configuration, and control of these bundles - without requiring restarts.

>[!NOTE]
>
>Full information on OSGi technology can be found at the [OSGi website](https://www.osgi.org).
>
>In particular, their Basic Education page holds a collection of presentations and tutorials.

This architecture lets you extend Sling with application-specific modules. Sling, and therefore AEM, uses the [Apache Felix](https://felix.apache.org/documentation/index.html) implementation of OSGi. They are both collections of OSGi bundles running within an OSGi framework.

This functionality lets you perform the following actions on any of the packages within your installation:

* Install
* Start
* Stop
* Update
* Uninstall
* See latest status
* Access more detailed information about specific bundles, for example, symbolic name, version, and location

See [Configuring OSGi for AEM as a Cloud Service](/help/implementing/deploying/configuring-osgi.md) for more information.

## Structure within the Repository {#structure-within-the-repository}

The following list gives an overview of the structure that you see within the repository.

* `/apps` - Application related; includes component definitions specific to your website. The components that you develop can be based on the out of the box components available at `/libs/core/wcm/components`.
* `/content` - Content created for your website.
* `/etc`
* `/home` - User and Group information.
* `/libs` - Libraries and definitions that belong to the core of AEM. The subfolders in `/libs` represent the out-of-the box AEM features. The content in `/libs` may not be modified. Features specific to your website should be made under `/apps`.
* `/tmp` - Temporary working area.
* `/var` - Files that change and are updated by the system; such as audit logs, statistics, event-handling.

>[!CAUTION]
>
>Changes to this structure, or the files within it, should be made with care. Make sure that you fully understand the implications of any changes you make.
>
>Do not change anything in the `/libs` path. For configuration and other changes, copy the item from `/libs` to `/apps` and make any changes within `/apps`.
