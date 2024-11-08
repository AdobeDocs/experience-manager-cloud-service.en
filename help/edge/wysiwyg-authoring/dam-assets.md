---
title: Publishing Pages with DAM Assets Using Edge Delivery Services
description: Learn what settings are required to ensure your DAM assets for your pages are published seamlessly to Edge Delivery Services.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: 160f0474-a72d-4183-a2b2-2f8ba177605d
---
# Publishing Pages with DAM Assets Using Edge Delivery Services {#dam-assets}

Learn what settings are required to ensure your DAM assets for your pages are published seamlessly to Edge Delivery Services.

## Universal Editor, DAM Assets, and Edge Delivery {#overview}

When editing content for the Universal Editor, you of course can select assets from the DAM. When you publish your content to Edge Delivery Services, the related DAM content is published as well.

To ensure this seamless behavior, AEM and Edge Delivery Services must have proper access to the DAM in order to publish. This includes:

* [Ensuring that assets folders are accessible.](#accessible)
* [Ensuring that the assets folder is assigned the proper configuration (as required).](#configuration)

## Ensuring Assets Folders are Accessible {#accessible}

When publishing pages from AEM to Edge Delivery Services, [a technical account](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md) is used. This account, with a name in the format `<hash>@techacct.adobe.com`, is created automatically as a user in AEM by Cloud Manager whenever you first publish a page created with the Universal Editor.

![Technical account](/help/edge/wysiwyg-authoring/assets/dam-assets/technical-account.png)

This technical account must have access rights to all DAM folders in order to publish their content. You can either:

* Not use private DAM folders.
* Grant the technical account user access to the DAM folders.

## Ensuring Assets Folder is Assigned Proper Configuration {#configuration}

Generally assuring that your technical account has access to your assets in DAM is sufficient for publishing your assets along with your pages to Edge Delivery Services.

Additional configuration is needed in two additional cases, however:

* If you wish to publish pages with non-image assets such as PDFs or videos to Edge Delivery Services.
* If you wish to publish image assets to Edge Delivery Services independently of pages.

To support both these use cases, a [configuration](/help/implementing/developing/introduction/configurations.md) must be assigned to the DAM folder.

1. Sign into your AEM authoring environment.
1. Under **Sites** select the site where you are publishing your assets or the site with which the assets will be associated.
1. Tap or click **Properties** in the tool bar.
1. On the **Advanced** tab in the properties window, take note of the configuration in the field **Cloud Configuration**.
   * This is created automatically when you create your site in the format `/conf/<site-name>`.
1. Tap or click **Cancel** in the properties window and navigate to **Assets** -&gt; **Files** and select your DAM folder.
1. Tap or click **Properties** in the tool bar.
1. On the **Cloud Services** tab of the properties window, in the **Cloud Configuration** field, select the same configuration as you noted previously.
1. Tap or click **Save &amp; Close**.
