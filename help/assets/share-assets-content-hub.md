---
title: Share Assets in [!DNL the Content Hub]
description: Share Assets in [!DNL the Content Hub]
role: User
exl-id: 5284d229-1596-40bf-aa5f-af4b6500ebdf
---
# Share assets in Content Hub {#search-assets-as-a-link}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

![Share assets banner image](assets/share-assets-banner.png)

>[!AVAILABILITY]
>
>Content Hub guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Content Hub Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/content-hub.pdf"}

Create a link to selected assets to share them with others easily. As an authorized [!DNL Content Hub] user, select one or more assets available in your [!DNL Content Hub] environment, generate a link, and send it to other [!DNL Content Hub] or public users.

## Prerequisites {#prerequisites}

[Content Hub users](deploy-content-hub.md#onboard-content-hub-users) can create a link to selected assets and share it with other users. 

## Share assets {#share-assets}

To share one or more assets with [!DNL Content Hub] or public users, navigate to your [!DNL Content Hub] homepage, select one or more assets and click ![share](/help/assets/assets/share.svg) **[!UICONTROL Share]** to display a single selected asset or a list of multiple selected assets in the **[!UICONTROL Share assets]** dialog box. You can also select and share assets available in ![collections](/help/assets/assets/Smock_Collection_18_N.svg) **[!UICONTROL Collections]**. 
View an asset or review the list of assets available in this dialog box. Click ![unselect](/help/assets/assets/Close.svg) next to an asset to unselect it from the list. After reviewing the assets, follow the steps in [Share assets with [!DNL Content Hub] users](#share-assets-with-content-hub-users) or [Share assets with public users](#share-assets-with-public-users) sections based on your sharing requirement.
![generate link share](/help/assets/assets/generate-link-share.png)

### Share assets with [!DNL Content Hub] users {#share-assets-with-content-hub-users}

[!DNL Content Hub] users sign in to their [!DNL Content Hub] environment to access and download the shared assets. Execute the following steps to share one or more assets available in the **[!UICONTROL Share assets]** dialog box with [!DNL Content Hub] users:

1. Click the dropdown in the **[!UICONTROL Period of expiration]** field and select a duration after which the recipient cannot access the selected assets. 
1. Select **[!UICONTROL Generate share link]** to generate a link and copy it subsequently. 
1. Share this link with your [!DNL Content Hub] users. See [Access the shared assets](#access-shared-assets) section to learn how they access, preview, and download the shared assets after signing in to their [!DNL Content Hub] environment.

### Share assets with public users {#share-assets-with-public-users}

Public users, as guests, access and download the shared assets without signing in. Execute the following steps to share one or more assets available in the **[!UICONTROL Share assets]** dialog box with public users:

1. Enable the **[!UICONTROL Public Link]** toggle, click the dropdown in the **[!UICONTROL Period of expiration]** field and select a duration after which the recipient cannot access the selected assets. 
1. Click **[!UICONTROL Generate public share link]** to generate a link and copy it subsequently.
![generate public link share](/help/assets/assets/generate-public-link-share.png)
1. Share this link with public users. See [Access the shared assets](#access-shared-assets) section to learn how a public user access, preview, and download the shared assets.

## Share an asset from its preview page {#share-asset-from-preview-page}

Execute the following steps to share an asset while previewing it:

1. Navigate to the [!DNL Content Hub] homepage and click the asset thumbnail to display the asset preview and the menu options available on the right pane of the dialog box.
1. Select ![share](/help/assets/assets/share.svg) to display the **[!UICONTROL Share]** panel.
![share asset while previewing it](/help/assets/assets/share-asset-link-from-preview.png)
1. Generate and share the asset link from this panel by following the steps in [share assets with [!DNL Content Hub] users](#share-assets-with-content-hub-users) or [share assets with public users](#share-assets-with-public-users) sections.

## Access the shared assets {#access-shared-assets}

After receiving the link to shared assets, click the link, sign-in to your [!DNL Content Hub] environment (if required) to access the page that displays the shared assets. 

If you access the page without signing in, you can do the following:

* Select one or more assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** to download them. 
* Select ![download](/help/assets/assets/download-icon.svg) available on the asset card to download the asset.
* Click the asset thumbnail to preview the asset and display the asset metadata in the **[!UICONTROL Asset details]** panel. Click ![download](/help/assets/assets/download-icon.svg) to display the asset's static renditions in the **[!UICONTROL Download]** panel. Select the renditions and click **[!UICONTROL Download]** to download them.

If you sign in to [!DNL Content Hub] to access the page, you can do the following:

* Select one or more assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** to download the selected assets from the **[!UICONTROL Download assets]** dialog box.
* Click the asset thumbnail to preview the asset and display the asset metadata in the **[!UICONTROL Asset details]** panel. Select ![download](/help/assets/assets/download-icon.svg) to see the available asset renditions such as, the original, dynamic and smart crop renditions in the **[!UICONTROL Download]** panel. See [view and manage renditions in Experience Manager Assets](/help/assets/renditions.md) article to learn how to make renditions available on this panel. Select and download the renditions on the panel.
    ![download asset renditions](/help/assets/assets/private-link-download-assets-rendition.png)
* Click ![download](/help/assets/assets/download-icon.svg) available on the asset card to display the available asset renditions in the **[!UICONTROL Download assets]** dialog box. See [view and manage renditions in Experience Manager Assets](/help/assets/renditions.md) article to learn how to make renditions available on this panel. Select and download the renditions on the panel. 
    ![download asset rendition from asset card](/help/assets/assets/download-assets-rendition-from-asset-card.png)




