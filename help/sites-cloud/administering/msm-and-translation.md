---
title: Multi Site Manager and Translation
description: Learn how to reuse your content across your project and manage multilingual websites in AEM.
feature: Administering
role: Admin
exl-id: a3d48884-081e-44f8-8055-ee3657757bfd
solution: Experience Manager Sites
---
# Multi Site Manager and Translation {#msm-and-translation}

Adobe Experience Manager's built-in Multi Site Manager and translation tools simplifies localizing your content.

* Multi Site Manager (MSM) and its Live Copy features enable you to use the same site content in multiple locations, while allowing for variations:
  * [Reusing Content: Multi Site Manager and Live Copy](msm/overview.md)
* Translation lets you automate the translation of page content to create and maintain multilingual websites:
  * [Translating Content for Multilingual Sites](translation/overview.md)

These two features can be combined to cater for websites that are both [multinational and multilingual](#multinational-and-multilingual-sites).

>[!TIP]
>
>If you are new to translating content, see [Sites Translation Journey](/help/journey-sites/translation/overview.md). It is a guided path through translating your AEM Sites content using AEM's powerful translation tools; ideal if you have no AEM or translation experience.

## Multinational and Multilingual Sites {#multinational-and-multilingual-sites}

You can efficiently create content for multinational and multilingual sites through the combined use of the Multi Site Manager and the translation workflow.

Typically, you create a primary site in one language and for a specific country, then use that content as a basis for the other sites, using translation where required.

1. [Translate](translation/overview.md) the primary site into different languages.
1. Use [Multi Site Manager](msm/overview.md) to:
   1. Reuse content from the primary site and its translations to create sites for other countries and cultures.
   1. Where required, detach elements of the Live Copies to add localization details.

>[!TIP]
>
>Limit the use of Multi Site Manager to content within one language.
>
>For example, use the primary English to create the English version of pages for the US, Canada, and UK pages. Then, use the primary French to create the French version of pages for France, Switzerland, Canada, and so on.

The following diagram illustrates how the main concepts intersect (but does not show all levels/elements involved):

![Localization overview](assets/localization-overview.png)

In this scenario, and comparable ones, MSM does not manage the different language versions as such.

* [MSM](msm/overview.md) manages the deployment of translated content from a blueprint (that is, a primary global) to the Live Copies (that is, the local sites), within the boundaries of a language.
* The [translation](translation/overview.md) integration capabilities of AEM, with third-party translation management services, manages the languages and translating content into these different languages.

For more advanced use-cases, MSM may be used across primary languages, too.

>[!TIP]
>
>For all use-cases it is recommended to read the following best practices:
>
>* [Best Practices for MSM](msm/best-practices.md)
>* [Best Practices for Translation](translation/best-practices.md)
