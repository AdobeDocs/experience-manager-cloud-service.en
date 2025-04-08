---
title: Creating Content Fragments - Headless Setup
description: Learn how to use AEM's Content Fragments to design, create, curate, and use page-independent content for headless delivery.
exl-id: a227ae2c-f710-4968-8a00-bfe48aa66145
feature: Headless, Content Fragments,GraphQL API
role: Admin, Developer
---
# Creating Content Fragments - Headless Setup {#creating-content-fragments}

Learn how to use AEM's Content Fragments to design, create, curate, and use page-independent content for headless delivery.

## What are Content Fragments? {#what-are-content-fragments}

[Now that you have created an assets folder](create-assets-folder.md) where you can store your Content Fragments, you can now create the fragments!

Content Fragments allow you to design, create, curate, and publish page-independent content. They allow you to prepare content ready for use in multiple locations and over multiple channels.

Content fragments contain structured content and can be delivered in JSON format.

## How to Create a Content Fragment {#how-to-create-a-content-fragment}

Content authors will create any number of Content Fragments to represent the content that they create. This is their main task in AEM. For the purposes of this getting started guide, we will only need to create one.

1. Log into AEM as a Cloud Service and from the main menu select **Navigation** &gt; **Content Fragments**.

1. Select the [folder you created previously](create-assets-folder.md).
1. Select **Create**.
1. The creation of a Content Fragment is presented as a dialog. 
   Select the location and model you want to use to create your content fragment.
   
   * The models available depend on the [**Cloud Configuration** you defined for the assets folder](create-assets-folder.md) in which you are creating the Content Fragment.
   * If your model is not available, check the configuration of your assets folder.

   Add the Title, Name, and if necessary, Description.

   ![Create New Content Fragment dialog](/help/sites-cloud/administering/content-fragments/assets/cfc-console-create.png)

1. Select **Create** or  **Create and open**.

Content Fragments can reference other Content Fragments, allowing for a nested content structure if necessary.

Content Fragments can also reference other assets in AEM. [These assets need to be stored in AEM](/help/assets/manage-digital-assets.md) before creating a referencing Content Fragment.

## Next Steps {#next-steps}

Now that you have created a Content Fragment, you can move on to the final part of the getting started guide and [create API requests to access and deliver content fragments](create-api-request.md).

>[!TIP]
>
>For complete details about managing Content Fragments, see the [Content Fragments documentation](/help/sites-cloud/administering/content-fragments/overview.md).
