---
title: Getting started with Forms Experience Builder
description: Learn the basics of creating your first AI-powered form with Forms Experience Builder. Step-by-step tutorial with examples and best practices.
hide: yes
index: no
hidefromtoc: yes
role: Admin, Developer
exl-id: c4f838bc-a001-48e7-afaa-c2ff9034f5d4
---
# Getting started with Forms Experience Builder {#getting-started-forms-experience-builder}

Forms Experience Builder revolutionizes form creation by leveraging AI to transform natural language descriptions into fully functional digital forms. This guide will help you create your first form and understand the core concepts that make Forms Experience Builder powerful.

## What is Forms Experience Builder? {#what-is-forms-experience-builder}

Forms Experience Builder is an AI-powered form creation tool that allows you to build sophisticated digital forms using conversational language. Instead of traditional drag-and-drop interfaces or complex coding, you simply describe what you want, and the AI creates the form for you.

**Key capabilities:**

* **Natural language form creation** - Describe your form requirements in plain English

* **Intelligent import and conversion** - Transform existing documents into interactive forms

* **Smart field generation** - AI-powered fields with pre-populated options

* **Business logic automation** - Create conditional rules and validation through conversation

* **System integration** - Connect forms to your existing business workflows

## Prerequisites {#prerequisites-getting-started}

Before you begin, ensure you have:

* **Access to Forms Experience Builder** - Available through the Early Access Program
* **AEM Forms as a Cloud Service** - Production author environment with Adaptive Forms Core Components
* **Basic understanding** - Familiarity with form concepts and business requirements

For detailed technical setup requirements and environment configuration, see [Deploy and configure Forms Experience Builder](deploy-forms-experience-builder.md).

## Ways to create forms {#two-ways-to-create-forms}

After you use the Forms Wizard to select a [Core Components template](/help/forms/creating-adaptive-form-core-components.md) or [Edge Delivery Services](/help/edge/docs/forms/universal-editor/create-forms.md) template, theme, and other options, the Forms Experience Builder offers two primary approaches for form creation:

### 1. Create from scratch {#create-from-scratch}

Build forms using natural language descriptions of your requirements.

**When to use:**

* Building new forms from requirements

* Creating forms for new business processes

* When you have clear specifications but no existing documents

**Example:**

    Create a customer feedback form with:
    - Product rating (1-5 stars)
    - Comment field for detailed feedback
    - Customer email (optional)
    - Submit to email notification

>[!VIDEO](https://video.tv.adobe.com/v/3473104)



### 2. Import and convert {#import-and-convert}

Transform existing documents into interactive digital forms.

Before using this option, upload your PDF file or an image of the form. The PDF can be either an AcroForm or an XFA-based PDF form. For [other types of PDF forms](https://experienceleague.adobe.com/en/docs/experience-manager-learn/forms/document-services/pdf-forms-and-documents), use the [Prepare Form](https://helpx.adobe.com/in/acrobat/using/creating-distributing-pdf-forms.html) option in Adobe Acrobat to convert them into an AcroForm

**When to use:**

* Converting existing PDF forms

* Modernizing paper-based processes

* When you have existing form designs to enhance

**Example:**

    /create-form convert the attached PDF file to an adaptive form

>[!VIDEO](https://video.tv.adobe.com/v/3474042)


## Your first form: Step-by-step tutorial {#first-form-tutorial}

Let's create a simple contact form to understand the basic workflow.

### Step 1: Start with a simple description {#step-1-simple-description}

Begin with a basic form description:

    Create a basic contact form with name, email, and message fields

This creates a form with three essential fields.

![Form with three essential field - created using natural language prompt](/help/forms/assets/forms-experience-builder-contact-us-form.png)

### Step 2: Add validation and requirements {#step-2-add-validation}

Enhance the form with validation rules:

    Make @name and @email mandatory fields with appropriate validation

The `@` symbol references specific fields for targeted modifications.

![Added validation in form experience builder using natural language prompt](/help/forms/assets/forms-experience-builder-contact-us-form-add-validation.png)


### Step 3: Improve user experience {#step-3-improve-ux}

Add helpful placeholder text and guidance:

    Add placeholder text: @name "Your full name", @email "your.email@company.com", @message "Tell us how we can help"

![Added validatiom using natural language prompts in forms experience builder](/help/forms/assets/forms-experience-builder-contact-us-form-add-placeholder.png)

### Step 4: Add advanced features {#step-4-advanced-features}

Include additional functionality:

    Add two dropdowns

    - inquiryType with options: "General Question", "Support Request", "Sales Inquiry", "Partnership"

    - urgencyLevel with options (Low, Medium, High)
    

![Added a dropdown components using natural language prompts in forms experience builder](/help/forms/assets/forms-experience-builder-contact-us-form-add-dropdown.png)


### Step 5: Implement conditional logic {#step-5-conditional-logic}

Create smart, context-aware behavior by adding rules such as:

    Hide the @urgencyLevel dropdown on form load
    Show @urgencyLevel dropdown (Low, Medium, High) only when @inquiryType equals "Support Request"

These are two separate rules: one hides the urgency level dropdown when the form loads, and the other shows it only when the inquiry type is "Support Request." You need to create each rule with a separate prompt—only one rule can be created at a time.

## Understanding the AI conversation approach {#ai-conversation-approach}

Forms Experience Builder uses a conversational interface where you can:

### Reference fields with @ symbols {#reference-fields}

Use `@fieldName` to reference specific fields:

    Make @email a required field
    Add validation to @phoneNumber for US format
    Change @submitButton text to "Send Message"

>[!VIDEO](https://video.tv.adobe.com/v/3474043)


### Use natural language commands {#natural-language-commands}

Describe what you want in plain English:  

    - Add a section for company information
    - Create a dropdown for department selection
    - Include a file upload for resume
    - Set up email notifications when form is submitted

### Build incrementally {#build-incrementally}

Start simple and add complexity gradually:

1. **Basic structure** - Create the essential fields first
2. **Add validation** - Implement required fields and format validation
3. **Enhance UX** - Add placeholders, help text, and styling
4. **Implement logic** - Add conditional rules and business logic
5. **Configure submission** - Set up form processing and notifications


## Common form patterns {#common-form-patterns}

### Contact and feedback forms {#contact-feedback-forms}

**Basic contact form:**

    Create a contact form with:
    - Name (required)
    - Email (required, validated)
    - Subject dropdown (General, Support, Sales, Partnership)
    - Message (required, multi-line)
    - Submit button

**Customer feedback form:**

    Create a customer feedback form with:
    - Product rating (1-5 stars)
    - Comment field for detailed feedback
    - Customer email (optional)
    - Submit to email notification

### Registration and onboarding forms {#registration-onboarding-forms}

**User registration:**

    Create a user registration form with:
    - Personal information (name, email, phone)
    - Account preferences (newsletter, notifications)
    - Terms and conditions acceptance
    - Password creation with strength validation

**Employee onboarding:**

    Create an employee onboarding form with:
    - Personal details and contact information
    - Employment information and start date
    - Document uploads (resume, ID, tax forms)
    - Benefits selection and preferences

### Survey and assessment forms {#survey-assessment-forms}

**Customer satisfaction survey:**

    Create a customer satisfaction survey with:
    - Overall rating (1-10 scale)
    - Category ratings (product, service, support)
    - Open-ended feedback sections
    - Demographic information (optional)

**Skills assessment:**

    Create a skills assessment form with:
    - Skill categories with proficiency levels
    - Experience duration for each skill
    - Certification and training information
    - Self-assessment and goals

## Testing and validation {#testing-validation}

### Always test your forms {#always-test-forms}

Before deploying any form:

1. **Test all fields** - Ensure validation works correctly

2. **Verify conditional logic** - Check that rules trigger properly

3. **Test submission** - Confirm data is processed correctly

4. **Validate on different devices** - Ensure mobile compatibility

5. **Review with stakeholders** - Get feedback from end users

### Common validation patterns {#validation-patterns}

**Email validation:**

    Add email format validation to @email field

**Phone number validation:**

    Add US phone number format validation to @phoneNumber

**Age validation:**

    Add age validation: must be 18 or older for @dateOfBirth

**File upload validation:**

    Add file type validation: only PDF, DOC, DOCX allowed for @resume
    Add file size limit: maximum 5MB for @resume

## Next steps {#next-steps}

Now that you understand the basics, explore these advanced topics:

* **[LLM-enhanced smart fields](forms-experience-builder-llm-smart-fields.md)** - Create fields with pre-populated options using AI knowledge
* **[AI-powered form creation](forms-experience-builder-prompt-examples-library.md)** - Advanced prompt patterns and examples
* **[Intelligent import and conversion](intelligent-import-conversion.md)** - Transform existing documents into forms
* **[Form submission and integration](form-submission-integration.md)** - Connect forms to your business systems


## Related articles

* [Forms Experience Builder Overview](product-overview.md)
* [LLM-enhanced smart fields](forms-experience-builder-llm-smart-fields.md)
* [AI-powered form creation](forms-experience-builder-prompt-examples-library.md)
* [Intelligent import and conversion](intelligent-import-conversion.md)
* [Form submission and integration](form-submission-integration.md)
* [Frequently asked questions](forms-experience-builder-frequently-asked-questions.md)
