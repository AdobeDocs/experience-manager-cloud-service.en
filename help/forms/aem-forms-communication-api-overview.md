---
title: AEM Forms Communications APIs - Overview
description: Overview of AEM Forms Communications APIs including authentication methods and complete API reference
role: Developer, User
feature: Adaptive Forms, APIs & Integrations
hide: yes
hidefromtoc: yes
index: no
---

# AEM Forms Communications APIs - Overview

AEM Forms Communications APIs provide a comprehensive suite of cloud-native APIs designed to help businesses automate document workflows. 

AEM Forms APIs are structured and accessed through two primary consoles:

* [Adobe Developer Console (ADC)](https://developer.adobe.com/developer-console/) - Adobe Developer Console is the gateway to Adobe APIs, Events, Runtime and App Builder.
  
* [AEM Developer Console](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console) - AEM Developer Console provides tools for debugging and inspecting AEM as a Cloud Service environments.

Each console provides access to different APIs and services for document processing, generation, conversion, encryption, and communication tasks. The APIs support different [authentication methods](#authentication-methods).

## Authentication Methods

APIs support multiple authentication methods for secure integration between your applications and Adobe services:

| Aspect | OAuth Server-to-Server (Recommended)| JWT (JSON Web Token)|
|-------------|------------------------------------------|---------------------------|
| Description | Modern and secure method for API access without user interaction. | Older method using signed tokens for access. |
| Setup Location | Adobe Developer Console and AEM Developer Console | AEM Developer Console only |
| Security | High – uses client credentials and scopes | Moderate – depends on key management |
| Scalability | Highly scalable for backend integrations | Limited, suited for legacy use |
| Token Management | Automatic generation and renewal | Manual token signing and rotation |
| Status | Recommended | Deprecated |


>[!NOTE]
>
> Click the below links to know more about:-
> 
> * [OAuth Server-to-Server (Recommended)](/help/forms/oauth-api-authetication.md)
> * [JWT (JSON Web Token)](/help/forms/jwt-api-authentication.md) 

<!--### Execution Models

The following table highlights the key differences between Synchronous (On-Demand) and Asynchronous (Batch) execution models supported in AEM Forms Communications APIs:

| Feature | Synchronous (On-Demand) | Batch (Asynchronous) |
|---------|-------------------------|----------------------|
| **Execution Model** | Real-time, immediate | Queued, scheduled |
| **Response Time** | Seconds | Minutes to hours |
| **Volume** | Single or few documents | Hundreds to thousands |
| **Testing Environment** | Author & Publish | Author Only |
| **Use Case** | User-triggered actions | Scheduled bulk operations |
| **Console Access** | ADC & AEM Developer Console | AEM Developer Console Only |-->

## API Classification Overview

All AEM Forms APIs are divided into two main parts:

* [Adaptive Form Delivery & Runtime APIs](https://developer-stage.adobe.com/experience-cloud/experience-manager-apis/api/stable/forms/)

* [AEM Forms Communication APIs](#aem-forms-communications-apis)

| Details | Adaptive Form Delivery & Runtime APIs | Communication APIs |
|--------------|----------------------------|--------------------------|
| Purpose | Handle Adaptive Form delivery and runtime operations | Document generation and manipulation |
| Use Cases | - Form rendering<br>- Data prefill<br>- Form submissions<br>- Draft management | - PDF generation<br>- Document merging<br>- Batch processing<br>- Print operations |
| Authorization Method | Supports OAuth Server-to-Server / User authentication methods. | Supports only OAuth Server-to-Server authentication. |
 
### AEM Forms Communications APIs 

Communication APIs are the primary focus for document-centric operations. 

The table below lists all the [AEM Forms Communications APIs](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/) along with their supported authentication methods and execution models:

#### Document Generation APIs


| API Endpoint      |   Description |Execution Model     | Authentication Method         |
| ----- | ------ |------- | ------ |
| [/adobe/forms/batch/output/config](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-batch/#tag/Batch-Configuration/operation/CreateBatchConfig) | Creates a new batch configuration for document generation jobs.                                      | Asynchronous/Batch |[OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md) |
| [/adobe/forms/batch/output/config/{configName}](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-batch/#tag/Batch-Configuration/operation/GetBatchConfigbyName)  | Retrieves details of a specific batch configuration.                       | Asynchronous/Batch  | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)   |
| [/adobe/forms/batch/output/config/configs](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-batch/#tag/Batch-Configuration/operation/GetAllBatchConfigs) | Returns a list of all available batch configurations.                              | Asynchronous/Batch   | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)  |
| [/adobe/forms/batch/output/config/{configName}/execution](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-batch/#tag/Batch-Execution/operation/StartBatchRun)               |  Starts a batch output generation run using a configuration.    | Asynchronous/Batch |[OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)  |
| [/adobe/forms/batch/output/config/{configName}/execution/{executionId}](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-batch/#tag/Batch-Execution/operation/GetBatchRunInstanceState) | Retrieves the execution status of a batch job.   |Asynchronous/Batch | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)  |
| [/adobe/forms/batch/output/config/{configName}/executions](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-batch/#tag/Batch-Execution/operation/GetAllRunningInstancesForBatch)              |  Lists all running instances for a specific batch configuration.   |Asynchronous/Batch | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)   |
| [/adobe/forms/doc/v1/generatePDFOutput](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-sync/#tag/Communications-Services/paths/~1adobe~1forms~1doc~1v1~1generatePDFOutput/post)                                 |  Generates PDF output synchronously based on templates and data.   | Synchronous      | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)  |
| [/adobe/forms/doc/v1/generatePrintedOutput](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-sync/#tag/Batch-Execution/operation/GetAllRunningInstancesForBatch)  | Generates print-ready output formats (e.g., PCL, PostScript).                           | Synchronous    | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)  |
| [/adobe/forms/doc/v1/generate/afp](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/output-sync/#tag/Communications-Services/paths/~1adobe~1forms~1doc~1v1~1generate~1afp/post)       | Generates AFP output for high-volume printing.                               | Synchronous  | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)   |
| [/adobe/document/generate/pdfform](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#operation/renderPDFForm)     |  Renders a PDF Form (XFA/XDP) with merged data.  | Synchronous  |[OAuth Server to Server](/help/forms/oauth-api-authetication.md)      |
| [/adobe/document/generate/pdfform/jobs/{id}/status](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#operation/renderPDFFormJobStatus)  | Retrieves the status of a PDF form generation job.  | Synchronous        |[OAuth Server to Server](/help/forms/oauth-api-authetication.md)      |
| [/adobe/document/generate/pdfform/jobs/{id}/result](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#operation/renderPDFFormJobResult)    | Fetches the output/result of a completed PDF form job. | Synchronous        | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)    |


#### Document Manipulation APIs

| API Endpoint   | Description    | Execution Model     | Authentication Method         |
| ------------------ | ---------------- | ----------| ---------- |
| [/adobe/forms/assembler/ddx/invoke](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/assembler-sync/#tag/DDX-execution/operation/InvokeDDX)|  Executes DDX instructions to combine, split, or manipulate PDFs.   | Synchronous | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)  |
| [/adobe/forms/assembler/pdfa/convert](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/assembler-sync/#tag/Document-conversion/operation/ConvertToPDFA) |  Converts a PDF document to PDF/A format. | Synchronous |[OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)   |
| [/adobe/forms/assembler/pdfa/validate](https://developer.adobe.com/experience-manager-forms-cloud-service-developer-reference/api/assembler-sync/#tag/Document-validation/operation/CheckIsPDFA) | Validates whether a PDF complies with PDF/A standard  | Synchronous |[OAuth Server to Server](/help/forms/oauth-api-authetication.md)/[JWT](/help/forms/jwt-api-authentication.md)   |

#### Document Conversion APIs

| API Endpoint |  Description | Execution Model     | Authentication Method        |
|--------- | -------|---------|----------------------|
| [/adobe/document/convert/pdftoxdp](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Conversion/paths/~1convert~1pdftoxdp/post) | Converts a PDF form into XDP format. | Synchronous | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)  |

#### Document Extraction APIs

| API Endpoint | Description   |  Execution Model     | Authentication Method         |
|---------| -------|---------|----------------------|
| [/adobe/forms/doc/v1/extract/pdfproperties](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Extraction/paths/~1extract~1pdfproperties/post) |  Extracts properties and structural information from a PDF. | Synchronous |[OAuth Server to Server](/help/forms/oauth-api-authetication.md)  |
| [/adobe/forms/doc/v1/extract/usagerights](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#operation/extractUsageRights) | Extracts usage rights embedded in a PDF.  | Synchronous | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)  |
| [/adobe/forms/doc/v1/extract/metadata](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Extraction/paths/~1extract~1metadata/post) | Extracts metadata such as title, author, and keywords.  | Synchronous |[OAuth Server to Server](/help/forms/oauth-api-authetication.md) |
| [/adobe/forms/doc/v1/extract/data](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#operation/exportData) |  Extracts form data (XML/JSON) from PDF forms.  | Synchronous| [OAuth Server to Server](/help/forms/oauth-api-authetication.md) |
| [/adobe/document/extract/security](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Extraction/paths/~1extract~1security/post) |  Extracts security settings such as permissions and encryption.  | Synchronous| [OAuth Server to Server](/help/forms/oauth-api-authetication.md)  |

#### Document Transformation APIs


| API Endpoint  | Description   | Execution Model     | Authentication Method        |
|--------|---------|---------|----------------------|
| [/adobe/document/transform/metadata](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Transformation/paths/~1transform~1metadata/post) | Updates or adds metadata in a PDF document.  | Synchronous | [OAuth Server to Server](/help/forms/oauth-api-authetication.md)  |
| [/adobe/document/field/signature/add](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Transformation/paths/~1field~1signature~1add/post) | Adds a digital signature field to a PDF.  | Synchronous |[OAuth Server to Server](/help/forms/oauth-api-authetication.md)|
| [/adobe/document/field/signature/clear](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Transformation/paths/~1field~1signature~1clear/post) | Clears the contents of a signature field.   | Synchronous | [OAuth Server to Server](/help/forms/oauth-api-authetication.md) |
| [/adobe/document/field/signature/remove](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Transformation/paths/~1field~1signature~1remove/post) | Removes a signature field from a PDF.  | Synchronous | [OAuth Server to Server](/help/forms/oauth-api-authetication.md) |

#### Document Assurance APIs

| API Endpoint  | Description  | Execution Model     | Authentication Method        |
|---------|-------|---------|----------------------|
| [/adobe/document/assure/usagerights](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#operation/applyUsageRights) | Applies usage rights to a PDF (e.g., comment, fill, sign).   | Synchronous | [OAuth Server to Server](/help/forms/oauth-api-authetication.md) |
| [/adobe/document/assure/encrypt](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Assurance/paths/~1assure~1encrypt/post) | Encrypts a PDF with password or certificate security.   | Synchronous |  [OAuth Server to Server](/help/forms/oauth-api-authetication.md) |
| [/adobe/document/assure/decrypt](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Assurance/paths/~1assure~1decrypt/post) | Decrypts a secured PDF document.  | Synchronous |   [OAuth Server to Server](/help/forms/oauth-api-authetication.md) |
| [/adobe/document/assure/sign](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Assurance/paths/~1assure~1sign/post) | Digitally signs a PDF document.   | Synchronous | [OAuth Server to Server](/help/forms/oauth-api-authetication.md) |
| [/adobe/document/assure/certify](https://developer.adobe.com/experience-cloud/experience-manager-apis/api/experimental/document/#tag/Document-Assurance/paths/~1assure~1certify/post) | Certifies a PDF with a digital certificate.  | Synchronous |  [OAuth Server to Server](/help/forms/oauth-api-authetication.md) |


## Next Steps

Learn how to set environment for Synchronous (On-Demand) and Asynchronous (Batch) Forms Communications APIs:

<!-- START CARDS HTML - DO NOT MODIFY BY HAND -->
<div class="columns">
    <!-- Synchronous APIs Card -->
    <div class="column is-half-tablet is-half-desktop is-one-third-widescreen" aria-label="AEM Forms Communications APIs - Synchronous">
        <div class="card" style="height: 100%; display: flex; flex-direction: column;">
            <div class="card-image">
                <figure class="image x-is-16by9">
                    <a href="/help/forms/aem-forms-cloud-service-communications-on-demand-processing.md" title="Synchronous APIs" target="_self" rel="referrer">
                        <img class="is-bordered-r-small" src="/help/forms/assets/sync-api.png" alt="Synchronous APIs"
                             style="width: 100%; aspect-ratio: 16 / 9; object-fit: cover; overflow: hidden; display: block; margin: auto;">
                    </a>
                </figure>
            </div>
            <div class="card-content is-padded-small" style="display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between;">
                <div class="top-card-content">
                    <p class="headline is-size-6 has-text-weight-bold">
                        <a href="/help/forms/aem-forms-cloud-service-communications-on-demand-processing.md" target="_self" rel="referrer" title="AEM Forms Communications APIs - Synchronous">AEM Forms Communications APIs - Synchronous</a>
                    </p>
                    <p class="is-size-6">Learn how to set up environment for Synchronous (on-demand) Forms Communications APIs that generate or process documents instantly. </p>
                </div>
                <a href="/help/forms/aem-forms-cloud-service-communications-on-demand-processing.md" target="_self" rel="referrer" class="spectrum-Button spectrum-Button--outline spectrum-Button--primary spectrum-Button--sizeM" style="align-self: flex-start; margin-top: 1rem;">
                    <span class="spectrum-Button-label has-no-wrap has-text-weight-bold">Learn more</span>
                </a>
            </div>
        </div>
    </div>
    <!-- Asynchronous APIs Card -->
    <div class="column is-half-tablet is-half-desktop is-one-third-widescreen" aria-label="AEM Forms Communications APIs - Asynchronous">
        <div class="card" style="height: 100%; display: flex; flex-direction: column;">
            <div class="card-image">
                <figure class="image x-is-16by9">
                    <a href="/help/forms/aem-forms-cloud-service-communications-batch-processing.md" title="AEM Forms Communications APIs - Asynchronous" target="_self" rel="referrer">
                        <img class="is-bordered-r-small" src="/help/forms/assets/async-api.png" alt="Asynchronous APIs"
                             style="width: 100%; aspect-ratio: 16 / 9; object-fit: cover; overflow: hidden; display: block; margin: auto;">
                    </a>
                </figure>
            </div>
            <div class="card-content is-padded-small" style="display: flex; flex-direction: column; flex-grow: 1; justify-content: space-between;">
                <div class="top-card-content">
                    <p class="headline is-size-6 has-text-weight-bold">
                        <a href="/help/forms/aem-forms-cloud-service-communications-batch-processing.md" target="_self" rel="referrer" title="Asynchronous APIs">AEM Forms Communications APIs - Asynchronous (Batch)</a>
                    </p>
                    <p class="is-size-6">Learn how to set up environment for Asynchronous (Batch) Forms Communications APIs that generate or process multiple documents in a scheduled manner.</p>
                </div>
                <a href="/help/forms/aem-forms-cloud-service-communications-batch-processing.md" target="_self" rel="referrer" class="spectrum-Button spectrum-Button--outline spectrum-Button--primary spectrum-Button--sizeM" style="align-self: flex-start; margin-top: 1rem;">
                    <span class="spectrum-Button-label has-no-wrap has-text-weight-bold">Learn more</span>
                </a>
            </div>
        </div>
    </div>
</div>
<!-- END CARDS HTML - DO NOT MODIFY BY HAND -->


>[!MORELIKETHIS]
>
>* [Introduction to AEM Forms as a Cloud Service Communications](/help/forms/aem-forms-cloud-service-communications-introduction.md)
>* [AEM Forms as a Cloud Service Architecture for Adaptive Forms and Communication APIs](/help/forms/aem-forms-cloud-service-architecture.md)
>* [Communication Processing - Synchronous APIs](/help/forms/aem-forms-cloud-service-communications.md)
>* [Communication Processing - Batch APIs](/help/forms/aem-forms-cloud-service-communications-batch-processing.md)
>* [Communication Processing - On-Demand APIs](/help/forms/aem-forms-cloud-service-communications-on-demand-processing.md)