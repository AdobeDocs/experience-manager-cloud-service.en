---
title: Pipeline-free URL Redirects
description: Learn how to declare 301 or 302 redirects without access to Git or Cloud Manager pipelines.
feature: Dispatcher
role: Admin
exl-id: dacb1eda-79e0-4e76-926a-92b33bc784de
---
# Pipeline-free URL Redirects {#pipeline-free-redirects}

For various reasons, organizations rewrite URLs in a way that causes a 301 (or 302) redirect, meaning that the browser is redirected to a different page.

Scenarios include:

* A removed HTML page, so the user is taken to a replacement page (sometimes the home page) rather than seeing a `404 Page Not Found` error.
* A renamed HTML page.
* SEO optimization.

AEM as a Cloud Service offers [several approaches](https://experienceleague.adobe.com/en/docs/experience-manager-learn/foundation/administration/url-redirection) to implement client-side redirects, but the strategy described in this article, pipeline-free redirects, is a good choice when:

* The people maintaining the redirects are business users, who do not have the necessary access to commit file changes to source control or the possibility to execute a Cloud Manager web-tier configuration pipeline.
* The number of redirects ranges from a few to tens of thousands.
* You want the option of a user interface, either created as a custom project or by using the [ACS Commons Redirect Map Manager](https://adobe-consulting-services.github.io/acs-aem-commons/features/redirect-map-manager/index.html) or [ACS Commons Redirect Manager](https://adobe-consulting-services.github.io/acs-aem-commons/features/redirect-manager/subpages/rewritemap.html).

The core of this feature is the ability for AEM Apache/Dispatcher to load (or reload) one or more rewrite map files that have been placed in a specified location in the publish repository (so that it is downloadable from AEM publish). It is important to mention that how the files get there is outside the scope of this feature but you can consider one of the following methods:

* Ingesting the rewrite map as an asset in the author user interface and publishing it.
* Installing the [ACS Commons Redirect Map Manager](https://adobe-consulting-services.github.io/acs-aem-commons/features/redirect-map-manager/index.html) ([at least 6.7.0 version or higher](https://github.com/Adobe-Consulting-Services/acs-aem-commons/releases)), which includes a user interface to manage the url mappings and can also publish the rewrite map file.
* Installing the [ACS Commons Redirect Manager](https://adobe-consulting-services.github.io/acs-aem-commons/features/redirect-manager/subpages/rewritemap.html) ([at least 6.10.0 version or higher](https://github.com/Adobe-Consulting-Services/acs-aem-commons/releases)), which also includes a user interface to manage the url mappings and can also publish the rewrite map file.
* Full flexibility by writing a custom application. For example, either a user interface or command line interface to manage the url mappings or alternatively a form to upload a rewrite map, which then uses AEM APIs to publish the rewrite map file.

>[!NOTE]
> This feature requires AEM version **18311 or higher**.

>[!NOTE]
> This feature's usage of Redirect Map Manager requires ACS Commons version **6.7.0 or higher** whereas usage of Redirect Manager requires version **6.10.0 or higher**.

## The rewrite map {#rewrite-map}

The rewrite map is reloaded (if changed) by the Apache HTTP server every 300 seconds by default (the value is configurable). The file format should follow the plain text key-value map RewriteMap file format described in the [Apache documentation](https://httpd.apache.org/docs/2.4/rewrite/rewritemap.html#txt).

A file named `managed-rewrite-maps.yaml` should be created to specify the location of the rewrite map file and it must be deployed once, by using the Cloud Manager full stack pipeline or the web tier pipeline. The file must be created in the [src/opt-in](https://github.com/adobe/aem-project-archetype/tree/develop/src/main/archetype/dispatcher.cloud/src/opt-in) folder of your dispatcher configuration. Make sure you use the [flexible mode file structure](/help/implementing/dispatcher/validation-debug.md#flexible-mode-file-structure).

You can configure it with the following pattern:

```
maps:
- name: my.map
  path: <path-in-publish-repository>/redirectmap.txt

```

If, for example, your chosen method to place the rewrite map file is to ingest it in AEM as an asset named `mysite-redirectmap.txt` and then publish it, you can specify a folder under `/content/dam`:

```
maps:
- name: my.map
  path: /content/dam/redirectmaps/mysite-redirectmap.txt

```

Next, in an Apache configuration file such as `rewrites/rewrite.rules` or `<yourfile>.vhost`, you must configure the map file referenced by the name property (`my.map` in the sample above). Once loaded, this map file is saved in the dispatcher local storage under the **fixed** location `/tmp/rewrites/`.

The `RewriteMap` directive should indicate that the data is stored in a database manager (DBM) file format by using the `sdbm` (simple DBM) format, and the full file path is derived from the storage location prefix and the name property.

The rest of the configuration depends on the format of the `redirectmap.txt`. The simplest format, shown in the sample below, is a one to one mapping between the original url to the mapped url:

```
# RewriteMap from managed rewrite maps
RewriteMap map.foo dbm=sdbm:/tmp/rewrites/my.map
RewriteCond ${map.foo:$1} !=""
RewriteRule ^(.*)$ ${map.foo:$1|/} [L,R=301]

```


## Considerations {#considerations}

Keep in mind the following:
 
* By default, when loading a rewrite map, Apache starts up without waiting for the full map file(s) to load, and thus there can be temporary inconsistencies until the full map(s) loads. This setting can be changed so that Apache waits for the full map contents to be loaded, but it takes longer for Apache to start up. To change this behavior so Apache waits, add `wait:true` to the `managed-rewrite-maps.yaml` file.
* To change the frequency between loads, add `ttl: <integer>` to the `managed-rewrite-maps.yaml` file. For example: `ttl: 120`.
* Apache has a 1024 length limit for RewriteMap single entries.
