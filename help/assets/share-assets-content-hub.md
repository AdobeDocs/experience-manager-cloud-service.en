---
title: Share Assets and Collections in [!DNL the Content Hub]
description: Share Assets and Collections in [!DNL the Content Hub]
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 5284d229-1596-40bf-aa5f-af4b6500ebdf
---
# Share assets and collections in Content Hub {#search-assets-collections-as-a-link}

Create a link to selected assets and collections to share them with others easily. As an authorized [!DNL Content Hub] user, select one or more assets and collections available in your [!DNL Content Hub] environment, generate a link, and send it to other private or public users.

>[!VIDEO](https://video.tv.adobe.com/v/3474890/?learn=on&enablevpops=on){transcript=true}

## Prerequisites {#prerequisites}

[Content Hub users](deploy-content-hub.md#onboard-content-hub-users) can create a link to selected assets and collections and share it with other users. 

## Share Assets and Collections {#share-assets-and-collections}

Public link sharing enables you to securely share multiple assets and collections through a single public link. You can update shared content without regenerating links, protect access with passwords and expiration dates, revoke access when needed, un-share publicly shared links anytime, and provide recipients with a branded landing experience. This streamlines external content distribution while improving security, governance, and brand consistency.

Follow these steps to share assets and collections with private or public users:

1. Navigate to your Content Hub homepage, select one or more assets and collections, and click ![share](/help/assets/assets/share.svg) **[!UICONTROL Share]** > **[!UICONTROL Share with a link]** and select the **[!UICONTROL New link]** option.
![share in public link](/help/assets/assets/public-link.png)

   You can view an asset or collection available from the **[!UICONTROL List View]**. Click ![unselect](/help/assets/assets/Close.svg) next to an asset to remove it from the ![list](/help/assets/assets/ViewList.svg) **[!UICONTROL List View]**. 

2. Specify a title and an optional description that defines the set of selected assets and collections. 
3. Select **[!UICONTROL Period of expiration]**. 
4. Under **[!UICONTROL Who can access]** drop down, select the access option **[!UICONTROL Anyone with the link]** or **[!UICONTROL Authenticated users]** and click **[!UICONTROL Create Link]** to generate the link. 
5. If you want to create a password to restrict access to private users, select **[!UICONTROL Anyone with the link]** under **[!UICONTROL Who has access]** and toggle the **[!UICONTROL Require password protection]** option. Share the generated password with users to enable access to the link.
6. Click **[!UICONTROL Create link]** to create the shared link. 
![new public link dialog box](/help/assets/assets/new-public-link.png)

   If you want to update the link details such as title, description, password, delete or copy the link, click ![List](/help/assets/assets/List.svg) **[!UICONTROL More options]** next to the asset and select the appropriate option. 

   ![customize](/help/assets/assets/customize.png)

   >[!NOTE]
   > 
   > [Enable public link sharing from the configuration page](/help/assets/configure-content-hub-ui-options.md#enable-public-link-sharing) to display **[!UICONTROL Public Link]** toggle on the **[!UICONTROL Share assets]** dialog box.

### Add assets in an existing collection {#add-assets-in-an-existing-collection}

To add additional assets to the shared collection, go to **[!UICONTROL All assets]** in the Content Hub homepage and select the assets you want to add. Click ![share](/help/assets/assets/share.svg) **[!UICONTROL Share]** > **[!UICONTROL Add to link]**. Search for the shared link you created, click the add button and click **[!UICONTROL Save]**. 
![new public link dialog box](/help/assets/assets/add-assets.png)
   You can view and download the newly added assets within an existing collection under **[!UICONTROL Shared]**.


## Share an asset or collection from its preview page {#share-asset-or-collection-from-preview-page}

Execute the following steps to share an asset or collection while previewing it:

1. Navigate to the [!DNL Content Hub] homepage and click the asset thumbnail to preview the asset or collection and display the menu options on the right pane of the dialog box.
2. Select ![share](/help/assets/assets/share.svg) to display the **[!UICONTROL Share]** panel.
![share asset while previewing it](/help/assets/assets/share-link-asset-preview.png)
3. Follow Steps 3 to 5 in [Share assets](#share-assets) section to generate and share the asset or collection link (Private or public) from this **[!UICONTROL Share]** panel. 

## Access the shared assets and collections

Access the shared assets and collections page through the link and do the following:

* If prompted, enter the password shared by the administrator to access the assets or collection. This provides an additional layer of security and helps prevent unauthorized access.
* Once password authentication is complete, the shared assets or collection page is displayed. You can browse the shared assets or collection and download them as needed.
* Click the asset or collection thumbnail to see the asset's or collection's metadata.
* Select one or more assets or collections and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** to select the  **[!UICONTROL Original]**,  **[!UICONTROL Static]** or both from the available download options.
![download shared assets](/help/assets/assets/download-shared-assets.png)


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
