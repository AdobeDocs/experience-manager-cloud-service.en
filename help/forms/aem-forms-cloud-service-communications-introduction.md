---
title: An introduction to Forms as a Cloud Service Communications
description: Automatically merge data with XDP and PDF templates or generate output in PCL, ZPL, and PostScript formats
exl-id: b6f05b2f-5665-4992-8689-d566351d54f1
---
# Use AEM Forms as a Cloud Service Communications {#frequently-asked-questions}

Communications capability helps you to create brand-approved, personalized, and standardized documents such as business correspondences, statements, claim processing letters, benefit notices, monthly bills, or welcome kits.

The capability provides APIs to generate and manipulate the documents. You can generate or manipulate a document on demand or create a batch job to generate multiple documents at defined intervals. Communications APIs provide:

* streamlined on-demand and batch documentation generation capabilities.

* capability to combine, rearrange, and validate PDF documents on-demand.

* HTTP APIs for easier integration with external systems. Separate APIs for on demand (low-latency) and batch operations (high-throughput operations) are included.

* a secure access to data. Communications APIs connect to and access data only from customer designated data repositories, making Communications highly secure.

![A sample credit card statement](assets/statement.png)
A credit card statement can be created using Communications APIs. This sample statement uses same template but separate data for each customer depending on their usage of credit card.

## Document generation

Communications document generation APIs help to combine a template (XFA or PDF) with customer data to generate documents in PDF and Print Formats like PS, PCL, DPL, IPL, and ZPL formats. These APIs utilize PDF and XFA templates with [XML data](communications-known-issues-limitations.md#form-data) to generate a single document on demand or multiple documents using a batch job.

Typically, you create a template using [Designer](use-forms-designer.md) and use Communications APIs to merge data with the template. Your application can send the output document to a network printer, a local printer, or to a storage system for archival. A typical out of the box and custom workflows look like the following:

![Communications document generation Workflow](assets/communicaions-workflow.png)

Depending on the use case, you can also make these documents available for download via your Website or a storage server.

Some examples of document generation APIs are:

### Create PDF documents {#create-pdf-documents}

You can use the document generation APIs to create a PDF document that is based on a form design and XML form data. The output is a non-interactive PDF document. That is, users cannot enter or modify the form data. A basic workflow is to merge XML form data with a form design to create a PDF document. The following Illustration shows the merging of a form design and XML form data to produce a PDF document.

![Create PDF documents](assets/outPutPDF_popup.png)
Figure: Typical workflow to create a PDF document

### Create PostScript (PS), Printer Command Language (PCL), Zebra Printing Language (ZPL) document {#create-PS-PCL-ZPL-documents}

You can use document generation APIs to create PostScript (PS), Printer Command Language (PCL), and Zebra Printing Language (ZPL) document that are based on an XDP form design or PDF document. These APIs help to merge a form design with form data to generate a document. You can save the document to a file and develop a custom process to send it to a printer.

<!-- ### Processing batch data to create multiple documents

Communications APIs can create separate documents for each record within an XML batch data source. The APIs can also create a single document that contains all records (this functionality is the default). Assume that an XML data source contains ten records and you instruct the APIs to create a separate document for each record (for example, PDF documents). As a result, the APIs generate ten PDF documents.

The following illustration also shows Communications APIs processing an XML data file that contains multiple records. However, assume that you instruct the APIs to create a single PDF document that contains all data records. In this situation, the APIs generate one document that contains all of the records.

The following illustration shows Communications APIs processing an XML data file that con tains multiple records. Assume that you instruct the Communications APIs to create a separate PDF document for each data record. In this situation, the APIs generates a separate PDF document for each data record.

 -->

### Processing batch data to create multiple documents {#processing-batch-data-to-create-multiple-documents}

You can use document generation APIs to create separate documents for each record within an XML batch data source. You can generate documents in bulk and asynchronous mode. You can configure various parameters for the conversion and then start the batch process.

![Create PDF Documents](assets/ou_OutputBatchMany_popup.png)

<!-- You can can also create a single document that contains all records (this functionality is the default).  Assume that an XML data source contains ten records and you have a requirement to create a separate document for each record (for example, PDF documents). You can use the Communication APIs to generate ten PDF documents. -->

<!-- The following illustration shows the Communication APIs processing an XML data file that contains multiple records. However, assume that you instruct the Communication APIs to create a single PDF document that contains all data records. In this situation, the Communication APIs generate one document that contains all of the records.

![Create PDF Documents](assets/ou_OutputBatchSingle_popup.png)

The following illustration shows the Communication APIs processing an XML data file that contains multiple records. Assume that you instruct the Communication APIs to create a separate PDF document for each data record. In this situation, the Communication APIs generates a separate PDF document for each data record.

![Create PDF Documents](assets/ou_OutputBatchMany_popup.png)

For detailed information on using Batch APIs, see Communication APIs: Processing batch data to create multiple documents. 

### Flatten interactive PDF documents {#flatten-interactive-pdf-documents}

You can use document generation APIs to transform an interactive PDF document (for example, a form) to a non-interactive PDF document. An interactive PDF document lets users enter or modify data located in the PDF document fields. The process of transforming an interactive PDF document to a non-interactive PDF document is called flattening. When a PDF document is flattened, a user cannot modify the data located in the document’s fields. One reason to flatten a PDF document is to ensure that data cannot be modified.

You can flatten the following types of PDF documents:

* Interactive PDF documents created in Designer (that contain XFA streams).

* Acrobat PDF forms

If you attempt to flatten a non-interactive PDF document, an exception occurs.

### Retain Form State {#retain-form-state}

An interactive PDF document contains various elements that constitute a form. These elements may include fields (to accept or display data), buttons (to trigger events), and scripts (commands to perform a specific action). Clicking a button may trigger an event that changes the state of a field. For example, choosing a gender option may change the color of a field or the appearance of the form. This is an example of a manual event causing the form state to change.

When such an interactive PDF document is flattened using the Communications APIs, the state of the form is not retained. To ensure that the state of the form is retained even after the form is flattened, set the Boolean value _retainFormState_ to True to save and retain the state of the form. -->

## Document manipulation

Communications document manipulation APIs help to combine, rearrange, and validate PDF documents. Typically, you create a DDX and submit it to document manipulation APIs to assemble or rearrange a document. The [DDX document](https://helpx.adobe.com/content/dam/help/en/experience-manager/forms-cloud-service/ddxRef.pdf) provides instructions on how to use the source documents to produce a set of required documents. The DDX reference documentation provides detailed information about all the supported operations. Some examples of document manipulation are:

### Assemble PDF documents

You can use the document manipulation APIs to assemble two or more PDF or XDP documents into a single PDF document or PDF Portfolio. Here are some of the ways you can assemble PDF documents:

* Assemble a simple PDF document
* Create a PDF Portfolio
* Assemble encrypted documents
* Assemble documents using Bates numbering
* Flatten and assemble documents

![Assembling a simple PDF document from multiple PDF documents](assets/as_document_assembly.png)
Figure: Assembling a simple PDF document from multiple PDF documents

### Disassemble PDF documents

You can use the document manipulation APIs to disassemble a PDF document. The APIs can extract pages from the source document or divide a source document based on bookmarks. Typically, this task is useful if the PDF document was originally created from many individual documents, such as a collection of statements.

* Extract pages from a source document
* Divide a source document based on bookmarks

![Dividing a source document based on bookmarks into multiple documents](assets/as_intro_pdfsfrombookmarks.png)
Figure: Dividing a source document based on bookmarks into multiple documents

### Convert to and validate PDF/A-compliant documents

You can use the document manipulation APIs to convert a PDF document to a PDF/A-compliant document and to determine whether a PDF document is PDF/A-compliant. PDF/A is an archival format meant for long-term preservation of the document’s content. The fonts are embedded within the document, and the file is uncompressed. As a result, a PDF/A document is typically larger than a standard PDF document. Also, a PDF/A document does not contain audio and video content.

## Types of communications APIs

Communications provide HTTP APIs for on-demand and batch document generation:

* **[Synchronous APIs](https://www.adobe.io/experience-manager-forms-cloud-service-developer-reference/)** are suitable for on-demand, low latency, and single record document generation scenarios. These APIs are more suitable for user-action based use cases. For example, generating a document after a user completes filling a form.

* **[Batch APIs (Asynchronous APIs)](https://www.adobe.io/experience-manager-forms-cloud-service-developer-reference/)** are suitable for scheduled, high throughput, and multiple document generation scenarios. These APIs generate documents in batches. For example, phone bills, credit card statements, and benefits statements generated every month.

## Onboarding

Communications capability is available as a standalone and add-on module for Forms as a Cloud Service users. You can contact Adobe Sales team or your Adobe representative to request access. Adobe enables access for your organization and provide required privileges to the person designated as administrator in your organization. The administrator can grant access to your  Forms as a Cloud Service developers (users) of your organization to use the APIs.

After onboarding, to enable Communications capability for your  Forms as a Cloud Service environment:

1. Log in to Cloud Manager and open your AEM Forms as a Cloud Service Instance.

1. Open the Edit Program option, go to the Solutions & Add-ons tab, and select the **[!UICONTROL Forms - Communications]** option.

   ![Communications](assets/communications.png)

    If you have already enabled the **[!UICONTROL Forms - Digital Enrollment]** option, then select the **[!UICONTROL Forms - Communications Add-On]** option.  

   ![Addon](assets/add-on.png)

1. Click **[!UICONTROL Update]**.

1. Run the build pipeline. After the build pipeline succeeds, Communications APIs are enabled for your environment.

>[!NOTE]
>
> To enable and configure document manipulation APIs, add the following rule to [Dispatcher configuration](setup-local-development-environment.md#forms-specific-rules-to-dispatcher):
>
> `# Allow Forms Doc Generation requests`
> `/0062 { /type "allow" /method "POST" /url "/adobe/forms/assembler/*" }`

<!--

Communication help you combine a template and XML data to generate print documents in various formats. The service allows you to generate documents in synchronous and batch modes. The APIs enables you to create applications that let you:

  * Generate documents by populating template files (PDF and XDP) with XML data.
  * Generate output forms in various formats, including non-interactive PDF print streams.

Consider a scenario where you have one or more templates and multiple records of XML data for each template. You can use Communications APIs to generate a print document for each record.  You can also combine the records into a single document.  The result is a non-interactive PDF document. A non-interactive PDF document does not let users enter data into its fields.

 There are two main Communications APIs. The _generatePDFOutput_ generates PDFs, while the _generatePrintedOutput_ generates PostScript, ZPL, and PCL formats. These APIs are available as REST endpoints on your environment, both on author and publish instances. Since the publish instances are configured to scale faster than the author instances, it is recommended use these APIs via publish instances.

The first parameter of both the operations accept the path and name of the template file (for example ExpenseClaim.xdp). You can specify a fully qualified path, reference path of your AEM Repository, or path of a binary file. The second parameter accepts an XML document that is merged with the template while generating the output document.  

The [API reference documentation](https://documentcloud.adobe.com/link/track?uri=urn:aaid:scds:US:b1223732-ae0f-4921-bdc0-c31e48b56044) provides detailed information about all the parameters, authentication methods, and various services provided by APIs. The API reference documentation is also available in the .yaml format. You can download the .yaml for [Batch APIs](assets/batch-api.yaml) or [non-Batch API.yaml](assets/non-batch-api.yaml) file and upload it to postman to check functionality of APIs.

>[!VIDEO](https://video.tv.adobe.com/v/335771)

Uploading Communication APIs .yaml file to postman to check functionality of APIs.

## Using the Communications APIs {#workflows}

Typically, you create a template using [Designer](use-forms-designer.md) and use communications APIs ( generatePDFOutput and generatePrintedOutput) to:

* Convert these templates to various formats, including PDF, PostScript, ZPL, and PCL.
* Merge XML form data with a form design to generate a document.
* Generate a document without merging XML form data into the document. However, the primary workflow is merging data into the document.

Then, the output document is stored to a file. You can design custom workflows to send the file to a network printer, a local printer, or to a storage system for archival. A typical out of the box and custom workflows look like the following:

![Communications Workflow](assets/communicaions-workflow.png)

### Create PDF documents {#create-pdf-documents}

You can use the _generatePDFOutput_ API to create PDF document that is based on a form design and XML form data. The output is a non-interactive PDF document. That is, users cannot enter or modify form data. A basic workflow is to merge XML form data with a form design to create a PDF document. The following illustration shows the merging of a form design and XML form data to produce a PDF document.

![Create PDF Documents](assets/outPutPDF_popup.png)

### Create PostScript (PS), Printer Command Language (PCL), Zebra Printing Language (ZPL) document {#create-PS-PCL-ZPL-documents}

You can use Communications APIs to create PostScript (PS), Printer Command Language (PCL), and Zebra Printing Language (ZPL) document that are based on a XDP form design or PDF document. The _generatePrintedOutput_ API merges a form design with form data to generate a document. You can save the document to a file and develop a custom process to send it to a printer.

 ### Processing batch data to create multiple documents

Communications APIs can create separate documents for each record within an XML batch data source. The APIs can also create a single document that contains all records (this functionality is the default). Assume that an XML data source contains ten records and you instruct the APIs to create a separate document for each record (for example, PDF documents). As a result, the APIs generate ten PDF documents.

The following illustration also shows Communications APIs processing an XML data file that contains multiple records. However, assume that you instruct the APIs to create a single PDF document that contains all data records. In this situation, the APIs generate one document that contains all of the records.

The following illustration shows Communications APIs processing an XML data file that contains multiple records. Assume that you instruct the Communications APIs to create a separate PDF document for each data record. In this situation, the APIs generates a separate PDF document for each data record.

### Processing batch data to create multiple documents {#processing-batch-data-to-create-multiple-documents}

You create separate documents for each record within an XML batch data source. You can can also create a single document that contains all records (this functionality is the default). Assume that an XML data source contains ten records and you have a requirement to create a separate document for each record (for example, PDF documents). You can use the Communication APIs to generate ten PDF documents.

The following illustration shows the Communication APIs processing an XML data file that contains multiple records. However, assume that you instruct the Communication APIs to create a single PDF document that contains all data records. In this situation, the Communication APIs generate one document that contains all of the records.

![Create PDF Documents](assets/ou_OutputBatchSingle_popup.png)

The following illustration shows the Communication APIs processing an XML data file that contains multiple records. Assume that you instruct the Communication APIs to create a separate PDF document for each data record. In this situation, the Communication APIs generates a separate PDF document for each data record.

![Create PDF Documents](assets/ou_OutputBatchMany_popup.png)

For detailed information on using Batch APIs, see Communication APIs: Processing batch data to create multiple documents.

### Flatten interactive PDF documents {#flatten-interactive-pdf-documents}

You can use the Communications APIs to transform an interactive PDF document (for example, a form) to a non-interactive PDF document. An interactive PDF document lets users enter or modify data located in the PDF document fields. The process of transforming an interactive PDF document to a non-interactive PDF document is called flattening. When a PDF document is flattened, a user cannot modify the data located in the document’s fields. One reason to flatten a PDF document is to ensure that data cannot be modified.

You can flatten the following types of PDF documents:

* Interactive PDF documents created in Designer (that contain XFA streams).

* Acrobat PDF forms

If you attempt to flatten a non-interactive PDF document, an exception occurs.

### Retain Form State {#retain-form-state}

An interactive PDF document contains various elements that constitute a form. These elements may include fields (to accept or display data), buttons (to trigger events), and scripts (commands to perform a specific action). Clicking a button may trigger an event that changes the state of a field. For example, choosing a gender option may change the color of a field or the appearance of the form. This is an example of a manual event causing the form state to change.

When such an interactive PDF document is flattened using the Communications APIs, the state of the form is not retained. To ensure that the state of the form is retained even after the form is flattened, set the Boolean value _retainFormState_ to True to save and retain the state of the form.  -->
