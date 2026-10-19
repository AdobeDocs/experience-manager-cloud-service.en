---
title: Custom Instrumentation with OpenTelemetry
description: Add your own spans, span attributes, and trace-correlated logs to your AEM as a Cloud Service application code with the OpenTelemetry API, with worked examples from the WKND reference site.
feature: Developing
role: Developer
---
# Custom instrumentation with OpenTelemetry {#custom-instrumentation}

<!--

AUTHOR NOTE (October 2026): every code sample on this page comes from a working, instrumented build of the WKND
reference site (unit tests and the AEM analyser passing). The outcomes (span names, instrumentation scopes,
attributes, status, events, and log fields) were verified end to end on an AEM as a Cloud Service environment
running OpenTelemetry Java agent 2.27.0. The error path of Examples 4 and 5 was verified with the same agent and
collector configuration outside AEM as a Cloud Service, because the Content AI lookup did not fail on the
environment. Re-verify the API versions in Step 1 when Adobe moves to a newer agent.

-->

When [OpenTelemetry](/help/implementing/developing/introduction/opentelemetry-apm-integration.md) is enabled for your environment, AEM as a Cloud Service traces every request and exports JVM, HTTP, and AEM metrics automatically. That telemetry describes AEM. It shows that a page took 900 milliseconds to render and which components it rendered. It cannot show what your own code was doing, such as which list item a repository query was for and whether it found anything, or which pages fall back to an expensive search because an author left out a field.

You can add that knowledge yourself with the OpenTelemetry API. The spans and attributes that your code creates travel with the automatic telemetry: same service name, same processing, same APM provider. You do not configure an endpoint, a credential, or an exporter in your code.

The examples on this page instrument the [WKND reference site](https://github.com/adobe/aem-guides-wknd). Each example describes what you want to achieve, the code to add, and the outcome you can expect in your APM provider.

>[!NOTE]
>
>Custom instrumentation requires OpenTelemetry to be enabled for your environment. See [Set up the integration](/help/implementing/developing/introduction/opentelemetry-apm-integration.md#set-up).

## How custom instrumentation works {#how-it-works}

* The OpenTelemetry Java agent that Adobe runs in your AEM environment contains the OpenTelemetry SDK and exporters. Your code depends only on the OpenTelemetry **API**.
* When your code calls `GlobalOpenTelemetry`, the agent connects it to its own implementation. Your spans become part of the trace of the request that runs them, and your telemetry is exported with the rest of your environment's telemetry.
* Where the agent is not present (the local AEM SDK, unit tests, or an environment without OpenTelemetry enabled), the API does nothing, at negligible cost. You can deploy the same code to every environment.

| What you add | How | Sent to your APM provider |
|---|---|---|
| Spans | A `Tracer`, or the `@WithSpan` annotation | Yes |
| Attributes, events, and error status on spans | The `Span` API | Yes |
| Log entries correlated with traces | Your existing SLF4J logging | Yes, at `WARN` level and above, when logs are enabled |

>[!NOTE]
>
>Custom metrics, such as counters and histograms that your code creates, are planned for an upcoming release.

## Set up your project {#set-up-project}

### Step 1: Add the OpenTelemetry API {#add-api}

Add the OpenTelemetry API and the instrumentation annotations to the `dependencyManagement` section of your project's parent `pom.xml`, with the `provided` scope:

```xml
<properties>
    <opentelemetry.version>1.61.0</opentelemetry.version>
    <opentelemetry-instrumentation.version>2.27.0</opentelemetry-instrumentation.version>
</properties>

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.opentelemetry</groupId>
            <artifactId>opentelemetry-api</artifactId>
            <version>${opentelemetry.version}</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>io.opentelemetry.instrumentation</groupId>
            <artifactId>opentelemetry-instrumentation-annotations</artifactId>
            <version>${opentelemetry-instrumentation.version}</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

Then add both dependencies, without versions, to the `pom.xml` of each bundle that uses them, such as `core/pom.xml`:

```xml
<dependency>
    <groupId>io.opentelemetry</groupId>
    <artifactId>opentelemetry-api</artifactId>
</dependency>
<dependency>
    <groupId>io.opentelemetry.instrumentation</groupId>
    <artifactId>opentelemetry-instrumentation-annotations</artifactId>
</dependency>
```

Use `opentelemetry-api` 1.61.0 and `opentelemetry-instrumentation-annotations` 2.27.0, or earlier versions. They match the OpenTelemetry Java agent that AEM as a Cloud Service runs, and later versions of the agent continue to support them. API features added after the version that the agent supports have no effect.

<!-- AUTHOR NOTE: 1.61.0 / 2.27.0 match OpenTelemetry Java agent 2.27.0 (opentelemetry-init GENERIC_VERSION v2.27.0; the agent's instrumentation BOM imports opentelemetry-bom 1.61.0). When Adobe moves to a newer agent, these versions keep working; update them only if you want to recommend newer API features. -->

### Step 2: Embed the API in your bundle {#embed-api}

AEM as a Cloud Service does not export the OpenTelemetry API packages, so each bundle that uses the API must contain its own copy. Add the following instructions to the bnd configuration of your bundle. With the [AEM Project Archetype](https://github.com/adobe/aem-project-archetype), that is the `bnd-maven-plugin` configuration in `core/pom.xml`. Keep any entries that your `Import-Package` instruction already has.

```text
Import-Package: !io.opentelemetry.*,javax.annotation;version=0.0.0,*
-includepackage: io.opentelemetry.*
```

| Instruction | Why it is needed |
|---|---|
| `!io.opentelemetry.*` at the start of `Import-Package` | The API refers to optional OpenTelemetry packages that AEM does not provide, and loads them only if they are present. Without this exclusion, your bundle imports those packages, it cannot start, and the Cloud Manager build fails. See [Troubleshooting](#troubleshooting). |
| `-includepackage: io.opentelemetry.*` | Copies the **complete** API into your bundle. The agent connects your bundle's copy of the API to its own implementation only when the whole API is present. If you embed only the packages that your code refers to, for example with `-conditionalpackage`, your spans and attributes are discarded without an error. |

Each bundle that uses the API embeds its own copy, and the agent connects each copy separately.

>[!CAUTION]
>
>Do not add the OpenTelemetry SDK, an exporter, or the SDK autoconfigure module to your project, and do not create your own `OpenTelemetrySdk` instance or call `GlobalOpenTelemetry.set()`. Telemetry sent that way bypasses the agent, the removal of Cloud Service infrastructure details described in [What data is sent](/help/implementing/developing/introduction/opentelemetry-apm-integration.md#what-data-is-sent), and the endpoint that you configured.

### Step 3: Create a tracer {#create-tracer}

Create one `Tracer` for your code base and reuse it everywhere. In WKND, a small class holds it:

```java
package com.adobe.aem.guides.wknd.core.telemetry;

import io.opentelemetry.api.GlobalOpenTelemetry;
import io.opentelemetry.api.trace.Tracer;

public final class WkndTelemetry {

    /** Instrumentation scope: identifies telemetry produced by WKND code in your APM provider. */
    public static final String SCOPE = "com.adobe.aem.guides.wknd";

    public static final Tracer TRACER = GlobalOpenTelemetry.getTracer(SCOPE);

    private WkndTelemetry() {
    }
}
```

The scope name appears on every span that you create through this tracer, as the instrumentation scope (or library name). Use a name that identifies your code, such as your project's base Java package.

## Where your spans appear {#where-spans-appear}

On AEM as a Cloud Service, a page request already produces spans from AEM itself. The spans that your code creates are added inside them. For example, this is the path to the Image List component in a trace of the WKND Magazine page:

```text
GET /*                                                     the request (AEM)
└─ SlingMainServlet.service                                Sling request processing (AEM)
   └─ AEM component: cq:Page                               (AEM)
      └─ AEM component: wknd/components/page               the page component (AEM)
         └─ HTL: libs.core.wcm.components.page.v3.page.page__002e__html
            └─ ...                                         containers and layout grids (AEM)
               └─ AEM component: wknd/components/image-list
                  └─ HTL: apps.wknd.components.image__002d__list.image__002d__list__002e__html
                     └─ ...                                spans that the Image List's Sling Model creates
```

While a component renders, the span of its HTL script is the current span. A Sling Model that the script loads with `data-sly-use` runs inside that span, so spans that the model creates become its children.

Every request span is named `GET /*` (or `POST /*`, and so on). To find the traces for a particular page, search on the `url.path` attribute of the request span, or add your own attributes, as shown in [Example 3](#current-span).

## Examples {#examples}

### Example 1: Trace an expensive operation {#trace-operation}

#### What you want to achieve {#trace-operation-goal}

The WKND Image List component (`wknd/components/image-list`) displays a list of pages, each with its first image. To find that image, its Sling Model, `ImageListImpl`, runs one QueryBuilder query for every item in the list. AEM's own spans already show those queries: on the WKND Magazine page, which lists five articles, the trace contains five `JCR query` spans under the Image List's HTL span. They do not show which list item each query was for, whether it found an image, or the time spent processing the results. The original code timed the query with `System.currentTimeMillis()` and wrote the result to a `DEBUG` log entry, which is not available in production. You want each query to appear in the trace as a named operation, with that context.

#### The code {#trace-operation-code}

In `ImageListImpl.findPageComponentResources()`, create a span around the query:

```java
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.StatusCode;
import io.opentelemetry.context.Scope;

// ... build the QueryBuilder parameters, as before

final Span span = WkndTelemetry.TRACER.spanBuilder("ImageList.findPageComponentResources")
        .setAttribute("wknd.query.path", page.getContentResource().getPath())
        .setAttribute("wknd.query.resource_type", slingResourceType)
        .setAttribute("wknd.query.limit", limit)
        .startSpan();

try (Scope ignored = span.makeCurrent()) {
    // ... run the query and collect the resources, as before

    span.setAttribute("wknd.query.result_count", componentResources.size());
} catch (RuntimeException e) {
    span.recordException(e);
    span.setStatus(StatusCode.ERROR, "Image List query failed");
    throw e;
} finally {
    span.end();
}

return componentResources;
```

* `makeCurrent()` makes your span the parent of everything that runs inside the block, including the spans that AEM creates for the repository query.
* Always call `end()` in a `finally` block. A span that is not ended is never exported.
* Give the span a fixed name that describes the operation, and put values that vary, such as paths, in attributes.

#### The outcome {#trace-operation-outcome}

On the WKND Magazine page, which lists five articles, the trace now contains five `ImageList.findPageComponentResources` spans inside the Image List, one for each list item. Each one is the parent of the `JCR query` span that AEM creates for its query:

```text
AEM component: wknd/components/image-list
└─ HTL: apps.wknd.components.image__002d__list.image__002d__list__002e__html
   ├─ ImageList.findPageComponentResources        your span
   │  └─ JCR query                                AEM
   ├─ ImageList.findPageComponentResources
   │  └─ JCR query
   └─ ...                                         three more
```

Each of your spans has the instrumentation scope `com.adobe.aem.guides.wknd` and the following attributes:

| Attribute | Example value |
|---|---|
| `wknd.query.path` | `/content/wknd/us/en/magazine/arctic-surfing/jcr:content` |
| `wknd.query.resource_type` | `wknd/components/image` |
| `wknd.query.limit` | `1` |
| `wknd.query.result_count` | `1` |

You can now see, for each list item, which page the query searched, whether it found an image (`wknd.query.result_count` is `0` when it did not), and how long the whole lookup took, including processing the results. On the WKND Magazine page, each lookup takes about 6.5 milliseconds, of which the repository query itself takes about 3.5: half of the time goes into processing the results, which AEM's own spans do not show. Because the query count grows with the length of the list, you can also see how much of the component's rendering time the lookups account for.

### Example 2: Trace a method with an annotation {#with-span}

#### What you want to achieve {#with-span-goal}

WKND's `SocialImageImpl` model runs on every page to fill in the `og:image` meta tag. If an author has not set a featured image, the model walks the page's content tree to find the first image, visiting up to 500 resources. You want to know how often that walk runs, and how much of the tree it visits, without restructuring the method.

#### The code {#with-span-code}

Annotate the method with `@WithSpan`:

```java
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.instrumentation.annotations.WithSpan;

@WithSpan("SocialImage.resolveFromFirstImageOnPage")
protected boolean resolveFromFirstImageOnPage() {
    Resource contentResource = currentPage.getContentResource();
    if (contentResource == null) {
        return false;
    }

    int[] visitedCount = new int[]{0};
    Resource firstImage = findFirstImage(contentResource, 0, visitedCount);

    // Span.current() is the span that @WithSpan started for this method.
    Span.current().setAttribute("wknd.social_image.nodes_visited", visitedCount[0]);
    Span.current().setAttribute("wknd.social_image.walk_truncated", visitedCount[0] > MAX_NODES_TO_VISIT);

    // ... use firstImage, as before
}
```

* The agent starts a span each time the method runs and ends it when the method returns or throws an exception.
* `@WithSpan` works on public, protected, and private methods.
* To record a method parameter as an attribute, annotate the parameter with `@SpanAttribute`, for example `void applyTemplate(@SpanAttribute("wknd.page.template") String template)`.
* The annotation takes effect only where the agent runs. In the local AEM SDK and in unit tests, the method runs unchanged.

#### The outcome {#with-span-outcome}

A `SocialImage.resolveFromFirstImageOnPage` span appears only in the traces of pages that have no featured image:

| Attribute | Example value |
|---|---|
| `wknd.social_image.nodes_visited` | `21` |
| `wknd.social_image.walk_truncated` | `false` |
| `code.namespace` | `com.adobe.aem.guides.wknd.core.models.impl.SocialImageImpl` (added by the agent) |
| `code.function` | `resolveFromFirstImageOnPage` (added by the agent) |

Search for this span name to list the pages that need a featured image. If `wknd.social_image.walk_truncated` is `true`, the walk stopped at 500 resources and the page may have no social image at all.

Spans created by `@WithSpan` carry the agent's instrumentation scope (`io.opentelemetry.opentelemetry-instrumentation-annotations-1.16`), not yours.

### Example 3: Add business context to the current span {#current-span}

#### What you want to achieve {#current-span-goal}

You want to filter traces by a fact that your code knows, here, where the page's social image came from, without creating another span.

#### The code {#current-span-code}

In `SocialImageImpl`, add an attribute to the span that is already active:

```java
import io.opentelemetry.api.common.AttributeKey;
import io.opentelemetry.api.trace.Span;

private static final AttributeKey<String> IMAGE_SOURCE = AttributeKey.stringKey("wknd.social_image.source");

@PostConstruct
protected void init() {
    if (currentPage == null) {
        return;
    }

    final String source;
    if (resolveFromFeaturedImage()) {
        source = "featured_image";
    } else if (resolveFromFirstImageOnPage()) {
        source = "first_image_on_page";
    } else {
        source = "none";
    }

    Span.current().setAttribute(IMAGE_SOURCE, source);
}
```

* `Span.current()` returns the innermost active span, whether AEM or your code created it. For a Sling Model loaded from HTL, it is the span of the HTL script that loaded the model.
* If no span is active, the call does nothing.
* Defining `AttributeKey` constants once keeps attribute names consistent across your code.

#### The outcome {#current-span-outcome}

The span of the page's `customheaderlibs.html` script, where WKND loads this model, carries `wknd.social_image.source` with the value `featured_image`, `first_image_on_page`, or `none`. Search for traces where `wknd.social_image.source` is `none` to find the pages that are published without a social image.

On the WKND site, every page reports `first_image_on_page` or `none`: no page sets a featured image, so every page pays for the content-tree walk from [Example 2](#with-span). Setting a featured image on the most visited pages removes that work.

### Example 4: Record an error {#record-errors}

#### What you want to achieve {#record-errors-goal}

WKND's `ContentAIAvailabilityImpl` model checks whether Content AI search is configured by reading an OSGi configuration. If the lookup fails, the model treats Content AI as not configured and logs a warning. The page still renders and the request succeeds, so the failure is easy to miss. You want the failure to appear in your APM provider's error views, attached to the operation that failed.

#### The code {#record-errors-code}

```java
import io.opentelemetry.api.trace.Span;
import io.opentelemetry.api.trace.StatusCode;
import io.opentelemetry.context.Scope;

private boolean resolveConfigured() {
    if (configurationAdmin == null) {
        return false;
    }
    final Span span = WkndTelemetry.TRACER.spanBuilder("ContentAIAvailability.resolveConfigured").startSpan();
    // Close the scope in finally, not with try-with-resources: try-with-resources closes it before
    // the catch block runs, and the warning logged there must carry this span's trace and span IDs.
    final Scope scope = span.makeCurrent();
    try {
        Configuration configuration = lookupConfiguration();
        // ... read the API key, as before
        span.setAttribute("wknd.content_ai.configured", isConfigured);
        return isConfigured;
    } catch (IOException e) {
        span.recordException(e);
        span.setStatus(StatusCode.ERROR, "Content AI configuration lookup failed");
        LOGGER.warn("Unable to determine whether Content AI is configured (PID {})", CONTENT_AI_CLIENT_PID, e);
        return false;
    } finally {
        scope.close();
        span.end();
    }
}
```

* `recordException()` adds an `exception` event to the span, with the exception's type, message, and stack trace.
* `setStatus(StatusCode.ERROR, ...)` marks the span as failed. Set it on the span that represents the operation that failed. The request itself is not marked as failed, because the component recovered and the page rendered.

#### The outcome {#record-errors-outcome}

The trace contains a `ContentAIAvailability.resolveConfigured` span with the status **Error** and the description `Content AI configuration lookup failed`. The span has an `exception` event:

| Event attribute | Example value |
|---|---|
| `exception.type` | `java.io.IOException` |
| `exception.message` | `Configuration store unavailable` |
| `exception.stacktrace` | The full stack trace |

The span counts as an error in your APM provider, so it appears wherever your provider shows failed operations. The request span keeps its status, because the request returned HTTP 200.

### Example 5: Correlate logs with traces {#correlate-logs}

#### What you want to achieve {#correlate-logs-goal}

When the Content AI lookup in [Example 4](#record-errors) fails, you want to go from the warning in your logs to the trace of the request that produced it, and back.

#### The code {#correlate-logs-code}

You do not need any OpenTelemetry code. Log with SLF4J as usual, and enable logs (`logs: true`) in your [OpenTelemetry configuration](/help/implementing/developing/introduction/opentelemetry-apm-integration.md#example-configuration):

```java
LOGGER.warn("Unable to determine whether Content AI is configured (PID {})", CONTENT_AI_CLIENT_PID, e);
```

The agent adds the trace and span IDs of the current span to every log entry. Because `ContentAIAvailabilityImpl` logs while its span from [Example 4](#record-errors) is current, the warning is linked to that span.

#### The outcome {#correlate-logs-outcome}

Your APM provider receives a log entry such as the following, and can show it with its trace:

| Field | Example value |
|---|---|
| Severity | `WARN` |
| Body | `Unable to determine whether Content AI is configured (PID com.adobe.cq.wcm.core.components.internal.services.contentai.ContentAIClientImpl)` |
| Trace ID and span ID | The IDs of the `ContentAIAvailability.resolveConfigured` span |
| `exception.type`, `exception.message`, `exception.stacktrace` | The exception that was logged |
| Instrumentation scope | The logger name, `com.adobe.aem.guides.wknd.core.models.impl.contentai.ContentAIAvailabilityImpl` |

>[!NOTE]
>
>Only log entries at `WARN` level and above are sent. `INFO` and `DEBUG` entries are not. Do not rely on them for production diagnostics: record the information as a span attribute instead.

## Best practices {#best-practices}

* **Name spans after operations, not data.** Use names such as `ImageList.findPageComponentResources`, and put values that vary, such as paths and IDs, in attributes.
* **Prefix your own attribute names** with a namespace for your project, such as `wknd.`. This avoids clashes with the [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) and with names that AEM uses. Do not use the `aem.` prefix, which is reserved for AEM.
* **Do not record personal data or secrets** in span names, attributes, events, or log messages. This includes names, email addresses, IP addresses, tokens, and query strings that can contain them.
* **Add spans for operations, not iterations.** For example, [Example 2](#with-span) creates one span for the content-tree walk and records the number of resources visited as an attribute, rather than creating a span for each resource. AEM already creates many spans for a single page (about 260 for the WKND Magazine page), and every span adds to the volume that your APM provider ingests.
* **Create tracers once,** and reuse them.
* **End every span** in a `finally` block, and close every `Scope` on the thread that opened it.
* **Pass the context to threads that you start yourself,** for example with `Context.current().wrap(runnable)`, so that work done on another thread joins the same trace.
* **Expect a new trace for work outside a request.** Code that runs in a Sling job, a scheduled task, or an event listener has no request span. Spans that you create there start their own traces, one for each run.

## Test your instrumentation {#test}

* **Unit tests:** Without the agent, the API does nothing, so your existing unit tests keep passing unchanged.
* **Build:** Run `mvn clean install` locally. The AEM analyser, which Cloud Manager also runs, checks that your bundle's imports can be resolved.
* **Bundle contents:** Check that your bundle contains the complete API, as described in [Step 2](#embed-api). For example, `unzip -l core/target/<your-core-bundle>.jar | grep "io/opentelemetry/api/baggage/"` must list classes, and the bundle's `META-INF/MANIFEST.MF` must not import any `io.opentelemetry` package.
* **Your APM provider:** Deploy to a development environment that has OpenTelemetry enabled, request a page that runs your code, and search your APM provider for your span names or for the instrumentation scope that you chose in [Step 3](#create-tracer).

## Troubleshooting {#troubleshooting}

| Symptom | Cause and solution |
|---|---|
| The Cloud Manager build fails with `[api-regions-exportsimports] ... is importing package(s) [io.opentelemetry.api.incubator, io.opentelemetry.api.incubator.internal, io.opentelemetry.sdk.autoconfigure] in start level 20 but no bundle is exporting these for that start level.` | Your bundle imports optional OpenTelemetry packages. Add `!io.opentelemetry.*` at the start of `Import-Package`. See [Step 2](#embed-api). |
| Your bundle is installed but not active, with `missing requirement ... osgi.wiring.package=io.opentelemetry.api.incubator`. | Same cause and solution as the previous row. |
| `@WithSpan` spans appear, but your other spans and the attributes that you set with `Span.current()` do not. | Your bundle contains only part of the API, so the agent does not connect your copy of it. Add `-includepackage: io.opentelemetry.*`. See [Step 2](#embed-api). |
| None of your spans appear. | Check that OpenTelemetry is enabled for the environment and that a deployment has run since you deployed your code. Check that the code path ran, and that every span is ended. |
| Your spans appear as separate traces instead of inside the request. | The span was created on another thread without the request's context. Pass the context to the thread, for example with `Context.current().wrap(runnable)`. |
| Your log entries do not appear. | Only entries at `WARN` level and above are sent, and only when logs are enabled in your configuration. |

## Related articles {#related-articles}

* [OpenTelemetry](/help/implementing/developing/introduction/opentelemetry-apm-integration.md)
* [Logging](/help/implementing/developing/introduction/logging.md)
* [OpenTelemetry Java API](https://opentelemetry.io/docs/languages/java/api/) (opentelemetry.io)
* [Annotations for the OpenTelemetry Java agent](https://opentelemetry.io/docs/zero-code/java/agent/annotations/) (opentelemetry.io)
* [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) (opentelemetry.io)
* [WKND reference site](https://github.com/adobe/aem-guides-wknd) (GitHub)
