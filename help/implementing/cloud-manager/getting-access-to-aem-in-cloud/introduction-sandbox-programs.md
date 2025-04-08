---
title: Introduction to Sandbox Programs 
description: Learn what sandbox programs are and how they differ from production programs.
exl-id: 4606590c-6826-4794-9d2e-5548a00aa2fa
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Introduction to sandbox programs {#sandbox-programs}

Learn what sandbox programs are and how they differ from production programs.

## Introduction {#introduction}

A sandbox program is typically created to serve the purposes of training, running demos, enablement, or proof of concepts (POCs) and thus are not meant to carry live traffic.

A sandbox program is one of the two types of programs available in AEM Cloud Service, the other being a [production program](introduction-production-programs.md). See [Understanding Programs and Program Types](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md) to learn more about program types.

## Auto-creation {#auto-creation}

Sandbox programs feature auto-creation. Whenever you [create a sandbox program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md), Cloud Manager automatically:

* Adds AEM Sites, Assets, and Edge Delivery Services as default solutions to your program.

   ![Select solutions and add-ons for a sandbox](assets/sandbox-solutions-add-ons.png)

* Sets up a project git repository with a sample project based on the [AEM Project Archetype](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/overview).
* Creates a development environment.
* Creates a non-production pipeline that deploys to the development environment.

A sandbox program has only one development environment.

## Limitations and conditions {#limitations}

Because they are not meant for live traffic, sandbox programs have certain limitations and conditions on their usage, which differentiates them from production programs.

| Limitation/condition | Description |
| --- | --- |
| No live traffic | Sandbox programs are not meant to carry live traffic and are therefore not subject to [AEM as a Cloud Service Commitments](https://www.adobe.com/legal/service-commitments.html). |
| No auto-scaling | Environments created in a sandbox program are not configured for auto-scaling. Therefore, these environments are not suitable for performance or load testing. |
| No custom domains or IP Allow Lists | [Custom domains](/help/implementing/cloud-manager/custom-domain-names/introduction.md) and [IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/introduction.md) are not available in sandbox programs. |
| No additional publish regions | [Additional publish regions](/help/operations/additional-publish-regions.md) are not available in sandbox programs. |
| No 99.99% SLA | [99.99% SLA](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#sla) does not apply to sandbox programs. |
| No advanced networking | [Advanced networking features](/help/security/configuring-advanced-networking.md) (for example, self-serve provisioning of VPN, non-standard ports, dedicated egress IP addresses, and so on) are not available in sandbox programs. |
| No automatic AEM updates | AEM updates are not automatically pushed to sandbox programs, but can be applied manually to the environments in your sandbox program.<br>&bull; A manual update can only be run when the targeted environment has a properly configured pipeline.<br>&bull; A manual update to either a production or staging environment automatically updates the other. The Production+Stage environment set must be on the same AEM release.<br>See [AEM version updates](/help/implementing/deploying/aem-version-updates.md) for more details.<br>See [Updating Environment](/help/implementing/cloud-manager/manage-environments.md#updating-dev-environment) to learn how to update an environment. |
| No technical support | Because a sandbox program is typically created to serve the purposes of training, running demos, enablement, or POCs (proof of concepts), technical support is not available for issues experienced in a sandbox program.<br>If you experience issues creating and managing your sandbox programs, these issues are within the scope of technical support. |
| Hibernation and deletion | Environments in a sandbox program are automatically hibernated after eight hours of inactivity. Sandbox environments are deleted after six continuous months of hibernation.<br>See [Hibernating and De-hibernating Sandbox Environments](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/hibernating-environments.md) for more details about how to de-hibernate environments and automatic sandbox deletion. |
