---
title: Translating Content for Multilingual Sites
description: Get an overview of how to translate content for multilingual sites.
feature: Language Copy
role: Administrator
---

# Translating Content for Multilingual Sites {#translating-content-for-multilingual-sites}

Automate the translation of page content and assets to create and maintain multilingual websites. To automate translation workflows, you integrate translation service providers with AEM and create projects for translating content into multiple languages. AEM supports human and machine translation workflows.

* **Human translation:** Content is sent to your translation provider and translated by professional translators. When complete, the translated content is returned and imported into AEM. When your translation provider is integrated with AEM, content is automatically sent between AEM and the translation provider.
* **Machine translation:** The machine translation service immediately translates your content.

Translating content involves the following steps:

1. [Connect AEM with your translation service provider](integration-framework.md#connecting-to-a-translation-service-provider) and [create translation integration framework configurations](integration-framework.md).
1. [Associate the pages of your language master](integration-framework.md#configuring-pages-for-translation) with the translation service and framework configurations.
1. [Identify the type of content](rules.md) to translate.
1. [Prepare the content for translation](preparation.md) by authoring the language master and creating the root pages of language copies.
1. [Create translation projects](managing-projects.md) to gather the content to translate and to prepare the translation process.
1. Use the translation projects to [manage the content translation process](managing-projects.md).

If your translation service provider does not provide a connector to integration with AEM, AEM supports the manual extraction and re-insertion of translation content in XML format.

>[!NOTE]
>
>Your user needs to be a member of the `project-administrators` group to use the Language Copy features.

## Best Practices {#best-practices}

The [Translation Best Practices](best-practices.md) page contains important information regarding your implementation.
