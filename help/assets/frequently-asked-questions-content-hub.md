---
title: Content Hub frequently asked questions (FAQs)
description: Get responses to some of the most frequently asked questions (FAQs) for Content Hub.
exl-id: 74b5c308-c1d3-4787-9f1f-f64cf09d298a
---
# Content Hub frequently asked questions {#content-hub-frequently-asked-questions}

![Content Hub frequently asked question](assets/content-hub-faqs.png)

## What is Content Hub? {#what-is-content-hub} 

Content Hub is a feature of Adobe Experience Manager Assets as a Cloud Service.

Content Hub enables broader teams to easily discover relevant, approved assets through an intuitive portal and quickly adapt them to their needs.  In addition, Content Hub provides an ingestion mechanism that allows those users to easily self–serve as they upload assets into the DAM. This directly accommodates the need organizations have for higher content creation velocity, while preserving brand consistency and compliance with appropriate safeguards.

## Why cannot I enable Content Hub on my Cloud Manager program/environment? {#cannot-enable-content-hub}

Content Hub is at this point is only available on AEM Cloud Manager Production programs, which include an Assets license (Assets Cloud Service, Assets Ultimate, Assets Prime). When you click [Content Hub](/help/assets/deploy-content-hub.md#enable-content-hub) to enable it, it is deployed and associated with the author production environment of AEM in that program. See [Deploy Content Hub](/help/assets/deploy-content-hub.md) for details and prerequisites.

## I enabled Content Hub on my production program/environment, can I disable it? {#can-i-disable-content-hub}

Enabling Content Hub on a production program deploys it a part of production infrastructure. AEM Cloud Manager does not allow for removing or disabling production infrastructure to minimize risk to production usage by human errors. 

If you do not want to provide Content Hub to your users once it is deployed, do not assign any users to the Content Hub product profile in Admin Console. See [Deploy Content Hub](/help/assets/deploy-content-hub.md#content-hub-instance-product-profile) for details.

## How can I evaluate Content Hub in my organization given it is only available for production programs / production authoring environments? {#how-can-i-evaluate-content-hub}

Content Hub is a feature that Adobe provides and maintains and it does not have any custom code that would require typical validation via dev/stage/production. Additionally, access to the feature for users is fully controlled by the administrator, so you can evaluate it without exposing it to all users. 

It is possible to evaluate Content Hub without impacting your users/production content managed in AEM as a Cloud Service Assets. An evaluation procedure could look like this:

* [Enable Content Hub](/help/assets/deploy-content-hub.md#enable-content-hub) on production environment (Cloud Manager program)
* [Add an AEM Administrator user](/help/assets/deploy-content-hub.md#onboard-content-hub-administrator) from the production author to Content Hub product profile.
* AEM Administrator [configures Content Hub](/help/assets/configure-content-hub-ui-options.md)
* AEM Administrator or an AEM User on AEM production author [approves a number of assets for Content Hub](/help/assets/approve-assets-content-hub.md); if you do not want to change any production content in DAM, you might want to create a separate evaluation folder in the AEM author instance, and upload/tag or copy some assets from DAM into it.
* Admin Console administrator adds [a few selected users](/help/assets/deploy-content-hub.md#onboard-content-hub-users) to the Content Hub product profile, so that they can start evaluation.
* After the evaluation is completed, AEM Users in author instance can remove approval from test assets, approve production assets for Content Hub, and then Admin Console administrator can add all users who need access to Content Hub and approved content. Congratulations, your Content Hub is live now.

There is an early access program to Content Hub on Sandbox programs and their author production environments. For more information, see [Introduction to Sandbox Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md). To learn more about the early access program, reach out to your Adobe account team. 

Content Hub is not yet available for non-production environments (stage & dev). Expected availability for stage/dev environments for Assets Ultimate is March 2025.

## Why do not I see any assets after logging on to Content Hub? {#no-assets-in-content-hub}

The assets marked as approved in Assets as a Cloud Service are automatically available in Content Hub. If you cannot see any assets after logging on to Content Hub, approve assets using the AEM as a Cloud Service author environment to make them available in Content Hub. For more information, see [Approve assets for Content Hub](/help/assets/approve-assets-content-hub.md).

## Why do not I see my assets that I either upload directly using Content Hub or import them from Dropbox or OneDrive accounts using Content Hub? {#no-assets-uploaded-from-content-hub}

The display of assets uploaded using Content Hub depends on if you have enabled the [Auto-approval](/help/assets/configure-content-hub-ui-options.md#configure-import-options-content-hub) toggle available on the Configuration user interface:

* If the **Auto-approval** toggle is enabled, the assets that you upload using Content Hub are automatically available.

* If the **Auto-approval** toggle is disabled, the assets that you upload using Content Hub do not display automatically. The assets are available in the `hydrated-assets` folder of your Assets as a Cloud Service environment. Navigate to the folder and [bulk edit](/help/assets/approve-assets-content-hub.md) the status of those assets to `Approved` for those assets to display in Content Hub.

## How to quickly find assets uploaded using Content Hub on AEM as a Cloud Service environment? {#find-uploaded-assets-on-aem-cloud}

You can quickly find assets uploaded using Content Hub on AEM as a Cloud Service environment by:

1. Navigating to the `hydrated-assets` folder.

1. Clicking **[!UICONTROL Filters]** and setting **[!UICONTROL No Status]** in the **[!UICONTROL Asset Status]** field.

1. Sorting assets using the **[!UICONTROL Modified Date]** field.

## Why do not I see the Edit using Adobe Express option on my asset card to be able to remix assets to create new variations? {#edit-using-express-not-available}

To view the **Edit using Adobe Express** option on the asset card, the user must have Adobe Express Enterprise or Teams entitlement (see [plans](https://www.adobe.com/express/pricing)) in addition to privileges for [Content Hub users with rights to remix assets to new variations](#onboard-content-hub-users-add-assets). 

There are a few configurations of how users are assigned to [!DNL Content Hub] & [!DNL Adobe Express]:

1. The organization has [Assets Ultimate](/help/assets/assets-ultimate-overview.md) or [Assets Prime](/help/assets/assets-prime.md) license, and the user is assigned to one of the Experience Manager profiles in Admin console that include Adobe Express entitlement (Collaborator or Power user). The integration works without any additional configuration.
   
1. [!DNL Adobe Express] is deployed in the same [!DNL Adobe Admin Console] as [!DNL Experience Manager Assets] with [!DNL Content Hub]. The integration works without any additional configuration.

1. [!DNL Adobe Express] is deployed in a different [!DNL Adobe Admin Console] than [!DNL Experience Manager Assets] with [!DNL Content Hub]. In this case, the [!DNL Assets] administrator can configure the integration (see [documentation](/help/assets/connect-assets-with-creative-cloud.md)) for the integration to work.

   >[!NOTE]
   >
   >The user assigned to Express and Assets product profiles in two Admin Consoles needs to have the same email address and use a business **Enterprise or School** account, and not the **Personal** one. The ideal configuration is to have both Admin Consoles set up as **Federated ID** with trust relationship set up between them, so that the user has a seamless single sign-on experience. Some of the Express plans (for example, Express Teams) does not support Federated ID / single sign-on.
 
In addition to the right product entitlements, Adobe Express integration in Content Hub requires that the assigned user has at least [!UICONTROL Can Edit] permissions on the Assets author environment powering Content Hub, on at least the **[#UICONTROL /content/dam/hydrated-assets/]** folder hierarchy, where Content Hub users can save content that they created using Express. See [Permissions Management](/help/security/touch-ui-principal-view.md) in the Admin view (Touch UI) or a simplified [permissions management in Assets view](https://experienceleague.adobe.com/en/docs/experience-manager-assets-essentials/help/get-started-admins/folder-access/manage-permissions).

## Can I setup Content Hub so that my organization's brand guidelines display as a link on the home page? {#content-hub-setup-brand-guidelines}

You can add custom links as separate tabs in addition to the standard All Assets, Collections, and Insights tabs on the Content Hub home page. For information on how to set it up, see [Custom Links](/help/assets/configure-content-hub-ui-options.md#configure-custom-links-content-hub). 

## Is there any plan on migrating existing Brand Portal customers to Content Hub? {#migration-brand-portal}

Adobe provides migration support from Brand Portal to Content Hub that you can use by creating an Adobe support ticket.

## Why cannot I see the Product Settings/Configuration option in Content Hub? {#ui-configuration-option-missing}

To access the [Configuration User Interface](/help/assets/configure-content-hub-ui-options.md), you need to be a [Content Hub Administrator](/help/assets/deploy-content-hub.md##onboard-content-hub-administrator). If you are assigned to the AEM Administrators product profile on the production author instance in Adobe Admin Console and you still cannot see the configuration option, ensure that the AEM Administrators product profile is not renamed. See [AEM as a Cloud Service Team and Product Profiles](/help/onboarding/aem-cs-team-product-profiles.md) for more details.

## How Content Hub addresses the limitations of Brand Portal? {#content-hub-brand-portal-comparison} 


The table below outlines the key differences between the two solutions:

| Area | Capability |Content Hub|Brand Portal|
|---|---|----|----|
| Configuring distribution experience | Configure metadata for filters, asset details, and add assets page |&#10003;|&minus;|
|  | Configure external links from portal |&#10003;|&minus;|
|  | Configure banner messaging |&#10003;|&#10003;|
|  | Configure banner image for branding |&#10003;|&#10003;|
|  | Configure primary and secondary colors for UI as per branding requirements |&#10003;|&minus;|
|Sharing assets from the DAM  | Sharing original approved assets from DAM |&#10003;|&#10003;|
|  | Approved asset changes synced automatically |&#10003;|&minus;|
| Search and filters | Dynamic filters (options show dynamically based on assets displayed) |&#10003;|&minus;|
|  | Search history |&#10003;|&minus;|
| Asset upload | Local drive |&#10003;|&#10003;|
|  | Add configurable metadata while uploading assets |&#10003;|&minus;|
| Download and renditions | Download original asset |&#10003;|&#10003;|
|  | Share and download static renditions from DAM |&#10003;|&#10003;|
|  | Download dynamic renditions (preset & smart crops)  |&#10003;|&#10003;|
|  | Ability to restrict view and download of expired assets  |&#10003;|&minus;|
|  Link sharing and Collections| Link share for signed-in users |&#10003;|&#10003;|
|  | Public collections |&#10003;|&#10003;|
|  | Search within collections |&#10003;|&minus;|
|  | Anonymous link share |&#10003;|&#10003;|
|  | Private collections |&#10003;|&#10003;|
|  Permissions| ACL-based permissions |&minus;|&#10003;|
|  | Attribute-based access control |&#10003;|&minus;|
|  Express integration| Edit Content Hub Assets in Adobe Express and save to DAM |&#10003;|&minus;|
|  Dashboards and reports| Insights dashboard |&#10003;|&minus;|
| UI Extensibility| Custom extension points on asset details page |Limited availability|&minus;|
|  Innovations coming soon| Favourite collections by user |&#10003;|&minus;|
|  | Pinned collections by Admin |&#10003;|&minus;|
|  | Semantic Search |&#10003;|&minus;|
|  | Localised search and metadata display |&#10003;|&minus;|


