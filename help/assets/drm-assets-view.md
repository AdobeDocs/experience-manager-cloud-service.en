---
title: Digital Rights Management in Assets view 
description: Learn how to manage licenses with the Digital Rights Management service in Assets view.
contentOwner: AG
feature: Asset Management,DRM
role: User, Admin
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: fa5f94df-1c15-4593-afcb-1d24508da2bf
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Digital Rights Management for digital assets {#digital-rights-management-in-assets}

The Digital Rights Management (DRM) Service in Adobe Experience Manager Assets view uses artificial intelligence to extract usage-rights information from license documents and fill the metadata fields in assets. You can review the extracted information, save it as a reusable license record, and assign that license to one or more assets. License records are managed separately from assets. You can build a library of licenses before uploading assets, or assign existing licenses to assets. When you update a license, such as changing its expiration date, the change applies to all the assets associated with that license.

An asset can have multiple licenses. Before downloading a licensed asset, you need to review the restrictions and accept the applicable license terms.

## Prerequisites {#prerequisites}

Before you begin, confirm you have the source usage rights document available so that you can check the extracted information which gets populated in the metadata fields.

## Upload a license {#upload-and-review-license}

You can create a reusable license from a usage-rights document. AI extracts the information from the document, but you need to review the information before saving it.

* In **[!UICONTROL Licenses]**, click **[!UICONTROL Upload license]**. This is shown in the figure below.
   ![Licenses](assets/licenses.png)
* The **[!UICONTROL Assign License]** tab appears. Upload the source usage-rights document and click **[!UICONTROL Next]**.
   ![Uploading](assets/uploading.png)
* Enter a name for the license.
* Review the extracted usage-rights information including the usage dates, regions, channels, and restrictions.
* Click **[!UICONTROL Apply and Save]**.

The newly created license is now displayed in the license list.
![Newly created license](assets/newlicense.png)

>[!NOTE]
> 
>Creating a license is different from assigning it to assets. For example, you can create a license with its allowed regions, channels, and expiration date. You can then assign the same license to each asset rather than creating for every asset.

## View license {#view-license}

You can view the saved license records under **[!UICONTROL Licenses]**. Use it to find a license, review its usage rights, and view the assets associated with it.

To view a particular license, click **[!UICONTROL View]**. The **[!UICONTROL Property list]** tab appears. You can review and update the license details, including the expiration date. 

![Review license](assets/review.png)

To view the list of assets using that particular license, click **[!UICONTROL Assets using this license]**.

## Assign licenses to assets {#assign-licenses}

You can assign an existing license to an asset, or upload a new license document while assigning.

* Select the asset and click the ![More icon](assets/do-not-localize/more-icon.svg). Click **[!UICONTROL Assign License]**.

![Assign license](assets/assign.png)

Alternatively, you can open an asset by double clicking and assign a license by clicking **[!UICONTROL Assign license]**.
* The **[!UICONTROL Assign license]** tab appears. Choose an existing license from the list. Alternatively, you can upload a new license document to create a new license.
![Upload license](assets/upload.png)

* Select **[!UICONTROL Next]** and review the metadata information.
![Assigning license](assets/assigning.png)
* Click **[!UICONTROL Assign]**.
 
## Remove licenses {#remove-licenses}

An asset can have more than one license. To unassign license from an asset, follow the below steps:

* Double-click the asset to open it. 
* If multiple licenses are assigned to an asset, click the drop-down to review each license and its restrictions.
* To remove a license, click **[!UICONTROL Unassign license]** > **[!UICONTROL Unassign]**.  

![Unassign license](assets/unassign.png)

Alternatively, you can unassign a license by selecting the asset. Click the ![More icon](assets/do-not-localize/more-icon.svg). Click **[!UICONTROL Unassign License]**.


## Download assets with license {#download-licensed-assets}

You can download an asset that has license. Downloading an asset requires you to review and accept the applicable license terms.

* Select the licensed asset and click ![Download](assets/do-not-localize/download-icon.png) to start the download. 

Alternatively you can open the asset by double clicking and click **[!UICONTROL Download]**.

![Download licensed asset](assets/download.png)

* Review the usage-rights information and restrictions.
* Select the **[!UICONTROL I have read and accept all the terms and conditions]** check box and click **[!UICONTROL Proceed]**.

![Downloading licensed asset](assets/accept.png)
* Click **[!UICONTROL Ok]** from the **[!UICONTROL Downloading Asset]** tab.
![Download tab](assets/downloading.png)

**See also**

* [Translate [!DNL Assets]](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in [!DNL Assets] view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish [!DNL Assets] to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
