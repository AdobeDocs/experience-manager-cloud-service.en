---
title: What are the differences between AEM 6.5 Forms and AEM Cloud Services?
description: Compare AEM 6.5 Forms and AEM Cloud Services and learn the most prominent changes before upgrading or migrating to Cloud Service.  
exl-id: 46fcc1b4-8fd5-40e1-b0fc-d2bc9df3802e
role: Admin, Developer, User
feature: Adaptive Forms
contentOwner: khsingh
---
# Difference between AEM 6.5 Forms (AMS and on-Prem) and AEM Forms as a Cloud Services (AEM CS Forms) {#notable-changes-for-existing-AEM-Forms-users}

Adobe Experience Manager Forms as a Cloud Service brings some notable changes to existing features in comparison to Adobe Experience Manager Forms On-Premise and [!DNL Adobe-Managed Service] environments. The key differences are listed below:

## Cloud native capabilities

* The service has a Cloud-native architecture that allows auto-scaling based on load, Zero downtime for upgrades, frequent and after roll-out of new features and updates, and topologies optimized for maximum resilience and efficiency. 

*   The service includes no submit actions that store data to Adobe Experience Manager Cloud Service instances, making it super secure. Data captured via forms is sent directly to configured data stores.

* A free CDN (content delivery network) is also included to help you deliver and render forms at a faster pace. 


## Updates to development flow 

* The service provides an SDK to develop and test custom code in a local environment (local machine) before deploying the code to a Cloud Service. Developers develop and test custom components, themes, workflows applications, configurations, templates, and more using the SDK on their local machines. After testing the custom code in their local development environment, they deploy the custom code to a [Forms CS environment development or stage environment](/help/implementing/cloud-manager/deploy-code.md) for further testing before promoting it to a production environment. 

* Developers maintain code for Cloud Service and local development environment in a common [git repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/managing-code/cloud-manager-repositories.html). A git repository, based on AEM Archetype, is auto created on creation of an AEM as a Cloud Service program. 

    ![auto creation of git repository on AEM as a cloud service program](/help/forms/assets/git-repo-local-and-forms-cs.png)

* Development flow for Forms as a Cloud Service aligns with AEM Archetype for AEM Cloud Service. However, there are some changes required to Adobe Experience Manager Maven projects to be compatible with AEM Cloud Service. At a high-level, AEM requires a separation of content and code into discrete subpackages to respect the split between mutable and immutable content. Use the [Repository Modernizer tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/refactoring-tools/repo-modernizer.html) to restructure existing project packages by separating content and code into discrete packages to be compatible with the project structure defined for Adobe Experience Manager as a Cloud Service.

* Before using your customer bundles with Forms as a Cloud Service, recompile your custom code with the latest version of adobe-aemfd-docmanager.

*   Use [AEM Forms as a Cloud Service migration utility](/help/forms/migrate-to-forms-as-a-cloud-service.md) to prepare and migrate your Adaptive Forms, themes, templates, and cloud configurations from <!-- AEM 6.3 Forms--> AEM 6.4 Forms on OSGi and AEM 6.5 Forms on OSGi to [!DNL AEM] as a Cloud Service. Use the [Git repository of your program](/help/implementing/cloud-manager/managing-code/managing-repo.md) to import existing Adaptive Form templates.

*   Email supports only HTTP and HTTPs protocols, by default. [Contact the support team](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html#sending-email) to enable ports to send emails and  enable SMTP protocol for your environment.

## Localization

*   The URL convention of localized Adaptive Forms now supports specifying a locale in the URL. The new URL convention enables caching localized forms on a Dispatcher or CDN. On a Cloud Service environment, use the URL format `http://host:port/content/forms/af/<afName>.<locale>.html` to request a localized version of an Adaptive Form instead of `http://host:port/content/forms/af/afName.html?afAcceptLang=<locale>`. 

*   Adobe recommends using Dispatcher or CDN caching. It helps improve the rendering speed of prefilled forms. 


## Adaptive Forms

* **Rule editor:** AEM Forms as a Cloud Service provides a hardened [Rule editor](rule-editor.md#visual-rule-editor). The code editor is not available on Forms as a Cloud Service. 

    The [migration utility](/help/forms/migrate-to-forms-as-a-cloud-service.md) helps you migrate your forms that have custom rules (created in the code editor). The utility converts such rules into custom functions supported on Forms as a Cloud Service. You can use the reusable functions with Rule editor to continue obtaining results obtained with rule scripts. The `onSubmitError` or `onSubmitSuccess` functions are now available as actions in the Rule Editor.  

<!--* **Prefill Service:** By default, the prefill service merges data with an Adaptive Form at client as opposed to merging data on Server in AEM 6.5 Forms. The feature helps improve the time required to prefill an Adaptive Form. You can always configure to run the merge action on the Adobe Experience Manager Forms Server.-->

* **Prefill Service:** Prefill service fetches data from the server and merges to prefill your Adaptive Forms on the client side. This feature helps improve the time required to fill an Adaptive Form. You can always configure the [prefill service](https://experienceleague.adobe.com/docs/experience-manager-learn/forms/adaptive-forms/prefill-service-adaptive-forms-article-use.html) to run the merge action on the Adobe Experience Manager Forms Server.

*   **Submit actions:** The **Email** submit action provide options to send attachments and attach Document of Record (DoR) with email. You can use it in place of the **Email as PDF** action available in AEM 6.5 Forms.

*   **Automated Forms Conversion Service**: The service does not provide a meta-model for Automated Forms Conversion Service. You can [download it from the Automated Forms Conversion Service documentation](https://experienceleague.adobe.com/docs/aem-forms-automated-conversion-service/using/extending-the-default-meta-model.html?lang=en#default-meta-model).

*   **XSD-Based Adaptive Forms:** You can use XDP-template to design a template for Document for Record. The service does not support XFA-based Adaptive Forms 

* **Components**:  The service does not support in-form signing experience and does not include the Summary and Verify components for Adaptive Form.

* **Wizard interface:** You can use the [Wizard interface](/help/forms/creating-adaptive-form-core-components.md) to quickly configure the common options and eaily create an Adaptive Form.  

## Forms Portal

* The service does not retain metadata for drafts and submitted Adaptive Forms.

## Document Services: 

Forms as a Cloud Service provide Document Generation and Document Manipulation RESTful APIs. You can use these APIs to generate or manipulate docs on demand or in batches, as required:

* **Document Services: Document Generation APIs (Output Service)**: In a single API call or batch, you can use only one template with multiple DATA XML files. Using multiple templates with multiple data files in a single API call is not supported.

* **Document Manipulation APIs (Assembler Service)**:  

    *   The operations that rely on document services or applications are not available. For example, Microsoft&reg; Word to PDF, Microsoft&reg; Excel to PDF, and HTML to PDF, PostScript (PS) to PDF, XDP to PDF Forms are not supported. These operations rely on Microsoft&reg; Office, Adobe Acrobat, Adobe Distiller, Forms Document Service respectively.   
    
    *   Convert documents that are in a non-PDF format into a PDF format before using those with Communications Document Manipulation APIs. For example, if your documents are in Microsoft&reg; Office, HTML, PostScript (PS), XDP format, convert these documents to PDF format before using those with PDF documents. You can use the [ConvertPDF](https://experienceleague.adobe.com/docs/experience-manager-65/forms/use-document-services/using-convertpdf-service.html) service for such conversions. 

    * You can use an AEM 6.5 Forms environment for Digital Signature, Encryption, Reader Extension, Send to printer, Convert PDF, and Barcoded Forms service.


## Data integration (Form Data Model)

*   The service also provides support for JDBC connector, Microsoft&reg; Dynamics, SalesForce, SOAP-based web services, and services that support OData.

* You can also connect AEM user profile to retrieve and update user information.

* Forms data model supports only HTTP and HTTPS endpoints to submit data. The service does not support Mutual SSL for REST connector and x509 certificate-based authentication for SOAP data sources.

* Forms as a Cloud Service allows to use Microsoft&reg; Azure Blob, Microsoft&reg; Sharepoint, Microsoft&reg; OneDrive, and services supporting general CRUD (Create, Read, Update, and Delete) operations as data stores, both Open API specification 2.0 and Open API 3.0 specification are supported.


## E-Sign

* The service provides an OOTB integration with Adobe Sign and supports DocuSign for e-signatures. 

* The service also supports Adobe Sign roles. You can configure the roles in the Adaptive Forms editor for business users to easily configure signing workflows.


## HTML5 Forms

* You can use an AEM 6.5 Forms environment to:

    * render your XDP-based forms as HTML5 Forms. The service does not support HTML5 Forms.

    *   capture data offline and sync it the next time you return online with the [AEM Forms Workspace](https://experienceleague.adobe.com/docs/experience-manager-65/forms/use-aem-forms-workspace/introduction-html-workspace.html) app. 

## Interactive Communications

* You can use Communications APIs to produce personalized documents on-demand or in batches on Forms as a Cloud Service. You can use an AEM 6.5 Forms environment for Interactive Communications and Agent UI use-cases.

## See Also

* [Migrate from an AEM Forms (On-Premise and AMS environments) to AEM Forms as a Cloud Service](/help/forms/migrate-to-forms-as-a-cloud-service.md)
* [Add or create Adaptive Forms to AEM Sites Page](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md)
* [Create an Adaptive Form (Core Components)](/help/forms/creating-adaptive-form-core-components.md)
* [Introduction to AEM Forms as a Cloud Service](/help/forms/home.md)
* [Set up a local development environment and initial development project](/help/forms/setup-local-development-environment.md)


<!--

## Additional Information

* [Introduction to AEM Forms as a Cloud Service](/help/forms/home.md)
* [Set up a local development environment and initial development project](/help/forms/setup-local-development-environment.md)

-->
