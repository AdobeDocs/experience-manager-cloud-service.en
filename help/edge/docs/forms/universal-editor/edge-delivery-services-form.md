---
Title: How Edge Delivery Services Forms work?
Description: This article provides information on how Edge Delivery Services Forms work. It also provides information on various form authoring platforms, including the Universal Editor and document-based authoring.
Keywords: Universal Editor for WYSIWYG authoring, document-based authoring, Working of Edge Delivery Services Forms, How Edge Delivery Services Forms work?
feature: Edge Delivery Services
Role: User, Developer
hide: yes
hidefromtoc: yes
---

# Edge Delivery Services Forms

Adobe Edge Delivery Services Forms transform the way forms are authored, executed, and processed. By leveraging Edge Delivery Services, organizations can create fast, secure, and highly available digital forms, enhancing user experience and operational efficiency with a rapid development environment. With Edge Delivery Services Forms, you can boost conversions, reduce costs, and accelerate content delivery.

## Benefits of Edge Delivery Services Forms

* **Faster Form Creation**: Build high-performance forms with a perfect Lighthouse Score and continuously monitor their real-world performance using Real User Monitoring (RUM).

* **Streamlined Authoring Process**: Easily manage content from multiple sources for greater flexibility. Out of the box, you can create forms using both WYSIWYG and document-based authoring, allowing seamless integration of various content formats.

* **Ease of Use for Non-Technical Users**: Edge Delivery Services empowers non-programmers to easily manage and publish forms without requiring extensive programming knowledge.
  
* **Improved User Experience**: Ensure rapid load times and smooth interactions, providing users with minimal wait times and an intuitive form-filling experience.

* **Serverless Execution**: Edge Delivery Services enable serverless execution of form logic. This includes:

    * **Client-side Validation**: Form field validation occurs at the client side, reducing round-trip delays.

    * **Pre-fill & Personalization**: Form data pre-fill is handled at the client side for a seamless user experience.

    * **Submission Processing**: Form submissions are validated and forwarded securely without central server 

## How Edge Delivery Services Forms Work?

Users can author Edge Delivery Services Forms using document-based authoring tools such as Google Drive, SharePoint, or the Universal Editor (WYSIWYG authoring), while leveraging the basic styling, behaviour and components available in the GitHub repository. Once authored, Edge Delivery Services Forms can send data to any platform using the Forms Submission Service.

![How Edge Delivery Services Forms works](/help/edge/docs/forms/assets/eds-forms-working.png)

### Key components of Edge Delivery Services Forms

The key components of Edge Delivery Servies Forms are:

* **GitHub Repository**: The GitHub repository serves as a boilerplate for creating Edge Delivery Services Forms. The forms leverage basic styling and functionality from the repository and allow users to add customizations and custom components to the Edge Delivery Services Forms.

* **Form Authoring**: Edge Delivery Services Forms support two types of authoring: WYSIWYG and document-based authoring. Document-based authoring enables users to create forms using familiar tools like Google Docs and Microsoft Office. WYSIWYG authoring allows users to design forms visually using the Universal Editor, making it easy for non-technical users to create and manage forms. Universal Editor offers an intuitive form creation experience and provides access to numerous form capabilities.

* **Forms Submission Service**: The Forms Submission Service allows you to store data from forms submissions on any platform, such as OneDrive, SharePoint, or Google Sheets, making it easy to access and manage form data within your preferred system.

## Authoring a Form

Adobe Experience Manager offers and supports multiple editors to author a Form. You can use:
* [Universal Editor (for WYSIWYG authoring)](#universal-editor-for-wysiwyg-authoring)
* [Microsoft Excel or Google Sheets (known as Document based authoring)](#microsoft-excel-or-google-sheets-known-as-document-based-authoring)

### Universal Editor (for WYSIWYG authoring)

The Universal Editor is a versatile visual editor that offers a what-you-see-is-what-you-get (WYSIWYG) feature, ensuring an intuitive form creation experience. It is recommended to use the Universal Editor when creating new forms, as it provides a modern, user-friendly design and a convenient drag-and-drop interface.

To create forms using the Universal Editor, Edge Delivery Services templates available in the AEM environment are used. These forms inherit their look and feel from the configurations in the Edge Delivery Services GitHub repository. [A connection between your AEM environment and the Edge Delivery Services GitHub repository](/help/edge/docs/forms/publishing-forms.md) is established to enable the publishing of these forms on Edge Delivery Services.

For detailed steps on how to author using the Universal Editor, refer to the [Authoring Content with the Universal Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring) article.

### Microsoft Excel or Google Sheets (known as Document based authoring)

You can author the forms using document-based authoring with Microsoft Excel or Google Sheets files, allowing you to leverage the robust ecosystems and APIs of Google Sheets, Microsoft Excel, and Microsoft SharePoint. This approach is particularly useful for creating simple forms without advanced submission services.

To begin creating a form using Microsoft Excel or Google Sheets, [set up an AEM project using AEM Forms boilerplate](/help/edge/docs/forms/tutorial.md#create-a-new-aem-project-pre-configured-with-adaptive-forms-block) and clone the corresponding GitHub repository to your local machine. AEM Forms Edge Delivery provides a feature called the Adaptive Forms Block, which simplifies the process of creating forms for capturing and storing data. To learn how to create and publish forms using the Adaptive Forms Block on Edge Delivery Services, refer to [Create a Form](/help/edge/docs/forms/create-forms.md).

<!--
## Adaptive Forms editors (for Core Components or foundation components based authoring)

You can author forms that are engaging, responsive and dynamic. The Adaptive Form editor provides a user-friendly wizard that allows you to quickly create Adaptive Forms. The form wizard features easy tab navigation, enabling you to select pre-configured templates for foundation or core components, themes, data models, and submission options to create a form efficiently. 

[Authoring forms with Core Components](/help/forms/creating-adaptive-form-core-components.md) allows you to leverage standardized data capture components that can be customized, reducing development time and lowering maintenance costs for digital enrollment experiences. These forms can be published using the Adaptive Forms Block on Edge Delivery Services or through the AEM Publish instance. 

[Authoring forms with Foundation Components](/help/forms/create-an-adaptive-form.md) uses classic data capture components. These forms can only be published using the AEM Publish instance. 

You can also publish forms created using Adaptive Forms Editors on Edge Delivery Services by establishing [connection between your AEM environment and the Edge Delivery Services GitHub repository](/help/edge/docs/forms/publishing-forms.md).


| **Adaptive Forms editors** | Provides a wizard-driven approach to quickly start forms authoring using templates, styling, and predefined fields. | Use these editors to create Core Components based forms or Foundation Components based forms. | These forms can be published on Edge Delivery Services or via AEM Publish instances.  | Use these editors to create Core Components based forms or Foundation Components based forms. Ideal for scenarios involving complex forms, complex workflows, custom actions, or integrations with external systems. |  



## Types of Publishing for Edge Delivery Services Forms

You can publish Edge Delivery Services Forms on one of the following:

* **Edge Delivery Services Form Submission**: Edge Delivery Services Form Submissions ensure that form interactions, including submission and data processing, are handled efficiently and securely. This enables a faster and more reliable user experience, particularly during high traffic periods. By processing form submissions at the edge, Edge Delivery Services minimizes the reliance on a centralized server.

* **AEM Publish instance**: The AEM Forms server offers a publish instance that manages the forms and related assets available to end users.
-->

### How to choose between various types form authoring?

The following table outlines the features and use cases for each authoring editor, helping you choose the right one based on your requirements and form submission needs. 

| **Form Authoring Editor**    | **Key Approach**| **Features** | **Publishing Method** | **Use Cases** |
|--------|-----------|-------|-------|------------------------------------------------|
| **Document-based Authoring**    |  Leverages familiar tools like Google Docs and Microsoft Office for form creation.| Forms are designed using spreadsheets, with data directly submitted to Google Sheets or Microsoft Excel sheets. </br> </br> These forms are faster to create and deploy. You don't require any prior knowledge of AEM to develop custom components and styles for these forms.  | These forms are published on Edge Delivery Services and have a very high Google Lighthouse score. </br> </br>  The high score results in faster rendering and better SEO. | These forms are ideal for quick prototyping or basic forms where advanced submission services are not needed. </br> </br>  These are well-suited for surveys, registration, or feedback forms requiring data storage in spreadsheets. These forms are published on Edge Delivery services |  
| **Universal Editor**  </br> </br> If you are creating a new form, use Universal Editor to create forms.          | Offers a WYSIWYG interface for intuitive form creation.         | Forms are designed using intuitive drag-and-drop interface. </br> </br>  These forms borrow look and feel from configured Edge Delivery Services GitHub repository for the corresponding form. | These forms are published on Edge Delivery Services and have a very high Google Lighthouse score. </br> </br> The high score results in faster rendering and better SEO.  | These forms are ideal to create forms for Edge Delivery Service sites and pages. These forms scenarios involving complex forms, complex workflows, custom actions, or integrations with external systems |  

>[!NOTE]
>
>
> Should you find any features missing in the Universal Editor that were previously available in the Adaptive Forms editor, you can request them by emailing mailto:aem-forms-ea@adobe.com using your official email address.

## See also

{{see-more-forms-eds}}




