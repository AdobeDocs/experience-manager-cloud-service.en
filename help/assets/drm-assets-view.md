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

Before you begin, confirm the following:
* DRM license management is enabled for your Assets view environment.
* You have the source license document available so that you can check the extracted information which gets populated in the metadata fields. 

The **[!UICONTROL Licensing]** tab is provided by default. You do not need to add the tab to a custom metadata form. It appears alongside the asset's metadata even when the asset uses a different metadata form.

## Find and view licenses {#find-and-view-licenses}

The **[!UICONTROL Licenses]** field contains saved license records. Use it to find a license, review its usage rights, and view the assets associated with it.

* In Assets view, click **[!UICONTROL Licenses]**.
* Search or filter the list to find the required license.
* Open the license's properties to review its information, including its licensee, licensor, channels, regions, and usage dates.
* You can review the assets associated with the license to know where it is used.

## Upload a license {#upload-and-review-license}

You can create a reusable license from a usage-rights document. AI extracts the information from the document, but you need to review the information before saving it.

* In **[!UICONTROL Licenses]**, select **[!UICONTROL Upload license]**.
* Upload the source document and wait for extraction to finish.
* Enter a name for the license.
* Review the extracted usage-rights information including the usage dates, regions, channels, and restrictions.
* Click **[!UICONTROL Apply and Save]**.

The saved license appears in the license list. Note that creating a license is different from assigning it to assets. For example, you can create a license with its allowed regions, channels, and expiration date. You can then assign the same license to each asset rather than creating for every asset.

## Assign licenses to assets {#assign-licenses}

You can assign an existing license to an asset, or upload a new license document while assigning.

* Open the asset's details and select the **[!UICONTROL Licensing]** tab.
* Select **[!UICONTROL Assign license]**.
* Choose an existing license from the list. Alternatively, you can upload a new license document to create a new license.
* Select **[!UICONTROL Next]** and review the license information.
* Click **[!UICONTROL Assign]**.

The license is associated with the asset and is available for review in the **[!UICONTROL Licensing]** tab. Uploading a new license also adds it to the license list. You can also assign licenses in bulk. 


## Review and remove licenses {#review-and-remove}

An asset can have more than one license.

* Open the asset's **[!UICONTROL Licensing]** tab. 
* If multiple licenses are assigned, click the drop-down to review each license and its restrictions.
* To remove a license, click **[!UICONTROL Unassign license]** for the relevant license.

Unassigning a license dissociates that usage-rights record from the asset.

## Update license information for assets {#update-license-information}

You can update the license when its usage-rights information changes. The updates apply to all the assets associated with that license, so you do not need to edit each asset's license individually.

* In **[!UICONTROL Licenses]**, find the license and open its properties.
* Review the associated assets to identify the assets affected by the change.
* Update the relevant information, such as an expiration date and save the changes.

## Download assets with license {#download-licensed-assets}

You can download an asset that has license. Downloading an asset requires you to review and accept the applicable license terms.

* Select the licensed asset and start the download.
* Review the usage-rights information and restrictions. Review each license when the asset has multiple licenses.
* Accept the applicable terms and continue the download.

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
