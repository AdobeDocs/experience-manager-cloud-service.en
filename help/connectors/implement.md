---
title: Implementing an AEM Connector
description: Learn about Connectors, what they can do, and how to implement these valuable tools in Experience Manager.
exl-id: 70024424-8c52-493e-bbc9-03d238b8a5f5
feature: Operations
role: Admin
---

Implementing an AEM Connector
=============================

Provided below are useful references for building AEM Connectors and should be read with guidance on [submitting](submit.md) and [maintaining](maintain.md) connectors.

A Developer license for AEM can be obtained through the [Adobe Exchange Program](https://partners.adobe.com/technologyprogram/experiencecloud.html).

Common Integration Patterns
---------------------------

AEM is a cutting-edge web experience management solution and offers many potential areas of integrations. Common integration patterns include:

* Pulling data from an external system into AEM. For example, exporting contact information from a CRM to make it available to a wider audience visiting an AEM-powered website.  Implementations should use Sling's [Scheduled Jobs](https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html#scheduled-jobs), which guarantees that the job is executed even if containers go down. Code should be designed to assume that the job can potentially be triggered more than once. 
* Exporting data from AEM into an external system. For example, newsletter subscription settings are submitted on an AEM-powered website to a CRM.
* Retrieving assets from AEM. For example, an external Content Management System (CMS) referencing an asset stored in AEM Assets. Or as another example, a PIM system linking to an image in AEM Assets.
* Storing assets in the AEM infrastructure. For example, a Marketing Resource Management (MRM) system storing an approved asset in AEM Assets.
* Configuring and rendering a custom UI component. For example, allow an author to drag and drop a video component and configure a specific video to play on the live site. 
* Acting on an asset with a partner service. For example, sending an asset to a video platform when a page is published.
* Analyzing a site, page, or asset in the AEM Admin Console. For example, making SEO recommendations for an existing or unpublished page.
* Page-level access to user data maintained by an external service. For example, use demographic information to personalize the site experience. Read about ContextHub, a framework for storing, manipulating, and presenting context data. 
* Translating site copy or asset metadata. See the [AEM Translation Framework Bootstrap Connector](https://github.com/Adobe-Marketing-Cloud/aem-translation-framework-bootstrap-connector) for sample code using the AEM Translation Framework, which is the preferred implementation of translation connectors.


Useful Documentation
--------------------

Experience Manager as a Cloud Service [documentation](../overview/introduction.md) provides valuable insights into developing in AEM. Below are some specific technical topics and references that you may find useful while implementing an AEM connector:

* Adobe Consulting Services (ACS) [AEM Samples](https://adobe-consulting-services.github.io/acs-aem-samples/) for well-commented code to help educate AEM developers
* The various documentation links in the Common Integration Patterns section of this article

Community Resources 
--------------------

In addition to the static documentation above, Adobe and the AEM community offer resources to help bring a connector to market:

* The Adobe Community's [AEM Forum](https://help-forums.adobe.com/content/adobeforums/en/experience-manager-forum/adobe-experience-manager.html) is an active site where your peers ask and respond to questions
* Additional Adobe technical resources are available to certain partner levels. Learn more about the [Adobe Exchange Program](https://partners.adobe.com/technologyprogram/experiencecloud.html).
* If your organization would like implementation help, consider Adobe's [Professional Services](https://solutionpartners.adobe.com/s/directory) team or see the [Solution Partner Finder](https://solutionpartners.adobe.com/s/directory/) for a list of Adobe's partners across the globe

Package structure rules
-----------------------

To facilitate rolling deployments, AEM as a Cloud Service packages&mdash;such as connectors&mdash;maintain a strict division between "immutable" and "mutable" content. Packages should be clearly organized to include:

* `/apps`
* `/content` and `/conf`

Connectors should adhere to these packaging guidelines, which are described under [AEM Project Structure](/help/implementing/developing/introduction/aem-project-content-package-structure.md). Existing connectors should be refactored to conform, as well.

In addition, only Adobe should write code into `/libs`, with customers and partners writing into `/apps`.

Existing connectors may also need to be refactored to move any configuration that might once have been placed `/etc` into other top level folders such as `/conf`. This restructuring was done as part of AEM 6.5 and is described in the [AEM 6.5 documentation](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/implementing/deploying/restructuring/repository-restructuring).

Adobe recommends placing most of the connector code under `/apps/connectors/<vendor>` to maintain a clean repository structure, especially for customers using multiple connectors.

Cloud Services Configurations
-----------------------------

One aspect of the connector implementation is the code backing the configuration of the connector. This code causes a card with the connector's name to appear under Tools > Operations > Cloud Services. When clicked, a [configuration browser](/help/implementing/developing/introduction/configurations.md#using-configuration-browser) pops up where the customer selects the parent folder to contain the connector configuration. The connector's code should result in a form with all the properties that must be configured, ultimately storing the values in a configuration folder under `/conf`. This folder can later be selected under the Sites properties tab or the Assets properties tab.


Context-Aware Configurations
-----------------------------

[Context-Aware Configurations](https://sling.apache.org/documentation/bundles/context-aware-configuration/context-aware-configuration.html) let you layer configuration across different folders, including `/libs`, `/apps`, `/conf` and subfolders under `/conf`. It supports inheritance so a customer can configure global configuration while making specific changes for each microsite. Because it is possible to use this feature for Cloud Services Configurations, connector code should reference configuration using the Context-Aware Configuration API instead of referencing a specific configuration node.

If modified configurations are used in the Connector, architect the Connector to handle including/merging any future updates to Connector-provided default configurations with any customer configurations. Keep in mind that modifying customer-customized content or configurations without prior notice and consent can disrupt or cause unexpected behavior in their Connector.

Coding Best Practices
----------------------

Because AEM as a Cloud Service is a Cloud-native solution, there are some guidelines that may impact a connector's code strategies. See [AEM as a Cloud Service Development Guidelines](/help/implementing/developing/introduction/development-guidelines.md) for more details.

Testing the AEM Connector
-------------------------

New connectors should be created (or existing connectors modified) using local environment development techniques. The Partner Team provides ISV partners with a sandbox environment where they can deploy their AEM Connector to a vanilla application to ensure that it works.
