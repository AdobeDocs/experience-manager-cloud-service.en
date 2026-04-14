---
title: Introduction to Edge Delivery Services in Cloud Manager
description: Learn how to deliver your Cloud Manager projects using Edge Delivery Services.
exl-id: f33bd6f0-62fc-4ecc-b8d2-65d1f1c44d82
feature: Cloud Manager, Developing
role: Admin, Developer
---

# Introduction to Edge Delivery Services in Cloud Manager {#edge-delivery-services}

Edge Delivery Services is a composable set of services that allows for a high degree of flexibility in how you author content on your website. This ability lets you do the following:

* Create fast sites with a perfect Lighthouse Score.
* Continuously monitor performance through Operational Telemetry.
* Increase authoring efficiency by decoupling content sources.

You can use both AEM content management and WYSIWYG authoring using the Universal Editor and document-based authoring.

Cloud Manager in AEM as a Cloud Service lets you enable the Edge Delivery Service for your project.

>[!TIP]
>
>For details about Edge Delivery Services and how it can be used with AEM, see the [Edge Delivery Services overview](/help/edge/overview.md#how-does-it-work).

## About Edge Delivery Services in Cloud Manager {#edge-in-cloud-manager}

If you have licensed Edge Delivery Services as part of Adobe Experience Manager Sites, you can onboard your site with Edge Delivery Services directly in Cloud Manager and go live [using a guided, self-service experience](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md).

Additionally, you can access a unified experience for managing all your AEM properties while ensuring consistency across key workflows. These workflows include domain name management, SSL certificate management, and CDN mappings.

Cloud Manager offers two deployment types for Edge Delivery Services in Adobe Managed CDN with distinct capabilities. [Learn more](#edge-delivery-deployment-options).

>[!NOTE]
>
>Edge Delivery Services can also be integrated into existing AEM Sites as a Cloud Service environments using the Config Pipeline and origin selectors. For details, see [Proxying to Edge Delivery Services](/help/implementing/dispatcher/cdn-configuring-traffic.md#proxying-to-edge-delivery) and [Setup a proxy from an existing environment](https://www.aem.live/docs/byo-cdn-adobe-managed#option-1-setup-a-proxy-from-an-existing-environment).

## Edge Delivery Services deployment options in Adobe Managed CDN {#edge-delivery-deployment-options}

There are two deployment types for Edge Delivery Services in Adobe Managed CDN:

1. **With an existing AEMaaCS environment** — Set up an HTTP proxy from an existing AEM Sites as a Cloud Service environment. This approach is typically used when you already have an existing environment and you want to migrate part of a site to Edge Delivery Services. See [Setup a proxy from an existing environment](https://www.aem.live/docs/byo-cdn-adobe-managed#option-1-setup-a-proxy-from-an-existing-environment).

1. **Without an existing AEMaaCS environment (Edge Environment)** — Set up a new Edge Delivery site independently of an AEM Sites as a Cloud Service environment. This approach is used when you do not have an AEM Author or publish environment and you want to use Edge Delivery Services on its own. See [Setup an Edge Delivery site without an existing environment](https://www.aem.live/docs/byo-cdn-adobe-managed#option-2-setup-an-edge-delivery-site-without-an-existing-environment).

These two options also have different capabilities:

* **Config Pipeline** is available for AEM as a Cloud Service environments.
* **Config Pipeline** is currently available for Edge environments only by way of the limited Beta program.

For full setup instructions, see [Adobe Managed CDN](https://www.aem.live/docs/byo-cdn-adobe-managed)


## About Edge Delivery Services with AEM authoring (Beta) {#eds-aem-authoring}

>[!NOTE]
>
>The flexible publish tier and AEM authoring crosswalk features described here are in Beta. To join the Beta, email [grp-beta_xwalk-publish_config@adobe.com](mailto:grp-beta_xwalk-publish_config@adobe.com) with your Adobe Organization ID and Program ID.

Modern web experiences require high-performance delivery, but many organizations also rely on established AEM authoring workflows, governance, and content reuse patterns. To help your teams modernize delivery without disrupting authoring, Cloud Manager introduces capabilities that let you do the following:

* Deliver experiences using Edge Delivery Services.
* Continue using AEM Author for content creation.
* Provision only the infrastructure required for your architecture.

These capabilities let organizations adopt modern delivery incrementally, without sacrificing existing workflows.

### Authoring options for Edge Delivery sites {#authoring-options-eds}

When you create an Edge Delivery site in Cloud Manager, you can choose your preferred authoring approach:

* Document-based authoring — Author content in Google Drive or SharePoint. No AEM environment is required.
* AEM authoring — Author content in AEM using the Universal Editor. This method requires an AEM Author environment. With this option, a publish tier is not required when Edge Delivery handles content delivery.

Organizations can choose between these approaches, or use both incrementally, depending on their workflow preferences. See [Create your first Edge Delivery site with one click](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md).

### Flexible publish tier {#flexible-publish-tier}

Cloud Manager lets you configure whether a publish tier is provisioned for your program's environments. Not all architectures require a publish tier as seen in the following table:

| Architecture | Publish Tier |
| --- | --- |
| Traditional AEM Sites | Required |
| Headless / API-first | Required |
| Edge Delivery Services | Not required |

By enabling the publish tier only when needed, teams can provision environments faster, simplify infrastructure, and reduce unnecessary components. See [Flexible Publish Tier (Beta)](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#flexible-publish-tier).

## Benefits of using the Adobe recommended path for Edge Delivery Services {#recommended-path-eds}

Maximize your benefits from Adobe by accessing and consuming your Edge Delivery Services license through Cloud Manager. Doing so lets you take advantage of several key benefits.

* [Consume your license on your chosen program](/help/implementing/cloud-manager/edge-delivery/add-edge-delivery-site.md), or [update other programs](/help/implementing/cloud-manager/edge-delivery/manage-edge-delivery-sites.md), or both.
* [Use an external Git repository](/help/implementing/cloud-manager/managing-code/external-repositories.md) (Bring Your Own Git) to sync and deploy your Edge Delivery Services site code. To leverage this capability, you must first [onboard your site in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/add-edge-delivery-site.md). <!-- NEW from CQDOC-22867 -->
* [Use the Edge Delivery Config Pipeline](/help/implementing/dispatcher/cdn-configuring-traffic.md) to configure Adobe-managed CDN settings for your Edge Delivery site by defining rules such as traffic filters, origin selectors, and redirects. <!-- NEW from CQDOC-22867 -->
* Take advantage of [API-first](https://developer.adobe.com/experience-cloud/experience-manager-apis/) benefits for performing CRUD (Create, Read, Update, Delete) operations.
* [Access SLA reporting](/help/implementing/cloud-manager/reports/report-sla.md).
* [Gain access to Adobe support](/help/edge/overview.md#support-ticket) for your registered production programs.

If you have an Edge Delivery Services (EDS) license, you can use an [Adobe-managed CDN](/help/implementing/dispatcher/cdn.md#aem-managed-cdn) for your Edge Delivery site. Doing so enables self-service CDN management and DV certificates that renew automatically every three months unless you delete the certificate.

Alternatively, if you choose to use your CDN (that is, a non-Adobe-managed CDN), regardless of your Edge Delivery Services licensing, you must configure it on the `aem.live` platform. See [BYO CDN Setup](https://www.aem.live/docs/byo-cdn-setup). 


## About adding Edge Delivery Services to a production program or sandbox program {#about-adding-eds-to-prod-sandbox}

An Edge Delivery Services can be added in a number of different ways depending on how you began your project or when you want to create the site.

| Use case | Description |
| --- | --- |
| I want to add Edge Delivery Services to a new production program. | See [Create production programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md).<br>In the wizard, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. |
| I want to add Edge Delivery Services to an existing production program. | See [Edit programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md).<br>In the **Edit Program** dialog box, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. |
| I want to add an Edge Delivery site to Cloud Manager | See [Add an Edge Delivery site](/help/implementing/cloud-manager/edge-delivery/add-edge-delivery-site.md). |
| I want to create an Edge Delivery site now | See [Create an Edge Delivery site quickly in Cloud Manager with the click of a button](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md). |
| I want to add Edge Delivery Services to a new or existing sandbox program. | See [Create sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md).<br>When you create a sandbox program, Edge Delivery Services is added to the program by default; you do not need to select it.<br>Existing sandbox programs prior to the general availability of Edge Delivery, inherit Edge Delivery Services automatically. |
| I want to create an Edge Delivery site that uses AEM authoring | See [Create an Edge Delivery site](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md#one-click-edge-delivery-site). When using AEM authoring with Edge Delivery, a publish tier is optional. See [Flexible Publish Tier (Beta)](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#flexible-publish-tier). |

>[!NOTE]
>
>* To add or edit programs, you must be a member of the **Business Owner** role or be given permission to do so.
>* Your organization must have an unused Edge Delivery Services license before it can be applied to a Production program.
>* Once the Edge Delivery Services license is applied to or removed from a program, the change takes effect immediately without the need to run a pipeline.


## About the Edge Delivery to-do list in Cloud Manager {#ed-todo-list}

<!-- &#x2460; for "1" inside circle -->

The **Edge Delivery to-do list** in Cloud Manager is an onboarding task checklist meant to guide you through onboarding, managing your Edge Delivery site all the way to [Go-Live](/help/journey-onboarding/go-live-checklist.md).

![Edge Delivery site to-do list in Cloud Manager](/help/implementing/cloud-manager/assets/cm-eds-todo-list.png)

|   | Task  | Description |
| --- | --- | --- |
| 1 | Join the product collaboration channel | Clicking **Submit request now** submits a request to Adobe to create a channel for your company. If the channel already exists, you are forwarded to your company's channel. |
| 2 | Complete prerequisites | See [View Getting Started tutorial](https://www.aem.live/developer/tutorial). |
| 3 | Add Edge Delivery Site OR <br>Create a site now | See [Add an Edge Delivery site](#eds-add-site).<br>See [Create an Edge Delivery site in Cloud Manager](/help/implementing/cloud-manager/edge-delivery/create-edge-delivery-site.md). |
| 4 | Configure an Edge Delivery site to use an external Git repository | See [Configure an Edge Delivery site to use an external Git repository](/help/implementing/cloud-manager/edge-delivery/config-edge-delivery-site-with-byog.md). |
| 5 | Add domain | See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). |
| 6 | Add SSL certificate | See [Add SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md). |
| 7 | Configure the CDN of your Edge Delivery site | See [Add a Domain Mapping](/help/implementing/cloud-manager/domain-mappings/add-domain-mapping.md). |
| 8 | Setup push validation | See [Setup push validation for an Edge Delivery site](/help/implementing/cloud-manager/edge-delivery/cdn-setup-push-invalidation.md). |
| 9 | Go-Live | See [Go-Live checklist](https://www.aem.live/docs/go-live-checklist). |

>[!VIDEO](https://video.tv.adobe.com/v/3428020?learn=on)

## Log a support ticket {#eds-support-ticket}

{{support-ticket}}



