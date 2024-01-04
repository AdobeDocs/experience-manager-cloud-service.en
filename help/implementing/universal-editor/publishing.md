---
title: Publishing Content with the Universal Editor
description: Learn how the Universal Editor publishes content and how your apps can handle the published content.
exl-id: aee34469-37c2-4571-806b-06c439a7524a
---

# Publishing Content with the Universal Editor {#publishing}

Learn how the Universal Editor publishes content and how your apps can handle the published content.

{{universal-editor-status}}

## Similarities with AEM {#similarities}

For users of AEM, the process to publish content with the Universal Editor works as you are accustomed: on publication in AEM, the content is replicated from the author tier to the publish tier.

## Differences {#differences}

What makes publishing with the Universal Editor a bit different is not so much the editor itself, but rather the external hosting of the app that the Universal Editor makes possible.

When externally hosted, it is the concern of the web app to ensure that content is loaded from the author tier when the app is opened by authors within the editor, and is loaded from the publish tier when the app is accessed by visitors.

## Detecting the Tier in the App {#detecting}

Determining whether the author or publishing tier should be access can be accomplished by a simple conditional statement in the app to choose the appropriate author or publish endpoint when detecting that its being opened within the editor.

Another option is to deploy the app to two different environments that are configured differently, so that one retrieves its content from the author tier, and one that retrieves it from the publish tier. To allow authors to open the published URL in the Universal Editor, a small script can  be created to "convert" the publish-side URL to its equivalent on the author environment (for example, by prepending an `author` sub-domain), so that the authors are automatically redirected.

## Summary {#summary}

The objective of the Universal Editor is to not impose any particular pattern, so that the implementation can best achieve its goals in a fully-decoupled manner while still keeping everything simple and straight-forward for the implementation.

Likewise the Universal Editor does not make any requirements on how any particular project should go about determining from which tier to delivery the content. Rather it enables several possibilities and allows the project to determine which solution is best for its own requirements.
