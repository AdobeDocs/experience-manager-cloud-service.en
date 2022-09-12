---
title: Creating and Managing Offers (Offers Console)
description: Use the Offers console to create offers that you can use in activity experiences
exl-id: 81d2fda2-06a9-48f6-820a-dd9e11d94fcc
---
# Creating and Managing Offers (Offers Console) {#creating-and-managing-offers}

The **Offers** console will be deprecated in the future. So, from now, it is:

* Only available to customers that have *legacy* offers already defined (i.e pre-existing)
* Recommended that any such legacy offers be converted to Experience Fragment offers
  * As soon as the last legacy offer is converted/removed, the **Offers** console will no longer be available.

![Personalization Consoles](/help/sites-cloud/authoring/assets/offers-consoles.png)

>[!NOTE]
>
>Customers that have pre-existing legacy offers can still use the **Offers** console to both see existing, and create new, legacy offers.
>
>Customers without pre-existing legacy offers will not see the **Offers** console.
>
>All customers can use **Experience Fragments Offers** to create and manage offers.

## Converting a Legacy Offer to an Experience Fragment {#convert-legacy-offer-to-experience-fragment}

A **Convert to experience fragment variation** option, and workflow, has been implemented to help you convert your legacy offer to an Experience Fragment:

>[!NOTE]
>
>This is is the recommended workflow to convert legacy offers to experience fragments.

>[!NOTE]
>
>You can also create a new Experience Fragment yourself, manually transfer the content from your legacy offer to the fragment, then delete the legacy offer.

>[!CAUTION]
>
>The **Convert to experience fragment variation** option is available for all Core Components. 
>
>This option will not be supported for custom components. For such components, you must manually convert the content into an experience fragment. 

>[!CAUTION]
>
>As soon as the last legacy offer is converted/removed:
>
>* The **Offers** console will no longer be available.
>* The target icon within the toolbar bar of any other impacted components will no longer appear.  

1. Open a page that contains the offer for editing.

1. Switch to **Targeting** mode for that page.

1. Select **Start Targeting**. 

1. Select the appropriate component. 

1. The component toolbar will provide an option to **Convert to experience fragment variation**:

   ![Converting Legacy Offer to Experience Fragment](/help/sites-cloud/authoring/assets/offers-convert-legacy-icon.png)

1. A dialog will be shown. Here you can select the required **Action**:

   * Create a new Experience Fragment
   * Add the content to an existing Experience Fragment

   For this scenario, select **Create a new Experience Fragment**.

   ![Convert to Experience Fragment Variation dialog](/help/sites-cloud/authoring/assets/offers-convert-dialog.png)

1. Complete the required fields in the dialog:

   * **Parent path** 
     Specify the parent path of the new experience fragment
   * **Template** 
     Select the template to use for creating the experience fragment. 
   * **Fragment title**
     Specify the title.
   * **Fragment tags**
     Add tags, if required.

1. Confirm with **Done**.

   If you now navigate to the **Experience Fragment Offers** console, you will see your new experience fragment, together with its associated variations.

## The Offers Console {#offers-console}

>[!CAUTION]
>
>This console is being deprecated in the future, as it offers a legacy way of personalizing content.
>
>You have some time to prepare. See how to [convert your existing legacy offers into an experience fragment offer](#convert-legacy-offer-to-experience-fragment).

Use the Offers console to create offers that you can [use in activity experiences](/help/sites-cloud/authoring/personalization/targeted-content.md). Creating offers in the Offers console saves time when several experiences require the same offer:

* Create the offer once in the library and use it in multiple experiences of your brand activities.
* Change the offer in the library and the change affects all of the experiences that use it.

The Offers console organizes offers by brand. Each brand contains a library of offers that can be used in a brand's experiences. Use folders to define a hierarchical structure for organizing offers in each library. A logical folder structure enables authors to easily find offers by browsing. Tagging and search tools also enable authors to find offers.

### Add a Brand Using the Offers Console {#add-a-brand-using-the-offers-console}

Create a brand with which your offers are associated. Open a brand in the Offers console to access its offer library where you can create folders and offers.

When you create a brand using the Offers console, it also appears in the [Activities console](/help/sites-cloud/authoring/personalization/activities.md) where you can add and administer activities for the brand.

1. In the Navigation console, click or tap **Personalization** &gt; **Offers**.

   ![Navigating to the Offers console](/help/sites-cloud/authoring/assets/offers-navigation.png)

1. Click or tap **Create** and then **Create** **Brand**.
1. Select the brand template and click or tap **Next**.
1. Type a title for the brand as you want it to appear in the Offers and Activities consoles. Optionally, type or select one or more tags to associate with the brand.
1. Click or tap **Create**.

### Add a Folder to an Offer Library {#add-a-folder-to-an-offer-library}

Add a folder to the offer library of a brand to organize and store offers. You can create a folder below the brand or below other folders.

1. In the Offers console, open the location where you want to create the folder. For example, open the brand to create a top-level folder, or open another folder in the library.
1. Click or tap **Create** &gt; **Create Folder or Offer**.

   ![Creating offer folder](/help/sites-cloud/authoring/assets/offers-create-folder.png)

1. Select **Folder** and click **Next**.
1. Type a title for the folder as you want it to appear in the offer library and type or select tags.

   ![Defining folder properties](/help/sites-cloud/authoring/assets/offers-folder-properties.png)

1. Click or tap **Create**.

### Add an Offer to an Offer Library {#add-an-offer-to-an-offer-library}

Add an offer to a brand's offer library so that it can be added to the brand's experiences. When you add an offer you provide a title. You can also associate the offer with one or more tags for enhancing searchability.

After you create the offer you can open it to author the content.

1. In the Offers console, open the location where you want to create the offer. For example, open the brand to create a top-level offer, or open a folder in the library.
1. Click or tap **Create** &gt; **Create Folder or Offer**.

   ![Creating offer folder](/help/sites-cloud/authoring/assets/offers-create-folder.png)

1. Select the **Offer Page** template and then click or tap **Next**.
1. Type a title for the offer and optionally select or type one or more tags to associate with the offer, then click or tap **Create**.
1. In the confirmation dialog box, to open the offer for editing click or tap **Open Page**.

### Editing an Offer {#editing-an-offer}

Open an offer and edit the content as you want it to appear in the experiences that use it. When you edit an offer that is used in any experiences, your changes appear in the experiences.

You can open an offer from a folder in an offer library or from search results. You can also open an offer from an experience that uses the offer.

1. In the Offers console, tap or click the icon next to the offer and click or tap **Edit**.
1. Add components to the offer and edit the component content as usual.

### Deleting an Offer {#deleting-an-offer}

Delete an offer when it is no longer needed. When you attempt to delete an offer that is used in an experience, you are prompted to confirm the deletion. Confirming deletes the offer and removes it from the experiences.

You can delete an offer while viewing either folder contents in an offer library or search results.

1. In the Offers console, tap or click the icon next to the offer and click or tap **Delete**.

   Select the offer and click or tap **Delete**.

1. In the dialog box that appears, click or tap **Delete** to confirm the deletion.
1. If the offer is used in one or more experiences, a dialog box appears to indicate that the offer is referenced:

    * To delete the offer and remove it from the experiences, click or tap **Force Delete**.
    * To keep the offer, click or tap **Cancel**.

### Searching for Offers {#searching-for-offers}

Search for offers of any brand using keywords for matching the title.

![Searching for an offer](/help/sites-cloud/authoring/assets/offers-search.png)

The current search criteria appear next to the search results. You can also sort the results by column in ascending or descending order. You can perform a search from any folder of any offer library. The search results are the same regardless of the current folder.

To search offers:

1. At the top of the Offers console, click or tap the magnifying glass icon. By default the search is limited to offers.
1. Enter your keyword to search for offers. Select from the results.
