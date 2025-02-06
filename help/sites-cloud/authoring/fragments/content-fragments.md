---
title: Content Fragments
description: Adobe Experience Manager as a Cloud Service Content Fragments allow you to design, create, curate, and use channel-independent content that can also be used when authoring your pages.
exl-id: 7a44fc4e-3793-4aa3-8c21-db0567c93244
solution: Experience Manager Sites
feature: Authoring, Content Fragments
role: User
---
# Content Fragments {#content-fragments}

Content fragments in Adobe Experience Manager (AEM) as a Cloud Service are [created and managed as page-independent assets](/help/sites-cloud/administering/content-fragments/overview.md), allowing you to create channel-neutral content, together with (possibly channel-specific) variations. You can use these fragments, and their variations, when authoring your content pages.

>[!CAUTION]
>
>This page must be read in conjunction with [Working with Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md) (and related pages) as it introduces basic terminology and concepts, together with information about creating and managing fragments, and delivering structured content fragments to channels other than AEM pages.

>[!NOTE]
>
>Content Fragments are a **Sites** feature, but are stored as **Assets**. 
>
>They are now primarily managed with the **[Content Fragments](/help/sites-cloud/administering/content-fragments/managing.md#content-fragments-console)** console, though they can still be managed from the **[Assets](/help/assets/content-fragments/content-fragments-managing.md)** console.
>
>There are two editors for authoring Content Fragments:
>
>* The new editor for [Content Fragments - Authoring](/help/sites-cloud/administering/content-fragments/authoring.md), is primarily accessed from the **Content Fragments** console.
>* The [original editor](/help/assets/content-fragments/content-fragments-variations.md) is primarily accessed from the **Assets** console. 

>[!NOTE]
>
>**Content Fragments** and **[Experience Fragments](/help/sites-cloud/authoring/fragments/content-fragments.md)** are different features within AEM:
>* **Content Fragments** are editorial content, with definition and structure, but without additional visual design and/or layout. They can be used to access structured data, including texts, numbers, and dates, amongst others. 
>* **Experience Fragments** are fully laid out content; a fragment of a web page.
>
>Experience Fragments can contain content in the form of Content Fragments, but not the other way around.
>
>For more information, see [Understanding Content Fragments and Experience Fragments in AEM](https://experienceleague.adobe.com/docs/experience-manager-learn/sites/content-fragments/understand-content-fragments-and-experience-fragments.html#content-fragments).

The content fragments enable:

* **Marketing and Campaign Strategy**
  * Review content via centrally managed content fragments.
* **Creative Pro**
  * Tracking of creative assets via collections associated with content fragments.
* **Copy Writers**
  * Write in the AEM content fragment editor.
  * Can create content variations.
  * Can associate relevant content with the content fragment.
  * Can use versioning/workflow.
  * Can share content fragment.
  * Can manage translations centrally.
* **Producers and Journey Managers**
  * Select from predefined fragments and variations with authoring in AEM.
  * Can rely on fragment and associated content always being up-to-date as copy writers and creatives make their updates in centrally managed fragments and assets.
  * Can rely on associated media content being curated for relevancy.
  * Can create ad-hoc content variations on the fly while still ensuring those variations remain centrally managed in the fragment.

## Adding a Content Fragment to Your Page {#adding-a-content-fragment-to-your-page}

1. Open your page for editing.
2. Add the **Content Fragment** component; from either the **Components** browser or **Insert New Component**.
3. You can either:
    * Open the **Assets** browser and filter for **Content Fragments** (the default is Images). Then drag the required fragment onto the component instance.
    * Select the content fragment component, then **Configure** from the toolbar. In the dialog you can open the selection dialog to browse and select the required **Content Fragment**.

   >[!NOTE]
   >
   >An alternative method is to drag a specific content fragment directly onto the page. This will automatically create the associated component (Content Fragment).

4. Initially, the content from the **Main** Element and **Master** (variation) are shown. You can [select other elements and/or variations](#selecting-the-element-or-variation) as required.

   ![Content Fragments in the Assets Browser](/help/sites-cloud/authoring/assets/content-fragments.png)

   >[!NOTE]
   >
   >For more information about further editing functionality see also:
   >
   >* [Responsive Layout](/help/sites-cloud/authoring/page-editor/responsive-layout.md)
   >* [Editing Page Content](/help/sites-cloud/authoring/page-editor/edit-content.md)

### Selecting the Element or Variation {#selecting-the-element-or-variation}

Open the fragment's **Configuration** dialog to configure the fragment for use on the current page. The dialog can depend on the component used.

>[!NOTE]
>
>See also [Core Components, the Content Fragment Component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/content-fragment-component.html)

In the appropriate configuration dialog you can select the available parameters, including:

* **Content Fragment**
  * Specify the fragment to be used.
* **Display Mode**:
  * **Single Text Element**
  * **Multiple Elements**
* **Element**
  * A selection is available dependent on the model used.

  >[!NOTE]
  >
  >The elements available depend on the model used.

* **Variation**
  * The default **Master** is always be available.
  * A selection is available if variations were created for the fragment.

* **ID**

  * **HTML ID** attribute to apply to the component.

### Quick Connection to Fragment Editor {#quick-connection-to-fragment-editor}

You can open the fragment source for editing (the asset) using the **Edit** icon on the component toolbar. This will allow you to [edit and manage the content fragment](/help/sites-cloud/administering/content-fragments/overview.md).

>[!CAUTION]
>
>As always, editing the fragment source will impact all pages that reference that content fragment.

### Adding In-Between Content {#adding-in-between-content}

When a specific content fragment is added to the page, there is a **Drag components here** placeholder between each HTML paragraph (and at the top/bottom) of the fragment.

This lets you add extra content [in-between (that is, in-between content)](/help/assets/content-fragments/content-fragments.md#in-between-content-when-page-authoring-with-content-fragments) the fragment content (at any of the available points), without having to change the root fragment.

For in-between content you can:

* Add components from the [Components browser](/help/sites-cloud/authoring/page-editor/editor-side-panel.md#components-browser)
* Add assets from the [Assets browser](/help/sites-cloud/authoring/page-editor/editor-side-panel.md#assets-browser)
* Use [Associated Content](#using-associated-content) as a source for in-between content.

>[!CAUTION]
>
>The in-between content is page content. It is not stored in the content fragment.

![Insert component](/help/sites-cloud/authoring/assets/content-fragments-insert.png)

>[!NOTE]
>
>You can also [insert visual assets (images) to the fragment itself](/help/assets/content-fragments/content-fragments-variations.md#inserting-assets-into-your-fragment).
>
>Visual assets inserted into the fragment itself are attached to the preceding paragraph in the fragment. This means that you cannot position in-between content between a visual asset and the preceding paragraph. If you need this level of connection you can add the image to the fragment (as a [mixed-media fragment](/help/assets/content-fragments/content-fragments.md#fragments-with-visual-assets)).

>[!CAUTION]
>
>After you have added in-between content to a content fragment on your page, then changing the structure of the underlying content fragment (that is, in the content fragment editor) could lead to erroneous/unexpected results.
>
>When this occurs the in-between content is kept as is:
>
>* In-between components have an absolute position within the sequence of components in the fragment flow. This position does not change, even when the content of paragraphs in the fragment changes.
>
>  This can make it appear as if the relative positioning has changed, as in-between paragraphs have no contextual relationship to the (fragment) paragraphs they are positioned next to.
>* Unless the two paragraph structures conflict; in such a case, the in-between content is not displayed (although it is still present internally).

### Using Associated Content {#using-associated-content}

If you have [associated content](/help/assets/content-fragments/content-fragments-assoc-content.md) with the [content fragment](/help/assets/content-fragments/content-fragments.md) these assets are available from the side panel (after you place your fragment on the content page). Associated content is effectively a special source of content for [in-between content](/help/assets/content-fragments/content-fragments.md#in-between-content-when-page-authoring-with-content-fragments). 

>[!NOTE]
>
>There are various methods of adding [visual assets (for example, images)](/help/assets/content-fragments/content-fragments.md#fragments-with-visual-assets) to the fragment and/or page.

>[!NOTE]
>
>If you have multiple content fragments on the one page, the **Associated Content** tab will show assets appropriate to all fragments.

Once you have added a fragment with associated content to your page a new tab (**Associated Content**) is opened in the side panel.

From here you can drag the assets to the required location (either to an existing component or to the required position where the appropriate component is created):

![Inserting an image](/help/sites-cloud/authoring/assets/content-fragments-image.png)

### Assets Inserted into the Fragment {#assets-inserted-into-the-fragment}

If assets (for example, images) have been inserted into the fragment itself (as [mixed-media fragments](/help/assets/content-fragments/content-fragments.md#fragments-with-visual-assets)), then the options for editing these assets in the page editor is limited.

For example, for an image you can

* Crop, rotate or flip the image.
* Add a title or alternative text.
* Specify a size.
* You can also configure the layout.

Other changes, such as move, copy, delete must be made in the fragment editor.

### Publishing {#publishing}

Fragments need to be published so they can used used on your published web pages:

* A fragment can be published after [creating the fragment in the Content Fragments console](/help/sites-cloud/administering/content-fragments/managing.md#publishing-and-previewing-a-fragment). 
* If an *unpublished fragment* is used on a page that is being published, the fragment can also be published at this time.

## Exporting Content Fragments {#exporting-content-fragments}

For export to Adobe Target, JSON can be used to deliver the fragment. See:

* [Integrating with Adobe Target](/help/sites-cloud/integrating/integrating-adobe-target.md)
* [Exporting Content Fragments to Adobe Target](/help/sites-cloud/integrating/content-fragments-target.md)
