---
title: XMP metadata
description: Learn about the XMP (Extensible Metadata Platform) metadata standard for metadata management. It is used by AEM as a standardized format for creation, processing, and interchange of metadata.
contentOwner: AG
---

# XMP metadata {#xmp-metadata}

XMP (Extensible Metadata Platform) is the metadata standard used by AEM Assets for all metadata management. XMP provides a standard format for the creation, processing, and interchange of metadata for a wide variety of applications.

Aside from offering universal metadata encoding that can be embedded into all file formats, XMP provides a rich [content model](#xmp-core-concepts) and is [supported by Adobe](#advantages-of-xmp) and other companies, so that users of XMP in combination with AEM Assets have a powerful platform to build upon.

## XMP overview and ecosystem {#xmp-ecosystem}

AEM Assets natively supports the XMP metadata standard. XMP is a standard for processing and storing standardized and proprietary metadata in digital assets. XMP is designed to be the common standard that allows multiple applications to work effectively with metadata.

Production professionals, for example, use the built-in XMP support within Adobe's applications to pass information across multiple file formats. The AEM Assets repository extracts the XMP metadata and uses it to manage the content lifecycle and offers the ability to create automation workflows.

XMP standardizes how metadata is defined, created, and processed by providing a data model, a storage model, and schemas. All of these concepts are covered in this section.

All legacy metadata from EXIF, ID3, or Microsoft Office is automatically translated to XMP, which can be extended to support customer-specific metadata schema, such as product catalogs.

Metadata in XMP consists of a set of properties. These properties are always associated with a specific entity referred to as a resource; that is, the properties are “about” the resource. In the case of XMP, the resource is always the asset.

XMP defines a [metadata](https://en.wikipedia.org/wiki/Metadata) model that can be used with any defined set of metadata items. XMP also defines particular [schemas](https://en.wikipedia.org/wiki/XML_schema) for basic properties useful for recording the history of a resource as it passes through multiple processing steps, from being photographed, [scanned](https://en.wikipedia.org/wiki/Image_scanner), or authored as text, through photo editing steps (such as [cropping](https://en.wikipedia.org/wiki/Cropping_%28image%29) or color adjustment), to assembly into a final image. XMP allows each software program or device along the way to add its own information to a digital resource, which can then be retained in the final digital file.

XMP is most commonly serialized and stored using a subset of the [W3C](https://en.wikipedia.org/wiki/World_Wide_Web_Consortium) [Resource Description Framework](https://en.wikipedia.org/wiki/Resource_Description_Framework) (RDF), which is in turn expressed in [XML](https://en.wikipedia.org/wiki/XML).

### Advantages of XMP {#advantages-of-xmp}

XMP has the following advantages over other encoding standards and schemata:

* XMP-based metadata is very powerful and fine-grained.
* XMP lets you have multiple values for one property.
* XMP has standardized encoding, which lets you easily exchange metadata.
* XMP is extensible. You can add additional information into your assets.

The XMP standard is designed to be extensible, allowing you to add custom types of metadata into the XMP data. EXIF, on the other hand, does not - it has a fixed list of properties that cannot be extended.

>[!NOTE]
>
>XMP generally does not allow binary data types to be embedded. To carry binary data in XMP, for example, thumbnail images, they must be encoded in an XML-friendly format such as `Base64`.

### XMP core concepts {#xmp-core-concepts}

**Namespaces and schemata** 

An XMP schema is a set of property names in a common XML namespace that includes
the data type and descriptive information. An XMP schema is identified by its XML namespace URI. Using namespaces prevents conflicts between properties in different schemas that have the same name but a different meaning.

For example, the **Creator** property in two independently designed schemas might mean the person who created the asset or it could mean the application that created the asset (for example, Adobe Photoshop).

**XMP properties and values**

XMP may include properties from one or more of the schemas. For example, a typical subset used by many Adobe applications might include the following:

* Dublin core schema: `dc:title`, `dc:creator`, `dc:subject`, `dc:format`, `dc:rights`
* XMP basic schema: `xmp:CreateDate`, `xmp:CreatorTool`, `xmp:ModifyDate`, `xmp:metadataDate`
* XMP rights management schema: `xmpRights:WebStatement`, `xmpRights:Marked`
* XMP media management schema: `xmpMM:DocumentID`

**Language alternatives**

XMP offers you the ability to add an `xml:lang` property to text properties to specify the language of the text.

## XMP writeback to renditions {#xmp-writeback-to-renditions}

This XMP write-back feature in Adobe Experience Manager (AEM) Assets replicates asset metadata changes to the renditions of the asset.

When you change the metadata for an asset from within AEM Assets or while uploading the asset, changes are initially stored within the asset node in CRXDE.

The XMP write-back feature propagates the metadata changes to all or specific renditions of the asset.

Consider a scenario where you modify the [!UICONTROL Title] property of the asset titled `Classic Leather` to `Nylon`.

![metadata](assets/metadata.png)

In this case, the AEM Assets saves the changes to the **[!UICONTROL Title]** property in the `dc:title` parameter for the asset metadata stored in the asset hierarchy.

![metadata_stored](assets/metadata_stored.png)

However, AEM Assets does not automatically propagate any metadata changes to the renditions of an asset.

The XMP write-back feature lets you propagate the metadata changes to all or specific renditions of the asset. However, the changes are not stored under the metadata node in the asset hierarchy. Instead, this feature embeds the changes in the binary files for the renditions.

### Enable XMP write-back {#enable-xmp-writeback}

<!-- asgupta, Engg: Need attention here to update the configuration manager changes.
-->

To enable the metadata changes to be propagated to the renditions of the asset when uploading it, modify the **[!UICONTROL Adobe CQ DAM Rendition Maker]** configuration in Configuration Manager.

1. To open Configuration Manager, access `https://[aem_server]:[port]/system/console/configMgr`.
1. Open the **[!UICONTROL Adobe CQ DAM Rendition Maker]** configuration.
1. Select the **[!UICONTROL Propagate XMP]** option, and then save the changes.

### Enable XMP write-back for specific renditions {#enable-xmp-writeback-for-specific-renditions}

To let the XMP write-back feature propagate metadata changes to select renditions, specify these renditions to the [!UICONTROL XMP Writeback Process] workflow step of DAM Metadata WriteBack workflow. By default, this step is configured with the original rendition.

For the XMP write-back feature to propagate metadata to the rendition thumbnails 140.100.png and 319.319.png, perform these steps.

1. Tap/click the AEM logo, and then navigate to **[!UICONTROL Tools]** &gt; **[!UICONTROL Workflow]** &gt; **[!UICONTROL Models]**.
1. From the Models page, open the **[!UICONTROL DAM Metadata Writeback]** workflow model.
1. In the **[!UICONTROL DAM Metadata Writeback]** properties page, open the **[!UICONTROL XMP Writeback Process]** step.
1. In the **[!UICONTROL Step Properties]** dialog box, tap/click the **[!UICONTROL Process]** tab.
1. In the **[!UICONTROL Arguments]** box, add `rendition:cq5dam.thumbnail.140.100.png,rendition:cq5dam.thumbnail.319.319.png`, and then tap/click **[!UICONTROL OK]**.

   ![step_properties](assets/step_properties.png)

1. Save the changes.
1. To regenerate the Pyramid TIFF (PTIFF) renditions for Dynamic Media images with the new attributes, add the **[!UICONTROL Dynamic Media Process Image Assets]** step to the DAM Metadata write-back workflow. PTIFF renditions are only created and stored locally in a Dynamic Media Hybrid implementation.

1. Save the workflow.

The metadata changes are propagated to the renditions renditions thumbnail.140.100.png and thumbnail.319.319.png of the asset, and not the others.

<!--
>[!NOTE]
>
>For XMP writeback issues in 64 bit Linux, see [How to enable XMP write-back on 64-bit RedHat Linux](https://helpx.adobe.com/experience-manager/kb/enable-xmp-write-back-64-bit-redhat.html).
>
>For more information about supported platforms, see [XMP metadata write-back prerequisites](/help/sites-deploying/technical-requirements.md#requirements-for-aem-assets-xmp-metadata-write-back).
-->

<!--
TBD: The method has changed in AEMaaCS. Find the new ones.

### Filter XMP metadata {#filtering-xmp-metadata}

AEM Assets supports filtering of properties/nodes for XMP metadata that is read from asset binaries and stored in JCR when assets are ingested. Filtering is possible via a blocked list and an allowed list.

Filtering using a blocked list lets you import all XMP metadata properties except the properties that are specified for exclusion. However, for asset types such as INDD files that have huge amounts of XMP metadata (for example 1000 nodes with 10,000 properties), the names of nodes to be filtered are not always known in advance. If filtering using a blocked list allows a large number of assets with numerous XMP metadata to be imported, the AEM instance/cluster can encounter stability issues, for example clogged observation queues.

Filtering of XMP metadata via allowed list resolves this issue by letting you define the XMP properties to be imported. This way, other/unknown XMP properties are ignored. For backward compatibility, you can add some of these properties to the filter that uses a blocked list.

>[!NOTE]
>
>Filtering works only for the properties derived from XMP sources in asset binaries. For the properties derived from non-XMP sources, such as EXIF and IPTC formats, the filtering does not work. For example, the date of asset creation is stored in property named `CreateDate` in EXIF TIFF. AEM stories this value in the metadata field named `exif:DateTimeOriginal`. As the source is a non-XMP source, filtering does not work on this property.

1. To open Configuration Manager, access `https://[aem_server]:[port]/system/console/configMgr`.
1. Open the **[!UICONTROL Adobe CQ DAM XmpFilter]** configuration.
1. To apply filtering via an allowed list, select **[!UICONTROL Apply Whitelist to XMP Properties]**, and specify the properties to be imported in the **[!UICONTROL Whitelisted XML Names for XMP filtering]** box.

1. To filter out blocked XMP properties after applying filtering via allowed list, specify them in the **[!UICONTROL Blacklisted XML Names for XMP filtering]** box.

   >[!NOTE]
   >
   >The **[!UICONTROL Apply Blacklist to XMP Properties]** option is selected by default. In other words, filtering using a blocked list is enabled by default. To disable such filtering, deselect the **[!UICONTROL Apply Blacklist to XMP Properties]** option.

1. Save the changes.
-->

>[!MORELIKETHIS]
>
>* [XMP specification by Adobe](https://www.adobe.com/devnet/xmp.html)
