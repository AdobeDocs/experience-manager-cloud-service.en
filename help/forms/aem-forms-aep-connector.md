---
title: Connect AEM Forms with Adobe Experience Platform (AEP) | Data Integration Guide
description: Learn how to integrate AEM Forms with Adobe Experience Platform to leverage customer profiles, submit form data, and create personalized experiences. Step-by-step guide.
contentOwner: Khushwant Singh
docset: CloudService
role: Admin, Developer, User
feature: Adaptive Forms, Core Components
exl-id: b0eb19d3-0297-4583-8471-edbb7257ded4
---
# AEM Forms Integration with Adobe Experience Platform (AEP) {#aem-forms-aep-integration}

<span class="preview"> The capability to connect Adaptive Forms (AEM Forms) with Adobe Experience Platform (AEP) is under the early access program. To request access to the capability, simply send an email from your official address to [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com?subject=Request%20for%20Early%20Access%20to%20AEP%20Connector%20\(AEM%20Forms%20Integration%20with%20Adobe%20Experience%20Platform\)&body=Dear%20AEM%20Forms%20Team%2C%0D%0A%0D%0AI%20hope%20this%20message%20finds%20you%20well.%0D%0A%0D%0AI%20am%20writing%20to%20request%20access%20to%20the%20Early%20Access%20Program%20for%20the%20AEP%20Connector%2C%20which%20enables%20integration%20between%20AEM%20Forms%20and%20Adobe%20Experience%20Platform.%0D%0A%0D%0AOrganization%20Name%3A%20%5BYour%20organization%20name%5D%0D%0AOrganization%20ID%3A%20%5BYour%20organization%20ID%2C%20if%20available%5D%0D%0AUse%20Case%3A%20%5BBriefly%20describe%20your%20intended%20use%20case%2C%20including%20goals%20or%20benefits%20you%20aim%20to%20achieve%20with%20the%20integration%5D%0D%0A%0D%0AThank%20you%20for%20your%20time%20and%20consideration.%0D%0A%0D%0ABest%20regards%2C%0D%0A%5BYour%20Full%20Name%5D%0D%0A%5BYour%20Job%20Title%2C%20if%20applicable%5D%0D%0A%5BYour%20Contact%20Information%2C%20if%20appropriate%5D). You can also visit the <a href="/help/forms/early-access-ea-features.md">Early Access Program </a>page to discover all the available innovations and capabilities. . </span>

## Overview {#overview}

You can connect AEM Forms with Adobe Experience Platform to transform your form experiences. This powerful integration enables organizations to leverage real-time customer profiles for personalized form experiences, streamline **AEM Forms data submission to Experience Platform**, and create unified customer records across the Adobe ecosystem. By connecting your adaptive forms with Experience Platform's robust data management capabilities, you can create more relevant experiences and improve conversion rates while maintaining a single source of truth for customer data.

### What is AEM Forms Connector for Adobe Experience Platform (AEP)? {#what-is-connector}

The AEM Forms Connector for Adobe Experience Platform (AEP) is an out of the box (OOTB) connector provided by AEM Forms that enables seamless integration between AEM Forms and Adobe Experience Platform (AEP). This integration allows you to create forms using XDM schemas available in AEP and submit data back to AEP for personalization and profile hydration purposes.

## Why connect AEM Forms with Adobe Experience Platform (AEP)? {#benefits}

Connecting your Adaptive Forms with Adobe Experience Platform delivers significant advantages for both your organization and your customers:

* **Unified customer profiles** - Enrich customer profiles with form submission data, creating a comprehensive view of customer interactions and preferences
* **Personalized form experiences** - Leverage existing profile data to pre-populate fields and customize forms based on known customer information
* **Streamlined data collection** - Capture form data directly into AEP datasets without building custom connectors or integration code
* **Real-time data activation** - Send form submission data to other Adobe applications through Real-Time CDP for immediate activation
* **Simplified compliance management** - Manage consent and data governance policies centrally through AEP
* **Reduced development time** - Eliminate custom integration work with a pre-built connector that follows best practices
* **Customer profile enrichment with form data** - Automatically update and enhance customer profiles with every form submission, creating richer customer insights

## Key Features {#key-features}

* Create forms using AEP XDM schemas
* Submit form data to AEP for personalization
* Support for streaming data ingestion
* Enable profile hydration for enhanced user experiences
* Integration with AEP's profile system
* XDM schema integration with adaptive forms for standardized data collection
* AEP streaming connection for forms enabling real-time data processing

The video below gives a step-by-step guide on the prerequisites (like creating a schema, setting up data configuration, and authentication) and shows how to create and connect Adaptive Forms to Adobe Experience Platform (AEP)

>[!VIDEO](https://video.tv.adobe.com/v/3457850/)

## Prerequisites {#prerequisites}

Before setting up the AEP Connector in AEM Forms, ensure you have completed the following in Adobe Experience Platform:

1. Schema Setup
    * [Create an XDM schema](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui)
    * [Enable schema for profiling](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui#profile)
    * [Define identity field](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui#profile)

2. Data Configuration
    * [Create a dataset](https://experienceleague.adobe.com/en/docs/platform-learn/getting-started-for-data-architects-and-data-engineers/create-datasets)
    * [Set up streaming connection](https://experienceleague.adobe.com/en/docs/experience-platform/ingestion/tutorials/create-streaming-connection) (You need the streaming endpoint URL later, so make a note of it now.)

3. Authentication
    * [Generate API credentials](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-authentication#generate-credentials) (Client ID and Client Secret) from Adobe Developer Console


## Implementation Steps

### 1. Create AEP Cloud Configuration

1. Navigate to your **Adobe Experience Manager instance** > **Tools** > **Cloud Services** > **Adobe Experience Platform**.
1. Select a **Configuration Container** to store the configuration.
1. Click **Create** to open the AEP configuration wizard
1. Enter the following details:
    * Title
    * Client ID (obtained from developer console)
    * Client Secret (obtained from developer console)
    * OAuth URL (There is a default URL but it can be obtained from the developer console also) 

1. Click **Connect** to establish the connection. After establishing the connection, configure these additional settings:
    * Base URL: platform.adobe.io (This is a default URL and can be obtained from the developer console also, the oauth and platform URLs are defaulted to prod URLs. In case, you are required to connect to stage - stage URLs should be used.)
    * Organization ID (This is obtained from the developer console along with client ID/secret)
    * Sandbox name (required for both development and production environments)

### 2. Form Creation with XDM Schema Integration {#form-creation}

1. Access the form creation wizard:
    * Navigate to your **Adobe Experience Manager instance** > **Forms** > **Forms & Documents**.
    * Click **Create** > **Adaptive Form**.
1. In the **source** tab, select a template
1. In the **Data** tab, select the **Adobe Experience Platform** option.

1. In the properties pane, select your cloud configuration. The system loads all available schemas from Adobe Experience Platform

    >[!NOTE]
    >
    >
    > * Only profile-enabled and non-system-generated schemas are fetched.
    > * Initial schema loading may take some time on first-time setup.
1. Select the appropriate/required fields of the schema. (See video for detailed steps)
1. In the submission tab:
    * Select the **Submit to Adobe Experience Platform** submit action
    * Configure the form submission settings for **AEM Forms data submission to Experience Platform**
1. In the properties pane:
    * Add the streaming URL (obtained from AEP Sources > Streaming Connection)
    * Add the data flow ID (found in AEP Sources > Flow > API Usage Information)
1. Click **Save**. Provide the form details:
    * Title
    * Name
    * Storage path
1. Add the submit button to the form. Your form is ready to submit data to AEP.


## Important Notes {#important-notes}

* Data submitted through forms becomes visible in AEP after approximately 10-15 minutes
* By default, only profile-enabled schemas are listed
* While data submission works for all schemas, prefill functionality is limited to profile-enabled schemas
* Data in non-profile-enabled schemas won't be used for profile creation, even if the schema is later enabled for profiling
* **Customer profile enrichment with form data** requires proper identity field configuration in your XDM schema
* **AEM Forms data submission to Experience Platform** uses **AEP streaming connection for forms** to ensure real-time data flow

## Best Practices {#best-practices}

1. Plan your schema structure carefully before enabling profiling
1. Consider data volume and system scaling requirements when setting up **AEP streaming connection for forms**
1. Test the integration thoroughly before production deployment
1. Monitor data ingestion and profile creation processes
1. Design your **XDM schema integration with adaptive forms** to collect only necessary data
1. Use **customer profile enrichment with form data** strategically to enhance personalization

## Technical Considerations {#technical-considerations}

* The connector uses public streaming APIs for data submission
* Profile creation is based on the identity field
* Data unification occurs automatically in AEP
* The integration supports both new form creation and existing form modification
* XDM schema integration with adaptive forms standardizes data structure across different touchpoints
* AEP streaming connection for forms provides real-time data ingestion capabilities

## Frequently Asked Questions (FAQ) {#faq}

### General Questions {#general-questions}

**Q: "Is this connector available with multiple offerings of AEM Forms?**
A: No, this integration is only available for AEM Forms as a Cloud Service and is under the Early Access program.

**Q: Does this connector work with both Adaptive Forms Core Components and Foundation Components?**
A: This connector works with both Adaptive Forms Core Components and Adaptive Forms Foundation Components.

**Q: Can I send data to multiple AEP datasets from a single form?**
A: Currently, each form can only submit to one dataset. 

**Q: Is there a limit to how many form submissions can be processed?**
A: Form submissions are subject to your AEP streaming ingestion [quotas and rate limits](https://experienceleague.adobe.com/en/docs/experience-platform/data-lifecycle/api/quota).

<!-- >
**Q: Can form attachments be sent to AEP?**
A: No, form attachments cannot be directly sent to AEP. You would need to store attachments separately and only send metadata to AEP. -->

### Implementation Questions {#implementation-questions}

**Q: How do I troubleshoot connection issues between AEM Forms and AEP?**
A: Verify your cloud configuration settings, ensure API credentials are correct, and check that the streaming endpoint URL is properly configured.

**Q: Can I use custom XDM schemas with this integration?**
A: Yes, you can use any custom XDM schema as long as it's properly configured in AEP and, for prefill functionality, enabled for profiles.

**Q: How do I enable form prefilling with AEP profile data?**
A: Ensure your schema is profile-enabled and your form is configured to use the same identity field that's defined in your schema.

**Q: What if I need to transform data before sending it to AEP?**
A: You can use form rules or custom functions to transform data before submission. For complex transformations, consider using a custom submit action.

**Q: Can I use this integration in a hybrid deployment model?**
A: No, this integration is specific to AEM Forms as a Cloud Service.

## Summary and Next Steps {#summary-next-steps}

The AEM Forms Integration with Adobe Experience Platform enables organizations to create a seamless flow of data between forms and the broader Experience Platform ecosystem. This integration empowers you to build more personalized form experiences, streamline data collection, and enhance customer profiles with valuable form submission data.

To get started with this integration:

1. **Request access** - If you haven't already, join the Early Access program by contacting [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com?subject=Request%20for%20Early%20Access%20to%20AEP%20Connector%20\(AEM%20Forms%20Integration%20with%20Adobe%20Experience%20Platform\)&body=Dear%20AEM%20Forms%20Team%2C%0D%0A%0D%0AI%20hope%20this%20message%20finds%20you%20well.%0D%0A%0D%0AI%20am%20writing%20to%20request%20access%20to%20the%20Early%20Access%20Program%20for%20the%20AEP%20Connector%2C%20which%20enables%20integration%20between%20AEM%20Forms%20and%20Adobe%20Experience%20Platform.%0D%0A%0D%0AOrganization%20Name%3A%20%5BYour%20organization%20name%5D%0D%0AOrganization%20ID%3A%20%5BYour%20organization%20ID%2C%20if%20available%5D%0D%0AUse%20Case%3A%20%5BBriefly%20describe%20your%20intended%20use%20case%2C%20including%20goals%20or%20benefits%20you%20aim%20to%20achieve%20with%20the%20integration%5D%0D%0A%0D%0AThank%20you%20for%20your%20time%20and%20consideration.%0D%0A%0D%0ABest%20regards%2C%0D%0A%5BYour%20Full%20Name%5D%0D%0A%5BYour%20Job%20Title%2C%20if%20applicable%5D%0D%0A%5BYour%20Contact%20Information%2C%20if%20appropriate%5D)
2. **Prepare your environment** - Ensure you have the necessary permissions and configurations in both AEM Forms and Adobe Experience Platform
3. **Follow the implementation steps** - Use the guide above to set up your cloud configuration and create your first AEP-connected form with XDM schema integration
4. **Test thoroughly** - Validate both the data submission and prefill capabilities in a development environment
5. **Plan for production** - Work with your implementation team to schedule the deployment of AEM Forms data submission to Experience Platform in production

## Related Resources {#related-resources}

* [AEM Forms as a Cloud Service documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/home.html)
* [Adobe Experience Platform documentation](https://experienceleague.adobe.com/docs/experience-platform/landing/home.html)
* [XDM System overview](https://experienceleague.adobe.com/docs/experience-platform/xdm/home.html)
* [Streaming ingestion in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/ingestion/streaming/overview.html)
* [Real-time Customer Profile overview](https://experienceleague.adobe.com/docs/experience-platform/profile/home.html)
* [AEM Forms Early Access Features](/help/forms/early-access-ea-features.md)
* [Creating Adaptive Forms with Core Components](/help/forms/creating-adaptive-form-core-components.md)
* [Using Form Data Models in AEM Forms](/help/forms/using-form-data-model.md)

<!--
Schema markup for technical documentation
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Connect AEM Forms with Adobe Experience Platform (AEP) | Data Integration Guide",
  "description": "Learn how to integrate AEM Forms with Adobe Experience Platform to leverage customer profiles, submit form data, and create personalized experiences.",
  "datePublished": "2025-05-28",
  "author": {
    "@type": "Corporation",
    "name": "Adobe"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Adobe Experience League",
    "logo": {
      "@type": "ImageObject",
      "url": "https://experienceleague.adobe.com/assets/img/favicons/apple-touch-icon.png"
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/aem-forms-aep-connector.html"
  },
  "articleSection": "AEM Forms",
  "keywords": "AEM Forms, Adobe Experience Platform, XDM schema, data integration, form submission, customer profiles, personalization"
}
-->
