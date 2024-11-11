---
Title: How to configure Marketo Engage data for Adaptive Forms?
Description: Learn how to use Marketo Engage schema in Adaptive Forms.
Keywords: Use Marketo Engage data source in Adaptive Forms, How to connect a Marketo instance data source with form? , Connect a form to Marketo.
Feature: Adaptive Forms, Core Components
Role: User, Developer
---

# Configure Marketo Engage data source for Adaptive Forms

After creating the cloud service configuration to integrate Marketo Engage with AEM Forms, you can configure the data source for an Adaptive Form.

Configuring data integration enables users to connect to various data sources or schemas. Integrating with the Marketo Engage data source and using it across different forms facilitates operations on that data. To explore the supported out-of-the-box data sources for an Adaptive Form, refer to the [Configure Data Sources](/help/forms/configure-data-sources.md) article.

## Consideration for configuring the Marketo Engage data source for forms

Consideration while configuring Marketo Engage data source for forms are:

* It is not possible to connect Edge Delivery Services Forms with Marketo Engage.

## Prerequisite to use Marketo Engage data source for forms

Prerequisite to use Marketo Engage data source with forms:

* Create the [cloud service configuration to integrate Marketo Engage with forms](/help/forms/integrate-form-to-marketo-engage.md). 

## How to configure Adaptive Form for Marketo Engage data source?

To configure an Adaptive Form with the Marketo Engage data source, perform the following steps:
1. Log in to your [!DNL Experience Manager Forms] Author instance. 

1. Open the Adaptive Form for editing. Alternatively, you can also [create new Adaptive Form based on core components](/help/forms/creating-adaptive-form-core-components.md).
1. Open the Content Tree and select the **[!UICONTROL Guide Container]**. 
1. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure data source opens. 
1. Open the **[!UICONTROL Data Model]** tab and select a data model as **Marketo Engage**.
1. Select the **[!UICONTROL Connector]** from the drop-down list. 
  Based on the selected Marketo Engage connector, the form elements are displayed in the **[!UICONTROL Data Model Objects]** tab of the **[!UICONTROL Content Browser]** in the sidebar. You can drag-drop these elements to build your Adaptive Form.
1. Click **[!UICONTROL Done]**.
   
Alternatively, you can also edit the Adaptive Form properties to change its associated connector.

<!--
1. Select **[!UICONTROL Adobe Experience Manager]** &gt; **[!UICONTROL Forms]** &gt; **[!UICONTROL Forms & Documents]**.
2. Select **[!UICONTROL Create]**  &gt; **[!UICONTROL Adaptive Forms]**. The form creation wizard opens. 
3. In the **[!UICONTROL Source]** tab, select a template and a theme.
4. In the **[!UICONTROL Data]** tab, select a data model as **Marketo Engage**.
5. Select the **[!UICONTROL Connector]** from the drop-down list that appears in the right-pane of the screen. 
    By default all fields of the associated connector appears. The wizard offers the convenience of allowing you to selectively choose which fields should be included in the Adaptive Form through the use of checkboxes. 

6. In the **[!UICONTROL Submission]** tab, select submit action as **[!UICONTROL Submit to Marketo]**.

    When you select the data model as **Marketo Engage**, then the submit action as **Submit to Marketo**  is auto-selected. You can select a different submit action from the **[!UICONTROL Submission]** tab. The **[!UICONTROL Submission]** tab displays all the available submit actions.

7. Select **[!UICONTROL Create]**. Specify title, name, and location to save the Adaptive Form.
-->

The Adaptive Form is now configured with the data source from the connected Marketo Engage instance. Now, configure it to send data to Adobe Marketo Engage.

## FAQs

**Q: What happens when you change the connector of the form?**  
    **A:** If you change the connector of the form, the existing bindings become invalid.

**Q: What are the three operations available in the Invoke Service of the Rule Editor for forms integrated with Marketo Engage?**  
    **A:** The three out-of-the-box operations available in the **Invoke Service** for forms integrated with Marketo Engage are:
* Sync Lead
* Get Lead by ID
* Get Lead by Filter Type

## Next Step

Now, you have configured the Marketo Engage data source for Adaptive Forms. Next, you can [configure an Adaptive Form to send data to Marketo Engage](/help/forms/submit-adaptive-form-to-marketo-engage.md).

## Related Article

{{af-submit-action}}

## See Also

{{marketo-engage-see-also}}

    