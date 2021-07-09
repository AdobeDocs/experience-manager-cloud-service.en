---
title: Translate content
description: Use the translation connector and rules to translate your headless content.
---
# Translate Content {#translate-content}

Use the translation connector and rules to translate your headless content.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless localization journey, [Configure Translation Rules](translation-rules.md) you learned how how to use AEM's translation rules to identify your translation content. After reading this document you should:

* Understand what the translation rules do.
* Be able to define your own translation rules.

Now that your connector and translations rules are set up, this article takes you through the next step of translating your headless content.

## Objective {#objective}

This document helps you understand how to use AEM's translation projects along with the connector and your translations rules to translate content. After reading this document you should:

* Understand what a translation project is.
* Be able to create new translation projects.
* Use translation projects to translate your headless content.

## Creating a Translation Project {#creating-translation-project}

Translation projects enable you to manage the translation of headless AEM content. A translation project contains the content to be translated into other languages.

When content is added to a translation project, a translation job is created for it. Jobs provide commands and status information that you use to manage the human translation and machine translation workflows that execute on the resources.

To create a translation project:

1. Navigate to **Navigation** -&gt; **Assets** -&gt; **Files**. Remember that headless content in AEM is stored as assets known as Content Fragments.
1. Select the English (or language master) of your project. In this case we have selected `/content/dam/wknd/en`.
1. Tap or click the rail selector and show the **References** panel.
1. Tap or click on **Language Copies**.
1. Check the **Language Copies** checkbox.
1. Expand the section **Update Language Copies** at the bottom of the references panel.
1. In the **Project** dropdown, select **Create Translation Project(s)**.
1. Provide an appropriate title for your translation project.
1. Tap or click **Start**.

![Create a translation project](assets/create-translation-project.png)

You receive a message that the project was created.

>[!NOTE]
>
>It is assumed that the necessary, empty folders for the translations languages have already been created as part of the [definition of your content structure.](getting-started.md#content-structure) This should be done in collaboration with the content architect.

## Using a Translation Project {#using-translation-project}

