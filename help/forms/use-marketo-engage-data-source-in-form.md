---
Title: How to configure Marketo Engage data for Adaptive Forms?
Description: Learn how to use Marketo Engage schema in Adaptive Forms.
Keywords: Use Marketo Engage data source in Adaptive Forms, How to connect a Marketo instance data source with form? , Connect a form to Marketo.
Feature: Adaptive Forms, Form Data Model
Role: User, Developer
exl-id: 4656ec65-f1ad-4e97-8d93-25933cdc7f7b
---
# Configure Marketo Engage data source for existing Adaptive Forms

<span class="preview"> The feature is available under early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

![Workflow](/help/forms/assets/workflow-marketo-2.png)

After creating the cloud service configuration to integrate Marketo Engage with existing AEM Forms, you can configure the data source for forms.

Configuring data integration enables users to connect to various data sources or schemas. Integrating with the Marketo Engage data source and using it across different forms facilitates operations on that data. To explore the supported out-of-the-box data sources for an Adaptive Form, refer to the [Configure Data Sources](/help/forms/configure-data-sources.md) article.

## Consideration for configuring the Marketo Engage data source for forms

Consideration while configuring Marketo Engage data source for forms are:

* It is not possible to connect Edge Delivery Services Forms with Marketo Engage.

## Prerequisite to use Marketo Engage data source for forms

Prerequisite to use Marketo Engage data source with forms:

* Create the [cloud service configuration to integrate Marketo Engage with forms](/help/forms/integrate-form-to-marketo-engage.md).

## How to configure existing Adaptive Form for Marketo Engage data source?

>[!VIDEO](https://video.tv.adobe.com/v/3442871/marketo-aem-forms-aem-marketo-engage)

To configure an Adaptive Form with the Marketo Engage data source, perform the following steps:
1. Log in to your [!DNL Experience Manager Forms] Author instance. 

2. Open the Adaptive Form for editing.
3. Open the Content Tree and select the **[!UICONTROL Guide Container]**. 
4. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure data source opens. 
5. Open the **[!UICONTROL Data Model]** tab and select a form model as **Connector**.
6. Select the **[!UICONTROL Connector]** from the drop-down list. 

7. After selecting the **[!UICONTROL Connector]**, you can select the cloud configuration.

    ![Select Marketo Connector](/help/forms/assets/select-marketo-connector.png)

    Based on the selected Marketo Engage configuration, the form elements are displayed in the **[!UICONTROL Data Model Objects]** tab of the **[!UICONTROL Content Browser]** in the sidebar. You can drag-drop these elements to build your Adaptive Form.

    ![Marketo Data Source](/help/forms/assets/marketo-engage-data-source.png)

8. Click **[!UICONTROL Done]**.
   
Alternatively, you can also edit the Adaptive Form properties to change its associated configuration.

The Adaptive Form is now configured with the data source from the connected Marketo Engage instance. Now, configure it to send data to Adobe Marketo Engage.

## Frequently asked questions (FAQs)

**Q: What happens when you change the connector of the form?**  
    **A:** If you change the connector of the form, the existing bindings become invalid.

**Q: What are the three operations available in the Invoke Service of the Rule Editor for forms integrated with Marketo Engage?**  
    **A:** The three out-of-the-box operations available in the **Invoke Service** for forms integrated with Marketo Engage are:
* Sync Lead
* Get Lead by ID
* Get Lead by Filter Type

## Next step

Now, you have configured the Marketo Engage data source for Adaptive Forms. Next, you can [configure an Adaptive Form to send data to Marketo Engage](/help/forms/submit-adaptive-form-to-marketo-engage.md).

## Related articles

{{af-submit-action}}

## See also

{{marketo-engage-see-also}}
