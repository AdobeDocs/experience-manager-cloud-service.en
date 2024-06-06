---
title: Release Notes for Cloud Manager 2024.6.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2024.6.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
---

# Release Notes for Cloud Manager 2024.6.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2024.6.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2024.6.0 in AEM as a Cloud Service is 6 June 2024. The next release is planned for 11 July 2024.

## What's New {#what-is-new}

* You can now [use your own GitHub repositories](/help/implementing/cloud-manager/managing-code/private-repositories.md) as sources for both full-stack and frontend pipelines.
  * Additionally, you can take advantage of GitHub repositories with [git submodules,](/help/implementing/cloud-manager/managing-code/git-submodules.md) providing you with enhanced control over the auto-generated pipelines used for pull request validation and allowing you to define behaviors for crucial metrics during the code scanning phase.
  * [You also have the choice](/help/implementing/cloud-manager/managing-code/github-check-config.md) to preserve the report history on GitHub, name the pipeline, and set pipeline variables to suit your needs.
* [Self-service content restore](/help/operations/restore.md) provides backup restoration for up to seven days and features:
  * Point-in-time backup restoration for the previous 24 hours
  * Fixed time restorations for up to seven days

## Early Adoption Program {#early-adoption}

For a chance to test some upcoming features, be a part of Adobe's early adoption program.

### Edge Delivery Services Support in Cloud Manager {#edge-delivery-services}

If you have licensed Edge Delivery Services as part of Adobe Experience Manager Sites, [you can now onboard your site with Edge Delivery Services directly in Cloud Manager](/help/implementing/cloud-manager/edge-delivery-services.md) and go live using a guided, self-service experience.

This enables a unified experience for all of your AEM properties, ensuring consistency with all critical workflows including domain name management, SSL certificate management, and CDN mappings.

If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-cmedgedelsvs-program-adopter@adobe.com` from the email address associated with your Adobe ID. 

### Domain Validated (DV) Certificates

Cloud Manager now allows you to [self-service generate and manage domain validated (DV) SSL certificates.](/help/implementing/cloud-manager/managing-ssl-certifications/domain-validated-certificates.md) This gives you the fastest, easiest, and most cost-effective solution to create a secure website for your online business.

If you are interested in testing this new feature and sharing your feedback, please send an email to `Grp-aemcs-dv-dert-adopter@adobe.com` from the email address associated with your Adobe ID.

### Client-Side Collection via Real User Monitoring (RUM) {#rum}

You can leverage the [Real User Monitoring (RUM) Data Service](/help/implementing/cloud-manager/content-requests.md#cliendside-collection) to enable client-side collection for AEM as a Cloud Service.

Real User Monitoring (RUM) Data Service offers a more precise reflection of user interactions, ensuring a reliable measure of website engagement. It is a great opportunity to gain advanced insights into your page performance. This is beneficial for customers who use either Adobe-managed CDN or non-Adobe managed CDN. For customers using a non-Adobe managed CDN, automated traffic reporting can now be enabled for them, thus removing the need to share any traffic report with Adobe.

If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-rum-adopter@adobe.com` from the email address associated with your Adobe ID. Please include the domain name for production, stage, and dev environments in your email.  Availability of the early adopter program of this feature is limited.

### Experience Audit Dashboard {#experience-audit-dashboard}

[The Cloud Manager Experience Audit dashboard](/help/implementing/cloud-manager/experience-audit-dashboard.md) includes a trended view of your page performance scores along with insights and recommendations to help you improve them. Experience Audit is included as a step in the Cloud Manager production pipeline.

The dashboard uses Google Lighthouse, an open-source, automated tool for improving the quality of your web apps. You can run it against any web page, public, or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO, and more.

Interested in test-driving the new dashboard? To get started, send an email to `aem-lighthouse-pilot@adobe.com` from your email associated with your Adobe ID.
