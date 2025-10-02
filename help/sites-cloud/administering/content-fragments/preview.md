---
title: Previewing Content Fragments
description: Understand how to preview your Content Fragments by a range of methods.
feature: Content Fragments
role: User, Developer, Architect
solution: Experience Manager Sites
---
# Previewing Content Fragments {#previewing-content-fragments}

Previewing your Content Fragments can be used for both headless delivery and page authoring.

There are several methods available for Content Fragments. The console and editor described in this section have been developed for headless content delivery (though they can be used for all scenarios).

You can preview your fragment:

* using the [Preview URL pattern](#preview-url-pattern)

* by publishing to, and unpublishing from, the [Preview instance](#preview-instance)

<!--
* with a HTML template, using **[Preview]()** from the Content Fragments console
-->

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

You can **Publish**, and **Unpublish**, your fragment to your Preview instance (as well as to your Publish instance).

You can publish your fragment from either the editor, or the console. 

See:

* [Publishing and Previewing a Fragment](/help/sites-cloud/administering/content-fragments/managing.md#publishing-and-previewing-a-fragment) for full details.

* [Unpublishing a fragment](/help/sites-cloud/administering/content-fragments/managing.md#unpublishing-a-fragment) for full details.

<!--
## Preview based on a HTML Template {#preview-based-on-a-html-template}

The Content Fragment console provides a **Preview** option for every fragment.

The icon can be selected to open a dialog that represents the fragment based on a HTML template. You can use the default template, or develop and load your own.
-->
