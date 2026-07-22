---
title: Content Fragments Properties, Tags and Metadata
description: Learn how to view and edit the properties, tags and metadata for managing your AEM Content Fragments from both the console and editor.
feature: Content Fragments
role: User, Developer
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
solution: Experience Manager Sites
---
# Properties, Tags and Metadata {#properties-tags-and-metadata}

You can view, and edit, the properties, tags and metadata used to manage a Content Fragment from both the Content Fragments console and the new Content Fragment editor.

* [Properties](#properties)

  The properties of a Content Fragment are the **Basic** items of information about the fragment. For example, path, related Content Fragment Model, locale and more. Many are managed by AEM and cannot be directly edited by the user, but a few can be.

* [Tags](#tags)

  Tags are a quick and easy method of classifying content within a website. Tags may be thought of as keywords or labels that can be attached to a page, an asset, or other content to enable searches to find that content and related content.

  Tags can be managed from either the main panel of the Content Fragments console, or the Properties tab of the new Content Fragment editor.

  >[!NOTE]
  >
  >See also [Using Tags](/help/sites-cloud/authoring/sites-console/tags.md).

* [Metadata](#metadata)

  Content Fragment metadata allows you to define a set of information that is relevant to, and required for, a group of fragments. This allows you to classify your fragments according to your requirements, then search and action according to the metadata values. 
  
  The metadata is defined using Assets metadata [schemas](/help/assets/metadata-schemas.md) and [forms](/help/assets/metadata-assets-view.md) and applied to the folders containing your fragments.

## Properties {#properties}

You can manage the (basic) properties from both:

* Content Fragments console

  In the console you can [manage properties](/help/sites-cloud/administering/content-fragments/managing.md#manage-properties-and-metadata) by using the information ( **i** ) icon to open the right hand panel.

* new Content Fragment editor

  In the **Basic** tab of the right hand **Properties** panel of the editor, [the properties (and tags) can be viewed and edited](/help/sites-cloud/administering/content-fragments/authoring.md#view-and-edit-properties-metadata-and-tags). 

  The properties can be either:

  * for the **Content Fragment** - if **Main** is currently selected
  * for a specific **Variation**

>[!NOTE]
>
>From the editor the information shown can differ between **Main** and any **Variations**.

## Tags {#tags}

The tags can be:

* Managed from the [main panel of the console](/help/sites-cloud/administering/content-fragments/managing.md#manage-tags-console)

* You can also view, and edit, the tags applied to a fragment using the [Properties](/help/sites-cloud/administering/content-fragments/authoring.md#view-and-edit-properties-metadata-and-tags) tab of the editor

  >[!NOTE]
  >
  >The information shown differs between **Main** and any **Variations**.

## Metadata {#metadata}

The metadata structure for a Content Fragment is defined by a [metadata form](#metadata-forms) that is assigned to the folder containing the fragment.

The [metadata values can then be viewed and edited](/help/sites-cloud/administering/content-fragments/authoring.md#view-and-edit-properties-metadata-and-tags) in both the **Metadata** tab of the right hand **Properties** panel of the Content Fragments console and the new Content Fragment editor.

### Create Metadata forms {#create-metadata-forms}

You can define the metadata using metadata forms:

1. From [Assets View](/help/assets/assets-view-introduction.md):

   1. [Create a metadata form](/help/assets/metadata-assets-view.md#metadata-forms):

      ![Assets view - create a metadata form](/help/sites-cloud/administering/content-fragments/assets/cf-metadata-form-create.png)

   1. Select your metadata form for action:

      ![Assets view - select the metadata form](/help/sites-cloud/administering/content-fragments/assets/cf-metadata-form-overview-actions.png)

   1. [Define the individual items within that metadata form](/help/assets/metadata-assets-view.md#edit-metadata-forms):

      ![Assets view - edit the metadata form](/help/sites-cloud/administering/content-fragments/assets/cf-metadata-form-edit.png)

   1. [Assign the metadata form to the folder](/help/assets/metadata-assets-view.md#assign-metadata-form-folder):

      ![Assets view - assign the metadata form to a folder](/help/sites-cloud/administering/content-fragments/assets/cf-metadata-form-assign.png)


### Use Metadata forms {#use-metadata-forms}

Then view and edit the metadata for your Content Fragment in:

1. [The Content Fragments console](/help/sites-cloud/administering/content-fragments/managing.md#manage-properties-and-metadata)

   ![Content Fragments console - metadata](/help/sites-cloud/administering/content-fragments/assets/cf-metadata-form-console.png)

1. The [new Content Fragment editor](/help/sites-cloud/administering/content-fragments/authoring.md#view-and-edit-properties-metadata-and-tags)

   ![Content Fragments editor - metadata](/help/sites-cloud/administering/content-fragments/assets/cf-metadata-form-editor.png)

  >[!NOTE]
  >
  >To use your (older) Assets metadata forms with the Content Fragments console and the new Content Fragment editor you will need to [import your forms](/help/assets/import-metadata-form-from-admin-view-to-assets-view.md) from the Admin View to the [Assets View](/help/assets/assets-view-introduction.md), where you can also [manage your metadata forms](/help/assets/metadata-assets-view.md#metadata-forms). Once imported the two versions are not synchronized.
