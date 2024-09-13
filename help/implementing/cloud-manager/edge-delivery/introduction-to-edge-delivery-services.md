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
>For details about Edge Delivery Services and how it can be used with AEM, see [Edge Delivery Services overview](/help/edge/overview.md).

<!-- RELEASED TO GA SEPTEMBER 5, 2024
>[!NOTE]
>
>This feature is only available to [the early adopter program](/help/implementing/cloud-manager/release-notes/current.md#early-adoption). -->


## About Edge Delivery Services in Cloud Manager {#edge-in-cloud-manager}

If you have licensed Edge Delivery Services as part of Adobe Experience Manager Sites, you can onboard your site with Edge Delivery Services directly in Cloud Manager and go live [using a guided, self-service experience](/help/implementing/cloud-manager/managing-code/private-repositories.md).

Additionally, you can access a unified experience for managing all your AEM properties while ensuring consistency across key workflows. These include domain name management, SSL certificate management, and CDN mappings.

## Add Edge Delivery Services to a production program or sandbox program

To add or edit programs, you must be a member of the **Business Owner** role or be given permission to do so.

Your organization must have an unused Edge Delivery Services license before it can be applied to a Production program.

>[!NOTE]
>
>Once the Edge Delivery Services license is applied to or removed from a program, the change takes effect immediately without the need to run a pipeline. <!-- https://wiki.corp.adobe.com/display/DMSArchitecture/%5BKT%5D+Cloud+Manager+2024.9.0+Release -->

Depending on your use case, do one of the following:

| Use case | Description |
| --- | --- |
| I want to add Edge Delivery Services to a new production program. | See [Create production programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md).<br>In the wizard, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. |
| I want to add Edge Delivery Services to an existing production program. | See [Edit programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md).<br>In the **Edit Program** dialog box, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. |
| I want to add an Edge Delivery site to Cloud Manager | See [Add an Edge Delivery site](/help/implementing/cloud-manager/edge-delivery/add-edge-delivery-site.md). |
| I want to add Edge Delivery Services to a new or existing sandbox program. | See [Create sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md).<br>When you create a sandbox program, Edge Delivery Services is added to the program by default; you do not need to select it.<br>Existing sandbox programs prior to the general availability of Edge Delivery, inherit Edge Delivery Services automatically. |

## Adobe recommended path for contracted customers {#recommended-path-eds}

As a contracted customer, ensure you maximize your benefits from Adobe by accessing and consuming your Edge Delivery Services license through Cloud Manager. This approach lets you use [Adobe managed CDN](/help/implementing/dispatcher/cdn.md#aem-managed-cdn) and take advantage of key benefits such as self-service CDN management, including the configuration and addition of DV certificates. Additionally, after a DV certificate is created, Adobe renews it automatically every three months, unless it is deleted. If you do not have an Edge Delivery Services license with Adobe and decide to bypass these benefits, you can only use a customer-managed CDN. This setup must be on the `aem.live` platform.

If you are contracted with AEM as a Cloud Service Sites Edge Delivery Services licenses, log into Cloud Manager to ensure you are able to do the following:

* Consume your license on your chosen program. 
* Take advantage of [API-first](https://developer.adobe.com/experience-cloud/experience-manager-apis/) benefits for performing CRUD (Create, Read, Update, Delete) operations.
<!-- REMOVED AS PER https://wiki.corp.adobe.com/display/DMSArchitecture/Cloud+Manager+Self-service+access+to+Edge+Delivery+Services+and+Adobe+Managed+CDN * Access to license dashboard and reporting -->
* Access SLA reporting (*coming soon*) <!-- ADD LINK TO IT WHEN FINALLY ADDED -->
* Gain Adobe support. Make sure that your Edge Delivery Services sites are registered through a Production program in Cloud Manager for proper recognition and support from Adobe.


## About the Edge Delivery to-do list {#ed-todo-list}

The **Edge Delivery to-do list** is an onboarding task checklist meant to guide you through onboarding, managing your Edge Delivery site all the way to [Go-Live](/help/journey-onboarding/go-live-checklist.md).

![Edge Delivery site to-do list](/help/implementing/cloud-manager/assets/cm-eds-todo-list.png)

|  | Task | Description |
| --- | --- | --- |
| 1 | Join the product collaboration channel | Clicking **Submit request now** submits a request to Adobe to create a channel for your company. If the channel already exists, you are forwarded to your company's channel. |
| 2 | Complete prerequisites | Clicking **View Getting Started tutorial**, directs you to the [Getting Started - Developer Tutorial](https://www.aem.live/developer/tutorial). |
| 3 | Add Edge Delivery Site | See [Add an Edge Delivery site](#eds-add-site). |
| 4 | Add domain | See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). |
| 5 | Add SSL certificate | See [Add SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md). |
| 6 | Configure the CDN of your Edge Delivery site | See [Add a CDN configuration](#add-cdn). |

>[!VIDEO](https://video.tv.adobe.com/v/3428020?learn=on)

<!--
Edge Delivery Services can be enabled when adding a new production program or editing an existing one.

![Add production program with Edge Delivery Services](assets/add-production-program-with-edge.png)

For more information about adding programs, see the following:

* [Create Production programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md)
* [Create Sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md) -->
