---
title: AEM as a Cloud Service Developer Console (Beta)
description: Learn about CRX/DE Lite and AEM as a Cloud Service Developer Console
feature: Developing
role: Admin, Architect, Developer
exl-id: 4b0fc3e9-b7c4-4c95-bd97-8b24e4d5cb3d
---
# AEM as a Cloud Service Developer Console (Beta) {#developer-console}

>[!NOTE]
>
>This article describes a revamped experience for the AEM Cloud Service Developer Console, which is now in beta, and available to some customers by clicking a button at the top of the classic UI. We appreciate any feedback you can send to `aemcs-new-devconsole-ui-beta@adobe.com`. For information about the classic AEM Developer Console, see [this article](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console).

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

* This produces an overview of OSGI bundles that are deployed on the selected environment type. It enables a full-text search. 
* It's useful to get information of the actual state of bundles in the environment. You can get information such as exported packages, imported packages, used services and more. 
* Developers want to verify on the actual environment, and check if the bundle does what they expect it to do. 
* **Example use-case:** A version range of a dependency is specified in your bundle. Something is going wrong in the dependency. You want to check which version of the dependency is being wired into your bundle. To check this, you go to the bundle details, and use importing bundles / packages to check which bundle version or package version is being used at runtime to find out. With this information you can adjust your maven dependency version range or adapt your code.

## Java Packages {#java-packages}

![Java Packages tab in the Dev Console UI](/help/implementing/developing/introduction/assets/java-packages-dev-console-ui.png)

* This provides a search prompt you can use to search packages that are active in the environment's OSGI system. In this location you can see which bundle exports (or provides) the package, and you can see which bundle imports (or uses) the package. You can also check for duplicate packages (same package, different versions), which can cause problems in some cases. 
* **Example use-case:** A custom service that is using the [dynamic class loader](https://sling.apache.org/apidocs/sling9/org/apache/sling/commons/classloader/DynamicClassLoaderManager.html) is loading a class without specifying a version, that is exported by multiple bundles with different versions, causing the implementation to be different and the behaviour to change. The developer wants to see which packages are in the environment without analysing the feature model, so they search for this package and see all the versions being exported. This gives them the information to enter a better version range. 

## Servlets {#servlets}

![Servlets tab in the Dev Console UI](/help/implementing/developing/introduction/assets/servlets-dev-console-ui.png)

* This provides a search prompt on which you can specify a path with selectors and an extension with either GET or POST. It then provides results of servlets in order of preference which will handle the request in Sling.
* **Example use case:** You have OSGI servlet that should be activated on a request and print something to the response, but you get an empty response back instead. You need to check if some other servlet is taking precedence over your servlet due to more specific selectors, `resourceType`, extensions or ranking. You search for the expected path, and find out another servlet is active with a higher rank. Then, you decide if you can get your servlet above in rank by adding selectors, for example. 

## Services {#services}

![Services tab in the Dev Console UI](/help/implementing/developing/introduction/assets/services-dev-console.png)

* Similar to the OSGI Components view, but based on services. You can quickly search which services are provided with certain properties. 

## OSGi Components {#osgi-components}

![OSGi Components Tab in the Dev Console UI](/help/implementing/developing/introduction/assets/osgi-components-dev-console.png)

* This produces an overview of OSGI components present in the selected environment type. It enables a full-text search. 
* You can get the live state of OSGI components in the environment. You can see which services it satisfies, the bundle providing it and the activation type (immediate or delayed).
* **Example use-case 1:** As developer, you want to verify if a component that is activated with a configuration is active or not on a particular environment, because you are not getting the behaviour that you expect. You simply lookup the component in the search and check to see if the component is active or not.
* **Example use-case 2:** You are interested to see which out of the box components are present on the environment, and which services they satisfy, to learn more about Adobe Experience Manager as a Cloud Service. You can check them out in the component list. 

## Integrations {#integrations}

![Integrations tab in the Dev Console UI](/help/implementing/developing/introduction/assets/integrations-dev-console-ui.png)

* Gives admins the capability to generate, rename and delete service-credentials and developer tokens.

## Repository {#repository}

* Opens the [Repository browser](/help/implementing/developing/tools/repository-browser.md).

## Status Dumps/Queries {#status-dumps-queries}

![Status Dumps / Queries tab in the Dev Console UI](/help/implementing/developing/introduction/assets/status-dumps-queries.png)

* Gives a full text or JSON dump of the current state of bundles, packages, configurations, services, components, sling jobs or oak definitions.
* This can be useful especially if the developer has discovered some unexpected state, and wants to communicate or document this for other developers. Downloading the dump gives you a snapshot of the state for later reference.

## Configurations {#configurations}

![Configurations tab in the Dev Console UI](/help/implementing/developing/introduction/assets/configurations-dev-console.png)

* This gives you a searchable list of configurations that are active on the environment. You can see which properties are provided by the configurations by checking out the details page.
* **Example use case:** A developer wants to make sure that the configurations they specified are actually present on the environment. If the configuration is lacking, they can check the feature model or the configuration runmode or folder.

For Production programs, access to the AEM as a Cloud Service Developer Console is defined by the "Cloud Manager - Developer Role" in the Adobe Admin Console, while for sandbox programs, the AEM as a Cloud Service Developer Console is available to any user with a product profile giving them access to AEM as a Cloud Service. For all programs, "Cloud Manager - Developer Role" is needed for status dumps and the repository browser and users must also be defined in the AEM Users or AEM Administrators Product Profile on both author and publish services to view data from both services. For more information about setting up user permissions, see [Cloud Manager Documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/requirements/setting-up-users-and-roles.html).
