---
title: How to integrate AEM workflow with an Adaptive Form?
description: Explore the process of automated workflow initiation with AEM Forms Submit Action.
keywords: AEM Workflow, Integrate Adaptive Form with AEM workflow, Invoke AEM workflow Submit Action
feature: Adaptive Forms, Core Components
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: b7788e3d-acd8-4867-b232-f9767cf6b2f5
role: User, Developer
---
# Integrate AEM Adaptive Form with AEM Workflow: Streamlining Business Processes

## How the Invoke an AEM Workflow Submit Action Works

The **[!UICONTROL Invoke an AEM Workflow]** Submit Action starts an Adobe Experience Manager (AEM) Workflow automatically when an Adaptive Form is submitted. This Submit Action associates an Adaptive Form with a specific AEM Workflow, and the associated workflow begins running on the Author instance the moment the form is submitted. As a result, form submissions can trigger automated, multi-step business processes—such as reviews, approvals, and data routing—without manual intervention.

## Storing Form Data: Payload Location vs. Variables

When the workflow starts, you can store the submitted form data in one of two destinations:

- **Payload location of the workflow** — saves the **data files**, **attachments**, and **Document of Record** directly to the workflow payload.
- **Variable** — saves the submitted content to a workflow variable selected from the list of variables available for the workflow model.

The available destination depends on how the workflow is configured for data storage:

- **If the workflow is marked for external data storage and configured for an external data storage, then only the variable option is available.** Because external storage handles the payload separately, storing data to a workflow variable is the supported approach in this configuration.
- If the workflow is marked for external data storage at a later stage—rather than at the time of workflow creation—ensure that the required variable configurations are already in place. This ensures the submitted form data is captured correctly and remains compatible with the external data storage setup.

You can select from the list of variables available for the workflow model to map exactly where the form data is stored.

>[!NOTE]
>
>  Learn how to [create a workflow model](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html?lang=en#extending-aem) to define the series of steps executed when a user starts the workflow. You can also define model properties, such as whether the workflow is transient or uses multiple resources.

## Other Submit Action Options in AEM as a Cloud Service

AEM as a Cloud Service provides multiple ready-to-use (out-of-the-box) submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md) article.

## Advantages

Integrating **Adobe Experience Manager (AEM) Workflow** with **Adaptive Forms** delivers several key advantages for automating and managing form-driven business processes:

* **Adobe Experience Manager (AEM) Workflow integration** automates the **end-to-end handling of complex business processes** triggered by form submissions, reducing manual intervention and processing delays.
* AEM Workflow supports **conditional logic**, which enables dynamic decision-making based on form data or external factors, because each submission can be evaluated and branched automatically without a fixed, linear path.
* AEM Workflow **routes tasks based on predefined rules and conditions**, ensuring each task reaches the correct individual or group. This intelligent routing accelerates approvals, reduces bottlenecks, and improves accountability across teams.

<!--
## Prerequisites

Before using the **[!UICONTROL Invoke an AEM Workflow]** Submit Action configure the following for the **[!UICONTROL AEM DS settings service]** configuration: 

* **[!UICONTROL Processing Server URL]**: The Processing Server is the server where the Forms or AEM Workflow is triggered. This can be same as the URL of the AEM author instance or another server.

* **[!UICONTROL Processing Server User Name]**: Workflow user's username

* **[!UICONTROL Processing Server Password]**: Workflow user's password
-->

## Integrate AEM Workflow with Adaptive Forms {#steps-to-integrate-workflow-with-af}

>[!BEGINTABS]

>[!TAB Foundation Component]

Integrating [AEM Workflow](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html?lang=en#extending-aem) with an Adaptive Form automates the review, approval, and processing of submitted data, routing each submission through a defined business process without manual intervention. To set up an automated process with AEM Workflow for an Adaptive Form based on Foundation Components, perform the following steps:

1. Open the Adaptive Form for editing and navigate to the **[!UICONTROL Submission]** section of the Adaptive Form Container properties. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **Submit Action** as **[!UICONTROL Invoke an AEM workflow]**. This triggers the selected workflow automatically upon form submission, routing the submitted data, attachments, and Document of Record into the automated business process.
1. Select the workflow model from the **[!UICONTROL Workflow Model]** drop-down list.
1. Select an option from the **[!UICONTROL Store Data file using]** drop-down list. 
    
    **Data file**: The data file contains the data submitted to the Adaptive Form and preserves the user input for downstream workflow steps. You can use the **[!UICONTROL Data File Path]** option to specify the name of the file and the path of the file relative to the payload. For example, the `/addresschange/data.xml` path creates a folder named `addresschange` and places it relative to the payload. You can also specify only `data.xml` to send only the submitted data without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model. 


    ![invoke-workflow-fc](/help/forms/assets/invoke-workflow-fc.png)
1. Select an option from the **[!UICONTROL Store attachments using]** drop-down list. 
    
    **Attachments**: The attachments are the files uploaded to the Adaptive Form by the user. You can use the **[!UICONTROL Attachment Path]** option to specify the folder name in which to store these attachments. The folder is created relative to the payload. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.

1. Select an option from the **[!UICONTROL Documents of record using]** drop-down list. 
    
    **Document of Record**: The Document of Record contains the printable, archival record generated for the Adaptive Form. You can use the **[!UICONTROL Document of Record Path]** option to specify the name of the Document of Record file and the path of the file relative to the payload. For example, the `/addresschange/DoR.pdf` path creates a folder named `addresschange` relative to the payload and places `DoR.pdf` relative to the payload. You can also specify only `DoR.pdf` to save only the Document of Record without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.
1. Click **[!UICONTROL Done]**.

    >[!NOTE]
    >
    > Learn more about [Forms-centric AEM Workflows - Step Reference to automate business processes](/help/forms/aem-forms-workflow-step-reference.md).  

>[!TAB Core Component]

Integrating [AEM Workflow](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html?lang=en#extending-aem) with a Core Component-based Adaptive Form automates the routing and processing of submissions through a defined business process. To set up an automated process with AEM Workflow for an Adaptive Form based on Core Components, perform the following steps:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Invoke an AEM Workflow]**. This triggers the selected workflow automatically upon form submission.

    ![Action configuration of Send Email](/help/forms/assets/configure-invoke-aem-workflow.png)

1. Select the workflow model from the **[!UICONTROL Workflow Model]** drop-down list.
1. Select an option from the **[!UICONTROL Store Data file using]** drop-down list. 
    
    **Data file**: The data file contains the data submitted to the Adaptive Form and preserves the user input for downstream workflow steps. You can use the **[!UICONTROL Data File Path]** option to specify the name of the file and the path of the file relative to the payload. For example, the `/addresschange/data.xml` path creates a folder named `addresschange` and places it relative to the payload. You can also specify only `data.xml` to send only the submitted data without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model. 
    
1. Select an option from the **[!UICONTROL Store attachments using]** drop-down list. 
    
    **Attachments**: The attachments are the files uploaded to the Adaptive Form by the user. You can use the **[!UICONTROL Attachment Path]** option to specify the folder name in which to store these attachments. The folder is created relative to the payload. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.

1. Select an option from the **[!UICONTROL Documents of record using]** drop-down list. 
    
    **Document of Record**: The Document of Record contains the printable, archival record generated for the Adaptive Form. You can use the **[!UICONTROL Document of Record Path]** option to specify the name of the Document of Record file and the path of the file relative to the payload. For example, the `/addresschange/DoR.pdf` path creates a folder named `addresschange` relative to the payload and places `DoR.pdf` relative to the payload. You can also specify only `DoR.pdf` to save only the Document of Record without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.
1. Click **[!UICONTROL Done]**.

    >[!NOTE]
    >
    > Learn more about [Forms-centric AEM Workflows - Step Reference to automate business processes](/help/forms/aem-forms-workflow-step-reference.md).

>[!TAB Universal Editor]

To set up an automated process with an [Adobe Experience Manager (AEM) Workflow](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html?lang=en#extending-aem) for an Adaptive Form authored in Universal Editor, perform the following steps:

1. Open the Adaptive Form for editing.
1. Click the **Edit Form Properties** extension on the editor. 
    The **Form Properties** dialog appears.

    >[!NOTE]
    >
    > * If you do not see the **Edit Form Properties** icon in your Universal Editor interface, enable the **Edit Form Properties** extension in the Extension Manager. 
    > * Refer to the [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions) article to learn how to enable or disable extensions in the Universal Editor.
    
1. Click **Submission** tab and select **[!UICONTROL Invoke an AEM Workflow]** submit action.

    ![Action configuration of Send Email](/help/forms/assets/invoke-service-ue.png)

1. Select workflow model from the **[!UICONTROL Workflow Model]** drop-down list.
1. Select option from the **[!UICONTROL Store Data file using]** drop-down list. 
    
    **Data file**: It contains data submitted to the Adaptive Form. You can use the **[!UICONTROL Data File Path]** option to specify the name of the file and path of file relative to the payload. For example, the `/addresschange/data.xml` path creates a folder named `addresschange` and places it relative to payload. This keeps the submitted data grouped under a dedicated folder within the payload. You can also specify only `data.xml` to send only submitted data without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model. This routes the data file to the external storage destination defined for the workflow instead of the default payload location. 
    
1. Select option from the **[!UICONTROL Store attachments using]** drop-down list. 
    
    **Attachments**: You can use the **[!UICONTROL Attachment Path]** option to specify the folder name to store the attachments uploaded to the Adaptive Form. The folder is created relative to the payload, ensuring uploaded files are stored alongside the workflow data they belong to. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model.

1. Select option from the **[!UICONTROL Documents of record using]** drop-down list. 
    
    **Document of Record**: It contains the Document of Record (DoR) generated for the Adaptive Form, a fixed, archivable rendering of the submitted form. You can use the **[!UICONTROL Document of Record Path]** option to specify the name of the Document of Record file and path of file relative to the payload. For example, the `/addresschange/DoR.pdf` path creates a folder named `addresschange` relative to the payload and places the `DoR.pdf` relative to payload. This ensures the generated record is organized within the workflow payload structure. You can also specify only `DoR.pdf` to save only the Document of Record without creating a folder hierarchy. If the workflow is marked for external data storage, use the variable option and select the variable from the list of variables available for the workflow model. This directs the Document of Record to the external storage location referenced by the workflow rather than the default payload path.
1. Click **[!UICONTROL Done]**.

    >[!NOTE]
    >
    > Learn more about [Forms-centric AEM Workflows - Step Reference to automate business processes](/help/forms/aem-forms-workflow-step-reference.md).

>[!ENDTABS]

<!--
## Best Practices

* When configuring the **[!UICONTROL Invoke an AEM Workflow]** Submit Action, select the appropriate workflow model that aligns with the desired business process.
* In case, the workflow involves external data storage, be sure to configure the workflow accordingly. It is recommended to set up variables appropriately and in accordance with any external storage requirements.
-->

## Related Articles

{{af-submit-action}}
