---
title: HTTP2 Delivery of Content FAQ
description: Learn about HTTP2 content delivery and how it improves communication between browsers and servers for faster information transfer.
contentOwner: Rick Brough
feature: Dynamic Media,Configuration,FAQ
role: Admin,User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 0a8a5fd8-a341-4e7f-84a5-409e2de97efe
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---
# HTTP/2 Delivery of Content FAQ{#http-delivery-of-content-faq}

Adobe announces the availability of HTTP/2 delivery of content. When using HTTP/2, performance increases.

>[!NOTE]
>
>This feature requires that you use the standard Content Delivery Network that is bundled with Adobe Experience Manager - Dynamic Media. Any other custom Content Delivery Network is not supported with this feature.

## What is HTTP/2? {#what-is-http}

HTTP/2 improves the way browsers and servers communicate. It allows for faster transfer of information while reducing the amount of processing power that is needed.

The website article [What you must know about HTTP/2](https://www.engadget.com/2015-02-24-what-you-need-to-know-about-http-2.html) describes HTTP/2 and its benefits concisely.

## What are the key benefits of moving to HTTP/2 for content delivery? {#what-are-the-key-benefits-of-moving-to-http-for-content-delivery}

Performance improvement varies widely because it is based on various factors. For example, your website code, Dynamic Media usage, and the user's device or location.

Adobe's own testing yielded the following results:

* For images, response time improved 7%-28% depending on device and browser. The most significant performance gains were on iOS devices.
* For viewers, load time performance improved by up to 15%.

## Am I eligible to transition to HTTP/2? {#am-i-eligible-to-switch-over-to-http}

To use HTTP/2, you must meet the following requirements:

* Use secure HTTPS for your rich media requests.
* Use the Adobe-bundled CDN (Content Delivery Network) as part of your Dynamic Media Classic license.
* Use a dedicated domain (that is, `images.company.com` or `mycompany.scene7.com`), not a generic Dynamic Media domain (that is, `s7d1.scene7.com`, `s7d2.scene7.com`, or `s7d13.scene7.com`).

  To find your domains, open the [Dynamic Media Classic desktop application](https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/getting-started/signing-out#getting-started), then sign in to your account.

  Go to **[!UICONTROL Setup]** > **[!UICONTROL Application Setup]** > **[!UICONTROL General Settings]**. Look for the field labeled **Published Server Name**. If you are currently using a generic Dynamic Media domain, you can request a change to your own custom domain as part of this transition.

## What is the process for enabling HTTP/2 for my Dynamic Media account? {#what-is-the-process-for-enabling-http-for-my-dm-account}

[Use the Admin Console to create a support case](https://helpx.adobe.com/business/enterprise.html) and request to switch to HTTP/2; it is not automatically done for you.

1. Provide the following information in your support case:

     * Primary contact, email, and phone number.
     * All domains to be transitioned to HTTP/2. That is, `images.company.com` or `mycompany.scene7.com`.

     To find your domains, open the [Dynamic Media Classic desktop application](https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/getting-started/signing-out#getting-started), then sign in to your account.

     Go to **[!UICONTROL Setup]** > **[!UICONTROL Application Setup]** > **[!UICONTROL General Settings]**. Look for the field labeled **[!UICONTROL Published Server Name]**.

     * Verify that you use secure HTTPS for rich media requests.
     * Verify you are using the CDN through Adobe and not one managed with a direct relationship.
     * Verify you are using a dedicated domain. That is, `images.company.com` or `mycompany.scene7.com`, not a generic Dynamic Media domain such as `s7d1.scene7.com`, `s7d2.scene7.com`, `s7d13.scene7.com`.

     To find your domains, Open the [Dynamic Media Classic desktop application](https://experienceleague.adobe.com/en/docs/dynamic-media-classic/using/getting-started/signing-out#getting-started), then sign in to your account.

     Go to **[!UICONTROL Setup]** > **[!UICONTROL Application Setup]** > **[!UICONTROL General Settings]**. Look for the field labeled **[!UICONTROL Published Server Name]**. If you are currently using a generic Dynamic Media domain, you can request changing to your own custom domain as part of this transition.

     1. Customer Support adds you to the HTTP/2 customer queue based on the order in which requests were submitted.
     1. When Adobe is ready to handle your request, Customer Support contacts you to coordinate the transition and set a target date.
     1. You are notified after completion and can verify a successful transition to HTTP/2.

## When can I expect to be transitioned to HTTP/2? {#when-can-i-expect-to-be-transitioned-over-to-http}

Customer Support processes requests in the order that they are received.

>[!NOTE]
>
>There is a delay because the transition to HTTP/2 involves removing cached data. Therefore, only a limited number of customer transitions can be handled at a time.

## What are the risks with moving to HTTP/2? {#what-are-the-risks-with-moving-to-http}

The transition to HTTP/2 removes your cached data at the CDN because it involves moving to a new CDN configuration.

The non-cached content is sent directly to Adobe's origin servers until the cache is refreshed. Therefore, Adobe plans to process a limited number of customer transitions at a time. This method ensures that acceptable performance is maintained when retrieving requests from the origin.

## How can you verify whether a URL or website is activated with HTTP/2? {#how-can-you-verify-whether-a-url-or-website-is-activated-with-http}

Download an extension to use with your Web browser. For Firefox and Chrome, there is an extension called **[!UICONTROL HTTP/2 and SPDY Indicator]**. Browsers only support HTTP/2 securely, so it is necessary to call a URL with HTTPS to verify. If HTTP/2 is supported, the extension indicates it with a blue symbol, and a header "X-Firefox-Spdy": "h2."
