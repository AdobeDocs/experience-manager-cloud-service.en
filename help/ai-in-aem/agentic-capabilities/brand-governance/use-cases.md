---
title: Brand Governance Agentic Capabilities Overview
description: Learn how the Brand Governance Agentic Capabilities in AEM help you safeguard brand integrity and compliance.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Brand Governance Agentic Capabilities {#brand-governance-agentic-capabilites}

The Brand Governance Agentic Capability of Adobe Enterprise Manager (AEM) as a Cloud Service collaborates with [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview) to safeguard brand integrity and compliance. It enforces security, regulatory, and brand policies to ensure every interaction and activation adheres to established standards.

## Use cases {#use-cases}

A range of use-cases are covered.

| Use Case | Description | Skill(s) | Application | Sample Prompts |
| --- | --- | --- | --- | --- |
| Full brand context lookup | Retrieve the cascade-resolved brand rules and verticals for a brand | enterprise-context | Adobe Experience Manager (AEM)  | "Give me the full brand context for this brand"<br>"What verticals exist for this brand?"<br>"Resolve the owning brand for this asset path" |
| Create or update brand rules | Add or modify a brand-context rule for a claim-type vertical | enterprise-context | Adobe Experience Manager (AEM) | "Add a new disclaimer rule for the pharma vertical"<br>"Update rule #42 to require a citation" |
| Guideline & segment lookup | Retrieve detailed brand guidelines, scoped by segment, market, or category | enterprise-context | Adobe Experience Manager (AEM) | "What are the tone-of-voice guidelines for this brand?"<br>"List the claim categories used in the health vertical" |
| Evaluate content against brand guidelines | Evaluate a published/authored page, text block, or image against configured brand checks | aem-governance | Adobe Experience Manager (AEM) | "Evaluate this landing page against SecurBank guidelines"<br>"Does this tagline pass our tone-of-voice checks?" |
| Check configuration | List all configured checks (guidelines) for one or every brand | aem-governance | Adobe Experience Manager (AEM) | "List every check configured for SecurBank"<br>"What guidelines apply to this URL?" |
| Brand inventory discovery | List and identify all configured brands for the organization | aem-governance | Adobe Experience Manager (AEM) | "List all brands configured"<br>"What guidelines apply to this URL `http://frescopa-coffee`" |
| Audit AEM permissions | Explore configured permission policies, ACLs, and inheritance rules for group, or service account at a given path | aem-governance | Adobe Experience Manager (AEM) | "Audit Amit's access under `/content/folder`"<br>"What can this service account do at this path?"<br>"Show the access policies applied to this content path `/content/`" |
| Debug AEM permissions | debug / understand permission policies, ACLs, and inheritance rules. | aem-governance | Adobe Experience Manager (AEM) | "Why can principal admin write `/content/folder/us` on `https://author/` ?"<br>"Why can't sample-author write in `/content/dam` on `https://author`" |
