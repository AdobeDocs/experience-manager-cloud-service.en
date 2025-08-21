---
title: Forms Experience Builder - Prompt Library
description: Collection of proven prompt patterns and examples for building forms with AI assistance across Forms Management UI, Adaptive Forms Editor, and Universal Editor.
feature: Edge Delivery Services
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

This library provides reusable prompt patterns for common form-building scenarios. For comprehensive best practices, see the [Forms Experience Builder Getting Started Guide](forms-ai-assistant-getting-started.md#best-practices).

### Quick Tips for This Library

- **Start with examples** - Use provided prompts as templates and adapt to your needs
- **Two creation methods** - Choose Create from Scratch or Import & Convert approaches
- **Be specific** - Add your own details to generic examples  
- **Test thoroughly** - Always validate results in your specific environment

### Brand Templates and Styles

**Prepare brand assets in advance for consistent form creation:**

- **Brand Templates** - Create standardized form templates with your organization's colors, fonts, and layout patterns
- **Style Guidelines** - Define consistent field styling, button designs, and spacing standards
- **Component Library** - Build reusable form components that match your brand identity
- **Visual Assets** - Prepare logos, icons, and background elements for form integration

**Example Brand Template Prompt:**

```
Create a brand template for financial services forms with:
- Corporate blue (#003366) and silver (#C0C0C0) color scheme
- Open Sans font family for all text
- 16px minimum font size for accessibility
- Consistent 24px spacing between sections
- Corporate logo in header with proper sizing
- Professional button styling with hover effects
```

>[!NOTE]
>
>**Custom Components**: Check with your development team about using organization-specific components and their compatibility with Forms Experience Builder before implementing custom brand elements.

>[!NOTE]
>
> This prompt library has been updated to reflect the streamlined Forms Experience Builder capabilities. Some advanced integration and testing features shown in examples may require additional configuration.



## Incremental Development Examples

These examples show how to build forms step-by-step, starting simple and adding complexity gradually:

### Example 1: Building a Contact Form Incrementally

**Step 1 - Start Simple:**

```
Create a basic contact form with name, email, and message fields
```

**Step 2 - Add Validation:**

```
Make @name and @email mandatory fields with appropriate validation
```

**Step 3 - Enhance User Experience:**

```
Add placeholder text: @name "Your full name", @email "your.email@company.com", @message "Tell us how we can help"
```

**Step 4 - Add Advanced Features:**

```
Add a dropdown @inquiryType with options: "General Question", "Support Request", "Sales Inquiry", "Partnership"
```

**Step 5 - Implement Conditional Logic:**

```
Show @urgencyLevel dropdown (Low, Medium, High) only when @inquiryType equals "Support Request"
```

### Example 2: Building a Registration Form Incrementally

**Step 1 - Basic Structure:**

```
Create a user registration form with personal information panel
```

**Step 2 - Add Required Fields:**

```
Add fields for @firstName, @lastName, @email, @phoneNumber with appropriate validation
```

**Step 3 - Add Business Logic:**

```
Create a rule: if @age is under 18, show parent/guardian information section
```

**Step 4 - Enhance with Preferences:**

```
Add a preferences panel with @newsletterSubscription, @marketingConsent, @termsAccepted
```

**Step 5 - Add File Upload:**

```
Include a file upload field for @profilePicture with size limit of 5MB
```

## Form Creation & Management

**When to use:** When you need to create new forms or modify existing ones. 

**How to use:** Choose one of two approaches: Create from Scratch or Import & Convert (see [Getting Started Guide](/help/edge/docs/forms/forms-ai-assistant-getting-started.md)).

**Example Prompt - Simple Form Creation:**

```
Create a customer feedback form with:
- Product rating (1-5 stars)
- Comment field for detailed feedback
- Customer email (optional)
- Submit to email notification
```

**Example Prompt - Complex Form Creation:**

```
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
```

**Form Management Prompts:**

```
Import this PDF application form and convert it to an adaptive form with enhanced validation
```

```
Update the existing contact form to include social media handles and preferred contact method
```

```
Reorganize the registration form into a 3-step wizard: personal info, preferences, confirmation
```

## Field Management & Configuration

**When to use:** When you need to add, modify, or configure form fields.

**How to use:** Be specific about field types, validation rules, and user experience requirements.

**Example Prompt - Basic Field Addition:**

```
Add a text input field for "Company Name" with placeholder "Enter your company name"
```

**Example Prompt - Advanced Field Configuration:**

```
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
```

**Field Configuration Prompts:**

```
Make @email field required with real-time validation and custom error message
```

```
Add a dropdown for @country with options for USA, Canada, UK, Germany, France, and "Other"
```

```
Configure @phoneNumber field with format (XXX) XXX-XXXX and validation
```

```
Add a file upload field for @resume with PDF and DOC restrictions, max 5MB
```

## LLM-Enhanced Smart Fields

**When to use:** When you need fields with pre-populated options that leverage the AI's knowledge base.

**How to use:** Request fields that require comprehensive data sets - the AI can automatically populate options using its built-in knowledge.

### Geographic and Location Fields

**Airports and Transportation:**

```
Add a dropdown for departure airports with all major international airports
Add arrival airport field with IATA codes and full names
Create a field for nearest airport to user location
Add a selection of train stations for European cities
```

**Administrative Regions:**

```
Add a complete list of US states with abbreviations
Create a country dropdown with ISO codes and full names
Add a field for major world cities with time zones
Include a dropdown of Canadian provinces and territories
Add a field for UK counties and postal areas
```

### Business and Industry Data

**Company Classifications:**

```
Add a field for industry classification with NAICS codes
Create a dropdown of business entity types (LLC, Corporation, Partnership, etc.)
Add a field for company size categories (startup, SME, enterprise)
Include department selection for large organizations
Add a field for professional service types
```

**Professional Classifications:**

```
Add a field for job titles with common industry roles
Create a dropdown of professional certifications by field
Include education levels with degree types
Add a field for years of experience ranges
Create a selection for programming languages and frameworks
```

### Standards and Regulatory

**Financial and Legal:**

```
Add a field for currency codes with symbols and exchange rates
Create a dropdown of tax ID types by country
Include a field for legal document types
Add payment method options with security features
Create a selection for banking institutions by country
```

**Technical Standards:**

```
Add a dropdown of file format types with extensions
Include network protocol options
Add a field for database types and versions
Create a selection for API authentication methods
```

### Healthcare and Medical

**Medical Classifications:**

```
Add a field for medical specialties
Create a dropdown of common medications with generic names
Include a field for insurance provider types
Add a selection for medical emergency contact relationships
Create a field for dietary restrictions and allergies
```

### Time and Calendar Intelligence

**Date and Time Fields:**

```
Add a field for business hours with time zone handling
Create a dropdown of public holidays by country
Include seasonal options with date ranges
Add a field for conference room booking with availability
Create a selection for recurring meeting patterns
```

### Product and Service Categories

**E-commerce Classifications:**

```
Add a field for product categories with subcategories
Create a dropdown of shipping methods with delivery estimates
Include a field for return policy options
Add a selection for customer priority levels
Create a field for subscription billing cycles
```

**Example Smart Field Prompts:**

```
"Add a departure airport field with all major airports worldwide including IATA codes and city names"
```

```
"Create a comprehensive industry field using standard NAICS classification with technology subcategories"
```

```
"Include a professional certification dropdown that adapts based on the selected job field"
```

```
"Add an international phone number field that formats based on the selected country"
```

```
"Create a university selection field with major institutions organized by country and ranking"
```

## Rule Creation & Business Logic

**When to use:** When you need to implement conditional logic, validation rules, or business processes.

**How to use:** Describe the business logic clearly, specifying conditions and actions.

**Example Prompt - Simple Conditional Logic:**

```
Create a rule that shows @spouseInformation panel only when @maritalStatus equals "Married"
```

**Example Prompt - Complex Business Rules:**

```
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
```

**Rule-Specific Prompts:**

```
Create a **visibility rule** that shows @spouseInformation panel only when @maritalStatus equals "Married" or "Domestic Partnership"
```

```
Add **progressive disclosure** where additional questions appear based on previous answers. Start with basic info, then show relevant follow-ups
```

```
Implement **smart defaults** where @country selection auto-sets related fields. Allow manual override
```

## Data Integration & Submission

**When to use:** When you need to connect forms to backend systems, databases, or external services.

**How to use:** Start with basic submission setup, then add additional integrations incrementally. Specify the integration type, data format requirements, and error handling preferences.

**Example Prompt - Start with Basic Submission:**

```
Configure basic form submission for @applicationForm:

**Primary Submission:**
- Send form data to REST endpoint: `/api/v1/applications`
- Format data as JSON
- Show success message: "Application submitted successfully"
- Show error message if submission fails: "Submission failed, please try again"
```

**Then Add Secondary Actions Incrementally:**

```
Add email notification to @applicationForm: Send confirmation email to @email address with application reference number
```

```
Add CRM integration to @applicationForm: Create new lead record with @firstName, @lastName, @email, and set Status to "New Application"
```

**Example Prompt - Standard Multi-Channel Submission:**

```
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
```

**Integration-Specific Prompts:**

```
Connect this form to **CRM system** to create new leads. Map @firstName to FirstName, @email to Email, set LeadSource to "Web Form", and Status to "New"
```

```
Set up **workflow trigger** when form is submitted. Pass all form data and trigger approval workflow with manager notification
```

```
Configure **database integration** to save form submissions as records. Create new folder for each submission with uploaded documents
```

## Import & Convert Existing Forms

**When to use:** When you have existing forms, documents, or designs to transform into modern AEM forms.

**How to use:** Upload your source file and describe the conversion requirements (see [Import Guide](/help/edge/docs/forms/forms-ai-assistant-getting-started.md)).

**Example Prompt - PDF Form Conversion:**

```
Convert this uploaded **PDF application form** into a functional AEM adaptive form:

**Source Analysis:**
- Analyze the PDF layout and identify all form fields
- Preserve the visual hierarchy and grouping
- Maintain the professional appearance and branding

**Field Mapping:**
- Convert PDF text fields to adaptive form text inputs
- Transform checkboxes to checkbox components
- Convert dropdown lists to AEM dropdown components
- Map signature areas to digital signature fields

**Enhancements:**
- Add real-time validation that wasn't possible in PDF
- Implement conditional logic for dependent fields
- Make the form responsive for mobile devices
- Add progress saving capability
- Include accessibility improvements (ARIA labels, keyboard navigation)

**Styling:**
- Match the original color scheme and fonts
- Maintain professional business appearance
- Ensure consistent spacing and alignment
- Add subtle animations for better user experience

Preserve all original field labels and help text, but improve the user experience with modern form interactions
```

**Design Import Prompts:**

```
Import this **design mockup** and convert it into an adaptive form. Maintain the exact visual design but add proper validation and mobile responsiveness
```

```
Analyze this **image of a paper form** and recreate it digitally. Improve the layout for better mobile experience while keeping all mandatory fields
```

```
Convert this **existing HTML form** to AEM adaptive form format. Preserve all functionality but add AEM-specific features like rules and themes
```

## Mobile Optimization & Responsiveness

**When to use:** When forms need to work seamlessly across all device types and screen sizes.

**How to use:** Start with basic mobile optimization, then enhance with advanced features. Emphasize mobile-first approach and specify breakpoint behaviors incrementally.

**Example Prompt - Start with Basic Mobile Optimization:**

```
Make @contactForm mobile-friendly with:

**Basic Mobile Layout:**
- Single column layout for all form sections
- Larger touch targets for buttons and inputs
- Responsive design that works on phones and tablets
```

**Then Add Advanced Mobile Features:**

```
Enhance @contactForm mobile experience with:
- Sticky submit button at bottom of screen
- Touch-friendly date pickers
- Swipe gestures for multi-step navigation
```

**Example Prompt - Comprehensive Mobile-First Optimization:**

```
Optimize this form for **mobile-first responsive design**:

**Mobile Layout (320px - 768px):**
- Single column layout for all form sections
- Larger touch targets (minimum 44px height)
- Simplified navigation with collapsible sections
- Sticky submit button at bottom of screen
- Auto-zoom disabled on input focus

**Tablet Layout (768px - 1024px):**
- Two-column layout for shorter fields (name, email)
- Single column for complex fields (address, comments)
- Side navigation for multi-step forms
- Optimized for both portrait and landscape

**Desktop Layout (1024px+):**
- Multi-column layouts where appropriate
- Horizontal form sections for related fields
- Sidebar navigation for long forms
- Hover states and advanced interactions
```

**Mobile-Specific Prompts:**

```
Make this form **touch-friendly** with larger buttons and simplified navigation for mobile users
```

```
Optimize form for **tablet users** with appropriate field sizes and navigation patterns
```

```
Add **swipe gestures** for multi-step form navigation on mobile devices
```

## Accessibility & Compliance

**When to use:** When forms need to meet accessibility standards (WCAG) or compliance requirements.

**How to use:** Specify the required compliance level and any specific accessibility features needed.

**Example Prompt - Basic Accessibility:**

```
Make @contactForm accessible with:

**Basic Accessibility:**
- Proper ARIA labels for all form fields
- Keyboard navigation support
- High contrast color scheme
- Screen reader compatibility
- Focus indicators for all interactive elements
```

**Example Prompt - Advanced Accessibility:**

```
Implement comprehensive accessibility for @applicationForm:

**WCAG 2.1 AA Compliance:**
- Semantic HTML structure with proper headings
- ARIA landmarks and roles for navigation
- Color contrast ratio of at least 4.5:1
- Keyboard-only navigation support
- Screen reader announcements for dynamic content

**Form-Specific Accessibility:**
- Error messages announced to screen readers
- Field validation with clear error descriptions
- Progress indicators for multi-step forms
- Skip navigation links for keyboard users
- Alternative text for all images and icons

**User Experience:**
- Clear focus indicators on all interactive elements
- Logical tab order through form fields
- Descriptive link text and button labels
- Help text available for complex fields
- Timeout warnings for session expiration
```

**Accessibility-Specific Prompts:**

```
Add **screen reader support** to this form with proper ARIA labels and announcements
```

```
Implement **keyboard navigation** for all form interactions and navigation elements
```

```
Ensure **color contrast** meets WCAG AA standards for all text and interactive elements
```

## Performance Optimization

**When to use:** When forms need to load quickly and perform well under various conditions.

**How to use:** Specify performance requirements and optimization strategies.

**Example Prompt - Basic Performance:**

```
Optimize @contactForm for performance:

**Loading Optimization:**
- Lazy load non-critical form sections
- Minimize initial bundle size
- Optimize images and assets
- Enable caching for static resources
```

**Example Prompt - Advanced Performance:**

```
Implement comprehensive performance optimization for @applicationForm:

**Loading Performance:**
- Progressive loading of form sections
- Optimize images with WebP format
- Minimize JavaScript bundle size
- Enable gzip compression for all assets

**Runtime Performance:**
- Debounce validation calls to reduce API requests
- Optimize conditional logic execution
- Cache frequently used data
- Implement virtual scrolling for long lists

**User Experience:**
- Show loading indicators for async operations
- Provide offline capability for form data
- Auto-save form progress every 30 seconds
- Optimize form submission with retry logic

**Monitoring:**
- Track form load times and user interactions
- Monitor validation performance
- Measure submission success rates
- Alert on performance degradation
```

**Performance-Specific Prompts:**

```
Optimize form **loading speed** by implementing progressive loading and asset optimization
```

```
Add **auto-save functionality** to prevent data loss during form completion
```

```
Implement **offline support** so users can complete forms without internet connection
```

## Testing & Quality Assurance

**When to use:** When forms need comprehensive testing to ensure reliability and user satisfaction.

**How to use:** Specify testing scenarios, validation requirements, and quality metrics.

**Example Prompt - Basic Testing:**

```
Add comprehensive testing for @contactForm:

**Functional Testing:**
- Test all form field validations
- Verify submit functionality works correctly
- Test error handling and user feedback
- Validate conditional logic and rules
```

**Example Prompt - Advanced Testing:**

```
Implement comprehensive testing strategy for @applicationForm:

**Functional Testing:**
- Unit tests for all validation rules
- Integration tests for submit actions
- End-to-end testing for complete user flows
- Cross-browser compatibility testing

**User Experience Testing:**
- Usability testing with target user groups
- Accessibility testing with screen readers
- Mobile device testing on various screen sizes
- Performance testing under load conditions

**Quality Assurance:**
- Automated testing for regression prevention
- Manual testing for edge cases and scenarios
- Security testing for data protection
- Compliance testing for regulatory requirements

**Monitoring:**
- Track form completion rates and abandonment
- Monitor error rates and user feedback
- Measure performance metrics and load times
- Analyze user behavior and interaction patterns
```

**Testing-Specific Prompts:**

```
Add **automated testing** for all form validations and submit functionality
```

```
Implement **user acceptance testing** scenarios for complete form workflows
```

```
Set up **performance monitoring** to track form load times and user interactions
```

## Troubleshooting

Quick solutions for common Forms Experience Builder issues:

| Issue | Quick Fix |
|-------|-----------|
| Form not submitting | Check submit action configuration and validation rules |
| Validation errors not showing | Verify field validation settings and error message placement |
| Mobile layout issues | Review responsive design settings and field sizing |
| Fields not appearing | Check conditional logic and visibility rules |
| Import failures | Verify file format compatibility and size limits |
| Integration errors | Validate API endpoints and authentication credentials |
| Performance issues | Optimize field count and remove unnecessary validations |
| Accessibility problems | Review field labels, ARIA attributes, and tab order |

**Debug Mode Prompt:**

```
Enable debug mode to identify issues with form submission and field validation
```

**Error Analysis Prompt:**

```
Analyze form errors: check validation rules, API responses, and user input patterns
```

## Advanced Analytics & Insights

**When to use:** When you need to understand form performance and user behavior.

**How to use:** Specify the analytics requirements and insights needed.

**Example Prompt - Basic Analytics:**

```
Add analytics to @contactForm:

**Basic Metrics:**
- Form completion rates
- Field abandonment rates
- Submit success/failure rates
- User session duration
```

**Example Prompt - Advanced Analytics:**

```
Implement comprehensive analytics for @applicationForm:

**User Behavior Analytics:**
- Track field completion rates and abandonment
- Monitor user session duration and patterns
- Analyze form navigation and user flow
- Identify bottlenecks and friction points

**Performance Analytics:**
- Measure form load times and performance
- Track API response times and failures
- Monitor validation rule effectiveness
- Analyze submission success rates

**Business Intelligence:**
- Generate reports on form effectiveness
- Track conversion rates and ROI
- Monitor user satisfaction and feedback
- Identify opportunities for optimization

**Predictive Analytics:**
- Predict form completion likelihood
- Identify users likely to abandon
- Recommend form improvements
- Optimize user experience based on data
```

**Analytics-Specific Prompts:**

```
Add **conversion tracking** to measure form completion rates and user behavior
```

```
Implement **A/B testing** to compare different form designs and optimize performance
```

```
Create **analytics dashboard** to monitor form performance and user insights
```

## Security & Data Protection

**When to use:** When forms handle sensitive data and need security measures.

**How to use:** Specify security requirements and data protection measures.

**Example Prompt - Basic Security:**

```
Add security measures to @contactForm:

**Basic Security:**
- HTTPS encryption for all data transmission
- Input validation and sanitization
- CSRF protection for form submissions
- Secure session management
```

**Example Prompt - Advanced Security:**

```
Implement comprehensive security for @applicationForm:

**Data Protection:**
- End-to-end encryption for sensitive data
- PII data masking and anonymization
- Secure file upload with virus scanning
- Data retention and deletion policies

**Access Control:**
- Role-based access control for form data
- Multi-factor authentication for admin access
- Audit logging for all data access
- Secure API authentication and authorization

**Compliance:**
- GDPR compliance for data handling
- HIPAA compliance for health information
- PCI DSS compliance for payment data
- SOC 2 compliance for data security

**Monitoring:**
- Real-time security monitoring and alerts
- Intrusion detection and prevention
- Data breach notification systems
- Regular security audits and assessments
```

**Security-Specific Prompts:**

```
Implement **data encryption** for sensitive form submissions and user information
```

```
Add **access control** to restrict form data access based on user roles and permissions
```

```
Set up **security monitoring** to detect and prevent unauthorized access to form data
```

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
| `/configure-submit` | Setting up data handling | `/configure-submit to CRM and send confirmation email` |
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

For comprehensive best practices and validation guidelines, see the [Forms Experience Builder Getting Started Guide](forms-ai-assistant-getting-started.md#best-practices).

*This prompt library is continuously updated based on user feedback and new Forms Experience Builder capabilities. For the latest features and examples, check the [AEM Forms documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/home.html).*
