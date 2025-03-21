---
title: Dynamic Media with OpenAPI capabilities frequently asked questions
description: Dynamic Media with OpenAPI capabilities frequently asked questions
role: User
exl-id: 3450e050-4b0b-4184-8e71-5e667d9ca721
---
# Dynamic Media with OpenAPI capabilities frequently asked questions {#new-dynaminc-media-apis-frequently-asked-questions}

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

>[!AVAILABILITY]
>
>Dynamic Media with OpenAPI capabilities guide is now available in PDF format. Download the entire guide and use Adobe Acrobat AI Assistant to answer your queries. 
>
>[!BADGE Dynamic Media with OpenAPI capabilities Guide PDF]{type=Informative url="https://helpx.adobe.com/content/dam/help/en/experience-manager/aem-assets/dynamic-media-with-openapi-capabilities.pdf"}

+++**Are all assets in Experience Manager Assets as a Cloud Service repository available for search and delivery using Dynamic Media with OpenAPI capabilities?**

No, only [approved and latest version of the assets](/help/assets/approve-assets.md) are available for search and delivery using Dynamic Media with OpenAPI capabilities, ensuring brand consistency across all channels and applications.

+++

+++**How can administrators mark new and existing assets added to a folder as approved?**

The status of an asset in Experience Manager Assets is governed by `jcr:content/metadata/dam:status` property. The values of this property can be:

* Approved

* Rejected

* Changes requested

Experience Manager Assets distinguishes Approved status using an approved icon available on the asset card, as depicted in the following images for Admin and Asset views:

**Admin view**

![Approved assets in Admin view](/help/assets/assets/approved-assets-thumbs-up.png)

**Assets view**

![Approved assets in Assets view](/help/assets/assets/approved-assets-thumbs-up-assets-view.png)


To approve all assets in a folder, see instructions on [how to bulk approve assets in a folder](/help/assets/approve-assets.md#bulk-approve-assets). There is also a video that depicts the entire process.

After setting up a folder for bulk approval, all new assets that are added to the folder are approved automatically. All existing assets are approved after reprocessing assets. See [Reprocessing digital assets](/help/assets/reprocessing.md) for instructions on how to reprocess assets. If you copy or move unapproved assets from any other folder, you need to [reprocess the assets](/help/assets/reprocessing.md).

The asset is marked as `Rejected`, if the administrator specifies `Rejected` or `Changes requested` values. Experience Manager Assets distinguishes the Rejected status using ![Reject Assets](/help/assets/assets/do-not-localize/reject-assets.svg) available on the asset card in Admin view.

Similarly, Experience Manager Assets distinguishes the Rejected status in Assets view using the following Rejected status on the asset card:

![Rejected assets in Assets view](/help/assets/assets/rejected-assets-admin-view.png)


+++

+++**How can you get Adobe IMS (Adobe Identity Management Services) user or group ID to be used to set the roles on assets in Experience Manager Admin view, for securing delivery and search experience?**

Users requiring access to Experience Manager Author environment are managed as Adobe IMS users in Adobe's Admin Console. For information about what Adobe IMS users are, and how they are accessed and managed in Admin Console, see [Adobe IMS users](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/adobe-ims-users.html?lang=en).

+++

+++**Can you approve multiple assets simultaneously within a folder?**

Yes, you can approve multiple assets within a folder simultaneously.

Execute the following steps to approve multiple assets simultaneously in [!DNL Experience Manager Assets Admin view]:

1. Select the asset(s) and click **[!UICONTROL Properties]**.
1. In the **[!UICONTROL Basic]** tab, scroll down to **[!UICONTROL Review Status]**.
1. Change the review status to **[!UICONTROL Approved]**.
1. Click **[!UICONTROL Save & Close]**.

Similarly, to approve multiple assets simultaneously within a folder in Assets view:

1. Select the asset(s) and click **[!UICONTROL Bulk Metadata Edit]**.

1. Select **[!UICONTROL Approved]** in the **[!UICONTROL Status]** field available in the [!UICONTROL Properties] section in the right pane.

1. Click **[!UICONTROL Save]**.


+++

+++**How can I secure asset delivery and search for the Dynamic Media OpenAPIs?**

Central asset governance in Experience Manager allows the DAM Administrators or Brand Managers to manage access to assets. They can restrict the access by configuring roles or by setting activation and deactivation time for approved assets on the authoring side, specifically on the AEM as a Cloud Service author instance.

End-users searching or utilizing delivery URLs can gain access to restricted assets upon successfully passing the authorization process.

For more information, see [Restrict access to assets in Experience Manager](restrict-assets-delivery.md#authoring).

+++

+++**How can you get permissions to edit the approval status of an asset?**

As a DAM user, you might not have permissions to [approve assets](approve-assets.md#approve-assets). To get the permissions to edit the approval status of an asset, the administrators can edit the default or any other metadata schema applied to the asset folder to provide edit permissions to the **[!UICONTROL Review Status]** field. For more information, see [how to disable edit for the Review Status](approve-assets.md#configuration) field.

+++

+++**How Dynamic Media with OpenAPI capabilities is different from Dynamic Media solution?**

Dynamic Media with OpenAPI capabilities and Dynamic Media represent distinct solutions, each offering its specialized delivery capabilities. It is imperative to thoroughly review your specific requirements to determine the most fitting solution that aligns with your needs.

General guidance from Adobe is to leverage Dynamic Media with OpenAPI stack for any integration use cases (1st or 3rd party apps). If there already exists an integration with Dynamic Media stack, recommendation is to not change it as OpenAPI stack URLs are different in structure. Only for any net new integration use cases, leverage OpenAPI stack. If your use case requires advanced modifiers not available with OpenAPI stack, then avoid the OpenAPI stack until Adobe bridges the gap. Even for basic native delivery from AEM Assets Cloud Services, OpenAPI stack can be evaluated as long as your use case is covered with the modifiers available with OpenAPI stack. In conclusion, Dynamic Media and Dynamic Media with OpenAPI stack can co-exist, depending on the nature of your use case.

The following are some of the key differences between Dynamic Media with OpenAPI capabilities and Dynamic Media:

| Dynamic Media with OpenAPI capabilities | Dynamic Media |
|---|---|
| [Available only with Assets as a Cloud Service](/help/assets/dynamic-media-open-apis-overview.md#prerequisites-dynaminc-media-open-apis) | Also available with On-premise or Adobe Managed Services with additional configuration and provisioning steps. |
| [Limited set of supported image modifiers, such as width, height, rotate, flip, quality, and format](/help/assets/deliver-assets-apis.md) | Rich set of available image modifiers |
| [Restricted asset delivery based on users, roles, date, and time](/help/assets/restrict-assets-delivery.md) | Assets published to Dynamic Media are accessible to all users |
| Most developers are familiar with OpenAPI specifications. AEM Assets extensibility becomes really simple by using [Micro-Frontend Asset Selector](/help/assets/overview-asset-selector.md). | SOAP -based APIs, which become a barrier while developing integration customizations. |
| Any changes made to approved assets in DAM, including version updates and metadata modifications, are automatically reflected in the delivery URLs. With a short Time-to-Live (TTL) value of 10 minutes configured for Dynamic Media with OpenAPI capabilities via CDN, updates become visible across all authoring and published interfaces in under 10 minutes. | Recommended CDN TTL of 10 hours. You can override the TTL value using the cache invalidation action. |
| Only approved assets are available for asset delivery to downstream applications, enabling on brand approved assets in digital experiences.| Any updates to a Dynamic Media published asset are auto-published without any approval workflow, which does not ensure on brand approved assets in digital experiences.    |
| Usage reports based on number of assets delivered. This feature will be available soon.| Usage reports are not available. This feature will be available soon. |
| Assets marked as Expired on Assets as a Cloud Service repository are not anymore available to downstream applications.| No inherent asset expiry. An asset remains public until it is deleted from AEM as a Cloud Service repository.|
| Does not support image presets and video smart crop capabilities.| Supports image presets and video smart crop capabilities. |
| Dynamic video encodes, that ensure best encodes are served based on the input video. No setup is required for native video delivery.| Standard 3 encodes irrespective of input video (can impact video delivery performance). You need to manually set up different encodes for different video bit rates. |
|  Difficult to guess asset UID based URLs (enables URL obfuscation), but SEO optimized. | URL obfuscation only available for URL query parameters. Assets IDs (asset names) in URLs are recognizable. |

+++

+++**How Dynamic Media with OpenAPI capabilities addresses the limitations of the Connected Assets feature?**

The table below outlines the key differences between the two solutions:

| Dynamic Media with OpenAPI capabilities | Connected Assets |
|---|---|
| Assets on the remote DAM deployment are available on AEM as a Cloud Service. | Assets on the remote DAM deployment can be available on AEM as a Cloud Service or Adobe Managed Services. |
| Asset binaries are not copied when assets on a remote DAM deployment are available an AEM Sites instance. | Asset binaries are copied when assets on a remote DAM deployment are available on an AEM Sites instance. |
| Support for all asset format types that are supported by AEM Assets. | No support for videos. |
|You can use Dynamic Media on the local Sites deployment while fetching assets from remote DAM deployment.  |Dynamic Media on local Sites deployment is read-only.  |
| No restrictions on the number of AEM Sites instances connected to a remote DAM deployment. You can [restrict the access to assets on the Sites instance by configuring roles](/help/assets/restrict-assets-delivery.md) for approved assets on remote DAM. |Restriction to connect no more than 4 AEM Sites instances to the remote DAM deployment. Increased number requires additional testing.  |
|Both Asset Selector and Dynamic Media with OpenAPI capabilities are extensible to allow custom integrations.  |  Connected Assets APIs are not extensible to allow custom integrations.  |
| Any changes made to approved assets available on remote DAM deployment, including version updates and metadata modifications, are automatically reflected on the Sites instance within a short Time-to-Live (TTL) value of 10 minutes. |  Asset updates on remote DAM deployment are handled via lifecycle events automatically but takes much more time as compared to Dynamic Media with OpenAPI capabilities. |
| Asset metadata on remote DAM is available on AEM Sites instance as well.  |Asset metadata on remote DAM is not available on AEM Sites instance.  |

+++
