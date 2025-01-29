---
title: Best practices to integrate with [!DNL Adobe Creative Cloud]
description: Best practices integrate an Experience Manager deployment with Adobe Creative Cloud to streamline asset transfer workflows and achieve maximum efficiency.
contentOwner: AG
mini-toc-levels: 1
feature: Collaboration, Adobe Asset Link, Desktop App
role: User, Architect, Admin
exl-id: cbed0d62-5148-45eb-b6a0-9fd164060fdc
---
# Adobe Experience Manager and Creative Cloud integration best practices {#aem-and-creative-cloud-integration-best-practices}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/aem-cc-integration-best-practices.html?lang=en)                  |
| AEM as a Cloud Service     | This article         |

Adobe Experience Manager Assets is a digital asset management (DAM) solution that can integrate with Adobe Creative Cloud to help DAM users work together with creative teams, streamlining collaboration in the content creation process.

Adobe Creative Cloud provides creative teams with an ecosystem of solutions and services to help them to create digital assets. It includes desktop and mobile applications, cloud services like storage with desktop sync or web experience, and marketplaces like Adobe Stock.

Read on to know what integrations to pick between desktop and the enterprise-grade DAM based on your use case and what are the associated best practices for the connecting workflows.

>[!NOTE]
>
>Experience Manager to Creative Cloud folder sharing is now deprecated and no longer covered below. Adobe recommend newer capabilities like Adobe Asset Link or Experience Manager desktop app to provide creative users with access to the assets managed in Experience Manager.

## Collaboration need of creatives, marketers, and DAM users {#collaboration-need-of-creatives-marketers-and-dam-users}

| Requirements | Use case | Involved surfaces |
|---|---|---|
| Simplify experience for creatives on desktop | Streamline access to asset from a DAM ([!DNL Assets]) for creative professionals, or more broadly, users on desktop working in native asset creation applications. They need an easy and straightforward way to discover, use (open), edit and save changes to Experience Manager, and upload new files. | Win or Mac desktop; Creative Cloud apps |
| Provide high-quality, ready-to-use assets from [!DNL Adobe Stock] | Marketers help accelerate the content creation process by assisting with asset sourcing and discovery. Creative professionals use the approved assets right from within their creative tools. | [!DNL Assets]; [!DNL Adobe Stock] marketplace; metadata fields |
| Distribute and share assets by organizations | Internal departments/local branches and external partners, distributors, and agencies use the approved assets shared by the parent organization. The organization wants to securely and seamlessly share the created assets for wider reuse. | [!DNL Brand Portal], [!DNL Asset Share Commons] |
| Generate predefined variations of uploaded assets automatically | Automatically process assets using Adobe's unique media handling and transformation technology for predefined actions. Create custom logic to define your own actions using APIs and asset microservices. | [!DNL Assets] user interface |

## Adobe offerings to support the collaboration need {#adobe-offerings-to-support-the-collaboration-need}

| Value proposition for the involved personas | Adobe offering | Involved surfaces |
|---|---|---|
| Creative users discover assets from [!DNL Experience Manager], open and use them, edit and upload changes to [!DNL Experience Manager], and upload new files into [!DNL Experience Manager], without leaving their [!DNL Creative Cloud] app. | [Adobe Asset Link](https://helpx.adobe.com/enterprise/using/adobe-asset-link.html) | Photoshop, Illustrator,and InDesign. |
| Business users simplify opening and using assets, editing and uploading changes to [!DNL Experience Manager], and uploading new files into [!DNL Experience Manager] from the desktop environment. They use a generic integration to open any asset type in the native desktop application, including non-Adobe ones. | [[!DNL Experience Manager] desktop app](https://experienceleague.adobe.com/docs/experience-manager-desktop-app/using/using.html) | Experience Manager desktop app on Win and Mac desktop |
| Marketers and business users discover, preview, license and save, and manage the Adobe Stock assets from within Experience Manager. Licensed and saved assets provide select Adobe Stock metadata for better governance. | [Experience Manager and Adobe Stock integration](aem-assets-adobe-stock.md) | [!DNL Experience Manager] web interface |
| Improve collaboration between digital product designers and marketers. Let designers use the digital assets in design and wireframe models on Adobe XD canvas. | [[!DNL Adobe Asset Link] for [!DNL Adobe XD]](https://helpx.adobe.com/enterprise/using/adobe-asset-link-for-xd.html) | [!DNL Adobe XD] |
| Marketers can automatically create variations and derivatives based on uploaded assets and predefined actions created using customization. Use this automation to improve content velocity and reduce manual effort. | [Content automation](/help/assets/cc-api-integration.md) | [!DNL Experience Manager Assets] web interface |

This article focuses primarily on the first two aspects of the collaboration needs. Distribution and sourcing of assets at scale is briefly mentioned as a use case. For such needs solutions, consider Adobe Brand Portal or Asset Share Commons. Alternate solutions such as [Experience Manager Assets Brand Portal](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/home.html), solutions that can be built based on [Asset Share Commons](https://opensource.adobe.com/asset-share-commons/) components, [Link Share](share-assets.md), using [Experience Manager Assets web UI](/help/assets/manage-digital-assets.md) should be reviewed based on specific requirement.

![Creative Cloud connections for Experience Manager: Deciding which capability to use](assets/creative-connections-aem.png)

Deciding on which capability to use

### Mapping of use cases and Adobe solutions {#mapping-of-use-cases-and-adobe-solutions}

| Use case | Adobe Asset Link | Experience Manager desktop app | Remarks or alternate methods |
|----------------------------------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Discover - browse folders | Yes | Experience Manager Web UI + desktop actions | When browsing the network share, turn off the thumbnails to avoid downloading binary files of assets. |
| Discover - access collections | Yes | Experience Manager Web UI + desktop actions |  |
| Discover - search for assets | Yes | Experience Manager Web UI + desktop actions |  |
| Use - open asset | Yes | Yes - for any app | [Open from Web interface](/help/assets/manage-digital-assets.md#previewing-assets) or from Finder |
| Use - place asset from Experience Manager into a document | Yes - embedding | Yes - linking or embedding | Experience Manager desktop app gives access to assets as files on the local file system. These links in the native apps are represented by local paths. |
| Edit - open for editing | Yes - Check-out action | Yes - Open action (in the network share) | [Check-out in AAL](https://helpx.adobe.com/enterprise/using/manage-assets-using-adobe-asset-link.html) saves the asset to user's creative cloud storage account (synchronized by Creative Cloud app) by default. |
| Edit - work in progress outside Experience Manager | Yes - Asset available in user's Creative Cloud storage account synced to desktop. | Yes |  |
| Edit - upload changes | Yes - [Check-in action](https://helpx.adobe.com/enterprise/using/manage-assets-using-adobe-asset-link.html) with optional comment | Yes |  |
| Upload - single file | Yes - uploads current active document | Yes | [Upload via web interface](/help/assets/manage-digital-assets.md#uploading-assets) |
| Upload - multiple files / hierarchical folder structures | No | Yes | [Upload via web interface](/help/assets/manage-digital-assets.md#uploading-assets); Custom scripting or tool |
| Misc - user and login | Creative Cloud user logged into Creative Cloud desktop app gets recognized (SSO) | Experience Manager user / login | Users of both solutions count against the Experience Manager user quota. |
| Misc - network and access | Requires access from user's desktop to Experience Manager deployment over network | Requires access from user's desktop to Experience Manager deployment over network | Adobe Asset Link does not share network proxy environment. |


<!-- Removing this row from table as migration guide is not yet final.
| Misc - Migrate large number of assets | No | No | [Migration Guide](/help/assets/assets-migration-guide.md) |
-->

To support asset distribution use cases, consider the following options:

* [Experience Manager Assets Brand Portal](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/home.html) for a configurable add-on to Assets to publish assets.

* Custom solutions are created based on [Asset Share Commons](https://opensource.adobe.com/asset-share-commons/) code base.
* Experience Manager [link share](/help/assets/share-assets.md) to share assets on demand using links.
* [Assets web interface](/help/assets/manage-digital-assets.md) with areas for external parties secured by Experience Manager Access Control setup and with necessary IT / network configuration adjustments, giving these external users access to Experience Manager.

## Key concepts and use cases {#key-concepts-and-use-cases}

### Glossary of common terms {#glossary-of-common-terms}

* **Work-in-progress or creative work-in-progress (WIP):** A phase in asset lifecycle where an asset undergoes multiple changes and is typically not yet ready to be shared with broader teams.
* **Creative-ready assets:** Assets that are ready to be shared with a broader team, or have been  selected / approved  by the creative team for sharing with marketing or LOB teams.

* **Asset approvals:** The approval process that runs for assets already uploaded to DAM, which typically includes brand approvals, legal approvals, and so on.
* **Final asset:** An asset that has gone through all  approvals/metadata  tagging and is ready to be used by the broader team. Such an asset is stored in DAM and made available to all (or all interested) users. It can be used in marketing channels or by creative teams to create designs.

* **Minor asset  update/change :** A quick and small change to a digital asset. It is often made in response to a retouching or minor editing request, asset review, or approval (for example, reposition, change text size, adjust saturation/brightness, color, and so on).
* **Major asset  update/change :** A change to a digital asset that requires considerable work, and sometimes must be done over a longer period of time. It typically includes multiple changes. The asset must be saved multiple times while being updated. Major asset updates typically cause the asset to enter a WIP stage.
* **DAM:** Digital asset management. In this document, it is synonymous with Experience Manager Assets, unless specifically mentioned otherwise.
* **Creative user:** A creative professional, who creates digital assets using Creative Cloud apps and services. In some cases, a creative user may be a member of a creative team who may use Creative Cloud, but does not create digital assets (like a creative director or creative team manager).
* **DAM user:** A typical user of a DAM system. Depending on the organization, a DAM user can be a marketing or a non-marketing user, for example, a Line-of-Business (LOB) user, librarian, sales person, and so on.

### Considerations when using Experience Manager and Creative Cloud integration {#considerations-when-using-aem-and-creative-cloud-integration}

<!--incomplete and TBD: 

* DA2.0 best practices: See troubleshooting.md
* Stock integration: See ?
* AAL: See ?
* BP: See ?

--> 

This is a brief summary of best practices for Experience Manager and Creative Cloud Integration. Read the rest of this document to get the detailed understanding of these.

* **For creative users, working in Photoshop, InDesign, or Illustrator:** Adobe Asset Link provides the best user experience, including clean handling of the Work-in-progress on assets checked out from Experience Manager
* **For simplifying access to assets from desktop for any generic file format or application:** use Experience Manager desktop app
* **Understand why and when to store assets in DAM:** Updates to be made available to the broader team in your organization
* **Mind the volume of assets shared:** If your use case is asset distribution, governance and security might be the most important aspects. Consider using tools built for doing that at scale, like Brand Portal.
* **Understand asset lifecycle:** Know how assets are handled in your organization by different teams
* **Handle frequent saves to assets with care:** Adobe Asset Link takes care of that for you with PS, AI, ID. For other applications, do not carry out work in progress tasks in mapped/shared folder unless you need all the changes in DAM

### Access to Adobe Stock assets from Experience Manager Assets {#access-to-adobe-stock-assets-from-aem-assets}

[Experience Manager and Adobe Stock integration](/help/assets/aem-assets-adobe-stock.md) provides Experience Manager users with the ability to search, preview, license and save, assets from Adobe Stock into Experience Manager. Licensed and saved Adobe Stock assets have selected Stock metadata, which can be used to search for them with extra filters.

A few important points about this integration:

* When assets from Adobe stock are saved to Experience Manager, they become a regular Experience Manager Assets, with binary saved to the Experience Manager repository. Some metadata related to Adobe Stock are saved for the asset in Experience Manager, otherwise the ingestion process looks the same as for any other file. For example, if Smart Tags are active, the tags are added to these assets upon saving.
* The asset saved to Experience Manager is a copy, not a link back into Adobe Stock.

**Working with assets saved from Adobe Stock into Experience Manager in Creative Cloud**. This integration is independent of Adobe Asset Link, but Adobe Asset Link recognizes these assets saved from Stock that way, and displays additional metadata and Stock icon on these assets in Adobe Asset Link extension UI in Photoshop, Illustrator, or InDesign. The files are available for browsing, opening, and so on - because they are regular Experience Manager assets when saved to Experience Manager.
Creative users working in Creative Cloud apps with Adobe Asset Link extension present, in addition to having access to already-licensed assets from Adobe Stock into Experience Manager, can also use Creative Cloud Libraries panel to search, preview, and license Adobe Stock assets.
Assets from Adobe Stock licensed and saved into Experience Manager become available to the broader teams accessing Experience Manager Assets deployment, whereas creatives licensing assets from Adobe Stock via Creative Cloud Libraries panel make them available to themselves only by default in their Creative Cloud account.

## About storing assets in a DAM {#about-storing-assets-in-a-dam}

To design an efficient workflow between creative and marketing/line-of-business (LOB) teams and choose the best support capabilities, it is important to understand when and why assets are stored in DAM.

### Why assets are stored in DAM {#why-assets-are-stored-in-dam}

Storing assets in DAM makes them easily accessible and findable. It ensures that the assets can be used by numerous users across the organization or ecosystem, which includes partners, customers, and so on.

Most organizations choose to only store assets that are relevant to the downstream marketing/LOB processes (publishing to channels like web channel via Experience Manager Sites or other channels served by Adobe Experience Cloud - Marketing Cloud, Advertising Cloud, and measured by Analytics Cloud, providing to users/partners, and so on). In addition, organizations store assets that may be subjected to a review/approval process in DAM. This way, DAM stores mostly assets that have high chances of being used, and avoids storing idle assets.

Storing assets is also subject to technical and resource utilization considerations. DAM provides additional services around stored assets, including extracting metadata, versioning, generating previews/transcoding, managing references, and adding access control information. These services consume additional time and infrastructure resources.

Often, storing all assets and updates is not desirable. For example, if updates to specific assets are of poor quality and consume excessive resources, the assets may not be stored in DAM.

#### When assets are stored in DAM {#when-assets-are-stored-in-dam}

Creative teams (and organizations) are usually not interested in storing assets at each stage of the asset lifecycle. For example, they avoid storing assets in the following cases:

* Assets that are yet to be finalized or are subject to experimentation
* Assets that fail to pass the creative/internal team review cycle
* Compared to the asset in question, the team has better candidates to represent their work to external teams

Usually, the following classes assets are stored in DAM:

* Assets that reached a certain maturity and are considered ready to be shared
* Assets that were pre-selected by the creative team
* Specific asset formats that are usable or requested by marketing, depending on a specific contract or agreement (for example, JPG files converted from RAW files, TIFFs/images from PSD originals)

#### When updates to assets are stored in DAM {#when-updates-to-assets-are-stored-in-dam}

As a rule, only updates to assets that are relevant to the broader set of DAM users should be stored in DAM. It ensures that users (marketing and similar functions) only see relevant versions in the DAM asset timeline.

Typically changes related to major milestones in the asset lifecycle. For example, the initial marketing-ready asset or an official update based on request/review provided by the creative team should be stored and versioned in DAM.

The creative team's update for review by the marketing team after a request for a change in the existing asset in DAM is an example of a relevant update. It should be stored and versioned in DAM for further reference or for reverting to the previous version.

The following are examples of updates that are typically not relevant:

* Early versions of assets uploaded before it is ready for marketing review
* Frequent creative changes to the asset in the work-in-progress phase before creative and marketing teams decide that the asset is ready

### User access to DAM {#user-access-to-dam}

Experience Manager Assets supports two types of users based on their access to the Experience Manager Assets deployment. Typically, users inside the enterprise network (firewall) have direct access to DAM. Other users outside the enterprise network would not have direct access. The user type determines which integrations can be used from the technical standpoint.

#### Creative users with direct access to DAM {#creative-users-with-direct-access-to-dam}

Typically, in-house creative teams or agencies/creative professionals onboarded to the internal network have access to the DAM instance, including Experience Manager login. Experience Manager and network infrastructure can be set up to allow direct access to external parties - usually trusted organizations like agencies working for a client - to have access to Experience Manager over network, for example, via VPN or IP allowed list.

In such cases, Adobe Asset Link or Experience Manager desktop app provides easy access to final/approved assets and lets you save creative-ready assets to DAM.

#### Creative users without access to DAM {#creative-users-without-access-to-dam}

External agencies and freelancers without direct access to the DAM instance may require access to approved assets or want to add their new designs to the DAM.

Use the following strategies to provide access to final/approved assets:

* Use desktop app if Asset Link does not work.
* Use [Experience Manager Assets Brand Portal](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/home.html) for distributing assets securely to external partners
* Use a custom implementation of a distribution and sourcing portal based on [Asset Share Commons](https://adobe-marketing-cloud.github.io/asset-share-commons/)
* Use Access Control set up in Experience Manager and necessary network infrastructure (for example, VPN and IP allowed listing) to give external parties access to a dedicated area of content in your DAM. They can use Experience Manager Web UI to get assets and upload new content into your DAM.

#### Work in progress on assets from Experience Manager {#work-in-progress-on-assets-from-aem}

As discussed in this document, it is recommended to carry out major updates on assets, sometimes called work in progress, without having all the edits saved to the local file also uploaded to Experience Manager as changes. This speeds up a desktop user's work, limit network bandwidth used, and keep the assets timeline clean and focused on controlled, major updates.

Adobe Asset Link offers a good support for this use case:

* When users in Photoshop, InDesign, or Illustrator intent to edit a file, they execute a Check-out operation on the given asset
* The asset is downloaded in background, put into users Creative Cloud account synchronized to disk by Creative Cloud desktop app, and the check-out flag is toggled in Experience Manager on the asset to minimize editing conflicts
* From there on, the user works in a file that's stored locally in the synced location, and can continue working and saving necessary changes at any frequency required
* Also, because the asset is in the Creative Cloud account, it is also available on other devices that the user might have (for example, can be opened or edited in a dedicated Creative Cloud mobile app), and can be shared with other Creative Cloud users for collaboration purposes.
* When the creative user is done with the changes, they can execute a Check-in operation on that file in their Creative Cloud application, with an optional comment. The corresponding asset in Experience Manager are versioned and updated to with the new binary. Experience Manager users like Marketers or LOB users have access to major asset changes, or milestones, via Experience Manager asset timeline UI.

Experience Manager desktop app provides a network share for assets opened in the native app. By default, all the changes done locally are uploaded to Experience Manager automatically after a brief while. With such a configuration, frequent saves during the work-in-progress phase would all be uploaded into Experience Manager and versioned, creating a large amount of network traffic and potential scalability challenges - not to mention unnecessary versions in Experience Manager.

The recommended approach here is to use an option in Experience Manager desktop app to turn off automated updates, and upload changes to assets to Experience Manager manually, using the upload changes action in the app's Asset Status UI.

#### Bulk upload to DAM {#bulk-upload-to-dam}

You may have a requirement to simultaneously upload a larger number of files into DAM in some scenarios, for example:

* Uploading results of photoshoot or larger projects
* Uploading assets provided by creative agencies
* Uploading selected assets from a larger set if the selection is done outside DAM

This description refers to uploading files operationally (for example, every week or with every  photoshoot ), as a normal part of desktop user's workflow. Large asset migrations are not covered here.

You can use the following upload capabilities:

* To upload large/hierarchical folders in bulk, use Experience Manager desktop app that provides [folder upload](https://experienceleague.adobe.com/docs/experience-manager-desktop-app/using/using.html#bulk-upload-assets) functionality. You can also upload hierarchical folder structures. Assets are uploaded in background and, therefore, it is not tied to a web browser session
* To upload a few files from a single folder, drag the files directly to the web interface or use the Create option in the Experience Manager Assets web interface.
* Depending upon your business requirements, you can also use custom uploader.

#### Managing digital assets directly from desktop {#managing-digital-assets-directly-from-desktop}

If you use Network File Shares to manage digital assets, just using the network share mapped by Experience Manager desktop app could be seen as a convenient substitute. When transitioning from network file shares, Experience Manager web interface provides a rich set of Digital Asset Management capabilities that go well beyond what is possible on a network share (search, collections, metadata, collaboration, previews, and so on), and Experience Manager desktop app provides a handy link to connect the server-side DAM repository with the work on desktop.

Avoid using Experience Manager desktop app to manage assets directly in the network share of Experience Manager Assets. For example, avoid using Experience Manager desktop app to move/copy multiple files. Instead, use the Experience Manager Assets web UI to drag folders from Finder/Explorer to the network share or use the Experience Manager Assets Folder Upload feature.

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
