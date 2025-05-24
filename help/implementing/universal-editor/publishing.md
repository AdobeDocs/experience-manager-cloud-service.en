---
title: How the Universal Editor Publishes Content
description: Learn how how the Universal Editor publishes its content, how it differs from the process in the Sites Console, and considerations when developing your own apps to work with it.
feature: Developing
role: Admin, Architect, Developer
exl-id: 60f0bb4a-ee60-4f73-83ae-8568735474ad
---
# How the Universal Editor Publishes Content {#publishing}

Learn how how the Universal Editor publishes its content, how it differs from the process in the Sites Console, and considerations when developing your own apps to work with it.

>[!TIP]
>
>This article covers details of the Universal Editor's publishing process for the developer. For the content author, [the process of publishing your content is described here.](/help/sites-cloud/authoring/universal-editor/publishing.md)

## Similarities with the Sites Console Process {#similarities}

For users of the [AEM Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md) and [Sites Console,](/help/sites-cloud/authoring/sites-console/introduction.md) the process to publish content with the Universal Editor works as you are accustomed: on publication in AEM, the content is replicated from the author service to the publish service (or to [the preview service](/help/sites-cloud/authoring/sites-console/previewing-content.md) if available and depending on the options the author chooses when publishing.)

## Differences {#differences}

What makes publishing with the Universal Editor a bit different is not so much the editor itself, but rather the external hosting of the app that the Universal Editor makes possible.

When externally hosted, it is the concern of the web app to ensure that content is loaded from the author service when the app is opened by authors within the editor, and is loaded from the publish service when the app is accessed by visitors.

## Detecting the Service in the App {#detecting}

Determining whether the author or publishing service should be accessed can be accomplished by a simple conditional statement in the app to choose the appropriate author or publish endpoint when detecting that its being opened within the editor.

Another option is to deploy the app to two different environments that are configured differently, so that one retrieves its content from the author service, and one that retrieves it from the publish service. To allow authors to open the published URL in the Universal Editor, a small script can  be created to "convert" the publish-side URL to its equivalent on the author environment (for example, by prepending an `author` sub-domain), so that the authors are automatically redirected.

## Summary {#summary}

The objective of the Universal Editor is to not impose any particular pattern, so that the implementation can best achieve its goals in a fully-decoupled manner while still keeping everything simple and straight-forward for the implementation.

Likewise the Universal Editor does not make any requirements on how any particular project should go about determining from which service to delivery the content. Rather it enables several possibilities and allows the project to determine which solution is best for its own requirements.

## Additional Resources {#additional-resources}

To learn more about the technical details of the Universal Editor, please see these developer documents.

* [Universal Editor Introduction](/help/implementing/universal-editor/introduction.md) - Learn how the Universal Editor enables editing any aspect of any content in any implementation so you can deliver exceptional experiences, increase content velocity, and provide a state-of-the-art developer experience.
* [Getting Started with the Universal Editor in AEM](/help/implementing/universal-editor/getting-started.md) - Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.
* [Universal Editor Architecture](/help/implementing/universal-editor/architecture.md) - Learn about the architecture of the Universal Editor and how data flows between its services and layers.
* [Attributes and Types](/help/implementing/universal-editor/attributes-types.md) - Learn about the data attributes and types that the Universal Editor requires.
* [Universal Editor Authentication](/help/implementing/universal-editor/authentication.md) - Learn how the Universal Editor authenticates.
