---
title: Customizing and Extending Content Fragments
description: A content fragment extends a standard asset.
---

# Customizing and Extending Content Fragments{#customizing-and-extending-content-fragments}

Within Adobe Experience Manager as a Cloud Service a content fragment extends a standard asset; see:

* [Creating and Managing Content Fragments](/help/assets/content-fragments/content-fragments.md) and [Page Authoring with Content Fragments](/help/sites-cloud/authoring/fundamentals/content-fragments.md) for further information about content fragments.

* [Managing Assets](/help/assets/manage-digital-assets.md) and [Customizing and Extending the Asset Editor](/help/assets/extend-asset-editor.md) for further information about standard assets.

## Architecture {#architecture}

The basic [constituent parts](/help/assets/content-fragments/content-fragments.md#constituent-parts-of-a-content-fragment) of a content fragment are:

* A *Content Fragment*,
* consisting of one or more *Content Elements*,
* and which can have one or more *Content Variations*.

Depending on the type of fragment, either models or the **Simple Fragment** template are also used:

>[!CAUTION]
>
>[Content fragment models](/help/assets/content-fragments/content-fragments-models.md) are now recommended for creating all your fragments.
>
>Content fragment models are used for all examples in WKND.

* Content Fragment Models:

  * Used for defining content fragments that hold structured content.
  * Content fragment models define the structure of a content fragment when it is created.
  * A fragment references the model; so changes to the model may/will impact any dependent fragments.
  * Models are built-up of data types.
  * Functions to add new variations, etc., have to update the fragment accordingly.

  >[!NOTE]
  >
  >For you to display/render a Content Fragment, your account must have read permissions for the model.

  >[!CAUTION]
  >
  >Any changes to an existing content fragment model can impact dependent fragments; this can lead to orphan properties in those fragments.

* Content Fragment Template - **Simple Fragment**:

  * Used for defining simple content fragments.

  * This template defines the (basic, text-only) structure of a content fragment when it is created.

  * The template is copied to the fragment when it is created.

  * Functions to add new variations, etc., have to update the fragment accordingly.

  * The Content fragment template (**Simple Fragment**) operates in a different manner to that of other templating mechanisms within the AEM ecosystem (e.g. page templates, etc.). Therefore it should be considered separately.

  * When based on the **Simple Fragment** template the MIME type of the content is managed on the actual content; this means that each element and variation can have a different MIME type.

### Integration of Sites with Assets {#integration-of-sites-with-assets}

Content Fragment Management (CFM) is part of AEM Assets as:

* Content fragments are assets.
* They use existing Assets functionality.
* They are fully integrated with Assets (admin consoles, etc.).

Content Fragments are considered a Sites feature as:

* They are used when authoring your pages.

#### Mapping Structured Content Fragments to Assets {#mapping-structured-content-fragments-to-assets}

![content fragment to assets structured](assets/content-fragment-to-assets-structured.png)

Content fragments with structured content (i.e. based on a content fragment model) are mapped to a single asset:

* All content is stored under the `jcr:content/data` node of the asset:

  * The element data is stored under the master sub-node:
    `jcr:content/data/master`

  * Variations are stored under a sub-node that carries the name of the variation:
    e.g. `jcr:content/data/myvariation`

  * The data of each element is stored in the respective sub-node as a property with the element name:
    e.g. the content of element `text` is stored as property `text` on `jcr:content/data/master`

* Metadata and associated content is stored below `jcr:content/metadata`
  Except for the title and description, which are not considered traditional metadata and stored on `jcr:content`

#### Mapping Simple Content Fragments to Assets {#mapping-simple-content-fragments-to-assets}

![content fragment to assets simple](assets/content-fragment-to-assets-simple.png)

Simple content fragments (based on the **Simple Fragment** template) are mapped to a composite consisting of a main asset and (optional) sub-assets:

* All non-content information of a fragment (such as title, description, metadata, structure) is managed on the main asset exclusively.
* The content of the first element of a fragment is mapped to the original rendition of the main asset.

    * The variations (if there are any) of the first element are mapped to other renditions of the main asset.

* Additional elements (if existing) are mapped to sub-assets of the main asset.

    * The main content of these additional elements map to the original rendition of the respective sub-asset.
    * Other variations (if applicable) of any additional elements map to other renditions of the respective sub-asset.

#### Asset Location {#asset-location}

As with standard assets, a content fragment is held under:

`/content/dam`

#### Asset Permissions {#asset-permissions}

For further details see [Content Fragment - Delete Considerations](/help/assets/content-fragments/content-fragments-delete.md).

#### Feature Integration {#feature-integration}

To integrate with Assets core:

* The Content Fragment Management (CFM) feature builds on the Assets core.

* CFM provides its own implementations for items in the card/column/list views; these plug into the existing Assets content rendering implementations.

* Several Assets components have been extended to cater for content fragments.

### Using Content Fragments in Pages {#using-content-fragments-in-pages}

>[!CAUTION]
>
>The [Content Fragment component is part of Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/components/content-fragment-component.html). See [Developing Core Components](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/developing.html) for more details.

Content fragments can be referenced from AEM pages, just as any other asset type. AEM provides the **[Content Fragment core component](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/components/content-fragment-component.html)** - a [component that allows you to include content fragments on your pages](/help/sites-cloud/authoring/fundamentals/content-fragments.md#adding-a-content-fragment-to-your-page). You can also extend this **[Content Fragment](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/developing/developing.html)** core component.

* The component uses the `fragmentPath` property to reference the actual content fragment. The `fragmentPath` property is handled in the same manner as similar properties of other asset types; for example, when the content fragment is moved to another location.

* The component allows you to select the variation to be displayed.

* Additionally, a range of paragraphs can be selected to restrict the output; for example, this can be used for multi-column output.

* The component allows in-between content:

  * Here the component allows you to place other assets (images, etc.) in between the paragraphs of the referenced fragment.

  * For in-between content you need to:

    * be aware of the possibility of unstable references; in-between content (added when authoring a page) has no fixed relationship to the paragraph it is positioned next to, inserting a new paragraph (in the content fragment editor) before the position of the in-between content can lose the relative position

    * consider the additional parameters (such as variation and paragraph filters) to configure what is rendered on the page

>[!NOTE]
>
>**Content Fragment Model:**
>
>When using a content fragment that has been based on a content fragment model on a page, the model is referenced. This means that if the model has not been published at the time you publish the page, this will be flagged and the model added to the resources to be published with the page.
>
>**Content Fragment Template - Simple Fragment:**
>
>When using a content fragment that has been based on the content fragment template **Simple Fragment** on a page, there is no reference as the template was copied when creating the fragment.

### Integration with other Frameworks {#integration-with-other-frameworks}

Content fragments can be integrated with:

* **Translations**

  Content Fragments are fully integrated with the AEM translation workflow. On an architectural level, this means:

  * The individual translations of a content fragment are actually separate fragments; for example:

    * they are located under different language roots; but share exactly the same relative path below the relevant language root:

      `/content/dam/<path>/en/<to>/<fragment>`

      vs.

      `/content/dam/<path>/de/<to>/<fragment>`

  * Besides the rule-based paths, there is no further connection between the different language versions of a content fragment; they are handled as two separate fragments, although the UI provides the means to navigate between the language variants.

  >[!NOTE]
  >
  >The AEM translation workflow works with `/content`:
  >
  >* As the content fragment models reside in `/conf`, these are not included in such translations. You can internationalize the UI strings.

* **Metadata schemas**

  * Content fragments (re)use the [metadata schemas](/help/assets/metadata-schemas.md), that can be defined with standard assets.

  * CFM provides its own, specific schema:

    `/libs/dam/content/schemaeditors/forms/contentfragment`

    this can be extended if required.

  * The respective schema form is integrated with the fragment editor.

## The Content Fragment Management API - Server-Side {#the-content-fragment-management-api-server-side}

You can use the server-side API to access your content fragments; see:

[com.adobe.cq.dam.cfm](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/ref/javadoc/com/adobe/cq/dam/cfm/package-frame.html)

>[!CAUTION]
>
>It is strongly recommended to use the server-side API instead of directly accessing the content structure. 

### Key Interfaces {#key-interfaces}

The following three interfaces can serve as entry points:

* **Content Fragment** ([ContentFragment](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/ref/javadoc/com/adobe/cq/dam/cfm/ContentFragment.html))

  This interface allows you to work with a content fragment in an abstract way.

  The interface provides you with the means to:

  * Manage basic data (e.g. get name; get/set title/description)
  * Access meta data
  * Access elements:

    * List elements
    * Get elements by name
    * Create new elements (see [Caveats](#caveats))

    * Access element data (see `ContentElement`)

  * List variations defined for the fragment
  * Create new variations globally
  * Manage associated content:

    * List collections
    * Add collections
    * Remove collections

  * Access the fragment's model or template

  Interfaces that represent the prime elements of a fragment are:

  * **Content Element** ([ContentElement](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/ref/javadoc/com/adobe/cq/dam/cfm/ContentElement.html))

    * Get basic data (name, title, description)
    * Get/Set content
    * Access variations of an element:

      * List variations
      * Get variations by name
      * Create new variations (see [Caveats](#caveats))
      * Remove variations (see [Caveats](#caveats))
      * Access variation data (see `ContentVariation`)

    * Shortcut for resolving variations (applying some additional, implementation-specific fallback logic if the specified variation is not available for an element)

  * **Content Variation** ([ContentVariation](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/developing/ref/javadoc/com/adobe/cq/dam/cfm/ContentVariation.html))

    * Get basic data (name, title, description)
    * Get/Set content
    * Simple synchronization, based on last modified information

  All three interfaces ( `ContentFragment`, `ContentElement`, `ContentVariation`) extend the `Versionable` interface, which adds versioning capabilities, required for content fragments:

  * Create new version of the element
  * List versions of the element
  * Get the content of a specific version of the versioned element

### Adapting - Using adaptTo() {#adapting-using-adaptto}

The following can be adapted:

* `ContentFragment` can be adapted to:

  * `Resource` - the underlying Sling resource; updating the underlying `Resource` directly requires rebuilding the `ContentFragment` object.

  * `Asset` - the DAM `Asset` abstraction that represents the content fragment; updating the `Asset` directly requires rebuilding the `ContentFragment` object.

* `ContentElement` can be adapted to:

  * `ElementTemplate` - for accessing the element's structural information.

* `Resource` can be adapted to:

  * `ContentFragment`

### Caveats {#caveats}

It should be noted that:

* The entire API is designed to **not** persist changes automatically (unless otherwise noted in the API JavaDoc). So you will always have to commit the resource resolver of the respective request (or the resolver you are actually using).

* Tasks that might require additional effort:

  * Creating/removing new elements will not update the data structure of simple fragments (based on the **Simple Fragment** template).

  * Create new variations from `ContentFragment` to update the data structure.

  * Removing existing variations will not update the data structure.

## The Content Fragment Management API - Client-Side {#the-content-fragment-management-api-client-side}

>[!CAUTION]
>
>The client-side API is internal.

### Additional Information {#additional-information}

See the following:

* `filter.xml`

  The `filter.xml` for content fragment management is configured so that it does not overlap with the Assets core content package.

## Edit Sessions {#edit-sessions}

An editing session is started when the user opens a content fragment in one of the editor pages. The editing session is finished when the user leaves the editor by selecting either **Save** or **Cancel**.

### Requirements {#requirements}

Requirements for controlling an editing session are:

* Editing a content fragment, which can span multiple views (= HTML pages), should be atomic.

* The editing should also be *transactional*; at the end of the edit session the changes must either be committed (saved) or rolled back (cancelled).

* Edge cases should be handled properly; these include situations such as when the user leaving the page by entering a URL manually or using global navigation.

* A periodic auto save (every x minutes) should be available to prevent data loss.

* If a content fragment is edited by two users concurrently, they should not overwrite each other's changes.

<!--
#### Processes {#processes}

The processes involved are:

* Starting a session

  * A new version of the content fragment is created.

  * Auto save is started.

  * Cookies are set; these define the currently edited fragment and that there is an edit session open.

* Finishing a session

  * Auto save is stopped.

  * Upon commit:

    * The last modified information is updated.

    * Cookies are removed.

  * Upon rollback:

    * The version of the content fragment that was created when the edit session was started is restored.

    * Cookies are removed.

* Editing

  * All changes (auto save included) are done on the active content fragment - not in a separated, protected area.

  * Therefore, those changes are reflected immediately on AEM pages that reference the respective content fragment

#### Actions {#actions}

The possible actions are:

* Entering a page

  * Check if an editing session is already present; by checking the respective cookie.

    * If one exists, verify that the editing session was started for the content fragment that is currently being edited

      * If the current fragment, reestablish the session.

      * If not, try to cancel editing for the previously edited content fragment and remove cookies (no editing session present afterwards).

    * If no edit session exists, wait for the first change made by the user (see below).

  * Check if the content fragment is already referenced on a page and display appropriate information if so.

* Content change

  * Whenever the user changes content and there is no edit session present, a new edit session is created (see [Starting a session](#processes)).

-->

* Leaving a page

  * If an editing session is present and the changes have not been persisted, a modal confirmation dialog is shown to notify the user of potentially lost content and allow them to stay on the page.

## Examples {#examples}

### Example: Accessing an existing content fragment {#example-accessing-an-existing-content-fragment}

To achieve this you can adapt the resource that represents the API to:

`com.adobe.cq.dam.cfm.ContentFragment`

For example:

```java
// first, get the resource
Resource fragmentResource = resourceResolver.getResource("/content/dam/fragments/my-fragment");
// then adapt it
if (fragmentResource != null) {
    ContentFragment fragment = fragmentResource.adaptTo(ContentFragment.class);
    // the resource is now accessible through the API
}
```

### Example: Creating a new content fragment {#example-creating-a-new-content-fragment}

To create a new content fragment programmatically, you need to use a 
`FragmentTemplate` adapted from a model or template resource.

For example:

```java
Resource templateOrModelRsc = resourceResolver.getResource("...");
FragmentTemplate tpl = templateOrModelRsc.adaptTo(FragmentTemplate.class);
ContentFragment newFragment = tpl.createFragment(parentRsc, "A fragment name", "A fragment description.");

```

### Example: Specifying the auto-save interval {#example-specifying-the-auto-save-interval}

The [auto save interval](/help/assets/content-fragments/content-fragments-managing.md#save-cancel-and-versions) (measured in seconds) can be defined using the configuration manager (ConfMgr):

* Node: `<conf-root>/settings/dam/cfm/jcr:content`
* Property Name: `autoSaveInterval`
* Type: `Long`

* Default: `600` (10 minutes); this is defined on `/libs/settings/dam/cfm/jcr:content`

If you want to set an auto save interval of 5 minutes you need to define the property on your node; for example:

* Node: `/conf/global/settings/dam/cfm/jcr:content`
* Property Name: `autoSaveInterval`

* Type: `Long`

* Value: `300` (5 minutes equates to 300 seconds)

## Components for Page Authoring {#components-for-page-authoring}

For further information see

* [Core Components - Content Fragment Component](https://docs.adobe.com/content/help/en/experience-manager-core-components/using/components/content-fragment-component.html) (recommended)
