---
title: AEM Forms AI Assistant - Prompt Library
description: Collection of proven prompt patterns and examples for building forms with AI assistance across Forms Management UI, Adaptive Forms Editor, and Universal Editor.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
role: Admin, Architect, Developer
---


# AEM Forms AI Assistant - Prompt Library

Collection of reusable prompt patterns and examples for common form-building scenarios. Think of these as templates you can adapt to your specific needs. Each section covers a particular use case with guidance on when to use it and proven examples.

>[!NOTE]
>
> The AI Assistant for AEM Forms is available under the early-adopter program. Send an email from your work address to mailto:aem-forms-ea@adobe.com to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the AI Assistant for AEM Forms continues to evolve during the early-adopter program.

## Best Practices for Optimal Results

To get the most out of the AI Assistant, keep these tips in mind:

### Start Simple, Build Incrementally

Begin with smaller, specific commands (e.g., "Add a text input for 'First Name'") rather than overly complex multi-step requests initially. This approach helps ensure accuracy and makes it easier to troubleshoot if something doesn't work as expected.

**Example of Simple Start:**

```
Add a text input field for "First Name" with placeholder "Enter your first name"
```

**Then Build Incrementally:**

```
Make @firstName mandatory and add validation message "First name is mandatory"
```

### Use AEM Forms Terminology

Employ terms like "panel," "text input field," "checkbox group," "submit action," "rule," etc., for better understanding by the assistant. This ensures the AI interprets your requests correctly within the AEM Forms context.

**Preferred Terms:**

- "text input field" instead of "text box"
- "checkbox group" instead of "checkboxes"
- "dropdown" instead of "select list"
- "panel" instead of "section" or "container"
- "submit action" instead of "form submission"
- "rule" instead of "logic" or "condition"

### Reference Fields Clearly

When configuring existing fields, use the @fieldName notation (e.g., "Make @firstName mandatory"). This helps the AI identify exactly which field you're referring to, especially in complex forms with many fields.

**Examples:**

- `Make @email mandatory with real-time validation`
- `Show @spouseInfo panel when @maritalStatus equals "Married"`
- `Set @country default value to "United States"`

### Review Plans Always

Always review plans carefully for changes proposed by the assistant in the Universal Editor before clicking "Apply." The AI will show you what it plans to do - take a moment to verify this matches your expectations.

### Manually Validate

After the assistant makes changes, always preview and test your form to ensure it behaves and looks as expected. AI is a powerful tool, but final validation is key to ensuring quality.

**Validation Checklist:**

- Test form functionality in preview mode
- Verify conditional logic works correctly
- Check mobile responsiveness
- Test form submission
- Validate accessibility features

### Iterate and Refine

If the first prompt doesn't yield the exact result, try rephrasing or breaking down the request into smaller steps. The AI learns from context, so providing more specific details often improves results.

**Iteration Example:**

1. First attempt: "Make the form mobile-friendly"
2. Refined: "Optimize form layout for mobile screens under 768px with single-column layout and larger touch targets"

### Provide Feedback

Use the built-in feedback mechanism to help the assistant learn and improve. Your feedback helps make the AI better for everyone.


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

**Step 2 - Add Core Fields:**

```
Add text input fields: @firstName, @lastName, @email, @phone to the personal information panel
```

**Step 3 - Add Validation:**

```
Make @firstName, @lastName, and @email mandatory with real-time validation
```

**Step 4 - Add Account Information:**

```
Create a new panel "Account Information" with @username and @password fields
```

**Step 5 - Enhance Security:**

```
Add password confirmation field @confirmPassword with validation to match @password
```

**Step 6 - Add Preferences:**

```
Create "Preferences" panel with @newsletter checkbox and @communicationMethod radio group (Email, SMS, Phone)
```

This incremental approach helps you:

- Catch issues early before they compound
- Test each feature thoroughly
- Make adjustments based on user feedback
- Maintain better control over the development process

## Starting New Forms

**When to use:** At the beginning of any form project. This prompt helps the AI understand your requirements and build the foundation structure.

**How to use:** Start with basic structure and core requirements. Specify the form type, target audience, and primary purpose. Add complexity in subsequent prompts.

**Example Prompt - Starting Simple:**

```
Create a **customer onboarding form** for new bank account applications with:

**Purpose:** Collect personal information for account setup
**Target Users:** New customers applying for checking/savings accounts
**Basic Structure:** Single panel with essential fields
**Core Fields:** Name, email, phone, account type selection

Start with a simple layout that we can enhance step by step.
```

**Then Build Incrementally:**

```
Add an address panel to @customerOnboardingForm with street address, city, state, and zip code fields
```

```
Add employment information panel with @employer, @jobTitle, and @annualIncome fields
```

```
Add file upload field @identityDocuments for identity verification (Accept: .pdf,.jpg,.png)
```

**Alternative Simple Starting Prompts:**

```
Create a basic **event registration form** with name, email, and event selection fields
```

```
Build a simple **contact form** with name, email, and message fields
```

```
Design a basic **feedback survey** with rating scale and comments field
```

## Form Structure & Layout

**When to use:** When you need to organize complex forms or improve user experience through better layout design.

**How to use:** Focus on the user journey and logical grouping of information. Specify layout preferences and navigation patterns.

**Example Prompt - Multi-Step Form Structure:**

```
Convert this single-page form into a **3-step wizard** with:

**Step 1: Personal Information**
- Name, email, phone, address fields
- Progress indicator showing "Step 1 of 3"
- "Next" button (validate mandatory fields before proceeding)

**Step 2: Preferences & Requirements** 
- Service selection (checkbox group)
- Budget range (dropdown)
- Timeline preferences (radio group)
- Special requirements (text input field)

**Step 3: Review & Submit**
- Summary of all entered information
- Edit links to go back to specific steps
- Terms and conditions checkbox
- Submit button with confirmation

Include "Previous" and "Next" buttons, allow users to jump between completed steps, save progress automatically.
```

**Layout Optimization Prompts:**

```
Reorganize this form using a **wizard layout** for desktop and single column for mobile. 
```

```
Convert this long form into an **accordion layout** where users can expand/collapse sections.
```

```
Create a **vertical tabbed interface** for this form with tabs for: Basic Info, Contact Details, Preferences, and Review.
```

## Field Management & Validation

**When to use:** When you need to add, modify, or enhance form fields with specific validation rules and behaviors.

**How to use:** Be specific about field types, validation requirements, and user experience expectations. Reference existing fields using @fieldName syntax.

**Example Prompt - Field Enhancement:**

```
Enhance the form fields with these specific requirements:

**Email Field (@email):**
- Make mandatory with real-time validation
- Show green checkmark when valid format entered
- Display helpful error message: "Please enter a valid email address"
- Add placeholder: "your.email@company.com"

**Phone Number (@phone):**
- Type: tel for mobile optimization
- Make mandatory for business customers, optional for personal
- Add placeholder: "Enter your phone number"

**Date of Birth (@dateOfBirth):**
- Type: date with date picker
- Validate age is 18+ for account opening
- Show error if under 18: "Must be 18 or older to open account"

**File Upload (@documents):**
- Accept: .pdf,.doc,.docx
- Multiple: true for multiple document upload
- Show upload progress and file names after upload
```

**Field-Specific Prompts:**

```
Add a **file upload field** for resume with these specs: Accept only PDF/DOC/DOCX files, allow multiple files, show upload progress, display file names after upload.
```

```
Create a **dropdown field** for country selection with all countries listed. Set default value based on user's location if available.
```

```
Build a **repeatable panel** for work experience where users can add/remove multiple jobs. Each entry needs: company, title, start date, end date, description.
```

## Conditional Logic & Rules

**When to use:** When you need dynamic form behavior based on user input or business rules.

**How to use:** Clearly define the conditions and resulting actions. Use specific field references and logical operators.

**Example Prompt - Complex Conditional Logic:**

```
Implement these conditional rules for the application form:

**Business vs Personal Account Logic:**
- If @accountType equals "Business", show:
  - Business name field (mandatory)
  - Tax ID field (mandatory)
  - Business address section
  - Number of employees dropdown
- If @accountType equals "Personal", hide all business fields

**Income-Based Requirements:**
- If @annualIncome is less than 25000:
  - Show additional verification section
  - Make co-signer information mandatory
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
Create a **visibility rule** that shows @spouseInformation panel only when @maritalStatus equals "Married" or "Domestic Partnership".
```

```
Add **progressive disclosure** where additional questions appear based on previous answers. Start with basic info, then show relevant follow-ups.
```

```
Implement **smart defaults** where @country selection auto-sets related fields. Allow manual override.
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

**Example Prompt - Advanced Multi-Channel Submission:**

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
Connect this form to **CRM system** to create new leads. Map @firstName to FirstName, @email to Email, set LeadSource to "Web Form", and Status to "New".
```

```
Set up **workflow trigger** when form is submitted. Pass all form data and trigger approval workflow with manager notification.
```

```
Configure **database integration** to save form submissions as records. Create new folder for each submission with uploaded documents.
```

## Design Import & Conversion

**When to use:** When you have existing form designs (PDF, Figma, images) that need to be converted to functional AEM forms.

**How to use:** Provide clear context about the source design and specify any modifications or enhancements needed.

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

Preserve all original field labels and help text, but improve the user experience with modern form interactions.
```

**Design Import Prompts:**

```
Import this **design mockup** and convert it into an adaptive form. Maintain the exact visual design but add proper validation and mobile responsiveness.
```

```
Analyze this **image of a paper form** and recreate it digitally. Improve the layout for better mobile experience while keeping all mandatory fields.
```

```
Convert this **existing HTML form** to AEM adaptive form format. Preserve all functionality but add AEM-specific features like rules and themes.
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

**Touch Optimization:**
- Larger checkbox and radio button targets
- Swipe gestures for multi-step navigation
- Pull-to-refresh for saved drafts
- Touch-friendly date/time pickers

**Performance:**
- Lazy load non-critical form sections
- Optimize images and icons for mobile
- Minimize JavaScript for faster loading
- Progressive enhancement approach
```

**Mobile-Specific Simple Prompts:**

```
Make @checkoutForm mobile-optimized with large buttons and one-thumb navigation
```

```
Add touch-friendly controls to @surveyForm for tablet users
```

```
Enable offline functionality for @applicationForm with local data saving
```

## Accessibility & Compliance

**When to use:** When forms must meet accessibility standards (WCAG 2.1 AA) or compliance requirements.

**How to use:** Specify accessibility requirements and compliance standards that must be met.

**Example Prompt - Accessibility Implementation:**

```
Make this form **WCAG 2.1 AA compliant** with these accessibility features:

**Keyboard Navigation:**
- Logical tab order through all form elements
- Skip links to main content and form sections
- Keyboard shortcuts for common actions
- Focus indicators clearly visible on all interactive elements

**Screen Reader Support:**
- Proper ARIA labels for all form fields
- Descriptive error messages announced to screen readers
- Form section headings with proper hierarchy (h1, h2, h3)
- Progress announcements for multi-step forms

**Visual Accessibility:**
- Color contrast ratio minimum 4.5:1 for text
- Don't rely solely on color to convey information
- Text size minimum 16px for body text
- Scalable up to 200% without horizontal scrolling

**Motor Accessibility:**
- Large click targets (minimum 44x44px)
- Generous spacing between interactive elements
- No time limits or provide extension options
- Alternative input methods support

**Cognitive Accessibility:**
- Clear, simple language in all instructions
- Consistent navigation and layout patterns
- Error prevention and clear error recovery
- Help text and examples for complex fields

**Testing Requirements:**
- Test with screen readers (NVDA, JAWS, VoiceOver)
- Verify keyboard-only navigation
- Check color contrast with automated tools
- Validate HTML for semantic correctness
```

**Compliance-Specific Prompts:**

```
Ensure this **healthcare form meets HIPAA requirements** with proper data encryption, audit logging, and privacy controls.
```

```
Make this **financial form PCI DSS compliant** with secure payment field handling and data protection measures.
```

```
Create a **government form meeting Section 508 standards** with full accessibility and plain language requirements.
```

## Testing & Quality Assurance

**When to use:** When you need to validate form functionality, user experience, and technical performance.

**How to use:** Specify testing scenarios, edge cases, and quality criteria that must be verified.

**Example Prompt - Comprehensive Form Testing:**

```
Create a **comprehensive testing plan** for this application form:

**Functional Testing:**
- Test all field validations with valid and invalid data
- Verify conditional logic shows/hides fields correctly
- Test file upload with various file types and sizes
- Validate calculation fields update correctly
- Test form submission with complete and incomplete data

**User Experience Testing:**
- Test form completion time (target: under 10 minutes)
- Verify error messages are helpful and actionable
- Test progress saving and restoration
- Validate mobile touch interactions
- Check form accessibility with assistive technologies

**Edge Case Testing:**
- Test with extremely long text inputs
- Verify behavior with special characters and emojis
- Test with slow internet connections
- Validate offline functionality if applicable
- Test browser back/forward button behavior

**Performance Testing:**
- Measure form load time (target: under 3 seconds)
- Test with large file uploads
- Verify memory usage with long form sessions
- Test concurrent user submissions
- Validate database performance under load

**Security Testing:**
- Test input sanitization and XSS prevention
- Verify CSRF protection is working
- Test file upload security restrictions
- Validate data encryption in transit and at rest
- Check authentication and authorization controls

**Cross-Browser Testing:**
- Test on Chrome, Firefox, Safari, Edge
- Verify mobile browsers (iOS Safari, Chrome Mobile)
- Test on different operating systems
- Validate older browser fallbacks
- Check print functionality across browsers
```

**Testing-Specific Prompts:**

```
Create **automated test scripts** for this form's critical user paths: successful submission, validation errors, and conditional logic.
```

```
Design a **user acceptance testing plan** with realistic scenarios and success criteria for business stakeholders.
```

```
Set up **performance monitoring** to track form completion rates, abandonment points, and submission success rates.
```

## Advanced Features & Integrations

**When to use:** When you need sophisticated form capabilities like AI assistance, advanced workflows, or complex integrations.

**How to use:** Clearly define the advanced functionality and integration requirements.

**Example Prompt - AI-Enhanced Form:**

```
Add **AI-powered features** to enhance this application form:

**Smart Auto-Complete:**
- Use AI to suggest company names as user types
- Auto-populate address fields from partial input
- Suggest job titles based on industry selection
- Provide intelligent form completion suggestions

**Dynamic Question Generation:**
- Generate follow-up questions based on previous answers
- Adapt form complexity to user's experience level
- Show relevant optional fields based on user profile
- Personalize form sections for different user types

**Intelligent Validation:**
- Use AI to detect potentially incorrect information
- Suggest corrections for common data entry errors
- Validate business information against public databases
- Flag suspicious or inconsistent responses

**Content Optimization:**
- A/B test different form layouts automatically
- Optimize field order based on completion patterns
- Adjust form length based on user engagement
- Personalize help text based on user behavior

**Predictive Analytics:**
- Predict likelihood of form completion
- Identify users who might need assistance
- Suggest optimal times for form completion reminders
- Analyze drop-off points and suggest improvements

**Natural Language Processing:**
- Allow voice input for text fields
- Convert speech to text for accessibility
- Analyze open-text responses for sentiment
- Extract structured data from unstructured input
```

**Advanced Integration Prompts:**

```
Integrate with **CRM system** to pre-populate known customer data, update records in real-time, and trigger automated follow-up sequences.
```

```
Connect to **payment gateway** for secure transaction processing with PCI compliance, fraud detection, and multiple payment methods.
```

```
Implement **blockchain verification** for document authenticity, immutable audit trails, and decentralized identity verification.
```

## Troubleshooting & Optimization

**When to use:** When forms have performance issues, user experience problems, or technical difficulties.

**How to use:** Describe the specific problem and desired outcome clearly.

**Example Prompt - Performance Optimization:**

```
Optimize this form for **better performance and user experience**:

**Current Issues:**
- Form takes 8+ seconds to load on mobile
- Users are abandoning at the address section (60% drop-off)
- File uploads frequently fail or timeout
- Validation errors are confusing users

**Performance Improvements:**
- Implement lazy loading for non-critical form sections
- Optimize images and reduce bundle size
- Add progressive loading indicators
- Cache frequently used data (country lists, etc.)
- Minimize JavaScript execution time

**User Experience Fixes:**
- Simplify the address section with auto-complete
- Add inline validation with helpful error messages
- Implement smart defaults based on user location
- Add progress saving every 30 seconds
- Provide clear instructions for each section

**Technical Optimizations:**
- Implement chunked file uploads with resume capability
- Add client-side validation before server submission
- Optimize database queries for faster responses
- Implement proper error handling and retry logic
- Add comprehensive logging for debugging

**Monitoring & Analytics:**
- Set up form analytics to track user behavior
- Monitor completion rates by section
- Track error rates and types
- Measure performance metrics continuously
- A/B test improvements with real users
```

**Troubleshooting Prompts:**

```
**Debug this form submission error:** Users report getting "500 Internal Server Error" when submitting. Check validation logic, server endpoints, and data formatting.
```

```
**Fix mobile layout issues:** Form fields are overlapping on iPhone screens and submit button is not visible. Ensure proper responsive design.
```

```
**Resolve validation conflicts:** Some users can't submit even with valid data. Review validation rules for conflicts and edge cases.
```

## Environment-Specific Best Practices

### Forms Management UI

**When to use:** For high-level form creation and management tasks.

```
In Forms Management UI, create a new **customer survey template** that can be reused across different departments. Include standard branding, common field types, and configurable sections.
```

### Adaptive Forms Editor

**When to use:** For detailed form configuration and complex rule creation.

```
In the Adaptive Forms Editor, configure **advanced business rules** for this loan application: calculate debt-to-income ratio, determine eligibility, and show appropriate next steps.
```

### Universal Editor

**When to use:** For Edge Delivery Services forms with visual editing.

```
In Universal Editor, create a **responsive contact form** for the company website. Ensure it matches the site design and integrates with the existing content management workflow.
```

## Command Reference Quick Guide

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

## Supported Component Properties Reference

### Universal Properties (All Components)

- **Type**: Component type (text, email, number, tel, date, checkbox, radio, dropdown, file, etc.)
- **Name**: Field identifier for form submission
- **Label**: Display text for the field
- **Description**: Help text for the field
- **Visible**: Boolean for initial visibility
- **Mandatory**: Boolean for required fields

### Input Field Properties

- **Value**: Default/initial value
- **Placeholder**: Hint text for input fields
- **Min**: Minimum value (for numbers/dates)
- **Max**: Maximum value (for numbers/dates)

### File Upload Properties

- **Accept**: File types (.pdf, .doc, .docx, .jpg, .png, etc.)
- **Multiple**: Boolean for multiple file selection

### Selection Control Properties

- **Options**: Choices for dropdowns (comma-separated list)
- **Checked**: Default selection for checkboxes/radio

### Container Properties

- **Fieldset**: Grouping related fields
- **Repeatable**: Boolean for repeatable sections

### Advanced Properties

- **Visible Expression**: Formula for conditional visibility (=formula)
- **Value Expression**: Formula for calculated values (=formula)

## Best Practices Summary

### Technical Guidelines

- **Use only supported properties** from the official AEM Forms component specification
- **Follow proper syntax** for field references (@fieldName) and expressions (=formula)
- **Test incrementally** after each change to catch issues early
- **Plan for accessibility** from the beginning, not as an afterthought
- **Consider mobile users** in every design decision
- **Document complex rules** for future maintenance and team collaboration

### Strategic Approach

- **Start with user needs** - Focus on what users need to accomplish, not just technical features
- **Design for completion** - Minimize friction and cognitive load in form design
- **Plan data flow** early - Consider how data will be processed, stored, and used
- **Build for scale** - Design forms that can handle expected user volume and data growth
- **Implement progressive enhancement** - Ensure basic functionality works, then add advanced features

### Common Pitfalls to Avoid

- **Overly complex initial requests** - Break large tasks into smaller, manageable steps
- **Using unsupported properties** not in the AEM Forms specification
- **Ignoring mobile experience** until late in the development process
- **Skipping user testing** with real scenarios and edge cases
- **Assuming AI understands context** without providing clear, specific instructions
- **Forgetting about accessibility** and compliance requirements
- **Not validating changes** before moving to the next step

### Quality Assurance Approach

1. **Preview frequently** - Check your work in preview mode after each significant change
2. **Test edge cases** - Try unusual inputs, long text, special characters
3. **Validate across devices** - Test on mobile, tablet, and desktop
4. **Check accessibility** - Verify keyboard navigation and screen reader compatibility
5. **Performance test** - Ensure forms load quickly and respond smoothly
6. **User acceptance testing** - Have real users test the form before deployment


*This prompt library is continuously updated based on user feedback and new AI Assistant capabilities. For the latest features and examples, check the [AEM Forms documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/home.html).* 
