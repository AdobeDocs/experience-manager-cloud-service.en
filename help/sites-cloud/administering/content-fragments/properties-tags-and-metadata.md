---
title: Content Fragments Properties, Tags and Metadata
description: Learn how to view and edit the properties, tags and metadata for managing your AEM Content Fragments from both the console and editor.
feature: Content Fragments
role: User, Developer
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
solution: Experience Manager Sites
---
# Properties, Tags and Metadata {#properties-tags-and-metadata}

You can view, and edit, the properties, tags and metadata of a fragment from both the Content Fragments console and the new Content Fragment editor.

* Properties

  The properties of a Content Fragment are the **Basic** items of information about the fragment. For example, title, path, related Content Fragment Model and more. Many are managed by AEM and cannot be directly edited by the user, but a few can be.

* Tags

  Tags are a quick and easy method of classifying content within a website. Tags may be thought of as keywords or labels that can be attached to a page, an asset, or other content to enable searches to find that content and related content.

  Tags can be managed from either the main panel of the Content Fragments console, or the Properties tab of the new Content Fragment editor.

  >[!NOTE]
  >
  >See also [Using Tags](/help/sites-cloud/authoring/sites-console/tags.md).

* Metadata

  Content Fragment metadata allows you to define a set of information that is relevant to, and required for, a group of fragments. This allows you to classify the fragments according to your requirements. The metadata is defined using Assets metadata [schemas](/help/assets/metadata-schemas.md) and [forms](/help/assets/metadata-assets-view.md) and applied to the folders containing your fragments.

## Properties {#properties}

<!-- CQDOC-23782 -->

In the properties tab of the right panel, properties, metadata and tags can be viewed. The properties can be either:

* for the **Content Fragment** - if **Main** is currently selected
* for a specific **Variation**

<!-- CQDOC-23473 - new screenshot? -->

![Content Fragment Editor - Properties](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-properties.png) 

>[!NOTE]
>
>From the editor the information shown can differ between **Main** and any **Variations**.

### Edit Properties and Tags {#edit-properties-tags}

<!-- CQDOC-23782 -->

In the properties tab (right panel) you can also edit:

* **Title**
* **Description**
* **Tags**: using the drop-down list, or the selection dialog

  <!-- CQDOC-23473 - new screenshot? -->

  ![Content Fragment Editor - Manage Tags](/help/sites-cloud/administering/content-fragments/assets/cf-authoring-edit-tags.png) 

## Tags {#tags}

### Manage Tags (Console) {#manage-tags-console}

To manage the tags:

1. Navigate to the Content Fragment console.
1. Select a Content Fragment.
1. Select **Manage Tags** in the toolbar.
1. Use the Tag selector to select tags to apply, or remove:

   ![Manage Tags](/help/sites-cloud/administering/content-fragments/assets/cf-managing-manage-tags.png)

1. **Save** updates. This will return you to the console.

### Viewing, and Editing, Tags (Editor) {#viewing-and-editing-tags}

<!-- CQDOC-23782 -->

You can also view, and edit, the tags applied to a fragment using the [Properties](/help/sites-cloud/administering/content-fragments/authoring.md) tab of the editor. The information shown differs between **Main** and any **Variations**.

## Metadata {#metadata}