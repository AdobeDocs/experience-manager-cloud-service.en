---
title: Release Notes for Cloud Manager 2024.7.0 in Adobe Experience Manager as a Cloud Service
description: These are the release notes for Cloud Manager 2024.7.0 in AEM as a Cloud Service.
feature: Release Information
exl-id: 9c73d7ab-c2c2-4803-a07b-e9054220c6b2
role: Admin
---

# Release Notes for Cloud Manager 2024.7.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

This page documents the release notes for Cloud Manager release 2024.7.0 in AEM as a Cloud Service.

>[!NOTE]
>
>See [this page](/help/release-notes/release-notes-cloud/release-notes-current.md) for the current release notes for Adobe Experience Manager as a Cloud Service.

## Release Date {#release-date}

The release date for Cloud Manager release 2024.7.0 in AEM as a Cloud Service is 18 July 2024. The next release is planned for 8 August 2024.

## What's New {#what-is-new}

* The [production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline) and [non-production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md#adding-non-production-pipeline) trigger **On Git Changes** to start the pipeline on a commit t is now available for private repositories.
  * This will be rolled out in a phased manner with completion by mid-August.
* When adding an [Adobe-managed DV certificate,](/help/implementing/cloud-manager/managing-ssl-certifications/domain-validated-certificates.md) you can now add a single certificate that covers multiple domains instead of creating a certificate for each domain.
* Solutions that do not have [additional publish regions](/help/operations/additional-publish-regions.md) can now be added to a program as long as the program has at least a Sites or Forms solution applies to it.
* Solutions that do not have [99.99% SLA](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#sla) can now be added to a program as long as the program has at least a Sites or Forms solution applies to it.
* The [Experience Audit Dashboard](/help/implementing/cloud-manager/experience-audit-dashboard.md) has been enhanced in a number of ways.
  * Audits now run against `.com` endpoints via CDN, replacing the previous `.net` approach.
    * This change simulates real user experiences more accurately and helps you make more informed decisions about managing and optimizing your website.
  * Multiple enhancements were made to the Experience Audit UI including:
    * A trended view of performance, best practices, SEO, and accessibility was added.
    * The Lighthouse raw report link is now visible in a more intuitive way, directly in the scan snapshot details panel.
    * The Lighthouse recommendations section was enhanced.
  * The PWA metric was removed in accordance with Lighthouse version 12.0.0, which eliminated this metric.

## Early Adoption Program {#early-adoption}

For a chance to test some upcoming features, be a part of Adobe's early adoption program.

### Edge Delivery Services Support in Cloud Manager {#edge-delivery-services}

If you have licensed Edge Delivery Services as part of Adobe Experience Manager Sites, [you can now onboard your site with Edge Delivery Services directly in Cloud Manager](/help/implementing/cloud-manager/edge-delivery-services.md) and go live using a guided, self-service experience.

This enables a unified experience for all of your AEM properties, ensuring consistency with all critical workflows including domain name management, SSL certificate management, and CDN mappings.

If you are interested in testing this new feature and sharing your feedback, please send an email to `aemcs-cmedgedelsvs-program-adopter@adobe.com` from the email address associated with your Adobe ID. 

### Domain Validated (DV) Certificates

Cloud Manager now allows you to [self-service generate and manage domain validated (DV) SSL certificates.](/help/implementing/cloud-manager/managing-ssl-certifications/domain-validated-certificates.md) This gives you the fastest, easiest, and most cost-effective solution to create a secure website for your online business.

If you are interested in testing this new feature and sharing your feedback, please send an email to `Grp-aemcs-dv-dert-adopter@adobe.com` from the email address associated with your Adobe ID.

### Experience Audit Dashboard {#experience-audit-dashboard}

[The Cloud Manager Experience Audit dashboard](/help/implementing/cloud-manager/experience-audit-dashboard.md) includes a trended view of your page performance scores along with insights and recommendations to help you improve them. Experience Audit is included as a step in the Cloud Manager production pipeline.

The dashboard uses Google Lighthouse, an open-source, automated tool for improving the quality of your web apps. You can run it against any web page, public, or requiring authentication. It has audits for performance, accessibility, progressive web apps, SEO, and more.

Interested in test-driving the new dashboard? To get started, send an email to `aem-lighthouse-pilot@adobe.com` from your email associated with your Adobe ID.
