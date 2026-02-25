---
title: How to Import A Brand Policy
description: Use the Adobe Governance Agent to Import a Brand Policy
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# How to Import a Brand Policy {#how-to-import-a-brand-policy}

## Overview {#overview}

A brand policy defines the rules, standards, and constraints that ensure all content produced or updated by Adobe Experience Manager remains consistent with a company's brand identity. This typically includes tone of voice, terminology, visual guidelines, and editorial rules.

The Governance Agent uses brand policies as a source of truth to analyze existing pages and guide content generation. Customers can provide their own original brand policies, which the Governance Agent automatically converts into AI-readable policy checks. These checks are then used to validate content and to provide the Production Agent with a reliable, enforceable framework to generate or update pages that remain aligned with the brand.

## What is a Brand Policy in the Governance Agent {#what-is-a-brand-policy-in-the-governance-agent}

In the context of the Governance Agent, a brand policy is a structured representation of your brand rules that can be understood and enforced by AI. Rather than requiring customers to rewrite their guidelines in a technical format, the Governance Agent accepts brand policies in their original form (for example, documents, guidelines, or rule descriptions).

Once imported, the policy is transformed into a set of AI policy checks that can:

* Analyze existing pages to detect brand inconsistencies
* Flag deviations from tone, terminology, or mandatory rules
* Provide clear guidance to downstream agents
* Ensure that generated or updated content remains brand-compliant by design

This approach allows teams to reuse their existing brand documentation while benefiting from automated governance and scalable content production.

## How Brand Policies are Used {#how-brand-policies-are-used}

After a brand policy is imported:

* The Governance Agent interprets and normalizes the policy into enforceable AI checks
* Pages can be analyzed against the policy to identify gaps or violations
* The Production Agent uses these checks as constraints when generating or updating content
* Brand compliance becomes consistent, repeatable, and auditable across sites and teams


## Import a Brand Policy {#import-a-brand-policy}

To import a brand into the Governance Agent:

1. Create a brand, by giving a name and a main domain. You can do this by clicking on the **Governance Context** button on the left hand navigation in your Experience Manager home, then press the **+ Add Brand** button, as shown below:

   ![Adding a new brand](/help/ai-in-aem/agents/governance/assets/add_brand.png)

1. Set the name of the brand and a description in the following window

   ![Naming the brand](/help/ai-in-aem/agents/governance/assets/add_brand_dialogue.png)

1. New brands are created in draft status. Make sure you change your newly created brand to an Active status, by clicking on your brand's card, pressing the edit (pencil) in the top right corner of the screen, set the **Status** to **Active** in the following window, and click **Save Changes**. You need to enable the brands by setting them to Active before being able to use them.

   ![Set the brand's status to Active](/help/ai-in-aem/agents/governance/assets/set_brand_active.png)

1. Once the brand is created, create a main domain in the following window by pressing the **Domains** link on the left:

   ![Configuring a domain for the brand](/help/ai-in-aem/agents/governance/assets/add_domain.png)

   >[!IMPORTANT]
   >
   >Just like new brands, new domains are created with a default Draft status. To change this, go to your Brand, click on **Domains**, then edit your domain using the pencil icon and set its status to **Active**. 

1. After you've configured the main domain, you can upload your brand policy document by goint to **Policies** in the upper left corner of the window, and pressing the **+ Add Policy** button.

   ![Adding a policy from the Brand card](/help/ai-in-aem/agents/governance/assets/add_policy_treeview.png)

   >[!NOTE]
   >
   >Alternatively, you can also add policies by switching over to the **Policies** tab and pressing the **+ Add Policy** link.

1. In the next window, press on **Upload PDFs** and select your brand policy document(s) in PDF format

   ![Upload your brand policy document](/help/ai-in-aem/agents/governance/assets/upload_brand_policy_document.png)

   The Governance Agent will parse your brand policy guideline using natural lanuguage, and it will extract the checks obtained from the document and translate them into actual tasks. Once the document is processed, you can view a summary of the import, including the number of checks and the status of the policy, as shown below:

   ![An overview window of the brand policy status](/help/ai-in-aem/agents/governance/assets/policy_status.png)

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

1. Lastly, for a list of domains and the brands they are associated with, you can press the **Domains** tab. This section will allow you to add, delete or modify domains in your list.
   