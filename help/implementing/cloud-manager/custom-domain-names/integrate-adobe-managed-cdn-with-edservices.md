---
title: Integrate Edge Delivery Services with Adobe Managed CDN in Cloud Manager
description: 
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
hide: yes
hidefromtoc: yes


---

# Integrate Edge Delivery Services with Adobe Managed CDN in Cloud Manager {#integrate-adbe-cdn-with-edservices-in-cm}

Adobe Managed CDN (AMC-D) integrates natively with Edge Delivery Services to give you performant, globally distributed experiences for Adobe Experience Manager (AEM) Sites.

Together, they give you the following benefits:

* A turnkey, enterprise-grade CDN managed by Adobe.
* A modern edge-delivery layer that accelerates requests, optimizes caching, and protects against common attacks.
* A unified Cloud Manager workflow for domain management, SSL certificates, and pipeline-driven deployments.

<!--
Adobe's Edge Delivery Services (EDS) can take advantage of an Adobe managed CDN. EDS is a framework that optimizes website delivery for speed, simplicity, and scalability by pushing content closer to the user through edge nodes. It is not a replacement for a CDN, but rather a way to enhance content delivery, especially when you use the Adobe managed CDN. It offers you the following benefits:

* Adobe-Managed CDN: EDS can use an Adobe-managed CDN, offering features like self-service CDN management and automatic certificate renewal. 
* EDS and AEM: EDS is a feature of AEM as a Cloud Service and works alongside the AEM authoring environment. 
* Performance enhancement: EDS, in conjunction with an Adobe Managed CDN, improves website performance by caching content at edge locations closer to users, reducing latency. 
* Flexibility: EDS provides flexibility in content delivery, allowing your organization to choose between the Adobe-managed CDN or their own CDN setup, based on their needs and existing infrastructure. 
Self-Service CDN Management:
Adobe-managed CDN within EDS enables self-service configuration and management tasks like SSL certificate setup. 
 
Use Cases:
EDS with CDN integration is beneficial for various scenarios, including e-commerce storefronts and websites requiring high performance and scalability.
-->

## Edge Delivery Services deployment options in Adobe Managed CDN in Cloud Manager {#deployment-options}

This topic explains the two ways you can deploy Edge Delivery Services on Adobe Managed CDN in Cloud Manager and, just as importantly, helps you decide which option is best for your use case.

Edge Delivery Services can be set up using one of the following two options. Each has different capabilities.

|  | Deployment option | Key doc | Capability | Best for |
| --- | --- | --- | --- | --- |
| Option 1 | *With* an existing AEM as a Cloud Service (AEMaaCS) environment | [Set up a proxy from an existing environment](https://www.aem.live/docs/byo-cdn-adobe-managed#option-1-setup-a-proxy-from-an-existing-environment) | Config Pipeline is generally available for AEMaaCS environments | Teams that already run Sites in Cloud Manager and want a quick, low-risk performance boost. |
| Option 2 | *Without* an existing AEMaaCS environment; known as a standalone "Edge environment." | [Setup an Edge Delivery site without an existing environment](https://www.aem.live/docs/byo-cdn-adobe-managed#option-2-setup-an-edge-delivery-site-without-an-existing-environment)  | Config Pipeline is currently available only for Edge environments through the limited Beta program.<br>See [Add Edge Delivery Config Pipeline](/help/implementing/cloud-manager/release-notes/current.md#add-eds-pipeline). | New builds or migrations that want to embrace the full Edge Delivery architecture and granular routing. |

<!-- Ultimately this URL above will need to be updated on GA -->

| Option | Summary | Best for | Key docs |
| --- | --- | --- | --- |
| Adobe Managed CDN Proxy | Adobe Managed CDN fronts an existing AEM Sites environment. Your current Sites pipeline remains the "origin," while AMC-D handles edge caching and TLS termination. | Teams that already run Sites in Cloud Manager and want a quick, low-risk performance boost. | Set up an AMC-D proxy |
| Config Pipeline with originSelectors | A dedicated Edge Delivery Config Pipeline publishes static and dynamic content directly to the edge. `originSelectors` route traffic between AMC-D and your AEM author/publish tiers. | New builds or migrations that want to embrace the full Edge Delivery architecture and granular routing. | Configure the Edge Delivery pipeline |

>[!TIP]
>
>Unsure which path to pick? See [Choose a deployment model](#choose-deployment-model) below for decision guidelines.

## Choose a deployment model {#choose-deployment-model}

Both models can coexist within the same Cloud Manager program, allowing phased migrations.

| If you... | Then use... |
| :--- | :--- |
| Need a fast, minimal-change rollout and already host Sites in Cloud Manager | AMC-D Proxy |
| Plan to restructure content for Edge Delivery, or want fine-grained routing between multiple origins | Config Edge Deliver Pipeline + `originSelectors` |

## Prerequisites {#prerequisites}

1. Onboard your site in Cloud Manager – Required for both deployment models. Follow Onboard an AEM Site.

2. Bring Your Own Git (BYOG) (optional) – If you store site code outside Adobe Git, complete BYOG onboarding.

3. Edge Delivery license – Ensure your program is licensed for Edge Delivery Services.


