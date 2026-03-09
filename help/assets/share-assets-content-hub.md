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

## Share assets {#share-assets}

To share one or more assets with private or public users, execute the following steps:

1. Navigate to your [!DNL Content Hub] homepage, select one or more assets and click ![share](/help/assets/assets/share.svg) **[!UICONTROL Share]** to display a single selected asset or a list of multiple selected assets in the **[!UICONTROL Share assets]** dialog box.

   You can also select and share assets available in ![collections](/help/assets/assets/Smock_Collection_18_N.svg) **[!UICONTROL Collections]**. 

1. View an asset or review the list of assets available in **[!UICONTROL Share assets]** dialog box. Click ![unselect](/help/assets/assets/Close.svg) next to an asset to remove it from the list. 

1. Specify a title and an optional description that defines the set of selected assets.

1. Select **[!UICONTROL Period of expiration]**.

1. Under **[!UICONTROL Who can access]** drop down, select the access options and click **[!UICONTROL Get Link]** to generate a link to share with the selected users. Private users need to sign in to their [!DNL Content Hub] environment to access the shared assets page. Whereas, public users, as guests, can access the shared assets page without signing in to [!DNL Content Hub].

<!--1. Select a **[!UICONTROL period of expiration]** and click **[!UICONTROL Get Link]** to generate a link to share with private users. Private users sign in to their [!DNL Content Hub] environment to access the shared assets page.-->

   ![private and public link](/help/assets/assets/shared-link-for-assets.png)

   <!--Enable the **[!UICONTROL Public Link]** toggle, select a **[!UICONTROL period of expiration]** and click **[!UICONTROL Generate Public Link]** to generate a link to share with public users. Public users, as guests, access the shared assets page without signing in to [!DNL Content Hub].-->

   >[!NOTE]
   > 
   > [Enable public link sharing from the configuration page](/help/assets/configure-content-hub-ui-options.md#enable-public-link-sharing) to display **[!UICONTROL Public Link]** toggle on the **[!UICONTROL Share assets]** dialog box.

## Share an asset from its preview page {#share-asset-from-preview-page}

Execute the following steps to share an asset while previewing it:

1. Navigate to the [!DNL Content Hub] homepage and click the asset thumbnail to preview the asset and display the menu options on the right pane of the dialog box.
1. Select ![share](/help/assets/assets/share.svg) to display the **[!UICONTROL Share]** panel.
![share asset while previewing it](/help/assets/assets/share-link-asset-preview.png)
1. Follow Steps 3 to 5 in [Share assets](#share-assets) section to generate and share the asset link (Private or public) from this **[!UICONTROL Share]** panel. 

## Access the shared assets {#access-shared-assets}

Access the shared assets page through the link and do the following:

* Select one or more assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** to select the  **[!UICONTROL Original]**,  **[!UICONTROL Static]** or both renditions from the available download options.
![](/help/assets/assets/download-shared-assets.png)
* Click the asset thumbnail to see the asset's metadata. 
* On the shared assets page ([accessed through a private link](#share-assets)), click an asset thumbnail and select ![download](/help/assets/assets/download-icon.svg) to select and view the available dynamic renditions of the asset on the **[!UICONTROL Download]** panel before selecting and downloading them.
![](/help/assets/assets/download-renditions-shared-assets-page.png)

## Frequently asked questions {#faqs-share-assets-content-hub}

### What does sharing assets in AEM Assets Content Hub mean?

Sharing assets in AEM Assets Content Hub allows authorized users to easily share one or more assets or entire collections with others by generating a link. This link can be sent to private users (who must sign in) or public users (who can access as guests), giving recipients direct access to view and download the selected assets.

### How do I share assets or collections with others using AEM Assets Content Hub?

To share assets or collections in Content Hub, navigate to the Content Hub homepage, select one or more assets (or go to the Collections tab for collections), and click the Share icon. In the Share dialog, you can preview the assets, remove any if needed, add a title and description, select who can access the link (private or public), set an expiration period, and then click Get Link to generate and copy the shareable URL. The link can then be sent to team members or stakeholders.

### What access options are available when sharing assets in AEM Assets Content Hub, and how do they differ?

Content Hub allows you to choose between two access options for shared links: private and public. Private links require recipients to sign in to their Content Hub environment to view and download assets, providing added security. Public links can be accessed by anyone with the link, without requiring sign-in. Each link type comes with its own expiration settings, such as 24 hours to one week for public links and custom dates for private links.

### Is there any configuration managed by administrator to be able to generate public links for assets in AEM Assets Content Hub?

Yes, administrators can enable or disable the **Enable Public Link** toggle available in **Collections and Sharing** tab on the Configuration UI to be manage the generation of public links for assets in AEM Assets Content Hub.

### Can I set expiration dates for shared asset links in AEM Assets Content Hub, and why is this important?

Yes, you can set expiration dates for both private and public shared links in Content Hub. For public links, you can choose from presets like 24 hours up to one week, while private links allow you to select from presets or set a custom expiration date. Expiration dates are important because once the link expires, it can no longer be used to access or download the assets, which helps maintain the security and control of your content.

### What can recipients do with the shared asset link created using AEM Assets Content Hub, and are there options for downloading different renditions?

Recipients who receive a shared asset link can open it in their browser to preview, select, and download the assets provided. If asset renditions are enabled in Content Hub, recipients can choose which renditions (such as Original or Static) they want to download. The assets and renditions are downloaded as a zip file, and metadata can be viewed by clicking the asset thumbnail. The link remains functional until its set expiration date.




