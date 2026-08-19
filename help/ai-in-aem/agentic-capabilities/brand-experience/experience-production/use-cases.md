---
title: Experience Production Agentic Capabilities Overview
description: Learn how the Experience Production Agentic Capabilities in AEM help you accelerate your content creation and automatically orchestrate changes.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Experience Production Agentic Capabilities {#experience-production-agentic-capabilites}

The Experience Production Agentic Capability of Adobe Enterprise Manager (AEM) as a Cloud Service collaborates with [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview) to help you accelerate your content creation and automatically orchestrate changes. 

## Use cases {#use-cases}

A range of use-cases are covered.

| Use Case | Description | Skill(s) | Application | Sample Prompts |
| --- | --- | --- | --- | --- |
| Update AEM pages  | Perform actions such as updating, removing, replacing, or adding content elements to keep experiences accurate and current. Inputs can be natural language or visual annotations like PDFs or screenshots. | `aem-sites-pages-update` | Adobe Experience Manager (AEM) | On &lt;URL&gt; update the headline to Hello World<br><br>on &lt;URL&gt; change “Take our Coffee Quiz” button to a more engaging version<br><br>Update &lt;URL&gt; based on the attached<br><br>on &lt;URL&gt; I want to a add a new teaser section to the bottom of the page about a promotion we are running in the month of august that is buy a coffee machine and get 2 bags of coffee free. Also find image of friends drinking coffee and use that in the teaser |
| Update AEM in bulk | Perform bulk actions across multiple pages at the same time such as removing, replacing, or adding content elements to keep experiences accurate and current. | `aem-sites-pages-bulkreplace` | Adobe Experience Manager (AEM) | on &lt;aem path&gt; update all pages that contain copy "MyBarista\" to "BrewPass" |
| Edit Content Fragments | Use natural language to manage a single Content Fragment or hundreds at once. AI handles search, creation, updates, publishing, tagging, and other content operations while automatically enforcing the appropriate governance workflow. | `aem-sites-contentfragments-bulk-edit` | Adobe Experience Manager (AEM) | find Content Fragments under /content/dam/agentic-cf whose calories field is set to 150  and update to 20o also update the 'Serving Style' field on the same fragments to 'Iced'<br><br>Create 3 fragments ones under /content/dam/agentic-cf  name them 'Cortado Freddo Summer’, 'Turkish Coffee Summer’, 'Café de Olla Summer’ and 'Calories' 150 each. Tag the 3 fragments with the 'Frescopa : Coffee' tag |
| Discovery Content Fragments | Find content fragments using natural language. Supports both semantic (intent) based or keyword based search. | `aem-sites-contentfragments-discover` | Adobe Experience Manager (AEM) | find Content Fragments under /content/dam/agentic-cf whose calories field is set to 150  |
| Go from Figma to Visual Content Fragment - technical | Import designs directly from Figma into Adobe Experience Manager using natural language. The skill automatically creates the required content model, content fragment, assets, and visualization template, enabling business users to move from design to web-ready content in minutes without manual setup. | `aem-sites-visualcontentfragments-create` | Adobe Experience Manager (AEM) | Import from &lt;figma path&gt;<br><br>`import-https-www.figma.com-design-DbNX47efHBu8LaDUWmdvb5-Frescopa-Coffee-node-id-2026-08-06 (2).txt` |
| Inspect Content Fragments from a Couple of Perspectives (references, semantic readiness, publish readiness) | Optimize and manage Content Fragments for AI-powered experiences through readiness checks that include semantic analysis and impact assessment. Evaluates content quality, metadata, structure, schema compliance, and references to surface issues affecting search, publishing, translation, or headless delivery. Analyzes dependencies across Content Fragments, collections, assets, models, and pages to identify risks and recommend safe actions. Finally it provides assessments with guided, human-reviewed remediation steps. | `aem-sites-contentfragments-inspect` | Adobe Experience Manager (AEM) |Run a health check on the folder /content/dam/agentic-cf/beverages<br><br>Is content fragment  /content/dam/agentic-cf/beverages/cafe-de-olla ready to publish?<br><br>is folder "/content/dam/gw26summer/semantic-ready" ready for semantic search?<br><br>Is this Content Fragment /content/dam/agentic-cf/muster/americano being referenced by other fragments? What will happen if I delete it?<br><br>Show me the dependency tree for /content/dam/agentic-cf/muster/cocktails-and-specialty<br><br>What are the implications if I modify CF Model /conf/aemshowcase/Agentic-CF/muster/settings/dam/cfm/models/beverage-product? Could it break or alter existing CFs? If yes, which ones?<br><br>Which are the CFs I should think of archiving (not in use) under /content/dam/agentic-cf/muster?<br><br>What content fragments are using the picture content/dam/shared/boilerplate-frescopa/campaigns/3cups.png? |
| Create form using natural language intent | Generate a new Adaptive Form from a plain-language description of the fields and purpose | Form creation | Adobe Experience Manager (AEM) | "Create an employee onboarding form" |
| Create form using attached brief | Generate a form from an uploaded requirements brief describing fields and flow | Form creation | Adobe Experience Manager (AEM) | "Create a form using the attached brief" |
| Create form using attached image/screenshot | Generate a form by interpreting a screenshot or image of a reference form or mockup | Form creation | Adobe Experience Manager (AEM) | "Create a form as per the attached image" |
| Create form using attached PDF | Generate a form by importing an existing PDF form | Form creation | Adobe Experience Manager (AEM) | "Create a form from this attached PDF" |
| Update form — add/edit fields | Add, edit, or remove fields on an existing form | Form creation | Adobe Experience Manager (AEM) | "Add Middle Name field below First Name field" |
| Configure field properties | Set field-level properties such as placeholder text, format validation, dropdown options, and file-type/size restrictions | Form creation | Adobe Experience Manager (AEM) | "Add a text input field for Company Name with placeholder 'Enter your company name'"<br><br>"Configure the Phone Number field with format (XXX) XXX-XXXX and validation"<br><br>"Add a file upload field for Resume with PDF and DOC restrictions, max 5MB" |
| Add smart/knowledge-based fields | Add dropdown or selection fields pre-populated using the AI's built-in knowledge base, without manually specifying every option — for example, country/state lists, industry codes, currency codes, or job titles | Form creation | Adobe Experience Manager (AEM) | "Add a dropdown for departure airports with all major international airports"<br><br>"Add a complete list of US states with abbreviations"<br><br>"Add a field for industry classification with NAICS codes" |
| Update form layout | Adjust the layout of an existing form — field order, column span, panel structure | Form creation | Adobe Experience Manager (AEM) | "Put First Name and Last Name fields in a 2 column layout, 50/50" |
| Update form using attached guidelines | Revise an existing form to align with an uploaded guidelines document | Form creation | Adobe Experience Manager (AEM) | "Update this form to match the attached guidelines document" |
| Add business logic | Create conditional logic, show/hide rules, field dependencies, and define validation rules | Form creation | Adobe Experience Manager (AEM) | "Show the Company field only when Employee Type is Contractor"<br><br>"Make the Email field required and validate it as an email address"<br><br>"Hide the Shipping Address section when Same as Billing Address is checked" |
| Configure form submit action | Set up how a form submits — REST endpoint, email, etc. | Form creation | Adobe Experience Manager (AEM) | "Configure the form to send data to a REST endpoint" |
| Embed form onto a site's page | Place an existing or newly created form onto a designated AEM Sites page (supported on Edge Delivery Services pages only) | Form creation | Adobe Experience Manager (AEM) | "Embed this form on the homepage of our site" |

<!--
## Known limitations {#known-limitations}

Based on a team bug bash (~191 scripted scenarios), cross-checked against independent verification. Point-in-time snapshot as of 2026-08-14 — re-verify against ongoing testing before publishing.

Confirmed working:

- All four creation paths: natural-language intent, attached brief, attached screenshot, attached PDF
- Simple layout edits: column span/width, field and panel reordering, multi-column layout within a panel
- Guidelines-file-driven updates (e.g., a markdown guidelines doc)
- Site-page embedding — Edge Delivery Services (EDS) only
- Simple field-level rules (show/hide) on non-fragment fields
- REST and email submit to a known endpoint

Confirmed broken / not yet supported:

1. Structural layout conversion (flat form to wizard/accordion/tabs) is additive-only — it adds a new, empty structure alongside existing content instead of migrating it. Even a wizard built from scratch has no real multi-step or collapse behavior.
2. Site-page embedding on Core Components pages is not supported (EDS only).
3. Form Fragment blindness — fields living inside a referenced Form Fragment are invisible to rename, rules, colspan/styling, and field-count introspection. Largest cluster of bugs in the bash. High risk for any form built on reusable fragments/panels.
4. No post-creation branding/theme workflow — theme is only selectable at creation time; no way to change brand color, font, or add a logo afterward.
5. Repeatable fields/panels — backend properties (min/max, repeatable flag) can be set correctly, but the "add another instance" gesture is unreliable in the previewer.
6. Minor: checkbox creation intermittently fails (missing checked/unchecked values).
-->
