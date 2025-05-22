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

Create a shareable link to selected assets to share them with others easily. As an authorized [!DNL Content Hub] user, select one or more assets available in your [!DNL Content Hub] environment, generate a shareable link, and send it to other [!DNL Content Hub] or public users. [!DNL Content Hub] users must sign-in to their [!DNL Content Hub] environment to access and download the shared assets. Public users, as guests, can access and download the shared assets without signing in. [!DNL Content Hub] uses an asynchronous service to download assets from a shared link, ensuring faster and uninterrupted downloads.

## Prerequisites {#prerequisites}

Be a [Content Hub user](deploy-content-hub.md#onboard-content-hub-users) to share assets. 

## Share assets {#share-assets}

To share one or more assets with [!DNL Content Hub] or public users, navigate to your [!DNL Content Hub] homepage, select one or more assets and click ![share](/help/assets/assets/share.svg) **[!UICONTROL Share]**. A **[!UICONTROL Share assets]** dialog box displaying a single selected asset or a list of multiple selected assets displays. You can also select and share assets available in ![collections](/help/assets/assets/Smock_Collection_18_N.svg) **[!UICONTROL Collections]**. 
View a single asset or review the list of multiple assets available in this dialog box and click ![unselect](/help/assets/assets/Close.svg) to unselect an asset from the list. After reviewing the asset follow [Share assets with [!DNL Content Hub] users](#share-assets-with-content-hub-users) or [Share assets with public users](#share-assets-with-public-users) sections as per your requirement.
![generate link share](/help/assets/assets/generate-link-share.png)

### Share assets with [!DNL Content Hub] users {#share-assets-with-content-hub-users}

Execute the following steps to share one or more assets available in the **[!UICONTROL Share assets]** dialog box with [!DNL Content Hub] users:

1. Click the dropdown in the **[!UICONTROL Period of expiration]** field and select a duration after which the recipient cannot access the selected assets. 
1. Select **[!UICONTROL Generate share link]** to generate a link and copy it subsequently. 

Share this link with your [!DNL Content Hub] users. The user clicks the link and sign-in to their [!DNL Content Hub] environment to access the page displaying the shared assets. Selecting the assets and clicking ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** downloads the selected assets. Double clicking an asset displays its details.

### Share assets with public users {#share-assets-with-public-users}

Execute the following steps to share one or more assets available in the **[!UICONTROL Share assets]** dialog box with public users:

1. Enable the **[!UICONTROL Public Link]** toggle, click the dropdown in the **[!UICONTROL Period of expiration]** field and select a duration after which the recipient cannot access the selected assets. 
1. Click **[!UICONTROL Generate public share link]** to generate a link and copy it subsequently.
![generate public link share](/help/assets/assets/generate-public-link-share.png)

Share this link with public users. The user clicks the link to access the page displaying the shared assets. Selecting the assets and clicking ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** downloads the selected assets. Double clicking an asset displays its details.

## Share an asset from its preview page {#share-asset-from-preview-page}

Execute the following steps to share an asset while previewing it:

1. Navigate to the [!DNL Content Hub] homepage and click the asset thumbnail. The asset preview displays with menu options available on the right pane.
1. Select ![share](/help/assets/assets/share.svg), the **[!UICONTROL Share]** panel displays.
![share asset while previewing it](/help/assets/assets/share-asset-link-from-preview.png)
1. Generate an asset link to share the asset with [!DNL Content Hub] or public users: 

    1. **For [!DNL Content Hub] users:** Select a **[!UICONTROL Period of expiration]** and click **[!UICONTROL Generate share link]** to create the link and copy it subsequently. Share this link with your [!DNL Content Hub] users. The user clicks the link and sign-in to their [!DNL Content Hub] environment to access the page displaying the shared assets. Selecting the assets and clicking ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** downloads the selected assets. Double clicking an asset displays its details.
    1. **For public users:** Enable the **[!UICONTROL Public Link]** toggle, select a **[!UICONTROL Period of expiration]** and click **[!UICONTROL Generate public share link]** to create a link and copy it subsequently. Share this link with public users. The user clicks the link to access the page displaying the shared assets. Selecting the assets and clicking ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** downloads the selected assets. Double clicking an asset displays its details.
