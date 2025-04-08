---
Title: Authoring a Form
Description: This article provides information on various form authoring platforms, including the Universal Editor, document-based authoring, and Adaptive Forms editors (Core Components and Foundation Components).
Keywords: Universal Editor for WYSIWYG authoring, document-based authoring, Adaptive Forms editors, Adaptive Forms editors for Core Components authoring, Adaptive Forms editors for Foundation Components authoring
feature: Edge Delivery Services
Role: User, Developer
hide: yes
hidefromtoc: yes
---

# Authoring a Form

Adobe Experience Manager offers and supports multiple editors to author a Form. You can use:
* Universal Editor (for WYSIWYG authoring)
* Microsoft Excel or Google Sheets (known as Document based authoring)
* Adaptive Forms editors (for Core Components or foundation components based authoring)

**[image to be added]**

## Universal Editor (for WYSIWYG authoring)

The Universal Editor is a versatile visual editor that offers a what-you-see-is-what-you-get (WYSIWYG) feature, ensuring an intuitive form creation experience. It is recommended to use the Universal Editor when creating new forms, as it provides a modern, user-friendly design and a convenient drag-and-drop interface.

To create forms using the Universal Editor, Edge Delivery Services templates available in the AEM environment are used. These forms inherit their look and feel from the configurations in the Edge Delivery Services GitHub repository. [A connection between your AEM environment and the Edge Delivery Services GitHub repository](/help/edge/docs/forms/publishing-forms.md) is established to enable the publishing of these forms on Edge Delivery Services.

For detailed steps on how to author using the Universal Editor, refer to the [Authoring Content with the Universal Editor](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/sites/authoring/universal-editor/authoring) article.

## Microsoft Excel or Google Sheets (known as Document based authoring)

You can author the forms using document-based authoring with Microsoft Excel or Google Sheets files, allowing you to leverage the robust ecosystems and APIs of Google Sheets, Microsoft Excel, and Microsoft SharePoint. This approach is particularly useful for creating simple forms without advanced submission services.

To begin creating a form using Microsoft Excel or Google Sheets, [set up an AEM project using AEM Forms boilerplate](/help/edge/docs/forms/tutorial.md#create-a-new-aem-project-pre-configured-with-adaptive-forms-block) and clone the corresponding GitHub repository to your local machine. AEM Forms Edge Delivery provides a feature called the Adaptive Forms Block, which simplifies the process of creating forms for capturing and storing data. To learn how to create and publish forms using the Adaptive Forms Block on Edge Delivery Services, refer to [Create a Form](/help/edge/docs/forms/create-forms.md).

## Adaptive Forms editors (for Core Components or foundation components based authoring)

You can author forms that are engaging, responsive and dynamic. The Adaptive Form editor provides a user-friendly wizard that allows you to quickly create Adaptive Forms. The form wizard features easy tab navigation, enabling you to select pre-configured templates for foundation or core components, themes, data models, and submission options to create a form efficiently. 

[Authoring forms with Core Components](/help/forms/creating-adaptive-form-core-components.md) allows you to leverage standardized data capture components that can be customized, reducing development time and lowering maintenance costs for digital enrollment experiences. These forms can be published using the Adaptive Forms Block on Edge Delivery Services or through the AEM Publish instance. 

[Authoring forms with Foundation Components](/help/forms/create-an-adaptive-form.md) uses classic data capture components. These forms can only be published using the AEM Publish instance. 

You can also publish forms created using Adaptive Forms Editors on Edge Delivery Services by establishing [connection between your AEM environment and the Edge Delivery Services GitHub repository](/help/edge/docs/forms/publishing-forms.md).

## How to choose between various types form authoring?

The following table outlines the features and use cases for each authoring editor, helping you choose the right one based on your requirements and form submission needs. 

| **Form Authoring Editor**    | **Key Approach**| **Features** | **Publishing Method** | **Use Cases** |
|--------|-----------|-------|-------|------------------------------------------------|
| **Document-based Authoring**    |  Leverages familiar tools like Google Docs and Microsoft Office for form creation.| Forms are designed using spreadsheets, with data directly submitted to Google Sheets or Microsoft Excel sheets. </br> </br> These forms are faster to create and deploy. You don't require any prior knowledge of AEM to develop custom components and styles for these forms.  | These forms are published on Edge Delivery Services and have a very high Google Lighthouse score. </br> </br>  The high score results in faster rendering and better SEO. | These forms are ideal for quick prototyping or basic forms where advanced submission services are not needed. </br> </br>  These are well-suited for surveys, registration, or feedback forms requiring data storage in spreadsheets. These forms are published on Edge Delivery services |  
| **Universal Editor**  </br> </br> If you are creating a new form, use Universal Editor to create forms.          | Offers a WYSIWYG interface for intuitive form creation.         | Forms are designed using intuitive drag-and-drop interface. </br> </br>  These forms borrow look and feel from configured Edge Delivery Services GitHub repository for the corresponding form. | These forms are published on Edge Delivery Services and have a very high Google Lighthouse score. </br> </br> The high score results in faster rendering and better SEO.  | These forms are ideal to create forms for Edge Delivery Service sites and pages. These forms scenarios involving complex forms, complex workflows, custom actions, or integrations with external systems |  
| **Adaptive Forms editors** | Provides a wizard-driven approach to quickly start forms authoring using templates, styling, and predefined fields. | Use these editors to create Core Components based forms or Foundation Components based forms. | These forms can be published on Edge Delivery Services or via AEM Publish instances.  | Use these editors to create Core Components based forms or Foundation Components based forms. Ideal for scenarios involving complex forms, complex workflows, custom actions, or integrations with external systems. |  


>[!NOTE]
>
>
> Should you find any features missing in the Universal Editor that were previously available in the Adaptive Forms editor, you can request them by emailing mailto:aem-forms-ea@adobe.com using your official email address.

## Related Article

* [Document-based authoring using Microsoft Excel or Google Sheets](/help/edge/docs/forms/create-forms.md)
* [Universal Editor for WYSIWYG authoring](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/edge-delivery/wysiwyg-authoring/authoring)
* [Create an Adaptive Form (Foundation Components)](/help/forms/creating-adaptive-form.md)
* [Create an Adaptive Form (Core Components)](/help/forms/create-an-adaptive-form.md)

## See Also

{{see-more-forms-eds}}