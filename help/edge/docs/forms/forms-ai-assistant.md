---
title: AI Assistant for AEM Forms (Forms Experience Builder)
description: Craft powerful forms faster using Form Fragments
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Developer
---

# Getting started with AI Assistant for AEM Forms (Forms Experience Builder)

>[!NOTE]
>
>
> The AI Assistant for AEM Forms (Forms Experience Builder) capability is available under the **early-adopter program**. If you are interested, send a quick email from your work address to mailto:aem-forms-ea@adobe.com to request access to the capability.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This documentation is currently being tested against the product and is subject to updates and revisions. Features, commands, and examples may change as the AI Assistant for AEM Forms continues to evolve during the early-adopter program.

The AI Assistant for AEM Forms transforms how you create forms—simply describe what you need in natural language, and watch your forms come to life. Available in Forms Management UI, the Adaptive Forms Editor, and the Universal Editor, it understands your intent and builds exactly what you're looking for.

## Getting Started: Just Talk to It

The AI Assistant works like having a conversation with a knowledgeable colleague. Instead of learning complex menus and settings, you simply describe what you want to create.

### Quick Start

Get up and running quickly by watching our introductory video:

>[!VIDEO](https://video.tv.adobe.com/v/3463164/)

### Accessing the AI Assistant

You can access the AI Assistant from three different locations in AEM Forms:

1. **Forms Management UI**
   - Navigate to: Adobe Experience Manager > Forms > Forms & Documents
   - Look for the AI Assistant icon on the left side of the interface
   - Click the icon to open the AI Assistant panel
   
    ![AI Assistant icon*](/help/edge/docs/forms/assets/forms-manager.gif){width="50%"} 

2. **Adaptive Forms Editor**
   - Navigate to: Adobe Experience Manager > Forms > Forms & Documents
   - Select and open a form for editing
   - Click the AI Assistant icon in the editor interface
   
    ![AI Assistant icon*](/help/edge/docs/forms/assets/adaptive-forms-editor.gif){width="75%"} 

3. **Universal Editor**
 
    - Navigate to: Adobe Experience Manager > Forms > Forms & Documents
    - Look for the AI Assistant icon on the left side of the interface
    - Click the AI Assistant icon in the editor interface

### How to Start: Simple Conversations

The best way to begin with the AI Assistant is through natural language. Here's how:

**Just describe what you need:**

- "Create a contact form for my website"
- "I need a customer feedback form with rating scales"
- "Build a registration form for my upcoming event"
- "Make a simple survey about product satisfaction"

**Add details as you go:**

- "Create a contact form with name, email, phone, and message fields"
- "I need a multi-step registration form for a conference"
- "Build a customer feedback form with 5-star ratings and comment sections"

**Reference your existing fields:**

- "Make the email field required" (for @email)
- "Add validation to the phone number field" (for @phoneNumber)
- "Show the spouse information only if married is selected" (for @spouseInfo and @maritalStatus)

### What You Can Also Do

Beyond natural language, the AI Assistant offers additional ways to interact:

- **Upload files**: Attach images, PDFs, or Figma designs to show the AI what you're envisioning
- **Use quick commands**: Type `/` to see available shortcuts for common actions
- **Reference specific fields**: Use `@fieldName` to modify existing form fields (e.g., `@firstName`, `@emailAddress`)

## What You Can Create: Examples That Work

Here are real examples of what you can accomplish with simple, natural language:

### Starting a New Form

**Simple approach:**

```
"Create a contact form"
```

**More detailed approach:**

```
"Create a professional contact form for a law firm with fields for name, email, phone, case type, and message. Make it mobile-friendly."
```

**With design reference:**

```
"Create a contact form based on the attached design mockup. Include all the fields shown in the layout."
```

### Adding Form Elements

**Basic additions:**

```
"Add a section for personal information"
"Include a file upload for resume"
"Add a dropdown for country selection"
```

**Detailed specifications:**

```
"Add a personal information panel with fields for full name, date of birth, phone number, and email address"
"Include a secure file upload component for documents, limited to PDF files under 5MB"
"Add a country dropdown with options for USA, Canada, UK, and Germany"
```

### Creating Dynamic Behavior

**Simple logic:**

```
"Show additional fields when 'Other' is selected"
"Make the email field required"
"Calculate the total automatically"
```

**Complex business rules:**

```
"Show the spouse information fields only when marital status is set to 'Married'"
"Calculate the total cost by multiplying quantity and price, then add 10% tax"
"Enable the submit button only when all required fields are completed and terms are accepted"
```

### Form Layout and Design

**Layout changes:**

```
"Make this a multi-step form"
"Organize fields in two columns"
"Convert to an accordion layout"
```

**Design improvements:**

```
"Create a wizard-style form with 3 steps: personal info, preferences, and review"
"Arrange the address fields in a compact two-column layout"
"Update the layout to match the attached wireframe"
```

### Submission and Integration

**Basic submission:**

```
"Send form data to our email"
"Save responses to a spreadsheet"
"Redirect to a thank you page"
```

**Advanced integration:**

```
"Send form submissions to hr@company.com and create a case in our CRM system"
"Submit data to our REST API endpoint and trigger the new customer workflow"
"Email responses to the sales team and add the lead to our marketing automation platform"
```

## Working with Attachments

Upload files to help the AI understand exactly what you're looking for:

### Supported File Types

| File Type | Best For | Example Use |
|-----------|----------|-------------|
| **Images** (PNG, JPG, GIF) | Form layouts, UI mockups, paper form scans | "Create a form matching this layout" |
| **PDF Files** | Existing forms to convert, specifications | "Convert this PDF form to digital" |
| **Figma Files** | Design prototypes, brand guidelines | "Build this form from my Figma design" |
| **Design Files** | Visual references, style guides | "Match the styling in this design" |

### How to Use Attachments

1. **Click the attachment icon** in the AI Assistant interface
2. **Select your file** from your device
3. **Describe what you want** referencing the attached file:
   - "Create a form based on this attached PDF"
   - "Build a contact form matching the layout in this image"
   - "Convert this paper form to a digital version"

### Best Practices with Attachments

- **Use clear, high-quality images** for better AI analysis
- **Focus on one concept per attachment** (layout, styling, etc.)
- **Describe what you want** along with the attachment
- **Keep files under 10MB** for optimal processing

## Tips for Best Results

### Start Simple, Build Up

- Begin with basic requests: "Create a contact form"
- Add details gradually: "Add validation to the email field"
- Test and refine: "Make the phone field optional"

### Be Specific When Needed

- Instead of: "Make it look good"
- Try: "Use professional colors and clean typography"

### Use Natural Language

- Instead of: "Add text input component"
- Try: "Add a field for first name"

### Reference Existing Elements

- Use `@fieldName` for existing fields: "Make @email required"
- Be specific about field names: "Update the @phoneNumber field"

### Break Down Complex Requests

- Instead of one large request, try multiple smaller ones
- Build your form step by step
- Test each change before moving to the next

## Product Help and Learning

The AI Assistant can also teach you about AEM Forms features:

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

## Advanced Features Reference

For users who want to explore advanced capabilities:

### Quick Commands

Type `/` to see available shortcuts:

| Command | Purpose | Example |
|---------|---------|---------|
| `/create-form` | Start a new form | `/create-form customer survey` |
| `/add-form` | Add form in Universal Editor | `/add-form contact form` |
| `/update-layout` | Change form structure | `/update-layout wizard with 3 steps` |
| `/update-field` | Modify field properties | `/update-field @email to be required` |
| `/create-rule` | Add dynamic behavior | `/create-rule show @spouse if married` |
| `/create-panel` | Add field containers | `/create-panel Personal Information` |
| `/configure-submit` | Set up form submission | `/configure-submit to email support` |
| `/help` | Get assistance | `/help multi-step forms` |

### Field Reference Syntax

Use `@fieldName` to reference existing fields:

- `@firstName` - First name field
- `@email` - Email field  
- `@phoneNumber` - Phone number field
- `@dateOfBirth` - Date of birth field

### Component Types

Use these terms for best results:

- `text input` - Single line text field
- `text area` - Multi-line text field
- `dropdown` - Select list
- `checkbox` - Single checkbox
- `checkbox group` - Multiple checkboxes
- `radio group` - Radio button group
- `date picker` - Date selection
- `file upload` - File attachment
- `panel` - Container for grouping fields

## Troubleshooting

### Common Issues and Solutions

**AI Assistant Not Responding:**

- Check your internet connection
- Ensure you're in a supported environment
- Close and reopen the AI Assistant panel

**Unexpected Results:**

- Try rephrasing your request more specifically
- Break complex requests into smaller steps
- Use standard AEM Forms terminology

**Field References Not Working:**

- Check field names are spelled exactly as they appear
- Use `@fieldName` syntax for existing fields
- Ensure the field exists before referencing it

**Design Import Issues:**

- Verify files are clear and well-structured
- Use supported formats (PDF, PNG, JPG, Figma)
- Ensure file size is under 10MB

## Feedback and Support

Help us improve the AI Assistant:

- **Provide Feedback**: Use the feedback button in the AI Assistant interface
- **Report Issues**: Contact Adobe support through official channels
- **Share Experiences**: Your input helps make the assistant better for everyone

## Related Resources

[AEM Forms AI Assistant - Prompt Library](/help/forms/experience-builder/forms-experience-builder-prompt-examples-library.md)
