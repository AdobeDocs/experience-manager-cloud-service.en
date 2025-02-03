---
Title: How to integrate AEM workflow with an Adaptive Form?
Description: Explore the process of automated workflow initiation with AEM Forms Submit Action.
keywords: AEM Workflow, Integrate Adaptive Form with AEM workflow, Invoke AEM workflow Submit Action
feature: Adaptive Forms, Core Components
exl-id: b7788e3d-acd8-4867-b232-f9767cf6b2f5
---
# Integrate AEM Adaptive Form with AEM Workflow: Streamlining Business Processes

The **[!UICONTROL Invoke an AEM Workflow]** Submit Action associates an Adaptive Form with an AEM Workflow. When a form is submitted, the associated workflow starts automatically on the Author instance. You can save the data files, attachments, and Document of Record to the payload location of the workflow or to a variable. If the workflow is marked for external data storage and configured for an external data storage, then only the variable option is available. You can select from the list of variables available for the workflow model. If the workflow is marked for external data storage at a later stage and not at the time of workflow creation, then ensure that the required variable configurations are in place.

>[!NOTE]
>
>  Learn how to [create a workflow model](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html?lang=en#extending-aem) to define the series of steps executed when a user starts the workflow. You can also define model properties, such as whether the workflow is transient or uses multiple resources.

AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md)  article.

## Advantages

Some of the advantages of integrating AEM workflow with Adaptive Forms are:

* AEM Workflow integration allows for the automation of complex business processes involving form submissions.
*  AEM Workflow supports conditional logic, thus allowing dynamic decisions based on form data or external factors.
* AEM Workflow routes tasks based on predefined rules and conditions, ensuring tasks are assigned to the right individuals or groups.

<!--
## Prerequisites

Before using the **[!UICONTROL Invoke an AEM Workflow]** Submit Action configure the following for the **[!UICONTROL AEM DS settings service]** configuration: 

* **[!UICONTROL Processing Server URL]**: The Processing Server is the server where the Forms or AEM Workflow is triggered. This can be same as the URL of the AEM author instance or another server.

* **[!UICONTROL Processing Server User Name]**: Workflow user's username

* **[!UICONTROL Processing Server Password]**: Workflow user's password -->

## Integrate AEM Workflow with Adaptive Forms {#steps-to-integrate-workflow-with-af}

To set up automated process with [AEM Workflow](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html?lang=en#extending-aem) for an Adaptive Form, perform the following steps:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Invoke an AEM Workflow]** .
    ![Action configuration of Send Email](/help/forms/assets/configure-invoke-aem-workflow.png)

1. Select workflow model from the **[!UICONTROL Workflow Model]** drop-down list.
1. Select option from the **[!UICONTROL Store Data file using]** drop-down list. 
    
    **Data file**: It contains data submitted to the Adaptive Form. You can use the **[!UICONTROL Data File Path]** option to specify the name of the file and path of file relative to the payload. For example, the `/addresschange/data.xml` path creates a folder named `addresschange` and places it relative to payload. You can also specify only `data.xml` to send only submitted data without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model. 
    
1. Select option from the **[!UICONTROL Store attachments using]** drop-down list. 
    
    **Attachments**: You can use the **[!UICONTROL Attachment Path]** option to specify the folder name to store the attachments uploaded to the Adaptive Form. The folder is created relative to the payload. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.

1. Select option from the **[!UICONTROL Documents of record using]** drop-down list. 
    
    **Document of Record**: It contains the Document of Record generated for the Adaptive Form. You can use the **[!UICONTROL Document of Record Path]** option to specify the name of the Document of Record file and path of file relative to the payload. For example, the `/addresschange/DoR.pdf` path creates a folder named `addresschange` relative to the payload and places the `DoR.pdf` relative to payload. You can also specify only `DoR.pdf` to save only Document of Record without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.
1. Click **[!UICONTROL Done]**.

>[!NOTE]
>
> Learn more about [Forms-centric AEM Workflows - Step Reference to automate business processes](/help/forms/aem-forms-workflow-step-reference.md).  

<!--
## Best Practices

* When configuring the **[!UICONTROL Invoke an AEM Workflow]** Submit Action, select the appropriate workflow model that aligns with the desired business process.
* In case, the workflow involves external data storage, be sure to configure the workflow accordingly. It is recommended to set up variables appropriately and in accordance with any external storage requirements. -->

## Related Articles

{{af-submit-action}}
