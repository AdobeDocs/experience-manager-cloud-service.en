---
title: Integration of Adobe Workfront Fusion with AEM Forms Submission
description: Adobe Workfront Fusion allows you to focus on new tasks rather than focusing on repetitive tasks. You can connect Adobe Workfront Fusion to an Adaptive Form using Form Submission.
keywords: Submit an Adaptive Form to Adobe Workfront Fusion, Integration of Adobe Workfront Fusion with AEM Forms Submission, Adobe Workfront Fusion with AEM Forms, Workfront Fusion with AEM Forms, Connect Workfront Fusion to AEM Forms, AEM Forms and Workfront Fusion, How to connect Workfront Fusion with AEM Forms?, Connect Workfront Fusion to a Form
topic-tags: author, developer
feature: Adaptive Forms, Foundation Components, Edge Delivery Services, Core Components
role: Admin, User
exl-id: d3efb450-a879-40ae-8958-0040f99bdafc
---
# Submit an Adaptive Form to Adobe Workfront Fusion

<span class="preview"> The feature is available under early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

[Adobe Workfront Fusion](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-fusion/get-started-with-workfront-fusion/workfront-fusion-overview.html) automates the process of repeating the same tasks, like document approval workflows, email filtering and sorting, allowing you to focus on new tasks instead of recurring ones. Adobe Workfront Fusion includes multiple scenarios. A scenario consists of series of modules which executes data transfer between applications and web services. In a scenario, you add various steps (modules) to automate a task. 

For example, using Workfront Fusion, you can create a scenario to gather data with Adaptive Form, process the data, and send the data to a data store for archival. Once a scenario is set up, Workfront Fusion automatically executes the tasks whenever a user fills out a form, updating the data store seamlessly.

AEM Forms as a Cloud Service provides an OOTB connector to connect and submit an Adaptive Form to Adobe Workfront Fusion. Submitting a form to Adobe Workfront Fusion can offer several advantages:
* It enabled seamless transfer of form submissions data to Workfront Fusion workflows.
* It helps automate various tasks triggered by form submissions. This can include initiating projects, assigning tasks to specific team members, sending notifications, and updating project statuses—all without manual intervention.
* All form submissions captured within Workfront Fusion, provide a single source of truth for project-related information


<!--  AEM as a Cloud Service offers various out of the box submit actions for handling form submissions. You can learn more about these options in the [Adaptive Form Submit Action](/help/forms/configure-submit-actions-core-components.md)  article.-->

>[!VIDEO](https://video.tv.adobe.com/v/3427145/adaptive-forms-adobe-workfront-af-workfront-workfront-aem-forms/?quality=12&learn=on)

<span> This video is applicable only for Core Components. For UE/Foundation Components, please refer to the article.</span>

## Prerequisites to integrate AEM Forms with Adobe Workfront Fusion {#prerequisites}

To establish a connection between Workfront Fusion and AEM Forms, the following are necessary:

* A valid [ Workfront and Workfront Fusion license](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-fusion/get-started-with-workfront-fusion/license-automation-vs-integration.html).
* An AEM user with right to access [Dev Console](https://my.cloudmanager.adobe.com/) to [retrieve the service credentials](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html).

## Integrate AEM Forms with Adobe Workfront Fusion

### 1. Create a Workfront Scenario {#workflow-scenario}

To create a Workfront scenario, perform the following steps:

1. [Create a scenario](#create-scenario)
1. [Add a web hook to a scenario](#add-webhook)
1. [Add a connection to a web hook](#add-connection)

#### Create a scenario {#create-scenario}

To create a scenario:

1. Sign into your [Workfront Fusion account](https://app-qa.workfrontfusion.com/).
1. Click **[!UICONTROL Scenarios]** ![Share icon](/help/forms/assets/Smock_ShareAndroid_18_N.svg) in the left panel. 
 1. Click **[!UICONTROL Create a new scenario]** in the upper-right corner of the page. A page to create new scenario appears on-screen.
1. Select **[!UICONTROL New scenario]** in the upper-left corner on the page and type a proper name for the scenario.
1. Click the question mark and make sure you add first module as **[!UICONTROL AEM Forms]**.

    ![Add a AEM Forms module](/help/forms/assets/workfront-aemforms.png)

    The **[!UICONTROL Watch for Form Events]** dialog box appears.

    >[!NOTE]
    >
    > It is mandatory to add first module as **[!UICONTROL AEM Forms]**.

1. Select the **[!UICONTROL Watch for Form Events]** dialog box and a window to add a webhook appears.

#### Add a webhook {#add-webhook}

![Add a webhook](/help/forms/assets/workfront-add-webhook.png)

To add a webhook:

1. Click **[!UICONTROL Add]** and a **[!UICONTROL Add a webhook]** dialog box appears.
1. Specify a webhook name.

    >[!NOTE]
    >
    > It is recommended to choose your webhook name carefully, as the specified webhook name appears in the AEM instance. 

1. Click **[!UICONTROL Add]** to add new connection. The **[!UICONTROL Create a Connection]** dialog box appears.

>[!NOTE]
>
> Ensure that the Technical Account is a member of the **forms-users** group; otherwise, adding a webhook fails.

#### Add a connection to a webhook {#add-connection}

![Add a connection](/help/forms/assets/workfront-add-connection.png)

To add a connection:

1. Specify a **[!UICONTROL Connection Name]** in the **[!UICONTROL Create a Connection]** dialog box.

1. Select **Environment** and **Type** from the drop-down list.

1. Enter the **Instance URL**.

    >[!NOTE]
    >
    > Instance URL is the unique web address which points to a specific AEM Forms instance.

    You can retrieve the [service credentials from the Developer console](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html) required to create a connection.

1. Replace `ims-na1.adobelogin.com` in the **IMS endpoint** with the value of **imsEndpoint** from the service credentials in the Developer console.

    >[!NOTE]
    >
    > Retain the `https://` in the **IMS endpoint** textbox while adding the `imsEndpoint` URL. 

1. Specify the following values in the **[!UICONTROL Create a Connection]** dialog box:
    * Specify **Client ID** with value of **clientId** from the service credentials in the Developer console.
    * Specify **Client Secret** with value of **clientSecret** from the service credentials in the Developer console.
    * Specify **Technical Account ID**  with value of **id** from the service credentials in the Developer console.
    * Specify **Org ID**  with value of **org** from the service credentials in the Developer console.
    * **Meta Scopes**  with value of **metascopes** from the service credentials in the Developer console.
    * **Private Keys**  with value of **privateKey** from the service credentials in the Developer console.

    >[!NOTE]
    >
    >* For **Private Key**, remove `\r\n` from its value. 
    >  For example, if the private key value is:
    >`\r\nIJAVO8GDYAOZ9jMA0GCSqGSIb3DQEBCwUAMDAxL\r\nMy1lMTUxODMxLWNtc3RnLWludGVncmF0aW9uLTAw`, then after removing the `\r\n` from the private key, the key would look like the following, with both the values appearing in a separate line: 
    >
    >   `IJAVO8GDYAOZ9jMA0GCSqGSIb3DQEBCwUAMDAxL`
    >
    >   `My1lMTUxODMxLWNtc3RnLWludGVncmF0aW9uLTAw`
    > 
    >* You also have the option to retrieve a private key or certificate from the file by selecting the **Extract** button.

1. Click **Continue**.

    The created connection starts appearing in the drop-down list of the **[!UICONTROL Connection]** in the **[!UICONTROL Add a webhook]** dialog box.

1. Select the created connection **[!UICONTROL Connection]** from the drop-down list.
1. Click **[!UICONTROL Save]**.
1. Click **[!UICONTROL OK]** and save the changes for the scenario.
1. To activate the scenario, click the ON/OFF toggle button in the scenario editor.

>[!NOTE]
>
> In case you do not activate the Workfront scenario, it does not detect the form submission, and setting the submit action to Workfront results in a failed submission.

### 2. Configure submit action of an Adaptive Form for Workfront Fusion

>[!BEGINTABS]

>[!TAB Foundation Component]

To configure submit action of an Adaptive Form based on Foundation Components for Workfront Fusion:

1. Open the Adaptive Form for editing and navigate to **[!UICONTROL Submission]** section of the Adaptive Form Container properties. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Invoke a WorkFront Fusion Scenario]**.
    ![Submit action for Workfront Fusion](/help/forms/assets/workfront-fusion-fc.png)

1. Select **[!UICONTROL Workfront Fusion scenario]** from the drop-down list.
1. Click **[!UICONTROL Done]**.


>[!TAB Core Component]

To configure submit action of an Adaptive Form based on Core Components for Workfront Fusion:

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select **[!UICONTROL Invoke a WorkFront Fusion Scenario]**.
   
    ![Submit action for Workfront Fusion](/help/forms/assets/workfront-scenario-existing-af.png)
1. Select **[!UICONTROL Workfront Fusion scenario]** from the drop-down list.
1. Click **[!UICONTROL Done]**.

>[!TAB Universal Editor]

To configure submit action of an Adaptive Form authored using Universal Editor:

1. Open the Adaptive Form for editing.
1. Click the **Edit Form Properties** extension on the editor. 
    The **Form Properties** dialog appears.

    >[!NOTE]
    >
    > * If you do not see the **Edit Form Properties** icon in your Universal Editor interface, enable the **Edit Form Properties** extension in the Extension Manager. 
    > * Refer to the [Extension Manager Feature Highlights](https://developer.adobe.com/uix/docs/extension-manager/feature-highlights/#enablingdisabling-extensions) article to learn how to enable or disable extensions in the Universal Editor.
    
1. Click **Submission** tab and select **[!UICONTROL Invoke a WorkFront Fusion Scenario]** submit action.

    ![Submit action for Workfront Fusion](/help/forms/assets/workfront-fusion-ue.png)

1. Select **[!UICONTROL Workfront Fusion scenario]** from the drop-down list.
1. Click **[!UICONTROL Save&Close]**.

>[!ENDTABS]

## Best Practices {#best-practices}

* It is recommended to choose your webhook name carefully, as there is no way to get the scenario name at the AEM instance. In case, you change the webhook name in future it is not reflected at the AEM Forms submit action drop-down list.
* A scenario can have multiple webhook links but at a time only one webhook link is active. It is recommended to delete the unlinked webhook, so that it does not appear in AEM Forms submit action drop-down list.

<!-- During testing or development of Workfront, add the Author URL to the instance URL. However, when deploying Workfront Fusion in a production environment, it is recommended to replicate the scenario URLs for the Publish instance. -->

## Related Articles

{{af-submit-action}}