---
title: Share Assets and Collections in [!DNL the Content Hub]
description: Share Assets and Collections in [!DNL the Content Hub]
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 5284d229-1596-40bf-aa5f-af4b6500ebdf
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---
# Share assets and collections in Content Hub {#search-assets-collections-as-a-link}

Create a link to selected assets and collections to share them with others easily. As an authorized [!DNL Content Hub] user, select one or more assets and collections available in your [!DNL Content Hub] environment, generate a link, and send it to other private or public users.

>[!VIDEO](https://video.tv.adobe.com/v/3474890/?learn=on&enablevpops=on){transcript=true}

>[!IMPORTANT]
>
>This feature is available as a Limited Availability feature. You can [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) to enable it for your deployment. 

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

   If you want to update the link details such as title, description, password, delete or copy the link, click more options (![List](/help/assets/assets/List.svg)) and select the appropriate option. 

   ![customize](/help/assets/assets/customize.png)

   

   >[!NOTE]
   > 
   > [Enable public link sharing from the configuration page](/help/assets/configure-content-hub-ui-options.md#enable-public-link-sharing) so that the **[!UICONTROL Public Link]** toggle appears on the **[!UICONTROL Share assets]** dialog box. Without enabling this configuration, the **[!UICONTROL Public Link]** toggle does not display.

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

### What does sharing assets in AEM Assets [!DNL Content Hub] mean?

Sharing assets in **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]** **enables authorized users to share one or more assets, or entire collections, by generating a shareable link**. This link grants recipients direct access to **view and download** the selected assets, streamlining distribution without requiring recipients to navigate the full [!DNL Content Hub] environment. Because access is delivered through a single link, teams can quickly circulate approved brand assets, marketing materials, and creative files to internal and external stakeholders alike.

**Recipient types for a shared link include:**

- **Private users** — recipients who must sign in to access the shared assets, ensuring controlled, authenticated access.
- **Public users** — recipients who can access the assets as guests without signing in.

This dual-recipient approach makes link-based sharing flexible for a range of collaboration needs: private sharing supports secure, permission-controlled workflows, while public sharing supports broad, frictionless distribution to audiences outside the organization. As a result, authorized users can tailor how each set of assets is shared, distributed, and consumed.

### How do I share assets or collections with others using AEM Assets [!DNL Content Hub]?

Sharing assets or collections in **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]** generates a **shareable link** that you can distribute to team members or stakeholders. The process uses the built-in **Share** feature, which lets you control exactly what is shared, who can access it, and for how long.

#### Steps to Share Assets or Collections

1. Open the **[!DNL Content Hub] homepage**.
2. Select one or more assets. To share a collection instead, go to the **Collections** tab and select the collection.
3. Click the **Share icon** to open the **Share dialog**.
4. In the dialog, **preview the selected assets** and remove any that should not be included.
5. Add a **title** and **description** to give recipients context about the shared content.
6. Choose who can access the link by setting it to **private or public**.
7. Set an **expiration period** for the link.
8. Click **Get Link** to generate the shareable URL, which is automatically copied for you to distribute.

#### Sharing Options Explained

- **Access control (private or public):** Selecting **private or public** determines who can open the link, allowing you to restrict access to intended recipients or make the assets openly accessible.
- **Expiration period:** Setting an **expiration period** creates a time-limited link, which helps ensure shared assets are no longer accessible after they are no longer needed.
- **Title and description:** Adding a title and description helps recipients quickly understand what the shared assets or collection contain.

Once generated with **Get Link**, the shareable URL can be sent directly to team members or stakeholders for review, collaboration, or distribution.

### What access options are available when sharing assets in AEM Assets [!DNL Content Hub], and how do they differ?

Adobe Experience Manager (AEM) Assets [!DNL Content Hub] provides **two access options** for shared links: **private links** and **public links**. This lets users and administrators choose the appropriate level of control each time an asset is shared, balancing security against ease of distribution. The two options differ primarily in whether recipients must sign in and in how their link expiration is configured.

#### Private Links: Secure, Sign-In Required

**Private links** require recipients to sign in to their [!DNL Content Hub] environment before they can view and download assets. This provides added security, because access is restricted to authenticated members of [!DNL the Content Hub] environment rather than anyone who happens to obtain the link. Private links use **custom expiration dates**, allowing the person sharing the asset to define exactly how long access remains valid.

Private links are best suited for sharing sensitive, unreleased, or internal assets where controlling exactly who can access the content is essential.

#### Public Links: Open Access via Link

**Public links** can be accessed by anyone who has the link, without requiring sign-in. This makes public links the faster, more convenient option for broad distribution to external recipients or collaborators who do not have [!DNL Content Hub] access. Public links carry their own expiration settings, typically ranging from **24 hours to one week**, ensuring that open access is time-limited rather than permanent.

Public links are ideal for quickly distributing approved, non-sensitive assets to a wide audience.

#### Private vs Public Links: Key Differences

The two access options contrast across three dimensions:

- **Authentication:** Unlike public links, private links require recipients to sign in to their [!DNL Content Hub] environment, while public links are accessible to anyone with the link and require no sign-in.
- **Security:** Private links offer added security by limiting access to authenticated users; public links prioritize convenience and open reach.
- **Expiration:** Private links use **custom expiration dates** set by the sharer, whereas public links use preset windows such as **24 hours to one week**.

Choosing between private and public links depends on the balance a user needs between security and ease of access for each shared asset.

### Is there any configuration managed by administrator to be able to generate public links for assets in AEM Assets [!DNL Content Hub]?

Yes. Administrators control the generation of public links for assets in **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]** through the **Enable Public Link** toggle, located in the **Collections and Sharing** tab of the **Configuration UI**. Enabling or disabling this toggle determines whether public links can be generated for assets.

To locate and set this control:

1. Open the **Configuration UI** in AEM Assets [!DNL Content Hub].
2. Navigate to the **Collections and Sharing** tab.
3. Enable or disable the **Enable Public Link** toggle.

**Enable Public Link** is an administrator-managed setting, which means the ability to create public links is governed centrally rather than left to individual users. When the toggle is enabled, users can generate public links to share assets. When it is disabled, public link generation is turned off across [!DNL the Content Hub].

This centralized control allows administrators to align public link sharing with organizational governance and security requirements, ensuring that assets are only shared publicly when explicitly permitted.

### Can I set expiration dates for shared asset links in AEM Assets [!DNL Content Hub], and why is this important?

Yes — you can set expiration dates for both private and public shared asset links in **Adobe Experience Manager (AEM) Assets [!DNL Content Hub]**. This feature gives content owners direct control over how long a shared link remains active, ensuring assets are accessible only for the intended window.

#### Expiration Options for Public vs. Private Links

[!DNL Content Hub] applies different expiration controls depending on the link type:

- **Public links:** Choose from preset durations ranging from **24 hours up to one week**.
- **Private links:** Select from the available **presets**, or define a **custom expiration date** for more precise control over the sharing window.

Unlike public links, which are limited to fixed presets, private links add the flexibility of a fully custom expiration date, giving you finer control over exactly when access ends.

#### Why Setting Expiration Dates Matters

Expiration dates are important because they enforce automatic access control. **Once a link expires, it can no longer be used to access or download the assets.** As a result, expired links cannot be forwarded, reused, or exploited after the intended sharing period ends. This directly helps maintain the **security and control** of your content, reducing the risk of unauthorized distribution and limiting the exposure of sensitive or brand-restricted assets over time.

By pairing preset and custom expiration windows with public and private sharing, AEM Assets [!DNL Content Hub] allows teams to distribute assets externally while ensuring access does not persist longer than necessary.

### What can recipients do with the shared asset link created using AEM Assets [!DNL Content Hub], and are there options for downloading different renditions?

Recipients of a shared asset link can **preview, select, and download** assets directly in their web browser, with no application installation or account login required. Adobe Experience Manager (AEM) Assets [!DNL Content Hub] generates the link so that anyone who receives it can access the shared content immediately.

Recipients who receive a shared asset link can:

* **Open the link in a browser** to preview the shared assets.
* **Select the specific assets** they need from the shared collection.
* **Download the selected assets**, delivered together as a single **zip file**.
* **View asset metadata** by clicking the asset thumbnail.

**Downloading different renditions:** If asset renditions are enabled in AEM Assets [!DNL Content Hub], recipients choose which **renditions** they want to download. A rendition is an alternate version of the same source asset, such as the **Original** (the full, unmodified file) or a **Static** rendition. This lets recipients retrieve the exact format that fits their intended use rather than being limited to a single output. The assets and their selected renditions are packaged and downloaded together as a **zip file**, and recipients view metadata by clicking the asset thumbnail.

The link remains functional until its set **expiration date**, after which access is automatically revoked. This time-limited access ensures that shared content is available only for the intended window, giving asset owners controlled, secure distribution of their files.


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
