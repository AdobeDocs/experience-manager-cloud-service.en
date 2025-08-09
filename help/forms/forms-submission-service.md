---
title: Forms Submission Service for Edge Delivery Services
description: Store form submissions directly in spreadsheets using Adobe's hosted Forms Submission Service. Learn setup, configuration, and API usage for Google Sheets, OneDrive, and SharePoint integration.
keywords: Forms Submission Service, Edge Delivery Services forms, spreadsheet integration, Google Sheets forms, OneDrive forms, SharePoint forms, form data collection
feature: Edge Delivery Services
role: User, Developer, Admin
level: Beginner, Intermediate
hide: yes
hidefromtoc: yes
exl-id: 12b4edba-b7a1-4432-a299-2f59b703d583
---
# Forms Submission Service for Edge Delivery Services

The Forms Submission Service is Adobe's hosted solution that automatically stores form submission data directly in your preferred spreadsheets—Google Sheets, Microsoft OneDrive, or SharePoint. This eliminates the need for complex backend infrastructure while providing real-time data collection and management.



## Overview

![Forms submission service](/help/forms/assets/form-submission-service.png)
*Figure: Forms Submission Service workflow - from form submission to spreadsheet storage*

+++ Who Should Use This Service?

**Perfect for:**

- **Content creators** building simple data collection forms
- **Small businesses** needing quick form-to-spreadsheet workflows  
- **Marketing teams** collecting lead information
- **Event organizers** managing registrations

**Consider alternatives for:**

- Complex workflows requiring custom logic
- Enterprise integrations with databases
- Forms needing advanced validation or processing

+++

+++ Common Use Cases

| Use Case | Example | Spreadsheet Benefit |
|----------|---------|-------------------|
| **Contact Forms** | Website inquiries → Google Sheets | Easy follow-up and CRM import |
| **Event Registration** | Conference signups → Excel Online | Real-time attendee tracking |
| **Lead Generation** | Newsletter signups → SharePoint | Marketing campaign analysis |
| **Feedback Collection** | Survey responses → Google Sheets | Quick data visualization |

+++

## Key Benefits

The Forms Submission Service offers several advantages for streamlined data collection:



+++ Simplified Setup

- **No backend infrastructure** required - Adobe hosts the submission endpoint
- **Direct integration** with popular spreadsheet platforms
- **Automatic data mapping** from form fields to spreadsheet columns

+++


+++ Real-Time Data Management

- **Instant data capture** - submissions appear immediately in your spreadsheet
- **Structured storage** - organized columns for easy analysis
- **Live collaboration** - multiple team members can access and analyze data

+++

+++ Built-in Security & Access Control

- **Leverages existing permissions** - use your spreadsheet platform's sharing controls
- **Adobe-managed security** - secure submission endpoint with enterprise-grade protection
- **Data ownership** - your data stays in your chosen spreadsheet platform

+++

## Prerequisites

Before setting up the Forms Submission Service, ensure you have:



+++ Technical Requirements

- **GitHub repository** set up for your Edge Delivery Services project with the latest Adaptive Forms Block installed
- **Access approval** - repository added to the allowlist

+++

+++ Spreadsheet Platform Setup


Choose one of the supported platforms:

- **Google Sheets** - Google account with sheet creation permissions
- **Microsoft OneDrive** - Microsoft 365 account with Excel Online access
- **SharePoint** - SharePoint access with list/library permissions

+++

+++ Permissions & Access

- **Edit permissions** for the target spreadsheet
- **Sharing capabilities** to grant access to `forms@adobe.com`
- **Link generation** permissions for your chosen platform

+++

>[!TIP]
>
>**New to Edge Delivery Services?** Start with the [Getting Started Tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/tutorial) to set up your project foundation. 

## Configuration Methods

The Forms Submission Service offers two configuration approaches. Choose the method that best fits your workflow:


+++ Choose Your Configuration Method

| Method | Best For | Time Required | Technical Level |
|--------|----------|---------------|-----------------|
| **[Manual Setup](#manual-configuration)** | Content creators, one-time setup | 10-15 minutes | Beginner |
| **[API Configuration](#api-configuration)** | Developers, automated workflows | 5-10 minutes | Intermediate |

+++

+++ Project Setup

Before configuring either method, ensure your AEM project foundation is ready:

1. **Create or update your AEM project** with the latest Adaptive Forms Block ([Getting Started Tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/tutorial))

2. **Update `fstab.yaml`** in your project root:

   ```yaml
   # Replace with the path to your shared folder
   mountpoints:
     /: https://drive.google.com/drive/folders/your-shared-folder-id
   ```


3. **Share your project folder** with `forms@adobe.com` (edit permissions required)

+++

## Manual Configuration

![Workflow for forms submission service](/help/forms/assets/forms-submission-service-workflow.png)
*Figure: Complete workflow for manual Forms Submission Service setup*

Follow these step-by-step instructions to set up your form with spreadsheet submission:



+++ Step 1: Create Your Form Definition

Create your form structure using Google Sheets or Microsoft Excel.

**Form Creation Steps:**

1. **Open your spreadsheet platform** (Google Sheets or Microsoft Excel)
2. **Create a new spreadsheet** for your form project
3. **Name your sheet** (must be either `helix-default` or `shared-aem`)
4. **Define your form structure** using the [form creation guide](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/create-forms)

![Form Definition](/help/forms/assets/form-submission-definition.png)
*Example: Form definition with field types, labels, and validation rules*

>[!IMPORTANT]
>
>**Sheet Naming Requirements**
>
>Your form definition sheet must be named either:
>
>- `helix-default` (recommended for single forms)
>- `shared-aem` (for multi-form projects)
>
>Other sheet names will not be recognized by the system.

**Validation Checkpoint:**

- Form structure is complete with all required fields
- Sheet is named correctly (`helix-default` or `shared-aem`)
- Field types and validation rules are properly configured

+++

+++ Step 2: Create the Data Collection Sheet

Set up a dedicated sheet to receive form submission data.

**Data Sheet Setup:**

1. **Add a new sheet** to your existing spreadsheet
2. **Name the sheet exactly `incoming`** (case-sensitive)
3. **Set up column headers** that match your form fields
4. **Save the spreadsheet** to ensure changes are preserved

![Incoming sheet](/help/forms/assets/form-submission-incoming-sheet.png)
*Example: Incoming sheet with column headers matching form fields*

>[!WARNING] 
>
>**Critical Requirement**
>
>The sheet must be named exactly `incoming` (lowercase). Without this sheet:
>
>- Form submissions will be rejected
>- No data will be stored
>- Users will see submission errors

**Validation Checkpoint:**

- `incoming` sheet exists in your spreadsheet
- Column headers match your form field names
- Sheet is properly saved and accessible

>[!TIP]
>
>**Pro Tip:** Copy the exact field names from your form definition to ensure perfect matching between form fields and spreadsheet columns.

+++

+++ Step 3: Share Spreadsheet with Adobe Service

Grant the Adobe Forms Submission Service access to your spreadsheet.

**Sharing Process:**

1. **Click the Share button** in the top-right corner of your spreadsheet
2. **Add the Adobe service account:**
   - Email: `forms@adobe.com`
   - Permission level: **Editor** (required for data writing)
3. **Send the sharing invitation**
4. **Copy the spreadsheet link** for the next step

    ![Share incoming sheet](/help/forms/assets/form-submission-share-incoming.png)
*Step-by-step sharing process for granting Adobe service access*

**Platform-Specific Instructions:**

**Google Sheets:**

- Add `forms@adobe.com` as Editor
- Ensure "Anyone with the link can view" is enabled
- Copy the shareable link

**Microsoft Excel (OneDrive/SharePoint):**

- Add `forms@adobe.com` with Edit permissions
- Set link sharing to "Anyone with the link can edit"
- Copy the sharing URL

    ![Copy link of incoming sheet](/help/forms/assets/form-submission-copy-link.png)
*Example: Copying the shareable link for form configuration*

**Validation Checkpoint:**

- `forms@adobe.com` has Editor access to your spreadsheet
- Spreadsheet link is copied and ready for use
- Sharing permissions allow external access

+++

+++ Step 4: Connect Form to Spreadsheet

Link your form definition to the submission spreadsheet.

**Form-Spreadsheet Connection:**

1. **Open your form definition spreadsheet** (the one with `helix-default` or `shared-aem` sheet)
2. **Locate the Submit field row** in your form definition
3. **Paste the copied spreadsheet link** into the **Action** column for the Submit field
4. **Save the changes** to your form definition

    ![Link a spreadsheet](/help/forms/assets/form-submission-sheet-linking.png)
*Example: Connecting the submit action to your data collection spreadsheet*

**Publishing Your Form:**

1. **Open AEM Sidekick** in your browser
2. **Preview your form** to test the configuration
3. **Publish the form** to make it live

**Final Validation:**

- Spreadsheet link is correctly added to Submit field action
- Form definition is saved and published
- Form preview shows all fields correctly
- Submit button is properly configured

>[!SUCCESS]
>
>**Setup Complete!** Your form is now connected to the Forms Submission Service. Test it by submitting sample data and checking your `incoming` sheet.

**Reference Materials:**

- [Complete example spreadsheet](/help/forms/assets/spreadsheet.xlsx) with proper configuration
- [AEM Sidekick documentation](https://www.aem.live/docs/sidekick) for publishing guidance

+++

## API Configuration

The API method allows developers to programmatically submit data to the Forms Submission Service, ideal for automated workflows and custom integrations.


+++ When to Use the API

**Perfect for:**

- Automated data collection systems
- Custom form implementations
- Integration with existing applications
- Bulk data submission workflows

+++

+++ API Prerequisites

Before using the API, ensure you have:

- **Spreadsheet setup** completed (including `incoming` sheet)
- **Adobe service access** granted to `forms@adobe.com`
- **Form ID** from your published form
- **Repository information** (organization and site name)

>[!IMPORTANT]
>
>**Required Setup Steps**
>
>The API requires the same spreadsheet setup as manual configuration:
>
>- `incoming` sheet must exist
>- `forms@adobe.com` must have Editor access
>- Sheet must be published via AEM Sidekick

+++

+++ API Endpoint & Authentication

**Base URL:** `https://forms.adobe.com/adobe/forms/af/submit/{id}`

**Required Headers:**

- `Content-Type: application/json`
- `x-adobe-routing: tier=live,bucket=main--[repository]--[organization]`

**API Documentation:** [Complete API Reference](https://adobedocs.github.io/experience-manager-forms-cloud-service-developer-reference/references/aem-forms-submission-service/)

+++

+++ Using Postman

Postman provides a user-friendly interface for testing API submissions.

**Setup Instructions:**

1. **Create a new POST request** in Postman
2. **Configure the endpoint:** `https://forms.adobe.com/adobe/forms/af/submit/{id}`
3. **Replace placeholders:**
   - `{id}` → Your actual Form ID
   - `[repository]` → Your GitHub repository name
   - `[organization]` → Your GitHub organization/username

**Request Configuration:**
   
    ```json
POST https://forms.adobe.com/adobe/forms/af/submit/your-form-id

Headers:
Content-Type: application/json
x-adobe-routing: tier=live,bucket=main--your-repo--your-org

Body (JSON):
{
        "data": {
            "startDate": "2025-01-10",
            "endDate": "2025-01-25",
            "destination": "Australia",
            "class": "First Class",
            "budget": "2000",
            "amount": "1000000",
            "name": "Mary",
            "age": "35",
            "subscribe": null,
            "email": "mary@gmail.com"
                }
}
     ```

**Expected Response:**

- **Status Code:** `201 Created`
- **Data appears** in your `incoming` spreadsheet sheet immediately

![postman screen](/help/forms/assets/postman-api.png)
*Example: Successful API submission using Postman interface*

+++

+++ Using Command Line (curl)

For developers who prefer terminal/command prompt, use curl to submit data programmatically.

**Command Line Setup:**

Replace the following placeholders in the commands below:

- `{id}` → Your actual Form ID  
- `[repository]` → Your GitHub repository name
- `[organization]` → Your GitHub organization/username

>[!BEGINTABS]

>[!TAB macOS/Linux]

```bash
curl -X POST "https://forms.adobe.com/adobe/forms/af/submit/your-form-id" \
    --header "Content-Type: application/json" \
  --header "x-adobe-routing: tier=live,bucket=main--your-repo--your-org" \
    --data '{
        "data": {
            "startDate": "2025-01-10",
            "endDate": "2025-01-25",
            "destination": "Australia",
            "class": "First Class",
            "budget": "2000",
            "amount": "1000000",
            "name": "Joe",
            "age": "35",
            "subscribe": null,
      "email": "joe@example.com"
                }
            }'
        ```

>[!TAB Windows Command Prompt]
     
```cmd
curl -X POST "https://forms.adobe.com/adobe/forms/af/submit/your-form-id" ^
    --header "Content-Type: application/json" ^
  --header "x-adobe-routing: tier=live,bucket=main--your-repo--your-org" ^
  --data "{\"data\": {\"startDate\": \"2025-01-10\", \"endDate\": \"2025-01-25\", \"destination\": \"Australia\", \"class\": \"First Class\", \"budget\": \"2000\", \"amount\": \"1000000\", \"name\": \"Joe\", \"age\": \"35\", \"subscribe\": null, \"email\": \"joe@example.com\"}}"
```

>[!TAB Windows PowerShell]

```powershell
$body = @{
  data = @{
    startDate = "2025-01-10"
    endDate = "2025-01-25"
    destination = "Australia"
    class = "First Class"
    budget = "2000"
    amount = "1000000"
    name = "Joe"
    age = "35"
    subscribe = $null
    email = "joe@example.com"
  }
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Uri "https://forms.adobe.com/adobe/forms/af/submit/your-form-id" `
  -Method POST `
  -Headers @{"Content-Type"="application/json"; "x-adobe-routing"="tier=live,bucket=main--your-repo--your-org"} `
  -Body $body
    ```

>[!ENDTABS]

+++

+++ API Response & Verification

**Successful Response:**

```http
HTTP/1.1 201 Created
Connection: keep-alive
Content-Length: 0
X-Request-Id: 02a53839-2340-56a5-b238-67c23ec28f9f
X-Message-Id: 42ecb4dd-b63a-4674-8f1a-05a4a5b0372c
Date: Fri, 10 Jan 2025 13:06:10 GMT
Access-Control-Allow-Origin: *
```

**Data Verification:**

After a successful submission, verify the data appears in your spreadsheet:

![updated sheet](/help/forms/assets/updated-sheet.png)
*Example: Data successfully written to the incoming sheet via API*

**Response Validation:**

- **HTTP Status:** `201 Created` indicates successful submission
- **X-Request-Id:** Unique identifier for tracking the submission
- **Data appears** in your `incoming` sheet within seconds
- **All form fields** are properly mapped to spreadsheet columns

+++

## Troubleshooting



+++ Common Issues & Solutions

**Problem: 403 Forbidden Error**

```
Causes: Missing or incorrect access permissions
Solutions:
- Verify forms@adobe.com has Editor access to your spreadsheet
- Check that your repository is added to the allowlist
- Confirm the x-adobe-routing header format
```

**Problem: 404 Not Found Error**

```
Causes: Incorrect Form ID or endpoint URL
Solutions:  
- Verify your Form ID is correct
- Check the API endpoint URL format
- Ensure your form is published and live
```


**Problem: Data Not Appearing in Spreadsheet**

```
Causes: Missing 'incoming' sheet or permission issues
Solutions:
- Confirm 'incoming' sheet exists (case-sensitive)
- Verify column headers match form field names exactly
- Check forms@adobe.com has edit permissions
- Ensure spreadsheet is shared properly
```


**Problem: Invalid JSON Format Error**  

```
Causes: Malformed request body
Solutions:
- Validate JSON syntax using online JSON validators
- Ensure proper escaping of special characters
- Check quote marks and brackets are balanced
```


+++

+++ Getting Help

**Support Channels:**

- **Early Access Issues:** Email [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com)
- **API Documentation:** [Developer Reference](https://adobedocs.github.io/experience-manager-forms-cloud-service-developer-reference/references/aem-forms-submission-service/)
- **Community Support:** [Adobe Experience League Community](https://experienceleaguecommunities.adobe.com/)

+++

## Next Steps

Now that you have the Forms Submission Service configured, explore these related topics:


+++ Enhance Your Forms

- **[Create Advanced Forms](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/getting-started-edge-delivery-services-forms/create-forms)** - Add validation, conditional logic, and custom styling
- **[Form Components Guide](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/build-forms/forms-components)** - Explore available form field types

+++

+++ Alternative Submission Methods

- **[AEM Publish Submissions](/help/edge/docs/forms/configure-submission-action-for-eds-forms.md)** - For complex workflows and enterprise integrations
- **[Custom Submit Actions](/help/forms/configure-submit-actions-core-components.md)** - Advanced submission handling

+++

+++ Data Management

- **[Form Analytics](/help/forms/view-understand-aem-forms-analytics-reports.md)** - Track form performance and usage
- **[Data Integration](/help/forms/configure-data-sources.md)** - Connect forms to databases and CRM systems

+++

## Summary

The Forms Submission Service provides a powerful, no-code solution for collecting form data directly into spreadsheets. Key benefits include:

- **Quick setup** - No backend infrastructure required
- **Real-time data** - Immediate submission capture  
- **Flexible platforms** - Google Sheets, OneDrive, or SharePoint
- **API access** - Programmatic submission capabilities
- **Enterprise security** - Adobe-managed endpoints with access controls

**Ready to get started?** Follow the [manual configuration](#manual-configuration) guide for a visual setup, or jump to [API configuration](#api-configuration) for programmatic integration.
