---
title: Form creation skill
description: Learn about the Experience Production Agent's form creation skill and how to use natural language to create forms from scratch.
feature: Edge Delivery Services, Agentic AI
role: Admin, Architect, Developer
---

# Form Creation Skill {#form-creation-skill}

The form creation skill is a capability of the Experience Production Agent that is designed to develop forms using natural language interactions. It enables users to create digital forms without traditional manual processes. This skill eliminates the complexity of form creation by interpreting conversational prompts and automatically generating appropriate form structures, field types, validation rules, and business logic. The skill is surfaced through in AI assistant and Experience Hub.

Some of the key benefits of form creation skill include:

* **Accelerated form development**: Create forms quickly using
simple natural language commands, eliminating the need for learning traditional product interfaces.
* **Consistent and on-brand experiences**: Create forms that follow your organization's branding, templates, and style guidelines by using approved templates and styles.
* **Lower technical barrier**: Allows business users to create forms easily, without needing advanced technical or deep product expertise.

## Use cases and sample prompts {#use-cases-prompts}

The form creation skill allows you to create on-brand form experiences by submitting your requirements in plain language. 

You are prompted to choose the type of form to create, specify either a Core Components based adaptive forms template or an Edge Delivery Services based adaptive forms template and indicate your preferred path to save the form. If you are creating a form based on Edge Delivery Services, you can also specify the GitHub URL of your repository.

Based on these selections, the form creation skill automatically generates the appropriate form.


### Simple prompts {#sample-prompts}

* *Create an empty adaptive form*
* *Create a form for feedback collection with name, email, and message fields*
* *Create a customer feedback form with product rating (1-5 stars), comment field, and optional email*
* *Build a contact form with name, email, subject dropdown, and message fields*
* *Create a registration form with personal information, account preferences, and terms acceptance*
* *Create a credit card application form using the fsi theme and blank template*
* Generate forms using predefined boilerplates from GitHub repositories, ensuring consistency and best practices across your organization.
* *Create a form using the boilerplate at <https://github.com/adobe-rnd/aem-forms-boilerplate>*


## Next Steps {#refine-with-forms-experience-builder}

After creating your initial form structure using AI Assistant or Experience Hub, you can use Forms Experience Builder to refine and enhance your form:

* **Incremental field building**: Add or modify individual fields, adjust field types, and configure field properties through the visual editor.

* **Conditional logic and validations**: Create show/hide rules, set up field dependencies, and define validation rules for data quality.

* **Ongoing form updates**: Edit and update form structures, layouts, and styling as your requirements evolve.

* **Submit actions configuration**: Set up where form data goes after submission, configure email notifications, integrate with workflows, or connect to external systems.

* **Advanced customization**: Fine-tune form behavior, add calculations, configure prefill options, and optimize user experience.

For more information, see [Forms Experience Builder documentation](/help/forms/experience-builder/product-overview.md).

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
