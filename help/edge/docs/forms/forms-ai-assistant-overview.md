---
title: Forms Experience Builder
description: Craft powerful forms faster using Form Fragments
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
---

# Introduction to Forms Experience Builder

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This documentation is currently being tested against the product and is subject to updates and revisions. Features, commands, and examples may change as the Forms Experience Builder continues to evolve during the early-adopter program.

The AEM Forms Experience Builder leverages the power of Generative AI to democratize and accelerate the creation and updating of digital form experiences. By enabling intent-based workflows driven through natural language interactions, it empowers users to seamlessly design, modify, and optimize forms with speed and simplicity.

Built on modern web technologies and powered by advanced AI services, the Forms Experience Builder enables both technical and non-technical users to create sophisticated, professional-grade forms through conversational interfaces. This revolutionary approach reduces time to value from days to hours, eliminates technical barriers through interface simplicity, and scales modernization efforts across your entire form ecosystem.



## Core Capabilities

Forms Experience Builder offers two primary workflows for creating powerful digital forms:

### 1. AI-Powered Form Creation

**Natural Language Form Generation**

Create complete forms from scratch using plain English descriptions. Simply describe your requirements, such as "Create a customer feedback form with rating scales and comment fields," and the Forms Experience Builder generates the appropriate form structure. You use the experience builder of visual editors to add more fields, validation rules, and submission logic. 

**Dynamic Field Management**

Add, modify, or remove form fields through conversational commands. The AI understands context and can intelligently suggest field types, validation rules, and user interface improvements based on your requirements.

**Layout Optimization**

Update form layouts and configurations through natural language. Request changes like "Change form layout to wizard layout" and the Forms Experience Builder applies appropriate styling and layout adjustments.

**Comprehensive Submit Action Configuration**

Configure form submissions to integrate with your existing business systems:

- **Email Integration**: Set up automated email notifications and confirmations
- **REST API Endpoints**: Connect to custom applications and services
- **Cloud Storage**: Integrate with Azure Blob Storage, SharePoint, and OneDrive
- **Workflow Automation**: Connect to Power Automate and Workfront Fusion
- **Marketing Platforms**: Direct integration with Marketo for lead management
- **AEM Workflows**: Leverage existing AEM workflow capabilities


### 2. Intelligent Import and Conversion

**Supported Import Formats**

Transform existing forms and documents into interactive digital experiences. The Forms Experience Builder supports:

- **Acroforms**: Interactive PDF forms with existing field structures
- **XFA PDFs**: Complex XML-based form architectures
- **Flat PDFs**: Static documents converted to interactive forms
- **Images and Screenshots**: JPG, PNG formats (check with team for size limitations)
- **Hand-drawn Forms**: Sketches and paper form photographs


**Intelligent Conversion Process**

The uploaded content is analyzed to:

- Detect field types and relationships
- Preserve layout to extent possible
- Enhance with modern responsive design
- Add advanced validation and conditional logic
- Optimize for accessibility and mobile experience

## How It Works

The Forms Experience Builder follows a simple, conversational approach:

    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
    │  1. Describe    │───▶│  2. AI Creates  │───▶│  3. Refine &    │
    │  Your Form      │    │  Initial Form   │    │  Configure      │
    │  Requirements   │    │                 │    │                 │
    └─────────────────┘    └─────────────────┘    └─────────────────┘
             │                       │                       │
             │                       │                       │
             ▼                       ▼                       ▼
    ┌───────────────────────────────────────────────────────────────────────────┐
    │  "Create a loan application form"  →  Form with relevant                  │
    │  "Add email field"           →  fields and basic                          │
    │  "Set value of email filed to @firstname@gmail.com" →  validation rules   │
    └───────────────────────────────────────────────────────────────────────────┘

## Example Scenarios

:::: landing-cards-container
:::
![icon](https://cdn.experienceleague.adobe.com/icons/file-pdf.svg)

**Transform PDF Forms to Digital Forms**

Convert Acroforms, XFA PDFs, or flat PDF documents into responsive, interactive digital forms with enhanced functionality.
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/data-transfer-up.svg)

**Modernize Legacy XFA Forms**

Transform complex XFA applications into modern, accessible digital experiences with improved user workflows.
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/image.svg)

**Convert Screenshots to Digital Forms**

Turn images, screenshots, or hand-drawn forms into fully functional digital experiences.
:::
::::

<!-- #### Import and Enhance Web Forms

Import existing HTML forms and enhance them with advanced features while preserving existing functionality.

**Key benefits:**

- Advanced validation and business logic
- Conditional field behaviors
- Multi-channel submission options
- Enhanced user experience design -->

## Forms Experience Builder vs Traditional Development

| Aspect | Traditional Form Creation | Forms Experience Builder |
|--------|---------------------------|----------------------|
| **Time to Create** | 2-3 days | 2-3 hours |
| **Technical Knowledge** | Required | Not required |
| **Validation Rules** | Manual coding | Natural language |
| **Accessibility** | Manual implementation | Built-in compliance |


## Benefits for Organizations

:::: landing-cards-container
:::
![icon](https://cdn.experienceleague.adobe.com/icons/users.svg)

**Democratized Form Creation**

Empower non-technical users to create sophisticated forms without programming knowledge through natural language conversations.
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/bolt.svg)

**Reduced Time to Value (TTV)**

Dramatically accelerate form development from days to hours, enabling faster go-to-market for digital initiatives.
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/lightbulb.svg)

**Interface Simplicity**

Eliminate the learning curve with an intuitive conversational interface, reducing training time and increasing adoption.
:::

:::
![icon](https://cdn.experienceleague.adobe.com/icons/layers.svg)

**Scaling Modernization Efforts**

Modernize legacy form portfolios efficiently, preserving business logic and enhancing user experience across your entire form ecosystem.
:::
::::

## Onboarding 

The Forms Experience Builder is currently available as part of the Early Access (EA) program. To participate and gain access, you'll need the following information:

### Required Information

- **IMS Organization ID**: Your Adobe organization identifier
- **Program ID**: Your specific program identifier within Adobe Experience Cloud
- **Project Details**: Timeline, scope, and intended use cases
- **Official Work Email**: Associated with your organization's Adobe account


### How to Obtain IMS Organization ID and Program ID

For detailed steps to locate your IMS Organization ID and Program ID, see:

- [Adobe Experience Cloud Organization Setup Guide](/help/onboarding/cloud-manager-introduction.md)
- [Program and Environment Management](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md)

### Request Access

1. Gather your IMS Organization ID and Program ID using the guides above
2. Send an email to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) requesting access
3. Include in your request:
   - Organization name and IMS Organization ID
   - Program ID
   - Project timeline and scope
   - Intended use cases and business objectives

>[!IMPORTANT]
>
> **Limited Availability Program**: Access to Forms Experience Builder is subject to approval from internal stakeholders. Adobe will review your request based on program capacity and alignment with early access criteria. Approval is not guaranteed and depends on current program availability.

For more information about the Early Access program and its features, see the [AEM Forms Early Access documentation](/help/forms/early-access-ea-features.md).


## Getting Started

To get started with the Forms Experience Builder, visit the [Forms Experience Builder documentation](forms-ai-assistant-getting-started.md). You can access the Forms Experience Builder through the AEM Forms Editor or Universal Editor, depending on your preferred workflow.

For organizations aiming to transform their form creation processes, the Forms Experience Builder offers a powerful, intuitive solution that combines the flexibility of conversational AI with the robustness of enterprise-grade form management.
