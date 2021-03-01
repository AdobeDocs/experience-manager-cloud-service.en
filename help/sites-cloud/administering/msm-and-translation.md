---
title: Multi Site Manager and Translation
description: Learn how to reuse your content across your project and manage multilingual websites in AEM.
---

# Multi Site Manager and Translation {#msm-and-translation}

Adobe Experience Manager's built-in Multi Site Manager and translation tools simplifies localizing your content.

* Multi Site Manager (MSM) and its Live Copy features enable you to use the same site content in multiple locations, while allowing for variations:
  * [Reusing Content: Multi Site Manager and Live Copy](msm/overview.md)
* Translation allows you to automate the translation of page content to create and maintain multilingual websites:
  * [Translating Content for Multilingual Sites](translation/overview.md)

These two features can be combined to cater for websites that are both [multinational and multilingual](#multinational-and-multilingual-sites).

## Multinational and Multilingual Sites {#multinational-and-multilingual-sites}

You can efficiently create content for multinational and multilingual sites through the combined use of the Multi Site Manager and the translation workflow.

Typically you would create a master site in one language and for a specific country, then use that content as a basis for the other sites, using translation where required.

1. [Translate](translation/overview.md) the master site into different languages.
1. Use [Multi Site Manager](msm/overview.md) to:
   1. Re-use content from the master site and its translations to create sites for other countries and cultures.
   1. Where required, detach elements of the Live Copies to add localization details.

>[!TIP]
>
>Limit the use of Multi Site Manager to content within one language.
>
>E.g. use the English master to create the English version of pages for the US, Canada, UK, etc. pages and use the French master to create the French version of pages for France, Switzerland, Canada, etc.

The following diagram illustrates how the main concepts intersect (but does not show all levels/elements involved):

![Localization overview](assets/localization-overview.png)

In this, and comparable, scenarios MSM does not manage the different language versions as such.

* [MSM](msm/overview.md) manages the deployment of translated content from a blueprint (i.e. a global master) to the Live Copies (i.e. the local sites), within the boundaries of a language.
* The [translation](translation/overview.md) integration capabilities of AEM, in conjunction with third-party translation management services, manages the languages and translating content into these different languages.

For more advanced use-cases, MSM may be used across language masters as well.

>[!TIP]
>
>For all use-cases it is recommended to read the following best practices:
>
>* [Best Practices for MSM](msm/best-practices.md)
>* [Best Practices for Translation](translation/best-practices.md)
