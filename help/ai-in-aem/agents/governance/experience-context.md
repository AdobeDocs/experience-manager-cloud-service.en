---
title: Experience Context
description: Learn how Experience Context gives the AEM Governance Agent the brand rules it needs to generate and validate on-brand content.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Experience Context {#experience-context}

Experience Context is the single, authoritative place where your organization records everything an AI needs to create and check content on your behalf. The [Governance Agent](/help/ai-in-aem/agents/governance/overview.md) draws on this shared context to keep every experience on-brand.

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses.
>
>See also [Adobe Experience Cloud Generative AI User Guidelines](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html).

## What Is Experience Context? {#what-is-experience-context}

Modern content is increasingly created, adapted, and reviewed with the help of AI. For that to be safe at enterprise scale, the AI must know your rules: how your brand sounds, what you can claim, how you position against alternatives, and how your experiences should look. Experience Context captures this knowledge in one governed location so it applies consistently, instead of living in scattered PDFs, wikis, and people's heads.

Once your context is in place, it becomes the source of truth that guides content generation and powers automated validation of the content you already have.

## Why Capture It in One Place? {#why-capture-it-in-one-place}

Most organizations already *have* this knowledge, but it is fragmented. Brand voice lives in a style guide, claim rules live in a Legal team's inbox, positioning guidance lives in regional playbooks, and design standards live in a design file. When knowledge is scattered, every new piece of content depends on the right person remembering the right rule. This approach does not scale, and it becomes unreliable when AI is part of the workflow.

Capturing everything in Experience Context gives you:

* **One source of truth.** Every team and every tool works from the same rules, so content stays consistent regardless of who or what produces it.
* **Consistent from the start.** Because generation draws on your context up front, output follows your voice, claims, positioning, and design standards from the beginning, instead of being corrected in review.
* **Ongoing validation.** Because rules change over time, Experience Context lets you [audit existing content](#batch-analysis) against the current rules and identify content that no longer complies.
* **Reusable across tools.** Your context is not locked inside a single application. It is exposed through a standard interface, the Model Context Protocol (MCP), so that any AI system or agent, Adobe's or your own, can query the rules that apply to a task and stay within approved bounds.

Experience Context is the shared input for different AI agents. After you capture it once, any agent that generates, adapts, distributes, or checks your content can use it.

## What Data to Capture {#what-data-to-capture}

Experience Context is organized into categories. Each one answers a different question an AI needs answered before it can act on your behalf. You do not have to fill them all in at once. Start with the categories that matter most for your content, and build up over time.

| Category | Answers the question | Examples |
|---|---|---|
| [**Brand Voice**](#brand-voice) | *How should we sound?* | Tone, terminology, sentence style, words to prefer or avoid |
| **Claim Guardrails** | *What are we allowed to say?* | Positioning limits and messaging rules pre-approved by your organization |
| **Market Positioning** | *How do we talk about alternatives?* | Approved comparisons and differentiation language |
| **Design System** | *How should it look?* | Approved components, layouts, typography, color, and asset templates |

Together, these categories give an AI a consistent picture of how your brand communicates and presents itself.

<!-- Screenshot: the Experience Context categories as they appear for a brand in the app. -->

## Where Rules Apply {#where-rules-apply}

Experience Context rules are not flat. A rule carries **segments** that determine *when* it applies, so you can set a global default and then layer more specific overrides on top.

You define the segments that fit your organization. There is no fixed list to conform to. Common examples include:

| Example segment | What it might scope |
|---|---|
| **Country / Market** | Jurisdiction and cultural context |
| **Audience** | Who the content addresses (consumers, investors, partners, employees) |
| **Sub-brand** | Distinct brand entities within your organization |
| **Experience Type** | The kind of content (landing page, blog post, help page) |
| **Language** | Language variant, independent of country (for example, Spanish in Mexico versus Spain) |

These are only illustrations. Add whatever segments your content actually varies by.

Rules resolve by inheritance: a global baseline applies everywhere, and segment-specific overrides apply when their conditions match. For example, you might generate a consumer landing page for an automotive sub-brand in Germany, in German. That request layers several rule sets at once: the global brand rules, the automotive sub-brand overrides, any Germany- and consumer-specific adaptations, and German-language preferences.

## How Experience Context Is Used {#how-experience-context-is-used}

Once your context is in place, it does two jobs:

1. **Guides generation.** Before an AI produces content, it consults the rules that apply to the task, such as voice, claims, positioning, and design, so the result is on-brand from the start.
1. **Powers validation.** Experience Context also lets you [audit content you *already have*](#batch-analysis) against your current rules, surfacing where content has drifted from your voice, claims, or design standards so you can fix or regenerate it.

Because your context is exposed through a standard interface, the *same* rules drive both jobs, and remain available to any other AI tool or agent your organization uses.

## Get Started {#get-started}

You do not have to author every rule from a blank page. There are two main ways to populate Experience Context, and most organizations use both:

* **Add rules manually** for the knowledge you already have written down. Each context category ([Brand Voice](#brand-voice), Claim Guardrails, Market Positioning, and [Design System](#design-system)) has its own guided form.
* **Import from a document.** Upload an existing style guide, brand guidelines, or policy PDF as source material for your context. For step-by-step instructions, see [How to Import a Brand Policy](/help/ai-in-aem/agents/governance/how-to-import-a-brand-policy.md).

## Work with Experience Context {#work-with-experience-context}

The sections below describe the building blocks of Experience Context: the **brand** everything lives under, the **brand policies** you import, and the **rules and standards** you maintain.

>[!NOTE]
>
>Many entities carry a **Status**, and the agents use only *Active* ones. New entities are created as *Draft* by default, so you must set an entity to *Active* to put it into effect. This applies to brands, context rules, checks, and domains alike; the sections below add only the steps specific to each entity.

### Brands {#brands}

A **brand** is the top-level container in Experience Governance. It represents a brand whose experiences you want to keep on-brand, and everything else, such as brand policies, context rules, design system, checks, and domains, lives under it.

A brand has a **Name**, an optional **Description**, and a **Status**.

>[!IMPORTANT]
>
>To put a brand into effect, edit it and set its **Status** to *Active*.

<!-- Screenshot: the Brands list, showing the Status column. -->

### Brand Policies {#brand-policies}

A **brand policy** is a structured representation of your brand rules that an AI can understand and enforce. Instead of rewriting your guidelines in a technical format, you import them in their original form, a policy document (PDF) and/or a page URL, and the Governance Agent reads them and extracts everything it can into your Experience Context.

Importing does more than create checks. Any information the agent finds is added to your context. Depending on what the document contains, that can include [brand voice](#brand-voice) guidance, claim guardrails, market positioning, design-system standards, and the policy checks used to enforce them. A single import can populate your context rules *and* checks at once.

Once in place, this context lets the agents:

* analyze existing pages to detect brand inconsistencies,
* flag deviations from tone, terminology, or mandatory rules,
* provide guidance to downstream agents, and
* help keep generated or updated content brand-compliant.

This lets you reuse your existing brand documentation while gaining automated governance. For step-by-step import instructions, see [How to Import a Brand Policy](/help/ai-in-aem/agents/governance/how-to-import-a-brand-policy.md).

### Context Rules {#context-rules}

Context rules capture *how your content should be created*. Three categories are available, [**Brand Voice**](#brand-voice), **Claim Guardrails**, and **Market Positioning**, and they share the same fields:

| Field | What it is |
|---|---|
| **Category** | Groups related rules. Reuse an existing category or create a new one. |
| **Name** | A human-readable name for the rule. |
| **ID** | A stable identifier, generated from the name. |
| **Rule** | The guideline or constraint text itself. |
| **Segments** | Where the rule applies. Leave empty for a global rule. |
| **Status** | Whether the rule is in effect. |

A rule applies only while its **Status** is *Active*. Set it to *Inactive*, *Draft*, or *Archived* to take it out of effect.

>[!NOTE]
>
>**Segments** are what let you set a global default and then layer market- or audience-specific overrides on top. See [Where Rules Apply](#where-rules-apply) for how segments and inheritance work.

For an example of these fields in practice, see [Brand Voice](#brand-voice) below.

### Brand Voice {#brand-voice}

**Brand Voice** is one of the three [context rule](#context-rules) categories in Experience Context. It answers the question *how should we sound?*, capturing your organization's tone, terminology, sentence style, and the words you prefer or avoid, the kind of guidance that would otherwise live scattered across a style guide.

Brand Voice rules use the same fields as any other context rule: **Category**, **Name**, **ID**, **Rule**, **Segments**, and **Status**. Rules extracted automatically when you [import a brand policy](/help/ai-in-aem/agents/governance/how-to-import-a-brand-policy.md) appear alongside those you add manually, and only rules with an *Active* **Status** are applied by the agents.

![A brand's Brand Voice rules](/help/ai-in-aem/agents/governance/assets/brand_voice_rules.png)

### Design System {#design-system}

The **Design System** captures your brand's visual standards, colors and typography, so generated experiences look on-brand.

* **Colors** are organized into groups (for example, *Brand* or *Secondary*). Each color has a **name** and a **hex value**.
* **Typography** is organized into font groups (for example, *Heading* or *Body*). Each style has a **style name**, **font family**, **font size** (with unit), **font weight**, **line height**, **letter spacing** (with unit), and **font style**.

You can scope both colors and typography with **segments**, so different markets or sub-brands can carry different visual standards.

<!-- Screenshot: a brand's Design System, showing color groups and type styles. -->

### Checks {#checks}

A **check** is an automated rule the Governance Agent applies when it reviews content. Checks are how your policies and context become enforceable. The agent may create checks for you when you import a brand policy, or you can define them directly.

A check has:

| Field | What it is |
|---|---|
| **Name** | A human-readable name for the check. |
| **Rule** | The check logic, written with references to your context. |
| **Brand** | The brand the check belongs to. |
| **Category** | An optional grouping for related checks. |
| **Scope** | What the check runs against: **Images**, **Text**, or both. |
| **Status** | Whether the check is in effect. |

A check runs only while its **Status** is *Active*.

### Domains {#domains}

A **domain** defines which URLs a brand's checks apply to, for example a pattern like `*.example.com`. A domain has a **URL Pattern**, a **Brand**, and a **Status**.

>[!IMPORTANT]
>
>To put a domain into effect, go to your brand, click **Domains**, edit the domain using the pencil icon, and set its **Status** to *Active*.

### Batch Analysis {#batch-analysis}

**Batch analysis** runs your checks against a set of existing pages, so you can validate content you already have.

To run a batch analysis:

1. From the brand's **Governance Insights** tab, select **Batch Analysis** in the left panel, then click **+ Start batch analysis** to open the **Start a new batch analysis** dialog.

1. For **Type**, select **List** to paste the URLs you want to analyze directly, one per line.

   ![Starting a batch analysis with a list of URLs](/help/ai-in-aem/agents/governance/assets/start_batch_analysis_list.png){width="70%"}

1. Alternatively, select **Sitemap Discovery** to have Batch Analysis crawl a sitemap instead of supplying URLs manually. Enter the site or page URL to crawl, set a **Max pages** limit (default 50), and optionally add **Include patterns** or **Exclude patterns** (glob patterns, for example `*/en/*` to include only certain paths, or `*/content/dam/*` to exclude others).

   ![Starting a batch analysis with sitemap discovery](/help/ai-in-aem/agents/governance/assets/start_batch_analysis_sitemap_discovery.png){width="70%"}

1. Click **Start analysis** to queue the job. The **Batch Analysis** list shows every job you run, along with its date, type, scope, status, and number of pages.

1. Once a job completes, review its results under **Evaluation Results**, as shown below:

   ![Overview of batch analysis results](/help/ai-in-aem/agents/governance/assets/batch_analysis_results.png)

   This view reports:

   * Summary cards for **Total Pages** evaluated, **Aligned Pages** and **Non-Aligned Pages** (whether pages meet brand standards), and the overall **Pass Rate**
   * A **Checks** breakdown showing how many individual checks passed, failed, or did not apply (N/A) across the analyzed pages
   * A per-page table listing each URL with its last check date, alignment status, and counts of succeeded, failed, not-applicable, and errored checks, with a link to view full details for that page

   Results can be filtered to **Pages** or **Images**.

## Related Topics {#related-topics}

* [Governance Agent Overview](/help/ai-in-aem/agents/governance/overview.md)
* [How to Import a Brand Policy](/help/ai-in-aem/agents/governance/how-to-import-a-brand-policy.md)
