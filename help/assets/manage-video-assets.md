---
title: Manage video assets
description: Upload, preview, annotate, and publish video assets in [!DNL Adobe Experience Manager].
contentOwner: AG
feature: Asset Management, Publishing, Collaboration, Video
role: User
exl-id: 91edce4a-dfa0-4eca-aba7-d41ac907b81e
---
# Manage video assets {#manage-video-assets}

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

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/managing/managing-video-assets.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

Video format is a critical part of digital assets of an organization. [!DNL Adobe Experience Manager] offers mature offerings and features to manage the entire lifecycle of your video assets after their creation.

Learn how to manage and edit the video assets in [!DNL Adobe Experience Manager Assets]. Video encoding and transcoding, for example, FFmpeg transcoding, is possible using Processing Profiles and using [!DNL Dynamic Media] integration. Without [!DNL Dynamic Media] license, [!DNL Experience Manager] provides basic support for videos, such as transcoding using FFmpeg, extraction of preview thumbnails for the supported file formats, and preview in the user interface for formats that are supported for playback in the browser directly.

## Upload and preview video assets {#upload-and-preview-video-assets}

You can upload and preview video assets of supported format to [!DNL Experience Manager Assets]. 
<!-- It generates previews for video assets with the extension MP4. -->

### Upload video assets

To upload a video asset, follow these steps:

1. In the digital assets folder or subfolders, navigate to the location where you need to add the asset.
1. Click **[!UICONTROL Create]** from the toolbar and choose **[!UICONTROL Files]**. <br>Alternatively, drag a file on the user interface. 
Learn more about [uploading assets](manage-digital-assets.md#uploading-assets) in [!DNL Experience Manager Assets].

<!-- 1. To preview a video in the card view, click the **[!UICONTROL Play]** ![play option](assets/do-not-localize/play.png) option on the video asset. You can pause or play video in the card view only. The [!UICONTROL Play] and [!UICONTROL Pause] options are not available in the list view.
1. To preview the video in the asset details page, select **[!UICONTROL Edit]** on the card. The video plays in the native video player of the browser. You can play, pause, control the volume, and zoom the video to full screen. -->

### Preview video assets

You can preview videos in supported renditions in the [!DNL Assets] user interface. To preview a video asset, follow these steps:

1. Upload a video asset of a supported format to [!DNL Experience Manager Assets]. Learn more about the [supported video formats](file-format-support.md#video-formats). <br>Once uploaded, the video asset is processed, and a preview rendition is generated.
1. Click the asset, and select ![details option](assets/do-not-localize/details_icon.svg) **[!UICONTROL Details]**  from the top toolbar. The video asset opens in the video viewer.
1. Click the ![play option](assets/do-not-localize/play.png) icon on the video thumbnail. <br>You can play, pause, control the volume, and zoom the video to full screen.

For existing video assets in [!DNL Experience Manager Assets], you need to **[!UICONTROL Reprocess]** the assets in [!DNL Experience Manager] to enable the video preview feature. Learn how to [reprocess digital assets](reprocessing.md) in [!DNL Experience Manager].

### Limitations of video preview

* MXF files do not show video previews even though the rendition is generated.
* WebM files do not generate preview renditions as they are playable natively by web browsers.

## Publish video assets {#publish-video-assets}

After publishing, you can include the video assets in a web page as a URL or directly embed the assets. For details, see [publish [!DNL Dynamic Media] assets](/help/assets/dynamic-media/publishing-dynamicmedia-assets.md).

## Publish videos to YouTube {#publishing-videos-to-youtube}

You can publish video assets managed in Experience Manager Assets directly to a YouTube channel that you have previously created.

To publish video assets to YouTube, you tag video assets in Experience Manager Assets with tags. You associate these tags with a YouTube channel. If a video asset's tag matches the tag of a YouTube channel, then the video is published to YouTube. Publish to YouTube occurs along with a normal publish of the video as long as an associated tag is used.

YouTube does its own encoding. As such, the original video file that was uploaded into Experience Manager is published to YouTube instead of any video rendition that Dynamic Media's encoding has created. While it is not required to process videos using Dynamic Media, it is expected that they do so in case a viewer preset is needed for playback.

When you bypass the video processing profile and publish directly to YouTube, it simply means that your video asset in Experience Manager Asset does not get a viewable thumbnail. It also means that videos that are not encoded do not work with any of the Dynamic Media asset types.

Publishing video assets to YouTube servers involves completing the following tasks to ensure safe and secure server-to-server verification with YouTube:

1. [Configure Google Cloud settings](#configuring-google-cloud-settings)
1. [Create a YouTube channel](#creating-a-youtube-channel)
1. [Add tags for publishing](#adding-tags-for-publishing)
1. [Set up YouTube in Experience Manager](#setting-up-youtube-in-aem)
1. [(Optional) Automate the setting of default YouTube properties for your uploaded videos](#optional-automating-the-setting-of-default-youtube-properties-for-your-uploaded-videos)
1. [Publish videos to your YouTube channel](#publishing-videos-to-your-youtube-channel)
1. [(Optional) Verify the published video on YouTube](/help/assets/dynamic-media/video.md#optional-verifying-the-published-video-on-youtube)
1. [Link YouTube URLs to your Web Application](#linking-youtube-urls-to-your-web-application)

You can also [unpublish videos to remove them from YouTube](#unpublishing-videos-to-remove-them-from-youtube).

### Configure Google Cloud settings {#configuring-google-cloud-settings}

To publish to YouTube, you need a Google account. If you have a GMAIL account, then you already have a Google account; if you do not have a Google account, you can easily create one. You need the account because you need credentials to publish video assets to YouTube. <!-- hidden March 3 2022 If you have an account already created, then skip this task and proceed directly to [Create a YouTube channel](#creating-a-youtube-channel). -->

The account used with Google Cloud and the Google account used for YouTube do not need to be the same.

Google periodically changes their user interface. As such, the steps to publish videos to YouTube can vary slightly from what is documented below. This caveat also applies to YouTube when you try to check if videos are uploaded to it.

>[!NOTE]
>
>The following steps were accurate at the time of writing. However, Google periodically updates their cloud web pages without notice. As such, some configuration options may be named slightly differently in the Google user interface from the name used in the steps.

**To configure Google Cloud settings:**

1. Create a Google account.

   If you already have a Google account, you can skip to the next step.

1. Go to [https://cloud.google.com/](https://cloud.google.com/).
1. On the **[!UICONTROL Google Cloud]** page, near the upper-right corner, select **[!UICONTROL Console]**.

   If necessary, **[!UICONTROL Sign in]** using your Google account credentials to see the **[!UICONTROL Console]** option.

1. On the **[!UICONTROL Dashboard]** page, to the right of **[!UICONTROL Google Cloud Platform]**, select the **[!UICONTROL Project]** drop-down list to open the **[!UICONTROL Select a project]** dialog box.
1. In the **[!UICONTROL Select a project]** dialog box, select **[!UICONTROL New Project]**.
1. In the **[!UICONTROL New Project]** dialog box, in the **[!UICONTROL Project name]** field, type the name of your new project.

   Your Project ID is based on your project name. As such, choose the project name carefully; it cannot be changed after it is created. Also, you must enter the same Project ID again when you set up YouTube in Experience Manager later on. Therefore, write it down.

1. Select **[!UICONTROL Create]**.

1. Do either one of the following:

    * On your project's Dashboard, in the **[!UICONTROL Getting Started]** card, select **[!UICONTROL Explore and enable APIs]**.
    * On your project's Dashboard, in the **[!UICONTROL APIs]** card, select **[!UICONTROL Go to APIs overview]**.

1. Near the top middle of the **[!UICONTROL APIs & Services]** page, select **[!UICONTROL ENABLE APIS AND SERVICES]**.<!-- NEXT STEP BELOW IS STEP 10 --> 
1. On the **[!UICONTROL API Library]** page, on the left side, under **[!UICONTROL Category]**, select **[!UICONTROL YouTube]**. On the right side of the page, select **[!UICONTROL YouTube]**.
1. On the **[!UICONTROL YouTube]** page, select **[!UICONTROL YouTube Data API v3]**.
1. On the **[!UICONTROL YouTube Data API v3]** page, select **[!UICONTROL MANAGE]**.

   ![6_5_googleaccount-apis-manage](/help/assets/dynamic-media/assets/6_5_googleaccount-apis-manage.png)

1. To use the API, you need credentials. If necessary, on the left side of the **[!UICONTROL APIs & Services]** page, select **[!UICONTROL Credentials]**.
1. On the **[!UICONTROL Credentials]** page, near the top, select **[!UICONTROL CREATE CREDENTIALS]**, then select **[!UICONTROL OAuth client ID]**.
1. On the **[!UICONTROL Create OAuth client ID]** page, in the **[!UICONTROL Application type]** drop-down list, select **[!UICONTROL Web application]**.

   ![6_5_googleaccount-apis-applicationtype](/help/assets/dynamic-media/assets/6_5_googleaccount-apis-applicationtype.png)

1. Do one of the following:

   * In the **[!UICONTROL Name]** field, enter a unique name for your OAuth 2.0 client.
   * Use the default name that Google already provided in the **[!UICONTROL Name]** field.

1. Under the **[!UICONTROL Authorized JavaScript origins]** heading, select **[!UICONTROL ADD URI]**.

   ![6_5_googleaccount-apis-nameauthorizations](/help/assets/dynamic-media/assets/6_5_googleaccount-apis-nameauthorizations.png)

1. In the **[!UICONTROL URIs]** text field, enter the following path, substituting your own domain and port number in the path, then press **[!UICONTROL Enter]** to add the path to the list:

   `https://<servername.domain>:<port_number>`

   For example, `https://1a2b3c.mycompany.com:4321`

   >[!NOTE]
   >
   >The URI path example above is hypothetical and for explanation purposes only.

1. Under the **[!UICONTROL Authorized redirect URIs]** heading, select ADD URI.
1. In the **[!UICONTROL URIs]** text field, enter the following path, substituting your own domain and port number in the path, then press **[!UICONTROL Enter]** to add the path to the list:

   `https://<servername.domain>:<port_number>/etc/cloudservices/youtube.youtubecredentialcallback.json`

   For example, `https://1a2b3c.mycompany.com:4321/etc/cloudservices/youtube.youtubecredentialcallback.json`

   >[!NOTE]
   >
   >The URI path example above is hypothetical and for explanation purposes only.

1. Near the bottom of the **[!UICONTROL Create OAuth client ID]** page, select **[!UICONTROL Create]**.
1. On the **[!UICONTROL OAuth client created]** dialog box, do the following:

   * (Optional) Copy the values in the **[!UICONTROL Your Client ID]** and **[!UICONTROL Your Client Secret]** fields, and save.
   * Select **[!UICONTROL DOWNLOAD JSON]**, then save the JSON file.

   You need this downloaded JSON file when you set up YouTube in Adobe Experience Manager later on.

   ![6_5_googleaccount-apis-oauthclientcreated](/help/assets/dynamic-media/assets/6_5_googleaccount-apis-oauthclientcreated.png)

1. On the **[!UICONTROL OAuth client created]** dialog box, select **[!UICONTROL OK]**.
1. Log out of your Google account. Now create a YouTube channel.

### Create a YouTube channel {#creating-a-youtube-channel}

Publishing videos to YouTube requires that you have one or more channels. If you have already created a YouTube channel, you can skip this task and go to [Add tags for publishing](/help/assets/dynamic-media/video.md#adding-tags-for-publishing).

>[!CAUTION]
>
>Be sure you have already set up one or more channels in YouTube *before* you add channels under YouTube Settings in Experience Manager (see [Set up YouTube in Experience Manager](#setting-up-youtube-in-aem) below). If you fail to do the channel setup, you are not warned of no existing channels. However, Google verification still occurs when you add a channel, but there is not an option to choose which channel the video is sent.

**To create a YouTube channel:**

1. Go to [https://www.youtube.com](https://www.youtube.com/) and sign in using your Google account credentials.
1. In the upper-right corner of the YouTube page, select your profile picture (it can also appear as a letter within a solid colored circle), then select **[!UICONTROL YouTube settings]** (round gear icon).
1. On the Overview page, under the Additional Features heading, select **[!UICONTROL See all my channels or create a channel]**.
1. On the Channels page, select **[!UICONTROL Create a new channel]**.
1. On the Brand Account page, in the Brand Account Name field, enter a company name or any other channel name you choose where you want to publish your video assets, then select **[!UICONTROL Create]**.

   Remember the name that you enter here; you must enter it again when you have to set up YouTube in Experience Manager.

1. (Optional) If necessary, add more channels.

   Now you add tags for publishing.

### Add tags for publishing {#adding-tags-for-publishing}

To publish to your videos to YouTube, Experience Manager associates tags to one or more YouTube channels. To add tags for publishing, see [Administer Tags](/help/sites-cloud/authoring/sites-console/tags.md).

Or, if you intend to use the default tags in Experience Manager, you can skip this task and go to [Set up YouTube in Experience Manager](#setting-up-youtube-in-aem).

>[!NOTE]
>
>After the Cloud Service is configured, other configuration is not required to enable the YouTube Publish replication agent at this point. The reason is because it was enabled when the Cloud Service configuration was saved.

<!-- ### Enabling the YouTube Publish replication agent {#enabling-the-youtube-publish-replication-agent}

After you enable the YouTube Publish replication agent, if you want to test the connection to the Google Cloud account, select **[!UICONTROL Test Connection]**. A browser tab displays the connection results. If you have added YouTube Channels, then a listing of those is displayed as part of the test.

1. In the upper-left corner of Experience Manager, select the Experience Manager logo, then in the left rail, navigate to **[!UICONTROL Tools]** > **[!UICONTROL Deployment]** > **[!UICONTROL Replication]** > **[!UICONTROL Agents on Author]**.
1. On the Agents of Author page, select **[!UICONTROL YouTube Publish (youtube)]**.
1. On the toolbar, to the right of Settings, select **[!UICONTROL Edit]**.
1. Select the **[!UICONTROL Enabled]** checkbox to turn on the replication agent.
1. Select **[!UICONTROL OK]**. -->

### Set up YouTube in Experience Manager {#setting-up-youtube-in-aem}

Starting with Experience Manager 6.4, a new touch user interface method was introduced to set up YouTube publishing in Experience Manager. Based on the installed instance of Experience Manager that you are using, do one of the following:

* To configure YouTube in Experience Manager before 6.4, see [Set up YouTube in Experience Manager before 6.4](/help/assets/dynamic-media/video.md#setting-up-youtube-in-aem-before).
* To configure YouTube in Experience Manager 6.4 or later, see [Set up YouTube in Experience Manager 6.4 and later](#setting-up-youtube-in-aem-and-later).

#### Set up YouTube in Experience Manager 6.4 and later {#setting-up-youtube-in-aem-and-later}

1. Be sure you log in to your instance of Dynamic Media as an Administrator.
1. In the upper-left corner of Experience Manager, select the Experience Manager logo, then in the left rail, navigate to **[!UICONTROL Tools]**(hammer icon) > **[!UICONTROL Cloud Services]** > **[!UICONTROL YouTube Publishing Configuration]**.
1. Select **[!UICONTROL global]** (do not select it).

1. Near the upper-right corner of the global page, select **[!UICONTROL Create]**.
1. On the Create YouTube Configuration page, under Google Cloud Platform Settings, in the **[!UICONTROL Application Name]** field, enter the Google Project ID.

   You specified the project ID when you initially configured Google Cloud settings earlier.
   Leave the Create YouTube Configuration page open; you are returning to it in a moment.

   ![6_5_youtubepublish-createyoutubeconfiguration](/help/assets/dynamic-media/assets/6_5_youtubepublish-createyoutubeconfiguration.png)

1. Using a plain text editor, open the JSON file that you downloaded and saved earlier in the task [Configure Google Cloud settings](/help/assets/dynamic-media/video.md#configuring-google-cloud-settings).
1. Select and copy the entire JSON text.
1. Return to the YouTube Account Settings dialog box. In the **[!UICONTROL JSON Config]** field, paste the JSON text.
1. Near the upper-right corner of the page, select **[!UICONTROL Save]**.

   Now set up YouTube channels in Experience Manager.

1. Select **[!UICONTROL Add Channel]**.
1. In the Channel Name field, enter the name of the channel that you created in the task **[!UICONTROL Adding one or more channels to YouTube]** earlier.

   You can optionally add a description, if desired.

1. Select **[!UICONTROL Add]**.
1. YouTube/Google verification is displayed. If you are not already logged into the Google Cloud account, then skip this step.

    * Enter the Google username and password associated with the Google Project ID and the JSON text above.
    * Depending on how many channels your account has you see two or more items. Select a channel. Do not select the e-mail address; it is not a channel.
    * On the next page, select **[!UICONTROL Accept]** to allow access to this channel.

1. Select **[!UICONTROL Allow]**.

   Now set up tags for publishing.

1. **[!UICONTROL Setting up tags for publishing]** - On the Cloud Services > YouTube page, select the pencil icon to edit the list of tags that you want to use.
1. To display the list of available tags in Experience Manager, select the drop-down list icon (upside-down caret).
1. To add them, select one or more tags.

   To delete a tag that you have added, select the tag, and select **[!UICONTROL X]**.

1. When you are finished adding the tags that you want, select **[!UICONTROL Save]**.

   Now you publish videos to your YouTube channel.

#### Set up YouTube in Experience Manager before 6.4 {#setting-up-youtube-in-aem-before}

1. Be sure you log in to your instance of Dynamic Media as an Administrator.

1. In the upper-left corner of Experience Manager, select the Experience Manager logo, then in the left rail, navigate to **[!UICONTROL Tools]** (hammer icon) > **[!UICONTROL Deployment]** > **[!UICONTROL Cloud Services]**.
1. Under the Third-Party Services heading, under YouTube, select **[!UICONTROL Configure now]**.
1. In the Create Configuration dialog box, enter a title (mandatory) and name (optional) in the respective fields.
1. Select **[!UICONTROL Create]**.
1. In the YouTube Account Settings dialog box, in the **[!UICONTROL Application Name]** field, enter the Google Project ID.

   You specified the project ID when you initially [configured Google Cloud settings](/help/assets/dynamic-media/video.md#configuring-google-cloud-settings) earlier.
   Leave the YouTube Account Setting dialog box open; you are returning to it in a moment.

1. Using a plain text editor, open the JSON file that you downloaded and saved earlier in the task Configuring Google Cloud settings.
1. Select and copy the entire JSON text.
1. Return to the YouTube Account Settings dialog box. In the **[!UICONTROL JSON Config]** field, paste the JSON text.
1. Select **[!UICONTROL OK]**.

   Now set up YouTube channels in Experience Manager.

1. To the right of **[!UICONTROL Available Channels]**, select **+** (plus sign icon).
1. In the YouTube Channel Settings dialog box, in the Title field, enter the name of the channel that you created in the task **[!UICONTROL Adding one or more channels to YouTube]** earlier.

   You can optionally add a description, if desired.

1. Select **[!UICONTROL OK]**.
1. YouTube/Google verification is displayed. If you are not already logged into the Google Cloud account, then skip this step.

    * Enter the Google username and password associated with the Google Project ID and the JSON text above.
    * Depending on how many channels your account has you see two or more items. Select a channel. Do not select the e-mail address; it is not a channel.
    * On the next page, select **[!UICONTROL Accept]** to allow access to this channel.

1. Select **[!UICONTROL Allow]**.

   Now set up tags for publishing.

1. **[!UICONTROL Setting up tags for publishing]** - On the Cloud Services > YouTube page, select the pencil icon to edit the list of tags that you want to use.
1. To display the list of available tags in Experience Manager, select the drop-down list icon (upside-down caret).
1. To add them, select one or more tags.

   To delete a tag that you have added, select the tag, and select **X**.

1. When you are finished adding the tags that you want, select **[!UICONTROL OK]**.

   Now you publish videos to your YouTube channel.

### (Optional) Automate the setting of default YouTube properties for your uploaded videos {#optional-automating-the-setting-of-default-youtube-properties-for-your-uploaded-videos}

You can optionally automate the setting of YouTube properties on upload of your videos. Create a metadata processing profile in Experience Manager.

To create the metadata processing profile, you are first going to copy values from the **[!UICONTROL Field Label]**, **[!UICONTROL Map to property]**, and **[!UICONTROL Choices]** fields, all found in Metadata Schemas for video. Then, you build your YouTube video metadata processing profile by adding those values to it.

**To automate the setting of default YouTube properties for your uploaded videos:**

1. In the upper-left corner of Experience Manager, select the Experience Manager logo, then in the left rail, navigate to **[!UICONTROL Tools]** (hammer icon) > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Schemas]**.
1. Select **[!UICONTROL default]**. (Do not add a checkmark to the selection box to the left of "default".)
1. On the **[!UICONTROL default]** page, check the box to the left of **[!UICONTROL video]**, then select **[!UICONTROL Edit]**.
1. On the Metadata Schema Editor page, select the **[!UICONTROL Advanced]** tab.
1. Under the YouTube Publishing heading, select **[!UICONTROL YouTube Category]**.
1. On the right side of the page, under the **[!UICONTROL Settings]** tab, do the following:

    * In the **[!UICONTROL Map to property]** text field, select and copy the value.
      Paste the copied value into the open text editor. You are going to need this value later when you create your metadata processing profile. Leave the text editor open.

    * Under **[!UICONTROL Choices]**, select and copy the default value that you want to use (such as People & Blogs or Science & Technology).
      Paste the copied value into the open text editor. You are going to need this value later when you create your metadata processing profile. Leave the text editor open.

1. Under the YouTube Publishing heading, select **[!UICONTROL YouTube Privacy]**.
1. On the right side of the page, under the **[!UICONTROL Settings]** tab, do the following:

    * In the **[!UICONTROL Map to property]** text field, select and copy the value.
      Paste the copied value into the open text editor. You are going to need this value later when you create your metadata processing profile. Leave the text editor open.

    * Under **[!UICONTROL Choices]**, select and copy the default value that you want to use. Notice that the Choices are grouped in pairs of two. The bottom field in the pair is the default value that you want to copy, such as public, unlisted, or private.
      Paste the copied value into the open text editor. You are going to need this value later when you create your metadata processing profile. Leave the text editor open.

1. Near the upper-right corner of the Metadata Schema Editor page, select **[!UICONTROL Cancel]**.
1. In the upper-left corner of Experience Manager, select the Experience Manager logo, then in the left rail, select **[!UICONTROL Tools]** (hammer icon) > **[!UICONTROL Assets]** > **[!UICONTROL Metadata Profiles]**.

1. On the Metadata Profiles page, near the upper-right corner of the page, select **[!UICONTROL Create]**.
1. In the Add Metadata Profile dialog box, in the **[!UICONTROL Profile title]** text field, enter the name `YouTube Video` then select **[!UICONTROL Create]**.
1. On the Metadata Profile Editor page, select the **[!UICONTROL Advance]** tab.
1. Add the copied YouTube Publishing values to the profile by doing the following:

    * On the right side of the page, select the **[!UICONTROL Build Form]** tab.
    * (Optional) Drag the component labeled **[!UICONTROL Section Header]** to the left and drop it in the form area.
    * (Optional) Select **[!UICONTROL Field Label]** to select the component.
    * (Optional) On the right side of the page, under the Settings tab, in the Field Label text field, enter `YouTube Publishing`.
    * Select the **[!UICONTROL Build Form]** tab, then drag the component labeled **[!UICONTROL Multi Value Text]** and drop it below the **[!UICONTROL YouTube Publishing]** heading that you created.

    * To select the component, select **[!UICONTROL Field Label]**.
    * On the right side of the page, under the Settings tab, paste the YouTube Publishing values (Field Label value and Map to property value) that you copied earlier, into their respective fields on the form. Paste the Choices value into the Default Value field.

1. Add the copied YouTube Privacy values to the profile by doing the following:

    * On the right side of the page, select the **[!UICONTROL Build Form]** tab.
    * (Optional) Drag the component labeled **[!UICONTROL Section Header]** to the left and drop it in the form area.
    * (Optional) Select **[!UICONTROL Field Label]** to select the component.
    * (Optional) On the right side of the page, under the Settings tab, in the Field Label text field, enter `YouTube Privacy`.
    * Select the **[!UICONTROL Build Form]** tab, then drag the component labeled **[!UICONTROL Multi Value Text]** and drop it below the **[!UICONTROL YouTube Privacy]** heading you created.

    * To select the component, select **[!UICONTROL Field Label]**.
    * On the right side of the page, under the Settings tab, paste the YouTube Publishing values (Field Label value and Map to property value) that you copied earlier, into their respective fields on the form. Paste the Choices value into the Default Value field.

1. Near the upper-right corner of the page, select **[!UICONTROL Save]**.
1. Apply the YouTube Publishing metadata profile to the folders where you are going to upload videos. You must have both the Metadata Profile and the Video Profile set.

   See [Metadata Profiles](/help/assets/metadata-profiles.md) and [Video Profiles](/help/assets/dynamic-media/video-profiles.md).

### Publish videos to your YouTube channel {#publishing-videos-to-your-youtube-channel}

Now you associate the tags that you added earlier to video assets. This process lets Experience Manager know which assets to publish to your YouTube channel.

>[!NOTE]
>
>Publish immediately does not automatically publish to YouTube. When Dynamic Media is set up, there are two publish options to choose from: **[!UICONTROL Immediately]** or **[!UICONTROL Upon Activation]**.
>
>**[!UICONTROL Publish Immediately]** means that the uploaded asset&ndash;after it is synched with IPS&ndash;is published automatically to the delivery system. While that is true for Dynamic Media, it is not true for YouTube. To publish to YouTube, you must publish by way of Experience Manager Author.

>[!NOTE]
>
>To publish content from YouTube, Experience Manager uses the **[!UICONTROL Publish to YouTube]** workflow, which lets you monitor progress and view any failure information.
>
>See [Monitor video encoding and YouTube publishing progress](#monitoring-video-encoding-and-youtube-publishing-progress).
>
>For more detailed progress information, you can monitor the YouTube log under replication. Be aware, however, that such monitoring requires Administrator access.

**To publish videos to your YouTube channel:**

1. In Experience Manager, navigate to a video asset that you want to publish to your YouTube channel.
1. Select the video asset (the adaptive video set).
1. On the toolbar, select **[!UICONTROL Properties]**.
1. In the Basic tab, under the Metadata heading, select **[!UICONTROL Open Selection Dialog]** to the right of the Tags field.
1. On the Select Tags page, navigate to the tags you want to use, and then select one or more tags.

   Remember that the tags must be associated with the YouTube channel.

1. In the upper-right corner of the page, select **[!UICONTROL Select]**.
1. In the upper-right corner of the video's properties page, select **[!UICONTROL Save and Close]**.
1. On the toolbar, select **[!UICONTROL Quick Publish]**.

   See also [Use Publication Management with Experience Manager Sites](https://experienceleague.adobe.com/docs/experience-manager-learn/sites/page-authoring/publication-management-feature-video-use.html#page-authoring).

   You can optionally verify the published video on your YouTube channel.

### (Optional) Verify the published video on YouTube {#optional-verifying-the-published-video-on-youtube}

You can optionally monitor progress of your YouTube publishing (or unpublishing).

See [Monitor video encoding and YouTube publishing progress](#monitoring-video-encoding-and-youtube-publishing-progress).

Publishing times can vary greatly depending on numerous factors that include the format of your primary source video, file size, and upload traffic. The publishing process can take anywhere from a few minutes to several hours. Also, higher resolution formats are rendered much more slowly. For example, 720p and 1080p take longer to appear than 480p.

After eight hours, if you still see a status message that says **[!UICONTROL Uploaded (processing, please wait)]**, try removing the video from your site and uploading it again.

### Link YouTube URLs to your Web Application {#linking-youtube-urls-to-your-web-application}

You can obtain a YouTube URL string that is generated by Dynamic Media after you publish the video. When you copy the YouTube URL, it lands on the Clipboard so you can paste it as necessary to pages in your website or application.

>[!NOTE]
>
>The YouTube URL is not available to copy until you have published the video asset to YouTube.

To link YouTube URLs to your web application:

1. Navigate to the *YouTube published* video asset whose URL that you want to copy, then select it.

   Remember that YouTube URLs are only available to copy *after* you have first *published* the video assets to YouTube.

1. On the toolbar, select **[!UICONTROL Properties]**.
1. Select the **[!UICONTROL Advanced]** tab.
1. Under the YouTube Publishing heading, in the YouTube URL List, select, and copy the URL text to your web browser to preview the asset or to add to your web content page.

### Unpublish videos so you can remove them from YouTube {#unpublishing-videos-to-remove-them-from-youtube}

When you unpublish a video asset in Experience Manager, the video is removed from YouTube.

>[!CAUTION]
>
>If you remove a video directly from within YouTube, Experience Manager is unaware and continues to behave as if the video is still published to YouTube. Always unpublish a video asset from YouTube by way of Experience Manager.

>[!NOTE]
>
>To remove content from YouTube, Experience Manager uses the **[!UICONTROL Unpublish from YouTube]** workflow, which lets you monitor progress and view any failure information.
>
>See [Monitor video encoding and YouTube publishing progress](#monitoring-video-encoding-and-youtube-publishing-progress).

**To unpublish videos to remove them from YouTube:**

1. Navigate to the video assets that you want to unpublish from your YouTube channel.
1. In an asset selection mode, select one or more published video assets.
1. On the toolbar, select **[!UICONTROL Manage Publication]**. If necessary, select the three dots icon (`. . .`) on the toolbar to see **[!UICONTROL Manage Publication]**.
1. On the Manage Publication page, select **[!UICONTROL Unpublish]**.
1. In the upper-right corner of the page, select **[!UICONTROL Next]**.
1. In the upper-right corner of the page, select **[!UICONTROL Unpublish]**.

## Monitor video encoding and YouTube publishing progress {#monitoring-video-encoding-and-youtube-publishing-progress}

When you upload a new video to a folder that has video encoding applied or, you publish your video to YouTube, monitor how your video encoding/Youtube publishing is progressing (or failing). Actual YouTube publishing progress is only available by way of the logs. But whether it fails or succeeds, it is listed in other ways described in the following procedure. In addition, you receive email notifications when a YouTube publish workflow or video encoding completes or is interrupted.

### Monitor progress {#monitoring-progress}

You can monitor progress, including failed encoding/YouTube publish.

1. View video-encoding progress in your assets folder:

    * In card view, video encoding progress displays on the asset by percent. If there is an error, this information also displays on the asset.

   ![chlimage_1-429](/help/assets/dynamic-media/assets/chlimage_1-429.png)

    * In list view, video encoding progress displays in the **[!UICONTROL Processing Status]** column. If there is an error, this message displays in that same column.

   ![chlimage_1-430](/help/assets/dynamic-media/assets/chlimage_1-430.png)

   This column does not display by default. To enable the column, select **[!UICONTROL View Settings]** from the views drop-down menu, and add the **[!UICONTROL Processing Status]** column and select **[!UICONTROL Update]**.

   ![chlimage_1-431](/help/assets/dynamic-media/assets/chlimage_1-431.png)

1. View progress in the asset details. When you select an asset, open the drop-down menu and select **[!UICONTROL Timeline]**. To narrow it down to workflow activities like encoding or YouTube publishing, select **[!UICONTROL Workflows]**.

   ![chlimage_1-432](/help/assets/dynamic-media/assets/chlimage_1-432.png)

   Any workflow information--such as encoding--displays in the timeline. For YouTube publish, the Workflow timeline also includes the name of the YouTube channel and the YouTube video URL. In addition, you see any failure notifications in the Workflow timeline after the publish is complete.

   >[!NOTE]
   >
   >It can take a long time for failure/error messages to finally be recorded due to multiple workflow configurations on **[!UICONTROL retries]**, **[!UICONTROL retry delay]**, and **[!UICONTROL timeout]** from [https://localhost:4502/system/console/configMgr](https://localhost:4502/system/console/configMgr), for example:
   >
   >* Apache Sling Job Queue Configuration
   >* Adobe Granite Workflow External Process Job Handler
   >* Granite Workflow Timeout Queue
   >
   >You can adjust the **[!UICONTROL retries]**, **[!UICONTROL retry delay]**, and **[!UICONTROL timeout]** properties in these configurations.

1. For workflows in progress, see Workflow Instances available from **[!UICONTROL Tools]** > **[!UICONTROL Workflow]** > **[!UICONTROL Instances]**.

   >[!NOTE]
   >
   >You need administrative rights to access the **[!UICONTROL Tools]** menu.

   ![chlimage_1-433](/help/assets/dynamic-media/assets/chlimage_1-433.png)

   Select the instance and select **[!UICONTROL Open History]**.

   ![chlimage_1-434](/help/assets/dynamic-media/assets/chlimage_1-434.png)

   From the Workflow Instances area, you can also suspend, terminate, or rename workflows. See [Administer workflows](/help/sites-cloud/authoring/workflows/overview.md) for more information.

1. For failed jobs, see Workflow Failures available from **[!UICONTROL Tools]** > **[!UICONTROL Workflow]** > **[!UICONTROL Failures]**. The **[!UICONTROL Workflow Failure]** lists all failed workflow activities.

   >[!NOTE]
   >
   >You need administrative rights to access the **[!UICONTROL Tools]** menu.

   ![chlimage_1-435](/help/assets/dynamic-media/assets/chlimage_1-435.png)

   >[!NOTE]
   >
   >It can take a long time for the error message to finally be recorded due to multiple workflow configurations on **[!UICONTROL retries]**, **[!UICONTROL retry delay]**, and **[!UICONTROL timeout]** from [https://localhost:4502/system/console/configMgr](https://localhost:4502/system/console/configMgr), for example:
   >
   >* Apache Sling Job Queue Configuration
   >* Adobe Granite Workflow External Process Job Handler
   >* Granite Workflow Timeout Queue
   >
   >You can adjust the **[!UICONTROL retries]**, **[!UICONTROL retry delay]**, and **[!UICONTROL timeout]** properties in these configurations.

1. For completed workflows, see Workflow Archive available from **[!UICONTROL Tools]** > **[!UICONTROL Workflow]** > **[!UICONTROL Archive]**. The **[!UICONTROL Workflow Archive]** lists all completed workflow activities.

   >[!NOTE]
   >
   >You need administrative rights to access the **[!UICONTROL Tools]** menu.

   ![chlimage_1-436](/help/assets/dynamic-media/assets/chlimage_1-436.png)

1. You receive email notifications about aborted or failed workflow jobs. These email notifications are configurable by an administrator. See [Configure email notifications](#configuring-e-mail-notifications).

<!-- EMAIL NOT AVAILABLE IN SKYLINE

#### Configuring e-mail notifications {#configuring-e-mail-notifications}

>[!NOTE]
>
>You may need administrative rights to access the **[!UICONTROL Tools]** menu.

How you configure notification depends on whether you want notifications for YouTube publishing jobs.

* For encoding jobs, you can access the configuration page for all Experience Manager workflow email notifications at **[!UICONTROL Tools]** > **[!UICONTROL Operations]** > **[!UICONTROL Web Console]** and by searching for **[!UICONTROL Day CQ Workflow Email Notification Service]**. You can select or clear the check boxes for **[!UICONTROL Notify on Abort]** or **[!UICONTROL Notify on Complete]** accordingly.

For YouTube publishing jobs, do the following:

1. In Experience Manager, navigate to **[!UICONTROL Tools]** > **[!UICONTROL Workflow]** > **[!UICONTROL Models]**.
1. On the Workflow Models page, select **[!UICONTROL Publish to YouTube]**, then select **[!UICONTROL Edit]** on the toolbar.
1. Near the upper-right corner of the Publish to YouTube workflow page, select **[!UICONTROL Edit]**.
1. Hover the mouse pointer on the YouTube Upload component, then select once to display the inline toolbar.

   ![6_5_publishtoyoutubeworkflow](assets/6_5_publishtoyoutubeworkflow.png)

1. On the inline toolbar, select the Configuration icon (wrench). Select the **[!UICONTROL Arguments]** tab.

   ![6_5_publishtoyoutubeworkflow-configurationicon](assets/6_5_publishtoyoutubeworkflow-configurationicon.png)

1. In the YouTube Upload Process - Step Properties dialog box, select the **[!UICONTROL Arguments]** tab.

   ![6_5_publishtoyoutubeworkflow-arguments-tab](assets/6_5_publishtoyoutubeworkflow-arguments-tab.png)

1. You can select or clear the following check boxes:

    * Publish Start
    * Publish Failure
    * Publish Completion - includes information on channels and URLs

   Clearing a check box means that you will not receive the specified email notification from the YouTube Publish workflow.

   >[!NOTE]
   >
   >These emails are specific to YouTube and are in addition to the generic workflow email notifications. As a result, you may receive two sets of email notification - the generic notification available in the **[!UICONTROL Day CQ Workflow Email Notification Service]** and one specific to YouTube depending on your configuration settings.

1. When you are finished, near the upper-right corner of the dialog box, select the **[!UICONTROL Done]** icon (check mark).
1. On the Publish to YouTube workflow page, near the upper-right corner, select **[!UICONTROL Sync]**.

-->

## Transcode using Processing Profile {#transcode-video}

[!DNL Experience Manager] as a [!DNL Cloud Service] lets you do basic transcoding of MP4 video files using Processing Profiles. The functionality lets you not just upload but also preview and scale a MP4 video file.

![Create Processing Profile for video transcoding in [!DNL Experience Manager]](assets/video-processing-profile-for-mp4.png)

*Figure: A Processing Profile for video transcoding in [!DNL Experience Manager].*

If you provide only width or only height and leave the other field blank, the renditions maintain the aspect ratio. H.264 video codec is available for transcoding.

To process assets using a processing profile, add a profile to a folder. See [use processing profiles to process assets](/help/assets/asset-microservices-configure-and-use.md#use-profiles).

## Annotate video assets {#annotate-video-assets}

You can add annotations to video assets. While annotating videos, the player pauses to let you annotate on a frame. For details, see [managing video assets](manage-video-assets.md). 

>[!NOTE]
>
>MXF video format is not yet supported with video asset annotations.

1. From the [!DNL Assets] console, select **[!UICONTROL Edit]** on the asset card to display the asset details page.
1. To play the video, click **[!UICONTROL Preview]**.
1. To annotate the video, click **[!UICONTROL Annotate]**. An annotation is added at the particular time (frame) in the video. When annotating, you can draw on the canvas and include a comment with the drawing. Comments are auto-saved. To exit the annotation wizard, click **[!UICONTROL Close]**.
1. Seek to a specific point in the video, specify the time in seconds in the **text** field and click **Jump**. For example, to skip the first 20 seconds of video, enter 20 in the text field.
1. To view it in the timeline, click an annotation. To delete the annotation from the timeline, click **[!UICONTROL Delete]**.

## Best practices and limitations {#tips-limitations}

* Without [!DNL Dynamic Media] license, you can only process MP4 files using processing profiles.
* When transcoding MP4 files using Processing Profiles, the following guidelines and limitations apply:

  * Apple ProRes files can only transcode to a maximum resolution of 1080p.
  * If the source file has a bitrate >200 Mbps, you can only transcode to a maximum resolution of 1080p.
  * If the source framerate >=60 fps then, the maximum size of the source file that you can use is,

    * 400 MB for 4k transcoding.
    * 800 MB for 1080p transcoding.
    * 8 GB for 720p transcoding.

  * Maximum file size you can transcode to 4k resolution is 2.55 GB MP4 file of 4k resolution, 12 Mbps bitrate, and 23 fps.

  **See also**

* [Translate Assets](translate-assets.md)
* [Assets HTTP API](mac-api-assets.md)
* [Assets supported file formats](file-format-support.md)
* [Search assets](search-assets.md)
* [Connected assets](use-assets-across-connected-assets-instances.md)
* [Asset reports](asset-reports.md)
* [Metadata schemas](metadata-schemas.md)
* [Download assets](download-assets-from-aem.md)
* [Manage metadata](manage-metadata.md)
* [Search facets](search-facets.md)
* [Manage collections](manage-collections.md)
* [Bulk metadata import](metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)

>[!MORELIKETHIS]
>
>* [Dynamic Media video documentation](/help/assets/dynamic-media/video.md).
>* [Know more about use, types, and configuration of processing profiles](/help/assets/asset-microservices-configure-and-use.md).
