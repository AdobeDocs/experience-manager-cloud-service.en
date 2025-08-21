---
title: Forms Experience Builder
description: Craft powerful forms faster using Form Fragments
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
exl-id: 92357836-1f56-44b1-9934-f9e8dd990e58
---
# Introduction to Forms Experience Builder

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This documentation is currently being tested against the product and is subject to updates and revisions. Features, commands, and examples may change as the Forms Experience Builder continues to evolve during the early-adopter program.

The Forms Experience Builder brings the power of artificial intelligence to Adobe Experience Manager (AEM) Forms. This innovative solution transforms how organizations create, manage, and optimize their digital forms through natural language interactions and intelligent automation.

Built on modern web technologies and powered by advanced AI services, the Forms Experience Builder enables both technical and non-technical users to create sophisticated, professional-grade forms through conversational interfaces. Whether you're a business analyst needing a simple registration form or a developer creating complex multi-step workflows, the Forms Experience Builder streamlines the entire form creation process.

## Conversational Interface

The Forms Experience Builder provides an intuitive chat-based interface that makes form creation as simple as having a conversation:

```
┌─────────────────────────────────────────────────────────┐
│ Forms Experience Builder                               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  👤 User: Create a customer feedback form              │
│                                                         │
│  🤖 AI: I'll help you create a feedback form. What    │
│       type of feedback do you want to collect?         │
│                                                         │
│  👤 User: Product reviews with ratings and comments    │
│                                                         │
│  🤖 AI: Perfect! I've created a feedback form with:   │
│       * Product rating (1-5 stars)                     │
│       * Comment field                                   │
│       * Customer email (optional)                       │
│       * Submit to email notification                    │
│                                                         │
│  👤 User: Add a field for product category             │
│                                                         │
│  🤖 AI: Added a dropdown field with common categories  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Core Capabilities

### AI-Powered Form Creation

**Natural Language Form Generation**

Create complete forms from scratch using plain English descriptions. Simply describe your requirements, such as "Create a customer feedback form with rating scales and comment fields," and the Forms Experience Builder generates the appropriate form structure, field types, and validation rules.

**Dynamic Field Management**

Add, modify, or remove form fields through conversational commands. The AI understands context and can intelligently suggest field types, validation rules, and user interface improvements based on your requirements.

**Layout Optimization**

Update form layouts and configurations through natural language. Request changes like "Make the form more mobile-friendly" or "Reorganize fields in a logical flow," and the Forms Experience Builder applies appropriate styling and layout adjustments.

### Intelligent Import and Conversion

**PDF to Form Conversion**

Transform static PDF documents into interactive, dynamic forms. Upload any PDF document, and the Forms Experience Builder analyzes the structure to create a corresponding digital form with appropriate field types and validation.

**URL to Form Conversion**

Convert existing web forms or pages into AEM Forms. Simply provide a URL, and the Forms Experience Builder extracts form elements and recreates them as native AEM Forms with enhanced functionality.

**Multi-Format File Support**

Handle various file types for form creation, including PDFs, images, screenshots, and existing form templates. The Forms Experience Builder can process and convert these into functional AEM Forms.

### Advanced Form Logic and Integration

**Intelligent Rule Generation**

Create complex form validation and business logic rules through natural language. The Forms Experience Builder can generate sophisticated conditional logic, field dependencies, and validation rules that would typically require extensive coding knowledge.

**Comprehensive Submit Action Configuration**

Configure form submissions to integrate with your existing business systems:

- **Email Integration**: Set up automated email notifications and confirmations
- **REST API Endpoints**: Connect to custom applications and services
- **Cloud Storage**: Integrate with Azure Blob Storage, SharePoint, and OneDrive
- **Workflow Automation**: Connect to Power Automate and Workfront Fusion
- **Marketing Platforms**: Direct integration with Marketo for lead management
- **AEM Workflows**: Leverage existing AEM workflow capabilities

**Performance Analytics**

Analyze form conversion performance and user engagement patterns. The Forms Experience Builder provides insights into form effectiveness and suggests optimizations to improve completion rates and user experience.

## How It Works

The Forms Experience Builder follows a simple, conversational approach:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  1. Describe    │───▶│  2. AI Creates  │───▶│  3. Refine &    │
│  Your Form      │    │  Initial Form   │    │  Configure      │
│  Requirements   │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  "Create a loan application form"  →  Form with relevant        │
│  "Add conditional logic"           →  fields and basic          │
│  "Connect to CRM system"           →  validation rules          │
└─────────────────────────────────────────────────────────────────┘
```

## Use Case Examples

### Loan Application Form 

```
┌─────────────────────────────────────────────────────────┐
│ Loan Application - Multi-Step Form                    │
├─────────────────────────────────────────────────────────┤
│ Step 1: Personal Information                           │
│  🏠 Property Type: [Primary] [Investment] [Commercial] │
│  💰 Loan Amount: [$_______] (triggers different paths) │
│  📊 Income Verification: [W2] [Self-Employed] [Other]  │
│                                                         │
│ Step 2: Financial Details (conditional based on above) │
│  ↳ If Self-Employed: Show tax returns, profit/loss     │
│  ↳ If W2: Show employment history, pay stubs           │
│  ↳ Complex debt-to-income calculations                 │
│                                                         │
│ Step 3: Compliance & Review                            │
│  📋 Regulatory disclosures, digital signatures         │
│  🔍 Automated eligibility pre-screening                │
└─────────────────────────────────────────────────────────┘
```

### Insurance Claim Form

```
┌─────────────────────────────────────────────────────────┐
│ Insurance Claim - Adaptive Form                        │
├─────────────────────────────────────────────────────────┤
│ 🚗 Claim Type: [Auto] [Property] [Health] [Business]   │
│                                                         │
│ ↳ Auto Selected: Shows accident details, police report │
│ ↳ Property: Shows damage assessment, repair estimates  │
│ ↳ Health: Shows medical provider network, pre-auth     │
│                                                         │
│ 📎 Dynamic Document Requirements:                       │
│   * Photos/videos of damage                            │
│   * Police reports (auto only)                         │
│   * Medical records (health only)                      │
│   * Repair estimates (property only)                   │
│                                                         │
│ 🔄 Real-time claim status updates                      │
└─────────────────────────────────────────────────────────┘
```

### Migration and Conversion Scenarios

Transform your existing forms into powerful digital experiences with AI-powered conversion.


### 📄 PDF to Digital

**From static documents to interactive forms**

Transform PDF forms with 50+ fields into dynamic digital experiences with automated calculations and mobile-responsive design.

**Key benefits:**

- Automated tax calculations and field dependencies
- Digital signatures and e-filing integration
- Mobile-responsive layout optimization
- 95% reduction in processing errors

**Best for:** Tax forms, government applications, complex business documents

**Time savings:** 2-3 hours → 15 minutes per form



### 🏛️ Legacy XFA Modernization  

**Breathe new life into outdated forms**

Convert complex XFA applications into modern multi-step wizards with real-time validation and accessibility compliance.

**Key benefits:**

- Streamlined multi-step wizard interface
- Real-time validation with contextual help
- Government database integration
- Full WCAG 2.1 accessibility compliance

**Best for:** Government permits, enterprise applications, compliance forms

**Impact:** 70% faster completion, 90% fewer errors




### 📱 Screenshot to Digital

**Turn any paper form into a digital experience**

Upload an image of any paper form and watch AI extract fields, optimize layout, and create integration-ready digital forms.

**Key benefits:**

- Intelligent field type detection (99%+ accuracy)
- Optimized responsive layout generation
- Enhanced validation beyond original paper
- Integration-ready architecture

**Best for:** Paper applications, handwritten forms, legacy documents

**Processing time:** 2 hours → 5 minutes per form



### 🌐 HTML Enhancement

**Supercharge your existing web forms**

Add advanced validation, conditional logic, and multi-channel submission to basic HTML forms without breaking existing functionality.

**Key benefits:**

- Advanced validation logic and rules
- Conditional field behaviors and workflows
- Multi-channel submission options
- Built-in analytics and performance tracking

**Best for:** Contact forms, registration forms, simple web applications

**Conversion improvement:** +40% with enhanced user experience


## Forms Experience Builder vs Traditional Development

| Aspect | Traditional Form Creation | Forms Experience Builder |
|--------|---------------------------|----------------------|
| **Time to Create** | 2-3 days | 2-3 hours |
| **Technical Knowledge** | Required | Not required |
| **Validation Rules** | Manual coding | Natural language |
| **Mobile Optimization** | Manual CSS/JS | Automatic |
| **Accessibility** | Manual implementation | Built-in compliance |
| **Updates** | Code changes required | Natural language |


## Benefits for Organizations

### Democratized Form Creation

Empower non-technical users to create sophisticated forms without programming knowledge. Business analysts, subject matter experts, and content creators can directly translate their requirements into functional forms through natural language conversations.

### Reduced Time to Value (TTV)

Dramatically accelerate form development from days to hours. What previously required extensive development cycles can now be accomplished in a single session through conversational AI, enabling faster go-to-market for digital initiatives.

### Interface Simplicity

Eliminate the learning curve with an intuitive conversational interface. Users can create complex forms using natural language instead of learning technical form building tools, reducing training time and increasing adoption.

### Scaling Modernization Efforts

Modernize legacy form portfolios efficiently. Convert existing PDF, XFA, and HTML forms to responsive digital experiences while preserving business logic and enhancing user experience across your entire form ecosystem.

## Getting Started

To get started with the Forms Experience Builder, visit the [Forms Experience Builder documentation](forms-ai-assistant-getting-started.md). You can access the Forms Experience Builder through the AEM Forms Editor or Universal Editor, depending on your preferred workflow.

For organizations aiming to transform their form creation processes, the Forms Experience Builder offers a powerful, intuitive solution that combines the flexibility of conversational AI with the robustness of enterprise-grade form management.

## Onboarding and Early Access

The Forms Experience Builder is currently available as part of the Early Access (EA) program. To participate and gain access, follow these steps:

1. Ensure you are using your official work email address associated with your organization.
2. Send an email to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) requesting access to the Forms Experience Builder.
3. Include your organization name and any relevant project details in your request to help expedite the onboarding process.

>[!NOTE]
>
> Access to the Forms Experience Builder is limited to approved participants in the Early Access program. Adobe will review your request and provide further instructions for onboarding if you are eligible.

For more information about the Early Access program and its features, see the [AEM Forms Early Access documentation](/help/forms/early-access-ea-features.md).
