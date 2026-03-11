---
title: Cascading metadata
description: This article describes how to define cascading metadata for assets in assets view.
feature: Metadata
role: Admin, User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: e7c80792-f4db-4604-a51f-b20f066b2c1b
---
# Cascading Metadata Assets View{#cascading-metadata-assets-view}

When capturing the metadata information of an asset, users provide information in the various available fields. You can display specific metadata fields or field values that are dependent on the options selected in the other fields. Such conditional display of metadata is called cascading metadata. In other words, you can create a dependency between a particular metadata field/value and one or more fields and/or their values.

Use metadata Forms to define rules for displaying cascading metadata. For example, if your metadata form includes an asset type field, you can define a pertinent set of fields to be displayed based on the type of asset a user selects.

Here are some use cases for which you can define cascading metadata:

* Where user location is required, display relevant city names based on the user's choice of country and state.
* Load pertinent brand names in a list based on the user's choice of product category.
* Toggle the visibility of a particular field based on the value specified in another field. For example, display separate shipping address fields if the user wants the shipment delivered at a different address.
* Designate a field as mandatory based on the value specified in another field.
* Change options displayed for a particular field based on the value specified in another field.
* Set the default metadata value in a particular field based on the value specified in another field.

>[!IMPORTANT]
>
>The Cascading Metadata feature is available as Limited Availability features. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment.

## Configure cascading metadata in [!DNL Experience Manager] {#configure-cascading-metadata-in-aem}

Consider a scenario where you want to display cascading metadata based on the type of asset that is selected. For example-

* For a video, display applicable fields such as format, codec, duration, and so on.
* For a Word or PDF document, display fields, such as page count, author, and so on.

We are using a dropdown field named `Image` as an example to categorize files based on their image type. The dropdown contains options representing supported image extensions (such as JPG/JPEG, GIF, etc.). To ensure data consistency and prevent unsupported formats from being selected or processed, a validation rule is applied to this field. The rule evaluates the selected dropdown value and enforces constraints that align with the accepted image formats. 

>[!IMPORTANT]
>
>You can create rules based on dropdown fields only.

Irrespective of the asset type chosen, display the copyright information as a required field. You can use the [pre-defined metadata components](metadata-assets-view.md#property-components) and [assign metadata to a folder](metadata-assets-view.md#assign-metadata-form-folder).

### Build Metadata Forms {#build-metadata-schema-forms}

Consider the steps below to create a new Metadata Form:

1. Select the [!DNL Experience Manager] logo, and go to **[!UICONTROL Settings]** > **[!UICONTROL Metadata Forms]** > **[!UICONTROL Create]**.

1. From the **[!UICONTROL Type]** dropdown, select the appropriate form type: **[!UICONTROL File]**, **[!UICONTROL Folder]**, or **[!UICONTROL Collection]**.

1. Specify the title of the metadata form in the **[!UICONTROL Name]** field.

1. Alternatively, choose an existing metadata form template from the **[!UICONTROL Choose from existing form template]** dropdown.

1. A blank Metadata Form appears. Add a new tab.

   ![Metadata Form UI](assets/metadata-form-ui.png)

   * **A:** Switch between [!UICONTROL Edit] or [!UICONTROL Preview]
   * **B:** [Components of Metadata Form](metadata-assets-view.md#property-components)
   * **C:** Switch to other Metadata Form
   * **D:** Add a new tab
   * **E:** Canvas
   * **F:** General settings for the selected component
   * **G:** Rules tab
   * **H:** Component properties

Watch this video to view the sequence of steps, [Setup Metadata Forms](https://video.tv.adobe.com/v/341275).

### Modify an existing Metadata Form {#modify-existing-metadata-form}

To modify an existing metadata form, follow the steps below:

1. Open an existing Metadata Form and navigate to the [pre-defined components](metadata-assets-view.md#property-components) that you want to add in the form and drop the elements on your canvas.

   In accordance with the **Image** use case, add a dropdown field to define image asset types. Specify the name and property path in **Settings**, and optionally configure the field as **[!UICONTROL Read-Only]** or **[!UICONTROL Multiple Selections]**.

1. Provide the key-value options for the dropdown either by entering them manually, specifying a JSON path, or importing a CSV file.

    * To specify the values manually, select **[!UICONTROL Add Manually]** under **[!UICONTROL Choices]** and click `Add` and specify the option label and value. For example, specify Video, PDF, and Image asset types.

      ![Image Asset Type](assets/image-asset-type.png)
         
   * To fetch values from a JSON path, select **[!UICONTROL Add through JSON Path]** and specify the path of the JSON file.

      >[!NOTE]
      >
      >Ensure to store JSON file in a shared location accessible to all DAM editors and authors.

      ![Add Choices through JSON path](assets/add-json-choices.png)

   * To fetch the values from a CSV dynamically, click **[!UICONTROL Import CSV]** and provide the path of the CSV file. [!DNL Experience Manager] fetches the key-value pairs in the real time when the form is presented to the user.

      ![Add Choices through CSV](assets/import-csv-choices.png)
    
   >[!NOTE]
   > 
   >You cannot import the options from a CSV file and edit them manually as both the options are mutually exclusive.

1. To create a dependency between the Image field and other fields, select the dependent field and open the **[!UICONTROL Rules]** tab. Each component supports a specific set of rules. For this use case, Image Asset Type options are used to define the rule logic.

   <!--![Image Asset Type Rule](assets/image-asset-type-rule.png)-->

   <!--![rule tab](assets/rule-tab.png)-->

1. Under **[!UICONTROL Required]**, choose the **[!UICONTROL Required based on new rule]** option. Click ![plus icon](assets/do-not-localize/aem_assets_add_icon.png) to add a new rule.

   ![rule](assets/image-required-rule1.png)

   In the current use case, the Asset Type field is required when the image asset format is JPG/JPEG, PNG, GIF, TIFF, or WEBP. Additionally, click ![edit icon](assets/do-not-localize/edit.svg) to redefine the rule or click ![delete icon](assets/do-not-localize/delete.svg) to delete the defined rule.

   ![rule](assets/image-required-rule2.png)

1. Under **[!UICONTROL Visibility]**, choose the **[!UICONTROL Visible, based on new rule]** option. Click ![plus icon](assets/do-not-localize/aem_assets_add_icon.png) to add a new rule.

   >[!NOTE]
   >
   >You can apply the **[!UICONTROL Requirement]** condition and **[!UICONTROL Visibility]** condition independent of each other.

   ![rule](assets/image-visible-rule1.png)
   
   In the current use case, the Asset Type field is visible when the image asset format is JPG/JPEG, PNG, or GIF. Additionally, click ![edit icon](assets/do-not-localize/edit.svg) to redefine the rule or click ![delete icon](assets/do-not-localize/delete.svg) to delete the defined rule.

   ![rule](assets/image-visible-rule2.png)

1. Select **[!UICONTROL Choices based on rule]** to create a dependency and define rule. Click ![plus icon](assets/do-not-localize/aem_assets_add_icon.png) to add a new rule.
   
   ![rule](assets/image-choices-rule1.png)

   To configure rule-based choices for the Asset Type dropdown, create a rule and set Image as the dependent field. Then define the display values for each image format by selecting Image for JPG/JPEG, PNG, GIF, and TIFF, and selecting Video for WEBP, ensuring only the intended values are checked for each format to dynamically display relevant options. Additionally, click ![edit icon](assets/do-not-localize/edit.svg) to redefine the rule or click ![delete icon](assets/do-not-localize/delete.svg) to delete the defined rule.

   ![rule](assets/image-choices-rule2.png)

1. Similarly, repeat the steps to create dependency between the other assets such as PDF and Word in the [!UICONTROL Asset Type] field and fields such as [!UICONTROL Page Count] and [!UICONTROL Author].

1. Click **[!UICONTROL Save]**. Apply the metadata form to a folder.

1. Navigate to the folder to which you applied the Metadata Form and open the properties page of an asset. Depending upon your choice in the Asset Type field, pertinent cascading metadata fields are displayed.

   ![Cascading Metadata Form Output](assets/cascading-metadata-form-output.png)

>[!NOTE]
> 
>To get early access to the Cascading Metadata on your Assets View account, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

## Next Steps {#next-steps}

* [Watch a video to manage metadata forms in Assets view](https://experienceleague.adobe.com/docs/experience-manager-learn/assets-essentials/configuring/metadata-forms.html)

* Provide product feedback using the [!UICONTROL Feedback] option available on the Assets view user interface

* Provide documentation feedback using [!UICONTROL Edit this page] ![edit the page](assets/do-not-localize/edit-page.png) or [!UICONTROL Log an issue] ![create a GitHub issue](assets/do-not-localize/github-issue.png) available on the right sidebar

* Contact [Customer Care](https://experienceleague.adobe.com/?support-solution=General#support)
