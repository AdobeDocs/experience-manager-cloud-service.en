---
title: Associate UI in Interactive Communication Editor
description: Discover associate UI in Interactive Communication Editor by enabling customer-facing agent to generate personalized, compliant communications.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
---

# Associate UI in Interactive Communication Editor

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

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

Designs and manages the Interactive Communication using Associate UI. ß

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
> Associate must be part of the **forms-associates** group.

## Dynamic Use Cases

The Associate UI supports instant, personalized document generation, crucial for industries with real-time servicing needs.

| Industry | Example Use Cases |
|----------|-------------------|
| **Financial Services** | Generate real-time loan confirmation letters, risk-profile summaries, account creation. |
| **Insurance** | Produce instant Proof-of-Insurance cards or claim disposition summaries. |
| **Healthcare** | Create patient treatment plan summaries with calculated copay and schedules. |
| **Public Sector** | Generate police verification reports, citizen service receipts, grievance acknowledgment letters, and case update summaries on-the-spot. |
| **Government** | Create application status summaries, service approval letters, and real-time communication for welfare scheme enrollments. |

## Enabling the Associate UI Workflow

Author can ollow the steps below to configure and publish an Interactive Communication (IC) for Associate UI access:

>[!NOTE]
>
> Supported components for associate.

### Create the IC

Design and configure the Interactive Communication, ensuring branding, data bindings, compliance rules, and integrations are correctly set.

### Enable the Associate UI

From the top action bar, enable the Associate UI option to make the IC available for associate-driven.

### Enable the Associate UI in component

### Configure Editable Fields

In the required fields section, enable the fields that associates can edit.
Set validations to ensure accurate and controlled data input.

### Publish the IC

After finalizing all configurations, publish the Interactive Communication for secure access.

### Share the Published IC with Associates

Provide the published IC link to the Associate, allowing them to authenticate, enter customer-specific information, and generate the final communication with valid inputs.

The **Associate UI** bridges the gap between structured content authoring and real-time customer engagement.  
By combining intuitive design, robust backend configuration, and strict compliance controls, organizations can deliver **fast, accurate, and personalized communications** at scale.
