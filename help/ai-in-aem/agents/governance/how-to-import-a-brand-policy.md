---
title: How to Import A Brand Policy
description: Use the Adobe Governance Agent to Import a Brand Policy
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
exl-id: 8057e82b-36d4-4280-b433-f26cfcfe9fe6
---
# How to Import a Brand Policy {#how-to-import-a-brand-policy}

## Overview {#overview}

[Experience Context](/help/ai-in-aem/agents/governance/experience-context.md) provides Adobe Experience Manager (AEM) agents with organization-specific knowledge and guidance, enabling them to understand the context in which they operate. It can capture brand identity, tone of voice, terminology, editorial guidance, and other standards that are important for creating consistent and relevant experiences.

Importing a brand policy is one way to establish this Experience Context in AEM. The Governance Agent processes your organization's existing brand policy and transforms it into structured, precise, and actionable context. From this context, the Governance Agent can derive [governance checks](/help/ai-in-aem/agents/governance/experience-context.md#checks) to evaluate content against specific brand requirements.

Experience Context goes beyond governance checks. Once established, it can provide AI-powered and agentic capabilities with the relevant and targeted context they need for a given task. This enables agents to use the appropriate brand guidance when generating, updating, or evaluating content, rather than relying on generic instructions or the complete brand policy for every interaction.

## What is a Brand Policy in the Governance Agent {#what-is-a-brand-policy-in-the-governance-agent}

A brand policy contains the principles, guidelines, and requirements that define how your organization's brand should be represented, including tone of voice, terminology, messaging, visual identity, and other brand-specific guidance.

When a brand policy is imported, the Governance Agent analyzes its content and transforms the relevant guidance into structured [Experience Context](/help/ai-in-aem/agents/governance/experience-context.md). This makes the information easier for AI-powered and agentic capabilities to consume and apply to specific tasks.

As part of this process, the Governance Agent derives [governance checks](/help/ai-in-aem/agents/governance/experience-context.md#checks) from the Experience Context. These checks translate specific brand requirements into actionable criteria that can be used to evaluate content for brand compliance.

Experience Context itself remains broader than these checks. It provides a reusable source of precise brand knowledge that can be segmented and surfaced according to the needs of different agentic workflows.

This approach allows teams to reuse their existing brand documentation while benefiting from automated governance and scalable content production.

## How Brand Policies are Used {#how-brand-policies-are-used}

After a brand policy is imported and processed, the resulting Experience Context can be used across AI-powered and agentic workflows in AEM.

Experience Context enables agents to retrieve and apply the specific brand knowledge that is relevant to the task they are performing, rather than relying on the complete brand policy for every interaction. Agents select the appropriate context based on the brand, content, or task at hand.

For governance use cases, the Governance Agent derives actionable [checks](/help/ai-in-aem/agents/governance/experience-context.md#checks) from this context. These checks can be used to:

* Analyze existing content and identify brand inconsistencies
* Flag deviations from specific brand requirements
* Provide actionable guidance for content updates
* Help ensure generated or updated content remains aligned with the brand

Beyond governance, Experience Context can also provide other AI-powered and agentic capabilities with precise, relevant brand guidance when generating, updating, or evaluating content.

## Import a Brand Policy {#import-a-brand-policy}

To import a brand into the Governance Agent:

1. In AEM, select **Experience Context** from the left navigation. The Experience Context console displays the brands available in your organization. To create Experience Context for a new brand, select **+ Add Brand**.

   ![The Experience Context console](/help/ai-in-aem/agents/governance/assets/experience_context_console.png){width="70%"}

1. In the **Add brand** dialog, enter the information used to establish the brand and its initial Experience Context:

   * **Name** — Enter the name of the brand. This field is required.
   * **Description** — Optionally provide a description of the brand.
   * **Domain** — Optionally specify the primary website URL associated with the brand.
   * **Brand guideline document** — upload an existing brand guideline in PDF format. The Governance Agent analyzes the document to extract key brand information and uses it to establish structured context for the brand.

   You can drag and drop the brand guideline document, or select **Browse files** to choose it. When finished, select **Add brand**.

   ![The Add brand dialog](/help/ai-in-aem/agents/governance/assets/add_brand_dialog.png){width="60%"}

1. New brands are created in draft status. Make sure you change your newly created brand to an Active status by clicking on your brand's card, pressing the edit (pencil) icon in the top right corner of the screen, setting the **Status** to **Active** in the following window, and clicking **Save Changes**. You need to enable the brands by setting them to Active before being able to use them.

   ![Set the brand's status to Active](/help/ai-in-aem/agents/governance/assets/set_brand_active.png){width="60%"}

1. To manage the domains associated with a brand, open the brand and select **Enterprise Knowledge**, then select **Domains** in the left navigation. The **Allowed Domains** section lists the domains associated with the brand. From here, you can add a new domain by entering its URL and selecting **Add Domain**, edit an existing domain, or delete a domain that is no longer needed. Wildcards are supported for subdomains. For example, `*.example.com` allows subdomains of `example.com`.

   ![Managing a brand's allowed domains](/help/ai-in-aem/agents/governance/assets/manage_allowed_domains.png){width="70%"}

   >[!IMPORTANT]
   >
   >Just like new brands, new domains are created with a default Draft status. To change this, edit your domain using the pencil icon and set its status to **Active**.

1. After configuring your brand, you can add a brand policy by opening the brand, selecting **Enterprise Knowledge**, then **Policies**, and pressing **+ Add Policy**.

   ![Adding a policy from Enterprise Knowledge](/help/ai-in-aem/agents/governance/assets/add_policy_enterprise_knowledge.png){width="70%"}

1. Pressing **+ Add Policy** opens the **Add context** dialog, where you provide the actual policy content: a **Context page URL**, a PDF document, or both:

   * **Context page URL** — Specify the public page where the relevant context or policy is available.
   * **Upload PDF** — Upload a PDF containing the brand guidelines or policy information that you want to add to the brand's Experience Context.

   Select **Add context** to start processing the information.

   ![The Add context dialog](/help/ai-in-aem/agents/governance/assets/add_context_dialog.png){width="60%"}

   The Governance Agent analyzes the submitted document or page using natural language, and extracts the checks obtained from it, translating them into actual tasks. This processing can take some time; you can return to the **Policies** view to check the status. Once processing is complete, the policy is displayed with its status and the number of governance checks linked to it, as shown below:

   ![An overview of the brand policy status, including linked checks](/help/ai-in-aem/agents/governance/assets/policy_status_linked_checks.png)

<!-- Alexandru: commenting out for now
1. Once your brand is created, and your policy document is uploaded, you can get a detailed per-brand view by going to the **Brands** tab, and clicking on a brand's card. This is the view you'll want to use for creating cagtegories of checks, by pressing the three dots next to an existing category, and selecting **+ Add Category**, as shown in the screenshot below:

   ![Add category](/help/ai-in-aem/agents/governance/assets/add_category.png)

   You can also use this view to create, edit and delete checks, which we will detail in the steps below.

1. For a more granular view of each individual check, you can switch over to the **Checks** tab, and view a list of each individual check extracted from your guideline documents. You can filter checks based on brand or status:

   ![See individual brand checks](/help/ai-in-aem/agents/governance/assets/see_brand_checks.png)

   Additionally, you can view additional details on each individual check by clicking the three dots (**...**) to the left of the check, and pressing **View details**. This will open a new window with more information about the check:

   ![View individual check details](/help/ai-in-aem/agents/governance/assets/view_check_details.png)

   You can also delete checks by pressing **Delete** from the same menu location, or edit them by pressing **Edit**:

   ![Editing a check](/help/ai-in-aem/agents/governance/assets/edit_check.png)

1. You can manually add a check by pressing **Add Check** in the upper left corner of the Checks window:

   ![Adding a check](/help/ai-in-aem/agents/governance/assets/add_check.png)

   In the following screen, you can configure details such as:

   * The name of the check
   * The rule, described in natural language
   * The category
   * The scope(s) it applies to

   ![Configuring the check details](/help/ai-in-aem/agents/governance/assets/add_check_window.png)
-->

For details on how checks are created, categorized, and managed, see the [Checks](/help/ai-in-aem/agents/governance/experience-context.md#checks) section of Experience Context.

## Related topics {#related-topics}

* [Experience Context](/help/ai-in-aem/agents/governance/experience-context.md)
* [Governance Agent overview](/help/ai-in-aem/agents/governance/overview.md)
