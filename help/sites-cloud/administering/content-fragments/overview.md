---
title: An Overview of working with Content Fragments
description: Learn how Content Fragments in Adobe Experience Manager (AEM) as a Cloud Service allow you to create and use structured content; ideal for headless delivery, and page authoring.
feature: Content Fragments
role: User, Developer, Architect
exl-id: ce9cb811-57d2-4a57-a360-f56e07df1b1a
solution: Experience Manager Sites
---
# An overview of working with Content Fragments {#overview-working-with-content-fragments}

>[!IMPORTANT]
>
>Various features of the Content Fragments and Content Fragment Models are available through the Early Adopter Program.
>
>To see the status, and how to apply if you are interested, check the [Release Notes](/help/release-notes/release-notes-cloud/release-notes-current.md).

With Adobe Experience Manager (AEM) as a Cloud Service, Content Fragments allow you to design, create, curate, and publish page-independent content. They allow you to prepare content ready for use in multiple locations, and over multiple channels, ideal for [headless delivery](/help/headless/what-is-headless.md), and [page authoring](/help/sites-cloud/authoring/fragments/content-fragments.md).

>[!IMPORTANT]
>
>Content Fragments can be accessed from two consoles: **Content Fragments** and **Assets**.
>
>There are also two editors for authoring Content Fragments; although the basic functionality is the same, there are some differences. Both editors are accessible from both consoles.
>
>This section deals with the **Content Fragments** console and the *new* Content Fragment editor. These have been developed for headless content delivery (though they can be used for all scenarios)
>
>For further information see:
>
>* use of the **Assets** console for [managing Content Fragments](/help/assets/content-fragments/content-fragments-managing.md)
>* use of the [*original* Content Fragment editor](/help/assets/content-fragments/content-fragments-variations.md),
>* using [Content Fragments for page-authoring](/help/sites-cloud/authoring/fragments/content-fragments.md).


Content fragments contain structured content:

* Each fragment is based on a [Content Fragment Model](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md).
  * The [Content Fragment Model defines the structure](/help/sites-cloud/administering/content-fragments/content-fragment-models.md) of the resulting fragment.
* Every fragment consists of:
  * **[Main](#main-and-variations)** - an integral part of the fragment that holds the core content; always exists, cannot be deleted
  * **[Variations](#main-and-variations)** - one, or more, permutations of the content, created by the author
* The structure can range between:
  * Basic
    * For example, a single, multi line text field.
    * Can be used for preparing straightforward content for use in page authoring.
    * Can also be used for headless delivery to your application.
  * Complex
    * A combination of many fields of varying data types, including text, number, boolean, and date and time, among others.
    * Can be used either for preparing more structured content for page authoring, or for headless delivery to your application.
  * Nested
    * The reference data types available allow you to nest your content.
    * Tends to be used for headless delivery to your application.

Content Fragments can also be delivered in JSON format, using the Sling Model (JSON) export capabilities of AEM core components. This form of delivery:

* enables you to use the component to manage which elements of a fragment to deliver
* allows bulk-delivery; by adding multiple [Content Fragment Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/wcm-components/content-fragment-component.html) on the page being used for API delivery

The number of communication channels is increasing annually. Typically channels refer to the delivery mechanism, either as the:

* Physical channel; for example, desktop, mobile.
* Form of delivery in a physical channel; for example, the "product detail page", "product category page" for desktop, or "mobile web", "mobile app" for mobile.

However, you (probably) do not want to use the *exact* same content for all channels - you need to optimize your content according to the specific channel.

Content fragments allow you to:

* Consider how to reach target audiences efficiently across channels.
* Create and manage channel-neutral editorial content.
* Build content pools for a range of channels.
* Design content variations for specific channels.
* Add images to your text by inserting assets.
* Create nested content to reflect the complexity of your data.

These Content Fragments can then be assembled to provide experiences over a variety of channels.

>[!NOTE]
>
>**Content Fragments** and **[Experience Fragments](/help/sites-cloud/authoring/fragments/content-fragments.md)** are different features within AEM:
>* **Content Fragments** are editorial content, with definition and structure, but without additional visual design and/or layout. They can be used to access structured data, including texts, numbers, and dates, among others. 
>* **Experience Fragments** are fully laid out content; a fragment of a web page.
>
>Experience Fragments can contain content in the form of Content Fragments, but not the other way around.
>
>For further information, see [Understanding Content Fragments and Experience Fragments in AEM](https://experienceleague.adobe.com/docs/experience-manager-learn/sites/content-fragments/understand-content-fragments-and-experience-fragments.html#content-fragments).

This and the following pages cover the tasks for creating, configuring, maintaining, and using your Content Fragments:

* [Enable Content Fragment functionality for your instance](/help/sites-cloud/administering/content-fragments/setup.md)
* [Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md) - enabling, creating, and [defining](/help/sites-cloud/administering/content-fragments/content-fragment-models.md) your models
* [Create your Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md#creating-a-content-fragment) (using the Content Fragment Console)

After the fragments have been created, you can:

* [Use the Content Fragments console](/help/sites-cloud/administering/content-fragments/managing.md) - to:
  * access, publish (to preview or production), and reference your fragments
* [Use the Content Fragments editor](/help/sites-cloud/administering/content-fragments/authoring.md) - to:
  * edit, publish (to preview or production), and reference your fragments
  * collaborate with other authors using Comments
* [Analyze](/help/sites-cloud/administering/content-fragments/analysis.md)  the structure of your Content Fragment, using the editor
* [Access your fragments with GraphQL, for headless delivery to your applications](/help/sites-cloud/administering/content-fragments/content-delivery-with-graphql.md). 
* [Or use your fragments for page authoring](/help/sites-cloud/authoring/fragments/content-fragments.md)

>[!NOTE]
>
>These pages can be read together with:
>
>* [Customizing and Extending Content Fragments](/help/implementing/developing/extending/content-fragments-customizing.md)
>* [Content Fragments Configuring Components for Rendering](/help/implementing/developing/extending/content-fragments-configuring-components-rendering.md)
>* [Content Fragments Support in AEM Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md)
>* [AEM GraphQL API for use with Content Fragments](/help/headless/graphql-api/content-fragments.md)
>* [Page Authoring with Content Fragments](/help/sites-cloud/authoring/fragments/content-fragments.md).
>* The [Content Fragment and Content Fragment Model OpenAPIs](/help/headless/content-fragment-openapis.md) are also available.


## Main and Variations {#main-and-variations}

Variations are a significant feature of AEM's Content Fragments. They allow you to create and edit copies of the **Main** content for use on specific channels, and scenarios, making headless content delivery and page authoring even more flexible.

* **Main**

  * **Main** is not a variation as such, but is the basis of all variations.
  * An integral part of the fragment

    * Every Content Fragment has one instance of **Main**.
    * **Main** cannot be deleted.

  * **Main** is accessible in the fragment editor under **[Variations](/help/sites-cloud/administering/content-fragments/authoring.md#variations)**.

  >[!NOTE]
  >
  >In the editor available from the **Assets** console, **Main** is labeled as **Master**.

* **Variations**

  * Renditions of fragment text that are specific to editorial purpose; can be related to channel but is not compulsory, can also be for ad-hoc local modifications.
  * Are created as copies of **Main**, but can then be edited as required; there is often content overlap between the variations themselves.
  * Can be defined during fragment authoring; from the left panel.
  * Stored in the fragment, to help avoid scattering of content copies.
  * Variations can be [compared and synchronized](/help/sites-cloud/administering/content-fragments/authoring.md#compare-and-synchronize-rich-text) with **Main**.
  <!--
  * Can be [Summarized](/help/sites-cloud/administering/content-fragments/authoring.md#summarizing-text) to quickly truncate the text to a predefined length.
  -->

## Content Fragments and Content Services {#content-fragments-and-content-services}

AEM Content Services are designed to generalize the description and delivery of content in/from AEM beyond a focus on web pages.

They provide the delivery of content to channels that are not traditional AEM web pages, using standardized methods that can be consumed by any client. These channels can include:

* Single Page Applications
* Native Mobile Applications
* other channels and touch-points external to AEM

Delivery is made in JSON format using the JSON Exporter.

AEM Content Fragments can be used to describe and manage structured content. Structured content is defined in models that can contain a variety of content types; including text, numerical data, boolean, date and time, and more.

Together with the JSON export capabilities of AEM core components, this structured content can then be used to deliver AEM content to channels other than AEM pages.

>[!NOTE]
>
>See [Headless and AEM](/help/headless/introduction.md) for an introduction to Headless Development for AEM Sites as a Cloud Service.

>[!NOTE]
>
>AEM also supports the translation of fragment content. See [Translating Assets](/help/assets/translate-assets.md) for further information.

## Content Type {#content-type}

Content fragments are:

* A **Sites** feature.

* Stored as **Assets**:

  * Content fragments (and their variations) can be created and maintained from the [Content Fragments console](#content-fragments-console).
  * Authored and edited in the [Content Fragment Editor](/help/sites-cloud/administering/content-fragments/authoring.md).

* Accessible for content delivery using the [AEM GraphQL API](/help/headless/graphql-api/content-fragments.md).

* Available in the [page editor by using the Content Fragment component](/help/sites-cloud/authoring/fragments/content-fragments.md) (referencing component):

  * The [Content Fragment Core Component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/wcm-components/content-fragment-component.html) is available to page authors. It allows them to reference, and deliver, the required Content Fragment in either HTML or JSON format.

Content Fragments are a content structure that:

* Are without layout or design (text formatting is possible for text fields).
* Are independent from the delivery mechanism (such as the page, or channel).
* Contain one, or more, [constituent parts](#constituent-parts-of-a-content-fragment).
* Can [contain, or be connected to, images](#fragments-with-visual-assets).

### Fragments with Visual Assets {#fragments-with-visual-assets}

To give authors more control of their content, images can be added to and/or integrated with a Content Fragment.

Assets can be used with a Content Fragment in several ways; each with its own advantages:

* as a **Content Reference**
* within a **Multi line text** field

### Constituent Parts of a Content Fragment {#constituent-parts-of-a-content-fragment}

The Content Fragment assets are made up of the following parts (either directly or indirectly):

* **Fragment Elements**

  * Elements correlate to the data fields holding content.
  * You use a [Content Fragment Model](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md) to create the Content fragment. The elements (fields) [specified in the model define the structure of the fragment](/help/sites-cloud/administering/content-fragments/content-fragment-models.md). These elements (fields) can be of a variety of data-types.

* **Fragment Paragraphs**

  * Blocks of text, often multi line, that are delimited as individual entities.

  * Enable content control during page authoring.

* **Fragment Metadata**

  * Use the [Assets metadata schemas](/help/assets/metadata-schemas.md).
  * Tags can be created when you:

    * Create and author the fragment
    * Or later, when you [view or edit the properties](/help/sites-cloud/administering/content-fragments/authoring.md#view-properties-tags) when in the fragment editor

  >[!CAUTION]
  >
  >Metadata processing profiles do not apply to Content Fragments.

  >[!CAUTION]
  >
  >A Content Fragment Model can often define data fields named **Title** and **Description**. If these two fields exist, they are user-defined fields and can be updated in the content area of the editor.
  >
  >The Content Fragment, and its variations, also has metadata (property) fields called **Title** and **Description**. These two metadata fields are an integral part of any Content Fragment, and variation, and initially defined when the fragment is created. They can be updated in the properties/metadata area of the editor.

* **[Main](#main-and-variations)**
* **[Variations](#main-and-variations)**

### Required by Fragments {#required-by-fragments}

To create Content Fragments you need:

* **Content Model**

  * Are [enabled using the Configuration Browser](/help/sites-cloud/administering/content-fragments/setup.md).
  * Are [created using the Content Fragment Console](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#creating-a-content-fragment-model).
  * Required to [create a fragment](/help/sites-cloud/administering/content-fragments/managing.md#creating-content-fragments).
  * Defines the structure of a fragment (title, content elements, tag definitions).
  * Content Fragment Model definitions require a title and one data element; everything else is optional. 
  * The model can define default content - if applicable. 
  * Authors cannot change the defined structure when authoring fragment content; though they can open the model editor from the fragment editor.
  * Changes made to a model after dependent Content Fragments have been created, can impact those Content Fragments.

To use your Content Fragments for headless content delivery you also need:

* a [GraphQL query](/help/headless/graphql-api/content-fragments.md) to request the required content
* this content can then be used for developing your own SPAs for AEM; for more information, review the following documents:

  * [SPA WKND Tutorial](/help/implementing/developing/hybrid/wknd-tutorial.md)
  * [Getting Started Using React](/help/implementing/developing/hybrid/getting-started-react.md)
  * [Getting Started Using Angular](/help/implementing/developing/hybrid/getting-started-angular.md)

To use your Content Fragments for page authoring you also need:

* A **Content Fragment Component**

  * Instrumental to delivering the fragment in HTML and/or JSON format.
  * Required to [reference the fragment on a page](/help/sites-cloud/authoring/fragments/content-fragments.md).
  * Responsible for layout and delivery of a fragment; for example, channels.
  * Fragments need one or more dedicated components to define layout and deliver some or all elements/variations and associated content.
  * Dragging a fragment onto a page in authoring automatically associates the required component.
  * See the [Content Fragment Core Component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/wcm-components/content-fragment-component.html).

## The Content Fragments Console {#content-fragments-console}

The Content Fragments console is dedicated to managing, searching for, and creating [Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md), [Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md) and [Assets](/help/sites-cloud/administering/content-fragments/assets-content-fragments-console.md). It has been optimized for use in a Headless context, but is also used when creating Content Fragments and Content Fragment Models for use in page authoring.

The console can be directly accessed from the top level of the Global Navigation.

![Global Navigation - Content Fragments console](assets/cf-managing-global-navigation.png)

You can use the far left panel to select the resource type to view, browse and manage:

![Content Fragments console - navigation](/help/sites-cloud/administering/content-fragments/assets/cf-console-assets-navigation.png)

For detailed information see:

* [Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md)
* [Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md)
* [Assets](/help/sites-cloud/administering/content-fragments/assets-content-fragments-console.md)

* A selection of [keyboard shortcuts](/help/sites-cloud/administering/content-fragments/keyboard-shortcuts.md) are available for use in this console

>[!CAUTION]
>
>This console is *only* available in the online Adobe Experience Manager (AEM) as a Cloud Service.

>[!NOTE]
>
>Your project team can customize the console and editor if necessary. See [Customizing the Content Fragment Console and Editor](/help/implementing/developing/extending/content-fragments-console-and-editor.md) for further details.

## Example Usage {#example-usage}

A fragment, with its elements and variations, can be used to create coherent content for multiple channels. When designing your fragment you need to consider what will be used, and where.

### WKND Sample {#wknd-sample}

The [WKND Site and WKND Shared](/help/implementing/developing/introduction/develop-wknd-tutorial.md) samples are provided to help you learn about AEM as a Cloud Service. 

<!-- CHECK: which links can/should be used these days? -->

The WKND project includes:

* Content Fragment Models available under:

  * `.../libs/dam/cfm/models/console/content/models.html/conf/wknd`

  * `.../ui#/aem/libs/dam/cfm/models/console/content/models.html/conf/wknd-shared`

* Content Fragments (and other content) available under:

  * `.../assets.html/content/dam/wknd/en`
