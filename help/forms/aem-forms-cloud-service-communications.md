---
title: AEM Forms as a Cloud Service - Communications
description: Automatically merge data with XDP and PDF templates or generate output in PCL, ZPL, and PostScript formats
exl-id: 9fa9959e-b4f2-43ac-9015-07f57485699f
---

# Use AEM Forms as a Cloud Service Communications APIs {#frequently-asked-questions}

**The Communications feature is in beta.**

Communications APIs help you combine XDP templates, XDP-based PDF documents, and Acrobat Forms (AcroForm) with XML data to generate print documents in various formats and enable you to create applications that let you:

- Generate documents by populating template files with XML data.

- Generate forms in various formats, including non-interactive PDF print streams.

- Generate print PDFs from XFA form PDFs.

- Generate PDF, PostScript, PCL, and ZPL documents in bulk by merging multiple sets of data with source templates.

Consider a scenario where you have one or more templates and multiple records of XML data for each template. You can use Communications APIs to generate a print document for each record. <!-- You can also combine the records into a single document. --> The result is a non-interactive PDF document. A non-interactive PDF document does not let users enter data into its fields.

The [API reference documentation](https://documentcloud.adobe.com/link/track?uri=urn:aaid:scds:US:b1223732-ae0f-4921-bdc0-c31e48b56044) provides detailed information about all the APIs, parameters, authentication methods, and various services provided by APIs. The API reference documentation is also available in the .yaml format. You can download the .yaml for [Batch APIs](assets/batch-api.yaml) or [non-Batch API.yaml](assets/non-batch-api.yaml) file and upload it to postman to check functionality of APIs.

>[!VIDEO](https://video.tv.adobe.com/v/335771)

Uploading Communication APIs .yaml file to postman to check functionality of APIs.

>[!NOTE]
>
>Only members of forms-users group can access Communications APIs.

## Enabling Communications 

To enable Communications for your  Forms as a Cloud Service environment:

1. Login to Cloud Manager and open your AEM Forms as a Cloud Service Instance. 

1. Open the Edit Program option, go to the Solutions & Add-ons tab, and select the **[!UICONTROL Forms - Communications]** option.

   <!-- ![Communications](assets\communications.png)

    If you have already enabled the **[!UICONTROL Forms - Digital Enrollment]** option, then select the **[!UICONTROL Forms - Communications Add-On]** option.  

    <!-- ![Addon](assets\add-on.png) -->

1. Click **[!UICONTROL Update]**.

1. Run the build pipeline.

After the build pipleine succeeds, Communication APIs are enabled for your environment.

## Using the Communications APIs {#workflows}

Typically, you create a template using [Designer](use-forms-designer.md) and use communications APIs to:

- Convert these templates to various formats, including PDF, PostScript, ZPL, and PCL.
- Merge XML form data with a form design to generate a document.
- Generate a document without merging XML form data into the document. However, the primary workflow is merging data into the document.

Then, the output document is stored to a file. You can design custom workflows to send the file to a network printer, a local printer, or to a storage system for archival. A typical out of the box and custom workflows look like the following:

![Communications Workflow](assets/communicaions-workflow.png)

### Create PDF documents {#create-pdf-documents}

You can use the _generatePDFOutput_ API to create PDF document that is based on a form design and XML form data. The output is a non-interactive PDF document. That is, users cannot enter or modify form data. A basic workflow is to merge XML form data with a form design to create a PDF document. The following illustration shows the merging of a form design and XML form data to produce a PDF document.

![Create PDF Documents](assets/outPutPDF_popup.png)

### Create PostScript (PS), Printer Command Language (PCL), Zebra Printing Language (ZPL) document {#create-PS-PCL-ZPL-documents}

You can use Communications APIs to create PostScript (PS), Printer Command Language (PCL), and Zebra Printing Language (ZPL) document that are based on a XDP form design or PDF document. The _generatePrintedOutput_ API merges a form design with form data to generate a document. You can save the document to a file and develop a custom process to send it to a printer.

<!-- ### Processing batch data to create multiple documents

Communications APIs can create separate documents for each record within an XML batch data source. The APIs can also create a single document that contains all records (this functionality is the default). Assume that an XML data source contains ten records and you instruct the APIs to create a separate document for each record (for example, PDF documents). As a result, the APIs generate ten PDF documents.

The following illustration also shows Communications APIs processing an XML data file that contains multiple records. However, assume that you instruct the APIs to create a single PDF document that contains all data records. In this situation, the APIs generate one document that contains all of the records.

The following illustration shows Communications APIs processing an XML data file that contains multiple records. Assume that you instruct the Communications APIs to create a separate PDF document for each data record. In this situation, the APIs generates a separate PDF document for each data record.

 -->

### Processing batch data to create multiple documents {#processing-batch-data-to-create-multiple-documents}

You can create separate documents for each record within an XML batch data source. You can generate documents in bulk and asynchronous mode. You can configure various parameters for the conversion and then start the batch process. <!-- You can can also create a single document that contains all records (this functionality is the default).  Assume that an XML data source contains ten records and you have a requirement to create a separate document for each record (for example, PDF documents). You can use the Communication APIs to generate ten PDF documents. -->

<!-- The following illustration shows the Communication APIs processing an XML data file that contains multiple records. However, assume that you instruct the Communication APIs to create a single PDF document that contains all data records. In this situation, the Communication APIs generate one document that contains all of the records.

![Create PDF Documents](assets/ou_OutputBatchSingle_popup.png)

The following illustration shows the Communication APIs processing an XML data file that contains multiple records. Assume that you instruct the Communication APIs to create a separate PDF document for each data record. In this situation, the Communication APIs generates a separate PDF document for each data record.

![Create PDF Documents](assets/ou_OutputBatchMany_popup.png)

For detailed information on using Batch APIs, see Communication APIs: Processing batch data to create multiple documents. -->

### Flatten interactive PDF documents {#flatten-interactive-pdf-documents}

You can use the Communications APIs to transform an interactive PDF document (for example, a form) to a non-interactive PDF document. An interactive PDF document lets users enter or modify data located in the PDF document fields. The process of transforming an interactive PDF document to a non-interactive PDF document is called flattening. When a PDF document is flattened, a user cannot modify the data located in the document’s fields. One reason to flatten a PDF document is to ensure that data cannot be modified.

You can flatten the following types of PDF documents:

- Interactive PDF documents created in Designer (that contain XFA streams).

- Acrobat PDF forms

If you attempt to flatten a non-interactive PDF document, an exception occurs.

### Retain Form State {#retain-form-state}

An interactive PDF document contains various elements that constitute a form. These elements may include fields (to accept or display data), buttons (to trigger events), and scripts (commands to perform a specific action). Clicking a button may trigger an event that changes the state of a field. For example, choosing a gender option may change the color of a field or the appearance of the form. This is an example of a manual event causing the form state to change.

When such an interactive PDF document is flattened using the Communications APIs, the state of the form is not retained. To ensure that the state of the form is retained even after the form is flattened, set the Boolean value _retainFormState_ to True to save and retain the state of the form.

### Considerations for Communications APIs {#considerations-for-communications-apis}

#### Form data {#form-data}

Communications APIs accepts both a form design that is typically created in Designer and XML form data as input. To populate a document with data, an XML element must exist in the XML form data for every form field that you want to populate. The XML element name must match the field name. An XML element is ignored if it does not correspond to a form field or if the XML element name does not match the field name. It is not necessary to match the order in which the XML elements are displayed. The important factor is that the XML elements are specified with corresponding values.

Consider the following example loan application form:

![Loan application Form](assets/loanFormData.png)

To merge data into this form design, create an XML data source that corresponds to the form. The following XML represents an XML data source that corresponds to the example mortgage application form.

```XML

<?xml version="1.0" encoding="UTF-8" ?>
- <xfa:datasets xmlns:xfa="http://www.xfa.org/schema/xfa-data/1.0/">
- <xfa:data>
- <data>
    - <Layer>
        <closeDate>1/26/2007</closeDate>
        <lastName>Johnson</lastName>
        <firstName>Jerry</firstName>
        <mailingAddress>JJohnson@NoMailServer.com</mailingAddress>
        <city>New York</city>
        <zipCode>00501</zipCode>
        <state>NY</state>
        <dateBirth>26/08/1973</dateBirth>
        <middleInitials>D</middleInitials>
        <socialSecurityNumber>(555) 555-5555</socialSecurityNumber>
        <phoneNumber>5555550000</phoneNumber>
    </Layer>
    - <Mortgage>
        <mortgageAmount>295000.00</mortgageAmount>
        <monthlyMortgagePayment>1724.54</monthlyMortgagePayment>
        <purchasePrice>300000</purchasePrice>
        <downPayment>5000</downPayment>
        <term>25</term>
        <interestRate>5.00</interestRate>
    </Mortgage>
</data>
</xfa:data>
</xfa:datasets>


```

#### Supported document types {#supported-document-types}

For complete access to the rendering capabilities of the Communications APIs, it is recommended that you use an XDP file as input. In some cases, a PDF file can be used. However, using a PDF file as input has the following limitations:

- A PDF document that does not contain an XFA stream cannot be rendered as PostScript, PCL, or ZPL. Communications APIs can render PDF documents with XFA streams (that is, forms created in Designer) into laser and label formats. If the PDF document is signed, certified, or contains usage rights (applied using AEM Forms Reader Extensions service), it cannot be rendered to these print formats.

<!-- * Run-time options such as PDF version and tagged PDF are not supported for Acrobat forms. They are valid for PDF forms that contain XFA streams; however, these forms cannot be signed or certified. 

#### Email support {#email-support}

For email functionality, you can create a process in AEM Workflows that uses the Email Step. A workflow represents a business process that you are automating. -->

#### Printable areas {#printable-areas}

The default 0.25-inch nonprintable margin is not exact for label printers and varies from printer to printer and from label size to label size. It is recommended that you keep the 0.25-inch margin or reduce it. However, it is recommended that you do not increase the nonprintable margin. Otherwise, information in the printable area does not print properly.

Always ensure that you use the correct XDC file for the printer. For example, avoid choosing an XDC file for a 300-dpi printer and sending the document to a 200-dpi printer.

#### Scripts {#scripts}

A form design that is used with the Communications APIs can contain scripts that run on the server. Ensure that a form design does not contain scripts that run on the client. For information about creating form design scripts, see Designer Help.

<!-- #### Working with Fonts
 Document Considerations for Working with Fonts>> -->

#### Font mapping {#font-mapping}

If a font is installed on a client computer, it is available in the drop-down list in Designer. If the font is not installed, it is necessary to specify the font name manually. The “Permanently replace unavailable fonts” option in Designer can be off. Otherwise, when the XDP file is saved in Designer, the substitution font name is written to the XDP file. This means that the printer-resident font is not used.

To design a form that uses printer-resident fonts, choose a typeface name in Designer that matches the fonts that are available on the printer. A list of fonts that are supported for PCL or PostScript are located in the corresponding device profiles (XDC files). Alternatively, font mapping can be created to map nonprinter-resident fonts to printer-resident fonts of a different typeface name. For example, in a PostScript scenario, references to the Arial® font can be mapped to the printer-resident Helvetica® typeface.

Two types of OpenType® fonts exist. One type is a TrueType OpenType® font that PCL supports. The other is CFF OpenType®. PDF and PostScript output supports embedded Type-1, TrueType, and OpenType® fonts. PCL output supports embedded TrueType fonts.

Type-1 and OpenType® fonts are not embedded in PCL output. Content that is formatted with Type-1 and OpenType® fonts is rasterized and generated as a bitmap image that can be large and slower to generate.

Downloaded or embedded fonts are automatically substituted when generating PostScript, PCL, or PDF output. This means that only the subset of the font glyphs that are required to properly render the generated document is included in the generated output.

#### Working with device profile files (XDC file) {#working-with-xdc-files}

A device profile (XDC file) is a printer description file in XML format. This file enables the Communications APIs to output documents as laser or label printer formats. Communications APIs use the XDC files including these:

- hppcl5c.xdc

- hppcl5e.xdc

- ps_plain_level3.xdc

- ps_plain.xdc

- zpl300.xdc

- zpl600.xdc

- zpl300.xdc

- ipl300.xdc

- ipl400.xdc

- tpcl600.xdc

- dpl300.xdc

- dpl406.xdc

- dpl600.xdc

It is not necessary to modify these files to create documents. However, you can modify them to meet your business requirements.

These files are sample XDC files that support the features of specific printers, such as resident fonts, paper trays, and stapler. The purpose of these samples is to help you understand how to set up your own printers by using device profiles. The samples are also a starting point for similar printers in the same product line.

#### Working with the XCI configuration file {#working-with-xci-files}

Communications APIs use an XCI configuration file to perform tasks, such as controlling whether the output is a single panel or paginated. Although this file contains settings that can be set, it is not typical to modify this value. <!-- The default.xci file is located in the svcdata\XMLFormService folder. -->

You can pass a modified XCI file while using a Communications API. When doing so, create a copy of the default file, change only the values that requires modification to meet your business requirements, and use the modified XCI file.

Communications APIs start with the default XCI file (or the modified file). Then it applies values that are specified using the Communications APIs. These values override XCI settings.

The following table specifies XCI options.

| XCI option                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| config/present/pdf/creator            | Identifies the document creator using the Creator entry in the Document Information dictionary. For information about this dictionary, see the PDF Reference guide.                                                                                                                                                                                                                                                                                                                                         |
| config/present/pdf/producer           | Identifies the document producer using the Producer entry in the Document Information dictionary. For information about this dictionary, see the PDF Reference guide.                                                                                                                                                                                                                                                                                                                                       |
| config/present/layout                 | Controls whether the output is a single panel or paginated.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| config/present/pdf/compression/level  | Specifies the degree of compression to use when generating a PDF document.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| config/present/pdf/scriptModel        | Controls whether XFA-specific information is included in the output PDF document.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| config/present/common/data/adjustData | Controls whether the XFA application adjusts the data after merging.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| config/present/pdf/renderPolicy       | Controls whether the generation of page content is done on the server or deferred to the client.                                                                                                                                                                                                                                                                                                                                                                                                            |
| config/present/common/locale          | Specifies the default locale used in the output document.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| config/present/destination            | When contained by a present element, specifies the output format. When contained by an openAction element, specifies the action to perform upon opening the document in an interactive client.                                                                                                                                                                                                                                                                                                              |
| config/present/output/type            | Specifies either the type of compression to apply to a file or the type of output to produce.                                                                                                                                                                                                                                                                                                                                                                                                               |
| config/present/common/temp/uri        | Specifies the Form URI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| config/present/common/template/base   | Supplies a base location for URIs in the form design. When this element is absent or empty, the location of the form design is used as the base.                                                                                                                                                                                                                                                                                                                                                            |
| config/present/common/log/to          | Controls the location that log data or output data is written to.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| config/present/output/to              | Controls the location that log data or output data is written to.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| config/present/script/currentPage     | Specifies the initial page when the document is opened.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| config/present/script/exclude         | Informs to AEM Forms server/Communications APIs which events to ignore.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| config/present/pdf/linearized         | Controls whether the output PDF document is linearized.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| config/present/script/runScripts      | Controls which set of scripts AEM Forms executes.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| config/present/pdf/tagged             | Controls the inclusion of tags into the output PDF document. Tags, in the context of PDF, are additional information included in a document to expose the logical structure of the document. Tags assist accessibility aids and reformatting. For example, a page number may be tagged as an artifact so that a screen reader does not enunciate it in the middle of the text. Although tags make a document more useful, they also increase the size of the document and the processing time to create it. |
| config/present/pdf/version            | Specifies the version of PDF document to generate.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

### Known issues

- Ensure that the size of the template and XCI configuration files is larger than 16KB.

- Ensure that the data xml file does not contain the XML declaration header. For example, `<?xml version="1.0" encoding="UTF-8"?>`

- For a batch configuration, only one instance of combination of values of OutputType(PDF, PRINT) and RenderType(PostScript, PCL, IPL, ZPL, etc.) is allowed.

- Do not modify the Data Source USC Configuration/Azure Cloud Configuration used in a batch configuration while the batch is being run. Even after execution, if any update is required, create a copy of configuration instead of updating the one used in an existing batch configuration. 

### Best Practices 

- Adobe recommends to host data files blob container store in the cloud region used by AEM Cloud Service.

<!-- Using API

 There are two main Communications APIs. The _generatePDFOutput_ generates PDFs, while the _generatePrintedOutput_ generates PostScript, ZPL, and PCL formats. These APIs are available as HTTP endpoints on your environment, both on author and publish instances. Since the publish instances are configured to scale faster than the author instances, it is recommended use these APIs via publish instances.

The first parameter of both the operations accept the path and name of the template file (for example ExpenseClaim.xdp). You can specify a fully qualified path, reference path of your AEM Repository, or path of a binary file. The second parameter accepts an XML document that is merged with the template while generating the output document. -->


