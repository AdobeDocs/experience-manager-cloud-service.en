---
title: Form Creation Job
description: Learn about the Brand Experience Agent's form creation job and how to use natural language to create forms from scratch.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Architect, Developer
exl-id: 24ad5f36-405b-4ea2-9819-de6aea856a7a
---

# Form Creation Job {#form-creation-job}

The form creation job is a capability of the [Brand Experience Agent](/help/ai-in-aem/agents/brand-experience/overview.md) that is designed to develop forms using natural language prompts. This job automatically generates appropriate form structure and  field types. The job is surfaced through AI Assistant.

Some of the key benefits of form creation job include:

* **Accelerated form development**: Create forms quickly using simple natural language commands, eliminating the need for learning traditional product interfaces.
* **Consistent and on-brand experiences**: Create forms that follow your organization's branding, templates, and style guidelines by using approved templates and styles.
* **Lower technical barrier**: Allow business users to create forms easily, without needing advanced technical or deep product expertise.

## Capabilities {#capabilities}

* **Create a new form with plain text prompt**: You can create a form by submitting your requirements in plain language. The skill automatically generates appropriate form structure, field types, and on-brand experiences based on your natural language description and specified template. This capability accelerates form creation while ensuring brand and compliance standards are maintained.

* **Import a PDF document and convert it into form**: You can import and transform existing PDF documents into forms. The skill analyzes uploaded content to detect field types, preserve layouts, and enhance forms with responsive design and validation logic while ensuring brand and compliance standards are maintained.

When you use either of these capabilities, you are prompted to choose the type of form to create. Specify either a Core Components-based adaptive forms template or an Edge Delivery Services-based adaptive forms template and indicate your preferred path to save the form. If you are creating a form based on Edge Delivery Services, you can also specify the GitHub URL of your repository.


### Sample Prompts {#sample-prompts}

* *Create a form for feedback collection with name, email, and message fields*
* *Create a customer feedback form with product rating (1-5 stars), comment field, and optional email*
* *Build a contact form with name, email, subject dropdown, and message fields*
* *Create a registration form with personal information, account preferences, and terms acceptance*
* *Create a credit card application form by importing the PDF file available at `https://[aem-author-url]/path/to/pdf/file`*
* *Create a feedback form using the boilerplate at `https://github.com/wkndforms/wesecure`*

## Refine your Form {#refine-with-forms-experience-builder}

After creating your initial form structure using the AI Assistant, you can use the Forms Experience Builder to:

* **Update forms**: Add or modify fields, adjust field types, and update styling as needed through the visual editor.

* **Update layout**: Rearrange sections, groups, or fields, adjust spacing, and modify the visual hierarchy to enhance usability and ensure your form is clear and intuitive for your audience.

* **Add business logic**: Create conditional logic, show/hide rules, field dependencies, and define validation rules.

* **Configure submission**: Configure where form data is submitted, including setting up email notifications, integrations with workflows, or connections to external systems.

For more information, see [Forms Experience Builder documentation.](/help/forms/experience-builder/product-overview.md)

## Activation {#activation}

You can explore AEM Agents through the [Playground](https://www.aem.live/developer/aem-playground), or connect with your CSM or TAM to discuss access via the Agentic SKU.

<!-- 
#### Import and convert {#import-and-convert}

Transform existing documents into interactive digital forms. The agent analyzes uploaded content to detect field types, preserve layouts, and enhance forms with responsive design and validation logic. Supported formats include Acroforms, XFA PDFs, flat PDFs, images (JPG, PNG), and hand-drawn form photographs.

>[!VIDEO](https://video.tv.adobe.com/v/3474042)

**Prompt examples:**

* *Convert the attached PDF file to an adaptive form*
* *Transform this scanned form image into an interactive digital form*
* *Import the employee onboarding PDF and create an editable form*
* *Convert this paper form photograph into a digital form with validation*
-->

<!-- 
### Embed an existing form to a sites page {#embed-existing-form}

The form creation skill enables seamless integration of existing forms into any sites page through natural language commands. Rather than manually locating, copying, and embedding form components, users can simply specify which form to add and where to place it. The agent handles the technical implementation, ensuring proper rendering and functionality.

>[!VIDEO](https://video.tv.adobe.com/v/PLACEHOLDER)

**Prompt examples:**

* *Embed the contact form to the homepage*
* *Add the existing customer feedback form to the support page*
* *Insert the newsletter signup form into the footer section*
* *Place the registration form on /content/site/signup*
* *Add form "contact-us-2024" to the current page*
-->

<!-- 
### Build and add a form to an existing sites page {#build-and-add-form}

The form creation skill combines form creation and site integration in a single conversational workflow. Users can describe the form they need and specify where to add it, and the agent creates the form and embeds it into the specified page automatically. This eliminates the traditional multi-step process of creating a form separately and then manually adding it to a page.

>[!VIDEO](https://video.tv.adobe.com/v/PLACEHOLDER)

**Prompt examples:**

* *Create a newsletter signup form with email field and add it to the footer*
* *Build a quick contact form with name, email, and message, then add it to /content/about-us*
* *Add a feedback form with rating stars and comment field to this page*
* *Create a simple survey form with 5 questions and embed it on the customer portal homepage*
* *Build an event registration form with name, email, and date selection, then add it to /content/events/conference-2025*
-->
