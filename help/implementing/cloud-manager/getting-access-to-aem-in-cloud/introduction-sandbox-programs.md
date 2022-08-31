---
title: Introduction to Sandbox Programs 
description: Learn what sandbox programs are how they differ from production programs.
exl-id: 4606590c-6826-4794-9d2e-5548a00aa2fa
---

# Introduction to Sandbox Programs {#sandbox-programs}

Learn what sandbox programs are how they differ from production programs.

## Introduction {#introduction}

A sandbox program is typically created to serve the purposes of training, running demos, enablement, or proof of concepts (POCs) and thus are not meant to carry live traffic.

A sandbox program is one of the two types of programs available in AEM Cloud Service, the other being a [production program.](introduction-production-programs.md) Please refer to the document [Understanding Programs and Program Types](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md) to learn more about program types.

## Auto-Creation {#auto-creation}

Sandbox programs feature auto-creation. Whenever you create a new sandbox program Cloud Manager automatically:

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

[Advanced networking features](/help/security/configuring-advanced-networking.md) (e.g. self-serve provisioning of VPN, non-standard ports, dedicated egress IP addresses, etc.) are not available in sandbox programs.

### Manual AEM Updates {#updates}

AEM updates are not automatically pushed to sandbox programs, but can be applied manually to the environments in your sandbox program.

* A manual update can only be run when the targeted environment has a properly configured pipeline. 
* A manual update to either a production or staging environment will automatically update the other. The Production+Stage environment set must be on the same AEM release.

Please refer to the document [AEM version updates](/help/implementing/deploying/aem-version-updates.md) for more details.

Please refer to the document [Updating Environment](/help/implementing/cloud-manager/manage-environments.md#updating-dev-environment) to learn how to update an environment.

### Hibernation and Deletion {#hibernation}

Environments in a sandbox program are automatically hibernated after 8 hours of inactivity. Once 
hibernated, they can be manually de-hibernated.

Sandbox programs are deleted after 6 months of being in continuous hibernation mode, after which time, they can be recreated.

Please refer to [Hibernating and De-hibernating Sandbox Environments](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/hibernating-environments.md) for more details.
