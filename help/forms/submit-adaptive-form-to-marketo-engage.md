---
Title: How to configure submit action to Marketo Engage for forms?
Description: Learn how to configure the submit action of Adaptive Form to send data to Marketo Engage.
Keywords: Submit data to Marketo engage, Configure submit action as Submit to Marketo Engage
Feature: Adaptive Forms, Form Data Model
Role: User, Developer
exl-id: 0683564b-1ac4-42b4-bc08-101c4fdef286
---
# Configure the submit action to Marketo Engage for existing forms 

<span class="preview"> The feature is available under early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

![Workflow](/help/forms/assets/workflow-marketo-3.png)

Adaptive Forms editor provides the **Submit to Marketo Engage** submit action to send Adaptive Forms data to Adobe Marketo Engage for processing. You can configure an existing Adaptive Form to submit data to [Adobe Marketo Engage](https://experienceleague.adobe.com/en/docs/marketo/using/home) on submission. 

Various out-of-the-box submit actions for handling form submissions are available. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md) article.

## Consideration while configuring submit action to Marketo Engage for form

* Ensure that the Adaptive Form is configured with the Marketo Engage data source to submit data to Marketo Engage upon form submission. However, you can change the submit action to alternatives, for example, **Submit to OneDrive** or **Submit to SharePoint**, even if the form is configured with the Marketo Engage data schema.

## Prerequisite to configure the submit action to Marketo Engage for existing form

Prerequisite to configure the submit action to Marketo Engage:

* Configure the [Marketo Engage data source for Adaptive Form](/help/forms/use-marketo-engage-data-source-in-form.md) and bind the form elements with Marketo Engage fields.

## How to configure submit action to Marketo Engage for existing forms?

>[!VIDEO](https://video.tv.adobe.com/v/3442866/submit-action-marketo-engage-marketo-aem-aem-forms-engage)

You can configure the submit action of an Adaptive Form to submit data to Adobe Marketo Engage. To configure the submit action to Marketo Engage, perform the following steps:

1. Open the Adaptive Form for editing.
2. Open the Content Tree and select the **[!UICONTROL Guide Container]**. 
3. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure submit action opens. 
4. Open the **[!UICONTROL Submission]** tab and select a submit action as **Submit to Marketo Engage**.
5. Click **[!UICONTROL Done]**.

![Marketo Submit Action](/help/forms/assets/marketo-engage-submit-action.png){width=50%, height=50%}


After configuring the submit action for the Adaptive Form as **Submit to Marketo Engage**, you can send data to Adobe Marketo Engage for processing. The data can be used to analyze and optimize marketing campaigns, automate follow-up emails, and trigger workflows based on form submissions.  

## Frequently asked question (FAQ)

**Q: Can you change the submit action for forms configured to connect with the Marketo Engage schema?** 
    **A:** By default, the **Submit to Marketo** action is selected when a form is configured to connect with the Marketo Engage schema. However, you can change the submit action for the forms if needed.

## Next step

You can also connect an Adaptive Form with the [Munchkin library](https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/administration/setup/munchkin) to track the number of visits, clicks, and form submissions.

## Related articles

{{af-submit-action}}

## See also

{{marketo-engage-see-also}}
