---
title: Get started with AEM headless localization
description: Get to know how to organize your headless content and how AEM's localization tools work.
---
# Get Started with AEM Headless Localization {#getting-started}

Get to know how to organize your headless content and how AEM's localization tools work.

## Objective {#objective}

This document helps you understand how to get started localizing headless content in AEM. After reading you should:

* Understand the importance of content structure to localization.
* Be familiar with AEM's localization tools.

## Requirements and Prerequisites {#requirements-prerequisites}

There are a number of requirements before you begin localizing your headless AEM content.

### Knowledge {#knowledge}

* Experience localizing content for a CMS
* Experience using the basic features of a large-scale CMS
* Understanding of the translation service you are using

>[!TIP]
>
>If you are not familiar with using a large-scale CMS like AEM, consider reviewing the [Basic Handling](/help/sites-cloud/authoring/getting-started/basic-handling.md) documentation before proceeding. The Basic Handling documentation is not part of the journey, so please return to this page when complete.

### Tools {#tools}

* Sandbox access for testing translating your content
* Credentials to connect to your preferred translation service

## Structure is Key {#content-structure}

AEM's content, be it headless or traditional web pages, is driven by its structure. AEM imposes few requirements on the content structure, but careful consideration of your content hierarchy as part of the project planning can make localization much simpler.

>[!TIP]
>
>Plan for translation and localization at the very beginning of the headless project. Work closely with the project manager and content architects early.
>
>An “Internationalization Project Manager” my be required as a separate persona whose responsibility it is to define what content should be translated and what not, and what translated content may be modified by regional or local content producers.

Create a plan on what content localization you will need.

* Do you just need different languages or also language to adopt to regional specifics?
* Do you need rich media content like images or videos to be different for different locales?

## How AEM Stores Headless Content {#headless-content-in-aem}

For the localization specialist, it is not important to understand in-depth how AEM manages headless content. However being familiar with the basic concepts and terminology will be very helpful as you later use AEM's localization tools.

### Content Models {#content-models}

In order for headless content to be delivered consistently across channels, regions, and languages, content must be highly structured. AEM uses Content Models to enforce this structure. Think of Content Models as a kind of template or pattern for creating headless content.

The content architect works early in the project to define this structure. As previously recommended, as the localization specialist, you should work closely with the content architect to organize the content.

### Content Fragments {#content-fragments}

Content Models are used by the content authors to create the actual headless content. Content authors select which model to base their content on an then create Content Fragments. Content Fragments are instances of the models and represent actual content to be delivered headlessly.

If the Content Models are the patterns for the content, the Content Fragments are the actual content based on those patterns.

Content Fragments are managed as assets in AEM as part of digital asset management (DAM). This is important since they will all be located under the path `/content/dam`.

## Recommended Content Structure {#recommended-structure}

As previously recommended, work with your content architect to determine the appropriate content structure for your own project. However the following is a proven, simple, and intuitive structure which has proven effective.

Define a base folder for your project under `/content/dam`.

```text
/content/dam/<your-project>
```

Your master language (e.g. English) should be below this path.

```text
/content/dam/<your-project>/en
```

All project content that may need to be localized should the be placed under the master language.

```text
/content/dam/<your-project>/en/<your-project-content>
```

Localizations should be created as sibling folders alongside the master language. For example, German would have the following path.

```text
/content/dam/<your-project>/de
```

The final structure may look something like the following.

```text
/content
    |- dam
        |- your-project
            |- en
                |- some
                |- exciting
                |- headless
                |- content
            |- de
            |- fr
            |- it
            |- ...
        |- another-project
        |- ...
```

## AEM Localization Tools {#localization-tools}

The localization tools in AEM are quite powerful, but are simple to understand at a high level.

* **Translation Connector** - The connector is the link between AEM and the translation service that you use.
* **Translation Rules** - Rules define what content should be translated.
* **Translation Projects** - Translation Projects gather together content that should be addressed as a single translation effort and tracks the progress of the translation, interfacing with the connector to transmit the content to be translated and receive it back from the translation service.

## What's Next {#what-is-next}

Now that you have completed this part of the headless localization journey you should:

* Understand the importance of content structure to localization.
* Be familiar with AEM's localization tools.

Build on this knowledge and continue your AEM headless localization journey by next reviewing the document [Configure the translation connector](configure-connector.md) where you will learn how to connect AEM to a translation service.|

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the headless localization journey by reviewing the document [Configure the translation connector](configure-connector.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the headless journey.

* [Identifying Content to Translate](/help/sites-cloud/administering/translation/rules.md) - Learn how translation rules identify content that needs translating.
* [Configuring the Translation Integration Framework](/help/sites-cloud/administering/translation/integration-framework.md) - Learn how to configure the Translation Integration Framework to integrate with third-party translation services.
* [Managing Translation Projects](/help/sites-cloud/administering/translation/managing-projects.md) - Learn how to create and manage both machine and human translation projects in AEM.
