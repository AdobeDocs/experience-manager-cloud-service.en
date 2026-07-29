---
title: AEM as a Cloud Service Developer Console - Beta
description: Learn about the AEM as a Cloud Service Developer Console and its set of read-only tools for debugging cloud environments.
feature: Developing
role: Admin, Developer
exl-id: 4b0fc3e9-b7c4-4c95-bd97-8b24e4d5cb3d
---

# AEM as a Cloud Service Developer Console (Beta) {#developer-console}

The AEM as a Cloud Service Developer Console includes a set of read-only tools for debugging cloud environments. It can be accessed through a per-environment link in Cloud Manager and offers features to view bundles, OSGi settings, services and servlets, and more.

>[!NOTE]
>
>This article describes a revamped experience for the AEM Cloud Service Developer Console, which is now in beta.
>
>* A limited set of users can access the new console via a button at the top of the current Developer Console.
>* Adobe welcomes any feedback, which you can send to `aemcs-new-devconsole-ui-beta@adobe.com`.
>* For the documentation about the current AEM Developer Console, please see [this article.](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console)
>* The AEM as a Cloud Service Developer Console should not be confused with the similarly named [*Adobe Developer Console*.](https://developer.adobe.com/developer-console/)

>[!TIP]
>
>The Developer Console is read-only. If you are working on local development using the SDK and need to modify OSGi settings or repository content, you can use:
>
>* [CRXDE Lite](/help/implementing/developing/tools/crxde.md)
>* [The Web Console](/help/implementing/developing/tools/web-console.md)

<!--
There are multiple ways of accessing it:

1. Launch from Cloud Manager  

1. Type a url that can be determined by adjusting the Author or Publish service urls as follows:
   ```  
   https://dev-console/-<namespace>.<cluster>.dev.adobeaemcloud.com
   ```  

1. As a shortcut, the following Cloud Manager CLI command can be used to launch the AEM as a Cloud Service Developer Console based on an environment parameter described below:    
   ```
   aio cloudmanager:open-developer-console <ENVIRONMENTID> --programId <PROGRAMID>
   ```
-->

## Prerequisites {#prerequisites}

The Developer Console is only accessible to users with certain roles in certain programs.

* For production programs, the "Cloud Manager - Developer Role" in the Adobe Admin Console controls access to the Developer Console.
* For sandbox programs, any user with a product profile granting AEM access can use the Developer Console.
* For all programs, the "Cloud Manager - Developer Role" is required for status dumps and access to the repository browser.

To view data from both author and publish services, users must also be assigned to the "AEM Users" or "AEM Administrators Product Profile" on both services. 

For more information about setting up user permissions, please see the [Cloud Manager Documentation.](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/requirements/users-and-roles)

## OSGi Bundles Tab {#osgi-bundles}

The **OSGi Bundles** tab provides an overview of OSGi bundles that are deployed in the selected environment and offers a full-text search.

![New OSGi Bundles Screen in the Developer Console](/help/implementing/developing/introduction/assets/osgi-bundles.png)

* The tab provides information on the actual state of bundles in the environment such as exported packages, imported packages, used services, and more.
* It is ideal to check the status of bundles see if the bundle does what it is expected to do. 

**Example use-case:** Let's say you specify a version range for a dependency in your bundle. But something goes wrong with the dependency and you need to check which version of the dependency is actually used by the bundle. To check, open the Developer Console and click on a bundle name on the **OSGi Bundles** tab to access the bundle details, and use the **Importing Bundles** accordion to check which bundle version or package version is being used at runtime. With this information, you can adjust your maven dependency version range or adapt your code.

## Java Packages Tab {#java-packages}

The **Java Packages** tab offers a search field to search packages that are active in the environment's OSGi system. 

![Java Packages tab in the Developer Console UI](/help/implementing/developing/introduction/assets/java-packages-dev-console-ui.png)

* You can see which bundle exports (or provides) the package, and you can see which bundles import (or use) the package.
* You can also check for duplicate packages (same package, different versions), which can cause problems in some cases.

**Example use-case:** Let's say that a custom service using the [dynamic class loader](https://sling.apache.org/apidocs/sling9/org/apache/sling/commons/classloader/DynamicClassLoaderManager.html) loads a class without specifying a version. Since multiple bundles export different versions, the implementation varies, causing changes in behavior. You want to check which packages are in the environment without analyzing the feature model. Using this tab you can search for the package and view all exported versions and you can then use a better version range.

## Configurations Tab {#configurations}

The **Configurations** tab offers a searchable list of configurations that are active in the environment. You can see which properties are provided by each configuration by click on it and viewing the details page.

![Configurations tab in the Developer Console UI](/help/implementing/developing/introduction/assets/configurations-dev-console.png)

* **Example use case:** Let's say you want to make sure that the configurations you specified are actually present in the environment. If you search the **Configurations** tab in the console and the configuration is missing, you can check the feature model, the configuration run mode, or folder.

## Servlets Tab {#servlets}

The **Servlets** tab offers a search field where you can specify a path with selectors and an extension with either GET or POST. It then provides a list of servlets in order of preference which handles the request in Sling.

![Servlets tab in the Developer Console UI](/help/implementing/developing/introduction/assets/servlets-dev-console-ui.png)

**Example use case:** Let's say you have an OSGi servlet that should activate upon a request and print output to the response. However, instead of the expected output, you get an empty response. You need to check if some other servlet is taking precedence over your servlet due to more specific selectors, `resourceType`, extensions, or ranking. You search for the expected path, and find another servlet is active with a higher rank. You can then decide if you can increase the rank of your servlet by adding selectors, for example. 

## Services Tab {#services}

The **Services** tab provides an overview of the services present in the selected environment and offers a full-text search.

![Services tab in the Developer Console UI](/help/implementing/developing/introduction/assets/services-dev-console.png)

Click on a service to view its details.

## OSGi Components Tab {#osgi-components}

The **OSGi Components** tab provides an overview of OSGi components that are present in the selected environment type and offers a full-text search. You can see the live state of OSGi components in the environment and which services it satisfies, the bundle providing it, and the activation type (immediate or delayed).

![OSGi Components Tab in the Developer Console UI](/help/implementing/developing/introduction/assets/osgi-components-dev-console.png)

* **Example use case 1:** Let's say you need to check whether a component activated with a configuration is active in a specific environment since you are encountering unexpected behavior. You simply look up the component in the search and check to see if the component is active or not.
* **Example use case 2:** Let's say you want to see which out-of-the-box components are available in the environment and identify the services they support in order to learn more about Adobe Experience Manager as a Cloud Service. You can check the components in the component list. 

## Integrations Tab {#integrations}

The **Integrations** tab allows admins to generate, rename, and delete service credentials and developer tokens.

![Integrations tab in the Developer Console UI](/help/implementing/developing/introduction/assets/integrations-dev-console-ui.png)

## Repository Tab {#repository}

The **Repository** tab opens the [Repository browser.](/help/implementing/developing/tools/repository-browser.md)

## Status Dumps / Queries Tab {#status-dumps-queries}

The **Status dumps / queries** tab allows you to download a full text or JSON dump of the current state of bundles, packages, configurations, services, components, sling jobs, or Oak definitions.

![Status Dumps / Queries tab in the Developer Console UI](/help/implementing/developing/introduction/assets/status-dumps-queries.png)

You can also open the [Query Performance tool.](/help/operations/query-and-indexing-best-practices.md#query-performance-tool)

* **Example use case:** This tab is especially useful if you encounter an unexpected state and want to communicate or document it for other developers. Downloading the dump gives you a snapshot of the state for later reference.
