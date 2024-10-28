---
title: Pipeline-free URL Redirects
description: Learn how to declare 301 or 302 redirects without access to Git or Cloud Manager pipelines. 
feature: Dispatcher
role: Admin
---
# Pipeline-free URL Redirects {#pipeline-free-redirects}

>[!NOTE]
>This feature is not yet released.

For various reasons, organizations rewrite some URLs in a way that causes a 301 (or 302) redirect, meaning that the browser is redirected to a different page.

Scenarios include:

* A removed HTML page, so the user should be taken to a replacement page (sometimes the home page) rather than seeing a 404 Page Not Found error.
* A renamed HTML page.
* SEO optimization.

AEM as a Cloud Service offers [several approaches](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/administration/url-redirection) to implement these client-side redirects, but the strategy described in this article, pipeline-free redirects, is a good choice when:

* The people maintaining the redirects are business users, who do not have access to commit file changes to source control, nor the ability to execute a Cloud Manager web-tier config pipeline.
* The number of redirects ranges from just a few to tens of thousands.
* You want the option of a user interface, either created as a custom project or using [ACS Commons Rewrite Map Manager](https://adobe-consulting-services.github.io/acs-aem-commons/features/redirect-map-manager/index.html).

The core of this feature is the ability for AEM Apache/Dispatcher to load (or reload) one or more rewrite map files that have been placed in a specified location in the publish repository. It is important to note that how the file(s) get there is outside the scope of this feature, but customers can consider one of these methods:

* Ingesting the rewrite map as an asset in the author UI and publishing it.
* Installing the [ACS Commons Rewrite Map Manager](https://adobe-consulting-services.github.io/acs-aem-commons/features/redirect-map-manager/index.html), which includes a UI to manage the url mappings, and publishes it.
* Full flexibility by writing a custom application – for example: either a user interface or command line interface to manage the url mappings, or alternatively a form to upload a rewrite map, which uses AEM APIs to publish the rewrite map file.

>[!NOTE]
> This feature requires AEM version 18311 or higher.

## The rewrite map {#rewrite-map}

The rewrite map is reloaded (if changed) by the Apache HTTP server every 300 seconds by default, although this is configurable. The file format should abide by the plain text key-value map RewriteMap file format, described in [Apache documentation](https://httpd.apache.org/docs/2.4/rewrite/rewritemap.html#txt).

A file named `managed-rewrite-maps.yaml` should be created to specify the location of the rewrite map file, and it must be deployed once, using the Cloud Manager full stack pipeline or web tier pipeline. It should be created in the [src/opt-in](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/dispatcher.cloud/src/opt-in) folder of your dispatcher configuration. Make sure to use the [flexible mode file structure](/help/implementing/dispatcher/validation-debug.md#flexible-mode-file-structure).

You can configure it with the following pattern:

```
maps:
- name: my.map
  path: <path-in-publish-repository>/redirectmap.txt

```

For example, if your chosen method for placing the rewrite map file is to ingest it in AEM as an asset named `mysite-redirectmap.txt` and then publish it, you might specify a folder under `/content/dam`:

```
maps:
- name: my.map
  path: /content/dam/redirectmaps/mysite-redirectmap.txt

```

Next, in an apache configuration file, for example: `rewrites/rewrite.rules` or `<yourfile>.vhost`, you must configure the map file referenced by the name property ( `my.map` in the example above).

The RewriteMap directive must indicate that the data is stored in a DBM (Database manager) file format, by using the `sdbm` (simple DBM) format.

The rest of the configuration will depend on the format of the `redirectmap.txt`. The simplest format, show in the snippet below, is a 1:1 mapping between the original url to the mapped url:

```
# RewriteMap from managed rewrite maps
RewriteMap map.foo dbm=sdbm:/tmp/rewrites/my.map
RewriteCond ${map.foo:$1} !=""
RewriteRule ^(.*)$ ${map.foo:$1|/} [L,R=301]

```

## Considerations {#considerations}

Keep in mind the following:

* Apache has an 1024 length limit for RewriteMap single entries.
* By default, for the first load of a redirect map, Apache will start up without waiting for the full map file(s) to load, and thus there can be temporary inconsistencies until the full map(s) loads. This setting can be changed so Apache waits for the full map(s) contents to be loaded, but it will take longer for Apache to startup.
