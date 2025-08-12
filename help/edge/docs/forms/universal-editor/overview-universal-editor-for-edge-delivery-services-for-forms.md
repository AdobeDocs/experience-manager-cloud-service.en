---
title: Universal Editor for Edge Delivery Services for Forms 
description: Use Universal Editor for Edge Delivery Services for Forms to create Adaptive Forms.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: d711e0d1-a2fc-4aa6-af87-6e77a7bc5d2e
---

# Universal Editor for Edge Delivery Services for Forms

The Universal Editor revolutionizes form creation for Adobe Edge Delivery Services by offering a simple, visual, and intuitive What You See Is What You Get (WYSIWYG) interface. Designed for content creators and form authors, it eliminates the complexity of traditional form-building processes, making it accessible even to non-technical users.

With the Universal Editor, you can quickly design responsive, interactive forms using pre-built components like text fields, checkboxes, and radio buttons. Its robust feature set supports dynamic rules, seamless data integration, and advanced personalization, ensuring every form is tailored to your needs.

Whether you're managing lightweight client-side rendering, ensuring cross-browser compatibility, or adhering to strict accessibility standards, the Universal Editor delivers a streamlined solution for creating and managing forms.

![Universal Editor](/help/edge/docs/forms/universal-editor/assets/universal-editor.png){width=80%, align-center} 

## Key Features of Universal Editor for Edge Delivery Services for Forms



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
| [**Styling**](/help/edge/docs/forms/universal-editor/style-theme-forms.md) | **[Pre-fill forms](/help/edge/docs/forms/universal-editor/prefill-form.md)** | [**A/B Testing**](https://github.com/adobe/aem-experimentation/blob/main/documentation/experiments.md) |
| Styling with CSS enables developers to customize the appearance of form elements and create a visually appealing design that aligns with the website aesthetics. | Pre-fill Services automatically populate form fields with relevant user data from various sources, reducing manual input and enhancing user experience. | A/B testing enables organizations to experiment with different form designs, layouts, and features to identify the best-performing variants. |

| ![Analytics & Tracking](/help/edge/docs/forms/universal-editor/assets/analyticsandtracking.svg) | ![Form Fragments](/help/edge/docs/forms/universal-editor/assets/form-fragments.svg) | ![Data Binding](/help/edge/docs/forms/universal-editor/assets/data-binding.svg) |
|:-------------:|:-------------:|:-------------:|
| [**Analytics & Tracking**](https://www.aem.live/developer/martech-integration) | **Form Fragments** (Coming Soon)| [**Data Binding**](/help/edge/docs/forms/universal-editor/integrate-forms-with-data-source.md) |
| Gain insights into user behavior, form interactions, and submission rates with built-in analytics and tracking to enable data-driven form optimization. | Form Fragments enable reusability by allowing commonly used sections to be created once and reused across multiple forms, ensuring consistency and reducing maintenance effort.| Data binding enables direct connections between form fields and backend data sources, supporting real-time updates and advanced data mapping. |

| ![CAPTCHA](/help/edge/docs/forms/universal-editor/assets/captcha.svg) | ![Embedding Forms](/help/edge/docs/forms/universal-editor/assets/embedding-forms.svg) | ![Thank You Configuration](/help/edge/docs/forms/universal-editor/assets/thank-you.svg) |
|:-------------:|:-------------:|:-------------:|
| [**CAPTCHA**](/help/edge/docs/forms/universal-editor/recaptcha-forms.md) | **Embedding Forms** (Coming Soon)| [**Thank You Configuration**](/help/edge/docs/forms/universal-editor/submit-action.md#show-a-custom-thank-you-message-on-adaptive-form-submission-submit-action-message-ue) |
| Use reCAPTCHA to protect forms from automated bots, ensuring secure and reliable data collection. | Embed forms directly into Edge Delivery Services Sites pages using the Universal Editor's built-in embed component. | Easily customize the acknowledgment message or page shown to users after successful form submission. |



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

## Frequently asked questions (FAQ)

**Q. Who can use the Universal Editor?**
The Universal Editor is designed for a broad audience, including:

- Content creators who want to build visually appealing forms.
- Developers who need advanced customization and integration capabilities.
- Organizations looking for scalable, secure, and compliant form solutions.

**Q: Can I integrate forms created with the Universal Editor into my existing systems?**
Absolutely. The Universal Editor supports seamless data binding with backend systems, enabling real-time updates and advanced data mapping. It also integrates with tools like Adobe Workfront for task management and supports secure endpoints for data submission workflows.

**Q: Is it possible to customize the form components?**
Yes, the Universal Editor allows developers to create custom components tailored to specific organizational needs. Additionally, you can extend the functionality of the editor through UI extensions and custom workflows.

**Q: What kind of analytics can I get from the forms?**
The Universal Editor includes built-in analytics and tracking tools to monitor user interactions, form submission rates, and conversion metrics. These insights help optimize your forms for better performance.

**Q: How does the Universal Editor handle accessibility?**
The Universal Editor is designed with strict adherence to accessibility standards, including WCAG (Web Content Accessibility Guidelines). This ensures that the forms are usable by individuals with disabilities, providing an inclusive experience.






