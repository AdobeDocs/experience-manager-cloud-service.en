---
title: Dynamic Media with OpenAPI capabilities frequently asked questions
description: Dynamic Media with OpenAPI capabilities frequently asked questions
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 3450e050-4b0b-4184-8e71-5e667d9ca721
---
# Dynamic Media with OpenAPI capabilities frequently asked questions {#new-dynaminc-media-apis-frequently-asked-questions}

Dynamic Media with **OpenAPI (Open Application Programming Interface)** capabilities delivers, transforms, and manages rich media assets—images, video, and other visual content—through standardized, developer-friendly API endpoints. This frequently asked questions guide answers the most common queries about how these capabilities work, what they enable, and how to adopt them.

## What Are Dynamic Media with OpenAPI Capabilities? {#what-are-dynamic-media-openapi-capabilities}

Dynamic Media is a set of media delivery and transformation services that automatically optimize, resize, and render assets for any device, channel, or screen. The **OpenAPI capabilities** expose these services through open, well-documented API specifications, allowing developers to integrate media delivery directly into their own applications, storefronts, and content experiences.

Because the interfaces follow the OpenAPI standard, they are self-describing and predictable. As a result, integration teams can discover available endpoints, understand request and response formats, and generate client code more quickly than with proprietary, undocumented interfaces.

## Key Benefits {#key-benefits}

The main advantages of Dynamic Media with OpenAPI capabilities include:

- **Standardized integration:** OpenAPI-compliant endpoints make it straightforward to connect media services to existing applications and toolchains.
- **On-demand media transformation:** Assets are optimized, resized, and reformatted at request time, eliminating the need to store multiple manual variants.
- **Multi-channel delivery:** A single asset can be delivered and adapted across web, mobile, and connected experiences.
- **Headless-ready architecture:** API-first delivery aligns with headless and composable technology stacks.
- **Faster development:** Self-describing specifications accelerate onboarding, client-code generation, and testing for integration teams.

## What can I do with Dynamic Media OpenAPI capabilities? {#what-can-i-do}

You can request media assets on demand, apply real-time transformations such as cropping, resizing, and format conversion, and deliver optimized content to web, mobile, and connected experiences—all through standardized API calls.

## How do OpenAPI capabilities differ from traditional Dynamic Media delivery? {#openapi-vs-traditional}

Traditional delivery relies on preset URL patterns and templates. OpenAPI capabilities add a standardized, programmatic interface that makes automation, custom integration, and headless (decoupled front-end) architectures easier to implement.

## Are these capabilities suitable for headless and composable architectures? {#headless-composable}

Yes. Because media is retrieved and transformed through APIs rather than fixed page templates, Dynamic Media OpenAPI capabilities fit naturally into headless content management and composable commerce setups, where the presentation layer is separated from content and services.

## Do I need developer resources to use these capabilities? {#developer-resources}

API-based integration typically involves developers to connect endpoints to an application. However, the OpenAPI specification reduces this effort by providing consistent, machine-readable definitions that support automated client generation and testing.

## Are all assets in Experience Manager Assets as a Cloud Service repository available for search and delivery using Dynamic Media with OpenAPI capabilities? {#assets-available-for-search}

No. Only the **approved and latest version of the assets** are available for search and delivery using **Dynamic Media with OpenAPI capabilities**. Assets that have not been approved, or that exist only as earlier revisions, are excluded from this search-and-delivery scope.

Two conditions govern whether an asset in the Experience Manager Assets as a Cloud Service repository is surfaced:

- **Approval status** — the asset must be marked as [approved](/help/assets/approve-assets.md). Assets still in draft or awaiting review are not exposed for search and delivery.
- **Version currency** — only the **latest version** of an approved asset is eligible. Superseded or historical versions are not returned.

This scoping is intentional. Because only approved, current assets are eligible, delivery is restricted to content that has passed governance review, which **ensures brand consistency across all channels and applications**. As a result, downstream experiences that consume assets through Dynamic Media with OpenAPI capabilities reliably reference vetted, up-to-date content rather than unapproved or outdated revisions.

## How can administrators mark new and existing assets added to a folder as approved? {#add-assets-to-folder-as-approved}

Administrators mark new and existing assets in a folder as approved by configuring the folder for bulk approval and then reprocessing any pre-existing assets. In Adobe Experience Manager (AEM) Assets, the status of an asset is governed by the **`jcr:content/metadata/dam:status`** property. This property controls whether an asset is treated as usable, blocked, or pending revision across the asset library.

The values of this property are:

* **Approved** — the asset is validated and available for use, and is flagged with an approved icon on the asset card.

* **Rejected** — the asset is blocked and flagged with a rejected indicator.

* **Changes requested** — the asset requires revision and is handled the same way as a rejected asset.

AEM Assets distinguishes the **Approved** status using an approved icon available on the asset card, as depicted in the following images for Admin and Asset views:

**Admin view**

![Approved assets in Admin view](/help/assets/assets/approved-assets-thumbs-up.png)

**Assets view**

![Approved assets in Assets view](/help/assets/assets/approved-assets-thumbs-up-assets-view.png)

To approve all assets in a folder, see instructions on [how to bulk approve assets in a folder](/help/assets/approve-assets.md#bulk-approve-assets). There is also a video that depicts the entire process.

After setting up a folder for bulk approval, all new assets that are added to the folder are approved automatically. This ensures a consistent approval status across the folder without requiring manual review of each new upload. All existing assets are approved only after they are reprocessed, because reprocessing re-evaluates the `dam:status` property against the folder's bulk-approval configuration. See [Reprocessing digital assets](/help/assets/reprocessing.md) for instructions on how to reprocess assets. If administrators copy or move unapproved assets from any other folder, they must [reprocess the assets](/help/assets/reprocessing.md) so that the moved assets inherit the approved status.

AEM Assets marks the asset as **`Rejected`** whenever the administrator specifies either the **`Rejected`** or **`Changes requested`** values, because both values represent a non-approved state. AEM Assets distinguishes the Rejected status using ![Reject Assets](/help/assets/assets/do-not-localize/reject-assets.svg) available on the asset card in Admin view.

Similarly, AEM Assets distinguishes the Rejected status in Assets view using the following Rejected status on the asset card:

![Rejected assets in Assets view](/help/assets/assets/rejected-assets-admin-view.png)

## How can you get Adobe IMS (Adobe Identity Management Services) user or group ID to be used to set the roles on assets in Experience Manager Admin view, for securing delivery and search experience? {#set-roles-secure-delivery-search}

Adobe IMS (Adobe Identity Management Services) user and group IDs are retrieved from Adobe's **Admin Console** and applied in the [!DNL Experience Manager Assets Admin view] to set roles that secure delivery and search experiences. Assigning roles based on these IMS user or group IDs ensures that only authorized identities can access, deliver, or search specific assets. Because asset-level access is governed by these identities, using the correct IMS ID is the foundational step for role-based security in Experience Manager.

Users requiring access to the **Experience Manager Author** environment are managed as **Adobe IMS users** in Adobe's **Admin Console**. For information about what Adobe IMS users are, and how they are accessed and managed in Admin Console, see [Adobe IMS users](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/adobe-ims-users.html?lang=en).

**How IMS identities map to asset roles:**

- **Adobe IMS users** represent individual people who are provisioned and managed centrally in Adobe's **Admin Console**, providing a single source of truth for identity across Adobe Experience Cloud applications.
- **Adobe IMS groups** allow multiple users to be managed together, so roles and permissions can be applied consistently to a group rather than to each user individually.
- The **user ID** or **group ID** obtained from the Admin Console is the value referenced when configuring roles on assets, tying delivery and search permissions directly to a known, managed identity.

Because delivery and search experiences are governed by the roles set on assets, retrieving the accurate Adobe IMS user or group ID from the Admin Console is essential. This approach centralizes identity management, reduces the risk of unauthorized asset access, and keeps permissions aligned with how identities are already administered across the Adobe environment.

## Can you approve multiple assets simultaneously within a folder? {#approve-multiple-assets-in-folder}

Yes. Adobe Experience Manager (AEM) Assets lets users approve multiple assets within a folder simultaneously, eliminating the need to approve each file individually. Bulk approval streamlines review workflows and saves considerable time when managing large asset libraries, because the **Approved** review status is applied to every selected asset in a single action.

There are two supported methods, depending on which interface you use: the **Assets Admin view** or the **Assets view**.

### Approve multiple assets in Assets Admin view

Execute the following steps to approve multiple assets simultaneously in [!DNL Experience Manager Assets Admin view]:

1. Select the asset(s) and click **[!UICONTROL Properties]**.
1. In the **[!UICONTROL Basic]** tab, scroll down to **[!UICONTROL Review Status]**.
1. Change the review status to **[!UICONTROL Approved]**.
1. Click **[!UICONTROL Save & Close]**.

This applies the **[!UICONTROL Approved]** review status to every selected asset at once, confirming and closing the changes in a single step.

### Approve multiple assets in Assets view

Similarly, to approve multiple assets simultaneously within a folder in Assets view:

1. Select the asset(s) and click **[!UICONTROL Bulk Metadata Edit]**.

1. Select **[!UICONTROL Approved]** in the **[!UICONTROL Status]** field available in the [!UICONTROL Properties] section in the right pane.

1. Click **[!UICONTROL Save]**.

Clicking **[!UICONTROL Save]** commits the **[!UICONTROL Approved]** status to all selected assets simultaneously, ensuring consistent review states across the folder.

## How can I secure asset delivery and search for Dynamic Media with OpenAPIs? {#secure-asset-delivery}

**Central asset governance** in Adobe Experience Manager gives **Digital Asset Management (DAM) Administrators** and **Brand Managers** direct control over who can access assets delivered through **OpenAPIs (Open Application Programming Interfaces)**. This governance model secures both asset search and asset delivery by enforcing access rules at the source, so only authorized users retrieve protected content.

These administrators restrict access on the authoring side—specifically on the **AEM as a Cloud Service author instance**—using two primary controls:

- **Role configuration:** Access is granted or denied based on assigned roles, ensuring that each user or group sees only the assets their permissions allow.
- **Activation and deactivation scheduling:** Administrators set precise activation and deactivation times for approved assets, so content becomes available or is withdrawn automatically according to defined publishing windows.

Because these controls are applied at the authoring level, they govern every downstream request. **End-users who search for assets or use delivery URLs receive restricted assets only after successfully passing the authorization process.** Requests that fail authorization are blocked, which prevents unauthorized retrieval even when a delivery URL is known. This ensures that governance decisions made by DAM Administrators and Brand Managers are consistently enforced across both search results and direct delivery links.

For more information, see [Restrict access to assets in Experience Manager](restrict-assets-delivery.md#authoring).

## How can you get permissions to edit the approval status of an asset? {#permissions-edit-approval-status}

To gain permissions to edit the approval status of an asset, an administrator must grant edit access to the **[!UICONTROL Review Status]** field within the metadata schema applied to the asset folder. As a Digital Asset Management (DAM) user, you may not have permissions to [approve assets](approve-assets.md#approve-assets) by default, because approval and review-status editing are controlled at the metadata-schema level rather than through general folder access.

Administrators can enable this access by following these steps:

1. Open the **default metadata schema** or any other metadata schema applied to the relevant asset folder.
2. Locate the **[!UICONTROL Review Status]** field within that schema.
3. Provide edit permissions to the **[!UICONTROL Review Status]** field.

Granting edit permissions to the **[!UICONTROL Review Status]** field ensures that the designated DAM users can change an asset's approval status directly, streamlining the review workflow. For more information, see [how to disable edit for the Review Status](approve-assets.md#configuration) field.

## What is the supported file size for videos? {#supported-file-formats-videos}

Dynamic Media with OpenAPI capabilities supports long form videos with a maximum file size of **50 GB** and a maximum duration of **2 hours** per video. These limits define the upper bounds for a single video upload, allowing full-length content such as recorded webinars, training sessions, product demonstrations, and extended presentations to be delivered without splitting the footage into shorter segments.

Because Dynamic Media accommodates files as large as **50 GB**, high-resolution and high-bitrate footage can be uploaded and streamed while preserving quality. The **2-hour** duration ceiling ensures that long-form assets fit within a single continuous file, which simplifies content management and playback for viewers.

## How Dynamic Media with OpenAPI capabilities is different from Dynamic Media solution? {#dynamic-media-and-dynamic-media-with-openapi-differences}

Dynamic Media with OpenAPI capabilities and Dynamic Media are distinct solutions, each offering its own specialized delivery capabilities. Thoroughly review your specific requirements to determine the solution that best aligns with your needs.

**Adobe's general guidance is to leverage the Dynamic Media with OpenAPI (Open Application Programming Interface) stack for any integration use cases, whether they involve 1st-party or 3rd-party applications.** Because the two stacks use different URL structures, use the following decision rules to choose the right approach:

- **Existing integrations:** If an integration already exists with the Dynamic Media stack, do not change it, because the OpenAPI stack URLs differ in structure.
- **Net-new integrations:** For any net-new integration use case, leverage the OpenAPI stack.
- **Advanced modifiers:** If your use case requires advanced modifiers not yet available with the OpenAPI stack, avoid the OpenAPI stack until Adobe bridges the gap.
- **Basic native delivery:** Even for basic native delivery from Adobe Experience Manager (AEM) Assets Cloud Services, the OpenAPI stack can be evaluated, as long as your use case is covered by the modifiers available with the OpenAPI stack.

In conclusion, Dynamic Media and the Dynamic Media with OpenAPI stack can co-exist, depending on the nature of your use case.

The following are some of the key differences between Dynamic Media with OpenAPI capabilities and Dynamic Media:

| Dynamic Media with OpenAPI capabilities | Dynamic Media |
|---|---|
| [Available only with Assets as a Cloud Service](/help/assets/dynamic-media-open-apis-overview.md#prerequisites-dynaminc-media-open-apis) | Also available with On-premise or Adobe Managed Services with additional configuration and provisioning steps. |
| [Rich set of supported image modifiers, such as width, height, rotate, flip, quality, and format](/help/assets/deliver-assets-apis.md) | Rich set of available image modifiers |
| [Restricted asset delivery based on users, roles, date, and time](/help/assets/restrict-assets-delivery.md) | Assets published to Dynamic Media are accessible to all users |
| Most developers are familiar with **OpenAPI specifications**, a widely adopted standard for describing APIs. Adobe Experience Manager (AEM) Assets extensibility becomes really simple by using [Content Advisor](/help/assets/integrate-adobe-non-adobe-applications.md). | **SOAP (Simple Object Access Protocol)-based APIs**, which become a barrier while developing integration customizations. |
| Any changes made to approved assets in Digital Asset Management (DAM), including version updates and metadata modifications, are automatically reflected in the delivery URLs. With a short **Time-to-Live (TTL) value of 10 minutes** configured for Dynamic Media with OpenAPI capabilities via Content Delivery Network (CDN), updates become visible across all authoring and published interfaces in **under 10 minutes**. | Recommended CDN TTL of **10 hours**. You can override the TTL value using the cache invalidation action. |
| Only approved assets are available for asset delivery to downstream applications, enabling on-brand approved assets in digital experiences.| Any updates to a Dynamic Media published asset are auto-published without any approval workflow, which does not ensure on-brand approved assets in digital experiences.    |
| Usage reports based on number of assets delivered. This feature will be available soon.| Usage reports are not available. This feature will be available soon. |
| Assets marked as Expired on the Assets as a Cloud Service repository are no longer available to downstream applications.| No inherent asset expiry. An asset remains public until it is deleted from AEM as a Cloud Service repository.|
| Does not support video smart crop capabilities.| Supports video smart crop capabilities. |
| **Dynamic video encodes** ensure the best encodes are served based on the input video, so no setup is required for native video delivery.| **Standard 3 encodes** irrespective of input video, which can impact video delivery performance. You must manually set up different encodes for different video bit rates. |
| Enables secure, **obfuscated URLs using asset UIDs** without compromising Search Engine Optimization (SEO). | URL obfuscation is only available for URL query parameters. Asset IDs (asset names) in URLs are recognizable. |

## How Dynamic Media with OpenAPI capabilities addresses the limitations of the Connected Assets feature? {#dynamic-media-openapi-addresses-connected-assets-limitations}

Dynamic Media with OpenAPI capabilities overcomes the core limitations of the Connected Assets feature by eliminating binary copying, supporting all AEM Assets format types (including videos), removing the four-instance connection limit, enabling extensible custom integrations, and delivering near-real-time asset updates. The table below outlines the key differences between the two solutions:

| Dynamic Media with OpenAPI capabilities | Connected Assets |
|---|---|
| Assets on the remote Digital Asset Management (DAM) deployment are available on AEM as a Cloud Service. | Assets on the remote DAM deployment can be available on AEM as a Cloud Service or Adobe Managed Services. |
| Asset binaries are **not** copied when assets on a remote DAM deployment are made available on an AEM Sites instance. Because the binaries remain at the source, this avoids duplicating storage and keeps a single source of truth for each asset. | Asset binaries are copied when assets on a remote DAM deployment are made available on an AEM Sites instance. |
| Supports **all asset format types** that are supported by AEM Assets, including videos. | No support for videos. |
| You can use Dynamic Media on the local Sites deployment while fetching assets from the remote DAM deployment. | Dynamic Media on the local Sites deployment is read-only. |
| **No restrictions** on the number of AEM Sites instances connected to a remote DAM deployment. You can [restrict the access to assets on the Sites instance by configuring roles](/help/assets/restrict-assets-delivery.md) for approved assets on the remote DAM. | Restriction to connect **no more than 4 AEM Sites instances** to the remote DAM deployment. An increased number requires additional testing. |
| Both Content Advisor and Dynamic Media with OpenAPI capabilities are **extensible** to allow custom integrations. | Connected Assets APIs are **not extensible** to allow custom integrations. |
| Any changes made to approved assets available on the remote DAM deployment, including version updates and metadata modifications, are automatically reflected on the Sites instance within a short **Time-to-Live (TTL) value of 10 minutes**. | Asset updates on the remote DAM deployment are handled via lifecycle events automatically, but take much more time compared to Dynamic Media with OpenAPI capabilities. |
| Asset metadata on the remote DAM is available on the AEM Sites instance as well. | Asset metadata on the remote DAM is not available on the AEM Sites instance. |

## Some modifiers are marked as Limited Availability. How can I start using them? {#use-limited-availability-modifiers}

Limited Availability modifiers require explicit enablement on your account before they can be used in production. Adobe does not activate these modifiers by default, so you must request access through Adobe Support. The process consists of two steps: opening a support case and providing the identifying details Adobe needs to provision the requested capabilities.

To enable the production use of [modifiers in Limited Availability](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/stable/assets/delivery/) on your account:

1. [Create an Adobe Support case using Admin Console](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

1. Mention the following details within the Adobe Support case so that Adobe can identify your organization and provision the requested capabilities:

   * **IMS Org** (Identity Management System Organization identifier)

   * List of modifiers to be enabled

1. Submit the case and wait for Adobe Support to confirm that the requested Limited Availability modifiers have been enabled for your IMS Org. Once Adobe confirms enablement, the specified modifiers become available for production use on your account.

## How do I test experimental modifiers? {#modifiers-not-generally-available}

**Experimental APIs let you test any modifier that is not yet generally available.** Experimental (or beta) APIs give developers early access to functionality that is still under evaluation, so you can validate new modifiers before they are promoted to the stable, generally available set. This allows you to trial upcoming capabilities, confirm they behave as expected in your workflows, and provide feedback ahead of a general release.

To test a modifier that is not generally available, invoke it through the experimental API path. For example:

`</adobe/experimental/advancemodifiers-expires-YYYYMMDD/assets>`

The `expires-YYYYMMDD` segment indicates that the experimental modifier is time-bound, signaling the date by which the experimental version is expected to change or expire — a reminder to migrate to the generally available equivalent once it is released.

For details on invoking these endpoints, refer to the guidance on how to use the [experimental APIs](https://developer.adobe.com/experience-cloud/experience-manager-apis/guides/how-to/#experimental-apis). To identify which modifiers are available, consult the [complete list of modifiers](https://developer.adobe.com/experience-cloud/experience-manager-apis/).

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
