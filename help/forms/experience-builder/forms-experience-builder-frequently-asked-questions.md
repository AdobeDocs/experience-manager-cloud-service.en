---
title: Forms Experience Builder - Frequently asked questions
description: Find answers to common questions about Forms Experience Builder, including setup, usage, troubleshooting, and best practices.
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Developer
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: f43c2586-9075-47dc-aa45-5ed2d2979b6d
---
# Forms Experience Builder - Frequently asked questions

>[!NOTE]
>
> The Forms Experience Builder is available under an early access program. Before you begin, please ensure you have requested and been granted access.

This FAQ addresses the most common questions about Forms Experience Builder, from basic setup to advanced features and troubleshooting.

## General questions

### What is Forms Experience Builder?

Forms Experience Builder is an AI-powered form creation tool that allows you to build sophisticated digital forms using conversational language. Instead of traditional drag-and-drop interfaces or complex coding, you simply describe what you want, and the AI creates the form for you.

### Who can use Forms Experience Builder?

Forms Experience Builder is designed for:

- **Form creators** who want to build forms quickly and efficiently
- **Business users** who need to create forms without technical expertise
- **Developers** who want to leverage AI for rapid form prototyping
- **Administrators** who need to configure and manage form creation workflows

### Is Forms Experience Builder available for all AEM Forms customers?

Forms Experience Builder is currently available through an Early Access Program. Contact your Adobe representative to request access and learn about availability for your organization.

## Setup and configuration

### What are the prerequisites for using Forms Experience Builder?

Before using Forms Experience Builder, ensure you have:

- Access to Forms Experience Builder through the Early Access Program
- AEM Forms as a Cloud Service with Adaptive Forms Core Components
- Basic understanding of form concepts and business requirements

For detailed technical setup requirements, see [Deploy and configure Forms Experience Builder](deploy-forms-experience-builder.md).

### How do I enable Forms Experience Builder in my environment?

Forms Experience Builder setup depends on your AEM Forms implementation:

**For Edge Delivery Services:**

- Prepare your project for Edge Delivery Services Forms
- Enable the Forms Experience Builder in the Universal Editor

**For Core Components-based forms:**

- Ensure Adaptive Forms Core Components are enabled
- Configure the Forms Experience Builder in the Adaptive Forms Editor

### Can I use Forms Experience Builder with existing forms?

Yes, Forms Experience Builder can work with existing forms in several ways:

- Import and convert existing PDF forms
- Enhance existing adaptive forms with AI-powered features
- Add intelligent fields to current form structures

## Creating forms

### How do I create my first form?

Start with a simple description of what you want:

    Create a contact form with name, email, and message fields

The AI will generate the basic form structure, which you can then enhance with additional features, validation, and styling.

### What types of forms can I create?

Forms Experience Builder supports various form types:

- Contact and feedback forms
- Registration and onboarding forms
- Survey and assessment forms
- Multi-step forms with conditional logic
- Forms with file uploads and complex validation

### Can I create multi-step forms?

Yes, you can create multi-step forms using natural language:

    Create a progressive form with 3 steps: personal info, preferences, confirmation

The AI will automatically set up the form structure with navigation between steps.

### How do I add validation to form fields?

Add validation using natural language commands:

    Make @email a required field with email format validation
    Add US phone number format validation to @phoneNumber
    Set age validation: must be 18 or older for @dateOfBirth

## Advanced features

### What are LLM-enhanced smart fields?

LLM-enhanced smart fields are intelligent form fields that come pre-populated with relevant options from AI knowledge bases. For example:

- Country dropdowns with all world countries
- Industry classifications with standard codes
- Geographic data with states, cities, and postal codes

### How do I import existing documents into forms?

You can import various document types:

- **PDF forms**: Upload static or interactive PDFs
- **Images**: Upload photos of paper forms or screenshots
- **Design files**: Import Figma designs or other design formats

Use the attachment icon in Forms Experience Builder to upload your document and describe your conversion requirements.

### Can I integrate forms with external systems?

Yes, Forms Experience Builder supports various integration options:

- Email submissions with custom templates
- REST API integration with external services
- Cloud storage integration (Azure, AWS, Google Cloud)
- Workflow integration (Power Automate, AEM Workflow)

## Troubleshooting

### The AI doesn't understand my request. What should I do?

Try these approaches:

- Be more specific in your description
- Break complex requests into smaller steps
- Use field references (@fieldName) for targeted changes
- Provide clear examples of what you want

### My form validation isn't working. How do I fix it?

Check these common issues:

- Verify field names match exactly (case-sensitive)
- Ensure validation syntax is correct
- Test validation rules individually
- Review error messages for specific issues

### Conditional logic isn't triggering properly. What's wrong?

Troubleshoot conditional logic by:

- Ensuring field names are referenced correctly
- Checking rule syntax and conditions
- Testing with different input combinations
- Verifying field types match rule requirements

### The interface isn't loading. What should I do?

Try these solutions:

- Refresh your browser and clear cache
- Check your internet connection
- Verify you have proper access permissions
- Contact your system administrator if issues persist

## Best practices

### How can I create better forms with Forms Experience Builder?

Follow these best practices:

- **Be specific**: Provide detailed descriptions of what you want
- **Start simple**: Begin with basic structure and add complexity gradually
- **Test thoroughly**: Validate all form functionality before deployment
- **Use incremental development**: Build forms step-by-step

### What should I avoid when creating forms?

Avoid these common mistakes:

- Being too vague in your descriptions
- Trying to create everything at once
- Skipping testing and validation
- Not considering mobile responsiveness

### How do I ensure my forms are accessible?

Forms Experience Builder includes accessibility features:

- Automatic WCAG compliance checking
- Screen reader compatibility
- Keyboard navigation support
- High contrast mode options

## Integration and deployment

### How do I deploy forms created with Forms Experience Builder?

Forms created with Forms Experience Builder follow standard AEM Forms deployment processes:

- Publish forms through AEM author environment
- Configure form submission endpoints
- Set up form processing workflows
- Test forms in production environment

### Can I customize the AI responses and behavior?

Yes, you can configure various aspects:

- Response style (concise, detailed, balanced)
- Language preferences and terminology
- Interface customization options
- Accessibility settings

### How do I get help with Forms Experience Builder?

For additional support:

- Check the [Getting Started guide](forms-experience-builder-getting-started.md)
- Review the [Deploy and configure guide](deploy-forms-experience-builder.md)
- Contact your system administrator
- Reach out to Adobe support for technical issues

## Related articles

- [Forms Experience Builder Overview](product-overview.md)
- [Getting started with Forms Experience Builder](forms-experience-builder-getting-started.md)
- [Deploy and configure Forms Experience Builder](deploy-forms-experience-builder.md)
- [LLM-enhanced smart fields](forms-experience-builder-llm-smart-fields.md)
- [Intelligent import and conversion](intelligent-import-conversion.md)
- [Form submission and integration](form-submission-integration.md)
