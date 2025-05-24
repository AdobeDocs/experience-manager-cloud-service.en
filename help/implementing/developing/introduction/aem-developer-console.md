---
title: AEM as a Cloud Service Developer Console - Beta
description: Learn about CRXDE Lite and AEM as a Cloud Service Developer Console.
feature: Developing
role: Admin, Architect, Developer
exl-id: 4b0fc3e9-b7c4-4c95-bd97-8b24e4d5cb3d
---
# AEM as a Cloud Service Developer Console (Beta) {#developer-console}

>[!NOTE]
>
>This article describes a revamped experience for the AEM Cloud Service Developer Console, which is now in beta. Some customers can access it by clicking a button at the classic UI's top. Adobe welcomes any feedback from you by sending it to `aemcs-new-devconsole-ui-beta@adobe.com`. For information about the classic AEM Developer Console, see [this article](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console).

The AEM as a Cloud Service Developer Console includes a set of tools for debugging in Cloud environments. It can be accessed through a per-environment link in Cloud Manager.

>[!NOTE]
>The AEM as a Cloud Service Developer Console should not be confused with the similarly named [*Adobe Developer Console*](https://developer.adobe.com/developer-console/).
>


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

Developers can access the features described below: 

## OSGi Bundles {#osgi-bundles}

![New OSGi Bundles Screen in Dev Console](/help/implementing/developing/introduction/assets/osgi-bundles.png)

* An overview of OSGI bundles that are deployed in the selected environment type. It enables a full-text search. 
* It is useful to get information of the actual state of bundles in the environment. You can get information such as exported packages, imported packages, used services and more. 
* Developers want to verify on the actual environment, and check if the bundle does what they expect it to do. 
* **Example use-case:** A version range of a dependency is specified in your bundle. Something is going wrong in the dependency. You want to check which version of the dependency is being wired into your bundle. To check, go to the bundle details, and use importing bundles / packages to check which bundle version or package version is being used at runtime. With this information, you can adjust your maven dependency version range or adapt your code.

## Java Packages {#java-packages}

![Java Packages tab in the Dev Console UI](/help/implementing/developing/introduction/assets/java-packages-dev-console-ui.png)

* A search prompt that you can use to search packages that are active in the environment's OSGI system. In this location you can see which bundle exports (or provides) the package, and you can see which bundle imports (or uses) the package. You can also check for duplicate packages (same package, different versions), which can cause problems in some cases. 
* **Example use-case:** A custom service using the [dynamic class loader](https://sling.apache.org/apidocs/sling9/org/apache/sling/commons/classloader/DynamicClassLoaderManager.html) loads a class without specifying a version. Since multiple bundles export different versions, the implementation varies, causing changes in behavior. The developer wants to check which packages are in the environment without analyzing the feature model. They search for the package and view all exported versions. This ability gives them the information to enter a better version range. 

## Servlets {#servlets}

![Servlets tab in the Dev Console UI](/help/implementing/developing/introduction/assets/servlets-dev-console-ui.png)

* A search prompt on which you can specify a path with selectors and an extension with either GET or POST. It then provides the results of servlets in order of preference which handles the request in Sling.
* **Example use case:** You have an OSGI servlet that should activate upon a request and print output to the response. However, instead of the expected output, the response returns empty. You need to check if some other servlet is taking precedence over your servlet due to more specific selectors, `resourceType`, extensions or ranking. You search for the expected path, and find out another servlet is active with a higher rank. Then, you decide if you can get your servlet above in rank by adding selectors, for example. 

## Services {#services}

![Services tab in the Dev Console UI](/help/implementing/developing/introduction/assets/services-dev-console.png)

* Similar to the OSGI Components view, but based on services. You can quickly search which services are provided with certain properties. 

## OSGi Components {#osgi-components}

![OSGi Components Tab in the Dev Console UI](/help/implementing/developing/introduction/assets/osgi-components-dev-console.png)

* An overview of OSGI components that are present in the selected environment type. It enables a full-text search. 
* You can get the live state of OSGI components in the environment. You can see which services it satisfies, the bundle providing it and the activation type (immediate or delayed).
* **Example use case 1:** As a developer, you need to check whether a component activated with a configuration is active in a specific environment. The reason is because the expected behavior is not occurring. You simply look up the component in the search and check to see if the component is active or not.
* **Example use case 2:** You want to see which out-of-the-box components are available in the environment and identify the services they support. This ability helps you learn more about Adobe Experience Manager as a Cloud Service. You can check them out in the component list. 

## Integrations {#integrations}

![Integrations tab in the Dev Console UI](/help/implementing/developing/introduction/assets/integrations-dev-console-ui.png)

* Admins have the capability to generate, rename, and delete, service-credentials and developer tokens.

## Repository {#repository}

* Opens the [Repository browser](/help/implementing/developing/tools/repository-browser.md).

## Status Dumps / Queries {#status-dumps-queries}

![Status Dumps / Queries tab in the Dev Console UI](/help/implementing/developing/introduction/assets/status-dumps-queries.png)

* A full text or JSON dump of the current state of bundles, packages, configurations, services, components, sling jobs or Oak definitions.
* Useful especially if the developer has discovered some unexpected state, and wants to communicate or document this state for other developers. Downloading the dump gives you a snapshot of the state for later reference.

## Configurations {#configurations}

![Configurations tab in the Dev Console UI](/help/implementing/developing/introduction/assets/configurations-dev-console.png)

* A searchable list of configurations that are active in the environment. You can see which properties are provided by the configurations by checking out the details page.
* **Example use case:** A developer wants to make sure that the configurations they specified are actually present in the environment. If the configuration is lacking, they can check the feature model or the configuration run mode or folder.

For Production programs, the "Cloud Manager - Developer Role" in the Adobe Admin Console controls access to the AEM as a Cloud Service Developer Console. For sandbox programs, any user with a product profile granting AEM access can use the Developer Console. For all programs, the "Cloud Manager - Developer Role" is required for status dumps and access to the repository browser. To view data from both author and publish services, users must also be assigned to the AEM Users or AEM Administrators Product Profile on both services. 

For more information about setting up user permissions, see [Cloud Manager Documentation](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/requirements/users-and-roles).

