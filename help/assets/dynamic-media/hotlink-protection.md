---
title: Activate hotlink protection in Dynamic Media
description: Learn how to activate hotlink protection in Dynamic Media.
contentOwner: Rick Brough
feature: Asset Management
role: User
exl-id: 0198b3a3-173e-46ca-a845-3f58f8eab769
---
# Activate hotlink protection in Dynamic Media {#activating-hotlink-protection-in-dynamic-media}

Hot linking is when a third-party website uses HTML code to display an image from your website. They use your bandwidth every time the picture is requested because the visitor's browser is accessing it directly from your server. Hotlink *protection* is a method to prevent other websites from directly linking to pictures, CSS, or JavaScript on your web pages. This kind of shield helps reduce unnecessary bandwidth usage under your Dynamic Media account.

[Adobe Customer Support](https://experienceleague.adobe.com/?support-solution=Experience+Manager#home) can configure a referrer filter at the CDN level. Doing so ensures that Dynamic Media content is only served to websites on your list of permitted websites for the domain.

>[!NOTE]
>
>This feature requires that you use the out-of-the-box CDN that is bundled with Adobe Experience Manager Dynamic Media. Any other custom CDN is not supported with this feature. To activate hot link protection, an Administrator must create a support ticket to request the configuration change to your Dynamic Media account. There is no additional cost for activating hot link protection.
