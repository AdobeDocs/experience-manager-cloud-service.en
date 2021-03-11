---
title: Introduction to Sandbox Programs 
description: Introduction to Sandbox Programs 
---

# Introduction to Sandbox Programs {#sandbox-programs}

## Introduction {#introduction}

A Sandbox program is one of the two types of programs available in AEM Cloud Service, the other being a Production program. 

A Sandbox is typically created to serve the purposes of training, running demos, enablement, or Proof of Concept (POC)s. They are not meant to carry live traffic. They are not subject to the [AEM as a Cloud Service Commitments](https://www.adobe.com/legal/service-commitments.html).

The environments created in a Sandbox are not configured for auto-scaling. Therefore, these environments are not suitable for performance or load testing.

Sandbox programs include Sites and Assets and are auto-populated with a Git repository, a Development environment, and a non-production pipeline.  The Git repository is populated with a sample project based on the AEM Project archetype.

Refer to [Understanding Programs and Program Types](/help/onboarding/getting-access-to-aem-in-cloud/understand-program-types.md) to learn more about the Program Types.

### Attributes of Sandbox Programs {#attributes-sandbox}

Sandbox Programs have the following attributes:

1. **Program Creation:** The Sandbox program creation includes automatic:
   * setup of project with sample code and content
   * creation of development environment
   * creation of non-production pipeline deploying to development environment (master branch deploying to development environment)
 
1. **Solutions:** Sandbox programs include AEM Sites and Assets.

1. **AEM Updates:** AEM updates can be applied manually to environments in a Sandbox program, and are not automatically pushed.
   Refer to [AEM Updates to Sandbox Environments](/help/onboarding/getting-access-to-aem-in-cloud/hibernating-de-hibernating-sandbox-environments.md#aem-updates-sandbox) for more details.

1. **Hibernation:** Environments in a Sandbox program are automatically hibernated if no activity is detected for a certain period of time. Hibernated environments can be manually de-hibernated.
   Refer to [Hibernating and De-hibernating Sandbox Environments](/help/onboarding/getting-access-to-aem-in-cloud/hibernating-de-hibernating-sandbox-environments.mdd) for more details.