---
title: Communication Creation Job
description: Learn about the Brand Experience Agents's communication creation job and how to use natural language to create Interactive Communications.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
exl-id: 49111cdb-e714-4590-8b81-382377083d6e
---

# Communication Creation skill {#ic-creation-skill}

>[!NOTE]
>
> The communications creation job is currently in alpha. If you would like to participate, please send a request from your official email address to [aem-forms-ea@adobe.com.](mailto:aem-forms-ea@adobe.com)

[Interactive Communications](/help/forms/introduction-to-interactive-communication.md) are personalized, data-driven documents designed for business correspondence such as account statements, policy documents, bills, welcome kits, and benefit notices. Unlike forms that collect input from users, Interactive Communications generate output documents with dynamic, recipient-specific content.

The communication creation job is a capability of the [Brand Experience Agent](/help/ai-in-aem/agents/brand-experience/overview.md) that is designed to develop Interactive Communications using natural language prompts. This job automatically generates personalized, data-driven correspondence for print (in PDF format). The job is surfaced through AI Assistant.

Some of the key benefits of communication creation job include:

* **Accelerated communication development**: Create communications quickly using simple natural language commands, eliminating the need for learning traditional product interfaces.
* **Consistent and on-brand correspondence**: Create communications that follow your organization's branding, templates, and style guidelines by using approved templates and styles.
* **Lower technical barrier**: Allow business users to create communications easily, without needing advanced technical or deep product expertise.

## Capabilities {#capabilities}

<!-- * **Create personalized communications with plain text prompt**: You can create communication documents for print (in PDF format) by submitting your requirements in plain language. The job automatically generates appropriate document structures, layouts, and data bindings based on your natural language description. -->

* **Create from templates**: You can use approved organizational templates to ensure brand consistency and compliance standards. The job leverages your existing templates and style guidelines to create on-brand correspondence that meets regulatory requirements.

* **Import and convert existing image and documents into Interactive Communications**: You can import and transform existing documents into Interactive Communications. The job analyzes uploaded content to detect fields, preserve layouts, and create data-driven correspondence with dynamic content capabilities. Supported formats include PDFs, images (JPG, PNG), and hand-drawn templates.

## Sample prompts {#sample-prompts}

* *Create a communication for a loan statement using the template at https://[aem-author-url]/path/to/pdf/file*
* *Create a communication from PDF at https://[aem-author-url]/path/to/pdf/file*
* *Create a communication from image file at https://[aem-author-url]/path/to/image/file*
* Create a letter using PDF file at https://[aem-author-url]/path/to/pdf/file

## Refine your communication {#refine-with-ic-editor}

After creating your initial communication structure using AI Assistant, you can use the Interactive Communications Editor to refine and enhance your document. In Interactive Communications Editor, you can provide prompts in natural language to:

* **Add fields and content**: Add new fields, text blocks, images, charts, tables, and other components to your communication documents using natural language prompts. The job interprets your instructions and inserts the appropriate elements with proper structure and formatting.

* **Edit fields and content**: Modify existing fields and content within your communication documents through conversational commands. Update field properties, change text content, adjust data bindings, and refine component configurations.

* **Remove fields and content**: Delete unwanted fields, components, or sections from your communication documents using natural language instructions. The job removes the specified elements while maintaining document structure and layout integrity.

* **Style fields and content**: Apply formatting and styling to fields and content through natural language prompts. Adjust fonts, colors, alignment, spacing, and other visual properties to match your brand guidelines and design requirements.

### Sample prompts for refining communications {#sample-prompts-refining}

* *Generate a Vehicle Insurance Claim Settlement letter*
* *Make the disclaimer text italic*
* *Change the font size of the disclaimer text to 12*
* *Update the font color of the disclaimer text to red*
* *Update the background color of the header and footer text boxes to light gray*
* *Add a new disclaimer panel with signature and confirmation fields*
* *Remove the confirmation text field*
* *Add a payment details table with three columns*
* *Update the alignment of the policy number field to center*
* *Change the line spacing of the terms and conditions section to 1.5*

For more information on capabilities of Interactive Communication editor, see [Interactive Communications documentation.](/help/forms/introduction-to-interactive-communication.md)
