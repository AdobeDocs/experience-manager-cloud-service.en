---
title: Publish translated content
description: Learn how to publish your localized content.
---
# Publish Translated Content {#publish-content}

Learn how to publish your localized content.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless localization journey, [Translate content,](configure-connector.md) you learned how to use AEM Translation Projects to translate your headless content. You should now:

* Understand what a translation project is.
* Be able to create new translation projects.
* Use translation projects to translate your headless content.

Now that your initial translation is complete, this article takes you through the next step of publishing that content and what to do to update your translations as the underlying language root content changes.

## Objective {#objective}

This document helps you understand how to publish headless content in AEM and how to create a continual workflow to keep your translations up-to-date. After reading this document, you should:

* Understand the author-publish model of AEM.
* Know how to publish your translated content.
* Be able to implement a continual update model for your translated content.

## AEM's Author-Publish Model {#author-publish}

Before you publish your content, it is a good idea to understand AEM's author-publish model. In its simplest terms, AEM divides users of the system into two groups.

1. Those who create and manage the content and the system
1. Those who consume the content from the system.

AEM is therefore physically separated into two instances.

1. The **author** instance is the system where content authors and administrators work to create and manage content.
1. The **publish** instance is the system that delivers the content to the consumers.

Once content is created on the author instance, it must be transferred to the publish instance for it to be available for consumption. The process of transferring from author to publish is called **publication**.

## Publishing Your Translated Content {#publishing}

Once you are happy with the state of your translated content, you can publish it so headless services can consume it. The easiest way to do this is to navigate to the project assets folder.

```text
/content/dam/<your-project>/
```

Under this path you have sub-folders for each translation language and can choose which to publish.

1. Go to **Navigation** -&gt; **Assets** -&gt; **Files** and open the project folder.
1. Here you will see the language root folder and all other language folders. Select the localized language or languages that you wish to publish.
![Select language folder](assets/select-language-folder.png)
1. Tap or click **Manage Publication**.
1. In the **Manage Publication** window, make sure that **Publish** is automatically selected under **Action** and that **Now** is selected under **Scheduling**. Tap or click **Next**.
![Manage publication options](assets/manage-publication-options.png)
1. In the next **Manage Publication** window, confirm that the proper path(s) is/are selected. Tap or click **Publish**.
![Manage publication scope](assets/manage-publication-scope.png)
1. AEM confirms the publish action with a pop-up message at the bottom of the screen.
![Resources published banner](assets/resources-published-message.png)

Your localized headless content is now published! It can now be accessed and consumed by your headless services.

>[!TIP]
>
>You can select multiple items (i.e. multiple language folders) when publishing in order to publish multiple localization at one time.

There are additional options when publishing your content such as scheduling a publication time which are beyond the scope of this journey. Please see the [Additional Resources](#additional-resources) section at the end of the document for more information.

## Updating Your Translated Content {#updating-translations}

Localization and translation is rarely a one-off exercise. Typically your content authors continue to add to and modify your content in the language root after initial localization is complete. This means that you will need to also update your translated content.

Specific project requirements will define how often you will need to update your translations and what decision process will be followed before performing an update. Once you have decided to update your translations, the process in AEM is very simple. As the initial translation was based on a translation project, so too are any updates.

1. Navigate to **Navigation** -&gt; **Assets** -&gt; **Files**. Remember that headless content in AEM is stored as assets known as Content Fragments.
1. Select the language root of your project. In this case we have selected `/content/dam/wknd/en`.
1. Tap or click the rail selector and show the **References** panel.
1. Tap or click on **Language Copies**.
1. Check the **Language Copies** checkbox.
1. Expand the section **Update Language Copies** at the bottom of the references panel.
1. In the **Project** dropdown, select **Add to an existing Translation Project**.
1. In the **Existing Translation Project** dropdown, select the project created for the initial translation.
1. Tap or click **Start**.

![Add items to existing translation project](assets/add-to-existing-project.png)

The content is added to the existing translation project. To view the translation project:

1. Navigate to **Navigation** -&amp; **Projects**.
1. Tap or click the project that you just updated.
1. Tap or click the language or one of the languages that you updated.

You will see that a new job card was added to the project. In this example, another Spanish translation was added.

![Additional translation job added](assets/additional-translation-job.png)

You will notice that the statistics listed on the new card (number of assets and content fragments) is different. This is because AEM recognizes what has changed since the last translation and only includes new content that needs to be translated (both re-translated updated content or first-time translation of new content).

From this point, you [start and manage your translation job just as you did the original.](translate-content.md#using-translation-project)

## End of the Journey? {#end-of-journey}

Congratulations! You have completed the headless localization journey! You should now:

* Have an overview of what headless content delivery is.
* Have a basic Understanding AEM's headless features.
* Understand AEM's localization features and how they related to headless content.
* Have the ability to start localizing your own headless content.

You are now ready to localize your own headless content in AEM. However AEM is a powerful tool and there are many additional options available. Check out some of the additional resources available in the next section to learn more about the features you saw in this journey.

## Additional Resources {#additional-resources}

* [Managing Translation Projects](/help/sites-cloud/administering/translation/managing-projects.md) - Learn the details of translation projects and additional features such as human translation workflows and multi-language projects.
* [Authoring concepts](/help/sites-cloud/authoring/getting-started/concepts.md) - Learn about the author and publish model of AEM in more detail. This document is focused on authoring pages rather than Content Fragments, but the theory still applies.
* [Publishing Pages](/help/sites-cloud/authoring/fundamentals/publishing-pages.md) - Learn about the additional features available when publishing content. This document is focused on authoring pages rather than Content Fragments, but the theory still applies.
