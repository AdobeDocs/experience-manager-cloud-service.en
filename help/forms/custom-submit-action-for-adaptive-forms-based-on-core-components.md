---
title: How to Create a Custom Submit Action for an Adaptive Form based on core components?
description: Learn how to create a custom Submit Action for an Adaptive Forms to process data before submitting it using the customized submit action.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Intermediate
exl-id: a369b585-d148-4b5a-8afe-d5673ea865d0
---
# Create a custom submit action for Adaptive Forms (Core Components)

A submit action allows users to select the destination for the data captured from a form and to define additional functionality to be executed on form submission. AEM form supports multiple [submit actions out-of-the-box (OOTB)](/help/forms/configure-submit-actions-core-components.md), such as sending an email or saving data to SharePoint or OneDrive.

You can also create a custom submit action to add functionality not included in the [out-of-the-box options](/help/forms/configure-submit-actions-core-components.md#select-and-configure-a-submit-action-for-an-adaptive-form-select-and-configure-submit-action). For example, integrate the form data with a third-party application or trigger a personalized SMS notification based on user input.

<!-- ![Custom Submit Image](/help/forms/assets/custom-submit-action-hero-image.png)
-->

## Pre-requisites

Before you begin creating your first custom submit action for Adaptive Forms, ensure you have the following:

* **Plain Text Editor (IDE)**: While any plain text editor can work, an Integrated Development Environment (IDE) like Microsoft Visual Studio Code offers advanced features for easier editing.

* **Git**: This version control system is required for managing code changes. If you do not have it installed, download it from https://git-scm.com.

## Create your first custom submit action for form

The below diagram depicts the steps to create a custom submit action for an Adaptive Form:

![Custom submit action workflow](/help/forms/assets/custom-submit-action-workflow.png){width=50%, height-50%}

### Clone AEM as a Cloud Service Git repository.

1. Open the command line and choose a directory to store your AEM as a Cloud Service repository, such as `/cloud-service-repository/`.

1. Run the below command to clone the repository:

    ```
    git clone https://git.cloudmanager.adobe.com/<organization-name>/<app-id>/
    ```
    **Where to find this information?**

    For step-by-step instructions on locating these details, refer to the Adobe Experience League article "[Accessing Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git)".

    **Your project is ready!**

    When the command completes successfully, you see a new folder created in your local directory. This folder is named after your application (for example, app-id). This folder contains all the files and code downloaded from your AEM as a Cloud Service Git repository. You can find `<appid>` for your AEM Project in the `archetype.properties` file. 

    ![Archetype Properties](/help/forms/assets/custom-submit-action-archetype-app-id.png)

    Throughout this guide, we refer to this folder as the `[AEMaaCS project directory]`.

## Add new submit action

1. Open the repository folder in an editor. 

    ![Clonned Repository](/help/forms/assets/custom-submit-action-clone-repo.png)

1. Navigate to the following directory within your `[AEMaaCS project directory]`:

    ```
    /ui.apps/src/main/content/jcr_root/apps/<app-id>/

    ```
    **Important**: Replace `<app-id>` with your actual application ID.

1. Create new folder for your custom submit action and give it a name of your choice. For example, name the folder as `customsubmitaction`.

    ![Create custom submit action folder](/help/forms/assets/custom-submit-action-create-folder.png)

1. Navigate to the added custom submit action directory.

    Within your `[AEMaaCS project directory]`, navigate to the following path:

    `/ui.apps/src/main/content/jcr_root/apps/<app-id>/customsubmitaction/`

    `Important`: Replace <app-id> with your actual application ID.

1. Create new configuration file.
   Within the `customsubmitaction` folder, create a new file named `.content.xml`. 

    ![Create Config File](/help/forms/assets/custom-submit-action-create-config-folder.png)

1. Open this file and paste the following content, replacing `[customsubmitaction]` with the name of your submit action 

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <jcr:root xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:sling="http://sling.apache.org/jcr/sling/1.0"
    jcr:description="[customsubmitaction]"
    jcr:primaryType="sling:Folder"

    guideComponentType="fd/af/components/guidesubmittype"
    guideDataModel="basic,xfa,xsd"
    submitService="[customsubmitaction]"/>
    ```

    For example, replace the `[customsubmitaction]` with your customized submit action name as `Custom Submit Action`.

      ![Create custom submit action configuration file](/help/forms/assets/custom-submit-action-config-file.png)

    >[!NOTE]
    >
    > Remember the name of the [customsubmitaction], as the same name appears in the `Submit action` drop-down list while authoring a form.


**Include the new folder in `filter.xml`**

1. Navigate to the `/ui.apps/src/main/content/META-INF/vault/filter.xml` file in your [AEMaaCS project directory].

1. Open the file and add the following line at the end:

    ```
    <filter root="/apps/<app-id>/[customsubmitaction-folder]"/>
    ```
    For example, add the following line of code to add the `customsubmitaction` folder in the `filter.xml` file:

    ```
    <filter root="/apps/wknd/customsubmitaction"/>
    ```

    ![Add the created folders in the filter.xml](/help/forms/assets/custom-submit-action-filter-xml.png)

1. Save the changes.

### Implement the service for the added submit action.

1. Navigate to the following directory within your `[AEMaaCS project directory]`:
    `/core/src/main/java/com/<app-id>/core/service/`
    `Important`: Replace <app-id> with your actual application ID.
1. Create new Java file to implement the service for the added submit action. For example, add new Java file as `CustomSubmitService.java`.

    ![Custom Submit Action Folder](/help/forms/assets/custom-submit-action-custom-submit-folder.png)

1. Open this file and add the code for your custom submit action implementation. 
        
    For example, the below Java code is an OSGi service that handles the form submission by logging the submitted data and returns a status `OK`. Add the following code in the `CustomSubmitService.java` file: 

    ```
    package com.wknd.core.service;

    import com.adobe.aemds.guide.model.FormSubmitInfo;
    import com.adobe.aemds.guide.service.FormSubmitActionService;
    import java.util.HashMap;
    import java.util.Map;
    import org.osgi.service.component.annotations.Component;
    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;

        @Component(
        service = FormSubmitActionService.class,
        immediate = true
            )
        public class CustomSubmitService implements FormSubmitActionService {

        private static final String serviceName = "Custom Submit Action";

        private static Logger log = LoggerFactory.getLogger(CustomSubmitService.class);

        @Override
        public String getServiceName() {
        return serviceName;
        }

        @Override
        public Map<String, Object> submit(FormSubmitInfo formSubmitInfo) {
        String data = formSubmitInfo.getData();
        log.info("Using custom submit action service, [data] --> " + data);
        Map<String, Object> result = new HashMap<>();
        result.put("status", "OK");
        return result;
         }
        }
    ```

    ![Custom Submit Action Service](/help/forms/assets/custom-submit-action-service.png)

1. Save the changes.

### Deploy the code.

**Deploy code for local development environment** 

* Deploy the AEM as a Cloud Service, `[AEMaaCS project directory]`, to your local development environment to try the new submit action on your local machine. To deploy to your local development environment:

    1. Ensure that your local development environment is up and running. If you have not already set up a local development environment, refer to the guide on [Setup a local development environment for AEM Forms](/help/forms/setup-local-development-environment.md).

    1. Open the terminal window or command prompt.

    1. Navigate to the `[AEMaaCS project directory]`.

    1. Run the following command:

        ```
        mvn -PautoInstallPackage clean install
        ```
        ![Local Deployment](/help/forms/assets/custom-submit-action-local-deployment.png)

**Deploy the code for the Cloud Service environment**

* Deploy the AEM as a Cloud Service, `[AEMaaCS project directory]`, to your Cloud Service environment. To deploy to your Cloud Service environment:

    1. Commit your changes:

        After adding the new custom submit action configuration, commit your changes with a clear Git message. (For example, "Added new custom submit action"). 

    1. Deploy the updated code:

        Trigger a deployment of your code through the [existing full-stack pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline). It automatically builds and deploys the updated code with the new custo m submit action support.

        If you haven't already set up a pipeline, refer to the guide on [how to set up a pipeline for AEM Forms as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline).

         ![Cloud Deployment](/help/forms/assets/custom-submit-action-cloud-deployment.png)

        **How to confirm the installation?**

        Once the project is built successfully, the custom submit action appears in the `Submit action` drop-down list while authoring a form. 

        ![Custom Submit Action Drop-Down list](/help/forms/assets/custom-submit-action-drop-down-list.png)

    Your environment is now ready to use the added custom submit action when authoring a form.

### Preview an Adaptive Form with newly added submit action
 
1. Log in to your AEM Forms as a Cloud Service instance.
1. Go to **Forms** >  **Forms and Documents**.

    ![Forms and Documents](/help/forms/assets/custom-submit-action-fnd.png)

1. Select an Adaptive Form and click **Edit**. The form opens in edit mode. 

    ![Edit Form](/help/forms/assets/custom-submit-action-edit-af.png)

1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens. 
1. Click the  **[!UICONTROL Submission]** tab. 
1. From the **[!UICONTROL Submit Action]** drop-down list, select the submit action. For example, select the submit action as `Custom Submit Action`. 

    ![Custom Submit Form](/help/forms/assets/custom-submit-action-select-submit-action.png)

1. Fill out the form and submit it.

    ![Submit Form](/help/forms/assets/custom-submit-action-submit-form.png)

    ![Thankyou message](/help/forms/assets/custom-submit-action-thankyou-msg.png)

    Once the form is submitted successfully, you can check the **Adobe Experience Manager Web Console Configuration** to verify the action of the custom submit action in the local development environment.
1. Go to `http://<host>:<port>/system/console/configMgr`.

1. Navigate to the **Adobe Experience Manager Web Console Log Support** at `http://<host>:<port>/system/console/slinglog`.

    ![ConfigMgr](/help/forms/assets/custom-submit-action-sling-log.png)

1. Click the `logs/error.log` option. 
      ![Open error.log file](/help/forms/assets/custom-submit-action-error-log.png)

1. Open the `error.log` file to see that the data has been appended to it.

    ![error.log file](/help/forms/assets/custom-submit-action-form-data-display.png)

    >[!NOTE]
    >
    > To view error logs in the AEM as a Cloud Service environment, you can use Splunk. 

<!--
## Best practices

 * It is recommended to use the OSGi service approach for creating a custom submit action, as it is faster than the AEM servlet approach. 

## Next steps
-->

## Related Articles

{{af-submit-action}}

<!-- The [Adaptive Forms Core Components](https://github.com/adobe/aem-core-forms-components) repository includes a sample folder, `customsubmission/logsubmit`, to simplify the process of adding new custom submit actions. It also provides the Java service implementation for the `logsubmit` custom submit action, named `CustomAFSubmitService`.java. These resources are available on GitHub. -->
