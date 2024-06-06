---
title: Introduction to Sandbox Programs 
description: Learn what sandbox programs are how they differ from production programs.
exl-id: 4606590c-6826-4794-9d2e-5548a00aa2fa
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Introduction to Sandbox Programs {#sandbox-programs}

Learn what sandbox programs are how they differ from production programs.

## Introduction {#introduction}

A sandbox program is typically created to serve the purposes of training, running demos, enablement, or proof of concepts (POCs) and thus are not meant to carry live traffic.

A sandbox program is one of the two types of programs available in AEM Cloud Service, the other being a [production program.](introduction-production-programs.md) See [Understanding Programs and Program Types](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md) to learn more about program types.

## Auto-Creation {#auto-creation}

Sandbox programs feature auto-creation. Whenever you create a sandbox program, Cloud Manager automatically:

* Adds AEM Sites and AEM Assets as solutions in your program.
* Sets up a project git repository with a sample project based on the [AEM Project Archetype.](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/overview.html)
* Creates a development environment.
* Creates a non-production pipeline that deploys to the development environment.

A sandbox program will have only one development environment.

## Limitations and Conditions {#limitations}

Because they are not meant for live traffic, sandbox programs have certain limitations and conditions on their usage, which differentiate them from production programs.

### No Live Traffic {#live-traffic}

Sandbox programs are not meant to carry live traffic and are therefore not subject to [AEM as a Cloud Service Commitments.](https://www.adobe.com/legal/service-commitments.html)

### No Auto-Scaling {#auto-scaling}

Environments created in a sandbox program are not configured for auto-scaling. Therefore, these environments are not suitable for performance or load testing.

### No Custom Domains or IP Allow Lists {#ip-allow}

Custom domains and IP allow lists are not available in sandbox programs.

### No Advanced Networking {#advanced-networking}

[Advanced networking features](/help/security/configuring-advanced-networking.md) (for example, self-serve provisioning of VPN, non-standard ports, dedicated egress IP addresses, and so on) are not available in sandbox programs.

### Manual AEM Updates {#updates}

AEM updates are not automatically pushed to sandbox programs, but can be applied manually to the environments in your sandbox program.

* A manual update can only be run when the targeted environment has a properly configured pipeline. 
* A manual update to either a production or staging environment will automatically update the other. The Production+Stage environment set must be on the same AEM release.

See [AEM version updates](/help/implementing/deploying/aem-version-updates.md) for more details.

See [Updating Environment](/help/implementing/cloud-manager/manage-environments.md#updating-dev-environment) to learn how to update an environment.

### Hibernation and Deletion {#hibernation}

Environments in a sandbox program are automatically hibernated after eight hours of inactivity. Sandbox environments are deleted after six continuous months of hibernation.

See [Hibernating and De-hibernating Sandbox Environments](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/hibernating-environments.md) for more details about how to de-hibernate environments and automatic sandbox deletion.

### No Technical Support {#no-support}

Because a sandbox program is typically created to serve the purposes of training, running demos, enablement, or proof of concepts (POCs), technical support is not available for issues experienced in a sandbox program.

If you experience issues creating and managing your sandbox programs, this is still within the scope of technical support.
