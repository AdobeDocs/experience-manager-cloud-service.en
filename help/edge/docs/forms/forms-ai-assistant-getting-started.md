---
title: Getting Started with Forms Experience Builder
description: Learn how to use the Forms Experience Builder to create and manage forms with progressive disclosure for all user types
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
exl-id: b8f64082-a23f-4919-ad66-042faad77d30
---

# Getting Started with Forms Experience Builder

>[!NOTE]
>
> The Forms Experience Builder capability is available under the **early-adopter program**. If you are interested, send a quick email from your work address to `aem-forms-ea@adobe.com` to request access to the capability.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This documentation is currently being tested against the product and is subject to updates and revisions. Features, commands, and examples may change as the Forms Experience Builder continues to evolve during the early-adopter program.

This comprehensive guide helps you get started with creating and managing forms using conversational AI technology. Whether you're a beginner looking to create your first form or an advanced user seeking to leverage sophisticated features, you'll find detailed information and practical examples to guide your journey through the Forms Experience Builder's capabilities.

## Prerequisites and Setup

### 1. Request Access

If you don't have access to the Forms Experience Builder:

1. **Request Access**: Send an email to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) from your work email
2. **Include Information**: Organization name and project details
3. **Wait for Approval**: Adobe will review and provide onboarding instructions

### 2. Verify Forms is Enabled

Before using Forms Experience Builder, ensure [AEM Forms is enabled for your environment](/help/forms/setup-forms-cloud-service.md).


### 3. Set Up Your Environment


* **For Edge Delivery Services (EDS):**
 
   * [Setup environment for Edge Delivery Services Forms](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md)
   * [Create a new form using the Edge Delivery Forms template](/help/edge/docs/forms/universal-editor/create-forms.md)
   
* **For Core Component based forms:**

   * On your Adobe Experience Manager instance, got to Forms > Forms & Documents
   * [Create a new page using the Core Components Template](/help/forms/creating-adaptive-form-core-components.md)

## Quick Start

### Access the Forms Experience Builder

**Universal Editor**

* Open your EDS page in Universal Editor
* Look for the Forms Experience Builder icon in the left panel
* Click to open the conversational interface

**Adaptive Forms Editor**

* Navigate to: AEM > Forms > Forms & Documents  
* Create or open a core components based form for editing
* Click the Forms Experience Builder icon in the editor toolbar

### Your First Form

Try this simple conversation to get started:

```
👤 You: "Create a simple contact form"
🤖 AI: "I'll create a contact form with name, email, and message fields for you."

👤 You: "Make the email field required"
🤖 AI: "Updated the email field to be required with validation."
```

### Essential Commands

| Symbol | Purpose | How to Use |
|--------|---------|------------|
| `/` | Quick actions and shortcuts | Type `/create` for form creation, `/help` for assistance |
| `@` | Reference existing form fields | Type `@fieldName` to modify specific fields (e.g., `@email`) |
| Plain text | Natural conversation | Describe what you want: "Add a required phone number field" |

### Tips for Success

* **Be specific**: "Add a required email field with validation" works better than "add email"
* **Reference existing fields**: Use `@fieldName` when modifying forms
* **Ask for help**: Type `/help` followed by your question
* **Iterate**: Make one change at a time for best results

## Core Features

### Two Ways to Create Forms

#### 1. Create from Scratch

Describe your form requirements in natural language, and the Forms Experience Builder generates the complete form structure:

**Examples:**

* "Create a loan application form with personal info, financial details, and document uploads"
* "Build a customer feedback form with ratings, comments, and product categories"
* "I need a multi-step registration form for a conference with payment processing"

#### 2. Import and Convert

Transform existing forms and documents into modern, interactive experiences:

**Supported Sources:**

* **PDF Forms**: Upload static PDFs → Interactive digital forms with validation
* **Screenshots/Images**: Photo of paper forms → Functional digital versions  
* **HTML Forms**: Basic web forms → Enhanced AEM Forms with advanced features
* **XFA Forms**: Legacy Adobe forms → Modern responsive forms
* **URLs**: Existing web forms → Native AEM Forms with improved UX

**How to Import:**

1. Click the attachment icon in the Forms Experience Builder interface
2. Upload your file (PDF, image, Figma design, etc.)
3. Describe your requirements:
   * "Convert this PDF form to a digital version"
   * "Create a form matching this screenshot layout"
   * "Build this form from my Figma design"

**Supported File Types:**

* **Images** (PNG, JPG, GIF): Form layouts, UI mockups, scanned forms
* **PDF Files**: Existing forms, specifications, documents
* **Figma Files**: Design prototypes, brand guidelines
* **Design Files**: Visual references, style guides

### Key Interactions

#### Adding Form Elements

**Basic additions:**

```
👤 You: "Add a section for personal information"
🤖 AI: "Added a personal information panel with standard fields"

👤 You: "Include a file upload for resume"
🤖 AI: "Added a secure file upload component for documents"

👤 You: "Add a dropdown for country selection"
🤖 AI: "Added a country dropdown with common options"
```

**Detailed specifications:**

```
👤 You: "Add a personal information panel with fields for full name, date of birth, phone number, and email address"
🤖 AI: "Created a personal information panel with all requested fields and appropriate validation"

👤 You: "Include a secure file upload component for documents, limited to PDF files under 5MB"
🤖 AI: "Added a file upload field with PDF restriction and 5MB size limit"

👤 You: "Add a country dropdown with options for USA, Canada, UK, and Germany"
🤖 AI: "Added a country dropdown with the specified options"
```

#### Creating Dynamic Behavior

**Simple logic:**

```
👤 You: "Show additional fields when 'Other' is selected"
🤖 AI: "Created a conditional rule that shows additional fields when 'Other' is chosen"

👤 You: "Make the email field required"
🤖 AI: "Updated the email field to be required with validation"

👤 You: "Calculate the total automatically"
🤖 AI: "Added calculation logic to automatically compute totals"
```

**Complex business rules:**

```
👤 You: "Show the spouse information fields only when marital status is set to 'Married'"
🤖 AI: "Created a conditional rule that displays spouse fields based on marital status"

👤 You: "Calculate the total cost by multiplying quantity and price, then add 10% tax"
🤖 AI: "Added calculation logic with quantity, price, and tax computation"

👤 You: "Enable the submit button only when all required fields are completed and terms are accepted"
🤖 AI: "Created validation logic that enables submission only when all conditions are met"
```

#### Form Layout and Design

**Layout changes:**

```
👤 You: "Make this a multi-step form"
🤖 AI: "Converted the form to a progressive layout with navigation"

👤 You: "Organize fields in two columns"
🤖 AI: "Updated the layout to display fields in a two-column arrangement"

👤 You: "Convert to an accordion layout"
🤖 AI: "Transformed the form to use accordion-style sections"
```

**Design improvements:**

```
👤 You: "Create a wizard-style form with 3 steps: personal info, preferences, and review"
🤖 AI: "Created a wizard form with three distinct steps and navigation"

👤 You: "Arrange the address fields in a compact two-column layout"
🤖 AI: "Organized address fields in a compact two-column format"

👤 You: "Update the layout to match the attached wireframe"
🤖 AI: "Modified the layout to match the provided design reference"
```

### Integration Setup

The Forms Experience Builder can configure various submission endpoints to connect your forms with external systems and services:

| Integration Type | Setup Command | Use Case |
|------------------|---------------|----------|
| **Email** | "Send form to email" | Notifications and confirmations for form submissions |
| **REST API** | "Submit to REST endpoint" | Custom applications and third-party systems |
| **Cloud Storage** | "Save to Azure/SharePoint" | Document storage and file management |
| **Workflow** | "Connect to Power Automate" | Business process automation and approvals |
| **Marketing** | "Integrate with Marketo" | Lead management and marketing automation |

**Advanced integration examples:**

```
👤 You: "Send form submissions to hr@company.com and create a case in our CRM system"
🤖 AI: "Configured email submission and CRM integration"

👤 You: "Submit data to our REST API endpoint and trigger the new customer workflow"
🤖 AI: "Set up REST API submission with workflow triggers"

👤 You: "Email responses to the sales team and add the lead to our marketing automation platform"
🤖 AI: "Configured multi-channel submission with email and marketing automation"
```





## Advanced Form Operations


### Complex Rule Creation

Create sophisticated validation and business logic that responds to user interactions and ensures data integrity:

```
👤 You: "Show the address section only if the user selects 'Ship to different address'"
🤖 AI: "Created a conditional rule that shows/hides the address panel based on checkbox selection"
```

### Multi-Step Form Creation

```
👤 You: "Create a progressive form with 3 steps: personal info, preferences, confirmation"
🤖 AI: "Created a progressive form with navigation between steps and validation at each stage"
```

### Advanced Field Types

* File upload with validation and size restrictions for document management
* Date pickers with constraints and business rules for scheduling
* Dropdowns with dynamic options that change based on user selections
* Radio buttons with conditional logic for complex decision trees


### PDF to Form Conversion

```
👤 You: "Convert this PDF into an interactive form"
🤖 AI: "Analyzed the PDF and created a form with appropriate field types and validation"
```

### URL to Form Conversion

```
👤 You: "Create a form from this website"
🤖 AI: "Extracted form elements and created a native AEM Form with enhanced functionality"
```

### Performance Analysis

```
👤 You: "Analyze this form's conversion performance"
🤖 AI: "Provided insights on form effectiveness and suggested optimizations"
```

### Advanced Customization

#### Custom Validation Rules

* Field dependencies that create dynamic form behavior based on user inputs
* Complex conditional logic that adapts the form experience to user needs
* Custom error messages that provide clear guidance to users
* Cross-field validation that ensures data consistency across multiple inputs

#### Layout Optimization

* Mobile responsiveness that ensures forms work seamlessly on all devices
* Accessibility compliance that makes forms usable by people with disabilities
* Visual design improvements that enhance user engagement and completion rates
* User experience enhancements that reduce friction and improve satisfaction

#### Integration Workflows

* Multi-step approval processes that route form submissions through business workflows
* Data transformation that converts form data into formats required by external systems
* Custom business logic that applies specific rules and calculations to form submissions
* Advanced error handling that provides graceful recovery from system issues

## Command Reference

### Essential Commands

| Symbol | Purpose | How to Use |
|--------|---------|------------|
| `/` | Quick actions and shortcuts | Type `/create` for form creation, `/help` for assistance |
| `@` | Reference existing form fields | Type `@fieldName` to modify specific fields (e.g., `@email`) |
| Plain text | Natural conversation | Describe what you want: "Add a required phone number field" |

### Slash Commands

| Command | Context | Example Usage |
|---------|---------|---------------|
| `/create-form` | All environments | `/create-form customer survey` |
| `/add-form` | Universal Editor | `/add-form contact form` |
| `/update-layout` | Form Editor | `/update-layout wizard with 3 steps` |
| `/update-field` | Form Editor | `/update-field @email to be required` |
| `/create-rule` | Form Editor | `/create-rule show @spouse if married` |
| `/create-panel` | Form Editor | `/create-panel Personal Information` |
| `/configure-submit` | Form Editor | `/configure-submit to email support` |
| `/help` | All environments | `/help multi-step forms` |

### Field References

Use `@fieldName` to reference existing fields:

* `@firstName`, `@lastName` * Name fields
* `@email`, `@phoneNumber` * Contact fields  
* `@address`, `@city`, `@zipCode` * Address fields
* `@dateOfBirth`, `@startDate` * Date fields

### Component Types

Use these terms when describing form elements:

* `text input` * Single line text field
* `text area` * Multi-line text field
* `dropdown` * Select list with options
* `checkbox` * Single checkbox
* `checkbox group` * Multiple checkboxes
* `radio group` * Radio button group
* `date picker` * Date selection field
* `file upload` * File attachment field
* `panel` * Container for grouping fields

### Integration Commands

| Service | Natural Language Command | Requirements |
|---------|--------------------------|--------------|
| Email | "Send submissions to [email]" | Valid email address |
| REST API | "Submit to REST endpoint [URL]" | API endpoint and credentials |
| Azure Storage | "Save files to Azure storage" | Storage account configuration |
| SharePoint | "Store in SharePoint [site]" | SharePoint site access |
| Power Automate | "Trigger Power Automate flow" | Flow configuration |
| Marketo | "Add leads to Marketo" | Marketo API credentials |

### Tips

1. **Use natural language**: The AI understands complex requests and can interpret detailed requirements
2. **Be specific**: Detailed descriptions yield better results and more accurate form generation
3. **Iterate**: Refine forms through conversation to achieve the perfect user experience
4. **Leverage context**: Reference existing form elements to build upon what you already have
5. **Test thoroughly**: Validate all user scenarios to ensure forms work as expected

## Product Help and Learning

The Forms Experience Builder can also teach you about AEM Forms features:

### Ask Questions Like:

* "How do I create a multi-step form?"
* "What's the difference between panels and sections?"
* "How do I set up email notifications?"
* "What are the best practices for mobile-friendly forms?"
* "How do I apply themes to my forms?"

### Get Help On:

* AEM Forms concepts and terminology
* Step-by-step instructions for complex features
* Best practices and recommendations
* Troubleshooting common issues

## Best Practices

### Form Design

* **Keep it simple**: Start with essential fields and add complexity only when necessary to avoid overwhelming users
* **Use clear labels**: Make field purposes obvious with descriptive labels that guide users through the form
* **Provide help text**: Guide users through complex fields with contextual help and examples
* **Test thoroughly**: Validate all user paths to ensure forms work correctly in all scenarios

### User Experience

* **Progressive disclosure**: Show relevant fields based on context to reduce cognitive load and improve completion rates
* **Clear navigation**: Help users understand where they are in the form and what steps remain
* **Responsive design**: Ensure forms work on all devices and screen sizes for maximum accessibility
* **Accessibility**: Follow WCAG guidelines to make forms usable by people with disabilities

### Performance

* **Optimize field count**: Only ask for necessary information to reduce form abandonment and improve completion rates
* **Use appropriate validation**: Prevent errors before submission to provide immediate feedback and guidance
* **Test completion rates**: Monitor and improve form effectiveness through analytics and user feedback
* **Regular updates**: Keep forms current with business needs and user expectations for optimal performance

### Brand Consistency

* **Create brand templates**: Prepare branded form templates with your organization's colors, fonts, and styling before starting form creation
* **Define style standards**: Establish consistent button styles, field layouts, and spacing guidelines that can be referenced in prompts
* **Use brand assets**: Prepare logos, color codes, and brand guidelines for easy reference when creating forms
* **Template library**: Build a collection of branded form templates for common use cases (contact, registration, feedback)
* **Style prompts**: Include brand-specific instructions: "Use company blue (#1234AB) for buttons and corporate font Helvetica"

### Tips for Best Results

**Start Simple, Build Up**

* Begin with basic requests: "Create a contact form"
* Add details gradually: "Add validation to the email field"
* Test and refine: "Make the phone field optional"

**Be Specific When Needed**

* Instead of: "Make it look good"
* Try: "Use professional colors and clean typography"

**Use Natural Language**

* Instead of: "Add text input component"
* Try: "Add a field for first name"

**Reference Existing Elements**

* Use `@fieldName` for existing fields: "Make @email required"
* Be specific about field names: "Update the @phoneNumber field"

**Break Down Complex Requests**

* Instead of one large request, try multiple smaller ones
* Build your form step by step
* Test each change before moving to the next

## Troubleshooting

| Issue | Quick Fix |
|-------|-----------|
| **Interface not loading** | Refresh browser, check internet connection |
| **Commands not working** | Try `/help` or use natural language instead |
| **@fieldName not recognized** | Check spelling, ensure field exists first |
| **File upload fails** | Use PDF/JPG/PNG under 10MB |
| **Form looks wrong** | Be more specific: "Make it mobile-friendly" |
| **Integration fails** | Verify API credentials and permissions |

**Still need help?** Type `/help` followed by your specific question or contact your system administrator.

For additional support, refer to the main [Forms Experience Builder Prompt Library](/help/edge/docs/forms/ai-assistant-prompt-library.md) or contact your system administrator for technical assistance.
