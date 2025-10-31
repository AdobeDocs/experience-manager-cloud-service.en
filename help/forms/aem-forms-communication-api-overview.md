---
title: AEM Forms Communications APIs - Overview
description: Overview of AEM Forms Communications APIs including authentication methods and complete API reference
role: Developer, User
feature: Adaptive Forms, APIs & Integrations
---

# AEM Forms Communications APIs - Overview

AEM Forms Communications APIs provide a comprehensive suite of cloud-native APIs designed to help businesses automate document workflows. 

## API Classification Overview

AEM Forms Communications APIs are organized into categories based on functionality, processing patterns, and onboarding types.

### 1. Core API Groups

<table>
  <thead>
    <tr>
      <th>API Group</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>AEM Forms APIs</strong></td>
      <td>Central entry point for all forms operations. Provides unified access to document and forms services.</td>
    </tr>
    <tr>
      <td><strong>Delivery & Runtime APIs</strong></td>
      <td>Deliver forms, render layouts, capture data, and manage submissions in real-time.</td>
    </tr>
    <tr>
      <td><strong>Communication APIs</strong></td>
      <td>Enable personalized document generation and delivery for automated communication workflows.</td>
    </tr>
  </tbody>
</table>

### 2. Invocation Patterns

<table>
  <thead>
    <tr>
      <th>Pattern</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Sync (On-Demand) APIs</strong></td>
      <td>Used for real-time, low-latency document generation triggered by user actions. Suitable for immediate responses, such as form submissions.</td>
    </tr>
    <tr>
      <td><strong>Batch APIs (Output Service Only)</strong></td>
      <td>Used for large-scale, asynchronous document processing. Ideal for background or scheduled jobs like billing statements or reports.</td>
    </tr>
  </tbody>
</table>

### 3. API Onboarding Types

<table>
  <thead>
    <tr>
      <th>Onboarding Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>DX API First Router Onboarded</strong></td>
      <td>Modern, standardized APIs using Adobe DX API First approach with OAuth server-to-server authentication and enhanced developer experience.</td>
    </tr>
    <tr>
      <td><strong>Non-DX API First Onboarded</strong></td>
      <td>Legacy or traditional APIs using older authentication methods, gradually migrating to DX API First standards.</td>
    </tr>
  </tbody>
</table>

### 4. Services APIs

<table>
  <thead>
    <tr>
      <th>Service Category</th>
      <th>Service Name</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <!-- Document Services APIs -->
    <tr>
      <td rowspan="5"><strong>Document Services APIs</strong></td>
      <td><strong>Document Generation</strong></td>
      <td>Creates new documents from templates or data sources such as XML or JSON.</td>
    </tr>
    <tr>
      <td><strong>Document Manipulation</strong></td>
      <td>Modifies the document structure or combines multiple documents into a single output.</td>
    </tr>
    <tr>
      <td><strong>Document Conversion</strong></td>
      <td>Performs format transformations, for example, converting PDF to XDP or vice versa.</td>
    </tr>
    <tr>
      <td><strong>Document Assurance</strong></td>
      <td>Validates, secures, or digitally signs documents to ensure authenticity and integrity.</td>
    </tr>
    <tr>
      <td><strong>Document Extraction</strong></td>
      <td>Extracts form data, metadata, or content from existing documents for reuse.</td>
    </tr>
    <tr>
      <td rowspan="10"><strong>PDF Utility APIs</strong></td>
      <td><strong>PDF to XDP</strong></td>
      <td>Converts a PDF document into XDP format for further editing or processing.</td>
    </tr>
    <tr>
      <td><strong>getPDFProperties</strong></td>
      <td>Retrieves key PDF properties, including version, encryption, and permission details.</td>
    </tr>
    <tr>
      <td><strong>getUsageRights</strong></td>
      <td>Returns information about the applied usage rights in a PDF document.</td>
    </tr>
    <tr>
      <td><strong>getMetadata (doc, XMP)</strong></td>
      <td>Fetches embedded document metadata and XMP information.</td>
    </tr>
    <tr>
      <td><strong>exportData</strong></td>
      <td>Exports form data from a PDF document in XML or other structured formats.</td>
    </tr>
    <tr>
      <td><strong>importMetadata</strong></td>
      <td>Imports or updates metadata fields in a PDF document.</td>
    </tr>
    <tr>
      <td><strong>applyUsageRights</strong></td>
      <td>Applies rights management or enables features such as form filling and commenting.</td>
    </tr>
    <tr>
      <td><strong>generate Interactive PDF</strong></td>
      <td>Creates an interactive and fillable PDF from form templates and data.</td>
    </tr>
    <tr>
      <td><strong>Check Async Status</strong></td>
      <td>Checks the processing status of asynchronous PDF generation or conversion tasks.</td>
    </tr>
    <tr>
      <td><strong>Retrieve Async Completed PDF</strong></td>
      <td>Retrieves the final PDF output generated through asynchronous processing.</td>
    </tr>
  </tbody>
</table>

### 5. Output and Security APIs

<table>
  <thead>
    <tr>
      <th>Security API</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>EC Service (Encryption &amp; Certification)</strong></td>
      <td>Encrypts, decrypts, or digitally signs documents and manages certification workflows.</td>
    </tr>
    <tr>
      <td><strong>Assembler Service</strong></td>
      <td>Combines multiple documents or creates PDF portfolios using DDX definitions.</td>
    </tr>
    <tr>
      <td><strong>PDF Utility APIs</strong></td>
      <td>Converts PDFs to XDP, extracts or imports data, retrieves metadata, and manages usage rights.</td>
    </tr>
  </tbody>
</table>

## Authentication Methods

APIs support multiple authentication methods for secure integration between your applications and Adobe services:

1. **OAuth Server-to-Server (Recommended)**: [OAuth 2.0 Server-to-Server authentication](https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/implementation) is the modern and recommended approach. It allows applications or backend services to securely access Adobe APIs without user interaction, using client credentials managed in the Adobe Developer Console. It offers enhanced security, scalability, and simplified token management.

2. **JWT (JSON Web Token - Deprecated)**: [JWT Authentication](https://developer.adobe.com/developer-console/docs/guides/authentication/JWT/) is the older method that uses signed tokens to exchange for access tokens. 

3. **Basic Authentication**: Simple username and password authentication.

## API Reference

### Document Generation APIs

These APIs allow you to produce high-fidelity PDF documents with dynamic data inputs.

| API Endpoint | Purpose | Method | Type | Authentication |
|--------------|---------|--------|------|----------------|
| `/adobe/document/generate/pdfform` | Generate a fillable PDF form from XDP/PDF template with optional data merging | POST | Synchronous | OAuth, JWT |
| `/adobe/forms/doc/v1/generatePDFOutput` | Generate PDF or print document by combining template and data | POST | Synchronous | OAuth, JWT |
| `/adobe/forms/doc/v1/generatePrintedOutput` | Generate print documents (PS, PCL, ZPL) by combining template and data | POST | Synchronous | OAuth, JWT |
| `/adobe/forms/batch/output/config` | Create batch configuration for PDF/print document generation | POST | Asynchronous | OAuth, JWT |
| `/adobe/forms/batch/output/config/{configName}` | Get, update, or delete batch configuration | GET, PATCH, DELETE | Asynchronous | OAuth, JWT |
| `/adobe/forms/batch/output/config/{configName}/execution` | Execute batch job using specified configuration | POST | Asynchronous | OAuth, JWT |
| `/adobe/forms/batch/output/config/{configName}/execution/{executionId}` | Get status of batch execution | GET | Asynchronous | OAuth, JWT |
| `/adobe/forms/batch/output/config/{configName}/executions` | List all executions for a configuration | GET | Asynchronous | OAuth, JWT |

### Document Manipulation APIs

These APIs help combine, rearrange, and validate PDF documents using DDX (Document Description XML).

| API Endpoint | Purpose | Method | Authentication |
|--------------|---------|--------|----------------|
| `/adobe/forms/assembler/ddx/invoke` | Assemble/rearrange PDF documents using DDX instructions | POST | OAuth, JWT |
| `/adobe/forms/assembler/pdfa/convert` | Convert PDF to PDF/A-compliant format | POST | OAuth, JWT |
| `/adobe/forms/assembler/pdfa/validate` | Validate if PDF is PDF/A-compliant | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/transform/metadata` | Replace metadata in a PDF document | POST | OAuth, JWT |

### Document Extraction APIs

These APIs extract data, metadata, and properties from PDF documents.

| API Endpoint | Purpose | Method | Authentication |
|--------------|---------|--------|----------------|
| `/adobe/forms/doc/v1/extract/data` | Extract data from a PDF form | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/extract/metadata` | Extract metadata from a PDF document | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/extract/pdfproperties` | Extract properties of a PDF document | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/extract/usagerights` | Extract usage rights granted to a PDF | POST | OAuth, JWT |

### Document Conversion APIs

These APIs convert documents between different formats.

| API Endpoint | Purpose | Method | Authentication |
|--------------|---------|--------|----------------|
| `/adobe/forms/doc/v1/convert/pdftoxdp` | Convert an eligible PDF document to XDP format | POST | OAuth, JWT |

### Document Assurance APIs

These APIs provide security features including encryption, digital signatures, and certification.

| API Endpoint | Purpose | Method | Authentication |
|--------------|---------|--------|----------------|
| `/adobe/forms/doc/v1/assure/sign` | Add digital signature to a PDF document | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/assure/certify` | Certify a PDF document | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/assure/encrypt` | Encrypt a PDF document with password | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/assure/encrypt` (DELETE) | Remove password-based encryption | PUT | OAuth, JWT |
| `/adobe/forms/doc/v1/assure/inspect` | Fetch the type of security used in PDF | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/assure/signfield` | Add visible/invisible signature field | POST | OAuth, JWT |
| `/adobe/forms/doc/v1/assure/usagerights` | Apply or remove usage rights to PDF | POST | OAuth, JWT |

>[!NOTE]
>
> Document Assurance APIs are under early adopter program. Contact `aem-forms-ea@adobe.com` from your official email address to join the program and request access.


