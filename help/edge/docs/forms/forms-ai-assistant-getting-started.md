---
title: Getting Started with Forms Experience Builder
description: Learn how to use the Forms Experience Builder to create and manage forms with progressive disclosure for all user types
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
---

# Getting Started with Forms Experience Builder

>[!NOTE]
>
> The Forms Experience Builder capability is available under the **Early Access (EA) program**. If you are interested, send a quick email from your work address to `aem-forms-ea@adobe.com` to request access to the capability.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This documentation is currently being tested against the product and is subject to updates and revisions. Features, commands, and examples may change as the Forms Experience Builder continues to evolve during the Early Access program.

This comprehensive guide helps you get started with creating and managing forms using conversational AI technology. Whether you're a beginner looking to create your first form or an advanced user seeking to leverage sophisticated features, you'll find detailed information and practical examples to guide your journey through the Forms Experience Builder's capabilities.

## Prerequisites and Setup

### 1. Request Access

The Forms Experience Builder is currently available as part of the Early Access (EA) program. To participate and gain access, you'll need the following information:

**Required Information**

- **IMS Organization ID**: Your Adobe organization identifier
- **Program ID**: Your specific program identifier within Adobe Experience Cloud
- **Project Details**: Timeline, scope, and intended use cases
- **Official Work Email**: Associated with your organization's Adobe account

**How to Obtain IMS Organization ID and Program ID**

For detailed steps to locate your IMS Organization ID and Program ID, see:

- [Adobe Experience Cloud Organization Setup Guide](/help/onboarding/cloud-manager-introduction.md)
- [Program and Environment Management](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md)

**Request Access**

1. Gather your IMS Organization ID and Program ID using the guides above
2. Send an email to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) requesting access
3. Include in your request:
   - Organization name and IMS Organization ID
   - Program ID
   - Project timeline and scope
   - Intended use cases and business objectives

>[!IMPORTANT]
>
> **Limited Availability Program**: Access to Forms Experience Builder is subject to approval from internal stakeholders. Adobe will review your request based on program capacity and alignment with Early Access criteria. Approval is not guaranteed and depends on current program availability.

### 2. Verify Forms is Enabled

Before using Forms Experience Builder, ensure [AEM Forms is enabled for your environment](/help/forms/setup-forms-cloud-service.md).


### 3. Set Up Your Environment


- **For Edge Delivery Services (EDS):**

  - [Setup environment for Edge Delivery Services Forms](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md)
  - [Create a new form using the Edge Delivery Forms template](/help/edge/docs/forms/universal-editor/create-forms.md)
   
- **For Core Component based forms:**

  - On your Adobe Experience Manager instance, got to Forms > Forms & Documents
  - [Create a new page using the Core Components Template](/help/forms/creating-adaptive-form-core-components.md)


## Quick Start

### Access the Forms Experience Builder

Forms Experience Builder is available in Forms Managment UI, Universal Editor, and Adaptive Forms Editor. You can use any of these methods to access form:

**Forms Management UI (for Core Components)**

1. **Navigate to Forms**: Go to AEM > Forms > Forms & Documents
1. Click the Forms Experience Builder icon in the toolbar. It is near top left of UI. 
     ![AI Assistant icon*](/help/edge/docs/forms/assets/forms-manager.gif){width="50%"} 
1. Begin your conversational form creation


**Adaptive Forms Editor (for Core Components)**

1. Go to AEM > Forms > Forms & Documents
2. [Create a new form using Core Components template](/help/forms/creating-adaptive-form-core-components.md)
3. Open your form for editing
4. Click the Forms Experience Builder icon in the editor toolbar
      ![AI Assistant icon*](/help/edge/docs/forms/assets/adaptive-forms-editor.gif){width="75%"} 

5. Begin your conversational form creation


**Universal Editor (for Edge Deilvery Services Forms)**

1. Follow the [Edge Delivery Services setup guide](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md) to create your EDS page
1. Navigate to your EDS page in Universal Editor
1. Look for the Forms Experience Builder icon in the right panel
1. Click to open the conversational interface



### Your First Form

| Conversation Example                                                                                                                        |   |
|--------------------------------------------------------------------------------------------------------------------------------------------|---|
| **Try this conversation to create a comprehensive contact form (based on Summit demo):**<br><br>**You:** "Create a contact form to capture personal information including full name, email address, phone number, company name, job title, and a message field for inquiries"<br><br>**AI:** Select a template<br>&nbsp;&nbsp;&nbsp;&nbsp;A drop-down to select a template<br><br>**AI:** Select a theme<br>&nbsp;&nbsp;&nbsp;&nbsp;A drop-down to select a theme<br><br>**AI:** Create Form| ![Your First Form](/help/edge/docs/forms/assets/create-form.png) |
| <br>**AI:** Open Created Form   | </br> The form is created and opened in editor |


### Essential Commands

| Symbol | Purpose | Example Usage |
|--------|---------|---------------|
| `/` | Quick actions and shortcuts | `/create-form contact form`, `/help validation rules`, `/update-layout wizard` |
| `@` | Reference existing form fields | `@email`, `@firstName`, `Make @phoneNumber required` |
| Plain text | Natural conversation | "Add a required phone number field", "Create validation for email" |

**Specific Command Examples:**

- `/create-form customer survey` - Creates a new customer survey form
- `/add-field @email validation` - Adds validation to existing email field
- `/create-rule show @spouse if @maritalStatus equals married` - Creates conditional logic
- `/configure-submit to email support@company.com` - Sets up email submission
- `/help multi-step forms` - Gets help on multi-step form creation

### Tips for Success

- **Be specific**: "Add a required email field with validation" works better than "add email"
- **Reference existing fields**: Use `@fieldName` when modifying forms
- **Ask for help**: Type `/help` followed by your question
- **Iterate**: Make one change at a time for best results


## Ways to start creating a Form

### 1. Start with natural language prompts

Describe your form requirements in natural language, and the Forms Experience Builder generates the complete form structure:

**Examples:**

- "Create a loan application form with personal info, financial details, and document uploads"
- "Build a customer feedback form with ratings, comments, and product categories"
- "I need a multi-step registration form for a conference with payment processing"

### 2. Import and Convert

Transform existing forms and documents into modern, interactive experiences:

**Supported Sources:**

- **PDF Forms**: Upload static PDFs to convert these to interactive digital forms with validations. 
- **Screenshots or Images**: Upload photo of paper forms to generate functional digital versions 
- **XFA Forms**: Comvert legacy XFA-based forms to modern responsive forms

**How to Import:**

1. Click the attachment icon in the Forms Experience Builder interface
2. Upload your file (PDF, image, Figma design, etc.)
3. Describe your requirements:
   - "Convert this PDF form to a digital version"
   - "Create a form matching this screenshot layout"
   - "Build this form from my Figma design"

**Supported File Types:**

- **Images** (PNG, JPG, GIF): Form layouts, UI mockups, scanned forms, hand-drawn sketches
- **PDF Files**: Existing forms, specifications, documents, Acroforms, XFA forms
- **Screenshots**: Desktop/mobile app screenshots, paper form photos, whiteboard sketches
- **Hand-drawn Sketches**: Napkin sketches, wireframes, concept drawings (photographed)

### Key Interactions

#### Adding Form Elements

**Basic additions:**

    👤 You: "Add a section for personal information"    
    👤 You: "Include a file upload for resume"
    👤 You: "Add a dropdown for country selection"

**Detailed specifications:**

    👤 You: "Add a personal information panel with fields for full name, date of birth, phone number, and email address"    
    👤 You: "Include a secure file upload component for documents, limited to PDF files under 5MB"
    👤 You: "Add a country dropdown with options for USA, Canada, UK, and Germany"

#### Creating Dynamic Behavior

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

#### Form Layout and Design

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

### Submit Configuration

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





## Advanced Form Operations


### Complex Rule Creation

Create sophisticated validation and business logic that responds to user interactions and ensures data integrity:

    👤 You: "Show the address section only if the user selects 'Ship to different address'"
    🤖 AI: "Created a conditional rule that shows/hides the address panel based on checkbox selection"

### Multi-Step Form Creation

    👤 You: "Create a progressive form with 3 steps: personal info, preferences, confirmation"
    🤖 AI: "Created a progressive form with navigation between steps and validation at each stage"

### Advanced Field Types

- File upload with validation and size restrictions for document management
- Date pickers with constraints and business rules for scheduling
- Dropdowns with dynamic options that change based on user selections
- Radio buttons with conditional logic for complex decision trees


### PDF to Form Conversion

    👤 You: "Convert this PDF into an interactive form"
    🤖 AI: "Analyzed the PDF and created a form with appropriate field types and validation"





## Product Help and Learning

The Forms Experience Builder can also teach you about AEM Forms features:

### Ask Questions Like:

- "How do I create a multi-step form?"
- "What's the difference between panels and sections?"
- "How do I set up email notifications?"
- "What are the best practices for mobile-friendly forms?"
- "How do I apply themes to my forms?"

### Get Help On:

- AEM Forms concepts and terminology
- Step-by-step instructions for complex features
- Best practices and recommendations
- Troubleshooting common issues

## Best Practices

### Form Design

- **Keep it simple**: Start with essential fields and add complexity only when necessary to avoid overwhelming users
- **Use clear labels**: Make field purposes obvious with descriptive labels that guide users through the form
- **Provide help text**: Guide users through complex fields with contextual help and examples
- **Test thoroughly**: Validate all user paths to ensure forms work correctly in all scenarios

### User Experience

- **Progressive disclosure**: Show relevant fields based on context to reduce cognitive load and improve completion rates
- **Clear navigation**: Help users understand where they are in the form and what steps remain
- **Responsive design**: Ensure forms work on all devices and screen sizes for maximum accessibility
- **Accessibility**: Follow WCAG guidelines to make forms usable by people with disabilities

### Performance

- **Optimize field count**: Only ask for necessary information to reduce form abandonment and improve completion rates
- **Use appropriate validation**: Prevent errors before submission to provide immediate feedback and guidance
- **Test completion rates**: Monitor and improve form effectiveness through analytics and user feedback
- **Regular updates**: Keep forms current with business needs and user expectations for optimal performance

### Brand Consistency

- **Create brand templates**: Prepare branded form templates with your organization's colors, fonts, and styling before starting form creation
- **Define style standards**: Establish consistent button styles, field layouts, and spacing guidelines that can be referenced in prompts
- **Use brand assets**: Prepare logos, color codes, and brand guidelines for easy reference when creating forms
- **Template library**: Build a collection of branded form templates for common use cases (contact, registration, feedback)
- **Style prompts**: Include brand-specific instructions: "Use company blue (#1234AB) for buttons and corporate font Helvetica"



## Troubleshooting

| Issue | Quick Fix |
|-------|-----------|
| **Interface not loading** | Refresh browser, check internet connection |
| **Commands not working** | Try `/help` or use natural language instead |
| **@fieldName not recognized** | Check spelling, ensure field exists first |
| **File upload fails** | Use PDF/JPG/PNG under 10MB |
| **Form looks wrong** | Be more specific: "Make it mobile-friendly" |
| **Submit configuration fails** | Verify API credentials and permissions |

**Still need help?** Type `/help` followed by your specific question or contact your system administrator.

For additional support, refer to the main [Forms Experience Builder Prompt Library](ai-assistant-prompt-library.md) or contact your system administrator for technical assistance.
