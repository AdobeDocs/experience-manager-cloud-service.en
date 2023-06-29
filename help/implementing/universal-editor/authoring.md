---
title: Authoring Content with the Universal Editor
description: Learn how easy and intuitive it is for content authors to create content using the Universal Editor.
exl-id: 15fbf5bc-2e30-4ae7-9e7f-5891442228dd
---
# Authoring Content with the Universal Editor {#authoring}

Learn how easy and intuitive it is for content authors to create content using the Universal Editor.

## Introduction {#introduction}

The Universal Editor enables editing any aspect of any content in any implementation so you can deliver exceptional experiences, increase content velocity, and provide a state-of-the-art developer experience.

To do this, it provides content authors with an intuitive UI that requires minimal training to be able to simply jump in and begin editing content.

>[!TIP]
>
>For a more detailed introduction to the Universal Editor, see the document [Universal Editor Introduction.](introduction.md)

>[!NOTE]
>
>The Universal Editor is still in development and can currently not edit all content types.

## Prepare the App {#prepare-app}

To author content for an app using the Universal Editor, the app must be instrumented by a developer to support the editor.

>[!TIP]
>
>See [Getting Started with the Universal Editor in AEM](getting-started.md) for an example of how to configure an AEM app to work with the Universal Editor.

## Sign In {#sign-in}

Once the app is instrumented to work with the Universal Editor, you will need to sign into the Universal Editor. You will need an Adobe ID to sign in and [have access to the Universal Editor.](getting-started.md#request-access)

After you are signed in, enter the URL of the page you want to edit in the [address bar.](#address-bar) so you can start [editing the content.](#edit-content)

## Understand The UI {#ui}

The UI is divided into four main areas.

* [The Experience Cloud header](#experience-cloud-header)
* [The Universal Editor header](#universal-editor-header)
* [The rail](#rail)
* [The editor](#editor)

![The Universal Editor UI](assets/ui.png)

### The Experience Cloud Header {#experience-cloud-header}

The Experience Cloud header is always present at the top of the screen. It is an anchor that tells you where you are within Experience Cloud and helps you navigate to other Experience Cloud apps.

![The Experience Cloud header](assets/experience-cloud-header.png)

#### Experience Manager {#experience-manager}

Select the Adobe Experience Cloud link at the left of the header to navigate to the root of your Experience Manager solution to access tools such as [Cloud Manager,](/help/onboarding/cloud-manager-introduction.md) [Cloud Acceleration Manager,](/help/journey-migration/cloud-acceleration-manager/introduction/overview-cam.md) and [Software Distribution.](https://experienceleague.adobe.com/docs/experience-cloud/software-distribution/home.html)

![Global Navigation button](assets/global-navigation.png)

#### Organization {#organization}

This displays the organization you are currently signed into. Tap or click to switch to another organization if your Adobe ID is associated with multiple.

![Organization indicator](assets/organization.png)

#### Solutions {#solutions}

Tapping or clicking the solutions switcher allows you to quickly jump to other Experience Cloud solutions.

![Solutions switcher](assets/solutions.png)

#### Help {#help}

The help icon provides quick access to learning and support resources.

![Help](assets/help.png)

#### Notifications {#notifications}

This icon is badged with the number of currently assigned incomplete [notifications](/help/implementing/cloud-manager/notifications.md).

![Notifications](assets/notifications.png)

#### User Properties {#user-properties}

Tap or click the icon representing your user to access your user settings. If you do not have a user picture configured, an icon is randomly assigned.

![User properties](assets/user-properties.png)

### The Universal Editor Header {#universal-editor-header}

The Universal Editor header is always present at the top of the screen just below [the Experience Cloud header.](#experience-cloud-header) It gives you quick access to navigate to another page to edit and to publish the current page.

![The Universal Editor header](assets/universal-editor-header.png)

#### The Hamburger Menu {#hamburger-menu}

The hamburger menu is not yet implemented.

![Hambuger menu](assets/hamburger-menu.png)

#### Location Bar {#Location-bar}

The location bar shows you the address of the page you are editing. Tap or click to enter the address of another page to edit.

![Location bar](assets/address-bar.png)

>[!TIP]
>
>Use the hot key `L` to open the address bar.

>[!NOTE]
>
>Any page that you wish to edit with the Universal Editor must be [instrumented to support he Universal Editor.](getting-started.md)

#### Open App Preview {#open-app-preview}

Tap or click the open app preview icon to open the page you are currently editing in its own browser, free of the editor to preview the changes.

![Open app preview](assets/open-app-preview.png)

>[!TIP]
>
>Use the hot key `O` to open the app preview.

#### Publish {#publish}

Tap or click the publish button so you can publish the changes to the content live for consumption by your readers.

![Publish button](assets/publish.png)

>[!TIP]
>
>See the document [Publishing Content with the Universal Visual Editor](publishing.md) for more information on publishing with the Universal Editor.

### The Rail {#rail}

The rail is always present along the left side of the editor. It allows for easy switching the editor between preview mode and edit mode.

![The rail](assets/rail.png)

#### Preview Mode {#preview-mode}

In preview mode, the page rendered in the editor as it would be seen on your published service. This allows the content author to navigate the content by clicking links, etc.

![Preview mode](assets/preview-mode.png)

>[!TIP]
>
>Use the hot key `P` to switch to preview mode.

#### Edit Mode {#edit-mode}

In edit mode, the page is rendered in the editor, but the content author can click to select content to edit it. This is the default mode of the editor when a page is loaded.

![Edit mode](assets/edit-mode.png)

### The Editor {#editor}

The editor occupies most of the window and is where the page specified in [the address bar](#address-bar) is rendered.

Depending on if the editor is in [edit mode](#edit-mode) or [preview mode,](#edit-mode) the content will either be editable or navigable, respectively.

![Editor](assets/editor.png)

## Editing Content {#editing-content}

Editing content is simple and intuitive. In [edit mode,](#edit-mode) as you mouse over content in the editor, editable content is highlighted with a blue box.

![Editable content is highlighted by a blue box](assets/editable-content.png)

Simply tap or click on the content in the blue box to start an in-place editor to make your changes. Press enter or return to save the changes.

![Editing content](assets/editing-content.png)

Note that in edit mode, tapping or clicking on content attempts to select it for editing. If you wish to navigate your content by following links, switch to [preview mode.](#preview-mode)

## Previewing Content {#previewing-content}

When you are finished editing content, you often want to navigate it to see how it looks in the content of other pages. In [preview mode](#preview-mode) you can click links to navigate your content as a reader would. The content is rendered in the editor as it would be published.

Note that in preview mode, tapping or clicking on content reacts as it would to a reader of the content. If you wish to select the content for editing, switch to [edit mode.](#edit-mode)

## Additional Resources {#additional-resources}

To learn more about the Universal Editor, see these documents.

* [Universal Editor Introduction](introduction.md) - Learn how the Universal Editor enables editing any aspect of any content in any implementation so you can deliver exceptional experiences, increase content velocity, and provide a state-of-the-art developer experience.
* [Publishing Content with the Universal Editor](publishing.md) - Learn how the Universal Visual Editor publishes content and how your apps can handle the published content.
* [Getting Started with the Universal Editor in AEM](getting-started.md) - Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.
* [Universal Editor Architecture](architecture.md) - Learn about the architecture of the Universal Editor and how data flows between its services and layers.
* [Attributes and Types](attributes-types.md) - Learn about the data attributes and types that the Universal Editor requires.
* [Universal Editor Authentication](authentication.md) - Learn how the Universal Editor authenticates.
