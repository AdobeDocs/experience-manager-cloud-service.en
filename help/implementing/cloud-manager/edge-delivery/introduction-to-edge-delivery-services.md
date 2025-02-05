---
title: Introduction to Edge Delivery Services in Cloud Manager
description: Learn how to deliver your Cloud Manager projects using Edge Delivery Services.
exl-id: f33bd6f0-62fc-4ecc-b8d2-65d1f1c44d82
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Introduction to Edge Delivery Services in Cloud Manager {#edge-delivery-services}

Edge Delivery Services is a composable set of services that allows for a high degree of flexibility in how you author content on your website. This ability lets you do the following:

* Create fast sites with a perfect Lighthouse Score.
* Continuously monitor performance through RUM (Real Use Monitoring).
* Increase authoring efficiency by decoupling content sources.

You can use both AEM content management and WYSIWYG authoring using the Universal Editor and document-based authoring.

Cloud Manager in AEM as a Cloud Service lets you enable Edge Delivery Service for your project.

>[!TIP]
>
>For details about Edge Delivery Services and how it can be used with AEM, see the [Edge Delivery Services overview](/help/edge/overview.md).

## About Edge Delivery Services in Cloud Manager {#edge-in-cloud-manager}

If you have licensed Edge Delivery Services as part of Adobe Experience Manager Sites, you can onboard your site with Edge Delivery Services directly in Cloud Manager and go live [using a guided, self-service experience](/help/implementing/cloud-manager/managing-code/private-repositories.md).

Additionally, you can access a unified experience for managing all your AEM properties while ensuring consistency across key workflows. These workflows include domain name management, SSL certificate management, and CDN mappings.

## Benefits of using the Adobe recommended path for Edge Delivery Services {#recommended-path-eds}

Maximize your benefits from Adobe by accessing and consuming your Edge Delivery Services license through Cloud Manager. Doing so lets you take advantage of several key benefits.

* [Consume your license on your chosen program](/help/implementing/cloud-manager/edge-delivery/add-edge-delivery-site.md), or [update other programs](/help/implementing/cloud-manager/edge-delivery/manage-edge-delivery-sites.md), or both.
* Take advantage of [API-first](https://developer.adobe.com/experience-cloud/experience-manager-apis/) benefits for performing CRUD (Create, Read, Update, Delete) operations.
* [Access SLA reporting](/help/implementing/cloud-manager/sla-reporting.md) (*coming soon*)
* [Gain access to Adobe support](/help/edge/overview.md#support-ticket) for your registered production programs.

In addition, using Cloud Manager lets you use [Adobe managed CDN](/help/implementing/dispatcher/cdn.md#aem-managed-cdn) for your Edge Delivery site and take advantage of key benefits such as self-service CDN management, including the configuration and addition of DV certificates. Additionally, after a DV certificate is created, Adobe renews it automatically every three months, unless it is deleted. If you do not have an Edge Delivery Services license with Adobe and decide to bypass these benefits, you can only use your own self-managed CDN. This setup must be on the [`aem.live` platform](https://www.aem.live/docs/go-live-checklist#cdn-configuration).

## About adding Edge Delivery Services to a production program or sandbox program

An Edge Delivery Services can be added in a number of different ways depending on how you began your project.

| Use case | Description |
| --- | --- |
| I want to add Edge Delivery Services to a new production program. | See [Create production programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md).<br>In the wizard, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. |
| I want to add Edge Delivery Services to an existing production program. | See [Edit programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md).<br>In the **Edit Program** dialog box, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. |
| I want to add an Edge Delivery site to Cloud Manager | See [Add an Edge Delivery site](/help/implementing/cloud-manager/edge-delivery/add-edge-delivery-site.md). |
| I want to add Edge Delivery Services to a new or existing sandbox program. | See [Create sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md).<br>When you create a sandbox program, Edge Delivery Services is added to the program by default; you do not need to select it.<br>Existing sandbox programs prior to the general availability of Edge Delivery, inherit Edge Delivery Services automatically. |

>[!NOTE]
>
>* To add or edit programs, you must be a member of the **Business Owner** role or be given permission to do so.
>* Your organization must have an unused Edge Delivery Services license before it can be applied to a Production program.
>* Once the Edge Delivery Services license is applied to or removed from a program, the change takes effect immediately without the need to run a pipeline.


## About the Edge Delivery to-do list in Cloud Manager {#ed-todo-list}

<!-- &#x2460; for "1" inside circle -->

The **Edge Delivery to-do list** in Cloud Manager is an onboarding task checklist meant to guide you through onboarding, managing your Edge Delivery site all the way to [Go-Live](/help/journey-onboarding/go-live-checklist.md).

![Edge Delivery site to-do list in Cloud Manager.](/help/implementing/cloud-manager/assets/cm-eds-todo-list.png)

|   | Task  | Description |
| --- | --- | --- |
| 1 | Join the product collaboration channel | Clicking **Submit request now** submits a request to Adobe to create a channel for your company. If the channel already exists, you are forwarded to your company's channel. |
| 2 | Complete prerequisites | See [View Getting Started tutorial](https://www.aem.live/developer/tutorial). |
| 3 | Add Edge Delivery Site | See [Add an Edge Delivery site](#eds-add-site). |
| 4 | Add domain | See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). |
| 5 | Add SSL certificate | See [Add SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md). |
| 6 | Configure the CDN of your Edge Delivery site | See [Add a CDN configuration](/help/implementing/cloud-manager/cdn-configurations/add-cdn-config.md). |
| 7 | Setup push validation | See [Setup push validation for an Edge Delivery site](/help/implementing/cloud-manager/edge-delivery/cdn-setup-push-invalidation.md). |
| 8 | Go-Live | See [Go-Live checklist](/help/edge/docs/go-live-checklist.md). |

>[!VIDEO](https://video.tv.adobe.com/v/3428020?learn=on)

## Log a support ticket {#eds-support-ticket}

{{support-ticket}}



