---
title: Integration of Adobe Workfront Fusion with AEM Forms Submission
description: Adobe Workfront Fusion allows you to focus on new tasks rather than focusing on repetitive tasks. You can connect Adobe Workfront Fusion to an Adaptive Form using Form Submission.
keywords: Integration of Adobe Workfront Fusion with AEM Forms Submission, Adobe Workfront Fusion with AEM Forms, Workfront Fusion with AEM Forms, Connect Workfront Fusion to AEM Forms, AEM Forms and Workfront Fusion, How to connect Workfront Fusion with AEM Forms?, Connect Workfront Fusion to a Form
topic-tags: author, developer
hide: yes
hidefromtoc: yes
---

# Integrate Adobe Workfront Fusion with AEM Forms Submission

[Adobe Workfront Fusion](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-fusion/get-started-with-workfront-fusion/workfront-fusion-overview.html) automates the process of repeating the same tasks, allowing you to focus on new tasks instead of recurring ones. Workfront Fusion connects AEM Forms using services to create scenarios that automatically transfer data. A scenario consists of series of modules which executes data transfer between applications and web services. In a scenario, you orchestrate various modules to automate tasks.

For example, using Workfront Fusion, you can create a scenario to monitor new data in an application using a module in an AEM Form. A subsequent module uses the gathered data to create a record in a table. Once a scenario is set up, Workfront Fusion automatically executes the tasks whenever a user fills out a new form, updating the database seamlessly.

## Advantages of using Adobe Workfront Fusion{#advatages-of-workfront-fusion}

Some of the advantages of using Adobe Workfront Fusion are:

- Automating tasks which are less prone to errors.
- Customizing requirements specific to an organization that are not directly included in Workfront.
- Handling simple logics and straightforward decisions, for example, if/then statements.

## Prerequisites to integrate AEM Forms with Adobe Workfront Fusion {#prerequisites}

You can integrate AEM Forms with Workfront Fusion using Form Submission. Some prerequisites required to connect Workfront Fusion to AEM Forms:

- Ensure user have a valid [Workfront Fusion license](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-fusion/get-started-with-workfront-fusion/license-automation-vs-integration.html).
- Ensure user acquire access to the [Dev Console](https://my.cloudmanager.adobe.com/) and [retrieve the service credentials](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html).

## Integrate AEM Forms with Adobe Workfront Fusion

To connect [Workfront fusion](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-fusion/get-started-with-workfront-fusion/workfront-fusion-overview.html) to a form, perform the following steps:

### 1. Create a Workfront Scenario {#workflow-scenario}

To create a Workfront scenario:
1. Click **[!UICONTROL Scenarios]** ![Share icon](/help/forms/assets/Smock_ShareAndroid_18_N.svg) in the left panel. 
 1. Click **[!UICONTROL Create a new scenario]** in the upper-right corner of the page.
1. Click **[!UICONTROL New scenario]** in the upper-left corner and type a proper name for the scenario.
1. Click the question mark, to add a first module to the scenario and select **[!UICONTROL AEM Forms]**.

      ![Add a AEM Forms module](/help/forms/assets/workfront-aemforms.png)

    >[!NOTE]
    >
    > It is mandatory to add first module as **[!UICONTROL AEM Forms]**.

    The **[!UICONTROL Watch for Form Events]** dialog box appears.
1. Select the **[!UICONTROL Watch for Form Events]** dialog box and a window to add a webhook appears.

#### 1.1 Add a webhook {#add-webhook}

![Add a webhook](/help/forms/assets/workfront-add-webhook.png)

To add a webhook:

1. Click **[!UICONTROL Add]** and a **[!UICONTROL Add a webhook]** dialog box appears.
1. Specify a webhook name.

    >[!NOTE]
    >
    > It is recommended to choose your webhook name carefully, as the specified webhook name appears in the AEM instance.

1. Click **[!UICONTROL Add]** to add new connection. The **[!UICONTROL Create a Connection]** dialog box appears.

#### 1.2 Add a connection to a webhook {#add-connection}

![Add a connection](/help/forms/assets/workfront-add-connection.png)

To add a connection:

1. Specify a connection name in the **[!UICONTROL Create a Connection]** dialog box.

1. Select **Environment** and **Type** from the drop-down list.

1. Enter the **Instance URL**.

    >[!NOTE]
    >
    >Add the Author URL to the instance URL, during testing or development of the Workfront. Change the Author URL to Publish URL while deploying the Workfront Fusion to production.

     You can retrieve the [service credentials from the Developer console](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html) required to create a connection.

1. Replace `ims-na1.adobelogin.com` in the **IMS endpoint** with the value from the service credentials in the Developer console.

1. Specify the following values from the service credentials:
    - **Client ID**
    - **Client Secret**, 
    - **Technical Account ID**
    - **Org ID**
    - **Meta Scopes**
    - **Private Keys**

    >[!NOTE]
    >
    >- Reorganize the Private Key by removing *\r\n* from its value. For example, if the private key value is:
    >*\r\nIJAVO8GDYAOZ9jMA0GCSqGSIb3DQEBCwUAMDAxL\r\nMy1lMTUxODMxLWNtc3RnLWludGVncmF0aW9uLTAw*, then restructure the private key before adding it as:
    >*IJAVO8GDYAOZ9jMA0GCSqGSIb3DQEBCwUAMDAxL**My1lMTUxODMxLWNtc3RnLWludGVncmF0aW9uLTAw*
    >- You also have the option to retrieve a private key or certificate from the file by selecting the **Extract** button.

1. Click **Continue**.

    The created connection starts appearing in the drop-down list of the **[!UICONTROL Connection]** in the **[!UICONTROL Add a webhook]** dialog box.

1. Select the created connection **[!UICONTROL Connection]** from the drop-down list.
1. Click **[!UICONTROL Save]**.
1. Click **[!UICONTROL Ok]** and save the changes for the scenario.

#### 1.3 Activate the Workfront scenario {#activate-scenario}

To make the scenario active:

1. Click **[!UICONTROL Scenarios]** ![Share icon](/help/forms/assets/Smock_ShareAndroid_18_N.svg) in the left panel. 
1. Click the **[!UICONTROL Inactive Scenario]** tab.
1. Click the **ON/OFF** toggle button for the created scenario.

Once you click the toggle button, the Workfront scenario starts appearing in the **[!UICONTROL Active Scenario]** tab.


### 2. Configure submit action of an Adaptive Form for Workfront Fusion

To configure submit action of an Adaptive Form for Workfront Fusion:

1. Log in to your AEM instance.
1. Go to **[!UICONTROL Forms]** > **[!UICONTROL Forms and Documents]** > **[!UICONTROL Create]** > **[!UICONTROL Adaptive Form]**. The **[!UICONTROL Create Form]** wizard appears.
1. Select an Adaptive Form template from the **[!UICONTROL Source]** tab.
1. Select a theme from the **[!UICONTROL Style]** tab.
1. Select the **[!UICONTROL Invoke a WorkFront Fusion Scenario]** from the **[!UICONTROL Submission]** tab.
1. Select the created webhook from the **[!UICONTROL Options]** tab in the **[!UICONTROL Properties]** window.

    >[!NOTE]
    >
    > The webhook name of the WorkFront scenario appears in the **Options** drop-down list.

1. Click **[!UICONTROL Create]**.
1. Specify the name for Adaptive Form and click **[!UICONTROL Create]**.


## Best Practices {#best-practices}

- During testing or development of Workfront, add the Author URL to the instance URL. However, when deploying Workfront Fusion in a production environment, it is recommended to update the Author URL with the Publish URL.

- It is recommended to choose your web hook name carefully, as there is no way to get the scenario name at the AEM instance. In case, you change the web hook name in future it is not reflected at the AEM Forms submit action drop-down list.
- A scenario can have multiple web hook links but at a time only one webhook link is active. It is recommended to delete the unlinked webhook, so that it does not appear in AEM Forms submit action drop-down list.
