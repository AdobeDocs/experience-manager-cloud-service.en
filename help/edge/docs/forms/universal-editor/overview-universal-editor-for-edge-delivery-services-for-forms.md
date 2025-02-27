---
title: Universal Editor for Edge Delivery Services for Forms 
description: Use Universal Editor for Edge Delivery Services for Forms to create Adaptive Forms.
feature: Edge Delivery Services
role: Admin, Architect, Developer
hide: yes
hidefromtoc: yes
exl-id: d711e0d1-a2fc-4aa6-af87-6e77a7bc5d2e
---

# Universal Editor for Edge Delivery Services for Forms

<span class="preview"> This feature is available through the early access program. To request access, send an email from your official address to <a href="mailto:aem-forms-ea@adobe.com">aem-forms-ea@adobe.com</a> with your GitHub organization name and repository name. For example, if the repository URL is https://github.com/adobe/abc, the organization name is adobe and the repository name is abc.</span> 

The Universal Editor revolutionizes form creation for Adobe Edge Delivery Services by offering a simple, visual, and intuitive What You See Is What You Get (WYSIWYG) interface. Designed for content creators and form authors, it eliminates the complexity of traditional form-building processes, making it accessible even to non-technical users.

With the Universal Editor, you can quickly design responsive, interactive forms using pre-built components like text fields, checkboxes, and radio buttons. Its robust feature set supports dynamic rules, seamless data integration, and advanced personalization, ensuring every form is tailored to your needs.

Whether you're managing lightweight client-side rendering, ensuring cross-browser compatibility, or adhering to strict accessibility standards, the Universal Editor delivers a streamlined solution for creating and managing forms.

![Universal Editor](/help/edge/docs/forms/universal-editor/assets/universal-editor.png){width=80%, align-center} --> 

## Key Features of Universal Editor for Edge Delivery Services for Forms



Here's the layout with equal-width cards (using fixed-width columns):

| ![WYSIWYG Interface](/help/edge/docs/forms/universal-editor/assets/generate-forms.svg) |  ![Rule Editor](/help/edge/docs/forms/universal-editor/assets/rule-editor.svg) | ![Submit Actions](/help/edge/docs/forms/universal-editor/assets/submit-actions.svg) |
|:-------------:|:-------------:|:-------------:|
| [**WYSIWYG Interface**](/help/edge/docs/forms/universal-editor/universal-editor-user-interface.md) | [**Rule Editor**](/help/edge/docs/forms/universal-editor/rule-editor-universal-editor.md) | [**Submit Actions**](/help/edge/docs/forms/universal-editor/submit-action.md) |
| Universal Editor provides a WYSIWYG interface for form design with a pre-built component library, responsive design, template-based creation, and real-time field modifications. | The rule editor lets users create dynamic form interactions using event-driven rules, instant validation, and error handling via lightweight JavaScript and JSON. | Submit Actions support backend integration, conditional submission logic, secure endpoints, and pre-processors, streamlining submission workflows. |

| ![Publishing/Unpublishing](/help/edge/docs/forms/universal-editor/assets/publish-unpublish.svg) | ![Responsive Mode](/help/edge/docs/forms/universal-editor/assets/responsive.svg) | ![Custom Components](/help/edge/docs/forms/universal-editor/assets/custom-components.svg) |
|:-------------:|:-------------:|:-------------:|
| [**Publishing/Unpublishing**](/help/edge/docs/forms/universal-editor/publish-forms.md) | [**Responsive Mode**](/help/edge/docs/forms/universal-editor/responsive-layout.md) | [**Custom Components**](/help/edge/docs/forms/universal-editor/create-custom-component.md) |
| Easily control the visibility of your forms—publish or unpublish them directly from the editor with just a few clicks. | Design forms that adapt seamlessly across devices (desktops, tablets, and mobile). Use the responsive mode to preview and test forms for various screen sizes. | Custom components allow developers to extend form capabilities by creating unique elements tailored to specific organizational use cases. |

| ![Styling](/help/edge/docs/forms/universal-editor/assets/personalization.svg) | ![Pre-fill Services](/help/edge/docs/forms/universal-editor/assets/prefill-services.svg) | ![A/B Testing](/help/edge/docs/forms/universal-editor/assets/experimentation-ab-testing.svg) |
|:-------------:|:-------------:|:-------------:|
| [**Styling**](/help/edge/docs/forms/universal-editor/style-theme-forms.md) | **Pre-fill Services** (Coming Soon) | [**A/B Testing**](https://github.com/adobe/aem-experimentation/blob/main/documentation/experiments.md) |
| Styling with CSS enables developers to customize the appearance of form elements and create a visually appealing design that aligns with the website aesthetics. | Pre-fill Services automatically populate form fields with relevant user data from various sources, reducing manual input and enhancing user experience. | A/B testing enables organizations to experiment with different form designs, layouts, and features to identify the best-performing variants. |

| ![Analytics & Tracking](/help/edge/docs/forms/universal-editor/assets/analyticsandtracking.svg) | ![Task Management](/help/edge/docs/forms/universal-editor/assets/adobe-workfront.svg) | ![Data Binding](/help/edge/docs/forms/universal-editor/assets/data-binding.svg) |
|:-------------:|:-------------:|:-------------:|
| [**Analytics & Tracking**](https://www.aem.live/developer/martech-integration) | **Task Management** (Coming Soon)| **Data Binding** (Coming Soon) |
| Gain insights into user behavior, form interactions, and submission rates with built-in analytics and tracking to enable data-driven form optimization. | Integration with Adobe Workfront lets teams manage tasks for form creation and maintenance, ensuring streamlined workflows. | Data binding enables direct connections between form fields and backend data sources, supporting real-time updates and advanced data mapping. |

| ![CAPTCHA](/help/edge/docs/forms/universal-editor/assets/captcha.svg) | ![Embedding Forms](/help/edge/docs/forms/universal-editor/assets/embedding-forms.svg) | ![Thank You Configuration](/help/edge/docs/forms/universal-editor/assets/thank-you.svg) |
|:-------------:|:-------------:|:-------------:|
| [**CAPTCHA**](/help/edge/docs/forms/universal-editor/recaptcha-forms.md) | **Embedding Forms** | [**Thank You Configuration**](/help/edge/docs/forms/universal-editor/submit-action.md#show-a-custom-thank-you-message-on-adaptive-form-submission-submit-action-message-ue) |
| Use reCAPTCHA to protect forms from automated bots, ensuring secure and reliable data collection. | Embed forms directly into Edge Delivery Services Sites pages using the Universal Editor's built-in embed component. | Easily customize the acknowledgment message or page shown to users after successful form submission. |


<!-- ![Universal Editor](/help/edge/docs/forms/universal-editor/assets/generate-forms.svg)  **WYSIWYG interface for Form creation**: Universal Editor provides a WYSIWYG interface for form design. It provides pre-built component library, responsive design support, and template-based form creation. You can instantly add or remove form fields and modify field properties (like label, data binding, validation). You can also plugin custom form components to Universal Editor.


* **Rule editor**: The rule editor stands out as a powerful mechanism for creating sophisticated form interactions. It supports event-driven rules, instant validation, and error handling through lightweight JavaScript and JSON-based definitions. This allows developers to implement complex form logic, such as conditional field visibility, automatic calculations, and dynamic form behaviour without extensive coding.

* **Submit actions**: Submit Actions enable form submission workflows. These actions provide comprehensive backend integration options, supporting protocols like REST API. The system allows you configure data pre-processors for automatic data transformation, conditional submission logic based on form field values, and secure endpoint connections. Organizations can define complex submission rules that validate data, and manage form responses with granular control.

* **Pre-fill services:** Pre-fill Services enhance user experience by intelligently populating form fields with relevant data. These services connect to various data sources, including user profiles, browser local storage, and external databases. The mechanism supports dynamic data population, enabling automatic completion of form fields based on contextual information. Users benefit from reduced manual data entry, while administrators gain flexibility in configuring pre-fill rules across different form types and scenarios. The pre-fill functionality adapts to different authentication methods, including session-based approaches and token-based systems, ensuring both convenience and security.

* **Data binding capabilities**: Data binding in the Universal Editor enables direct, dynamic connections between form fields and backend data sources. This feature allows real-time synchronization of form data, supporting complex data mapping scenarios. The system supports transforming form inputs into structured database records with minimal configuration. Advanced mapping supports nested data structures, allowing complex form designs to interact seamlessly with intricate data models.

* **Internationalization/localization capabilities**: Internationalization support ensures global accessibility, with multi-language rendering, right-to-left language compatibility, and locale-specific formatting.

* **Analytics and tracking mechanisms**: The built-in analytics and tracking mechanisms provide comprehensive insights into form interactions, submission rates, and user behavior, enabling continuous optimization of form design and performance. 

* **Experimentation (A/B Testing)**: The Universal Editor supports experimentation by allowing organizations to run A/B tests on form designs to identify the best-performing layouts or features.

* **Task Management via Adobe Workfront**: Integration with Adobe Workfront allows teams to manage tasks related to form creation and maintenance, ensuring streamlined collaboration and efficient workflows.

* **Editor Customization via UI Extension**: Developers can extend the functionality of the Universal Editor through UI extensions, enabling tailored solutions that fit specific organizational needs. --> 

## Pre-built Form Components

The Universal Editor provides the following form components out of the box:

<table>
  <thead>
    <tr>
      <th></th> 
      <th>Form Components</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="22"><img src="/help/edge/docs/forms/universal-editor/assets/adaptive-forms-components.png" alt="Form Components" style="width: 100%;"></td> 
      <td><b>Accordion</b></td>
      <td>Collapsible panel structure for organizing content.</td>
    </tr>
    <tr>
      <td><b>Button</b></td>
      <td>Adds interactive elements for actions like navigation or custom logic.</td>
    </tr>
    <tr>
      <td><b>Captcha</b></td>
      <td>Prevents spam by requiring users to complete a human verification task using Google reCaptcha or HCaptcha.</td>
    </tr>
    <tr>
      <td><b>Checkbox</b></td>
      <td>Allows users to configure a checkbox.</td>
    </tr>
    <tr>
      <td><b>Checkbox Group</b></td>
      <td>Allows users to select multiple options from a group.</td>
    </tr>
    <tr>
      <td><b>Date Picker</b></td>
      <td>Allows users to select a date using a calendar interface.</td>
    </tr>
    <tr>
      <td><b>Drop-Down Lists</b></td>
      <td>Offers single or multi-select options from a predefined list.</td>
    </tr>
    <tr>
      <td><b>Email</b></td>
      <td>Captures email addresses with basic format validation.</td>
    </tr>
    <tr>
      <td><b>File Attachment</b></td>
      <td>Enables uploading of documents, images, or other file types.</td>
    </tr>
    <tr>
      <td><b>Form Fragments</b></td>
      <td>Reusable form components for sections like address fields or contact details.</td>
    </tr>
    <tr>
      <td><b>Image</b></td>
      <td>Supports uploading and displaying images within forms.</td>
    </tr>
    <tr>
      <td><b>Modal</b></td>
      <td>Displays a pop-up dialog box, often used for alerts, additional information, or confirmation.</td>
    </tr>
    <tr>
      <td><b>Numeric Field</b></td>
      <td>Captures numeric input, allowing validation of numbers or ranges.</td>
    </tr>
    <tr>
      <td><b>Panel</b></td>
      <td>Organizes form sections with expandable/collapsible panels.</td>
    </tr>
    <tr>
      <td><b>Radio Buttons</b></td>
      <td>Enables single-choice selection from a group of options.</td>
    </tr>
    <tr>
      <td><b>Rating</b></td>
      <td>Allows users to provide a star-based rating.</td>
    </tr>
    <tr>
      <td><b>Reset Button</b></td>
      <td>Resets the form fields to their default state.</td>
    </tr>
    <tr>
      <td><b>Submit Button</b></td>
      <td>Triggers form submission and initiates defined workflows.</td>
    </tr>
    <tr>
      <td><b>Telephone Number Field</b></td>
      <td>Captures phone numbers with formatting based on country.</td>
    </tr>
    <tr>
      <td><b>Text</b></td>
      <td>Provides a dedicated section for displaying legal terms and collecting user agreement through checkboxes.</td>
    </tr>
    <tr>
      <td><b>Text Field</b></td>
      <td>DCaptures single-line input, such as names or email addresses.</td>
    </tr>
    <tr>
      <td><b>Wizard</b></td>
      <td>Guides users step-by-step through a multi-part form process.</td>
    </tr>
  </tbody>
</table>

<!-- * Footer: Adds a footer section for consistent design or additional information.
* Form Container: Wraps all form elements and manages overall form properties.
* Header: Adds a header section for form titles, branding, or instructions.-->
<!-- * 
* Prefillable Fields: Automatically populates form fields with data from predefined sources such as user profiles or APIs. 

* Switches/Toggle Buttons: Provides binary on/off choices for user input.


* Title: Adds a text-based heading or label to improve form clarity and organization.


In-addtion to pre-built form components, the Universal editor also provides support for:

* **Embedding Forms in Another Webpage**: The Universal Editor supports embedding forms directly into Edge Deliver Services Sites pages. This can be done using the embed component provided out of the box.

* **Validation Messages**: Validation messages provide real-time feedback to users when they enter incorrect or incomplete data. Features include:
    * Dynamic Error Display: Instantly alerts users to errors, such as invalid email addresses or missing required fields.
    * Customizable Messages: Allows form authors to define user-friendly error texts.
    * Rule-Based Validation: Supports advanced validation logic, such as checking dependencies between fields or implementing conditional rules.

* **Hidden Fields**: Hidden fields store data invisibly within the form, often for backend processing or prefilled values. Use cases include:
    * Passing contextual information (e.g., user ID or session data) to the backend without displaying it to users.
    * Capturing metadata like timestamps or tracking IDs.
    * Hidden fields are not visible to end-users but can be prefilled, updated dynamically, or used in workflows.

* **Custom Components**: Custom components allow developers to extend the functionality of forms by creating specialized or third-party integrations. Features include:
    * Flexibility: Developers can design unique form elements tailored to specific use cases.
    * Third-Party Integration: Embed widgets or tools like payment gateways, analytics trackers, or AI-driven input fields.
    * Seamless Compatibility: Custom components can integrate with the Universal Editor's drag-and-drop interface and existing features like data binding or validation.

* **Thank you Configuration**: Customize the acknowledgment message or page shown after form submission.
--> 


## Onboarding

To enable the Universal Editor and its advanced features like Rule Editor write to us at aem-forms-ea@adobe.com from your official email id . The Adobe team is here to assist you in transforming your form-building experience.

## Frequently asked questions (FAQ)

**Q. Who can use the Universal Editor?**
The Universal Editor is designed for a broad audience, including:

* Content creators who want to build visually appealing forms.
* Developers who need advanced customization and integration capabilities.
* Organizations looking for scalable, secure, and compliant form solutions.

**Q: Can I integrate forms created with the Universal Editor into my existing systems?**
Absolutely. The Universal Editor supports seamless data binding with backend systems, enabling real-time updates and advanced data mapping. It also integrates with tools like Adobe Workfront for task management and supports secure endpoints for data submission workflows.

**Q: Is it possible to customize the form components?**
Yes, the Universal Editor allows developers to create custom components tailored to specific organizational needs. Additionally, you can extend the functionality of the editor through UI extensions and custom workflows.

**Q: How does the Universal Editor handle accessibility?**
The Universal Editor is designed with strict adherence to accessibility standards, including WCAG (Web Content Accessibility Guidelines). This ensures that the forms are usable by individuals with disabilities, providing an inclusive experience.

**Q: What kind of analytics can I get from the forms?**
The Universal Editor includes built-in analytics and tracking tools to monitor user interactions, form submission rates, and conversion metrics. These insights help optimize your forms for better performance.


## Start creating forms

{{universal-editor-see-also}}

