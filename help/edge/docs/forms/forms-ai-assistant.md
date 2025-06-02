---
title: AI Assistant for AEM Forms (Forms Experience Builder)
description: Craft powerful forms faster using Form Fragments
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
role: Admin, Architect, Developer
---
# AI Assistant for AEM Forms (Forms Experience Builder)

>[!NOTE]
>
>
> The AI Assistant for AEM Forms (Forms Experience Builder) capability is available under the early-adopter program. If you are interested, send a quick email from your work address to mailto:aem-forms-ea@adobe.com to request access to the capability.


The AI Assistant for AEM Forms (Forms Experience Builder) enhances your authoring experience by streamlining common form-building tasks through natural language prompts. Available in Forms Manager, the Adaptive Forms Editor, and the Universal Editor, it empowers you to build smarter and faster by supporting both creation and configuration actions. This guide will help you get started and make the most of its capabilities.

## Getting Started

Before you dive deep, let's cover the basics of accessing and interacting with the AI Assistant.

### Accessing the AI Assistant

You can access the AI Assistant from three different locations in AEM Forms:

1. **Forms Manager**
   - Navigate to: Adobe Experience Manager > Forms > Forms & Documents
   - Look for the AI Assistant icon on the left side of the interface
   - Click the icon to open the AI Assistant panel
   
    ![AI Assistant icon*](/help/edge/docs/forms/assets/forms-manager.gif)

2. **Adaptive Forms Editor**
   - Navigate to: Adobe Experience Manager > Forms > Forms & Documents
   - Select and open a form for editing
   - Click the AI Assistant icon in the editor interface
   
    ![AI Assistant icon*](/help/edge/docs/forms/assets/adaptive-forms-editor.gif)

3. **Universal Editor**
 
    - Navigate to: Adobe Experience Manager > Forms > Forms & Documents
    - Look for the AI Assistant icon on the left side of the interface
    - Click the AI Assistant icon in the editor interface

The AI Assistant adapts its functionality based on your current location and task, providing relevant assistance for each context.

### How to Interact:

- Simply type your request in natural language.
- Use `/` to view a list of available commands or quick actions.
- Reference specific form fields using `@fieldName` (e.g., `@firstName`, `@emailAddress`) when you want the assistant to configure or update that particular field.


### Quick Start

Get up and running quickly by watching our introductory video:

>[!VIDEO](https://video.tv.adobe.com/v/3463164/)


This video covers launching the assistant in all environments, basic interaction, and an overview of its capabilities.

## AI Assistant Command Reference

| Command | Description | Purpose | Usage Context | Examples | Key Features |
|---------|-------------|---------|---------------|----------|--------------|
| /create-form | Start a new form in Forms Manager or Forms Editor | Initiates creation of a completely new form from scratch | Forms Manager, Adaptive Forms Editor | /create-form customer feedback survey | Provides options for forms structure and creates the form |
| /add-form | Add a new form in Universal Editor | Adds a new form block or component within Universal Editor | Universal Editor for Edge Delivery Services | /add-form contact form with name and email | Inserts form blocks, works with block-based editing |
| /update-layout | Change layout of form to accordion, tab-based, wizard, or single page responsive design | Modifies overall structural layout and navigation pattern | All editing environments | /update-layout wizard with 3 steps | Accordion, tabs, wizard, single-page responsive options |
| /update-field | Modify properties and configuration of existing form fields | Changes field attributes like labels, validation, formatting, behavior | All editing environments | /update-field @email to be required with validation | Labels, validation rules, field types, defaults, visibility |
| /create-rule | Create dynamic behavior and conditional logic for forms | Implements business logic, calculations, conditional interactions | All editing environments | /create-rule show @spouseName if @maritalStatus equals "Married" | Conditional visibility, calculations, validation, value setting |
| /create-panel | Create a new panel (container for grouping related fields) | Adds structural containers to organize form fields logically | All editing environments | /create-panel Personal Information with name, email, phone | Field grouping, titles, layout options, collapsible sections |
| /add-panel | Convert an image to form panel in Universal Editor | Uses AI to analyze uploaded images and convert to structured form panels | Universal Editor | /add-panel from uploaded form image | Image recognition, visual-to-functional conversion, layout preservation |
| /configure-submit | Set up form submission actions and data handling | Defines what happens when users submit the completed form | All editing environments | /configure-submit to send email to `support@company.com` | Email, REST API, workflows, spreadsheets, databases, Power Automate |
| /help | Access assistance and documentation within the AI Assistant | Provides contextual help, guidance, and answers about AEM Forms | All editing environments | /help how do I create multi-step forms? | Feature explanations, guides, best practices, troubleshooting |

### Command Categories

| Category | Commands | Primary Use Cases |
|----------|----------|-------------------|
| Form Creation | /create-form, /add-form | Starting new forms, adding form blocks |
| Structure & Layout | /update-layout, /create-panel, /add-panel | Organizing form structure, visual design |
| Field Management | /update-field | Configuring individual form elements |
| Logic & Rules | /create-rule | Adding dynamic behavior and validation |
| Submission | /configure-submit | Setting up data handling and workflows |
| Support | /help | Getting assistance and documentation |

### Syntax Guidelines

| Element | Format | Example | Notes |
|---------|--------|---------|-------|
| Commands | /command-name | /create-form | Always start with forward slash |
| Field References | @fieldName | @email, @firstName | Use @ symbol for existing fields |
| Natural Language | Command + description | /create-rule show field if condition | Combine commands with descriptive text |
| Multiple Actions | Separate commands | /create-panel then /update-layout | Apply one command at a time |


### Environment-Specific Features

| Environment | Available Commands | Special Features |
|-------------|-------------------|------------------|
| Forms Manager | /create-form, /help | Form-level creation and management |
| Adaptive Forms Editor and  Universal Editor | All commands | Full feature set, detailed configuration |



### Field Reference Syntax (Contextual elements)

Use `@fieldName` to reference existing fields:

- `@firstName` - First name field
- `@email` - Email field
- `@phoneNumber` - Phone number field
- `@dateOfBirth` - Date of birth field

### Component Types

This list covers common component types. The AI may recognize variations or more specialized types, but using these precise terms yields the best results:

- `text input` - Single line text field
- `text area` - Multi-line text field
- `dropdown` - Select list
- `checkbox` - Single checkbox
- `checkbox group` - Multiple checkboxes
- `radio group` - Radio button group
- `date picker` - Date selection
- `file upload` - File attachment
- `panel` - Container for grouping fields


## Core Capabilities & Expanded Prompt Examples

The AI Assistant understands a wide range of commands. Here are some examples to illustrate its power. Remember to use precise terms for components like "panel," "text input," "checkbox," etc.

| Feature Category          | Description                                                                 | Example Prompts                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Form Creation**         | Start a new form from scratch or based on a description.                    | `Create a new form titled 'Employee Onboarding'.` <br> `Generate a customer feedback form with fields for name, email, rating (1-5 stars), and comments.` <br> `Start a simple contact form with name, email, and message fields.` <br> `Design a multi-page registration form for an event.`                                                                                     |
| **Import Design**         | Convert an existing design (image, Figma, PDF) into an AEM Form.            | `Import the form design from this uploaded PDF file.` <br> `Convert the uploaded Figma design into an adaptive form, focusing on the 'User Profile' frame.` <br> `Use this JPEG image of our old paper form to create a new digital version.` <br> `Create a form based on the layout of the attached PNG.`                                                                    |
| **Adding Components & Panels** | Add various form fields and structural containers (panels).               | `Add a text input field for 'First Name'.` <br> `Add a 'Personal Details' panel with fields for full name, date of birth, and phone number.` <br> `Insert a checkbox group for 'Interests' with options: Technology, Sports, Music.` <br> `Add a file upload component for 'Resume'.` <br> `Create a repeatable panel named 'WorkExperience' with fields for company, title, and dates.` |
| **Layout Adjustments**    | Modify the structure and appearance of your form's layout.                | `Change the 'Personal Details' panel to a two-column layout.` <br> `Set the overall form layout to a wizard (multi-step) navigation.` <br> `Make the header section span the full width of the form.` <br> `Adjust the spacing between fields in the 'Address' panel to be compact.` <br> `Align all field labels to the left.`                                                           |
| **Rule Creation & Logic** | Implement dynamic behavior, calculations, and conditional visibility.       | `Make the 'Spouse Name' field visible only if 'Marital Status' is selected as 'Married'.` <br> `Calculate the 'Total Amount' by multiplying @quantity and @price.` <br> `Enable the submit button only when the @termsAndConditions checkbox is checked.` <br> `Set the value of @countryCode to '+1' if @country is 'United States'.` <br> `If @age is less than 18, show a message 'Must be 18 or older'.` |
| **Field Properties Update** | Modify attributes of specific form fields like labels, placeholders, etc. | `Change the label of @email to 'Primary Email Address'.` <br> `Set the @comment field to be a multi-line text area.` <br> `Make the @phoneNumber field mandatory.` <br> `Add placeholder text 'Enter your ZIP code' to the @zipCode field.` <br> `Change the @country field to a dropdown and populate it with: USA, Canada, UK, Germany.` <br> `Update the help description for @password to 'Must include an uppercase letter, a number, and be at least 8 characters long.'` <br> `Set the maximum length of the @username field to 15 characters.` <br> `Configure the @dateOfBirth field to use a date picker.` |
| **Submit Actions**        | Define what happens when a user submits the form.                         | `Configure the form to submit data to the REST endpoint /api/v2/application-submit.` <br> `Set up an email submission to hr@example.com and sales@example.com on successful submission.` <br> `Trigger an AEM workflow named 'NewLeadProcessing' when this form is submitted.` <br> `On submit, redirect the user to a thank you page at /content/thankyou.html.`              |
| **Theming**               | Apply existing AEM Forms themes to style your form.                         | `Apply the 'Modern Business' theme to this form.` <br> `Switch to the 'Accessible Dark' theme.` <br> `Revert to the default canvas theme.`                                                                                                                                                                                                                                     |
| **Navigation & Structure**| Add navigation elements or reorganize parts of the form.                    | `Add a 'Next' button to the current panel and a 'Previous' button to the next panel.` <br> `Create a Table of Contents based on the form's panels.` <br> `Move the 'Address' panel to be before the 'Contact Information' panel.`                                                                                                                                         |
| **Validation**            | Set specific validation rules for fields.                                   | `Set a regex pattern for the @employeeID field to be 'EMP\d{5}'.` <br> `Ensure the @age field only accepts numeric values between 18 and 99.` <br> `Validate the @email field to ensure it is a valid email format.`                                                                                                                                                     |
| **Review Plan** (Universal Editor) | Preview the assistant's proposed changes before execution.            | `Add a contact form with fields for name, email, subject, and message.` (The assistant will show a plan of components and properties it will create, then you click "Apply").                                                                                                                                                                                |

## Best Practices for Optimal Results

To get the most out of the AI Assistant, keep these tips in mind:

- **Start Simple, Build Incrementally:** Begin with smaller, specific commands (e.g., "Add a text input for 'First Name'") rather than overly complex multi-step requests initially.
- **Use AEM Forms Terminology:** Employ terms like "panel," "text input field," "checkbox group," "submit action," "rule," etc., for better understanding by the assistant.
- **Reference Fields Clearly:** When configuring existing fields, use the `@fieldName` notation (e.g., `Make @firstName mandatory`).
- **Review Plans** Always review plans carefully for changes proposed by the assistant in the Universal Editor before clicking "Apply."
- **Manually Validate:** After the assistant makes changes, always preview and test your form to ensure it behaves and looks as expected. AI is a powerful tool, but final validation is key.
- **Iterate and Refine:** If the first prompt doesn't yield the exact result, try rephrasing or breaking down the request into smaller steps.
- **Provide Feedback:** Use the built-in feedback mechanism to help the assistant learn and improve (see "Feedback & Support" section).

## Product Help with the AI Assistant

The AI Assistant for AEM Forms isn't just for building; it can also help you learn, understand, and use various features of AEM Forms.

### Supported Help Topics

You can ask the assistant questions like:

- "How do I create a new adaptive form from scratch?"
- "What is a panel in Adaptive Forms and how is it used?"
- "Explain how to apply a theme to a form."
- "What layout types are supported for forms and panels?"
- "How do I configure different submit actions like sending an email?"
- "Can you guide me on using a Figma design to create a form?"
- "What's the best way to create a multi-step form?"

### How to Ask for Help:

1. Open the AI Assistant in Forms Manager or the Adaptive Forms Editor.
2. Type your question in natural language (e.g., "How do I add a repeatable panel?").
3. The assistant will respond with:
    - Step-by-step instructions.
    - Explanations of AEM Forms concepts.
    - Links to relevant Adobe Experience League documentation, if applicable.

### Tips for Getting Better Help:

- **Be Specific:** Ask one clear question at a time.
- **Use Keywords:** Include keywords relevant to AEM Forms features or UI elements (e.g., "adaptive form editor," "rule editor," "theme").
- **Rephrase if Needed:** If the assistant doesn't understand or provide the desired information, try simplifying your question or using different terms.


## Troubleshooting Common Issues

- **Assistant Not Responding:**
    - Ensure you are actively working within a supported environment (Forms Manager, Adaptive Forms Editor, or Universal Editor).
    - Check your internet connection.
    - Try closing and reopening the AI Assistant panel.

- **Inaccurate or Unexpected Responses:**
    - Rephrase your request to be more specific or simpler.
    - Break down a complex request into smaller, individual commands.
    - Ensure you are using standard AEM Forms terminology.

- **Design Import Issues (PDF/Figma/Image):**
    - Verify the design file is clear, well-structured, and legible.
    - Ensure the file format is supported (PDF, Figma link, common image types like PNG, JPG).
    - For Figma, ensure the frame you're targeting is clearly defined and accessible.

- **Field `@fieldName` Not Recognized:**
    - Double-check the exact name of the field in your form. Field names are case-sensitive and must match precisely.
    - Ensure the field already exists if you are trying to modify it.


## Feedback & Support

Your input is invaluable for the continuous improvement of the AI Assistant.

- **Provide Feedback:** Use the built-in **"Provide Feedback" command or button** within the AI Assistant interface to share your experiences, report issues, or suggest enhancements. (e.g., you might type `/feedback` or look for a feedback icon).
- **Official Support:** For critical issues or further assistance, please reach out through the official Adobe support channels or your organization's designated support contacts.


## Related Content

[AEM Forms AI Assistant - Prompt Library](/help/edge/docs/forms/ai-assistant-prompt-library.md)
