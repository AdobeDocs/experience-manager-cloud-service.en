---
title: Configure translation connector
description: Learn how to connect AEM to a translation service.
---
# Configure translation connector {#configure-connector}

Learn how to connect AEM to a translation service.

## The Story So Far {#story-so-far}

In the previous document of the AEM headless localization journey, [Get started with AEM headless localization](learn-about.md) you learned how to organize your headless content and how AEM's localization tools work and you should now:

* Understand the importance of content structure to localization.
* Be familiar with AEM's localization tools.

This article builds on those fundamentals so you can take the first configuration step and set up a translation service, which you will use later in the journey to translate your content.

## Objective {#objective}

This document helps you understand how to set up an AEM connector to your chosen translation service. After reading you should:

* Understand the important parameters of the Translation Integration Framework in AEM.
* Be able to set up your own connection to your translation service.

## The Translation Integration Framework {#tif}

AEM's Translation Integration Framework integrates with third-party translation services to orchestrate the translation of AEM content. It involves three basic steps.

1. Connect to your translation service provider.
1. Create a Translation Integration Framework configuration.
1. Associate the cloud configurations with your pages.

## Connecting to a Translation Service Provider {#connect-translation-provider}

The first step is to choose which translation service you wish to use. There are many choices for human and machine translation services available to AEM. See the [Additional Resources](#additional-resources) section for a selection of options available.

Most providers will offer a translator package to be installed. For the purposes of this journey, we will use the Microsoft Translator which AEM provides with a trial license out-of-the-box. See the [Additional Resources](#additional-resources) section for more information about this provider.

## Creating a Translation Integration Configuration {#create-config}

Create a translation integration framework configuration to specify how to translate your content. The configuration includes the following information:

* Which translation service provider to use
* Whether human or machine translation is to be performed
* Whether to translate other content that is associated with the Content Fragment such as tags

To create a new translation configuration:

1. In the global navigation menu, click or tap **Tools** -&gt; **Cloud Services** -&gt; **Translation Cloud Services**.
1. Navigate to where you wish to create the configuration in your content structure. This is often based on a particular project or can be global.
   * For example, in this case, a configuration could be made globally to apply to all content, or just for the WKND project.

   ![Translation configuration location](assets/translation-configuration-location.png)

1. Provide the following information in the fields and then click or tap **Create**.
   1. Select **Configuration Type** in the drop-down. Select **Translation Integration** from the list.
   1. Enter a **Title** for your configuration. The **Title** identifies the configuration in the **Cloud Services** console as well as in page property drop-down lists.
   1. Optionally, type a **Name** to use for the repository node that stores the configuration.

   ![Create translation configuration](assets/create-translation-configuration.png)

1. Tap or click **Create** and the **Edit Configuration** window appears where you can configure the configuration properties.

1. Remember that Content Fragments are stored as assets in AEM. Tap or click the **Assets** tab.

![Translation configuration properties](assets/translation-configuration.png)

1. Provide the following information.

   1. **Translation Method** - Select **Machine Translation** or **Human Translation** depending on your translation provider. For the purposes of this journey we will assume machine translation.
   1. **Translation Providers** - Select the connector you installed for your translation service from the list.
   1. **Content Category** - Select the most appropriate category to better target the translation (only for machine translation).
   1. **Translate Content Fragment Assets** - ???
   1. **Translate Assets** - Check this to translate the assets.
   1. **Translate Metadata** - Check this to translate asset metadata.
   1. **Translate Tags** - Check this to translate tags that are associated with the asset.
   1. **Auto-Execute Translation** - Check this property if you want translations to be automatically sent to your translation service.

1. Tap or click **Save &amp; Close**.

You have now configured the connector to your translation service.

## What's Next {#what-is-next}

Now that you have completed this part of the headless localization journey you should:

* Understand the important parameters of the Translation Integration Framework in AEM.
* Be able to set up your own connection to your translation service.

Build on this knowledge and continue your AEM headless localization journey by next reviewing the document [Configure the translation connector,](configure-connector.md) where you will learn how to connect AEM to a translation service.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the headless localization journey by reviewing the document [Configure translation rules](translation-rules.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the headless journey.

* [Configuring the Translation Integration Framework](/help/sites-cloud/administering/translation/integration-framework.md) - Learn how to configure the Translation Integration Framework to integrate with third-party translation services.
* [Connecting to Microsoft Translator](/help/sites-cloud/administering/translation/connect-ms-translator.md) - AEM provides a trial Microsoft Translation account for testing purposes.
