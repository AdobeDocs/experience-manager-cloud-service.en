---
title: SPA and Server-Side Rendering
description: Using server-side rendering (SSR) in your SPA can accelerate the initial load of the page and then pass further rendering on to the client.
exl-id: be409559-c7ce-4bc2-87cf-77132d7c2da1
feature: Developing
role: Admin, Architect, Developer
---
# SPA and Server-Side Rendering{#spa-and-server-side-rendering}

Single page applications (SPAs) can offer the user a rich, dynamic experience that reacts and behaves in familiar ways, often just like a native application. [This functionality is achieved by relying on the client to load the content up front and then do the heavy lifting of handling user interaction](introduction.md#how-does-a-spa-work). This process minimizes the amount of communication that is needed between the client and the server, making the app more reactive.

However, this process can lead to longer initial load times, especially if the SPA is large and rich in its content. To optimize load times, some of the content can be rendered server-side. Using server-side rendering (SSR) can accelerate the initial load of the page and then pass further rendering on to the client.

## When to Use SSR {#when-to-use-ssr}

SSR is not required on all projects. Although AEM fully supports JS SSR for SPA, Adobe does not recommend implementing it systematically for every project.

When deciding to implement SSR, you must first estimate what additional complexity, effort, and cost adding SSR realistically represents for the project, including the long-term maintenance. An SSR architecture should be chosen only when the added value clearly exceeds the estimated costs.

SSR usually provides some value when there is a clear "yes" to either of the following questions:

* **SEO:** Is SSR still required for your site to be properly indexed by the search engines that bring traffic? Keep in mind that the main search engine crawlers now evaluate JS.
* **Page Speed:** Does SSR provide a measurable speed improvement in real-life environments and add to the overall user experience?

Only when at least one of these two questions is answered with a clear "yes" for your project does Adobe recommend implementing SSR. The following sections describe how to do this using Adobe I/O Runtime, part of [App Builder](https://developer.adobe.com/app-builder).

## Adobe I/O Runtime {#adobe-i-o-runtime}

If you [are confident that your project requires the implementation of SSR](#when-to-use-ssr), Adobe's recommended solution is to use Adobe I/O Runtime.

For more information on Adobe I/O Runtime, see the following:

* [https://developer.adobe.com/runtime](https://developer.adobe.com/runtime) - for an overview of the Runtime feature of App Builder
* [https://developer.adobe.com/app-builder](https://developer.adobe.com/app-builder) - for details on the full App Builder product
* [https://developer.adobe.com/runtime/docs/](https://developer.adobe.com/runtime/docs) - for detailed documentation

The following sections detail how Adobe I/O Runtime can be used to implement SSR for your SPA in two different models:

* [AEM-Driven Communication Flow](#aem-driven-communication-flow)
* [Adobe I/O Runtime-Driven Communication Flow](#adobe-i-o-runtime-driven-communication-flow)

>[!NOTE]
>
>Adobe recommends a separate Adobe I/O Runtime workspace per environment (stage, prod, testing, and so on). Do so allows for typical systems development life cycle (SDLC) patterns with different versions of a single application deployed to different environments. See [CI/CD for App Builder Applications](https://developer.adobe.com/app-builder/docs/guides/deployment/ci_cd_for_firefly_apps/) for more information.
>
>A separate workspace is not needed per instance (author, publish) unless there are differences in the runtime implementation per instance type.

>[!NOTE]
>
>Cloud Manager does not support deployment to Adobe I/O Runtime. As a result, your own infrastructure must be set up to deploy SSR code to the Adobe I/O Runtime.

## Remote Renderer Configuration {#remote-content-renderer-configuration}

AEM must know where the remotely rendered content can be retrieved. Regardless of [which model you choose to implement for SSR,](#adobe-i-o-runtime) you must specify to AEM how to access this remote rendering service.

This service is done by way of the **RemoteContentRenderer - Configuration Factory OSGi service**. Search for the string "RemoteContentRenderer" in the Web Console Configuration console at `http://<host>:<port>/system/console/configMgr`.

![Renderer Configuration](assets/renderer-configuration.png)

The following fields are available for the configuration:

* **Content path pattern** - Regular expression to match a portion of the content, if necessary
* **Remote endpoint URL** - URL of the endpoint that is responsible for generating the content
  * Use the secured HTTPS protocol if not in local network.
* **Additional request headers** - Additional headers to be added to the request sent to the remote endpoint
  * Pattern: `key=value`
* **Request timeout** - Remote host request timeout in milliseconds

>[!NOTE]
>
>Regardless of if you choose to implement the [AEM-driven communication flow](#aem-driven-communication-flow) or the [Adobe I/O Runtime-driven flow,](#adobe-i-o-runtime-driven-communication-flow) you must define a remote content renderer configuration.

>[!NOTE]
>
>This configuration uses the [Remote Content Renderer,](#remote-content-renderer) which has additional extension and customization options available.

## AEM-Driven Communication Flow {#aem-driven-communication-flow}

When using SSR, the [component interaction workflow](introduction.md#interaction-with-the-spa-editor) of SPAs in AEM includes a phase in which the initial content of the app is generated on Adobe I/O Runtime.

1. The browser requests the SSR content from AEM.
1. AEM posts the model to Adobe I/O Runtime.
1. Adobe I/O Runtime returns the generated content.
1. AEM serves the HTML returned by Adobe I/O Runtime via the HTL template of the backend page component.

![SSE CMS-driven AEM Adobe I/O](assets/ssr-cms-drivenaemnode-adobeio.png)

## Adobe I/O Runtime-Driven Communication Flow {#adobe-i-o-runtime-driven-communication-flow}

The previous section describes the standard and recommended implementation of server-side rendering regarding SPAs in AEM, where AEM performs the bootstrapping and serving of content.

Alternatively, SSR can be implemented so that Adobe I/O Runtime is responsible for the bootstrapping, effectively reversing the communication flow.

Both models are valid and supported by AEM. However, one should consider the advantages and disadvantages of each before implementing a particular model.

<table>
 <tbody>
  <tr>
   <th><strong>Bootstrapping</strong></th>
   <th><strong>Advantages</strong></th>
   <th><strong>Disadvantages</strong></th>
  </tr>
  <tr>
   <th><strong>via AEM</strong><br /> </th>
   <td>
    <ul>
     <li>AEM manages injecting libraries where needed</li>
     <li>Maintain resources on AEM only<br /> </li>
    </ul> </td>
   <td>
    <ul>
     <li>Possibly unfamiliar to SPA developer<br /> </li>
    </ul> </td>
  </tr>
  <tr>
   <th><strong>via Adobe I/O Runtime<br /> </strong></th>
   <td>
    <ul>
     <li>More familiar to SPA developers<br /> </li>
    </ul> </td>
   <td>
    <ul>
     <li>Clientlib resources required by the application, such as CSS and JavaScript, must be made available by the AEM developer by way of the <code><a href="/help/implementing/developing/introduction/clientlibs.md">allowProxy</a></code> property<br /> </li>
     <li>Resources must be synched between AEM and Adobe I/O Runtime<br /> </li>
     <li>To enable authoring of the SPA, a proxy server for Adobe I/O Runtime may be necessary</li>
    </ul> </td>
  </tr>
 </tbody>
</table>

## Planning for SSR {#planning-for-ssr}

Generally, only part of an application must be rendered server-side. The common example is the content that is displayed above the fold on the initial load of the page is rendered server side. This process saves time by delivering to the client, already rendered content. As the user interacts with the SPA, the additional content is rendered by the client.

As you consider implementing server-side rendering for your SPA, review for what parts of the app it is necessary.

## Developing an SPA using SSR {#developing-an-spa-using-ssr}

SPA components could be rendered by the client (in the browser) or server side. When rendered server side, browser properties such as window size and location are not present. Therefore SPA components should be isomorphic, making no assumption about where they are rendered.

To use SSR, you must deploy your code in AEM and on Adobe I/O Runtime, which is responsible for the server-side rendering. Most of the code is the same, however server-specific tasks differ.

## SSR for SPAs in AEM {#ssr-for-spas-in-aem}

SSR for SPAs in AEM requires Adobe I/O Runtime, which is called for the rendering of the app content server side. Within the HTL of the app, a resource on Adobe I/O Runtime is called to render the content.

Just as AEM supports the Angular and React SPA frameworks out-of-the box, server-side rendering is also supported for Angular and React apps. See the NPM documentation for both frameworks for further details.

## Remote Content Renderer {#remote-content-renderer}

The [Remote Content Renderer Configuration](#remote-content-renderer-configuration) that is required to use SSR with your SPA in AEM taps into a more generalized rendering service that can be extended and customized to meet your needs.

### RemoteContentRenderingService {#remotecontentrenderingservice}

`RemoteContentRenderingService` An OSGi service to retrieve content rendered on a remote server, such as from Adobe I/O. The content sent to the remote server is based on the request parameter passed.

`RemoteContentRenderingService` Can be injected by dependency inversion into either a custom Sling model or servlet when additional content manipulation is required.

This service is internally used by the [RemoteContentRendererRequestHandlerServlet](#remotecontentrendererrequesthandlerservlet).

### RemoteContentRendererRequestHandlerServlet {#remotecontentrendererrequesthandlerservlet}

The `RemoteContentRendererRequestHandlerServlet` is used to programmatically set the request configuration. `DefaultRemoteContentRendererRequestHandlerImpl`, the provided default request handler implementation, lets you create multiple OSGi configurations so you can map a location in the content structure to a remote endpoint.

To add a custom request Handler, implement the `RemoteContentRendererRequestHandler` interface. Be sure to set the `Constants.SERVICE_RANKING` component property to an integer higher than 100, which is the ranking of the `DefaultRemoteContentRendererRequestHandlerImpl`.

```javascript
@Component(immediate = true,
        service = RemoteContentRendererRequestHandler.class,
        property={
            Constants.SERVICE_RANKING +":Integer=1000"
        })
public class CustomRemoteContentRendererRequestHandlerImpl implements RemoteContentRendererRequestHandler {}
```

### Configure the OSGi Configuration of the Default Handler {#configure-default-handler}

The configuration of the default handler must be configured as described in the section [Remote Content Renderer Configuration](#remote-content-renderer-configuration).

### Remote Content Renderer Usage {#usage}

Have a servlet fetch and return some content that is injected into the page:

1. Ensure that your remote server is accessible.
1. Add one of the following snippets to the HTL template of an AEM component.
1. Optionally, create or modify the OSGi configurations.
1. Browse the content of your site

Usually, the HTL template of a page component is the main recipient of such a feature.

```html
<sly data-sly-resource="${resource @ resourceType='cq/remote/content/renderer/request/handler'}" />
```

### Requirements {#requirements}

The servlets use the Sling Model Exporter to serialize the component data. By default, both the `com.adobe.cq.export.json.ContainerExporter` and `com.adobe.cq.export.json.ComponentExporter` are supported as Sling Model adapters. If necessary, you can add classes that the request should be adapted to using the `RemoteContentRendererServlet` and implementing the `RemoteContentRendererRequestHandler#getSlingModelAdapterClasses`. The additional classes must extend the `ComponentExporter`.
