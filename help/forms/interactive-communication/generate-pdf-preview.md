---
title: PDF Preview in Interactive Communication Editor with Different Data Options
description: PDF Preview in Interactive Communication Editor with Different Data Options to preview Interactive Communications in three different ways.
products: SG_EXPERIENCEMANAGER/Cloud Service/FORMS
feature: Interactive Communication
role: User, Developer, Admin
exl-id: 17b3fe2b-6a1d-4fe2-9a92-a55a50400824
---
# PDF Preview in Interactive Communication Editor

>[!NOTE]
>
> The Interactive Communication capability is available under the early-adopter program. Send an email from your work address to `aem-forms-ea@adobe.com` to request access.

>[!IMPORTANT]
>
> **Documentation Subject to Change**: This prompt library is currently being tested against the product and is subject to updates and revisions. Prompts, examples, and best practices may change as the Forms Experience Builder continues to evolve during the early-adopter program.

The PDF preview feature enables users to preview Interactive Communications in three different ways: without data, with local JSON-based data, or with sample data from the configured data model. 

## Key Benefits

- Preview Interactive Communications with sample data to visualize how live data will appear when merged with the communication.

- Upload local JSON data files to generate data-driven previews without backend setup.

- Use connected Form Data Models (FDM) to simulate real-time data integration with sample data during design.

- Easily switch between data options (no data, local data, FDM) to validate layout, structure, and personalization.

## PDF Preview in Interactive Communication Editor with Different Data Options

Preview Interactive Communications using no data, local data, or sample data from configured data model for flexible testing and validation.

+++1. Preview with No Data.

1.1. Open your Interactive Communication in the IC Editor.

1.2. Use the PDF Preview option and select **No Data** option to view a communication without data.

![Find IC Docu](/help/forms/interactive-communication/assets/nodata.png)

+++

+++2. Preview with Local JSON Data

2.1. Prepare a structured JSON file. For reference, you can copy the sample data from the JSON schema [(FDM)](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/forms/integrate/use-form-data-model/work-with-form-data-model) used for the communication.

2.2. In the IC Editor, go to **PDF Preview** > Using Local Data.

2.3. Select and upload your JSON file to render a PDF preview with the provided data.

![Find IC Docu](/help/forms/interactive-communication/assets/localdata.png)

+++

+++3. Preview with Data Model 

3.1. Select **Using Data Model** to use sample data from an already configured Form Data Model (FDM) of the IC.

3.2. The preview auto-populates data from model fields. Ensure the sample data is saved in FDM on first use, or the preview may show as no-data.

![Find IC Docu](/help/forms/interactive-communication/assets/datamodel.png)

+++
