---
title: Introduction to IP Allow Lists
description: Learn how IP Allow Lists can limit from which addresses users can access domains in AEM as a Cloud Service.
exl-id: 352fae8e-d116-40b0-ba54-d7f001f076e8
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: a01bfd36-4ab8-4bf8-9dc0-5b45b890552e
    internal-label: APIs
subfeature_v2:
  - id: d9eb3b3e-9447-4ed4-bf4a-96c7b245cb27
    internal-label: Cloud Manager APIs
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Introduction to IP Allow Lists {#introduction}

Learn how IP Allow Lists can limit from which addresses users can access domains in AEM as a Cloud Service.

>[!CONTEXTUALHELP]
>id="aemcloud_golive_ipallowlist"
>title="Manage IP Allow Lists"
>abstract="AEM as a Cloud Service is accessible through the Internet and is secured through user authentication and authorization. Cloud Manager's IP Allow Lists can be used to limit and control access only to trusted IP addresses. Cloud Manager users with appropriate permissions can create allowlists of trusted IP addresses from which their site's users can access their AEM domains."
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/ip-allow-lists/add-ip-allow-lists" text="Add an IP Allow List"
>additional-url="https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/ip-allow-lists/managing-ip-allow-lists" text="View and update an IP Allow List"

## Overview {#overview}

AEM as a Cloud Service is, by default, accessible through the Internet. While security is handled through user authentication and authorization, IP allow-listing is a way to limit access only to trusted IP addresses.

Cloud Manager's IP Allow Lists can be used to limit and control access only to such trusted IP addresses. Cloud Manager users with appropriate permissions can [create and add IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md) of trusted IP addresses from which their site's users can access their AEM domains.

After adding, [IP Allow Lists can be applied or unapplied](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) multiple times as a unit or entity to an author service, or a publisher service, or both, in an environment.

>[!NOTE]
>
>If no IP Allow List is applied, by default all IP addresses are allowed. When an IP Allow List is applied, no IP addresses are allowed except for addresses on the IP Allow List.

## Usage notes {#usage-notes}

* A maximum of 50 IP Allow Lists can be added to your program.
* A maximum of 50 IP/CIDR addresses can be added to each IP Allow List.
* IP Allow List names are supported in Cloud Manager for author service, or publish service, or both, in an environment.

### Front-End Pipelines and IP Allow Lists {#front-end-pipeline}

If you use&mdash;or intend to use&mdash;the [front-end pipeline to develop sites](/help/implementing/developing/introduction/developing-with-front-end-pipelines.md), the following Cloud Manager IP Allow List must be added beforehand. 

When you [add the IP Allow List](/help/implementing/cloud-manager/ip-allow-lists/add-ip-allow-lists.md#add-cm-allowlist), name it *`Cloud Manager`*, then copy the list of addresses below and paste them into the IP Allow List dialog box.

```text
52.254.106.192/28
20.186.185.181
52.254.106.240/28
52.254.107.128/28
52.254.105.192/28
52.254.106.176/28
20.186.185.227
52.254.106.144/28
52.254.107.64/28
20.186.185.239
20.22.83.112
52.254.107.80/28
52.254.107.144/28
52.254.106.224/28
20.14.241.153
52.254.107.0/28
52.254.107.32/28
52.254.106.208/28
40.70.154.136/29
52.254.106.160/28
52.254.107.16/28
52.254.106.0/28
4.152.211.251
```

To avoid disruption of running the front-end pipeline, ensure that this Cloud Manager IP Allow List is added. Then, apply the list to the Author environment *before* you enable the pipeline.

See [Apply IP Allow List](/help/implementing/cloud-manager/ip-allow-lists/apply-allow-list.md) and [Enable front-end pipeline](/help/sites-cloud/administering/site-creation/enable-front-end-pipeline.md) for more information.

### The Universal Editor and IP Allow Lists {#universal-editor}

If you intend to use the Universal Editor to author your content, you must add the IP addresses that the Universal Editor Service uses to an Allow List and apply it.

1. Retrieve the IP addresses used by the Universal Editor Service from the following API endpoint: `http://universal-editor-service.adobe.io/ip-ranges`.
1. Create an allow list with those IP addresses, naming it `Universal Editor Service` or similar.
1. Apply the `Universal Editor Service` allow list.

The list of IP addresses used by the Universal Editor Service is subject to change and you must update your allow list accordingly.

### Edge Delivery Services and IP Allow Lists {#edge-delivery-services}

If you intend to use Edge Delivery Service to author your content, you must add the IP addresses that the Edge Delivery Service uses to an Allow List and apply it. 

See [Edge Delivery Services - Backend Integrations with IP Filtering](https://www.aem.live/docs/security#backends-with-ip-filtering) for more information.
