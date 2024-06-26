---
title: How do I apply e-signatures to a form using scribble signatures?
description: Learn to apply electronic signatures to a form using scribble signatures.
uuid: ffeba886-9b24-4ed1-95c0-e19356ff2f23
products: SG_EXPERIENCEMANAGER/FORMS
topic-tags: author
feature: Adaptive Forms, Foundation Components
exl-id: dc89ecb1-2d9e-4d1d-b85b-af90c550e7d8
role: "User, Developer"
---
# E-sign a form using scribble signatures{#apply-electronic-signatures-to-a-form-using-deprecated-scribble-signatures}

<span class="preview"> Adobe recommends using the modern and extensible data capture [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) for [creating new Adaptive Forms](/help/forms/creating-adaptive-form-core-components.md) or [adding Adaptive Forms to AEM Sites pages](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md). These components represent a significant advancement in Adaptive Forms creation, ensuring impressive user experiences. This article describes older approach to author Adaptive Forms using foundation components. </span>

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/signing-forms-using-scribble.html)                  |
| AEM as a Cloud Service     | This article        |


You can use the **Scribble Signature** component and **Signature Step** component to draw (Scribble) signature on an Adaptive Form. The Signature step component displays a PDF version of the Adaptive Form. You require a Document of Record option enabled or form template based Adaptive Forms to use the Signature step component.

![Scribble sign dialog](assets/scribble-signature.png)

## Various Options available in Signature Window

* **A:** Click the **Paint Brush** icon to draw your signature on canvas.
* **B:** Click the **Clear** icon to clear the signature on canvas.
* **C:** Click the **Geolocation** icon to add geolocation along with the signature.
* **D:** Click the **Keyboard** icon to type your name on canvas. 

 Once you select the Done ![aem_forms_save](assets/aem_forms_save.png) icon in Scribble signature window, you cannot edit the signature. In case, if you want to edit the signature, you have to disregard the current signature and re-sign using the above Paint Brush/Keyboard option.

You can select the **Configure** ![configure icon](assets/configure.png) icon to set the aspect ratio of Scribble Signature canvas. 
* When the aspect ratio of the Scribble Signature canvas is less than 1, the geolocation information is added at the bottom of the Scribble Signature canvas.


* When the aspect ratio of the Scribble Signature canvas is more than 1, the geolocation information is added to the right-side of the Scribble Signature canvas. 
 

 ![scribble signature-bottom](assets/scribble-signature-aspectratio.PNG)



   >[!NOTE]
   >
   >Signatures are always saved in a PNG format.
   >
   
## Configure an Adaptive Form to use Scribble Signature {#configure-an-adaptive-form-to-use-scribble-signature}

1. Create a Document of Record option enabled or form template based Adaptive Form. For step-by-step information, see [Creating an Adaptive Form](creating-adaptive-form.md).
1. Drag-and-drop the **Scribble Signature** component from component browser to the Adaptive Form.
1. Select the **Configure** ![configure](assets/configure.png) icon. It opens properties browser and displays properties of the Scribble Signature component. Configure properties of the Scribble Signature component.
1. Drag-and-drop the Signature Step component from component browser to the Adaptive Form.

   >[!NOTE]
   >
   >The Signature Step component takes up full width available for the form. It is recommended to not have any other component on the section containing the Signature Step component.

1. In the Content browser, select **Form Container**, and select the **Configure** ![configure icon](assets/configure.png) icon. It opens properties browser and displays Adaptive Form container properties. Navigate to **Adaptive Form Container** &gt; **Electronic Signature** and deselect the **Enable Adobe Sign** option. Select the Done ![aem_forms_save](assets/aem_forms_save.png) icon to save the changes.

   >[!NOTE]
   >
   >When you add a Signature Step component to an Adaptive Form, the Enable Adobe Sign option is selected automatically.

1. Select the **Configure** ![configure](assets/configure.png) icon. It opens properties browser and displays Signature step properties. Configure the following properties:

    * **Element Name**: Specify name of the component.

    * **Title:** Specify unique title of the component.
    * **Template message:** Specify the message to be displayed while the signature PDF is being loaded. Adobe Sign services take some time to prepare and load signature PDF.
    * **Signing Service:** Select the **Scribble Signature** option.

    * **CSS Class**: Specify CSS class of the client library, if any. Adobe recommends using [themes](themes.md) and [in-line styles](inline-style-adaptive-forms.md) instead of CSS Class.

   Select the Done ![aem_forms_save](assets/aem_forms_save.png) icon to save the changes. The Signature is configured successfully.

   Now, when you fill a form, a PDF version of Adaptive Form is displayed and options to sign the PDF document are provided. For detailed information, see [Sign an Adaptive Form using Scribble Signature](signing-forms-using-scribble.md#sign-an-adaptive-form-using-scribble-signature).

## Sign an Adaptive Form using Scribble Signature {#sign-an-adaptive-form-using-scribble-signature}

1. After you fill an Adaptive Form and reach the Signature Step page, the signature screen is displayed.

   ![Signature screen for EchoSign page](assets/esignscribblesign.jpg)

1. Click **[!UICONTROL Sign]**. The scribble sign dialog appears. Sign the form and click the Done ![aem_forms_save](assets/aem_forms_save.png) icon to save the signature.

   ![Scribble sign dialog](assets/scribblewidget.png)

1. Click complete to finish the signing process.

   ![Complete the signing process](assets/scribblecomplete.jpg)

The signatures are added to the form and the form control moves to the next panel.

## See Also {#see-also}

{{see-also}}