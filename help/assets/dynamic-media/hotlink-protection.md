---
title: Activate hotlink protection in Dynamic Media
description: Learn how to activate hotlink protection in Dynamic Media.
contentOwner: Rick Brough
feature: Asset Management
role: User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 0198b3a3-173e-46ca-a845-3f58f8eab769
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---
# Activate hotlink protection in Dynamic Media {#activating-hotlink-protection-in-dynamic-media}

Hotlinking is when a third-party website uses HTML code to display an image from your website. Bandwidth is consumed every time the image is requested because the visitor's browser is accessing it directly from your server. Hotlink *protection* is a method to prevent other websites from directly linking to pictures, CSS, or JavaScript on your web pages. This protection helps reduce unnecessary bandwidth usage for your Dynamic Media account.

[Adobe Customer Support](https://experienceleague.adobe.com/?support-solution=Experience+Manager#home) can configure a referrer filter at the CDN level. Doing so ensures that Dynamic Media content is only served to websites on your list of permitted websites for that domain.

>[!NOTE]
>
>This feature requires that you use the standard CDN that is bundled with Adobe Experience Manager Dynamic Media. No other custom CDN is supported with this feature. To activate hotlink protection, an administrator must submit a support request to change the configuration of your Dynamic Media account. There is no additional cost for activating hotlink protection.
