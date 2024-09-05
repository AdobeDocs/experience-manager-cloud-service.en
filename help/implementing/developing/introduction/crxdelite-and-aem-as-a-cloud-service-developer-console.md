---
title: CRX/DE Lite and AEM as a Cloud Service Developer Console
description: Learn about CRX/DE Lite and AEM as a Cloud Service Developer Console
feature: Developing
role: Admin, Architect, Developer
---

# CRX/DE Lite and AEM as a Cloud Service Developer Console {#crxde-lite-and-developer-console}

## Local Development {#local-development}

For local development, Developers have full access to CRXDE Lite (`/crx/de`)  and the AEM Web Console (`/system/console`).

On local development (using the SDK), `/apps` and `/libs` can be written to directly, which is different from Cloud environments where those top level folders are immutable.

## AEM as a Cloud Service Development tools {#aem-as-a-cloud-service-development-tools}

>[!NOTE]
>The AEM as a Cloud Service Developer Console should not be confused with the similarly named [*Adobe Developer Console*](https://developer.adobe.com/developer-console/).
>

Customers can access CRXDE lite on the author tier's development environment but not stage or production. The immutable repository (`/libs`, `/apps`) cannot be written to at runtime so attempting to do so will result in errors.

Instead, the Repository Browser can be launched from the AEM as a Cloud Service Developer Console, providing a read-only view into the repository for all environments on author, publish, and preview tiers. For more information see the [Repository Browser](/help/implementing/developing/tools/repository-browser.md).

A set of tools for debugging AEM as a Cloud Service developer environments are available in the AEM as a Cloud Service Developer Console for RDE, dev, stage, and production environments. The url can be determined by adjusting the Author or Publish service urls as follows:

`https://dev-console/-<namespace>.<cluster>.dev.adobeaemcloud.com`

As a shortcut, the following Cloud Manager CLI command can be used to launch the AEM as a Cloud Service Developer Console based on an environment parameter described below:

`aio cloudmanager:open-developer-console <ENVIRONMENTID> --programId <PROGRAMID>`

See [Release Information](/help/release-notes/home.md) for more information.

Developers can generate status information, and resolve various resources.

As illustrated below, available statuses information include the state of bundles, components, OSGI configurations, oak indexes, OSGI services, and Sling jobs.

### OSGi Bundles {#osgi-bundles}

* This produces an overview of OSGI bundles that are deployed on the selected environment type. It enables a full-text search. 
* It's useful to get information of the actual state of bundles in the environment. You can get information such as exported packages, imported packages, used services and more. 
* Sometimes as developer you want to verify on the actual environment, if the bundle does what you expect it to do. 
* Example use-case: You specified a version range of a dependency in your bundle. Something is going wrong in the dependency. You wonder which version of the dependency is being wired into your bundle. To check this, you go to the bundle details, and use importing bundles / packages to check which bundle version / package version is being used at runtime to find out. With this information you can adjust your maven dependency version range or adapt your code.

### Java Packages {#java-packages}

* This gives you a search prompt you can use to search packages that are active in the environment's OSGI system. In here you can see which bundle exports (provides) the package, and you can see which bundle imports (uses) the package. Also you can check for duplicate packages (same package, different versions), which can cause problems in some cases. 
* Example use-case: A custom service is using the [dynamic class loader](https://sling.apache.org/apidocs/sling9/org/apache/sling/commons/classloader/DynamicClassLoaderManager.html) is loading a class without specifying a version, that is exported by multiple bundles with different versions, causing the implementation to be different and the behaviour to change. The developer wants to see which packages are in the environment without analysing the feature model, so he searches for this package and sees all the versions being exported. This gives him the information to enter a (better) version range. 

### Servlets {#servlets}

* This gives you a search prompt on which you can specify a path +selectors + extension with either GET or POST. It then gives servlets in order of preference which will handle the request in Sling.
* Example use case: You have OSGI servlet that should be activated on a request an print something to the response, but you an empty response back instead. You wonder if some other servlet is taking precedence over your servlet with more selectors direct resourceType, extensions, rank etc. So you enter the path you expect and search, and find out another servlet is active on the path with a higher rank. Now you can see if you can get your servlet above this one by for example adding selectors. 

### Services {#services}

* Similar to the OSGI Components view, but based on services. You can quickly search which services are provided with certain properties. 

### OSGi Components {#osgi-components}

* This produces an overview of OSGI components present in the selected environment type. It enables a full-text search. 
* You can get the live state of OSGI components in the environment. You can see which services it satisfies, the bundle providing it, activation (immediate or delayed) etc.
* Example use case: As developer, you want to verify if a component that is activated with a configuration, is active or not on a particular environment, because you are not getting the behaviour that you expect. You simply lookup the component in the search and check to see if the component is active or not.
* Another use case: You are interested to see which OOTB components are present on the environment, and which services they satisfy, to learn more about AEM in the cloud. You can check them out in the component list. 

### Integrations {#integrations}

* Gives admins the capability to generate, rename and delete service-credentials and developer tokens.

### Repository {#repository}

* Opens the Repository browser

### Status Dumps/Queries {#status-dumps-queries}

* Gives a full text / json dump of the current state of bundles, packages, configurations, services, components, sling jobs or oak definitions.
* This can be useful especially if the developer has discovered some unexpected state, and wants to communicate / document this for other developers. Downloading the dump gives you a snapshot of the state for later reference.

### Configurations {#configurations}

* This gives you a (searchable) list of configurations that are active on the environment. You can see which properties are provided by the configurations by checking out the detail page.
* Example use case: A developer wants to make sure that the configurations he specified are actually present on the environment. If the configuration is lacking, he / she can check the feature model and / or the configuration runmode / folder.

For Production programs, access to the AEM as a Cloud Service Developer Console is defined by the "Cloud Manager - Developer Role" in the Adobe Admin Console, while for sandbox programs, the AEM as a Cloud Service Developer Console is available to any user with a product profile giving them access to AEM as a Cloud Service. For all programs, "Cloud Manager - Developer Role" is needed for status dumps and the repository browser and users must also be defined in the AEM Users or AEM Administrators Product Profile on both author and publish services to view data from both services. For more information about setting up user permissions, see [Cloud Manager Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/requirements/setting-up-users-and-roles.html).

## Performance Monitoring {#performance-monitoring}

Adobe monitors application performance and takes measures to address if deterioration is observed. At this time, application metricscannot be obeserved.