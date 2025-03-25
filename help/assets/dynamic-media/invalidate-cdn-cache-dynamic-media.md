---
title: Invalidate the Content Delivery Network cache by way of Dynamic Media
description: Learn how to invalidate your CDN (Content Delivery Network) cached content to let you quickly update assets that are delivered by Dynamic Media, instead of waiting for the cache to expire.
contentOwner: Rick Brough
feature: Asset Management
role: Admin,User
exl-id: c631079b-8082-4ff7-a122-dac1b20d8acd
---
# Invalidate the CDN cache by way of Dynamic Media {#invalidating-cdn-cache-for-dm-assets-in-aem-cs}

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

Dynamic Media assets are cached by the CDN (Content Delivery Network) for fast delivery to your customers. However, when you make updates to those assets, you want those changes to take effect immediately on your website. Purging or invalidating the CDN cache lets you quickly update assets that are delivered by Dynamic Media. You no longer have to wait for the cache to expire using a TTL (Time To Live) value (default is ten hours). Instead, you can send a request from within the Dynamic Media user interface to have the cache expire within minutes.

>[!NOTE]
>
>This feature requires that you use the Adobe-bundled CDN that comes with Adobe Experience Manager Dynamic Media. Any other custom CDN is not supported with this feature.

<!-- REMOVED MARCH 28, 2022 BECAUSE OF 404; NO REDIRECT WAS PUT IN PLACE BY SUPPORT See also [Cache overview in Dynamic Media](https://helpx.adobe.com/experience-manager/scene7/kb/base/caching-questions/scene7-caching-overview.html). -->

If you have enabled [Smart Imaging](/help/assets/dynamic-media/imaging-faq.md) on your account and you are using the Adobe-bundled CDN, you can purge all URLs with different query strings by purging the single base URL.

For example, invalidating `https://weekendsite.scene7.com/is/image/<CUSTOMER-NAME>/image`, also invalidates the following URLs:

* `https://weekendsite.scene7.com/is/image/<CUSTOMER-NAME>/image`
* `https://weekendsite.scene7.com/is/image/<CUSTOMER-NAME>/image?wid=300`
* `https://weekendsite.scene7.com/is/image/<CUSTOMER-NAME>/image?$PLP$`
* and so on.

This invalidation, however, is not the case for generic domains that do not support Smart Imaging, such as `s7d1.scene7.com`. Such domains still need the full URL to have invalidation work successfully.

**To invalidate the CDN cache by way of Dynamic Media:**

*Part 1 of 2: Creating a CDN Invalidation template*

1. In Adobe Experience Manager as a Cloud Service, go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL CDN Invalidation Template]**.

    ![CDN Validation feature](/help/assets/assets-dm/cdn-invalidation-template.png)

1. On the **[!UICONTROL CDN Invalidation template]** page, do one of the following options based on your scenario:

    | Scenario | Option |
    | --- | --- |
    | I have already created a CDN invalidation template in the past using Dynamic Media Classic. | The **[!UICONTROL Create Template]** text field is pre-populated with your template data. In such case, you can either edit the template, or continue to the next step. |
    | I have to create a template. What do I enter? | In the **[!UICONTROL Create Template]** text field, enter an image URL (including image presets or modifiers) referencing `<ID>`, instead of a specific image ID as in the following example:<br>`https://my.publishserver.com/is/image/company_name/<ID>?$product$`<br>If the template contains just `<ID>`, then Dynamic Media fills in `https://<publishserver_name>/is/image/<company_name>/<ID>` where `<publishserver_name>` is the name of your Publish Server that is defined in General Settings in Dynamic Media Classic. The `<company_name>` is the name of your company root associated with this Experience Manager instance, and `<ID>` is the selected assets through the asset picker to be invalidated.<br>Any presets/modifiers following `<ID>` are copied as-is in the URL definition.<br>Only images&ndash;that is, `/is/image`&ndash;can be auto formed based on the template.<br>For `/is/content/`, adding assets such as videos or PDFs using the asset picker does not auto generate URLs. Instead, you must specify such assets either in the CDN Invalidation template, or you can manually add the URL to such assets in *Part 2 of 2: Setting CDN Invalidation options*.<br>**Examples:**<br>In this first example, the invalidation template contains `<ID>` along with the asset URL having `/is/content`. For example, `http://my.publishserver.com:8080/is/content/dms7snapshot/<ID>`. Dynamic Media forms the URL based on this path, with `<ID>` being the assets selected through the asset picker that you want invalidated.<br>In this second example, the invalidation template contains the full URL of the asset used in your web properties with `/is/content` (not dependent on the asset picker). For example, `http://my.publishserver.com:8080/is/content/dms7snapshot/backpack` where backpack is the asset ID.<br>Asset formats that are supported in Dynamic Media are eligible for invalidation. Asset file types that are *not* supported for CDN invalidation include PostScript&reg;, Encapsulated PostScript&reg;, Adobe Illustrator, Adobe InDesign, Microsoft&reg; Powerpoint, Microsoft&reg; Excel, Microsoft&reg; Word, and Rich Text Format.<br><br>&bull; When you create the template, but sure you pay careful attention to syntax and typos; Dynamic Media does not do any template validation.<br>&bull; The CDN Invalidation Template can save text up to 2500 characters.<br>&bull; Specify URLs for image smart crops either in this CDN Invalidation template, or in the **[!UICONTROL Add URL]** text field in *Part 2: Setting CDN Invalidation options.*<br>&bull; Each entry in a CDN Invalidation template must be on its own line.<br>&bull; The following CDN Invalidation template example is for demonstration purposes only.|

    ![CDN Invalidation Template - Create](/help/assets/assets-dm/cdn-invalidation-template-create-2.png)

    >[!NOTE]
    >
    >The CDN Invalidation Template can save text up to 2500 characters.

1. In the upper-right corner of the **[!UICONTROL CDN Invalidation template]** page, select **[!UICONTROL Save]**, then select **[!UICONTROL OK]**.<br>
    *Part 2 of 2: Setting CDN Invalidation options*
    <br>

1. In Experience Manager as a Cloud Service, go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL CDN Invalidation]**.

    ![CDN Validation feature](/help/assets/assets-dm/cdn-invalidation-path.png)

1. On the **[!UICONTROL CDN Invalidation]** &ndash; **[!UICONTROL Add Details]** page, select the assets for CDN invalidation.

    ![CDN Invalidation - Add Details](/help/assets/assets-dm/cdn-invalidation-add-details-2.png)

    >[!NOTE]
    >
    >If you decide to leave the options **[!UICONTROL Invalidate asset associated image presets in CDN]** *and* **[!UICONTROL Invalidate based on template]** unchecked, then the base URL of the selected assets is formed for invalidation. Use this option arrangement for images only. 


   | Option | Description |
   | --- | --- |
   | **[!UICONTROL Invalidate asset associated image presets in CDN]** | (Optional) When you check this option, selected assets and all their associated image preset URLs are auto-formed for cache invalidation.<br>Assets and their associated pre-defined preset URLs are auto formed for invalidation. This option works only for image assets.|
   | **[!UICONTROL Invalidation based on template]** | (Optional) Check this option to use only the defined template for URL formation. |
   | **[!UICONTROL Add Assets]** | Use the Asset Picker to select assets you want to invalidate. You can select either published or unpublished assets.<br>Caching at the CDN is URL-based, not asset-based. Therefore, it is necessary for you to be aware of the complete URLs that are on your website. After you determine those URLs, you can add them to the template. Then, you can select and add those assets and invalidate the URLs in one step. <br>Use this option with **[!UICONTROL Invalidate asset associated image presets in CDN]**, or **[!UICONTROL Invalidation based on template]**, or both. |
   | **[!UICONTROL Add URL]** | Manually add or paste full URL paths to Dynamic Media assets whose CDN cache you want to invalidate. Use this option if you did not create a CDN Invalidation Template in ***Part 1 of 2: Creating a CDN Invalidation template***, and have only a few assets to invalidate.<br>**Important:** Each URL that you add must be on its own line.<br>You can invalidate up to 1000 URLs at a give time. If the number of URLs in the **[!UICONTROL Add URL]** text field is greater than 1000, you are unable to select **[!UICONTROL Next]**. In such cases, you must select **[!UICONTROL X]** to the right of a selected asset or a manually added URL to delete it from the invalidation list.<br>Specify URLs for image smart crops either in the CDN Invalidation template, or in this **[!UICONTROL Add URL]** text field.|

1. Near the upper-right corner of the page, select **[!UICONTROL Next]**.
1. On the **[!UICONTROL CDN Invalidation]** - **[!UICONTROL Confirm]** page, in the **[!UICONTROL URLs]** list box, you see a list of one or more URLs generated from the CDN Invalidation Template you created earlier and the assets you just added.

    For example, using the CDN Invalidation Template example that was shown in the steps earlier, suppose you added a single asset named `spinset`. When you go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL CDN Invalidation]**, it results in the following five generated URLs in the **[!UICONTROL CDN Invalidation - Confirm]** user interface:

    ![CDN Invalidation - Confirm](/help/assets/assets-dm/cdn-invalidation-confirm-2.png)

    If necessary, select **X** to the right of a URL to delete it from invalidation process.

1. Near the upper-right corner of the page, select **[!UICONTROL Submit]** to begin the CDN invalidation process.

## Troubleshoot CDN Invalidation errors

In all cases, either the entire batch is processed for invalidation, or the entire batch is failed.

| Error | Explanation |
| --- | --- |
| *Failed to retrieve URLs for selected assets.* | Occurs if any of the following scenarios are met:<br>&ndash; A Dynamic Media configuration is not found.<br>&ndash; There is an exception while retrieving a service user through which the Dynamic Media configuration is read.<br>&ndash; The publish server or the company root used to form the URLs is missing in the Dynamic Media configuration. |
| *Some URLs are not defined correctly. Correct and resubmit.* | Occurs if the IPS CDN cache invalidation API returns an error. The error indicates that the URL refers to a different company or the URL is not valid as per the validation done by the IPS cdnCacheInvalidation API. | 
| *Failed to invalidate CDN cache.* | Occurs if the CDN cache invalidation request fails for any other reason. |
| *No URLs entered to be invalidated.* | Occurs if there are no URLs present in the **[!UICONTROL CDN Invalidation]** &ndash; **[!UICONTROL Confirm]** page, and you select **[!UICONTROL Submit]**. |


   <!--  | I do not want to create a template. | Near the upper-right corner of the page, select **[!UICONTROL Cancel]**, then continue with ***Part 2: Working with CDN Invalidation***. While you are not required to create a template to use CDN Invalidation, Adobe recommends that you create one, especially if you have numerous assets that you need to update immediately, on a regular basis. The template is used at the time you set CDN invalidation options. | -->
