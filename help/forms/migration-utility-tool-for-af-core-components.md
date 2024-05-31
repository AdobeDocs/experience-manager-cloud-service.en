---
title: Migration Utility to convert Adaptive Forms based on foundation components to core component based forms
description: Learn to install and used Migration Utility to convert Adaptive Forms based on Foundation components to core component based forms.
Keywords: Migration Utility tool, Convert Adaptive Forms based on foundation components to core component based forms, Convert Foundation forms to Core components forms, Using Modernizer tool to convert Foundation Components to Core components in forms.
role: User, Developer, Admin
features: core components
hide: yes
hidefromtoc: yes
---

# Introduction 

You can use the migration utility to convert Adaptive Forms based on foundation components to core component-based forms. You can use the [AEM Modernize tool](https://opensource.adobe.com/aem-modernize-tools/) as a migration utility tool. The [AEM Modernize tools](https://opensource.adobe.com/aem-modernize-tools/) provide a suite of utilities used to convert Adaptive Forms based on foundation components to the modern and supported capabilities of core components.

## What is AEM Modernize Tools?

[AEM Modernize tools](https://opensource.adobe.com/aem-modernize-tools/) refers to a set of utilities or software applications designed to facilitate the process of modernizing or updating Adobe Experience Manager (AEM) projects. These tools typically assist in converting older components or functionalities within AEM to newer, more efficient, and supported alternatives.

AEM Modernize Tools converts Adaptive Forms that are based on older foundation components to newer core component-based forms. This conversion process ensures that the forms align with modern standards and capabilities, potentially improving performance, compatibility, and ease of maintenance within the AEM environment.

![AEM Modernize Tools](/help/forms/assets/aem-modernize-tools.png)

>[!NOTE]
> 
> It is recommended to install the AEM Modernize Tools on your local AEM setup. Migrate the foundation-based forms to core component-based forms. Download the form along with its assets. Then, upload the form and its assets to the required environment.

## Pre-requisites to use AEM Modernize Tools

* [Set up local development environment for AEM Forms](/help/forms/setup-local-development-environment.md)
* [Enable Adaptive Forms core components for your environment.](/help/forms/enable-adaptive-forms-core-components.md)

* Add your users to the [!DNL forms-users] group. The members of the [!DNL forms-users] group have permissions to create an Adaptive Form. 

* Users with the following roles have the permissions to install the AEM Modernize Tools within an AEM environment:
  * Developer role
  * Admin role
  For a detailed list of forms-specific user groups, see [Groups and permissions](forms-groups-privileges-tasks.md).

## Install and configure AEM Modernize Tools 

Steps to install and configure AEM Modernize tools:

1. [Install AEM Modernize Tools to your local AEM Forms environment](#install-aem-modernize-tools)
2. [Enable AEM Modernize Tools for your local AEM Forms environment](#enable-aem-modernize-tools)

### Install AEM Modernize Tools to your local AEM Forms environment {#install-aem-modernize-tools}

Perform the following steps to install AEM Modernize Tools to your local AEM Forms environment:

1. Start the local AEM Author Service by executing the following from the command line:

    `java -jar aem-author-p4502.jar`

    >[!NOTE]
    >
    > Provide the admin password as `admin`. Any admin password is acceptable, however it is recommend using the default for local development to reduce the need to reconfigure.

1. Clone the [AEM Modernize Tools](https://git.corp.adobe.com/livecycle/forms-modernizer/tree/convertForms) repository in your local system.

    ```Shell 

    git clone [Path of Git repository of AEM Modernize Tools]

    ```
    Replace the [Path of the Git repository of AEM Modernize Tools] with the actual URL of the corresponding Git Repository of the AEM Modernize Tools. 
    After executing the command successfully, you have a local copy of the AEM Modernize Tools repository available on your machine.

1. Navigate to the`[AEM Modernize Tools Repository]`  in your local system.
1. Run the following command: 

    ```Shell
        mvn clean install 
    
    ```
 ![Succesful installation image](/help/forms/assets/aem-modernize-install-steps.png)

After successful installation, AEM Modernize Tools become available for your environment. 

![Enable AEM Modernize Tools](/help/forms/assets/enable-aem-modernizer-tools.png) 


### Enable AEM Modernize Tools for your local AEM Forms environment{#enable-aem-modernize-tools}

To enable and use the AEM Modernize Tools for your AEM Environment, it is important to map the rules for migrating foundation components to core components:

1. Log in to your author instance.
1. Navigate to `http://[host]:[port]/system/console/configMgr`
1. Find and edit the `AEM Modernize Tools - Component Rewrite Rule Service`.
1. Add the `Component Rule Paths` as `/apps/forms-modernizer/rules`. 
1. Click **Save** to save the changes.

![AEM Modernize Component Rule](/help/forms/assets/aem-modernize-tools-component-rule.png)

## Run AEM Modernize Tools to convert foundation components based forms to core component based forms 

1. Go to **[!UICONTROL Tools > AEM Modernize Tools > Forms Conversion]**.
   
   ![Select AEM Modernize tools](/help/forms/assets/aem-modernize-tools-select.png)

1. Select the **[!UICONTROL Forms Conversion]** option.
   
   ![Select Forms Conversion option](/help/forms/assets/aem-modernize-forms-conversion.png)

1. Click **Create** to create a new job.

    ![AEM Modernize Tools Create Job](/help/forms/assets/aem-modernize-tools-create-job.png)

1. Specify the **[!UICONTROL Job Name]**.
1. In the **[!UICONTROL Form]** tab, you can select one of the following options:
   * **None** : Select this option if form handling is not required.
   * **Restore** : Select this option to restore the form to the state before the last conversion.
   * **Copy to Target**: Select this option to copy the form before performing the conversion.
  In our case, the **Copy to Target** option is selected. If the **Copy to Target** option is selected, the **[!UICONTROL Source Path]** and **[!UICONTROL Target Path]** options become visible.

1. Specify the `source folder` name in the **[!UICONTROL Source Path]**.
1. Specify the `target folder` name in the **[!UICONTROL Target Path]**.
1. Select **[!UICONTROL Next]**.
1. Click on **[!UICONTROL Add Forms]**. All the forms in the `source folder` appears on the screen.
1. Select the form based on foundation components to convert it to form based on core components. You can also select multiple forms.

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

You can now see that the Adaptive Form built on foundation components transforms into the Adaptive Form built on core components. 

## Considerations while using the Migration Utility tool {#considerations}

* If the form built on foundation components contains custom function rules, you have to rewrite these rules for the converted form based on core components. 
* The converted form does not include any rules in the rule editor, requiring the rewriting of rules for the converted form.
* You have to recreate the translation job for the converted form.

## Best Practices {#best-practices}

* The form built on foundation components includes only those components found in the core component-based components.
* Make sure that the rules are formatted in XML.


