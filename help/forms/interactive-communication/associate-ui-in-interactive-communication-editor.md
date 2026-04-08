---
title: Associate UI in Interactive Communication Editor
description: Discover associate UI in Interactive Communication Editor by enabling customer-facing agent to generate personalized, compliant communications.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 9ba58659-b14c-4ebc-a6d9-e56a4b6aa48b
---
# Associate UI in Interactive Communication Editor

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

The **Associate UI** is a specialized, simplified interface built on top of Interactive Communications (IC) editor. It is designed for customer-facing professionals, such as field associates and service agents to generate personalized, compliant, and accurate communications in real time during live interactions.

![Find IC Doc](/help/forms/interactive-communication/assets/associate-ui-preview.png)

## Associate UI Interface

The Associate UI provides a clean, two-panel workspace that enables fast and secure communication generation:

### Left Panel: Data Entry

- Associates enter or confirm customer-specific information.
- Validations, helper texts, and mandatory fields guide accurate input.

### Right Panel: Real-Time Preview

- Displays an instant preview of the final document.
- Automatically updates as the associate fills in data.

### Instant Document Generation

- Generate or download the finalized communication.

## User Personas and Responsibilities

The Associate UI is driven by three core roles, each with distinct responsibilities:

### 1. Administrator

Responsible for system setup, governance, backend integrations, and user access.

| Responsibility | Focus |
|---------------|-------|
| System Configuration | Sets up core infrastructure, user groups, Form Data Models (FDM), output . |
| Governance & Security | Manages user permissions and ensures system compliance. |
| Integration Management | Maintains backend integrations and live customer data connections. |

### 2. Author

Designs and manages the Interactive Communication and configures it for Associate UI (including enabling Associate View and optional workflow).

| Responsibility | Focus |
|---------------|-------|
| IC Authoring & Design | Creates layout, branding, and compliant document structure. |
| Field Configuration | Maps data fields, defines Editable, Mandatory, and Read-Only fields. |
| Publishing & Enablement | Publishes the IC and shares the link for associate access. |

### 3. Associate 

Uses the Associate UI to assist customers, update information and generate compliant communications.


| Responsibility | Focus |
|---------------|-------|
| Data Confirmation | Fills or validates customer data via the left entry panel. |
| Preview & Validation | Ensures accuracy using the real-time preview panel. |
| Delivery | Generates the PDF/email and sends it via approved channels. |

>[!NOTE]
>
> Associates must be part of the **forms-associates** group. For authors who also submit from the Associate UI on the Author instance, add them to **workflow-users** as well.

## Dynamic Use Cases

The Associate UI supports instant, personalized document generation, crucial for industries with real-time servicing needs.

| Industry | Example Use Cases |
|----------|-------------------|
| **Financial Services** | Generate real-time loan confirmation letters, risk-profile summaries, account creation. |
| **Insurance** | Produce instant Proof-of-Insurance cards or claim disposition summaries. |
| **Healthcare** | Create patient treatment plan summaries with calculated copay and schedules. |
| **Public Sector** | Generate police verification reports, citizen service receipts, grievance acknowledgment letters, and case update summaries on-the-spot. |
| **Government** | Create application status summaries, service approval letters, and real-time communication for welfare scheme enrollments. |

## Enabling the Associate UI

Authors enable the Associate UI and optionally configure a workflow for submissions in **Interactive Communication Settings**:

1. **Enable Associate View** — In **Associate Properties**, check **Enable Associate View Editing**, then click **Apply Changes** and save the document.
2. **Configure workflow (optional)** — In **Workflow**, turn **Configure Workflow for Update** On, select a workflow model, and optionally set a success message and redirection URL.
3. **Configure editable fields** — Enable the fields that associates can edit and set validations.
4. **Publish and share** — Publish the IC and share the link with associates.

For step-by-step instructions with screenshots and submission/workflow behavior (Author on Author vs Associate on Publish), see [Enable and configure Associate UI for Interactive Communications](/help/forms/interactive-communication/enable-configure-associate-ui.md). To build a workflow that generates PDF from IC submissions, see [Submission workflow for Associate UI — IC Generate PDF Output](/help/forms/interactive-communication/submission-workflow-associate-ui-ic-pdf.md).

The **Associate UI** bridges the gap between structured content authoring and real-time customer engagement.  
By combining intuitive design, robust backend configuration, and strict compliance controls, organizations can deliver **fast, accurate, and personalized communications** at scale.

## See also

- [Enable and configure Associate UI for Interactive Communications](/help/forms/interactive-communication/enable-configure-associate-ui.md)
- [Integrate Associate UI in Your Application](/help/forms/interactive-communication/invoke-associate-ui.md)
- [Submission workflow for Associate UI — IC Generate PDF Output](/help/forms/interactive-communication/submission-workflow-associate-ui-ic-pdf.md)
