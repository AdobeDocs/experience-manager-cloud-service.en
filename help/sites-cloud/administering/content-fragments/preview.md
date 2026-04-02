---
title: Previewing Content Fragments
description: Understand how to preview your Content Fragments by a range of methods.
feature: Content Fragments
role: User, Developer
solution: Experience Manager Sites
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
exl-id: 40c02806-76a2-43ed-982c-0410c2125a36
---
# Previewing Content Fragments {#previewing-content-fragments}

Content Fragments can be used for both headless delivery and page authoring. As the fragments are solely content, without formatting, reviewing them can be more challenging. So multiple methods of previewing your fragments, in a variety of scenarios, are provided.

There are several methods available for Content Fragments, accessible from the Console Fragments console and editor. The console and editor described in this section have been developed for headless content delivery (though they can be used for all scenarios).

You can preview your fragment:

* by publishing to, and unpublishing from, the [Preview instance](#preview-instance)

* in an [external application](#preview-url-pattern), using the [Preview URL pattern](#preview-url-pattern)

* with a [visualization (HTML) Template](#preview-with-visualization-html-templates) 

Of course, you can also view your fragment in the [Content Fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md).

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

## Preview Instance {#preview-instance}

You can **Publish**, and **Unpublish**, your fragment to your **[Preview Service](/help/headless/deployment/architecture.md)** (as well as to your Publish instance).

You can publish your fragment from either the editor, or the console. 

See:

* [Publishing and Previewing a Fragment](/help/sites-cloud/administering/content-fragments/managing.md#publishing-and-previewing-a-fragment) for full details.

* [Unpublishing a fragment](/help/sites-cloud/administering/content-fragments/managing.md#unpublishing-a-fragment) for full details.

## Preview in an external Application {#preview-in-an-external-application}

The Content Fragment editor provides authors with the option to preview their edits in an external frontend application. 

### Preview URL pattern {#preview-url-pattern}

To use this feature, you first need to:

* Work with your IT team to set up the external frontend application that will render the Content Fragment by consuming its JSON output. 

* When the external frontend application is set up, the **Default Preview URL Pattern** must be defined as a [property of the appropriate Content Fragment Model](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md#model-properties).

The preview URL should follow this pattern:

&nbsp;&nbsp;&nbsp;&nbsp;`https://<preview_url>?param=${expression}`

Available expressions are:

* `${contentFragment.path}`
* `${contentFragment.model.path}`
* `${contentFragment.model.name}`
* `${contentFragment.variation}`
* `${contentFragment.id}`

When the URL has been defined, the **[Preview](/help/sites-cloud/administering/content-fragments/authoring.md#preview-content-fragment)** button is active in the top toolbar of the editor. You can select this button to launch the external application (in a separate tab) to render the Content Fragment. 

### Preview a fragment in the external Application {#preview-a-fragment-in-the-external-application}

You can preview a Content Fragment in an external application:

>[!NOTE]
>
>The [Preview URL pattern](#preview-url-pattern) must be configured for this option.

1. In the Content Fragment console navigate to the location of your fragment.
1. Open your fragment in the editor
1. Select **Preview** from the top toolbar.
1. Select **Application** to open your fragment in the external application; for example, the [Universal Editor](/help/implementing/universal-editor/introduction.md).

## Preview with Visualization (HTML) Templates {#preview-with-visualization-html-templates}

AEM allows you to preview your Content Fragment using a visual layout based on an HTML template. 

See [Visual Content Fragments](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md) for details on how to [preview your fragment with templates](/help/sites-cloud/administering/content-fragments/visual-content-fragments.md#preview-your-template-with-a-template).

>[!NOTE]
>
>See [Visual Content Fragments - Templates](/help/implementing/developing/extending/content-fragments-visualization-templates.md) for details on how to create, customize and upload your own HTML templates.

