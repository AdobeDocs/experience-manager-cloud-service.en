---
title: Configure translation rules
description: Learn how to define translation rules to identify content for localization.
---
# Configure Translation Rules {#translation-rules}

Learn how to define translation rules to identify content for localization.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless localization journey, [Configure translation connector](configure-connector.md) you learned how to install and configure your translation connector and should now:

* Understand the important parameters of the Translation Integration Framework in AEM.
* Be able to set up your own connection to your translation service.

Now that your connector is set up, this article takes you through the next step of identifying what content you need to translate.

## Objective {#objective}

This document helps you understand how to use AEM's translation rules to identify your translation content. After reading this document you should:

* Understand what the translation rules do.
* Be able to define your own translation rules.

## Translation Rules {#translation-rules}

Translation rules identify the content that is included in, or excluded from, translation projects. When content is translated, AEM extracts the content based on these rules so that it can be sent to the translation service via the connector you already set up.

Translation rules include the following information:

* The path of the content to which the rule applies
  * The rule also applies to the descendants of the content
* The names of the properties that contain the content to translate
  * The property can be specific to a specific resource type or to all resource types

## Creating Translation Rules {#creating-rules}

Multiple rules can be created to support complex translation requirements. For example one project you may be working on requires all fields of the content to be translated, but on another only description fields must be translated while titles are left untranslated.

Translation rules are designed to handle such scenarios. However in this example we will illustrate how to create rules by focusing on a simple, single configuration.

There is a **Translation Configuration** console available for configuring translation rules. To access it:

1. Navigate to **Tools** -&gt; **General**.
1. Tap or click **Translation Configuration**.

The **Translation Configuration** UI, there are a number of options available for your translation rules. Here we will highlight the most necessary and typical steps needed for a basic headless localization configuration.

1. Tap or click **Add Context**, which allows you to add a path. This is the path of the content that will be affected by the rule.
![Add context](assets/add-translation-context.png)
1. Use the path browser to select the required path and tap or click the **Confirm** button to save. Remember, Content Fragments, which hold headless content, are generally located under `/content/dam/<your-project>`.
![Select the path](assets/select-context.png)
1. AEM saves the configuration.
1. You need to select the context you just created and then tap or click **Edit**. This will open the **Translation Rules Editor** to configure the properties.
![Translation rules editor](assets/translation-rules-editor.png)
1. By default all configurations are inherited from the parent path, in this case `/content/dam`. Uncheck the option **Inherit from `/content/dam`** in order to add additional fields to the configuration.
1. Once unchecked, under the **General** section of the list, add the property names that you [previously identified as fields for translation.](getting-started.md#content-models)
   1. Enter the property name in the **New Property** field.
   1. The options **Translate** and **Inherit** are checked automatically.
   1. Tap or click **Add**.
   1. Repeat these steps for all of the fields that you need to translate.
   1. Tap or click **Save**.
![Add property](assets/add-property.png)

You have now configured your translation rules.

## Advanced Usage {#advanced-usage}

There are a number of additional properties that can be configured as part of your translation rules. In addition, you can specify your rules by hand as XML, which allows for more specificity and flexibility.

Such features are generally note needed to get started localizing your headless content, but you can read about them further in the [Additional Resources](#additional-resources) section if you are interested.

## What's Next {#what-is-next}

Now that you have completed this part of the headless localization journey you should:

* Understand what the translation rules do.
* Be able to define your own translation rules.

Build on this knowledge and continue your AEM headless localization journey by next reviewing the document [Translate content](translate-content.md) where you will learn how your connector and rules work together to translate headless content.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the headless localization journey by reviewing the document [Translate content,](translate-content.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the headless journey.

* [Identifying Content to Translate](/help/sites-cloud/administering/translation/rules.md) - Learn how translation rules identify content that needs translating.
