---
title: Publishing Pages with DAM Assets Using Edge Delivery Services
description: Learn what settings are required to ensure your DAM assets for your pages are published seamlessly to Edge Delivery Services.
feature: Edge Delivery Services
exl-id: 26d4db90-3e4b-4957-bf21-343c76322cdc
role: Admin, Architect, Developer
---

# Publishing Pages with DAM Assets Using Edge Delivery Services {#dam-assets}

Learn what settings are required to ensure your DAM assets for your pages are published seamlessly to Edge Delivery Services.

## Universal Editor, DAM Assets, and Edge Delivery {#overview}

When editing content for the Universal Editor, you of course can select assets from the DAM. When you publish your content to Edge Delivery Services, the related DAM content is published as well.

To ensure this seamless behavior, AEM and Edge Delivery Services must have proper access to the DAM in order to publish. This includes:

* [Ensuring that assets folders are accessible.](#accessible)
* [Ensuring that the assets folder is assigned the proper configuration (as required).](#configuration)

## Ensuring Assets Folders are Accessible {#accessible}

When publishing pages from AEM to Edge Delivery Services, [a technical account](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md) is used. This account, with a name in the format `<hash>@techacct.adobe.com`, is created automatically as a user in AEM by Cloud Manager whenever you first publish a page.

![Technical account](/help/edge/wysiwyg-authoring/assets/dam-assets/technical-account.png)

This technical account must have access rights to all DAM folders in order to publish their content. You can either:

* Not use private DAM folders.
* Grant the technical account user access to the DAM folders.

## Ensuring Assets Folder is Assigned Proper Configuration {#configuration}

