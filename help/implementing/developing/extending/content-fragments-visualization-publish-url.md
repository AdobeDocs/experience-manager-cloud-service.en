---
title: Visual Content Fragments - using the Publish URL
description: Use the publish URL for visual Content Fragments.
feature: Developing, Content Fragments
role: Admin, Developer
---
# Visual Content Fragments - Using the Publish URL {#visual-content-fragments-using-the-publish-url}

When a Content Fragment is published through the CF Visualization service, the rendered HTML is stored in Azure Blob Storage and made available via the AEM publish tier at a URL with this structure:

```html
https://publish-p<programId>-e<envId>.adobeaemcloud.com/adobe/experimental/previewtemplates-expires-20260301/contentFragments/<templateId>/<fragmentId>/<variation>.html
```

This URL returns a *self-contained HTML document* (including inline CSS and structure) that can be embedded in any web context. 

## Embedding Techniques — Overview {#embedding-techniques-overview}

There are three distinct approaches for consuming the publish URL on a host page. Each comes with distinct trade-offs around style isolation, layout behavior, accessibility, and complexity.

| | Inline Element | iframe | Custom Element + Shadow DOM |
|--- |--- |--- |--- |
| Mechanism | `fetch()` the URL, inject the response HTML into a `<div>` via `innerHTML` | `<iframe src="publishURL">` | Define a Custom Element, `fetch()` the HTML, inject into an attached Shadow DOM root |
| Style isolation | None — fragment CSS leaks into host page and host CSS affects the fragment | Full — separate browsing context, complete CSS isolation | Strong — Shadow DOM boundary blocks host CSS cascade; fragment styles stay encapsulated |
| Layout participation | Full — content is part of the normal document flow, responds to flexbox/grid/container sizing | None — iframe has fixed dimensions; requires explicit `width`/`height` or JS-based auto-resize | Full — custom element participates in the host document’s normal flow like any other DOM element |
| Accessibility (a11y) | Best — content is in the main DOM tree, fully traversable by screen readers and assistive technology | Moderate — separate browsing context can confuse screen reader navigation; requires `title` attribute | Good — content is within the same document; shadow DOM is traversable by modern assistive technologies |
| SEO | Poor — content loaded via JS `fetch()` is not indexed by most crawlers | Poor — iframe content is typically not indexed in the parent page context | Poor — same as inline; JS-fetched content is not crawlable |
| JavaScript runtime | Shared — same window/document context; risk of script collisions if the fragment contains `<script>` tags | Isolated — separate window context; no risk of collision | Shared — same window context but DOM-scoped; scripts inside shadow root execute in the host context |
| Cross-origin support | Requires CORS headers on the publish URL (the service configures these) | Works natively — iframes load cross-origin content without CORS | Requires CORS headers on the publish URL (same as inline) |
| Implementation complexity | Minimal — a few lines of JS | Trivial — zero JS required; pure HTML | Low — ~20 lines of JS for the Custom Element definition, reusable across the page |
| Best suited for | Prototyping, trusted same-origin content, contexts where layout integration is critical and CSS conflicts are manageable | Quick embedding, sandboxed content, cross-origin scenarios where CORS is unavailable, content that must be fully isolated | Production use — balances isolation, layout participation, and accessibility (recommended for AEM Core Components and external sites) |

### Inline Element (fetch + innerHTML) {#inline-element-fetch-and-innerhtml}

The simplest approach: 

1. fetch the publish URL 
1. inject the HTML into a container element

```html
<div id="cf-container"></div>
<script>
  fetch("<publish-url>")
    .then(r => r.ok ? r.text() : Promise.reject(r.status))
    .then(html => {
      document.getElementById("cf-container").innerHTML = html;
    })
    .catch(err => console.error("Failed to load fragment", err));
</script>
```

When to use:

* Rapid prototyping or proof-of-concept pages
* Same-origin contexts where you control both the host page and fragment styles
* When maximum layout flexibility is more important than style encapsulation

>[!CAUTION]
>
>**CSS collision risk** 
>
>The fragment’s inline styles (including its `<style>` blocks, font-face declarations, and element selectors) will merge into the host page’s cascade. 
>
>This can cause unintended style overrides in both directions. 
>
>Use this technique only when you can tolerate or actively manage these conflicts.

### Iframe {#iframe}

Load the publish URL directly as the `src` of an `<iframe>`. No JavaScript is needed.

```iframe
<iframe
  src="<publish-url>"
  title="Content Fragment Preview"
  width="100%"
  height="600"
  frameborder="0"
  style="border: none;"
></iframe>
```

Auto-resizing (optional) 

To dynamically size the iframe to its content height (avoiding scrollbars), use a `postMessage` pattern or an appropriate library. 

An example of a lightweight approach is:

```iframe
<iframe id="cf-iframe" src="<publish-url>" title="Content Fragment Preview"
  width="100%" frameborder="0" style="border:none; overflow:hidden;"
  onload="this.style.height = this.contentDocument.documentElement.scrollHeight + 'px';"
></iframe>
```

>[!WARNING]
>
>The `onload` auto-resize approach above only works for **same-origin** iframes.
>
>For **cross-origin** publish URLs, you would need a `postMessage`-based solution or to set a fixed height.

When to use:

* Edge Delivery Services embed block (the default integration — see section below)
* Contexts where full CSS/JS isolation is critical
* Cross-origin embedding where CORS is not configured
* Quick, zero-code integration (just paste the URL)

### Custom Element + Shadow DOM (Recommended) {#custom-element-and-shadow-dom-recommended}

Define a reusable `<cf-visualization>` Custom Element that fetches the publish URL and injects the HTML into an encapsulated Shadow DOM root.

This provides:

* Shadow DOM isolation
  *The fragment’s markup and styles are encapsulated in a shadow root, preventing collisions with the host page’s CSS cascade.
* Inline layout participation
  * The rendered content participates in the host document’s normal flow, responding to container sizing and flexbox/grid contexts without manual dimension management.
* Single browsing context
  * No secondary document context is created; the fragment content shares the page’s JavaScript runtime and is fully traversable by assistive technologies.
* Minimal overhead
  *A single `fetch` call retrieves the pre-rendered HTML from the publish tier. No client-side rendering framework is required.

>[!IMPORTANT]
>
>This is the recommended approach for production use and is the technique used by AEM Core Components.

To define the Custom Element include the following script once per page. All `<cf-visualization>` instances on the page will use this definition:

```javascript

<script>
  class CfVisualization extends HTMLElement {
    connectedCallback() {
      const src = this.getAttribute("src");
      if (!src) return;

      const shadow = this.attachShadow({ mode: "open" });

      fetch(src)
        .then((r) => (r.ok ? r.text() : Promise.reject(r.status)))
        .then((html) => {
          shadow.innerHTML = html;
        })
        .catch((err) => {
          console.error("cf-visualization: failed to load", src, err);
        });
    }
  }

  if (!customElements.get("cf-visualization")) {
    customElements.define("cf-visualization", CfVisualization);
  }
</script>

```

To use the Custom Element:

```html
<cf-visualization src="<publish-url>"></cf-visualization>
```

When to use:

* AEM Sites pages using Core Components (this is the built-in behavior)
* External/third-party websites that need a clean, reusable integration
* Any context where you need both style isolation and layout-flow participation

## Integration with Edge Delivery Services (Embed Block) {#integration-with-edge-services-embed-block}

In Edge Delivery Services, the publish URL is consumed through the **Embed block**, which renders it as an `<iframe>`.

1. Ensure the Embed block exists in your project.

   If your EDS project does not already include the Embed block, copy it from the aem-block-collection repository:

   ```cmdline
   # From the aem-block-collection repo, copy blocks/embed/ into your project's blocks/ directory
   cp -r aem-block-collection/blocks/embed/ your-eds-project/blocks/embed/
   ```

1. Author the embed in the DA editor

   In Document Authoring, blocks are represented as tables. To add a CF visualization embed:

   | embed |
   |--- |
   | (paste the publish URL as a hyperlink) |

   Alternatively, if your project or Sidekick is configured with the Embed block in its block library, you can insert it via the slash menu and paste the publish URL into the block content.

1. Result

   The Embed block renders the publish URL inside an `<iframe>`. The fragment content loads in full CSS isolation within the EDS page layout.

## Integration - AEM Sites with Core Components {#integration-aem-sites-with-core-components}

The Content Fragment Core Component (`core/wcm/components/contentfragment/v1/contentfragment`) has built-in support for Visual Content Fragments rendering using the [Customer Element + Shadow DOM](#custom-element-and-shadow-dom-recommended) technique.

How it works:

* Author mode:

  When the component’s `displayMode` is set to `vcf`, the authoring clientlib (`vcfRenderer.js`) fetches the fragment HTML from the preview API and renders it inline in the authoring canvas.

  An example of an Author Preview Endpoint is:

  ```html
  GET /adobe/sites/cf/fragments/{fragmentId}/preview?templateId={templateId}&variation={variation}
  ```

* Publish mode:

  On the published page (`wcmmode.disabled`), the HTL template renders an inline script that fetches from the publish URL and injects the HTML into a Shadow DOM root.

  An example Core Component Visual Content Fragment (templates.html):

  ```html
  <div class="cmp-contentfragment cmp-contentfragment--vcf"
     data-cmp-contentfragment-id="{fragmentId}"
     data-cmp-contentfragment-vcf-template="{templateId}"
     data-cmp-contentfragment-variation="{variation}">
    <!-- Only rendered when wcmmode.disabled (publish) -->
    <div data-vcf-url="{vcfPublishUrl}" class="cmp-contentfragment__vcf-loader" style="display:none"></div>
    <script>
        (function() {
            var script = document.currentScript;
            var loader = script.previousElementSibling;
            var el = script.parentElement;
            if (!el || !loader) return;
            var url = loader.dataset.vcfUrl;
            if (!url) return;
            loader.remove();
            var shadow = el.attachShadow({ mode: "open" });
            var body = document.createElement("body");
            body.style.display = "none";
            shadow.appendChild(body);
            fetch(url)
                .then(function(r) { return r.ok ? r.text() : Promise.reject(r.status); })
                .then(function(html) {
                    body.innerHTML = html;
                    body.style.display = "";
                });
        })();
    </script>
  </div>
  ```

  Publish URL Format:

  The Sling Model (`ContentFragmentImpl`) builds the publish URL using the following pattern:

  ```html
  /adobe/experimental/previewtemplates-expires-20260301/contentFragments/{templateId}/{fragmentId}/{variation}.html
  ```

  This relative URL is resolved against the publish host at runtime.

## Integration with External Sites {#integration-with-external-sites}

For non-AEM websites use the [Customer Element + Shadow DOM](#custom-element-and-shadow-dom-recommended) technique. This gives you a clean, declarative integration without framework dependencies.

An example is:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Product Page</title>
</head>
<body>
  <h1>Product Details</h1>
  <p>Some host-page content here...</p>

  <!-- Embed the Content Fragment visualization -->
  <cf-visualization
    src="https://publish-p12345-e67890.adobeaemcloud.com/adobe/experimental/previewtemplates-expires-20260301/contentFragments/product_template/abc-123/master.html"
  ></cf-visualization>

  <p>More host-page content below the fragment...</p>

  <!-- Custom Element definition (include once) -->
  <script>
    class CfVisualization extends HTMLElement {
      connectedCallback() {
        const src = this.getAttribute("src");
        if (!src) return;
        const shadow = this.attachShadow({ mode: "open" });
        fetch(src)
          .then(r => r.ok ? r.text() : Promise.reject(r.status))
          .then(html => { shadow.innerHTML = html; })
          .catch(err => console.error("cf-visualization: failed to load", src, err));
      }
    }
    if (!customElements.get("cf-visualization")) {
      customElements.define("cf-visualization", CfVisualization);
    }
  </script>
</body>
</html>
```

>[!NOTE]
>
>You can place multiple `<cf-visualization>` elements on the same page with different `src` URLs. The Custom Element definition only needs to be included once.

## CORS and Security Considerations {#cors-and-security-considerations}

| Concern | Details | 
|--- |--- |
| CORS | The CF Visualization service configures CORS on the `/adobe/**` path with configurable allowed origins.<br>The [Inline Element (fetch + innerHTML)](#inline-element-fetch-and-innerhtml) 1 and [Customer Element + Shadow DOM](#custom-element-and-shadow-dom-recommended) techniques (which use `fetch()`) require the host page’s origin to be in the allowed list. <br>The [iFrame](#iframe) technique does not require CORS. | 
| CSP / X-Frame-Options | The service does not set `Content-Security-Policy` or `X-Frame-Options` headers on the published HTML. If your CDN or dispatcher adds these headers, verify that they permit framing (for [iFrame](#iframe)) or `fetch()` access (for inline/shadow DOM) from your host origins. | 
| Content trust | The published HTML is pre-rendered from authored Content Fragment data using [Handlebars templates](/help/implementing/developing/extending/content-fragments-visualization-templates.md) managed by the service. It does not include user-generated scripts. However, as with any innerHTML injection, ensure you trust the source origin. | 

### Choosing the appropriate technique {#choosing-the-appropriate-technique}

Decision guide:

* Need zero JavaScript and full isolation? 
  * Iframe
* Need layout-flow participation with style isolation? 
  * Custom Element + Shadow DOM (recommended)
* Need fastest prototype, same-origin, and CSS conflicts are acceptable? 
  * Inline Element
* Embedding in Edge Delivery Services? 
  * Embed block (iframe under the hood)
* Embedding in AEM Sites pages? 
  * Core Component (Shadow DOM, built-in)