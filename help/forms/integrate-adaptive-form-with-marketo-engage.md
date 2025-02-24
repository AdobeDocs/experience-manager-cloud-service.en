---
Title: How to integrate Marketo Engage with AEM Forms using Form wizard?
Description: Learn how to integrate your Marketo Engage instance with AEM Forms using form wizard.
Keywords: How to connect a Marketo instance with form? , Connect a form to Marketo, Integrate a form with Marketo Engage, Integrate an Adaptive Form with a Marketo instance.
Feature: Adaptive Forms, Form Data Model
Role: User, Developer
exl-id: 1fcba628-ffd8-416a-a8b5-76b35d4aabd4
---
# Integrate an Adaptive Form with Marketo Engage 

<span class="preview"> The feature is available under early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

![Workflow](/help/forms/assets/workflow-marketo-4.png)

After creating the cloud service configuration to integrate Marketo Engage with AEM Forms, you can configure an Adaptive Form to integrate with [Adobe Marketo Engage](https://experienceleague.adobe.com/en/docs/marketo/using/home). 

You can connect Marketo Engage to an Adaptive Form using the form wizard, which simplifies the configuration process by guiding you through each step. It includes selecting templates, styles, and data fields, as well as setting up data mapping to ensure your form is ready to communicate with Marketo Engage once created. Using the form wizard, you can also configure the Adaptive Form to submit data directly to Adobe Marketo Engage upon submission.

## Consideration for configuring the Marketo Engage data source for forms

Consideration while configuring Marketo Engage data source for forms are:

* It is not possible to connect Edge Delivery Services Forms with Marketo Engage.

## Prerequisite to connect Marketo Engage with forms

Prerequisite to connect Marketo Engage with forms:

* Create the [cloud service configuration to integrate Marketo Engage with forms](/help/forms/integrate-form-to-marketo-engage.md).

## How to configure new Adaptive Form to integrate with Marketo Engage?

>[!VIDEO](https://video.tv.adobe.com/v/3442867/marketo-aem-marketo-engage-engage-aem-forms)

To configure new Adaptive Form to integrate with Marketo Engage, perform the following steps:

1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.

    ![Select Forms and Documents](/help/forms/assets/select-forms.png)

1. Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The form creation wizard opens. 

    ![Select AF](/help/forms/assets/select-create-forms.png)

1. In the **[!UICONTROL Source]** tab, select a template 

    ![Select Templates](/help/forms/assets/select-template.png)

1. From the **[!UICONTROL Style]**, select the theme.

    ![Select Theme](/help/forms/assets/select-form-theme.png)


1. In the **[!UICONTROL Data]** tab, select a data model as **Marketo Engage**.

1. Select the **[!UICONTROL Cloud Configuration]** from the drop-down list that appears in the right-pane of the screen. 
    By default all fields of the associated configuration appears. The wizard offers the convenience of allowing you to selectively choose which fields should be included in the Adaptive Form through the use of checkboxes. 

    ![Select Data Model](/help/forms/assets/select-marketo-data.png)

1. In the **[!UICONTROL Submission]** tab, select submit action as **[!UICONTROL Submit to Marketo]**.

    When you select the data model as **Marketo Engage**, then the submit action as **Submit to Marketo**  is auto-selected. You can select a different submit action from the **[!UICONTROL Submission]** tab. The **[!UICONTROL Submission]** tab displays all the available submit actions.

    ![Submit to Marketo engage](/help/forms/assets/select-marketo-engage.png)

1. Select **[!UICONTROL Create]**. Specify title, name, and location to save the Adaptive Form.

    ![Create Form](/help/forms/assets/create-marketo-form.png)

1. Select **[!UICONTROL Create]**.

The Adaptive Form is now configured to connect with Marketo Engage instance. Alternatively, you can also edit the Adaptive Form properties to change its associated configuration.

## Frequently asked questions (FAQs)

**Q: Can you change the submit action for forms configured to connect with the Marketo Engage schema?** 
    **A:** By default, the **Submit to Marketo** action is selected when a form is configured to connect with the Marketo Engage schema. However, you can change the submit action for the forms if needed.


**Q: What happens when you change the connector of the form?**  
    **A:** If you change the connector of the form, the existing bindings become invalid.

**Q: What are the three operations available in the Invoke Service of the Rule Editor for forms integrated with Marketo Engage?**  
    **A:** The three out-of-the-box operations available in the **Invoke Service** for forms integrated with Marketo Engage are:
* Sync Lead
* Get Lead by ID
* Get Lead by Filter Type

## Next step

You can also connect an Adaptive Form with the [Munchkin library](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/administration/setup/munchkin) to track the number of visits, clicks, and form submissions.

## Related articles

{{af-submit-action}}

## See also

{{marketo-engage-see-also}}
