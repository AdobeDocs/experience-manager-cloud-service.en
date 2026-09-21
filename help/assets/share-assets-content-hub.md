---
title: Share Assets in [!DNL the Content Hub]
description: Share Assets in [!DNL the Content Hub]
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 5284d229-1596-40bf-aa5f-af4b6500ebdf
---
# Share assets in Content Hub {#search-assets-as-a-link}

Create a link to selected assets to share them with others easily. As an authorized [!DNL Content Hub] user, select one or more assets available in your [!DNL Content Hub] environment, generate a link, and send it to other private or public users.

>[!VIDEO](https://video.tv.adobe.com/v/3474890/?learn=on&enablevpops=on){transcript=true}

## Prerequisites {#prerequisites}

[Content Hub users](deploy-content-hub.md#onboard-content-hub-users) can create a link to selected assets and share it with other users. 

## Share Assets {#share-assets}

Public link sharing enables you to securely share multiple assets and collections through a single public link. You can update shared content without regenerating links, protect access with passwords and expiration dates, revoke access when needed, un-share publicly shared links anytime, and provide recipients with a branded landing experience. This streamlines external content distribution while improving security, governance, and brand consistency.

Follow these steps to share assets and collections with private or public users:

1. Navigate to your Content Hub homepage, select the asset or collection, and click **[!UICONTROL Share]** > **[!UICONTROL Share with a link]** and select the **[!UICONTROL New link]** option. The process for sharing assets and collections is identical.
   
![share in public link](/help/assets/assets/public-link.png)

1. The public link creation dialog box appears. Add a title and description to provide context and intended use of the asset or collection. For added security, you can set an expiration date to automatically revoke access after a specified period. To create a password to restrict access to authorized users, select **[!UICONTROL Anyone with the link]** under **[!UICONTROL Who has access]** and toggle the **[!UICONTROL Require password protection]** option. Click **[!UICONTROL Create link]**. 
   
![new public link dialog box](/help/assets/assets/new-public-link.png)

1. To add additional assets to the shared collection, go to **[!UICONTROL All assets]** in the Content Hub homepage and select the assets you want to add. Click on ![share](/help/assets/assets/share.svg) and then select **[!UICONTROL Add to link]**. From the dialog box, search for the link you created, click the add button and then click on **[!UICONTROL Save]**. 

![new public link dialog box](/help/assets/assets/add-assets.png)

   You can view the newly added assets within the existing collection under **[!UICONTROL Shared]**.  

   ![new public link dialog box](/help/assets/assets/added-assets.png)

1. To update the link details such as title, description, and password, or delete the link, click on the three dots and then select **[!UICONTROL Details]**. 

![customize](/help/assets/assets/customize.png)

## Share an asset from its preview page {#share-asset-from-preview-page}

Execute the following steps to share an asset while previewing it:

1. Navigate to the [!DNL Content Hub] homepage and click the asset thumbnail to preview the asset and display the menu options on the right pane of the dialog box.
1. Select ![share](/help/assets/assets/share.svg) to display the **[!UICONTROL Share]** panel.
![share asset while previewing it](/help/assets/assets/share-link-asset-preview.png)
1. Follow Steps 3 to 5 in [Share assets](#share-assets) section to generate and share the asset link (Private or public) from this **[!UICONTROL Share]** panel. 

## Access the shared assets

Access the shared assets page through the link and do the following:

* Select one or more assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** to select the  **[!UICONTROL Original]**,  **[!UICONTROL Static Renditions]** or **[!UICONTROL Smart Crop]** from the available download options.
![](/help/assets/assets/download-shared-assets.png)
* Click the asset thumbnail to see the asset's metadata. 
* On the shared assets page ([accessed through a private link](#share-assets)), click an asset thumbnail and select ![download](/help/assets/assets/download-icon.svg) to select and view the available dynamic renditions of the asset on the **[!UICONTROL Download]** panel before selecting and downloading them.
![](/help/assets/assets/download-renditions-shared-assets-page.png)


## Shared assets view {#shared-assets-view}

Use the shared link to access the assets page, and then follow these steps:

1. Enter the shared password to access the assets or collection. This provides an additional layer of security and helps prevent unauthorized access.
2. Once password authentication is complete, the shared assets or collection page is displayed. You can browse the shared assets or collection and download them as needed.

   ![browse](/help/assets/assets/browse.png)

## Frequently asked questions {#faqs-share-assets-content-hub}

### What does sharing assets in AEM Assets Content Hub mean?

Sharing assets in AEM Assets Content Hub allows authorized users to easily share one or more assets or entire collections with others by generating a link. This link can be sent to private users (who must sign in) or public users (who can access as guests), giving recipients direct access to view and download the selected assets.

### How do I share assets or collections with others using AEM Assets Content Hub?

To share assets or collections in AEM Assets Content Hub, navigate to the Content Hub homepage, select one or more assets (or go to the Collections tab for collections), and click the Share icon. In the Share dialog, you can preview the assets, remove any if needed, add a title and description, select who can access the link (private or public), set an expiration period, and then click Get Link to generate and copy the shareable URL. The link can then be sent to team members or stakeholders.

### What access options are available when sharing assets in AEM Assets Content Hub, and how do they differ?

Content Hub allows you to choose between two access options for shared links: private and public. Private links require recipients to sign in to their Content Hub environment to view and download assets, providing added security. Public links can be accessed by anyone with the link, without requiring sign-in. Each link type comes with its own expiration settings, such as 24 hours to one week for public links and custom dates for private links.

### Is there any configuration managed by administrator to be able to generate public links for assets in AEM Assets Content Hub?

Yes, administrators can enable or disable the **Enable Public Link** toggle available in **Collections and Sharing** tab on the Configuration UI to be manage the generation of public links for assets in AEM Assets Content Hub.

### Can I set expiration dates for shared asset links in AEM Assets Content Hub, and why is this important?

Yes, you can set expiration dates for both private and public shared links in AEM Assets Content Hub. For public links, you can choose from presets like 24 hours up to one week, while private links allow you to select from presets or set a custom expiration date. Expiration dates are important because once the link expires, it can no longer be used to access or download the assets, which helps maintain the security and control of your content.

### What can recipients do with the shared asset link created using AEM Assets Content Hub, and are there options for downloading different renditions?

Recipients who receive a shared asset link can open it in their browser to preview, select, and download the assets provided. If asset renditions are enabled in AEM Assets Content Hub, recipients can choose which renditions (such as Original or Static) they want to download. The assets and renditions are downloaded as a zip file, and metadata can be viewed by clicking the asset thumbnail. The link remains functional until its set expiration date.


**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
