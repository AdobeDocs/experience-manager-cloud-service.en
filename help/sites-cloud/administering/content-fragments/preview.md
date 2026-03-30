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

* using the [Preview URL pattern](#preview-url-pattern)

* by publishing to, and unpublishing from, the [Preview instance](#preview-instance)

<!--
* with a HTML template, using **[Preview]()** from the Content Fragments console
-->

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

## Preview URL pattern {#preview-url-pattern}

The Content Fragment editor provides authors with the option to preview their edits in an external frontend application. 

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

## Preview Instance {#preview-instance}

You can **Publish**, and **Unpublish**, your fragment to your **[Preview Service](/help/headless/deployment/architecture.md)** (as well as to your Publish instance).

You can publish your fragment from either the editor, or the console. 

See:

* [Publishing and Previewing a Fragment](/help/sites-cloud/administering/content-fragments/managing.md#publishing-and-previewing-a-fragment) for full details.

* [Unpublishing a fragment](/help/sites-cloud/administering/content-fragments/managing.md#unpublishing-a-fragment) for full details.

<!--
## Preview based on a HTML Template {#preview-based-on-a-html-template}

The Content Fragment console provides a **Preview** option for every fragment.

The icon can be selected to open a dialog that represents the fragment based on a HTML template. You can use the default template, or develop and load your own.
-->

## Preview with Visualization (HTML) Templates {#preview-with-visualization-html-templates}

AEM allows you to preview your content fragment using a visual layout based on an HTML template. A **Generic Template** is available within AEM as a default, but you can also create and customize your own templates.

To preview your Content Fragment using a template:

1. In the Content Fragment console navigate to the location of your fragment.
1. Select your fragment.
1. Select **Preview** from the top toolbar.
   A dialog will open. 
   1. If no customized templates are available, then AEM will use the **Generic Template** to display your fragment. The **Generic Template**:

      * displays the fields of your fragment in table form; name and content
      * shows the content of referenced fragments in separate tables, with the same format
   1. If customized templates are available, you can select the template you want to use (including the **Generic Template**)
   1. If configured you can also select the **Preview URL** and the **Publish URL**.

   For example, preview with the **Generic Template**:

   <!-- CQDOC-23232-CF-VTemplates - new screenshot -->

   ![Preview Fragment with Generic HTML Template](/help/sites-cloud/administering/content-fragments/assets/cf-preview-html-template-referenced-fragment.png)

>[!NOTE]
>
>See [Content Fragments - Visualization Templates](/help/implementing/developing/extending/content-fragments-visualization-templates.md) for details about creating and customizing templates.
