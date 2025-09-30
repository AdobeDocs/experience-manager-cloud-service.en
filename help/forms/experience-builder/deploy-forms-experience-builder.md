---
title: Deploy and configure Forms Experience Builder
description: Learn how to use the Forms Experience Builder to create and manage forms with progressive disclosure for all user types
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
exl-id: 977f227e-e941-4797-ba74-53d5b8c60ca9
---
# Deploy and configure Forms Experience Builder

>[!NOTE]
>
> The Forms Experience Builder is available under an early access program. Before you begin, please ensure you have requested and been granted access. For complete instructions, see the [Onboarding](product-overview.md#onboarding) information .

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This documentation is currently being tested against the product and is subject to updates and revisions. Features, commands, and examples may change as the Forms Experience Builder continues to evolve during the Early Access program.

This comprehensive guide helps you get started with creating and managing forms using conversational AI technology. Whether you're a beginner looking to create your first form or an advanced user seeking to leverage sophisticated features, you'll find detailed information and practical examples to guide your journey through the Forms Experience Builder's capabilities.

## Prerequisites and setup

### Access requirements

Before using Forms Experience Builder, ensure you have:

* **Access to Forms Experience Builder** - Available through the Early Access Program
* **AEM Forms as a Cloud Service** - Production author environment with Adaptive Forms Core Components
* **Basic understanding** - Familiarity with form concepts and business requirements

### Verify forms is enabled

Before using Forms Experience Builder, ensure [AEM Forms is enabled for your environment](/help/forms/setup-forms-cloud-service.md).

### Set up your environment

Your setup process depends on your AEM Forms implementation. Choose the path that matches your project.

**For Edge Delivery Services**

If you are using Edge Delivery Services Forms and primarily use the Universal Editor. [Prepare your project for Edge Delivery Services Forms](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md). This is a one-time setup to enable the Forms Experience Builder.

**For Core Components-based forms**

If you are using Adaptive Forms based on Core Components in the AEM author environment, ensure [Adaptive Forms Core Components are enabled](/help/forms/enable-adaptive-forms-core-components.md) for your environment.  



## Quick start

### Access the forms experience builder

You can access the Forms Experience Builder from three primary locations, depending on your workflow and form type.


**1. Adaptive Forms Editor (for Core Components)**

You can launch the builder directly while editing a specific form.

1. Navigate to **AEM > Forms > Forms & Documents**.
1. [Create a new form using a Core Components template](/help/forms/creating-adaptive-form-core-components.md) or open an existing one.
1. Select the **Forms Experience Builder** icon in the editor's toolbar to open the conversational interface.

      ![AI Assistant icon*](/help/edge/docs/forms/assets/adaptive-forms-editor.gif){width="75%"} 

**1. Universal Editor (for Edge Delivery Services Forms)**

For forms delivered via Edge Delivery Services, the builder is integrated into the Universal Editor.

1. Open your Edge Delivery Services form in the Universal Editor.
2. Select the **Forms Experience Builder** icon in the right panel to launch the conversational interface.

### Your first form

| Conversation Example                                                                                                                        |   |
|--------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Try this conversation to create a comprehensive contact form (based on Summit demo):**<br><br>**You:** "Create a contact form to capture personal information including full name, email address, phone number, company name, job title, and a message field for inquiries"<br><br>**AI:** Select a template<br>&nbsp;&nbsp;&nbsp;&nbsp;A drop-down to select a template<br><br>**AI:** Select a theme<br>&nbsp;&nbsp;&nbsp;&nbsp;A drop-down to select a theme<br><br>**AI:** Create Form| ![Your First Form](/help/edge/docs/forms/assets/create-form.png) |
| <br>**AI:** Open Created Form   | </br> The form is created and opened in editor |


### Essential commands

| Symbol | Purpose | Example Usage |
|--------|---------|---------------|
| `/` | Quick actions and shortcuts | `/create-form contact form`, `/help validation rules`, `/update-layout wizard` |
| `@` | Reference existing form fields | `@email`, `@firstName`, `Make @phoneNumber required` |
| Plain text | Natural conversation | "Add a required phone number field", "Create validation for email" |

**Specific Command Examples:**

* `/create-form customer survey` - Creates a new customer survey form
* `/add-field @email validation` - Adds validation to existing email field
* `/create-rule show @spouse if @maritalStatus equals married` - Creates conditional logic
* `/configure-submit to email support@company.com` - Sets up email submission
* `/help multi-step forms` - Gets help on multi-step form creation

### Tips for success

* **Be specific**: "Add a required email field with validation" works better than "add email"
* **Reference existing fields**: Use `@fieldName` when modifying forms
* **Ask for help**: Type `/help` followed by your question
* **Iterate**: Make one change at a time for best results


## Ways to start creating a form

### Start with natural language prompts

Describe your form requirements in natural language, and the Forms Experience Builder generates the complete form structure:

**Examples:**

* "Create a loan application form with personal info, financial details, and document uploads"
* "Build a customer feedback form with ratings, comments, and product categories"
* "I need a multi-step registration form for a conference with payment processing"


### Key interactions

#### Adding form elements

**Basic additions:**

    👤 You: "Add a section for personal information"    
    👤 You: "Include a file upload for resume"
    👤 You: "Add a dropdown for country selection"

**Detailed specifications:**

    👤 You: "Add a personal information panel with fields for full name, date of birth, phone number, and email address"    
    👤 You: "Include a secure file upload component for documents, limited to PDF files under 5MB"
    👤 You: "Add a country dropdown with options for USA, Canada, UK, and Germany"

#### Creating dynamic behavior

**Simple logic:**

    👤 You: "Show additional fields when 'Other' is selected"
    🤖 AI: "Created a conditional rule that shows additional fields when 'Other' is chosen"
    
    👤 You: "Make the email field required"
    🤖 AI: "Updated the email field to be required with validation"
    
    👤 You: "Calculate the total automatically"
    🤖 AI: "Added calculation logic to automatically compute totals"

**Complex business rules:**

    👤 You: "Show the spouse information fields only when marital status is set to 'Married'"
    🤖 AI: "Created a conditional rule that displays spouse fields based on marital status"
    
    👤 You: "Calculate the total cost by multiplying quantity and price, then add 10% tax"
    🤖 AI: "Added calculation logic with quantity, price, and tax computation"
    
    👤 You: "Enable the submit button only when all required fields are completed and terms are accepted"
    🤖 AI: "Created validation logic that enables submission only when all conditions are met"

#### Form layout and design

**Layout changes:**

    👤 You: "Make this a multi-step form"
    🤖 AI: "Converted the form to a progressive layout with navigation"
    
    👤 You: "Organize fields in two columns"
    🤖 AI: "Updated the layout to display fields in a two-column arrangement"
    
    👤 You: "Convert to an accordion layout"
    🤖 AI: "Transformed the form to use accordion-style sections"

**Design improvements:**

    👤 You: "Create a wizard-style form with 3 steps: personal info, preferences, and review"
    🤖 AI: "Created a wizard form with three distinct steps and navigation"
    
    👤 You: "Arrange the address fields in a compact two-column layout"
    🤖 AI: "Organized address fields in a compact two-column format"
    
    👤 You: "Update the layout to match the attached wireframe"
    🤖 AI: "Modified the layout to match the provided design reference"

### Submit configuration

The Forms Experience Builder can configure various submission endpoints to connect your forms with external systems and services:

| Submit Action Type | Setup Command | Use Case |
|------------------|---------------|----------|
| **Email** | "Send form to email" | Notifications and confirmations for form submissions |
| **REST API** | "Submit to REST endpoint" | Custom applications and third-party systems |
| **Cloud Storage** | "Save to Azure/SharePoint" | Document storage and file management |
| **Workflow** | "Connect to Power Automate" | Business process automation and approvals |
| **Marketing** | "Integrate with Marketo" | Lead management and marketing automation |

**Advanced submit configuration examples:**

    👤 You: "Send form submissions to hr@company.com and create a case in our CRM system"
    🤖 AI: "Configured email submission and CRM submit action"
    
    👤 You: "Submit data to our REST API endpoint and trigger the new customer workflow"
    🤖 AI: "Set up REST API submission with workflow triggers"
    
    👤 You: "Email responses to the sales team and add the lead to our marketing automation platform"
    🤖 AI: "Configured multi-channel submission with email and marketing automation"





## Advanced form operations


### Complex rule creation

Create sophisticated validation and business logic that responds to user interactions and ensures data integrity:

    👤 You: "Show the address section only if the user selects 'Ship to different address'"
    🤖 AI: "Created a conditional rule that shows/hides the address panel based on checkbox selection"

### Multi-step form creation

    👤 You: "Create a progressive form with 3 steps: personal info, preferences, confirmation"
    🤖 AI: "Created a progressive form with navigation between steps and validation at each stage"

### Advanced field types

* File upload with validation and size restrictions for document management
* Date pickers with constraints and business rules for scheduling
* Dropdowns with dynamic options that change based on user selections
* Radio buttons with conditional logic for complex decision trees


### PDF to form conversion

    👤 You: "Convert this PDF into an interactive form"
    🤖 AI: "Analyzed the PDF and created a form with appropriate field types and validation"





## Product help and learning

The Forms Experience Builder can also teach you about AEM Forms features:

### Ask questions like:

* "How do I create a multi-step form?"
* "What's the difference between panels and sections?"
* "How do I set up email notifications?"
* "What are the best practices for mobile-friendly forms?"
* "How do I apply themes to my forms?"

### Get help on:

* AEM Forms concepts and terminology
* Step-by-step instructions for complex features
* Best practices and recommendations
* Troubleshooting common issues


For additional support, refer to the main [Forms Experience Builder Prompt Library](/help/forms/experience-builder/forms-experience-builder-prompt-examples-library.md) or contact your system administrator for technical assistance.
