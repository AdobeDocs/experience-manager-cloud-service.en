---
title: Content Update Skill
description: Learn what the Brand Experience Agentic Capability content update job is and what it can do for you.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Content Update Skill {#content-update}

The content update skill is part of the [Experience Production Agentic Capability](/help/ai-in-aem/agentic-capabilities/brand-experience/experience-production/overview.md) automates content production to accelerate everyday tasks for Adobe Experience Manager (AEM) as a Cloud Service and Edge Delivery Services. 

Content Update performs updates to existing content in Adobe Experience Manager (AEM), including Content Fragments, Pages and Assets. It can perform actions such as updating, removing, replacing, or adding content elements to keep experiences current and accurate. It can use natural language descriptions or visual elements such as annotated PDFs and screenshots.

<!-- Add link when available -->

For more details see this video.

>[!NOTE]
>
>The Content Update skill is part of the [Experience Production Agentic Capability](/help/ai-in-aem/agentic-capabilities/brand-experience/experience-production/overview.md).

## Use cases {#use-cases}

| Use Case | Description | Skill(s) | Application | Sample Prompts |
| --- | --- | --- | --- | --- |
| Update AEM pages  | Perform actions such as updating, removing, replacing, or adding content elements to keep experiences accurate and current. Inputs can be natural language or visual annotations like PDFs or screenshots. | `aem-sites-pages-update` | Adobe Experience Manager (AEM) | On &lt;URL&gt; update the headline to Hello World<br><br>on &lt;URL&gt; change “Take our Coffee Quiz” button to a more engaging version<br><br>Update &lt;URL&gt; based on the attached<br><br>on &lt;URL&gt; I want to a add a new teaser section to the bottom of the page about a promotion we are running in the month of august that is buy a coffee machine and get 2 bags of coffee free. Also find image of friends drinking coffee and use that in the teaser |
| Update AEM in bulk | Perform bulk actions across multiple pages at the same time such as removing, replacing, or adding content elements to keep experiences accurate and current. | `aem-sites-pages-bulkreplace` | Adobe Experience Manager (AEM) | on &lt;aem path&gt; update all pages that contain copy "MyBarista\" to "BrewPass" |
| Edit Content Fragments | Use natural language to manage a single Content Fragment or hundreds at once. AI handles search, creation, updates, publishing, tagging, and other content operations while automatically enforcing the appropriate governance workflow. | `aem-sites-contentfragments-bulk-edit` | Adobe Experience Manager (AEM) | find Content Fragments under &lt;CF_path&gt; whose calories field is set to 150  and update to 200 also update the 'Serving Style' field on the same fragments to 'Iced'<br><br>Create 3 fragments ones under &lt;CF_path&gt;  name them 'Cortado Freddo Summer’, 'Turkish Coffee Summer’, 'Café de Olla Summer’ and 'Calories' 150 each. Tag the 3 fragments with the 'Frescopa : Coffee' tag |
| Discovery Content Fragments | Find content fragments using natural language. Supports both semantic (intent) based or keyword based search. | `aem-sites-contentfragments-discover` | Adobe Experience Manager (AEM) | find Content Fragments under &lt;CF_path&gt; whose calories field is set to 150  |
| Inspect Content Fragments for dependencies, semantic readiness, and publish readiness | Optimize and manage Content Fragments for AI-powered experiences through readiness checks that include semantic analysis and impact assessment. Evaluates content quality, metadata, structure, schema compliance, and references to surface issues affecting search, publishing, translation, or headless delivery. Analyzes dependencies across Content Fragments, collections, assets, models, and pages to identify risks and recommend safe actions. Finally it provides assessments with guided, human-reviewed remediation steps. | `aem-sites-contentfragments-inspect` | Adobe Experience Manager (AEM) |Run a health check on the folder &lt;CF_path&gt;<br><br>Is content fragment  &lt;CF_path&gt; ready to publish?<br><br>is folder &lt;CF_path&gt; ready for semantic search?<br><br>Is this Content Fragment &lt;CF_path&gt; being referenced by other fragments? What will happen if I delete it?<br><br>Show me the dependency tree for &lt;CF_path&gt; |
