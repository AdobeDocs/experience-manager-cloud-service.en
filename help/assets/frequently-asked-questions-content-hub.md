---
title: Content Hub frequently asked questions (FAQs)
description: Get responses to some of the most frquently asked questions (FAQs) for Content Hub.
---
# Content Hub frequently asked questions {#content-hub-frequently-asked-questions}

![Content Hub frequently asked question](assets/content-hub-faqs.png)

## What is Content Hub? {#what-is-content-hub} 

Content Hub is a feature of Adobe Experience Manager Assets as a Cloud Service. 

Content Hub enables broader teams to easily discover relevant, approved assets through an intuitive portal and quickly adapt them to their needs.  In addition, Content Hub provides an ingestion mechanism that allows those users to easily self–serve as they upload assets into the DAM. This directly accommodates the need organizations have for higher content creation velocity, while preserving brand consistency and compliance with appropriate safeguards.

## Why cannot I enable Content Hub on my Cloud Manager program/environment? {#cannot-enable-content-hub}

Content Hub is at this point is only available on AEM Cloud Manager Production programs, which include an Assets license. When you click [Content Hub](/help/assets/deploy-content-hub.md#enable-content-hub) to enable it, it is deployed and associated with the author production environment of AEM in that program. See [Deploy Content Hub](/help/assets/deploy-content-hub.md) for details and prerequisites.

Content Hub is not available for other program types, such as Sandbox programs, nor for non-production environments (stage, dev, and so on).

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

## Why do not I see any assets after logging on to Content Hub? {#no-assets-in-content-hub}

The assets marked as approved in Assets as a Cloud Service are automatically available in Content Hub. If you cannot view any assets after logging on to Content Hub, approve assets using the AEM as a Cloud Service author environment to make them available in Content Hub. For more information, see [Approve assets for Content Hub](/help/assets/approve-assets-content-hub.md).

## Why do not I see my assets that I either upload directly using Content Hub or import them from Dropbox or OneDrive accounts using Content Hub? {#no-assets-uploaded-from-content-hub}

The display of assets uploaded using Content Hub depends on if you have enabled the [Auto-approval](/help/assets/configure-content-hub-ui-options.md#configure-import-options-content-hub) toggle available on the Configuration user interface:

* If the **Auto-approval** toggle is enabled, the assets that you upload using Content Hub are automatically available.

* If the **Auto-approval** toggle is disabled, the assets that you upload using Content Hub do not display automatically. The assets are available in the `hydrated-assets` folder of your Assets as a Cloud Service environment. Navigate to the folder and [bulk edit](/help/assets/approve-assets-content-hub.md) the status of those assets to `Approved` for those assets to display in Content Hub.

## Why do not I view the edit using Adobe Express option on my asset card to be able to remix assets to create new variations? {#edit-using-express-not-available}

To view the edit using Adobe Express option on the asset card, you must have Adobe Express entitlements in addition to privileges for [Content Hub users with rights to remix assets to new variations](#onboard-content-hub-users-add-assets).




