---
title: AEM Forms Edge Delivery Services Overview
description: AEM Forms Edge Delivery Services built for peak performance, empowering you to envision the future of streamlined data collection and user engagement.
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
exl-id: ecea1e05-d36b-4d63-af9d-c69dafd2f94f
---
# AEM Forms Edge Delivery Services 

Streamline form creation and drive higher completion rates with Adobe's AEM Forms Edge Delivery Services. These powerful, composable service empowers you to build enterprise-grade forms with exceptional performance and visual appeal. AEM prioritizes both the user experience and your business goals, ensuring lightning-fast loading times and increased form conversions.

You can use the service to:

* **Build exceptional enrollment experiences**: Build enrollment experiences that load and render quickly, even on slow internet connections. Faster loading times and optimized user experience contribute to higher form completion rates and improved conversion rates. 

* **Create enrollment experiences with tools of your choice**: Increase authoring efficiency by decoupling content sources. Out of the box you can use both **document-based authoring** (Microsoft SharePoint or Google Drive) and **AEM authoring** (Adaptive Forms Editor). As such, you can work with multiple content sources on the same form and use your preferred authoring tools, such as Microsoft Excel, Google Sheets, or Adaptive Forms Editor.

* **Use developer friendly toolset:** AEM Forms use plain HTML, modern CSS, and vanilla JavaScript to create exceptional experiences without the usual overhead. Any developer with basic knowledge of HTML, CSS & JS should be able to build their own components and no need to learning any specific language or framework. No need of any pipeline or wait, check-in your code into Github and your changes are live. Additionally, there is no need of any pipeline or wait, check-in your code into Github and your changes are live.


## AEM Forms Edge Delivery Services Overview {#edge-overview}

The following diagram illustrates how you can edit content in Microsoft Excel or Google Sheets (document-based editing) and publish to Edge Delivery Services. It also shows the AEM publishing method using the Adaptive Forms Editor.

![Edge Delivery Architecture](/help/edge/assets/AEM-forms-with-EDS-publishing.png)

Edge Delivery services is a composable set of services that allows for a high degree of flexibility in how you author content on your website. As mentioned previously, you can use both [AEM content management](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/sites/authoring/getting-started/concepts.html) with [AEM authoring](/help/implementing/universal-editor/introduction.md) as well as [document-based authoring](https://www.aem.live/docs/authoring)

For example, you can use content directly from Microsoft Excel or Google Sheets. This means that content from those sources can become forms on your website. The new content is added instantly without a rebuild process.

Edge Delivery Services uses GitHub so customers can manage and deploy code directly from their GitHub repository. For example, you can write forms in either Google Sheets or Microsoft Excel and the components of your forms can be developed by using CSS and JavaScript in GitHub. When you are ready, you can use the Sidekick browser extension to preview and publish content updates.

AEM Forms Edge Delivery Services provides a forms block, known as [Adaptive Forms block](/help/edge/docs/forms/create-forms.md) to add a form to your Edge Delivery Services site.  

### Key Features of AEM Forms Edge Delivery Services 

Document based authoring a basic set of features and AEM authoring unlocks additional capabilities beyond the document-based authoring, empowering you to build more complex and interactive forms. The following table highlights key features for both:

<!-- 

>[!BEGINTABS]

>[!TAB Document-based authoring]

Document-based authoring is a versatile option suitable for creating simple forms with essential functionalities. It allows you to integrate various input types like text fields, dropdown menus, and radio buttons, enabling you to collect user data effectively. It offers a basic version of rules to add dynamic behaviour to forms. Key features of Document-based authoring are: 

* **[HTML5-based Form Field components](/help/edge/docs/forms/form-components.md)**: AEM Forms Edge Delivery Services allow you to create user-friendly and interactive forms using form components based on HTML5 [input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#input_types), <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea">textarea</a>, <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select">select</a>, and <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset">fieldset</a>  elements. These components cater to different types of data collection and can be easily customized to fit your specific needs.  

* **Accessibility**: The fields in the form block are accessible. Each label is linked with its respective input element, and IDs are auto-generated for linking. Descriptions associated with fields are linked via the aria-describedby attribute. Keyboard navigation using the standard Tab/Shift + Tab keys is supported.

* **[Styling](/help/edge/docs/forms/style-theme-forms.md)**: Each form field has a fixed HTML structure that can be easily decorated using custom CSS or JavaScript files. Selectors for targeting fields in CSS and JS are provided based on type and name. You can easily create new selectors due to the standradized structure and style your form. 

* **Basic Rules**: Easily create logic that adjusts field visibility, validation, and behavior based on user input or predefined conditions. Rules offer a flexible and intuitive way to add intelligence to your forms, ensuring they adapt seamlessly based on user inputs.

* **Validations**: Before submission, the form is validated, and invalid fields are appropriately marked with error messages displayed to the user. Adaptive Forms block support all the HTML form validation, supported by modern browsers, and provide additional validation mechanism like validation script, file size, file type, overall file size, and more. 

* **File Uploads**: You can add file attachment capabilities to your forms. Whether you need to gather documents, images, or other files from your users, file upload functionality serves you effortlessly. With custom handling options available, you can tailor the file upload process to suit your specific requirements.

* **reCAPTCHA**: Benefit from seamless integration of Google reCAPTCHA into your forms with our out-of-the-box (OOTB) support. Safeguard your forms against fraudulent activities, spam, and abuse, while maintaining a smooth and uninterrupted user experience. Adaptive Forms block supports reCaptcha V3 and reCaptcha Enterprise. 

* **Send email notification on form submission**: Eliminate the hassle of manual follow-ups and ensure timely communication with our built-in email automation for form submissions. This integrated solution lets you effortlessly notify relevant parties, including sending form data, whenever someone fills out a form on your website. No need for complex configurations or additional tools – it's ready to use out of the box.

>[!TAB AEM Authoring]

AEM Authoring unlocks additional capabilities beyond the document-based authoring, empowering you to build more complex and interactive forms. In additon to the features of Document-based authoring, AEM authoring offers the following additional features:  

* Advanced Rules: Define logic-based actions within your forms. You can use rules to conditionally show or hide form sections, pre-populate fields based on user input, and perform various validations to ensure data integrity.

* Server-side extensibility: Extend the functionalities of your forms by integrating them with server-side logic. This allows you to perform complex calculations, interact with external systems, and automate specific tasks based on user actions within the form.
* Streamline workflows and data management: Leverage the power of AEM to:
    * Design user-friendly forms using AEM editors.
    * Generate a "Document of Record" for secure and tamper-proof archiving of submitted data.
    * Facilitate e-signing with Adobe Sign for a smooth and secure signing experience.
    * Automate business processes through AEM workflows, triggering actions based on form submissions.
    * Effortlessly integrate with various data sources, enabling seamless data flow and exchange.

>[!ENDTABS]



## Start creating forms

-->

|                                           | Document-based authoring | AEM Authoring (Adaptive Forms Editor) |
| ----------------------------------------- | ------------------------ | ------------------------------------ |
| **Form Functionality**                       |                          |                                      |
| Accessible components                     | &#10003;                 | &#10003;                             |
| Standardized HTML structure               | &#10003;                 | &#10003;                             |
| Rules and Validations                     | &#10003;                 | &#10003;                             |
| File Attachments (File Upload)            | &#10003;                 | &#10003;                             |
| Google reCAPTCHA                          | &#10003;                 | &#10003;                             |
| Custom components                         | &#10003;                 | &#10003;                             |
| Submit to email                           | &#10003;                 | &#10003;                             |
| **Advanced Features**                        |                          |                                      |
| Advanced Rules with visual rule editor    |                          | &#10003;                             |
| Server-side extensibility                 |                          | &#10003;                             |
| Multiple Submit Actions                   |                          | &#10003;                             |
| **Form Design and Management**               |                          |                                      |
| Adaptive Forms editor for WYSIWYG editing |                          | &#10003;                             |
| **Integrations**                              |                          |                                      |
| Document of Record                        |                          | &#10003;                             |
| Integration with Adobe Sign               |                          | &#10003;                             |
| Inegration with Adobe Analytics           |                          | &#10003;                             |
| Integration with Marketo                  |                          | &#10003;                             |
| Integration with multiple data sources    |                          | &#10003;                             |
| Multiple Submit Actions                   |                          | &#10003;                             |


## Start creating forms

* [Getting started - developer tutorial](/help/edge/docs/forms/tutorial.md)
* [Create a form using Google Sheets or Microsoft Excel](/help/edge/docs/forms/create-forms.md)
* [Submit forms directly to your Microsoft Excel or Google Sheets](/help/edge/docs/forms/submit-forms.md)
* [Enhance the look of your forms: a guide to styling](/help/edge/docs/forms/style-theme-forms.md)


<!-- 

## Start creating forms

<div>

  <style>
    .card-container {
        width: calc(33.33% - 10px);;
        margin: 5px;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 5px;
        box-sizing: border-box;
        transition: background-color 0.3s ease; /* Adding transition effect */
    }
    .card-container:hover {
        background-color: #f0f0f0; /* Changing background color on hover */
    }
</style>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin: -5px;">
    <div class="card-container">
        <a href="/help/edge/docs/forms/create-forms.md">
            <img src="/help/edge/assets/smock_devices_18_n.svg" alt="Create a form using eds forms" style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Create a form using Google Sheets or Microsoft Excel</b>
        </a>
        <p>Create forms that load and render quickly and automatically reflows on mobile devices.</p>
    </div>
    <div class="card-container">
        <a href="/help/edge/docs/forms/create-forms.md#manually-configure-a-spreadsheet-to-accept-data">   
            <img src="/help/edge/assets/smock_platformdatamapping_18_n.svg" alt="Submit form" alt="Use Form Fragments in an EDS Form" style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Submit form to spreadsheet</b>
        </a>
        <p>Submit forms directly to your Microsoft Excel or Google Sheets.</p>
    </div>
     <div class="card-container">
        <a href="/help/edge/docs/forms/style-theme-forms.md">
            <img src="/help/edge/assets/smock_imageautomode_18_N.svg" alt="Apply styles or themes to an eds form" style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Customize a theme</b>
        </a>
        <p>Create a consistent brand image by applying the same theme across forms.</p>
    </div>
      <div class="card-container">
        <a href="/help/edge/docs/forms/validate-forms.md">
            <img src="/help/edge/assets/smock_condition_18_n.svg" alt="Add validations to form fields" style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Apply field validations</b>
        </a>
        <p>Reduce errors and frustration by checking form inputs for proper formatting.</p>
    </div> 
            <div class="card-container">
        <a href="/help/edge/docs/forms/rules-forms.md">
            <img src="/help/edge/assets/smock_documentfragment_18_n.svg" alt="Use rules to add dynamic behaviour to a form" style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Use rules to add dynamic behaviour to a form</b>
        </a>
        <p>Reuse preconfigured fragments across multiple forms.</p>
    </div>
    <div class="card-container">
        <a href="/help/edge/docs/forms/translate-forms.md">  
            <img src="/help/edge/assets/smock_abc_18_n.svg" alt="Translate an EDS Form" style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Translate a form</b>
        </a>
        <p>Extend the reach of your forms while keeping costs in check.</p>
    </div>
    <div class="card-container">
        <a href="/help/edge/docs/forms/repeatable-forms.md">  
            <img src="/help/edge/assets/smock_addto_18_n.svg" alt="Add repeatable sections to an EDS Form" style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Add repeatable sections</b>
        </a>
        <p>Effortlessly create and add repeatable sections to a form.</p>
    </div>
    <div class="card-container">
        <a href="/help/edge/docs/forms/custom-components-forms.md"> 
            <img src="/help/edge/assets/smock_userdeveloper_18_n.svg" alt="Create custom forms components using standard JavaScript and CSS"  style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Create custom components</b>
        </a>
        <p>Use standard JavaScript and CSS to create components and themes.</p>
    </div>
    <div class="card-container">
        <a href="/help/edge/docs/forms/recaptacha-forms.md">  
            <img src="/help//edge/assets/smock_keyclock_18_n.svg" alt="Use reCAPTCHA in an EDS Form" style="border-radius: 5px;"> </b>
            <br><b style="margin-top: 5px;">Use reCAPTCHA</b>
        </a>
        <p>Use OOTB reCAPTCHA integration for robust spam and bot protection.</p>
    </div>


</div>


</br>


--> 