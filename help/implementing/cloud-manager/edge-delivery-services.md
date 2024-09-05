---
title: Edge Delivery Services Support in Cloud Manager
description: Learn how to deliver your Cloud Manager projects using Edge Delivery Services.
exl-id: f33bd6f0-62fc-4ecc-b8d2-65d1f1c44d82
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Edge Delivery Services Support in Cloud Manager {#edge-delivery-services}

Learn how to deliver your Cloud Manager projects using Edge Delivery Services.

>[!NOTE]
>
>This feature is only available to [the early adopter program](/help/implementing/cloud-manager/release-notes/current.md#early-adoption).

## Edge Delivery Services in Brief {#edge-overview}

Edge Delivery Services is a composable set of services that allows for a high degree of flexibility in how you author content on your website. This ability lets you do the following:

* Create fast sites with a perfect Lighthouse Score.
* Continuously monitor performance through RUM (Real Use Monitoring).
* Increase authoring efficiency by decoupling content sources.

You can use both AEM content management and WYSIWYG authoring using the Universal Editor and document-based authoring.

Cloud Manager in AEM as a Cloud Service lets you enable Edge Delivery Service for your project.

>[!TIP]
>
>For details about Edge Delivery Services and how it can be used with AEM, please see the document [Edge Delivery Services Overview](/help/edge/overview.md).

## Edge Delivery Services in Cloud Manager {#edge-in-cloud-manager}

If you have licensed Edge Delivery Services as part of Adobe Experience Manager Sites, you can onboard your site with Edge Delivery Services directly in Cloud Manager and go live [using a guided, self-service experience](/help/implementing/cloud-manager/managing-code/private-repositories.md).

This functionality delivers a unified experience for managing all your AEM properties. It ensures consistency across key workflows. These include domain name management, SSL certificate management, and CDN mappings.

## Add Edge Delivery Services to a production program or a sandbox program

You must be a member of the **Business Owner** role to add or edit programs.

Depending on your use case, do one of the following:

| Use case | Description |
| --- | --- |
| I want to add Edge Delivery Services to a new production program. | See [Create production programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md).<br>In the wizard, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. |
| I want to add Edge Delivery Services to an existing production program. | See [Edit programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md).<br>In the **Edit Program** dialog box, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. |
| I want to add Edge Delivery Services to a new sandbox program. | See [Create sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md).<br>When you create a sandbox program, Edge Delivery Service is added to the program by default. You do not need to select it. |
| I want to add Edge Delivery Services to an existing sandbox program. | See [Edit programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md).<br>In the **Edit Program** dialog box, under the **Solutions & Add-ons** tab, select **Edge Delivery Services**. If you are unable to select Edge Delivery Services, you may not have the FINISH  |

## Recommended path for contracted customer {#recommended-path-eds}

EDIT/REWRITE THIS SECTION or MOVE TO CDN.MD ARTICLE?

    As a contracted customer you should ensure you get the benefits of your contract with Adobe by accessing and consuming your Edge Delivery Services license via Cloud Manager. This way you can leverage Adobe Managed CDN and reap benefits including the critical ones listed below.
    If for any reason (such as customer is not contracted with Adobe for an Edge Delivery Services license) and wishes to go direct and forgo the benefits that come with it (by not accessing and setting up via Cloud Manager), you can only take the path of using a customer managed CDN on aem.live.

If you are a customer contracted with AEMaaCS Sites Edge Delivery Services license(s), then log in to Cloud Manager to ensure you are able to:

    Consume your license on a program of your choice
    Leverage API-first benefits: 

    Adobe Experience Manager as a Cloud Service is developed with an "API first" philosophy. Using these APIs, you can programmatically perform basic CRUD (Create, Read, Update, Delete) operations.

    The API references listed above serve as high-level overviews of the available endpoints provided by each of the AEMaaCS solution API. For more detailed information on the use of these APIs, please refer to the documentation linked from within each reference.

    Leverage Adobe managed CDN functionality and benefit from self-service CDN management (including self-serve configure and install DV or EV/OV certificates)
    Access to license dashboard and reporting
    Access to SLA reporting
    And last, but not the least, access to Adobe support. (It is noteworthy that your Edge Delivery Services site(s) must be registered via a Production program in Cloud Manager in order for it to be recognized and given requisite support by Adobe)


(Note: Underlined text will have appropriate cross-linkage)

## Add an Edge Delivery site {#enabling}

After you add Edge Delivery Services to a production program, your Edge Delivery Services license is applied to it. A new tab called **Edge Delivery** is added to the Overview page. When you click the tab, a table is displayed listing each Edge Delivery Site you have added.

In the left navigation panel, under the **Services** grouping, **Edge Delivery Sites** is added.

ADD SCREENSHOT FOR ORIENTATION

**To add an Edge Delivery site:**

1. ADD STEPS TO ADD SITE




## Edge Delivery to-do list

WHEN IS THIS DONE?
DOES IT ALWAYS HAVE TO BE DONE? 
WHAT PARTS CAN BE DONE BUT OTHERS LEFT UNDONE?

ADD DOMAIN - LINK TO [Add SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md)




## CONFIGURE CDN





## DELETE AN EDGE DELIVERY SITE








<!--
Edge Delivery Services can be enabled when adding a new program.

![Add production program with Edge Delivery Services](assets/add-production-program-with-edge.png)

For more information about adding programs, see the following:

* [Create Production programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md)
* [Create Sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md) -->
