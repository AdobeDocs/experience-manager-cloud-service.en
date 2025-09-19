---
title: Form submission and integration
description: Learn how to configure form submissions and integrate Forms Experience Builder forms with external systems, APIs, and business workflows.
feature: Edge Delivery Services
hide: yes
index: no
hidefromtoc: yes
role: Admin, Architect, Developer
---

# Form submission and integration

>[!NOTE]
>
> The Forms Experience Builder is available under an early access program. Before you begin, please ensure you have requested and been granted access.

Forms Experience Builder provides powerful integration capabilities to connect your forms with external systems, APIs, and business workflows. This guide covers how to configure form submissions and set up various integration scenarios.

## Submission configuration options

### Email submissions

Configure forms to send submissions via email:

**Basic email setup:**

- Set recipient email addresses
- Configure email templates
- Add CC and BCC recipients
- Set up email notifications

**Advanced email features:**

- Dynamic recipient selection
- Email templates with form data
- Attachment handling
- Email delivery confirmation

### REST API integration

Connect forms to external APIs and services:

**API endpoint configuration:**

- Set REST API URLs
- Configure authentication methods
- Set request headers and parameters
- Handle response data

**Data mapping:**

- Map form fields to API parameters
- Transform data formats
- Handle nested JSON structures
- Manage error responses

### Cloud storage integration

Store form submissions in cloud storage services:

**Supported platforms:**

- Microsoft Azure Blob Storage
- Amazon S3
- Google Cloud Storage
- SharePoint Online

**Configuration options:**

- Set storage credentials
- Configure folder structures
- Set file naming conventions
- Manage access permissions

### Workflow integration

Connect forms to business process workflows:

**Microsoft Power Automate:**

- Trigger workflows on form submission
- Pass form data to workflow steps
- Handle workflow responses
- Manage approval processes

**Adobe Workflow:**

- Integrate with AEM Workflow
- Set up approval chains
- Configure notification steps
- Manage document processing

## Setting up form submissions

### Step 1: Access submission configuration

1. Open your form in Forms Experience Builder
2. Navigate to the submission settings
3. Select "Configure Form Submission"
4. Choose your integration type

### Step 2: Configure email submissions

**Basic email setup:**

    Configure email submission to hr@company.com with:
    - Subject: "New Employee Application"
    - Include form data in email body
    - Send confirmation to applicant

**Advanced email configuration:**

    Set up dynamic email routing:
    - If department equals "IT", send to it-hr@company.com
    - If department equals "Sales", send to sales-hr@company.com
    - Default to hr@company.com

### Step 3: Set up API integration

**REST API configuration:**

    Submit form data to REST endpoint:
    - URL: https://api.company.com/forms/submit
    - Method: POST
    - Authentication: Bearer token
    - Content-Type: application/json

**Data mapping example:**

    Map form fields to API:
    - firstName -> user.first_name
    - lastName -> user.last_name
    - email -> user.email_address
    - department -> user.department_id

### Step 4: Configure cloud storage

**Azure Blob Storage setup:**

    Store form submissions in Azure:
    - Container: form-submissions
    - Folder: /{year}/{month}/{day}/
    - File format: JSON with attachments
    - Access level: Private

## Integration examples

### Customer feedback form

**Submission configuration:**

- Email notification to support team
- Store data in CRM system via API
- Create support ticket automatically
- Send confirmation email to customer

**Implementation:**
    Submit customer feedback form to:
    1. Email <support@company.com> with form details
    2. POST to CRM API to create customer record
    3. Trigger support ticket creation workflow
    4. Send thank you email to customer

### Employee onboarding form

**Submission configuration:**

- Email HR team with new hire information
- Store documents in SharePoint
- Trigger onboarding workflow
- Create user accounts in various systems

**Implementation:**
    Process employee onboarding:
    1. Email <hr@company.com> with employee details
    2. Upload documents to SharePoint employee folder
    3. Start onboarding workflow in Power Automate
    4. Create accounts in HR system, email, and other tools

### Lead generation form

**Submission configuration:**

- Store lead data in marketing automation platform
- Send notification to sales team
- Add lead to CRM system
- Trigger follow-up email sequence

**Implementation:**
    Process lead generation:
    1. POST lead data to Marketo API
    2. Create lead record in Salesforce
    3. Email sales team with lead details
    4. Start automated email nurture sequence

## Advanced integration scenarios

### Multi-step form processing

**Complex workflow integration:**

- Validate form data against external systems
- Process payments through payment gateways
- Generate documents and contracts
- Send notifications to multiple stakeholders

### Real-time data validation

**API-based validation:**

- Validate email addresses against company directory
- Check product availability in inventory system
- Verify customer information in CRM
- Validate payment information

### Conditional submission routing

**Dynamic routing based on form data:**

- Route to different departments based on inquiry type
- Send to different systems based on customer tier
- Process differently based on form completion status
- Handle different business rules per region

## Security and compliance

### Data protection

**Encryption and security:**

- Encrypt sensitive data in transit
- Secure API credentials and tokens
- Implement proper access controls
- Follow data retention policies

### Compliance requirements

**GDPR and privacy:**

- Implement consent management
- Provide data export capabilities
- Enable data deletion requests
- Maintain audit trails

**Industry standards:**

- HIPAA compliance for healthcare forms
- PCI DSS for payment processing
- SOX compliance for financial forms
- Industry-specific regulations

## Testing and validation

### Submission testing

**Test scenarios:**

- Verify email delivery and formatting
- Test API connectivity and data mapping
- Validate cloud storage uploads
- Check workflow trigger functionality

**Error handling:**

- Test network failure scenarios
- Validate error message display
- Check retry mechanisms
- Verify fallback options

### Performance optimization

**Optimization strategies:**

- Implement asynchronous processing
- Use batch operations for bulk data
- Optimize API call frequency
- Cache frequently accessed data

## Troubleshooting integration issues

### Common problems

**Email delivery issues:**

- Check SMTP server configuration
- Verify recipient email addresses
- Review spam filter settings
- Test email template formatting

**API integration problems:**

- Verify API endpoint URLs
- Check authentication credentials
- Validate request format and headers
- Review API response handling

**Storage integration issues:**

- Confirm storage credentials
- Check folder permissions
- Verify file upload limits
- Test network connectivity

### Getting help

For integration issues:

- Check the [Forms Experience Builder FAQ](forms-experience-builder-frequently-asked-questions.md)
- Review the [Getting Started guide](forms-experience-builder-getting-started.md)
- Contact your system administrator for technical assistance
- Consult API documentation for external services

## Related articles

- [Forms Experience Builder Overview](product-overview.md)
- [Getting started with Forms Experience Builder](forms-experience-builder-getting-started.md)
- [Deploy and configure Forms Experience Builder](deploy-forms-experience-builder.md)
- [Intelligent import and conversion](intelligent-import-conversion.md)
- [Frequently asked questions](forms-experience-builder-frequently-asked-questions.md)
