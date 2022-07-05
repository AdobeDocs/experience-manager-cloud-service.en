---
title: AEM as a Cloud Service Terminology
description: Before you sign into AEMaaCS, it is helpful to understand some of the terminology of the system and its basic structure.
---

# AEM as a Cloud Service Terminology {#terminology}

Now that you understand what has led up to the onboarding process by reading the document [Onboarding Preparation,](preparation.md) it is helpful to understand some of the terminology of the system and its basic structure before logging in.

## Objective {#objective}

AEM as a Cloud Service is a powerful and flexible tool and to use any tool you should be familiar with its organization and the terminology and language used to describe it. This document summarizes some key terms you need to understand before you begin using the system.

After reading this document you will understand:

* The different layers that make up AEMaaCS.
* The basics of what each layer does.

## AEMaaCS Structure {#structure}

For the purposes of this onboarding journey, a complete understanding of the structure of AEM as a Cloud Service is not necessary. But familiarity with the following concepts will make it easier to follow along later in the journey.

![Cloud Manager structure](/help/journey-sites/quick-site/assets/cloud-manager-structure.png)

* **TENANT** - Every customer is provisioned with a tenant. A tenant is also referred to as an IMS org (more on IMS later in this journey)
* **PROGRAMS** - Each tenant has one or more programs, which often reflect the customer's licensed solutions.
* **ENVIRONMENTS** - Each program has multiple environments such as production for live content, one for staging, and one for development purposes.
* **REPOSITORY** - The environments have one or more git repositories where application and front-end code is maintained.
* **TOOLS &amp; WORKFLOWS** - Pipelines manage the deployment of code from the repositories to the environments.

An example is often helpful in contextualizing this hierarchy.

* WKND Travel and Adventure Enterprises might be a **tenant** that focuses on travel-related media.
* The WKND Travel and Adventure Enterprises tenant might have two **programs**: 
  * One Sites program for its WKND Magazine division
  * One Assets program for WKND Media division
* The WKND Magazine and WKND Media programs would both have development, staging, and production **environments**.
* **Repositories** are used to maintain the custom code and applications for WKND Magazine and WKND Media.
* Various **tools &amp; workflows** work across the repos to deploy code using CI/CD pipelines, access logs, access AEM, etc.

## What’s Next {#what-is-next}

Now that you have completed this part of the AEM onboarding journey you should understand:

* The different layers that make up AEMaaCS.
* The basics of what each layer does.

Build on this knowledge and continue your AEM onboarding journey by next reading the document [Accessing the Admin Console](admin-console.md), where you will learn how access the console and verify your status as a system administrator.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the Onboarding Journey by reviewing the document [Accessing the Admin Console](admin-console.md), the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [Admin Console Overview](https://helpx.adobe.com/enterprise/using/admin-console.html) - A more in-depth article on the Admin Console
* [Create or update your Adobe ID](https://helpx.adobe.com/ca/manage-account/using/create-update-adobe-id.html#HowtocreateorupdateyourAdobeID) - Learn more about Adobe IDs.
* [SAML 2.0 Authentication Handler](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/saml-2-0-authenticationhandler.html) - For details on SAML authentication
* [System administrators and support administrators](https://helpx.adobe.com/enterprise/using/admin-roles.ug.html) - Learn about the roles of system and support admins
* [Experience Cloud | Support and Expert Sessions](https://helpx.adobe.com/enterprise/admin-guide.html/enterprise/using/support-for-experience-cloud.ug.html) - Learn about expert sessions.
