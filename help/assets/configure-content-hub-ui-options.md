---
title: Configure Content Hub user interface
description: Configure Content Hub user interface
---
# Configure Content Hub user interface {#configure-content-hub-user-interface}

<!-- ![Download assets](assets/download-asset.jpg) -->
![Configure assets on Content Hub](assets/configure-assets.png)

Experience Manager Assets enables administrators to configure the options available on the Content Hub user interface. Based on the configuration options selected by the administrators, the Content Hub users are able to view fields on Content Hub. The configuration options include:

* Filters available to users while searching for assets.

* Asset details or properties available for each asset.

* Metadata fields available to users while adding assets to Content Hub.

* Asset metadata fields that are available for search on Content Hub.

* Branding content that you need to display for your organization.

* Any custom links that you need to include on Content Hub in addition to assets, collections, and insights.

## Prerequisites {#prerequisites-configuration-ui}

[Content Hub administrators](/help/assets/deploy-content-hub.md#step-3-onboard-content-hub-administrator) can add assets to Content Hub and can also set the Configuration options for other users within your organization. 

## Access configuration options on Content Hub {#access-configuration-options-content-hub}

To access configuration options on Content Hub:

1. Click the user icon in the right pane.

1. In the **[!UICONTROL Product Settings]** section, select **[!UICONTROL Configurations]**.

   ![Access configuration options on Content Hub](assets/access-content-hub-configuration-ui.png)

## Manage configuration options on Content Hub {#manage-configuration-options}

Manage the following configuration options for your users:

* [Import](#configure-import-options-content-hub)

* [Filters](#configure-filters-content-hub)

* [Asset details](#configure-asset-details-content-hub)

* [Search](#configure-metadata-search-content-hub)

* [Branding](#configure-branding-content-hub)

* [Custom Links](#configure-custom-links-content-hub)

### Import {#configure-import-options-content-hub}

You can configure the metadata fields that display to the users while uploading or importing assets to the Content Hub portal, such as Campaign Name, Keywords, Channels, Timeframe, Region, and so on. To do so, execute the following steps:

1. On the [Configurations](#access-configuration-options-content-hub) user interface, click **[!UICONTROL Import]**.

1. Click **[!UICONTROL Add metadata]**. 

1. Specify a label for the property, map it to a property using the **[!UICONTROL Metadata]** field, and select the input type for the new asset metadata.

1. Click the **[!UICONTROL Required field]** toggle to make the new metadata field mandatory to specify for users while uploading new assets.

1. Click **[!UICONTROL Confirm]**. The new metadata displays in the list of the existing asset properties.

1. Click **[!UICONTROL Save]** to apply the changes.

Similarly, you can click ![Edit icon](assets/do-not-localize/Edit_icon.svg), available next to each available property, to edit the labels, make these fields mandatory or non-mandatory to users while uploading assets using the **[!UICONTROL Required field]** toggle, or click the Delete icon to delete any metadata property. 

Click the **[!UICONTROL Auto-approval]** toggle if you need all assets that you add to the Experience Manager Assets repository to be auto-approved so that they are available in Content Hub immediately. Else, DAM authors or administrators need to manually approve the assets to make them available on Content Hub. The toggle is set to Off state by default.

Click **[!UICONTROL Save]** after making all modifications to apply the changes.

![Configuration UI upload details on Content Hub](assets/configuration-ui-upload-details.png)

Metadata enabled on the Configuration User Interface display on the asset upload page:

![Upload metadata on Content Hub](assets/configuration-ui-add-assets.png)

### Filters {#configure-filters-content-hub}

Content Hub allows administrators to configure filters that display while searching for assets. Execute the following steps to add a new filter:

1. On the [Configurations](#access-configuration-options-content-hub) user interface, click **[!UICONTROL Filters]**.

1. Click **[!UICONTROL Add filters]**. 

1. Specify a label for the filter, map it to a property using the **[!UICONTROL Metadata]** field, and select the input type for the new filter.
1. Click **[!UICONTROL Confirm]**. The new filter displays in the list of the existing filters.

1. Click **[!UICONTROL Save]** to apply the changes so that the new filter gets displayed on the Search page while filtering assets.

Similarly, you can click ![Edit icon](assets/do-not-localize/Edit_icon.svg), available next to each available filter, to edit the labels or click the delete icon to delete any existing filter. Click **[!UICONTROL Save]** after making all modifications to apply the changes.

   ![Configuration UI filters on Content Hub](assets/configuration-ui-filters.png)

The filters enabled on the Configuration User Interface display on the Search page:

![Search on Content Hub](assets/filters-for-search.png)


### Asset details {#configure-asset-details-content-hub}

You can also configure the asset properties that display for each asset, such as file name, title, format, size, and so on. To do so, execute the following steps:

1. On the [Configurations](#access-configuration-options-content-hub) user interface, click **[!UICONTROL Asset details]**.

1. Click **[!UICONTROL Add metadata]**. 

1. Specify a label for the property, map it to a property using the **[!UICONTROL Metadata]** field, and select the input type for the new asset metadata.
1. Click **[!UICONTROL Confirm]**. The new metadata displays in the list of the existing asset properties.

1. Click **[!UICONTROL Save]** to apply the changes so that the new property gets displayed on the asset details page.

Similarly, you can click ![Edit icon](assets/do-not-localize/Edit_icon.svg), available next to each available property, to edit the labels or click the delete icon to delete any existing asset detail. Click **[!UICONTROL Save]** after making all modifications to apply the changes.

   ![Configuration UI asset details on Content Hub](assets/configuration-ui-asset-details.png)

The properties enabled on the Configuration User Interface display on the Asset Details page:

![Asset properties on Content Hub](assets/config-ui-asset-properties.png)

### Search {#configure-metadata-search-content-hub}

Administrators can define the metadata fields that are searched when a user specifies a search criteria on Content Hub. Execute the following steps:

1. On the [Configurations](#access-configuration-options-content-hub) user interface, click **[!UICONTROL Add metadata]**.

1. Specify the metadata field and click **[!UICONTROL Confirm]**.

1. Click **[!UICONTROL Save]** to apply the changes so that the new metadata property gets displayed in the list of metadata fields.

Similarly, you can click ![Edit icon](assets/do-not-localize/Edit_icon.svg), available next to each available metadata property, to edit the property or click the delete icon to delete any existing property. Click **[!UICONTROL Save]** after making all modifications to apply the changes.

![Configuration UI Search on Content Hub](assets/configuration-ui-metadata-search.png)


### Branding {#configure-branding-content-hub}

Administrators can also personalize the title and body text on the banner of Content Hub portal, as per your branding requirements. To do so, execute the following steps:

1. On the [Configurations](#access-configuration-options-content-hub) user interface, click **[!UICONTROL Branding]**.

1. Specify text in **[!UICONTROL Title text on banner]** and **[!UICONTROL Body text on banner]** fields.

1. Click **[!UICONTROL Save]** to apply the changes.

![Configuration UI branding on Content Hub](assets/configuration-ui-branding.png)

The branding updates enabled on the Configuration User Interface display on the Content Hub portal banner:

![Configuration UI branding on Content Hub](assets/configuration-ui-branding-updates.png)

### Custom Links {#configure-custom-links-content-hub}

You can also add custom tabs in addition to standard **[!UICONTROL All Assets]**, **[!UICONTROL Collections]**, and **[!UICONTROL Insights]** tabs on the Content Hub portal just below the banner. To do so, execute the following steps:

1. On the [Configurations](#access-configuration-options-content-hub) user interface, click **[!UICONTROL Custom Links]**.

1. Click **[!UICONTROL Add link]**.

1. Specify text in **[!UICONTROL Label]** and **[!UICONTROL URL]** fields. The label that you define display as a tab and when you click the label, you navigate to the URL defined in the **[!UICONTROL URL]** field.

1. Click **[!UICONTROL Confirm]**.

1. Click **[!UICONTROL Save]** to apply the changes.

Similarly, you can click ![Edit icon](assets/do-not-localize/Edit_icon.svg), available next to each URL, to edit the links or click the delete icon to delete any existing URL. Click **[!UICONTROL Save]** after making all modifications to apply the changes.

   ![Configuration UI Custom Links on Content Hub](assets/configuration-ui-custom-links.png)

   The custom link display as a new tab next to Insights tab on the Content Hub home page.

   ![Configuration UI Custom Links tabs on Content Hub](assets/configuration-ui-custom-link-tab.png)


