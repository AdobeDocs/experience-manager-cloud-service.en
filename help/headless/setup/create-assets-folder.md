---
title: Creating an Assets Folder - Headless Setup
description: Use AEM Content Fragment Models to define the structure of Content Fragments, the basis of your headless content.
exl-id: 9a156a17-8403-40fc-9bd0-dd82fb7b2235
feature: Headless, Content Fragments,GraphQL API
role: Admin, Developer
---
# Creating an Assets Folder - Headless Setup {#creating-an-assets-folder}

Use AEM Content Fragment Models to define the structure of Content Fragments, the basis of your headless content. Content Fragments are then stored in assets folders.

## What is an Assets Folder? {#what-is-an-assets-folder}

[Now that you have created Content Fragment Models](create-content-model.md) that define the structure that you want for your future Content Fragments, you are probably excited to create some fragments.

However you first need to create an assets folder where you will store them.

Assets folders are used to [organize traditional content assets](/help/assets/manage-digital-assets.md) such as images and videos, together with Content Fragments.

## Create and configure an Assets Folder {#create-and-configure-an-assets-folder}

An administrator would only need to create folders occasionally to organize content as it is created. Use the Assets console to create your new folder.

Once created, you need to apply your [configuration](/help/headless/setup/create-configuration.md) to the folder. For details see [Apply the Configuration to your Folder](/help/sites-cloud/administering/content-fragments/setup.md#apply-the-configuration-to-your-folder).

You can create additional subfolders within the folder you created. The subfolders will inherit the **Cloud Configuration** of the parent folder. This can be overridden however if you want to use models from another configuration.

If you are using a localized site structure, you can [create a language root](/help/assets/translate-assets.md) below your new folder.

## Next Steps {#next-steps}

Now that you have created a folder for your Content Fragments, you can move on to the fourth part of the getting started guide and [create content fragments](create-content-fragment.md).

>[!TIP]
>
>For complete details about managing Content Fragments, see the [Content Fragments documentation](/help/sites-cloud/administering/content-fragments/overview.md)
