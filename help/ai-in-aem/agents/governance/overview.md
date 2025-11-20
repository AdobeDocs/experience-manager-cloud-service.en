---
title: Governance Agent Overview
description: Learn how the AEM Governance Agent safeguards brand integrity and compliance across AEM
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
---

# Governance Agent Overview {#governance-agent}

The **Governance Agent** is a solution designed to safeguard brand integrity and compliance across Adobe Experience Manager. It enforces security, regulatory, and brand policies to ensure every interaction and activation adheres to established standards. The Governance Agent is fully integrated in AI assistant and is designed to operate seamlessly within enterprise environments by leveraging **A2A (Agent-to-Agent)** and **MCP (Model Control Protocol)** tools. These integrations enable the agent to connect with advanced AI orchestrators such as ChatGPT, Claude, and other external AI systems, ensuring flexible and scalable intelligence across platforms.

Key capabilities include:

* **Brand governance:** Maintain brand consistency and reduce manual review by automating brand checks across content and assets
* **Permissions & Digital Rights Management (DRM):** Ensures secure and compliant collaboration by controlling permissions and usage rights across digital assets.

By combining these features, the Governance Agent reduces risk and enables fast, secure, and on-brand delivery at scale.

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses. 
>
>See also [Adobe Experience Cloud Generative AI User Guidelines](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html). 

## Skills in AEM Governance Agent {#skills-in-aem-governance-agent}

### Brand Governance {#brand-governance}

The governance agent can validate content against brand guidelines to ensure consistency across all digital experiences. It uses pre-ingested brand rules, such as tone, claims, logo usage, typography, and imagery. It operates in real-time within the chat, editors and batch mode in Experience Hub, making it ideal for AI-generated content, site migrations, and brief-based site creation. 

![Brand Governance Overview](/help/ai-in-aem/agents/governance/assets/brand-governance.png)

**Prompt Examples:**

* *Is this page aligned with my brand? `https://www.website/en.html`*
* *Does this `https://www.website/en.html` follow brand messaging guidelines?*
* *Check if `https://www.website/homepage` follows brand guidelines*
* *Show me my brand guidelines*

### Permission and Digital Rights Management {#permission-and-digital-rights-management}

#### Permission Management in Content Hub {#permission-management-in-content-hub}

In Content Hub, the governance agent ensures that only the right people access the right assets at the right time. By applying granular, attribute-based controls and usage rights, it protects sensitive content while enabling secure collaboration. This means reduced compliance risk, stronger brand integrity, and faster workflows, teams can confidently share and reuse assets without worrying about unauthorized access or misuse. This balance of security and flexibility translates into higher operational efficiency and trust across the organization.

![Permission Management Overview](/help/ai-in-aem/agents/governance/assets/permission-management.png)

**Prompt Examples:**

* *Show all existing Content Hub ABAC rules.*
* *Create a rule that gives the "Marketing" group access to all assets.* 
* *Give the Sales group access to assets where marketing:segment equals EMEA.*
* *Delete all the rules which gives access to external-agency*
* *What is ABAC in Content Hub and what can you help me do?*

#### Assets Digital Rights Management {#assets-digital-rights-management}

Using the agent, you can manage your Assets digital rights across your content ecosystem. It controls permissions and usage rights at a granular level, ensuring that assets are accessed and used only within defined compliance boundaries. This delivers peace of mind, protecting intellectual property, reducing regulatory risk, and maintaining brand integrity. By automating rights enforcement, teams can collaborate securely and confidently, accelerating content distribution without compromising security or compliance.

![DRM Management Overview](/help/ai-in-aem/agents/governance/assets/drm-management.png)

**Prompt Examples:**

* *Are any of my assets expiring soon?*
* *Find me all bike assets that expired last month.*
* *Which assets recently expired?*
* *Find me assets without an expiry date*
* *Show me all assets in /content/dam/products that are about to expire in the next 14 days*

