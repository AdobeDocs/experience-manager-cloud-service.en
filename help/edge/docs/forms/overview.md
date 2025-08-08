---
title: Edge Delivery Services for AEM Forms Overview
description: Create and deliver high-performing forms on Adobe Experience Manager Edge Delivery Services, with an emphasis on the Universal Editor authoring approach.
feature: Edge Delivery Services
exl-id: ecea1e05-d36b-4d63-af9d-c69dafd2f94f
role: Admin, Architect, Developer
---

# Edge Delivery Services for AEM Forms
 

Edge Delivery Services for AEM Forms is a composable set of services that enables a rapid development environment where authors can update, publish, and launch new forms rapidly. These services deliver exceptional and high impact forms experiences that drive engagement and conversions. These forms experiences are easy to author and develop.

These services enable you to:

- **Create enrolment experiences with tools of your choice:** Increase authoring efficiency by decoupling content sources. Out of the box you can use Document-based Authoring (Microsoft SharePoint or Google Drive), WYSIWYG Authoring (Universal Editor or Adaptive Forms Editor). You can work with multiple content sources on the same forms site and use your preferred authoring tools, such as Microsoft Excel, Google Sheets, Universal Editor, or Adaptive Forms Editor.

- **Deliver exceptional Digital Enrolment experiences:** Deliver Digital Enrolment experiences that load and render quickly and continuously monitor your forms performance through Operational Telemetry. Faster loading times and optimized user experience contribute to higher form completion and conversion rates. 

- **Use developer friendly toolset:** Edge Delivery Services for AEM Forms
 uses plain HTML, modern CSS, and vanilla JavaScript to create exceptional experiences, avoiding the steep learning curve of a specific framework. A developer with basic web development skills can customize and easily build form components and experiences. There is no need to wait for a pipeline to run, just check-in your code into GitHub and your changes are live.

## Choosing an authoring method


Adobe Experience Manager (AEM) Edge Delivery Services (EDS) lets you serve blazing-fast, highly scalable web experiences from the edge. This guide explains **how to build and publish forms for those experiences**—with a clear recommendation hierarchy:

- **Universal Editor (UE) – Best choice for most teams**  
- **Document-Based Authoring (Docs/Sheets) – Great for quick, simple forms**  
- **Document Authoring (DA) – Use to embed forms into DA-authored pages**

By the end you will be able to pick the right authoring method, understand submission options, and follow next steps toward production-ready forms.


| Team & Requirement | Recommended Method | Why |
|--------------------|--------------------|-----|
| Marketers / Designers need visual control, conditional logic, or AEM integrations | **Universal Editor** | Drag-and-drop, advanced rules, submits to FSS or AEM Publish |
| Content authors already working in Word / Google Docs / Sheets; simple data capture to spreadsheet/email | **Document-Based Authoring** | Familiar tools, fastest path for basic forms |
| Website pages built in **Document Authoring (DA)** | **Embed** a UE or Doc-Based form into the DA page | DA does not build forms itself |


## Authoring methods in detail

###  Universal Editor 

<!--
<span class="preview"> This is a pre-release feature available through our <a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features">pre-release channel</a>. </span>
-->

[Universal Editor](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) is a visual, drag-and-drop authoring tool for marketers and designers that combines speed with enterprise-grade power:

- Real-time WYSIWYG editing and device previews.
- Direct integration with AEM assets, workflows, and Form Data Model (FDM).
- Seamless hand-off to developers for custom components in vanilla JS/CSS.
- Advanced rules editor for creating complex logic.
- Server-side extensibility for custom functionalities.
- WYSIWYG editing experience for easy form creation and visualization.
- Document of record functionality to create tamper-proof archives of submitted data.
- Integration with Adobe Sign for electronic signatures.
- Integration with Adobe Workfront Fusion to triggering Adobe Workfront Fusion scenarios upon form submission.
- Integration with various data sources for pre-populating forms and submitting data.
- Form Data Model (FDM) for defining data structure and interactions with various data sources.
- Ability to choose from multiple submit actions for handling form submissions, including submitting data to Microsoft SharePoint, Microsoft OneDrive, Adobe Workfront Fusion, Salesforce, Microsoft Dynamics, many more data sources.
- Submit using Forms Submission Service (FSS) or AEM Publish submit actions

**Recommendation**: Start every new form project with Universal Editor unless your team is 100 % document-centric and the form is very basic.


### Document-Based authoring (Using Microsoft Docs or Google Sheets)

[Document-Based authoring](/help/edge/docs/forms/tutorial.md) is best suited for creating simple, low-complexity forms using familiar tools such as Microsoft Word, Google Docs, or Google Sheets. This method is ideal for content teams who require a fast and straightforward way to build forms.

- Accessible components for a user-friendly experience.
- Standardized HTML structure for consistent rendering.
- Rules and validations to ensure data accuracy.
- File attachment options for collecting additional information.
- Google reCAPTCHA integration for spam protection.
- Ability to create custom form components for specific needs.
- Submit form data directly to Microsoft Excel or Google Sheets or email addresses.
- Monitor your forms performance through Operational Telemetry


### Embedding Forms in Document Authoring (DA)

Document Authoring (DA) is designed for creating structured page content and does not support native form creation. To add a form to a DA-authored page, you can create the form using the **Universal Editor** (recommended) or Document-Based Authoring and embed the form to Document Authoring page. 

## Publishing Edge Delivery Services Forms {#edge-overview}

The following diagram illustrates how you can edit forms in Microsoft Excel or Google Sheets (Document-based Authoring) and publish to Edge Delivery Services. It also shows the AEM publishing method using the WYSIWYG Authoring (Universal Editor).

![Publish to Edge Delivery Services and AEM](/help/edge/docs/forms/assets/AEM-forms-with-EDS-publishing.png)


<!-- 
## Feature Comparison

| Capability | Universal Editor | Document-Based | Document Authoring |
|------------|-----------------|----------------|--------------------|
| Visual drag-and-drop | ✅ | – | – |
| Advanced rules editor | ✅ | Limited | – |
| Attachments | ✅ | EA | – |
| reCAPTCHA Enterprise | ✅ | ✅ | Depends on embed |
| Submit to spreadsheet/email | ✅ (FSS) | ✅ (FSS) | Via embed |
| Submit to AEM workflows/FDM | ✅ | – | Via UE embed |
| Custom components (JS/CSS) | ✅ | ✅ | Via embed |
| Localization via Sites | ✅ | Manual | Via embed |

-->

## Next Steps

- [Features and capabilities of Universal Editor for Edge Delivery Services for Forms](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md)
- [Create your first form using Universal Editor](/help/edge/docs/forms/universal-editor/create-forms.md)
- [Create your first form using Google Sheets or Microsoft Excel](/help/edge/docs/forms/tutorial.md).
- [Embed Forms in Document Authoring (DA)](https://www.aem.live/developer/da-tutorial)


You are now ready to create your first high-performance form with AEM Edge Delivery Services.


<!-- 

## Start creating forms

- [Get started with Edge Delivery Services for AEM Forms](/help/edge/docs/forms/tutorial.md)
- [Create a form using Google Sheets or Microsoft Excel](/help/edge/docs/forms/create-forms.md)
- [Set up your Google Sheets or Microsoft Excel files to start accepting data​](/help/edge/docs/forms/submit-forms.md)
- [Publish your form and start collecting data](/help/edge/docs/forms/publish-forms.md)
- [Customize the look of your forms​](/help/edge/docs/forms/style-theme-forms.md)
- [Add repeatable sections to a form​](/help/edge/docs/forms/repeatable-forms.md)
- [Show a custom thank you message after form submission​](/help/edge/docs/forms/thank-you-page-form.md)
- [Adaptive Form Block components and their properties](/help/edge/docs/forms/form-components.md)
- [Real Use Monitoring](https://www.aem.live/developer/rum#authentication)

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
        transition: background-color 0.3s ease; /- Adding transition effect */
    }
    .card-container:hover {
        background-color: #f0f0f0; /- Changing background color on hover */
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