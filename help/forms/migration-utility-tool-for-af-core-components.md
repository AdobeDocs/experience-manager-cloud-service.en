---
title: Migration Utility Tool/AEM Modernize Tools to convert Adaptive Forms based on Foundation Components to Core Component based forms
description: Learn to install and use Migration Utility/AEM Modernize Tools to convert Adaptive Forms based on Foundation Components to Core Component based forms.
Keywords: Migration Utility Tool, Convert Adaptive Forms based on Foundation Components to Core Component based forms, Convert Foundation forms to Core Components forms, Using Modernizer Tool to convert Foundation Components to Core Components in forms.
role: User, Developer, Admin
features: core components
hide: yes
hidefromtoc: yes
exl-id: ee71a576-96a7-4c81-b3a3-1d678f010cba
feature: Adaptive Forms, Core Components
---
# Introduction 

<span class="preview"> The feature is available under the early adopter program. You can write to aem-forms-ea@adobe.com from your official email id to join the early adopter program and request access to the capability. </span>

The Forms Conversion Utility, part of the [AEM Modernize Tool](https://opensource.adobe.com/aem-modernize-tools/) suite, helps you easily convert Adaptive Forms built with legacy Foundation Components to forms that leverage the modern, supported capabilities of Core Components.

## What is AEM Modernize Tools?

[AEM Modernize Tools](https://opensource.adobe.com/aem-modernize-tools/) refers to a set of utilities or software applications designed to facilitate the process of modernizing or updating Adobe Experience Manager (AEM) projects. These Tools typically assist in converting older components or functionalities within AEM to newer, more efficient, and supported alternatives. The Forms Conversion Utility is installed under AEM Modernize Tools to convert Adaptive Forms based on Foundation Components to Core Component based forms.

The Forms Conversion Utility converts Adaptive Forms that are based on older Foundation Components to newer Core Component based forms. This conversion process ensures that the forms align with modern standards and capabilities, potentially improving performance, compatibility, and ease of maintenance within the AEM environment.

![AEM Modernize Tools](/help/forms/assets/aem-modernize-tools.png)

>[!NOTE]
> 
> It is recommended to install the AEM Modernize Tools on your local AEM setup. Migrate the Adaptive Forms based on Foundation Components to Core Component based forms. Download the form along with its assets. Then, upload the form and its assets to the required environment.

## Considerations while using the AEM Modernize Tools {#considerations}

 * On successful conversions, all the rules applied to the form are removed. Rules are not automatically migrated. You should manually recreate and apply these rules to the converted form.
* The translation settings used in the original form are not carried over. Reconfigure translation for the converted form.
* If the form built on Foundation Components contains scripts or custom function rules, you have to rewrite these for the converted form based on Core Components.
* The following OOTB foundation components are not yet supported in Core Components and are therefore deleted in the converted form:
  * Adobe Sign Block
  * Chart
  * File Attachment Listing
  * Footnote Placeholder
  * Image Choice
  * Next Button
  * Previous Button
  * Scribble Signature
  * Summary Step
  * Toolbar

## Pre-requisites to use AEM Modernize Tools

* [Set up local development environment for AEM Forms](/help/forms/setup-local-development-environment.md)
* [Enable Adaptive Forms Core Components for your environment.](/help/forms/enable-adaptive-forms-core-components.md)

* Add your users to the [!DNL forms-users] group. The members of the [!DNL forms-users] group have permissions to create an Adaptive Form. 

* Users with the following roles have the permissions to install the AEM Modernize Tools within an AEM environment:
  * Developer role
  * Admin role

For a detailed list of forms-specific user groups, see [Groups and permissions](forms-groups-privileges-tasks.md).

## Install and configure AEM Modernize Tools 

To install and configure the AEM Modernize Tools:

1. [Install AEM Modernize Tools to your local AEM Forms environment](#install-aem-modernize-Tools)
2. [Enable AEM Modernize Tools for your local AEM Forms environment](#enable-aem-modernize-Tools)

### Install AEM Modernize Tools to your local AEM Forms environment {#install-aem-modernize-Tools}

Perform the following steps to install AEM Modernize Tools to your local AEM Forms environment:

1. Open the command prompt or terminal.
1. Start the local AEM Author Service. For example, execute the following code from the to start local AEM Author instance:

    `java -jar aem-author-p4502.jar`

1. Clone the [AEM Modernize Tool](https://github.com/adobe/forms-modernizer) repository in your local system.

    ```Shell 

    git clone [Path of Git repository of AEM Modernize Tool]

    ```

    After executing the command successfully, you have a local copy of the AEM Modernize Tool repository available on your machine.

1. Navigate to the`[AEM Modernize Tool Repository]`  in your local system.
1. Run the following command: 

    ```Shell
        mvn clean install 
    
    ```
 ![Succesful installation image](/help/forms/assets/aem-modernize-install-steps.png)

After successful installation, the AEM Modernize Tools becomes available for your environment. 

![Enable AEM Migration Utility Tool](/help/forms/assets/enable-aem-modernizer-tools.png) 


### Enable AEM Modernize Tools for your local AEM Forms environment{#enable-aem-modernize-Tools}

To enable and use the AEM Modernize Tools for your AEM Environment, it is important to map the rules for migrating Foundation Components to Core Components:

1. Log in to your author instance.
1. Navigate to `http://[host]:[port]/system/console/configMgr`
1. Find and edit the `AEM Modernize Tools - Component Rewrite Rule Service`.
1. Add the `Component Rule Paths` as `/apps/forms-modernizer/rules`. 
1. Click **Save** to save the changes.

![AEM Modernize Component Rule](/help/forms/assets/aem-modernize-tools-component-rule.png)

## Run the Form Conversion utility to convert Foundation Components based forms to Core Component based forms 

1. Go to **[!UICONTROL Tools > AEM Modernize Tools > Forms Conversion]**.
   
   ![Select AEM Modernize Tools](/help/forms/assets/aem-modernize-tools-select-form.png)

1. Select the **[!UICONTROL Forms Conversion]** option.
   
   ![Select Forms Conversion option](/help/forms/assets/aem-modernize-forms-conversion.png)

1. Click **Create** to create a new job.

    ![AEM Modernize Tools Create Job](/help/forms/assets/aem-modernize-tools-create-job.png)

1. Specify the **[!UICONTROL Job Name]**.
1. In the **[!UICONTROL Form]** tab, you can select one of the following options:
   * **None** : Select the option if you do not want to create a copy of the Foundation Component based forms before starting the form conversion.
   * **Restore** : Select the option to restore the form to the state it was in before starting the form conversion.
   * **Copy to Target**: Select the option to create a copy of the Foundation Component based forms before starting the form conversion.
  In our case, the **Copy to Target** option is selected. If the **Copy to Target** option is selected, the **[!UICONTROL Source Path]** and **[!UICONTROL Target Path]** options become visible.

1. Specify the `source folder` name in the **[!UICONTROL Source Path]**.
1. Specify the `target folder` name in the **[!UICONTROL Target Path]**.
1. Select **[!UICONTROL Next]**.
1. Click on **[!UICONTROL Add Forms]**. All the forms in the `source folder` appear on the screen.
1. Select the Adaptive Forms based on Foundation Components to convert it to Core Component based forms. You can also select multiple forms.

    ![AEM Modernize Tools Select Form](/help/forms/assets/aem-modernize-tools-select-form.png)

1. Click **[!UICONTROL Select]**.
1. Click **[!UICONTROL Schedule Job]** to start the conversion process.
1. Click **[!UICONTROL Convert]** from the **[!UICONTROL Convert Pages]** dialog box.

   ![AEM Modernize Tools Convert Pages](/help/forms/assets/aem-modernize-tools-convert-form.png)

   When the status of the process is changed to `success`. Navigate to the `target folder` to see the converted form.

   ![AEM Modernize Tools Success](/help/forms/assets/aem-modernize-tools-success.png)

1.  Select the Adaptive Form and select > **[!UICONTROL Properties]**. The Form Properties page opens. 
     ![AEM Modernize Tools Destination Folder](/help/forms/assets/aem-modernize-tools-destination-folder.png)

1. Select **[!UICONTROL Save and Close]** to save the properties of the converted form again.
    ![AEM Modernize Tools Adpative Form Properties](/help/forms/assets/aem-modernize-tools-af-properties.png)

You can now see that the Adaptive Form built on Foundation Components transforms into the Adaptive Form built on Core Components. 

## Best Practices {#best-practices}

* Ensure your Foundation Components based forms, use only those components that have an equivalent [Core Components](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/introduction#available-components-a-breakdown-by-component-type) available. In cases where you use Foundation Components that do not have an equivalent Core Component, the Foundation Component is not converted. As a result, it does not function properly while authoring a form
* Make sure that the rules to covert the Foundation Components to Core Components are formatted in XML.
