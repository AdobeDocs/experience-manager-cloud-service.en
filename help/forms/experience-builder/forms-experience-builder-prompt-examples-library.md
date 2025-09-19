---
title: Forms Experience Builder - Prompt Library
description: Collection of proven prompt patterns and examples for building forms with AI assistance across Forms Management UI, Adaptive Forms Editor, and Universal Editor.
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
exl-id: c8f64082-a23f-4919-ad66-042faad77d31
---

# Forms Experience Builder - Prompt Library

Collection of reusable prompt patterns and examples optimized for Forms Experience Builder. This streamlined library focuses on the two core creation methods: Create from Scratch and Import & Convert, with enhanced support for LLM-powered smart fields and brand consistency.

>[!NOTE]
>
> The Forms Experience Builder is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

## Using This Prompt Library

This library provides reusable prompt patterns for common form-building scenarios. For comprehensive best practices, see the [Forms Experience Builder Getting Started Guide](/help/forms/experience-builder/forms-experience-builder-getting-started.md).

### Quick Tips for This Library

- **Start with examples** - Use provided prompts as templates and adapt to your needs
- **Two creation methods** - Choose Create from Scratch or Import & Convert approaches
- **Be specific** - Add your own details to generic examples  
- **Test thoroughly** - Always validate results in your specific environment

### Brand Templates and Styles

**Prepare brand assets in advance for consistent form creation:**

- **Brand Templates** - Prepare standardized form templates with your organization's colors, fonts, and layout patterns
- **Style Guidelines** - Define consistent field styling, button designs, and spacing standards that Forms Experience Builder can apply
- **Component Library** - Work with your development team to prepare reusable form components that match your brand identity
- **Visual Assets** - Prepare logos, icons, and background elements for form integration


## Incremental Development Examples

These examples show how to build forms step-by-step, starting simple and adding complexity gradually:

### Example 1: Building a Contact Form Incrementally

**Step 1 - Start Simple:**

    Create a basic contact form with name, email, and message fields

**Step 2 - Add Validation:**

    Make @name and @email mandatory fields with appropriate validation

**Step 3 - Enhance User Experience:**

    Add placeholder text: @name "Your full name", @email "your.email@company.com", @message "Tell us how we can help"

**Step 4 - Add Advanced Features:**

    Add a dropdown inquiryType with options: "General Question", "Support Request", "Sales Inquiry", "Partnership"

**Step 5 - Implement Conditional Logic:**

    /create-rule show @urgencyLevel dropdown (Low, Medium, High) only when @inquiryType equals "Support Request"

### Example 2: Building a Registration Form Incrementally

**Step 1 - Basic Structure:**

    Create a user registration form with personal information panel

**Step 2 - Add Required Fields:**

    Add fields for @firstName, @lastName, @email, @phoneNumber with appropriate validation

**Step 3 - Add Business Logic:**

    Create a rule: if @age is under 18, show parent/guardian information section

**Step 4 - Enhance with Preferences:**

    Add a preferences panel with @newsletterSubscription, @marketingConsent, @termsAccepted

**Step 5 - Add File Upload:**

    Include a file upload field for @profilePicture with size limit of 5MB

## Form Creation & Management

**When to use:** When you need to create new forms or modify existing ones.

**How to use:** Choose one of two approaches: Create from Scratch or Import & Convert (see [Getting Started Guide](/help/forms/experience-builder/forms-experience-builder-getting-started.md).

**Example Prompt - Simple Form Creation:**

    Create a customer feedback form with:
    - Product rating (1-5 stars)
    - Comment field for detailed feedback
    - Customer email (optional)
    - Submit to email notification

**Example Prompt - Complex Form Creation:**

    Create a comprehensive employee onboarding form with:
    
    **Personal Information Section:**
    - Full name (first, middle, last)
    - Date of birth with age validation
    - Contact information (email, phone, address)
    - Emergency contact details
    
    **Employment Details:**
    - Position and department selection
    - Start date with business day validation
    - Salary information with confidentiality notice
    - Reporting structure
    
    **Document Upload:**
    - Resume/CV upload (PDF, DOC, DOCX)
    - ID verification documents
    - Tax forms and banking information
    - Signed employment agreement
    
    **Preferences:**
    - Benefits selection with cost calculator
    - Work schedule preferences
    - Training requirements
    - Equipment needs
    
    **Validation Rules:**
    - Email format validation
    - Phone number format validation
    - Age must be 18 or older
    - All required documents must be uploaded
    - Terms and conditions must be accepted
    
    **Submit Actions:**
    - Send confirmation email to new employee
    - Notify HR department
    - Create employee record in HR system
    - Schedule orientation meeting

**Form Management Prompts:**

    Import this PDF application form and convert it to an adaptive form with enhanced validation

    Update the existing contact form to include social media handles and preferred contact method

    Reorganize the registration form into a 3-step wizard: personal info, preferences, confirmation

## Field Management & Configuration

**When to use:** When you need to add, modify, or configure form fields.

**How to use:** Be specific about field types, validation rules, and user experience requirements.

**Example Prompt - Basic Field Addition:**

    Add a text input field for "Company Name" with placeholder "Enter your company name"

**Example Prompt - Advanced Field Configuration:**

    Add a comprehensive address section with:
    
    **Street Address:**
    - Address line 1 (required, max 100 characters)
    - Address line 2 (optional, max 100 characters)
    - City (required, dropdown with common cities)
    - State/Province (required, dropdown)
    - Postal code (required, format validation)
    - Country (required, default to "United States")
    
    **Validation Rules:**
    - Postal code must match state selection
    - Address line 1 cannot be empty
    - City must be a valid city for selected state
    
    **User Experience:**
    - Auto-complete for address fields
    - Clear labels and help text
    - Mobile-friendly input fields
    - Accessibility compliance

**Field Configuration Prompts:**

    Make @email field required with real-time validation and custom error message

    Add a dropdown for @country with options for USA, Canada, UK, Germany, France, and "Other"

    Configure @phoneNumber field with format (XXX) XXX-XXXX and validation

    Add a file upload field for @resume with PDF and DOC restrictions, max 5MB

## LLM-Enhanced Smart Fields

**When to use:** When you need fields with pre-populated options that leverage the AI's knowledge base.

**How to use:** Request fields that require comprehensive data sets - the AI can automatically populate options using its built-in knowledge.

### Geographic and Location Fields

**Airports and Transportation:**

    Add a dropdown for departure airports with all major international airports
    Add arrival airport field with IATA codes and full names
    Create a field for nearest airport to user location
    Add a selection of train stations for European cities

**Administrative Regions:**

    Add a complete list of US states with abbreviations
    Create a country dropdown with ISO codes and full names
    Add a field for major world cities with time zones
    Include a dropdown of Canadian provinces and territories
    Add a field for UK counties and postal areas

### Business and Industry Data

**Company Classifications:**

    Add a field for industry classification with NAICS codes
    Create a dropdown of business entity types (LLC, Corporation, Partnership, etc.)
    Add a field for company size categories (startup, SME, enterprise)
    Include department selection for large organizations
    Add a field for professional service types

**Professional Classifications:**

    Add a field for job titles with common industry roles
    Create a dropdown of professional certifications by field
    Include education levels with degree types
    Add a field for years of experience ranges
    Create a selection for programming languages and frameworks

### Standards and Regulatory

**Financial and Legal:**

    Add a field for currency codes with symbols and exchange rates
    Create a dropdown of tax ID types by country
    Include a field for legal document types
    Add payment method options with security features
    Create a selection for banking institutions by country

**Technical Standards:**

    Add a dropdown of file format types with extensions
    Include network protocol options
    Add a field for database types and versions
    Create a selection for API authentication methods

### Healthcare and Medical

**Medical Classifications:**

    Add a field for medical specialties
    Create a dropdown of common medications with generic names
    Include a field for insurance provider types
    Add a selection for medical emergency contact relationships
    Create a field for dietary restrictions and allergies

### Time and Calendar Intelligence

**Date and Time Fields:**

    Add a field for business hours with time zone handling
    Create a dropdown of public holidays by country
    Include seasonal options with date ranges
    Add a field for conference room booking with availability
    Create a selection for recurring meeting patterns

### Product and Service Categories

**E-commerce Classifications:**

    Add a field for product categories with subcategories
    Create a dropdown of shipping methods with delivery estimates
    Include a field for return policy options
    Add a selection for customer priority levels
    Create a field for subscription billing cycles

**Example Smart Field Prompts:**

    "Add a departure airport field with all major airports worldwide including IATA codes and city names"

    "Create a comprehensive industry field using standard NAICS classification with technology subcategories"

    "Include a professional certification dropdown that adapts based on the selected job field"

    "Add an international phone number field that formats based on the selected country"

    "Create a university selection field with major institutions organized by country and ranking"

## Rule Creation & Business Logic

**When to use:** When you need to implement conditional logic, validation rules, or business processes.

**How to use:** Describe the business logic clearly, specifying conditions and actions.

**Example Prompt - Simple Conditional Logic:**

    Create a rule that shows @spouseInformation panel only when @maritalStatus equals "Married"

**Example Prompt - Complex Business Rules:**

    Implement comprehensive loan application validation:
    
    **Income Validation:**
    - If @annualIncome is less than 30000:
      - Show warning message: "Income may be insufficient for requested loan amount"
      - Require additional income documentation
      - Display message: "Additional documentation may be required"
    - If @annualIncome is greater than 100000:
      - Show premium services options
      - Enable priority processing checkbox
    
    **Age-Based Validation:**
    - If @age is under 18:
      - Show parent/guardian information section
      - Make parent signature upload mandatory
      - Change submit button text to "Submit for Review"
    - If @age is 65 or older:
      - Show senior discount options
      - Add accessibility preferences section

**Rule-Specific Prompts:**

    Create a **visibility rule** that shows @spouseInformation panel only when @maritalStatus equals "Married" or "Domestic Partnership"

    Add **progressive disclosure** where additional questions appear based on previous answers. Start with basic info, then show relevant follow-ups

    Implement **smart defaults** where @country selection auto-sets related fields. Allow manual override

## Data Integration & Submission

**When to use:** When you need to connect forms to backend systems, databases, or external services.

**How to use:** Start with basic submission setup, then add additional integrations incrementally. Specify the integration type, data format requirements, and error handling preferences.

**Example Prompt - Start with Basic Submission:**

    Configure basic form submission for @applicationForm:
    
    **Primary Submission:**
    - Send form data to REST endpoint: `/api/v1/applications`
    - Format data as JSON
    - Show success message: "Application submitted successfully"
    - Show error message if submission fails: "Submission failed, please try again"

**Then Add Secondary Actions Incrementally:**

    Add email notification to @applicationForm: Send confirmation email to @email address with application reference number

    Add CRM integration to @applicationForm: Create new lead record with @firstName, @lastName, @email, and set Status to "New Application"

**Example Prompt - Standard Multi-Channel Submission:**

    Configure form submission with multiple data destinations:
    
    **Primary Submission:**
    - Send form data to REST endpoint: `/api/v1/applications`
    - Include authentication header with API key
    - Format data as JSON with nested objects for address and employment
    - Handle success response (201) by showing thank you message
    
    **Secondary Actions:**
    - Send notification email to applicant at @email address
    - Copy application data to tracking system
    - Trigger workflow for approval process
    - Create record in CRM with lead status "New Application"
    
    **Error Handling:**
    - If primary submission fails, save data locally and retry
    - Show user-friendly error message: "Submission temporarily unavailable"
    - Provide option to download form data as backup
    - Send alert email to admin team about failed submission
    
    **Success Flow:**
    - Redirect to confirmation page with application reference number
    - Send confirmation email with next steps
    - Display estimated processing timeline

**Integration-Specific Prompts:**

    Connect this form to **CRM system** to create new leads. Map @firstName to FirstName, @email to Email, set LeadSource to "Web Form", and Status to "New"

    Set up **workflow trigger** when form is submitted. Pass all form data and trigger approval workflow with manager notification

    Configure **database integration** to save form submissions as records. Create new folder for each submission with uploaded documents



## Command Reference

### Essential Commands

| Command | Best Use Case | Example |
|---------|---------------|---------|
| `/create-form` | Starting new forms | `/create-form employee onboarding with personal info and benefits selection` |
| `/add-form` | Adding forms to pages | `/add-form newsletter signup with email and preferences` |
| `/update-layout` | Changing form structure | `/update-layout wizard with 4 steps: info, preferences, review, confirm` |
| `/update-field` | Modifying field properties | `/update-field @email to be mandatory with real-time validation` |
| `/create-rule` | Adding dynamic behavior | `/create-rule show @spouseInfo if @maritalStatus equals "Married"` |
| `/create-panel` | Organizing form sections | `/create-panel Employment Details with job title, company, salary fields` |
| `/add-panel` | Converting designs | `/add-panel from uploaded form image with field recognition` |
| `/help` | Getting assistance | `/help how to implement multi-step validation?` |

### Field References

Use `@fieldName` syntax to reference existing fields in your prompts:

- `@email` - Reference email field
- `@firstName` - Reference first name field  
- `@maritalStatus` - Reference marital status field

### Component Types

**Input Components:**

- `text`, `email`, `number`, `tel`, `date`, `checkbox`, `radio`, `dropdown`, `file`, `textarea`

**Container Components:**

- `fieldset`, `panel`, `repeatable`, `wizard`

### Component Properties

**Universal Properties (All Components):**

- **Type**: Component type 
- **Name**: Field identifier for form submission
- **Label**: Display text for the field
- **Description**: Help text for the field
- **Visible**: Boolean for initial visibility
- **Mandatory**: Boolean for required fields

**Input Field Properties:**

- **Value**: Default/initial value
- **Placeholder**: Hint text for input fields
- **Min**: Minimum value (for numbers/dates)
- **Max**: Maximum value (for numbers/dates)

**File Upload Properties:**

- **Accept**: File types (.pdf, .doc, .docx, .jpg, .png, etc.)
- **Multiple**: Boolean for multiple file selection

**Selection Control Properties:**

- **Options**: Choices for dropdowns (comma-separated list)
- **Checked**: Default selection for checkboxes/radio

**Container Properties:**

- **Fieldset**: Grouping related fields
- **Repeatable**: Boolean for repeatable sections

**Advanced Properties:**

- **Visible Expression**: Formula for conditional visibility (=formula)
- **Value Expression**: Formula for calculated values (=formula)

### Integration Commands

**Submit Actions:**

- Email notifications
- REST API submissions
- Cloud storage (Azure, SharePoint)
- Workflow automation (Power Automate, Workfront Fusion)
- Marketing platforms (Marketo)
- CRM integrations

### Prompt Syntax Guidelines

- **Field References**: Use `@fieldName` for existing fields
- **Commands**: Use `/command` for specific actions  
- **Natural Language**: Describe requirements clearly and specifically

### Validation Checklist

For comprehensive best practices and validation guidelines, see the [Forms Experience Builder Getting Started Guide](/help/forms/experience-builder/forms-experience-builder-getting-started.md).

*This prompt library is continuously updated based on user feedback and new Forms Experience Builder capabilities. For the latest features and examples, check the [AEM Forms documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/home.html).*
