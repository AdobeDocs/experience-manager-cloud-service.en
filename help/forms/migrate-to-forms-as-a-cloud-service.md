---
title: How to migrate from an AEM 6.5 Forms and AEM 6.4 Forms to [!DNL AEM Forms] as a Cloud Service environment?
description: Migrate from an [!DNL AEM Forms] On-Premise environment to [!DNL AEM Forms] as a Cloud Service environment
contentOwner: khsingh
feature: Adaptive Forms
role: User, Developer
level: Intermediate
topic: Migration
exl-id: 090e77ff-62ec-40cb-8263-58720f3b7558
---
# Migrate to [!DNL AEM Forms] as a Cloud Service  {#Harden-your-AEM-Forms-as-a-Cloud-Service-environment}

You can migrate your Adaptive Forms, themes, templates, and cloud configurations from <!-- AEM 6.3 Forms--> AEM 6.4 Forms on OSGi and AEM 6.5 Forms on OSGi to [!DNL AEM] as a Cloud Service. Before migrating these assets, use the Migration Utility to convert the format used in the earlier versions to the format used in [!DNL AEM] as a Cloud Service. When you run Migration Utility, the following assets are updated:

* Custom components for Adaptive Forms
* Adaptive Forms templates and themes
* Cloud configurations
* Code editor scripts are converted to reusable functions and applied to visual rules.

## Considerations {#consideration}

* The service helps migrate content from only [!DNL AEM Forms] on OSGi environments. Migrating content from [!DNL AEM Forms] on JEE to a Cloud Service environment is not supported.

* (Only for AEM 6.3 Forms or a previous version environment upgraded to AEM 6.4 Forms or AEM 6.5 Forms) Adaptive Forms based on out-of-the-box templates and themes available in AEM 6.3 Forms or previous version are not supported on [!DNL AEM Forms] as a Cloud Service.

## Prerequisites {#prerequisites}

* [Enable Forms - Digital Enrollment](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/getting-started/setting-up-program.html?#editing-program) option on for your Forms Cloud Service program and [run the pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/deploying-code.html). 

    ![Dry Run Result](assets/enable-add-on.png)

* In a Cloud Service environment, the Migration Utility works in conjunction with the User Mapping Tool and Content Transfer Tool. The Migration Utility makes [!DNL AEM Forms] assets compatible with Cloud Service and the content transfer tool migrates the content from your [!DNL AEM Forms] environment to an [!DNL AEM] as a Cloud Service environment. Before using the Migration Utility, learn the process of [moving to AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/home.html). The process has two tools:
  * [User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#cloud-migration): The User Mapping Tool helps you map your users with corresponding Adobe IMS user accounts. 
  * [Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html?#cloud-migration): The Content Transfer Tool helps you prepare and transfer content from existing environment to a Cloud Service environment.
* Accounts with administrator privileges on [!DNL AEM Forms] as a Cloud Service and your local [!DNL AEM Forms] environment.
* Download and install Best Practice Analyzer, Content Transfer Tool, and [!DNL AEM Forms] Migration Utility from [Software Distribution Portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html)

* Run the [Best Practices Analyzer](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/best-practices-analyzer/overview-best-practices-analyzer.html?lang=en#cloud-migration) tool and fix the reported issue.

<!-- * Download the latest [compatibility package](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/forms-updates/aem-forms-releases.html?lang=en#aem-65-forms-releases) for your [!DNL AEM Forms] version. -->

## Migrate [!DNL AEM Forms] assets  {#use-the-migration-utility}

Perform the following steps to make your [!DNL AEM Forms] assets compatible with Cloud Service and transfer them to an [!DNL AEM] as a Cloud Service environment.

1. Create a [clone](https://experienceleaguecommunities.adobe.com/t5/adobe-experience-manager/correct-method-to-clone-the-aem-environment/qaq-p/363487) of your existing [!DNL AEM Forms] environment.

    Always use the cloned environment to run the Content Transfer Tool and the Migration Utility. Content Transfer Tool and Migration Utility make some changes to the content and assets. So, do not run the Content Transfer Tool and the Migration Utility on a production environment.

1. Log in to your cloned environment with administrative privileges.

1. Run the [User Mapping Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-user-mapping-tool.html?lang=en#cloud-migration) to map your users with corresponding Adobe IMS user accounts. You require Adobe IMS user accounts to login to a [!DNL AEM Forms] as a Cloud Service instance.

1. Download and install the [Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html?#cloud-migration) and [!DNL AEM Forms] as a Cloud Service Migration Utility from [Software Distribution Portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) on the cloned environment. You can use AEM Package Manager to install the tool and the utility.

1. Navigate to **[!UICONTROL Tools]** > **[!UICONTROL Operations]** > **[!UICONTROL Content Migration]**.

1. Open the **[!UICONTROL Prepare Forms for migration]** card. The browser displays five options:
    * **[!UICONTROL AEM Forms Assets Migration]**
    * **[!UICONTROL Adaptive Forms Custom Components Migration]**
    * **[!UICONTROL Adaptive Forms Templates Migration]**
    * **[!UICONTROL AEM Forms Cloud Configurations Migration]**
    * **[!UICONTROL Code Editor Script Migration]**

1. Use the option one-after another to make your [!DNL AEM Forms] assets compatible with [!DNL AEM] as a Cloud Service:

    1. Tap **[!UICONTROL AEM Forms Assets Migration]**, and in the next screen, tap **[!UICONTROL Start Migration]**. It makes Adaptive Forms and themes on your [!DNL AEM Forms] environment compatible with [!DNL AEM] as a Cloud Service .

    1. Tap **[!UICONTROL Adaptive Forms Custom Components Migration]** and in the Custom Components Migration page, tap **[!UICONTROL Start Migration]**. It makes any custom component developed for Adaptive Forms and component overlays on your [!DNL AEM Forms] environment compatible with [!DNL AEM] as a Cloud Service .

    1. Tap **[!UICONTROL Adaptive Forms Template Migration]** and in the Custom Components Migration page, tap **[!UICONTROL Start Migration]**. It makes Adaptive Form templates at /apps or /conf and created using AEM Template Editor compatible with [!DNL AEM] as a Cloud Service .

    1. Tap **[!UICONTROL AEM Forms Cloud Configurations Migration]** and then on the Configuration Migration page, tap **[!UICONTROL Start Migration]**. It updates and moves the following Cloud Services to a new location:

        * Form Data Model Cloud Service
        * Google reCAPTCHA Cloud Service
        * [!DNL Adobe Sign] Cloud Service
        * Adobe Fonts Cloud Service

    1. Tap **[!UICONTROL Code Editor Script Migration]**, specify a location to save reusable functions, and tap **[!UICONTROL Start Migration].

    The Cloud Service does not support rule editor scripts. The **[!UICONTROL Code editor script migration]** tool converts all rule scripts on your environment to reusable functions and applies the reusable functions to visual editor at appropriate location. These reusable functions are saved in the form of client libraries and help you keep existing functionality intact. The tool automatically applies the generated reusable functions to corresponding Adaptive Forms.

    Use the [Package Manager](https://experienceleague.adobe.com/docs/experience-manager-65/administering/contentmanagement/package-manager.html?lang=en#contentmanagement) to export the reusable functions (Client Libraries) to a package.

1. [Deploy](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/overview.html?lang=en#deploying-content-packages-via-cloud-manager-and-package-manager) the reusable functions (Client Libraries) package, [custom code, components, configurations](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/devops/deploy-code.html#cloud-manager), custom locale-specific libraries to your [!DNL AEM] as a Cloud Service environment.

    <!-- 1. Install the latest [Compatibility Package](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html?#cloud-migration) to your cloned [!DNL AEM Forms] environment. -->

1. Run the [Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/overview-content-transfer-tool.html?#cloud-migration). While specifying parameters on the **[!UICONTROL Create Migration Set]** screen, specify the path of Adaptive Forms, themes, templates, Form Data Models, Cloud Services, Custom Components and other AEM Forms-specific assets to the **[!UICONTROL Paths to be included]** option. It adds specified [!DNL AEM Forms] assets to migration set. 

## Paths of various AEM Forms-specific assets 

* **Adaptive Forms**: You can find adaptive forms at `/content/dam/formsanddocuments/`and /content/forms/af. For example, for an adaptive form titled WKND Registration add paths `/content/dam/formsanddocuments/wknd-registration` and `/content/forms/af/wknd-registration`. 
* **Form Data Mode**: You can find all the Form Data Models at `/content/dam/formsanddocuments-fdm`. For example, `/content/dam/formsanddocuments-fdm/ms-dynamics-fdm`.

* **Client libraries**: The default path of client libraries is `/etc/clientlibs/fd/theme`. 

* **Adaptive Form templates**: The default path of templates is `/conf/<template folder>`. For example, for a template titled basic add path `/conf/ReferenceEditableTemplates/settings/wcm/templates/basic`.

* **Adaptive Form themes and Client libraries**: The default path of themes is ` /content/dam/formsanddocuments-themes/` and default path of client libraries is `/etc/clientlibs/fd/theme`. For example, for a template titled WKND Theme add path ` /content/dam/formsanddocuments-themes/wkndtheme` and client libraries for the theme at `/etc/clientlibs/reference-themes/wkndtheme-3-0`. You can also have themes and client libraries at other custom paths.

* **Cloud Configurations**: You can find Cloud Configurations at `/conf/`. For example, Form Data Model cloud configuration is at `/conf/global/settings/cloudconfigs/fdm`.

* **Workflow Model**: You can find AEM Workflow Models at `/conf/global/settings/workflow/models/`. For example, for an workflow model titled WKND Registration add path `/conf/global/settings/workflow/models/wknd-registration`

You can add top level folder paths listed below or specific folder paths as described below. It enables you to migrate a certain assets and all the assets and forms at once.

* /content/dam/formsanddocuments-fdm
* /content/dam/formsanddocuments/themes
* /content/forms/af
* /etc/clientlibs/fd/theme

To migrate AEM Workflow models, specify the following paths:

* /conf/global/settings/workflow/models/
* /conf/global/settings/workflow/launcher
* /var/workflow/models
