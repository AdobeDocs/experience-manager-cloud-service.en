---
title: What has changed between AEM 6.5 Forms and AEM Cloud Services
description: Are you an Experience Manager Forms user and looking to upgrade to Adobe Experience Manager Forms as a Cloud Service? Learn the most prominent changes before upgrading or migrating to Cloud Service.  
contentOwner: khsingh
exl-id: 46fcc1b4-8fd5-40e1-b0fc-d2bc9df3802e
---
# Notable changes for existing Adobe Experience Manager Forms users  {#notable-changes-for-existing-AEM-Forms-users}

Adobe Experience Manager Forms as a Cloud Service brings some notable changes to existing features in comparison to Adobe Experience Manager FormsOn-Premise and [!DNL Adobe-Managed Service] environments. The key differences are listed below:

* The service provides a local and a cloud-native development environment. You can use a [local development environment](setup-local-development-environment.md) to develop and test your custom code, components, templates, themes, Adaptive Forms, other assets before deploying these assets to a cloud environment. It helps speed up the development process.
* [!DNL AEM] as Cloud Service is shipped with a built-in CDN. Its main purpose is to reduce latency by delivering cacheable content from the CDN nodes at the edge, near the browser. It is fully managed and configured for optimal performance of AEM applications.
* A cloud-native environment does not have web console (configuration manager). You can use [[!DNL AEM Forms] as a Cloud Service SDK to generate configurations](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/configuring-osgi.html?lang=en#generating-osgi-configurations-using-the-aem-sdk-quickstart) and CI/CD pipeline to [deploy the configuration](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/deploy-code.html?lang=en#deployment-process) to your Cloud Service instance.

* URL convention of localized Adaptive Forms now supports specifying a locale in the URL. New URL convention enables caching localized forms on a Dispatcher or CDN. On Cloud Service environment, use the URL format `http://host:port/content/forms/af/<afName>.<locale>.html` to request a localized version of an Adaptive Form instead of `http://host:port/content/forms/af/afName.html?afAcceptLang=<locale>`. Adobe recommends using Dispatcher or CDN caching. It helps improve rendering speed of prefilled forms.
* Prefill service merges data with an Adaptive Form on a client. It helps improve the time required to prefill an Adaptive Form. You can always configure to run the merge action on the Adobe Experience Manager FormsServer.
* Email support only HTTP and HTTPs protocols, by default. [Contact the support team](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/development-guidelines.html#sending-email) to enable ports for sending emails and to enable SMTP protocol for your environment.
* Adobe Experience Manager Forms as a Cloud Service brings many new features and possibilities into your AEM Projects. However, there are some changes required to Adobe Experience Manager Maven projects to be compatible with AEM Cloud Service. At a high-level, AEM requires a separation of content and code into discrete subpackages to respect the split between mutable and immutable content. Use the [Repository Modernizer](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/refactoring-tools/repo-modernizer.html) tool to restructure existing project packages by separating content and code into discrete packages to be compatible with the project structure defined for Adobe Experience Manager as a Cloud Service.

<!--  If your Cloud Configuration contains a secret (password), create a separate Cloud Configuration for every Author instance (Developer, Stage, and Production). If a Cloud Configuration is also required on Publish instances, publish/replicate a separate Cloud Configuration for every Publish instance (Developer, Stage, and Production). 

* When you create a Cloud Configuration that contains a secret, each Cloud Service instance (Developer, Stage, and Production) uses its own encryption key to encrypt the password before storing it. So, manually create such Cloud Configuration for every Cloud Service instance (Developer, Stage, and Production). Also, do not store secrets used in a Cloud Configuration to your Cloud Manager Git repository.

* Use [!DNL Cloud Manager] [APIs to convert and provide your passwords as secrets](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/configuring-osgi.html?lang=en#setting-values-via-api). Do not store plain text password or secrets on your environments. -->

* Use of environment-specific configurations for secret OSGi configuration values, such as passwords, private API keys, or any other values. These cannot be store into in Git for security reasons. [Use secret environment-specific configurations to store the value for secrets on all Adobe Experience Manager as a Cloud Service environments, including Stage and Production](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/configuring-osgi.html?lang=en#when-to-use-secret-environment-specific-configuration-values).

For a comprehensive list of changes in Adobe Experience Manager as a Cloud Service, See [What is New and What is Different](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/overview/what-is-new-and-different.html).

<!-- ## Feature comparison {#comparison}

[!DNL AEM Forms] as a Cloud Service and Experience Manager 6.5 Forms share a common set of features: Adaptive Forms, data integration, integration with [!DNL Adobe Sign], themes, templates, and forms management interface are identical. You can easily port your existing Adaptive Forms from an Experience Manager 6.5 Forms or an earlier version to [!DNL AEM Forms] as a Cloud Service.

### Features of AEM 6.5 Forms and [!DNL AEM Forms] as a Cloud Service {#feature-comparison}

The following table lists the major features of Experience Manager 6.5 Forms and provides information about whether the feature is partially or fully supported in [!DNL AEM Forms] as a Cloud Service, with a link to more information about the feature. The table also lists extra features available in [!DNL AEM Forms] as a Cloud Service.


| Feature/Capability | AEM 6.5 Forms | [!DNL AEM Forms] as a Cloud Service |
| - | - | - |
| Adaptive Forms | &#x2611; | &#x2611; |
| Data Integration | &#x2611; | &#x2611;(With some changes) |
| Automated Forms Conversion Service | &#x2611; | &#x2611; |
| Integration with Adobe Sign | &#x2611; | &#x2611;(With some changes) |
| Themes and Templates | &#x2611; | &#x2611; ([With some changes](themes.md#difference-in-themes))|
| Rule editor | &#x2611; | &#x2611; (With some changes) |
| Forms Portal | &#x2611; | --- |
| Integration with Adobe Analytics | &#x2611; | &#x2612; |
| Document Security | &#x2611; | &#x2612; | -->

<!-- ## New features {#comparison} -->



## Key enhancements {#whats-new}

<!-- [!DNL AEM Forms] as a Cloud Service offers benefits like auto-scaling, cost-effectiveness, zero downtime for upgrades, and cloud-native development environment and more. The list does not stop here. The following features are are start and are available only for [!DNL AEM Forms] as a Cloud Service: -->

The following features and enhancements are available only on [!DNL AEM Forms] as a Cloud Service: 

**Enhanced Visual Rule editor**
The service provides a hardened [Visual Rule editor](rule-editor.md#visual-rule-editor). The service has added following features to Visual rule editor to help you write capable rules:

* [New submission events](working-with-adobe-sign.md#available-operator-types-and-events-in-rule-editor): `Navigation`, `Step Completion`, `Successful Submission`, and `Error`

* [New data type `scope`](rule-editor.md#custom-functions). You can use the `scope` data type in a custom function to pass the entire scope of a form.

* Ability to use [@this to specify a JSDoc in a custom function](rule-editor.md#custom-functions). It allows invoking a custom function by using @this in an active component.

* Ability to add conditions for property-based rules.

**Core Components**
The [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html?lang=en) are a set of standardized Web Content Management (WCM) components for AEM to speed up development time and reduce maintenance cost. [!DNL AEM Forms] as a Cloud Service supports **[!UICONTROL AEM Forms Container]** Core Component. You can use the component to embed an Adaptive Form to an AEM Sites page.  

**AEM Archetype for Forms as a Cloud Service**
[AEM Archetype](https://github.com/adobe/aem-project-archetype/releases/tag/aem-project-archetype-27) helps you start developing for [!DNL AEM Forms] as a Cloud Service. You can use Archetype version 27 or later to create a project template compatible with [!DNL AEM Forms] as a Cloud Service environment. The Archetype also includes some sample themes and templates to help you started quickly.

**Secure and improved information flow between forms and Sign**
[Adaptive Forms and Adobe Sign integration](working-with-adobe-sign.md) on Cloud Service offer simultaneous submission of data and signing activity. It makes form submission independent of signing status paving a way for faster submissions. On top of it, the service does not save any data on Cloud Service instances making the signing process super secure.

**Best Practices Analyzer and migration tooling**
Best Practices Analyzer provides an assessment of your current AEM implementation. Run the tool before [migrating to Forms as a Cloud Service](migrate-to-forms-as-a-cloud-service.md). It  assesses readiness to move from an existing Adobe Experience Manager (AEM) deployment to AEM as a Cloud Service.

The service also provides an [improved migration experience](migrate-to-forms-as-a-cloud-service.md) to help you easily migrate from [!DNL AEM 6.4 Forms] and [!DNL AEM 6.5 Forms] to [!DNL AEM Forms] as a Cloud Service.

**Faster form renditions and Faster server-side validations**
The service uses CDN and Dispatcher caching to deliver faster renditions and server-side validations for Adaptive Forms.

**Improved CAPTCHA**
You can now [validate CAPTCHA](captcha-adaptive-forms.md) either on Adaptive Form submission or on a business logic. You can also add conditions to validate CAPTCHA on a user action and show or hide the CAPTCHA component in an Adaptive Form based on rules. 

The CAPTCHA component provides an out-of-the-box integration with Google reCAPTCHA. You can also configure more CAPTCHA services for the component, if necessary.

**Multiple master pages for Document of Record**
You can now use a different master page for each page of a Document of Record and control placement of an Adaptive Form panel on a Document of Record with pagination options.

**Add columns to headless tables**
You can add and delete columns to tables without headers. Hidden headers are added to such tables to help you add and delete columns. These headers are visible during authoring but remain hidden in the published form. Tables without headers are mostly found in Adaptive Forms created using the Automated Forms Conversion Service.

**Improved Submit Actions**
You can use the [Send Email](configuring-submit-actions.md#send-email#send-email) Submit Action to send a Document of Record (DoR) PDF as an attachment.

**Group email for workflow**
You can choose to [send notification emails](aem-forms-workflow-step-reference.md#assign-task-step) from the Assign Task step to a single person or a group.

**Enhanced Invoke Form Data Model step**
You can now specify path of folder for the Relative to Payload option of input service arguments in an Invoke Form Data Model step. It helps you map a file present in the specified folder to the service argument without specifying the exact filename.

**Improved readability of translation files**
On Forms as a Cloud Service, reading order of the fields and panels of an Adaptive Form and message keys of corresponding translation files (.XLIFF files) has similar structure. It helps improving manual translation speeds. 

<!-- ## Feature comparison {#feature-comparison}

[!DNL AEM Forms] as a Cloud Service and [!DNL AEM 6.5 Forms] share some features like Adaptive Forms, Data Integration, and Forms Portal. You can easily port your existing Adaptive Forms from an [!DNL AEM 6.5 Forms] or an earlier version to [!DNL AEM Forms] as a Cloud Service.

### Features of [!DNL AEM 6.5 Forms] and [!DNL AEM Forms] as a Cloud Service {#aem-6.5-vs-aem-forms-as-a-cloud-service}

The following table lists the major features of [!DNL AEM 6.5 Forms] and provides information about the features coming soon to [!DNL AEM Forms] as a Cloud Service:

| Feature/Capability | AEM 6.5 Forms  | [!DNL AEM Forms] as a Cloud Service |
|---|---|---|
| Cloud-native architecture | &#x2612; | &#x2611;  |
| Auto-scaling based on load | &#x2612; | &#x2611;  |
| Zero downtime for upgrades | &#x2612; | &#x2611;  |
| Feature roll-out frequency | Quarterly | Agile*  |
| CDN (content delivery network) included | &#x2612; | &#x2611;  |
| Topologies optimized for maximum resilience and efficiency | &#x2612; | &#x2611;  |
| Cloud-native development environment | &#x2612; | &#x2611;  |
| Self-Service via Cloud Manager | &#x2612; | &#x2611;  |
| Automated upgrades with Continuous Integration and Continuous Delivery (CI/CD)| &#x2611; | &#x2611;  |
| Adaptive Forms | &#x2611; | &#x2611; |
| Data Integration | &#x2611; | &#x2611; |
| Automated Forms Conversion Service | &#x2611; | &#x2611; |
| Integration with [!DNL Adobe Sign] | &#x2611; | &#x2611; |
| Integration with [!DNL AEM Sites] | &#x2611; | &#x2611; |
| Enhanced Visual Rule editor | &#x2612; | &#x2611; |
| Forms Portal | &#x2611; | Coming Soon |
| Integration with [!DNL Adobe Analytics] | &#x2611; | Coming Soon |
| Integration with [!DNL Adobe Target] | &#x2611; | Coming Soon |
| Document Security | &#x2611; | &#x2612; |

`*` New features every month and bug fix updates on daily basis.

For a comprehensive list of changes in AEM as a Cloud Service, See [What is New and What is Different](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/overview/what-is-new-and-different.html) and [Notable changes in [!DNL AEM Forms] as a Cloud Service](notable-changes.md) -->
