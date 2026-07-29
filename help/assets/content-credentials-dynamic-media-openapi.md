---
title: Content Credentials in Dynamic Media
description: Content Credentials, integrated into Dynamic Media, can offer context into the history of an asset, including how it was made and who was involved in creating it. Like a nutrition label for digital content, Content Credentials can help increase transparency and build trust with audiences.
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
---
# Content Credentials in Dynamic Media {#content-credentials-dynamic-media}

Brands are more concerned than ever about content transparency, AI disclosure, and preventing the tampering of assets. The Content Authenticity Initiative (CAI) at Adobe builds tools compliant with the [Coalition for Content Provenance and Authenticity](https://c2pa.org/specifications/specifications/1.1/specs/C2PA_Specification.html#_trust_model) (C2PA) technical standard. Using Content Credentials, assets which are generated through AI are digitally signed using the C2PA (Coalition for Content Provenance and Authenticity) specification. These signatures embed secure metadata within the asset, enabling users and systems to verify the content's origin and history The metadata can provide information such as:

1. The software or service used to create the image.
2. Whether generative AI was involved in the image creation process.
3. Edits or modifications made to the image, such as modification in height or width after it was generated.
4. The provenance and authenticity of the content.

Thus Content Credentials, which are a new kind of encrypted, tamper-evident metadata can help viewers understand the lineage of content and ensure the integrity of brand assets.

## Prerequisites of Assets using Content Credentials in Dynamic Media {#prerequisites-assets-using-content-credentials}

Ensure that you fulfil the following requirements before using Content Credentials:

1. Only eligible assets that have been created through GenAI such as Adobe's Firefly are supported, non-GenAI assets are not eligible for Content Credentials preservation. An asset is considered eligible in the following conditions:
    1. The source brand asset is identified as a content generated using GenAI.
    2. The source brand asset contains valid Content Credentials metadata.
2. Dynamic Media does not preserve Content Credentials for assets that do not already contain them.
3. For image or document assets, Content Credentials is supported for *.jpeg*, *.png*, *.gif*, *.tiff*, *.dng*, *.arw*, and *.nef* file formats. For video assets, Content Credentials is supported for *.mp4*, *.avi*, *.mov*, *.m4v* file formats.
4. Content Credentials preservation is supported only for asset download/export workflows. This includes exports from Adobe Experience Manager (AEM) /  Adobe Dynamic Media Classic and delivery through the **attachment** modifier, which forces download by setting the **[!UICONTROL Content-Disposition]** response header.

    >[!NOTE]
    >
    > If Content Credentials cannot be validated or processed, the asset can still be uploaded, processed, delivered, or exported normally, but the output does not include Content Credentials.

## Access Content Credentials for Dynamic Media assets {#access-content-credentials-for-dynamic-media-assets}  

1. Upload an asset in the Dynamic Media environment.
2. Open the asset and copy the URL.
3. Paste the copied URL in any web browser. You can generate rendition by customizing the height and width of the asset. 
4. Download the asset. You can download eligible assets or renditions from Dynamic Media using the **attachment** as a modifier. You can use **attachment=true** or **attachment=1** as a modifier in Dynamic Media - Scene7 mode and **attachment=true** in Dynamic Media with OpenAPI capabilities. For example, see the following URL: [https://<server>/is/image/<company>/<asset>?attachment=1]. When the source asset is eligible, Dynamic Media preserves the Content Credentials in the downloaded output.
For more information on downloading the asset using the **attachment** as a modifier (**attachment=true**), see [https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/#operation/getAssetSeoFormat!in=query&path=attachment&t=request]. 

   >[!NOTE]
   >
   > When you download a generated rendition, Dynamic Media creates a new output file. Because this output is newly generated, Dynamic Media signs the rendition again using the original asset as a source ingredient to preserve the content credentials chain and returns the generated file with Content Credentials when the source asset is eligible.

5. You can also export an asset from Dynamic Media. 

    >[!NOTE]
    >
    > For original exports, the original asset is returned with its existing Content Credentials.

6. Upload the downloaded asset in any C2PA software, for example, Adobe's CAILens interface.
You can now view the list of actions performed such as opening the asset, converting the asset's type from *.png* to *.avif*, resizing the asset, and editing the asset.
![C2PA Manifest](/help/assets/dynamic-media/assets/manifest.png)


## Limitations {#limitations-content-credentials}
 
To maintain the integrity and authenticity of Content Credentials, Dynamic Media enforces the following limitations:

1. Source assets that are above the configured maximum file size of 2 GiB and above the processing timeout of 60 seconds are not processed for Content Credentials preservation.
2. Composite Assets is not supported during signing and only the base image is considered for signing. If the base image is generated through any GenAI tool, the output is signed accordingly. However, the signature does not include any information about the GenAI-generated layers that are used to create the final rendition.
3. Adaptive video streaming files and video thumbnails are not signed. Also, there is no support for Content Credentials preservation for Dynamic Media hybrid solution.
4. Content Credentials processing has a configured timeout.
If any of these safeguards are reached, the asset continues through normal Dynamic Media processing, but Content Credentials may not be preserved in the generated output.

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
