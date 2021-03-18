---
title: Implementing an AEM Connector
description: Implementing an AEM Connector
---

Implementing an AEM Connector
=============================

Provided below are useful references for building [AEM Connectors](https://www.adobe.io/apis/experiencecloud/aem/aemconnectors.html) and should be read in conjunction with guidance on [submitting](submit.md) and [maintaining](maintain.md) connectors.

Note that a Developer license for AEM can be obtained through the [Adobe Exchange Program](https://partners.adobe.com/exchangeprogram/experiencecloud).

Common Integration Patterns
---------------------------

AEM is a cutting-edge web experience management solution and offers many potential areas of integrations. Common integration patterns include:

*   Pulling data from an external system into AEM. For example, exporting contact information from a CRM to make it available to a wider audience visiting an AEM-powered website.  Implementations should use Sling's [Scheduled Jobs](https://sling.apache.org/documentation/bundles/apache-sling-eventing-and-job-handling.html#scheduled-jobs), which guarantees that the job is executed even if containers go down. Code should be designed to assume that the job can potentially be triggered more than once. 
*   Exporting data from AEM into an external system. For example, newsletter subscription settings submitted on an AEM-powered website to a CRM.
*   Retrieving assets from AEM. For example, an external Content Management System (CMS) referencing an asset stored in AEM Assets. Or as another example,  a PIM system linking to an image in AEM Assets.
*   Storing assets in the AEM infrastructure. For example, a Marketing Resource Management (MRM) system storing an approved asset in AEM Assets.
*   Configuring and rendering a custom UI component. For example, allow an author to drag and drop a video component and configure a specific video to play on the live site. 
*   Acting on an asset with a partner service. For example, sending an asset to a video platform when a page is published.
*   Analyzing a site, page, or asset in the AEM admin console. For example, making SEO recommendations for an existing or unpublished page.
*   Page-level access to user data maintained by an external service. For example, leverage demographic information to personalize the site experience. Read about ContextHub, a framework for storing, manipulating, and presenting context data. 
*   Translating site copy or asset metadata. See the [AEM Translation Framework Bootstrap Connector](https://github.com/Adobe-Marketing-Cloud/aem-translation-framework-bootstrap-connector) for sample code using the AEM Translation Framework, which is the preferred implementation of translation connectors.


Useful Documentation
--------------------

Experience Manager as a Cloud Service [documentation](../overview/introduction.md) provides valuable insights into developing in AEM. Below are some specific technical topics and references that you may find useful while implementing an AEM connector:

*   Adobe Consulting Services (ACS) [AEM Samples](http://adobe-consulting-services.github.io/acs-aem-samples/) for well-commented code to help educate AEM developers
*   The various documentation links in the Common Integration Patterns section of this article

Community Resources 
--------------------

In addition to the static documentation above, Adobe and the AEM community offer resources to help bring a connector to market:

*   The Adobe Community's [AEM Forum](http://help-forums.adobe.com/content/adobeforums/en/experience-manager-forum/adobe-experience-manager.html) is an active site where your peers ask and respond to questions
*   Additional Adobe technical resources are available to certain partner levels. Learn more about the [Adobe Exchange Program](https://partners.adobe.com/exchangeprogram/experiencecloud).
*   If your organization would like implementation help, consider Adobe's [Professional Services](http://www.adobe.com/marketing-cloud/service-support/professional-consulting-training.html) team or see the [Solution Partner Finder](https://solutionpartners.adobe.com/home/partnerFinder.html) for a list of Adobe's partners across the globe

Package structure rules
-----------------------

In order to support rolling deployments, AEM as a Cloud Service packages, of which connectors are examples, have a strict separation between "immutable" and "mutable" content. Packages should be cleanly separated between those that include:

*   `/apps`
*   `/content` and `/conf`

Connectors should adhere to these packaging guidelines, which are described in [this article](/help/implementing/developing/introduction/aem-project-content-package-structure.md). Existing connectors should be refactored to conform, as well.

In addition, only Adobe should write code into `/libs`, with customers and partners writing into `/apps`.

Existing connectors may also need to be refactored to move any configuration that might once have been placed `/etc` into other top level folders such as `/conf`. This restructuring was done as part of AEM 6.5 and is described in the [AEM 6.5 documentation](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/restructuring/repository-restructuring.html).

It's recommended that the majority of connector code is placed under `/apps/connectors/<vendor>` to promote a clean repository structure for customers who have several connectors.

Cloud Services Configurations
-----------------------------

One aspect of the connector implementation is code backing the configuration of the connector. This code causes a card with the connector's name to appear under Tools > Operations > Cloud Services. When clicked, a [configuration browser](/help/implementing/developing/introduction/configurations.md#using-configuration-browser) pops up where the customer selects the parent folder to contain the connector configuration. The connector's code should result in a form with all the properties that must be configured, ultimately storing the values in a configuration folder under `/conf`. This folder can later be selected under the Sites properties tab or the Assets properties tab.


Context-Aware Configurations
-----------------------------

[Context-Aware Configurations](https://sling.apache.org/documentation/bundles/context-aware-configuration/context-aware-configuration.html) allows to layer configuration across different folders, including `/libs`, `/apps`, `/conf` and subfolders under `/conf`. It supports inheritance so a customer can configure global configuration while making specific changes for each microsite. Because it is possible to leverage this feature for Cloud Services Configurations, connector code should reference configuration using Context-Aware Configuration API instead of referencing a specific configuration node.

If modified configurations are used in the Connector, architect the Connector to handle including/merging any future updates to Connector-provided default configurations with any customer configurations. Remember that changing customized (as in changed by the customer) content or configuration without customer warning and consent may break (or create unexpected behavior) with their Connector. 

Coding Best Practices
----------------------

Since AEM as a Cloud Service is a Cloud-native solution, there are some guidelines which may impact a connector's code strategies. See [AEM as a Cloud Service Development Guidelines](/help/implementing/developing/introduction/development-guidelines.md) for more details.

Testing the AEM Connector
-------------------------

New connectors should be created (or existing connectors modified) using local environment development techniques. The Partner Team will provide ISV partners with a sandbox environment where they can deploy their AEM Connector to a vanilla application to ensure that it works. 
