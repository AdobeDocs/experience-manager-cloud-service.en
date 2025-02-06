---
title: Internationalizing Components
description: Internationalize your components and dialogs so that their UI strings can be presented in different languages
topic-tags: components
solution: Experience Manager, Experience Manager Sites
feature: Developing
role: Developer
exl-id: 0276b310-b9a9-44b6-b295-06c51ef17208
---
# Internationalizing Components{#internationalizing-components}

Internationalize your components and dialogs so that their UI strings can be presented in different languages. Components that are designed for internationalization enable UI strings to be externalized, translated, then imported to the repository. At runtime, the user's language preferences or the page locale determines which language is displayed in the UI.

![i18n-components-1.png](/help/implementing/developing/extending/assets/i18n-comp1.png)

Use the following process to internationalize your components and provide the UI in different languages:

1. [Implement your components using code that internationalizes strings](/help/implementing/developing/extending/i18n/dev.md). Your code identifies the strings to translate, and selects the language to present at runtime.
1. Create dictionaries and add the English strings to translate.
1. Export the dictionary to XLIFF format, translate the strings, then import the XLIFF files back into AEM.
1. Incorporate the dictionary into the release management process of your application.

>[!NOTE]
>
>The methods described here for internationalizing components is meant for translating static strings. When component strings are expected to change you should use conventional translation workflows. For example, when authors can edit a UI string using properties in the Edit dialog of a component, you should not use a language dictionary to internationalize the string.

## Language Dictionaries {#language-dictionaries}

The AEM internationalization framework uses dictionaries in the repository to store English strings and their translations in other languages. The framework uses English as the default language. Strings are identified using their English version. Typically, internationalization frameworks use alphanumeric IDs for UI strings. Using the English version of the string as the ID has several advantages:

* Code is easy to read.
* The default language is always available.

Translation changes need to come from Git via the [CI/CD pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) in AEM as a cloud service.

![i18n-components-2](/help/implementing/developing/extending/assets/i18n-comp2.png)


### Overlaying Strings in System Dictionaries {#overlaying-strings-in-system-dictionaries}

If your components use strings that are included in the AEM system dictionaries, duplicate the string in your own dictionary. All components will use the strings from your dictionary.

Note that you cannot predict which translation is used when strings are duplicated in dictionaries that are all located below the `/apps` node.
