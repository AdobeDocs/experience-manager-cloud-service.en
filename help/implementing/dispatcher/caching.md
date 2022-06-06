---
title: Caching in AEM as a Cloud Service
description: Caching in AEM as a Cloud Service 
feature: Dispatcher
exl-id: 4206abd1-d669-4f7d-8ff4-8980d12be9d6
---
# Introduction {#intro}

Traffic passes through the CDN to an apache web server layer, which supports modules including the dispatcher. In order to increase performance, the dispatcher is used primarily as a cache to limit processing on the publish nodes.
Rules can be applied to the dispatcher configuration to modify any default cache expiration settings, resulting in caching at the CDN. Note that dispatcher also respects the resulting cache expiration headers if `enableTTL` is enabled in the dispatcher configuration, implying that it will refresh specific content even outside of content being republished.

This page also describes how dispatcher cache is invalidated, as well as how caching works at the browser level with regards to client-side libraries.

## Caching {#caching}

### HTML/Text {#html-text}

* by default, cached by the browser for five minutes, based on the `cache-control` header emitted by the apache layer. The CDN also respects this value.
* the default HTML/Text caching setting can be disabled by defining the `DISABLE_DEFAULT_CACHING` variable in `global.vars`:

```
Define DISABLE_DEFAULT_CACHING

```

This can be useful, for example, when your business logic requires fine tuning of the age header (with a value based on calendar day) since by default the age header is set to 0. That said, **please exercise caution when turning off default caching.**

* can be overridden for all HTML/Text content by defining the `EXPIRATION_TIME` variable in `global.vars` using the AEM as a Cloud Service SDK Dispatcher tools.
* can be overridden on a finer grained level, including controlling CDN and browser cache independently, with the following apache mod_headers directives:

   ```
   <LocationMatch "^/content/.*\.(html)$">
        Header set Cache-Control "max-age=200"
        Header set Surrogate-Control "max-age=3600"
        Header set Age 0
   </LocationMatch>
   ```

   >[!NOTE]
   >The Surrogate-Control header applies to the Adobe managed CDN. If using a [customer managed CDN](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn.html?lang=en#point-to-point-CDN), a different header may be required depending on your CDN provider.

   Exercise caution when setting global cache control headers or those that match a wide regex so they are not applied to content that you might intend to keep private. Consider using multiple directives to ensure rules are applied in a fine-grained manner. With that said, AEM as a Cloud Service will remove the cache header if it detects that it has been applied to what it detects to be uncacheable by dispatcher, as described in dispatcher documentation. In order to force AEM to always apply the caching headers, one can add the **always** option as follows:

   ```
   <LocationMatch "^/content/.*\.(html)$">
        Header unset Cache-Control
        Header unset Expires
        Header always set Cache-Control "max-age=200"
        Header set Age 0
   </LocationMatch>

   ```

   You must ensure that a file under `src/conf.dispatcher.d/cache` has the following rule (which is in the default configuration):

   ```
   /0000
   { /glob "*" /type "allow" }

   ```

* To prevent specific content from being cached **at the CDN**, set the Cache-Control header to *private*. For example, the following would prevent html content under a directory named **secure** from being cached at the CDN:

   ```
      <LocationMatch "/content/secure/.*\.(html)$">.  // replace with the right regex
      Header unset Cache-Control
      Header unset Expires
      Header always set Cache-Control “private”
     </LocationMatch>

   ```

   >[!NOTE]
   >The other methods, including the [dispatcher-ttl AEM ACS Commons project](https://adobe-consulting-services.github.io/acs-aem-commons/features/dispatcher-ttl/), will not successfully override values.

   >[!NOTE]
   >Please note that dispatcher might still cache content according to its own [caching rules](https://experienceleague.adobe.com/docs/experience-cloud-kcs/kbarticles/KA-17497.html). To make the content truly private you should ensure that it is not cached by dispatcher.

### Client-Side libraries (js,css) {#client-side-libraries}

* by using AEM's Client-Side library framework, JavaScript and CSS code is generated in such a way that browsers can cache it indefinitely, since any changes manifest as new files with a unique path.  In other words, HTML that references the client libraries will be produced as needed so customers can experience new content as it is published. The cache-control is set to "immutable" or 30 days for older browsers who don't respect the "immutable" value.
* see the section [Client-side libraries and version consistency](#content-consistency) for additional details.

### Images and any content large enough to be stored in blob storage {#images}

The default behavior for programs created after mid-May 2022 (specifically, for program ids that are higher than 65000) is to cache by default, while also respecting the request's authentication context. Older programs (program ids equal or lower than 65000) do not cache blob content by default.

In both cases, the caching headers can be overridden on a finer grained level at the apache/dispatcher layer by using the apache `mod_headers` directives, for example:

   ```
      <LocationMatch "^/content/.*\.(jpeg|jpg)$">
        Header set Cache-Control "max-age=222"
        Header set Age 0
      </LocationMatch>

   ```

When modifying the caching headers at the dispatcher layer, please be cautious not to cache too widely, see the discussion in the HTML/text section [above](#html-text). Also, make sure that assets that are meant to be kept private (rather than cached) are not part of the `LocationMatch` directive filters.

#### New default caching behavior {#new-caching-behavior}

The AEM layer will set cache headers depending on whether the cache header has already been set and the value of the request type. Please note that if no cache control header has been set, public content is cached and authenticated traffic is set to private. If a cache control header has been set, the cache headers will be untouched.

| Cache control header exists? | Request type  | AEM sets cache headers to                      |
|------------------------------|---------------|------------------------------------------------|
| No                           | public        | Cache-Control: public, max-age=600, immutable  |
| No                           | authenticated | Cache-Control: private, max-age=600, immutable |
| Yes                          | any           | unchanged                                      |

While not recommended, it is possible to change the new default behavior to follow the older behavior (program ids equal or lower than 65000) by setting the Cloud Manager environment variable `AEM_BLOB_ENABLE_CACHING_HEADERS` to false.

#### Older default caching behavior {#old-caching-behavior}

The AEM layer will not cache blob content by default.

>[!NOTE]
>It is recommended to change the older default behavior to be consistent with the new behavior (program ids that are higher than 65000) by setting the Cloud Manager environment variable AEM_BLOB_ENABLE_CACHING_HEADERS to true. If the program is already live, make sure you verify that after the changes, content behaves as you expect.

>[!NOTE]
>The other methods, including the [dispatcher-ttl AEM ACS Commons project](https://adobe-consulting-services.github.io/acs-aem-commons/features/dispatcher-ttl/), will not successfully override the values.

### Other content file types in node store {#other-content}

* no default caching
* default cannot be set with the `EXPIRATION_TIME` variable used for html/text file types
* cache expiration can be set with the same LocationMatch strategy described in the html/text section by specifying the appropriate regex

### Further Optimizations {#further-optimizations}

* Avoid using `User-Agent` as part of the `Vary` header. Older versions of the default dispatcher setup (prior to archetype version 28) included this and we recommend you remove that using the steps below.
   * Locate the vhost files in `<Project Root>/dispatcher/src/conf.d/available_vhosts/*.vhost`
   * Remove or comment out the line: `Header append Vary User-Agent env=!dont-vary` from all vhost files, with the exception of default.vhost, which is read-only
* Use the `Surrogate-Control` header to control CDN caching independent from browser caching
* Consider applying [`stale-while-revalidate`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#stale-while-revalidate) and [`stale-if-error`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control#stale-if-error) directives to allow background refresh and avoid cache misses, keeping your content fast and fresh for users.
   * There are many ways to apply these directives, but adding a 30 minute `stale-while-revalidate` to all cache control headers is a good starting point.
* Some examples follow for various content types, which can be used as a guide when setting up your own caching rules. Please carefully consider and test for your specific setup and requirements:

   * Cache mutable client library resources for 12h and background refresh after 12h.
      ```
      <LocationMatch "^/etc\.clientlibs/.*\.(?i:json|png|gif|webp|jpe?g|svg)$">
         Header set Cache-Control "max-age=43200,stale-while-revalidate=43200,stale-if-error=43200,public" "expr=%{REQUEST_STATUS} < 400"
         Header set Age 0
      </LocationMatch>
      ```

   * Cache immutable client library resources long-term (30 days) with background refresh to avoid MISS.
      ```
      <LocationMatch "^/etc\.clientlibs/.*\.(?i:js|css|ttf|woff2)$">
         Header set Cache-Control "max-age=2592000,stale-while-revalidate=43200,stale-if-error=43200,public,immutable" "expr=%{REQUEST_STATUS} < 400"
         Header set Age 0
      </LocationMatch>
      ```

   * Cache HTML pages for 5min with background refresh 1h on browser and 12h on CDN. Cache-Control headers will always be added so it is important to ensure that matching html pages under /content/* are intended to be public. If not, consider using a more specifc regex.
      ```
      <LocationMatch "^/content/.*\.html$">
         Header unset Cache-Control
         Header always set Cache-Control "max-age=300,stale-while-revalidate=3600" "expr=%{REQUEST_STATUS} < 400"
         Header always set Surrogate-Control "stale-while-revalidate=43200,stale-if-error=43200" "expr=%{REQUEST_STATUS} < 400"
         Header set Age 0
      </LocationMatch>
      ```

   * Cache content services/Sling model exporter json responses for 5min with background refresh 1h on browser and 12h on CDN.
      ```
      <LocationMatch "^/content/.*\.model\.json$">
         Header set Cache-Control "max-age=300,stale-while-revalidate=3600" "expr=%{REQUEST_STATUS} < 400"
         Header set Surrogate-Control "stale-while-revalidate=43200,stale-if-error=43200" "expr=%{REQUEST_STATUS} < 400"
         Header set Age 0
      </LocationMatch>
      ```

   * Cache immutable URLs from the core image component long-term (30 days) with background refresh to avoid MISS.
      ```
      <LocationMatch "^/content/.*\.coreimg.*\.(?i:jpe?g|png|gif|svg)$">
         Header set Cache-Control "max-age=2592000,stale-while-revalidate=43200,stale-if-error=43200,public,immutable" "expr=%{REQUEST_STATUS} < 400"
         Header set Age 0
      </LocationMatch>
      ```

   * Cache mutable resources from the DAM like images and video for 24h and background refresh after 12h to avoid MISS
      ```
      <LocationMatch "^/content/dam/.*\.(?i:jpe?g|gif|js|mov|mp4|png|svg|txt|zip|ico|webp|pdf)$">
         Header set Cache-Control "max-age=43200,stale-while-revalidate=43200,stale-if-error=43200" "expr=%{REQUEST_STATUS} < 400"
         Header set Age 0
      </LocationMatch>
      ```

### HEAD request behavior {#request-behavior}

When a HEAD request is received at the Adobe CDN for a resource that is **not** cached, the request is transformed and received by the dispatcher and/or AEM instance as a GET request. If the response is cacheable then subsequent HEAD requests will be served from the CDN. If the response is not cacheable then subsequent HEAD requests will be passed to the dispatcher and/or AEM instance for a period of time that depends on the `Cache-Control` TTL.

## Dispatcher Cache Invalidation {#disp}

In general, it will not be necessary to invalidate the dispatcher cache. Instead you should rely on the dispatcher refreshing its cache when content is being republished and the CDN respecting cache expiration headers.

### Dispatcher Cache Invalidation during Activation/Deactivation {#cache-activation-deactivation}

Like previous versions of AEM, publishing or unpublishing pages will clear the content from the dispatcher cache. If a caching issue is suspected, customers should republish the pages in question and ensure that a virtual host is available that matches ServerAlias localhost, which is required for dispatcher cache invalidation.

When the publish instance receives a new version of a page or asset from the author, it uses the flush agent to invalidate appropriate paths on its dispatcher. The updated path is removed from the dispatcher cache, together with its parents, up to a level (you can configure this with the [statfileslevel](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/configuring/dispatcher-configuration.html#invalidating-files-by-folder-level)).


## Explicit dispatcher cache invalidation {#explicit-invalidation}

While Adobe's recommendation is to rely on standard cache headers to control the content delivery life cycle, it is possible to invalidate content directly in the dispatcher.

Here are some scenarios where one might want to explicitly invalidate the cache, while optionally listening to the completion of that invalidation:

* after publishing content such as experience fragments or content fragments, invalidating published and cached that reference those elements
* notifying an external system when referenced pages are successfully invalidated.

There are two approaches: using Sling Content Distribution (SCD) from the author, which is preferred, and using the Replication API to invoke the publish dispatcher flush replication agent. The approaches differ in terms of (a) tier availability, and (b) ability to deduplicate the events, and (c) event processing guarantee. The table below summarizes the options:

insert table here

In the table above, the SCD API’s INVALIDATE action and the Replication API’s DEACTIVATE action are the actions relevant to the pure cache invalidation use case.

From the table, we observe that:

SCD API is needed when every event must be guaranteed; for example, syncing with an external system that requires accurate knowledge. In addition, note that if there is a publish tier upscaling event at the time of the invalidation call, an addition events will be raised when each new publish processes the invalidation 

Using the Replication API isn’t common, but should be used in cases where the trigger to invalidate the cache comes from the publish tier and not author tier. This might be useful if dispatcher TTL is configured.

If you’re looking to invalidate dispatcher cache, the recommended option:

1. Use SCD API Invalidate action from Author.
2. (Optional) Listen for the event to then trigger any downstream actions.

### Sling Content Distribution (SCD) {#sling-distribution}

Here is the implementation pattern for using SCD:

1. From the author, write custom code to invoke the sling content distribution [API](https://sling.apache.org/documentation/bundles/content-distribution.html), passing the invalidate action with a list of paths:

```
@Reference
private Distributor distributor;

ResourceResolver resolver = ...; // the resource resolver used for authorizing the request
String agentName = "publish";    // the name of the agent used to distribute the request

String pathToInvalidate = "/content/to/invalidate";
DistributionRequest distributionRequest = new SimpleDistributionRequest(DistributionRequestType.INVALIDATE, false, pathToInvalidate);
distributor.distribute(agentName, resolver, distributionRequest);

```

2. Optionally listen for an event that reflects the resource being invalidated for all dispatcher instances:


```
package org.apache.sling.distribution.journal.shared;

import org.apache.sling.discovery.DiscoveryService;
import org.apache.sling.distribution.journal.impl.event.DistributionEvent;
import org.osgi.service.component.annotations.Component;
import org.osgi.service.component.annotations.Reference;
import org.osgi.service.event.Event;
import org.osgi.service.event.EventHandler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import static org.apache.sling.distribution.DistributionRequestType.INVALIDATE;
import static org.apache.sling.distribution.event.DistributionEventProperties.DISTRIBUTION_PATHS;
import static org.apache.sling.distribution.event.DistributionEventProperties.DISTRIBUTION_TYPE;
import static org.apache.sling.distribution.event.DistributionEventTopics.AGENT_PACKAGE_DISTRIBUTED;
import static org.osgi.service.event.EventConstants.EVENT_TOPIC;

@Component(immediate = true, service = EventHandler.class, property = {
        EVENT_TOPIC + "=" + AGENT_PACKAGE_DISTRIBUTED
})
public class InvalidatedHandler implements EventHandler {
    private static final Logger LOG = LoggerFactory.getLogger(InvalidatedHandler.class);

    @Reference
    private DiscoveryService discoveryService;

    @Override
    public void handleEvent(Event event) {

        String distributionType = (String) event.getProperty(DISTRIBUTION_TYPE);

        if (INVALIDATE.name().equals(distributionType)) {
            boolean isLeader = discoveryService.getTopology().getLocalInstance().isLeader();
            // process the OSGi event on the leader author instance
            if (isLeader) {
                String[] paths = (String[]) event.getProperty(DISTRIBUTION_PATHS);
                String packageId = (String) event.getProperty(DistributionEvent.PACKAGE_ID);
                invalidated(paths, packageId);
            }
        }
    }

    private void invalidated(String[] paths, String packageId) {
        // custom logic
        LOG.info("Successfully applied package with id {}, paths {}", packageId, paths);
    }
}

```

<!-- Optionally, instead of using the isLeader approach, one could add an OSGi configuration for the PID org.apache.sling.distribution.journal.impl.publisher.DistributedEventNotifierManager and property deduplicateEvent=true. But we'll stick with just one strategy and not mention it (double-check this).**review this**-->

3. Optionally execute some business logic in the invalidated(String[] paths, String packageId) method above.

Note: The Adobe CDN is not flushed when the dispatcher is invalidated. The Adobe-managed CDN respects TTLs and thus there is no need for it to be flushed.

### Replication API {#replication-api}

Here is the implementation pattern for using the Replication API:

1. On the publish tier, call the Replication API to trigger the publish dispatcher flush replication agent.

The flush agent endpoint is not configurable but rather preconfigured to point to the dispatcher, matched with the publish service running alongside the flush agent. The flush agent can typically be triggered by custom code based on OSGi events or workflows.

```
String[] paths = …
ReplicationOptions options = new ReplicationOptions();
options.setSynchronous(true);
options.setFilter( new AgentFilter {
  public boolean isIncluded (Agent agent) {
   return agent.getId().equals(“flush”);
  }
});

Replicator.replicate (session,ReplicationActionType.DELETE,paths, options);
```

<!-- In general, it will not be necessary to manually invalidate content in the dispatcher, but it is possible if needed.

>[!NOTE]
>Prior to AEM as a Cloud Service, there were two ways of invalidating the dispatcher cache.
>
>1. Invoke the replication agent, specifying the publish dispatcher flush agent
>2. Directly calling the `invalidate.cache` API (for example, `POST /dispatcher/invalidate.cache`)
>
>The dispatcher's `invalidate.cache` API approach will no longer be supported since it addresses only a specific dispatcher node. AEM as a Cloud Service operates at the service level, not the individual node level and so the invalidation instructions in the [Invalidating Cached Pages From AEM](https://experienceleague.adobe.com/docs/experience-manager-dispatcher/using/configuring/page-invalidate.html) page are not longer valid for AEM as a Cloud Service.

The replication flush agent should be used. This can be done using the [Replication API](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/com/day/cq/replication/Replicator.html). The flush agent endpoint is not configurable but pre-configured to point to the dispatcher, matched with the publish service running the flush agent. The flush agent can typically be triggered by OSGi events or workflows.

<!-- Need to find a new link and/or example -->
<!-- 
and for an example of flushing the cache, see the [API example page](https://helpx.adobe.com/experience-manager/using/aem64_replication_api.html) (specifically the `CustomStep` example issuing a replication action of type ACTIVATE to all available agents). 

The diagram presented below illustrates this.

![CDN](assets/cdnd.png "CDN")

If there is a concern that the dispatcher cache isn't clearing, contact [customer support](https://helpx.adobe.com/support.ec.html) who can flush the dispatcher cache if necessary.

The Adobe-managed CDN respects TTLs and thus there is no need fo it to be flushed. If an issue is suspected, [contact customer support](https://helpx.adobe.com/support.ec.html) support who can flush an Adobe-managed CDN cache as necessary. -->

## Client-Side libraries and Version Consistency {#content-consistency}

Pages are composed of of HTML, Javascript, CSS, and images. Customers are encouraged to leverage the [Client-Side Libraries (clientlibs) framework](/help/implementing/developing/introduction/clientlibs.md) to import Javascript and CSS resources into HTML pages, taking into account dependencies between JS libraries.

The clientlibs framework provides automatic version management, meaning that developers can check in changes to JS libraries in source control and the latest version will be made available when a customer pushes their release. Without this, developers would need to manually change HTML with references to the new version of the library, which is especially onerous if many HTML templates share the same library.

When the new versions of libraries are released to production, the referencing HTML pages are updated with new links to those updated library versions. Once the browser cache has expired for a given HTML page, there is no concern that the old libraries will be loaded from the browser cache since the refreshed page (from AEM) now is guaranteed to reference the new versions of the libraries. In other words, a refreshed HTML page will include all the latest library versions.

The mechanism for this is a serialized hash, which is appended to the client library link, ensuring a unique, versioned url for the browser to cache the CSS/JS. The serialized hash is only updated when the contents of the client library changes. This means that if unrelated updates occur (i.e no changes to the underlying css/js of the client library) even with a new deployment, the reference remains the same, ensuring less disruption to the browser cache.

### Enabling Longcache versions of Client Side Libraries - AEM as a Cloud Service SDK Quickstart {#enabling-longcache}

Default clientlib includes on an HTML page look like the following example:

```
<link rel="stylesheet" href="/etc.clientlibs/wkndapp/clientlibs/clientlib-base.css" type="text/css">

```

When strict clientlib versioning is enabled, a long term hash key is added as a selector to the client library. As a result, the clientlib reference look like this:

```
<link rel="stylesheet" href="/etc.clientlibs/wkndapp/clientlibs/clientlib-base.lc-7c8c5d228445ff48ab49a8e3c865c562-lc.css" type="text/css">

```

Strict clientlib versioning is enabled by default in all AEM as a Cloud Service environments.

To enable strict clientlib versioning in the local SDK Quickstart perform the following actions:

1. Navigate to the OSGi Configuration manager `<host>/system/console/configMgr`
1. Find the OSGi Config for Adobe Granite HTML Library Manager:
   * Check the checkbox to enable Strict Versioning
   * In the field labeled Long term client side cache key, enter the value of /.*;hash
1. Save the changes. Note that it is not necessary to save this configuration in source control since AEM as a Cloud Service will automatically enable this configuration in dev, stage and production environments.
1. Any time the contents of the client library are changed, a new hash key is generated and the HTML reference will be updated.
