---
title: How to configure Marketo Engage data for Adaptive Forms?
description: Learn how to use Marketo Engage schema in Adaptive Forms.
keywords: Use Marketo Engage data source in Adaptive Forms, How to connect a Marketo instance data source with form? , Connect a form to Marketo.
feature: Adaptive Forms, Form Data Model
role: User, Developer
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

<span> This video is applicable only for Core Components. For UE/Foundation Components, please refer to the article.</span>
 
>[!BEGINTABS]

>[!TAB Foundation Component]

To configure an Adaptive Form based on Foundation Components with the Marketo Engage data source, perform the following steps:

1. Log in to your [!DNL Experience Manager Forms] Author instance. 
1. Open the Adaptive Form for editing and navigate to **[!UICONTROL Data Model]** section of the Adaptive Form Container properties and select a form model as **Connector**.
1. Select the **[!UICONTROL Connector]** from the drop-down list. 
1. After selecting the **[!UICONTROL Connector]**, you can select the cloud configuration.

    ![Select Marketo Connector](/help/forms/assets/select-marketo-connector-af1.png){width=50%, height=50%}

    Based on the selected Marketo Engage configuration, the form elements are displayed in the **[!UICONTROL Data Model Objects]** tab of the **[!UICONTROL Content Browser]** in the sidebar. You can drag-drop these elements to build your Adaptive Form.

    ![Marketo Data Source](/help/forms/assets/marketo-engage-data-source-af1.png){width=50%, height=50%}

1. Click **[!UICONTROL Done]**.
   
Alternatively, you can also edit the Adaptive Form properties to change its associated configuration.

The Adaptive Form is now configured with the data source from the connected Marketo Engage instance. Now, configure it to send data to Adobe Marketo Engage.

>[!TAB Core Component]

To configure an Adaptive Form based on Core Components with the Marketo Engage data source, perform the following steps:

1. Log in to your [!DNL Experience Manager Forms] Author instance. 

1. Open the Adaptive Form for editing.
1. Open the Content Tree and select the **[!UICONTROL Guide Container]**. 
1. Click the Adaptive Form Container properties ![Adaptive Form Container properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box to configure data source opens. 
1. Open the **[!UICONTROL Data Model]** tab and select a form model as **Connector**.
1. Select the **[!UICONTROL Connector]** from the drop-down list. 

1. After selecting the **[!UICONTROL Connector]**, you can select the cloud configuration.

    ![Select Marketo Connector](/help/forms/assets/select-marketo-connector.png){width=50%, height=50%}

    Based on the selected Marketo Engage configuration, the form elements are displayed in the **[!UICONTROL Data Model Objects]** tab of the **[!UICONTROL Content Browser]** in the sidebar. You can drag-drop these elements to build your Adaptive Form.

    ![Marketo Data Source](/help/forms/assets/marketo-engage-data-source.png){width=50%, height=50%}

1. Click **[!UICONTROL Done]**.
   
Alternatively, you can also edit the Adaptive Form properties to change its associated configuration.

The Adaptive Form is now configured with the data source from the connected Marketo Engage instance. Now, configure it to send data to Adobe Marketo Engage.

>[!TAB Universal Editor]

To configure an Adaptive Form authored in Universal Editor with the Marketo Engage data source, perform the following steps:

1. Open the properties of the form for editing.
1. Select the **[!UICONTROL Form Model]**. 
1. Select **Connector** from the **[!UICONTROL Form Model]**.
1. After selecting the **[!UICONTROL Connector]**, you can select the cloud configuration.

    ![Select Marketo Connector](/help/forms/assets/select-marketo-connector-ue.png)

1. Click **[!UICONTROL Save & Close]**.

Based on the selected Marketo Engage configuration, the form elements are displayed in the **[!UICONTROL Datasource]** tab of the Content Browser in the Properties Panel. You can drag-drop these elements to build your Adaptive Form.

![Marketo Data Source](/help/forms/assets/marketo-engage-data-source-ue.png)
   
The form is now configured with the data source from the connected Marketo Engage instance. Now, configure it to send data to Adobe Marketo Engage.

>[!ENDTABS]

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
