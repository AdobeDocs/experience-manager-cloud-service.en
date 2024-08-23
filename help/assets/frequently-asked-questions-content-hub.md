---
title: Content Hub frequently asked questions (FAQs)
description: Get responses to some of the most frquently asked questions (FAQs) for Content Hub.
---
# Content Hub frequently asked questions {#content-hub-frequently-asked-questions}

## What is Content Hub? {#what-is-content-hub} 

Content Hub is a feature of Adobe Experience Manager Assets as a Cloud Service. 

Content Hub enables broader teams to easily discover relevant, approved assets through an intuitive portal and quickly adapt them to their needs.  In addition, Content Hub provides an ingestion mechanism allows those users to easily self–serve as they upload assets into the DAM. This directly accommodates the need organizations have for higher content creation velocity, while preserving brand consistency and compliance with appropriate safeguards.

## Why can't I enable Content Hub on my Cloud Manager program/environment? {#cannot-enable-content-hub}

Content Hub is at this point is only available on AEM Cloud Manager Production programs, which include an Assets license. When you click the "Content Hub" button, it is going to be deployed and associated with the author production environment of AEM in that program. See [Deploy Content Hub](/help/assets/deploy-content-hub.md) for details and prerequisites.

Content Hub is not available for other program types, like Sandbox programs, nor for non-production environments (stage, dev, etc).

## I enabled Content Hub on my production program/environment, can I disable it? {#can-i-disable-content-hub}

Enabling Content Hub on a production program deploys it a part of production infrastructure. AEM Cloud Manager does not allow for removing or disabling production infrastructure to minimize risk to production usage by human errors. 

If you don't want to provide Content Hub to your users once it was deployed, simply do not assign any users to the Content Hub product profile in Admin Console. See [Deploy Content Hub](/help/assets/deploy-content-hub.md#content-hub-instance-product-profile) for details.

## How can I evaluate Content Hub in my organization given it is only available for production programs / production authoring environments? {#how-can-i-evaluate-content-hub}

Content Hub is a feature that Adobe provides and maintains and it does not have any custom code that would require typical validation via dev/stage/prod. Additionally, access to the feature for users is fully controlled by the administrator, so you can evaluate it without exposing it to all users. 

Thus it is possible to evaluate Content Hub without impacting your users / production content managed in AEM CS Assets. An evaluation procedure could look like this:

* [Enable Content Hub](/help/assets/deploy-content-hub.md#enable-content-hub) on production environment (Cloud Manager program)
* [Add an AEM Administrator user](/help/assets/deploy-content-hub.md#onboard-content-hub-administrator) from the production author to Content Hub product profile
* AEM Administrator [configures Content Hub](/help/assets/configure-content-hub-ui-options.md)
* AEM Administrator or an AEM User on AEM production author [approves a number of assets for Content Hub](/help/assets/dynamicmedia/dynamic-media-open-apis/approve-assets.md); if you don't want to change any production content in DAM, you might want to create a separate evaluation folder in the author, and upload/tag or copy some assets from DAM into it
* Admin Console administrator adds [a few selected users](/help/assets/deploy-content-hub.md#onboard-content-hub-users) to the Content Hub product profile, so that they can start evaluation
* After the evaluation is completed, AEM Users in author can remove approval from test assets, and approve production assets for Content Hub, and then Admin Console administrator can add all users who need access to Content Hub and approved content. Congratulations, your Content Hub is live now!
