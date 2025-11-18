---
title: Production Agent Overview
description: Learn what agents are available in AEM to accelerate your content creation and automatically orchestrate changes.
feature: Edge Delivery Services, Agentic AI
role: Admin, Architect, Developer
---

# Production Agent Overview {#production-agent}

The Production Agent automates high effort and high-volume tasks. Empowering teams and turning manual, weeks-long processes into fast, AI-assisted workflows that keep every experience current and consistent helping the business achieve their goals.

## Jobs {#jobs}

The agent provides the following jobs:

* [Content Update](#content-update)
* [Form Creation](#form-creation)
* [Interactive Communications Creation](#interactive-communications-creation)
* [Site Migration](#site-migration)

### Content Update {#content-update}

The [Content Update](/help/ai-in-aem/agents/production/content-update.md) updates existing content across the CMS — including content fragments, pages, forms and assets — with ease. The agent can perform actions such as updating, removing, replacing, or adding content elements to keep experiences accurate and current. Inputs can be natural language description, and when used with Jira PDFs and screenshots can provide input too.

### Form Creation {#form-creation}

The [Form Creation](/help/ai-in-aem/agents/production/form-creation.md) skill enables users to build adaptive forms through natural language interactions without dependency on development or IT teams. This capability accelerates form deployment while maintaining brand consistency and allowing business users to create forms without deep technical knowledge.


### Interactive Communications Creation {#interactive-communications-creation}

The [Interactive Communications Creation](/help/ai-in-aem/agents/production/interactive-communications-creation.md) skill empowers business users to produce personalized, data-driven correspondence at scale. From account statements and policy documents to bills and welcome kits, the agent transforms natural language requirements into professional communications.

>[!NOTE]
>
>
> The Interactive Communications Creation capability is currently in alpha release. If you require access to this capability, send a request from your official email address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com).


### Site Migration {#site-migration}

The [Site Migration](/help/ai-in-aem/agents/production/site-migration.md) seamlessly migrate non-AEM sites into AEM (Experience Delivery Services) environments, ensuring they are performant, compliant, and agent-ready. The agent streamlines setup and transformation, reducing manual effort and time to value.

The agent should be able to work with other agent skills, examples include:

## Use with other agents {#use-with-other-agents}

* Get source assets from the Experience Advisory Agent

## Personas {#personas}

### Content Authors {#content-authors}

Content Authors are responsible for creating, editing, and publishing digital content using AEM's authoring interface. They focus on maintaining content accuracy, brand voice, and consistency across channels.

**Primary Goals**

* Quickly build and update pages using predefined components and templates.
* Manage media and assets effectively.
* Ensure content aligns with marketing and brand standards.

### Form Author {#form-authors}

Form Authors design, configure, and maintain interactive and adaptive forms in AEM Forms to collect user data and enable digital self-service experiences.

**Primary Goals**

* Build and manage adaptive forms without heavy coding.
* Ensure forms are accessible, responsive, and compliant.
* Integrate forms with back-end systems or workflows for data handling.

### Interactive Communications Authors {#interactive-communications-authors}

Interactive Communications Authors design and create personalized, data-driven correspondence such as account statements, policy documents, bills, and welcome kits using AEM's Interactive Communications editor.

**Primary Goals**

* Create and maintain professional correspondence with minimal technical expertise.
* Ensure communications are data-integrated, personalized, and compliant with brand standards.
* Integrate communications with back-end data sources for dynamic content generation.

### Marketing / Business Stakeholders {#stakeholders}

Marketing and Business Stakeholders define campaign goals, messaging strategies, and KPIs. They use AEM for content insights, personalization, and governance oversight rather than hands-on authoring.

**Primary Goals**

* Deliver consistent, personalized experiences across channels.
* Ensure brand and compliance standards are met.
* Measure content effectiveness and campaign impact.

### Developers {#developers}

Developers extend and customize AEM's capabilities to meet organizational needs. They work on back-end (OSGi, Sling, JCR) and front-end (HTL, JS, CSS) layers to implement new components, templates, and integrations.

**Primary Goals**

* Build and maintain scalable, performant AEM implementations.
* Enable authors with flexible, reusable components.
* Integrate AEM with other systems (CRM, commerce, analytics

## Activation {#activation}

To activate and gain access to the Production Agent you need to email Adobe. To get started you can contact:

* `experience-production-agent@adobe.com`
* or reach out to your account team

To speed up the process it helps to provide the following information:

* For AEM as a Cloud Service
  * You need to provide your:
    * Organization ID
    * `product_id` 
    * `profile_id`

  * These values could be found using the following steps:
    * Your administrator needs to visit <https://adminconsole.adobe.com/>
    * Select **Adobe Experience Manager as a Cloud Service**
    * Select the appropriate AEM instance
    * Select the profile that allows read and write operations for the content in question
    * Grab the browser URL
    * Extract `product_id` and `profile_id` from the URL. 
      For example, <https://adminconsole.adobe.com/products/profiles/users>

* Edge Delivery Document Authoring
  * Provide your Adobe team with the following information:
    * Relevant domains
    * Relevant Github information:
      * Org
      * Repo
      * Branch
