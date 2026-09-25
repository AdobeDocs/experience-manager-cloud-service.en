---
title: Share Assets in [!DNL the Content Hub]
description: Share Assets in [!DNL the Content Hub]
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 5284d229-1596-40bf-aa5f-af4b6500ebdf
---
# Share assets in [!DNL Content Hub] {#search-assets-as-a-link}

[!DNL Content Hub] enables authorized users to share one or more selected assets by generating a shareable **link**. As an authorized [!DNL Content Hub] user, you select the assets you want to distribute, generate a link, and send that link to both **private users** (internal, authenticated collaborators) and **public users** (external recipients).

Sharing via a **link** is one of the most efficient ways to distribute digital assets. This eliminates the need to download and re-upload files, ensuring recipients access the exact assets stored in your [!DNL Content Hub] environment.

## How to share assets as a link

To share selected assets with others, follow these steps:

1. **Sign in** as an authorized [!DNL Content Hub] user with access to your [!DNL Content Hub] environment.
2. **Select one or more assets** available in your [!DNL Content Hub] environment that you want to share.
3. **Generate a link** for the selected assets.
4. **Send the generated link** to other **private or public users** so they can access the shared assets.

## Practical uses of link-based sharing

Sharing assets as a **link** supports common collaboration and distribution needs, including:

- **Distributing assets to external partners or clients** without granting them full access to your [!DNL Content Hub] environment.
- **Sharing with internal team members** who need quick access to specific approved assets.
- **Sending a single, self-contained link** rather than transferring large files by email or other means.

Because the shared assets remain hosted within your [!DNL Content Hub] environment, recipients always receive the current, authorized version of each asset through the generated link.

>[!VIDEO](https://video.tv.adobe.com/v/3474890/?learn=on&enablevpops=on){transcript=true}

## Prerequisites {#prerequisites}

**[!DNL Content Hub] users** — that is, individuals who have been onboarded to [!DNL Content Hub] — can create a shareable **link** to specific **assets** selected from [!DNL the Content Hub] library and distribute it to other users. See [Content Hub users](deploy-content-hub.md#onboard-content-hub-users) for details on onboarding.

Link-based sharing is the standard mechanism for distributing assets, because it allows recipients to access the selected content directly without needing to locate the assets themselves. This streamlines collaboration and asset distribution across teams and with external stakeholders, ensuring the right people can reach the right assets efficiently.

## Share assets {#share-assets}

To share one or more assets with private or public users, execute the following steps:

1. Navigate to your [!DNL Content Hub] homepage, select one or more assets and click ![share](/help/assets/assets/share.svg) **[!UICONTROL Share]** to display a single selected asset or a list of multiple selected assets in the **[!UICONTROL Share assets]** dialog box. This dialog box aggregates the assets you have chosen so you can review the complete set before sharing.

   You can also select and share assets available in ![collections](/help/assets/assets/Smock_Collection_18_N.svg) **[!UICONTROL Collections]**.

1. View an asset or review the list of assets available in **[!UICONTROL Share assets]** dialog box. Click ![unselect](/help/assets/assets/Close.svg) next to an asset to remove that asset from the list. This step refines the final set of assets included in the share before you generate the link.

1. Specify a title and an optional description that defines the set of selected assets. A clear title and description help recipients identify the shared set at a glance.

1. Select **[!UICONTROL Period of expiration]**. This setting determines how long the shared link remains valid before access expires.

1. Under **[!UICONTROL Who can access]** drop down, select the access options and click **[!UICONTROL Get Link]** to generate a link to share with the selected users. This action produces the shareable link based on the access level you choose. The two access levels differ as follows:

   - **Private users** must sign in to their [!DNL Content Hub] environment to access the shared assets page.
   - **Public users** access the shared assets page as guests, without signing in to [!DNL Content Hub].

   <!--1. Select a **[!UICONTROL period of expiration]** and click **[!UICONTROL Get Link]** to generate a link to share with private users. Private users sign in to their [!DNL Content Hub] environment to access the shared assets page.-->

   ![private and public link](/help/assets/assets/shared-link-for-assets.png)

   <!--Enable the **[!UICONTROL Public Link]** toggle, select a **[!UICONTROL period of expiration]** and click **[!UICONTROL Generate Public Link]** to generate a link to share with public users. Public users, as guests, access the shared assets page without signing in to [!DNL Content Hub].-->

   

   >[!NOTE]
   > 
   > [Enable public link sharing from the configuration page](/help/assets/configure-content-hub-ui-options.md#enable-public-link-sharing) so that the **[!UICONTROL Public Link]** toggle appears on the **[!UICONTROL Share assets]** dialog box. Without enabling this configuration, the **[!UICONTROL Public Link]** toggle does not display.

## Share an asset from its preview page {#share-asset-from-preview-page}

You can share an asset directly from its preview page in [!DNL Content Hub], generating either a private or public link without leaving the preview view. Execute the following steps to share the asset while previewing the asset:

1. Navigate to [!DNL the Content Hub] homepage and click the asset thumbnail to preview the asset. This displays the menu options on the right pane of the dialog box.
1. Select ![share](/help/assets/assets/share.svg) to display the **[!UICONTROL Share]** panel.

   ![share asset while previewing it](/help/assets/assets/share-link-asset-preview.png)

1. Complete Steps 3 to 5 in the [Share assets](#share-assets) section to generate and share the asset link—Private or public—directly from this **[!UICONTROL Share]** panel. A Private link restricts access to authorized users, while a public link allows anyone with the URL to view the asset.

## Access the shared assets {#access-shared-assets}

Access the shared assets page through the provided link, then complete any of the following actions:

* Select one or more assets and click ![download](/help/assets/assets/download-icon.svg) **[!UICONTROL Download]** to choose the **[!UICONTROL Original]**, **[!UICONTROL Static]**, or both renditions from the available download options. This lets you download the full-resolution source file (**[!UICONTROL Original]**), a fixed, optimized version (**[!UICONTROL Static]**), or both at once—depending on whether you need the master asset or a delivery-ready copy.

   ![](/help/assets/assets/download-shared-assets.png)

* Click the asset thumbnail to view that asset's metadata, which provides identifying details such as file information and asset properties before you download.
* On the shared assets page ([accessed through a private link](#share-assets)), click an asset thumbnail and select ![download](/help/assets/assets/download-icon.svg) to select and view the available **dynamic renditions** of the asset on the **[!UICONTROL Download]** panel. Because dynamic renditions are generated on demand, previewing them on the panel confirms the correct size and format before selecting and downloading the renditions you need.

   ![](/help/assets/assets/download-renditions-shared-assets-page.png)

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
