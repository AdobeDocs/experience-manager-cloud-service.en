---
title: AEM as a Cloud Service SDK
description: An overview of the AEM as a Cloud Service Software Development Kit
exl-id: 06f3d5ee-440e-4cc5-877a-5038f9bd44c6
feature: Developing
role: Admin, Architect, Developer
---
# The AEM as a Cloud Service SDK {#aem-as-a-cloud-service-sdk}

The AEM as a Cloud Service SDK is composed of the following artifacts:

* **Quickstart Jar** - The AEM runtime used for local development
* **Java&trade; API Jar** - The Java&trade; Jar/Maven Dependency that exposes all allowed Java&trade; APIs that can be used to develop against AEM as a Cloud Service. Formerly referred to as the Uberjar
* **Javadoc Jar** - The javadocs for the Java&trade; API Jar
* **Dispatcher Tools** - The set of tools used to develop against Dispatcher locally. Separate artifacts for UNIX&reg; and windows

In addition, some customers who were previously deployed with AEM 6.5 or earlier versions use the artifacts below. If local compilation is not working with the Quickstart jar, and you suspect it is from the removal of interfaces from AEM deployed as a Cloud Service, contact Customer Support. They can determine if you need access. It requires changes in the backend.

* **6.5 Deprecated Java&trade; API Jar** - an extra set of interfaced that have been removed since AEM 6.5
* **6.5 Deprecated Javadoc Jar** - the Javadocs for the additional set of interfaced

>[!NOTE]
> 
> There are differences between AEM as a Cloud Service and the SDK, in a number of different areas. For situations where quick and iterative changes are needed, Adobe has introduced Rapid Development Environments. Have a look at [Rapid Development Environments](/help/implementing/developing/introduction/rapid-development-environments.md) for more information.

## Building for the SDK {#building-for-the-sdk}

The AEM as a Cloud Service SDK is used to build and deploy custom code. See the [AEM Project Archetype documentation](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/using.html). At a high level, the following steps are performed:

* **Compile code**. As expected, source code is compiled, generating the resulting content packages
* **Build artifacts**. Artifacts are built during this process
* **Analyze bundles**. Bundles are analyzed using the Maven analyzer plugin, which looks for problems in the Maven project such as missing dependencies
* **Deploy artifacts**. Artifacts are deployed to the local server.

The same steps are executed by Cloud Manager when deploying to Cloud Environments. Performing builds locally allows for local development and testing. Developers can efficiently discover code or structural issues before committing to source control and triggering Cloud Manager deployments, which can take longer.

>[!NOTE]
>
>The AEM as a Cloud Service SDK should be built with a distribution and version of Java supported by [Cloud Manager's build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md). AEM as a Cloud Service customers may download the Oracle JDK from the [Software Distribution portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html) and have Java 11 Extended Support until September 2026 due to Adobe's licensing and support terms for the Oracle Java technology when used in Adobe Experience Manager projects.

## Accessing the AEM as a Cloud Service SDK {#accessing-the-aem-as-a-cloud-service-sdk}

* You can check the AEM Admin Console's **About Adobe Experience Manager** icon to find out the version of AEM you are running on production.
* The quickstart jar and Dispatcher Tools can be downloaded as a zip file from the [Software Distribution portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html). Access to the SDK listings is limited to people who have environments on AEM Managed Services or AEM as a Cloud Service.
* The Java&trade; API Jar and Javadoc Jar can be downloaded through maven tooling, either command line or with your preferred IDE.
* The maven project poms should reference the following API Jar package. Dependency on any subpackage poms should also be referenced.

```
<dependency>
  <groupId>com.adobe.aem</groupId>
  <artifactId>aem-sdk-api</artifactId>
  <version>2019.11.3006.20191108T223635Z-191201</version>
  <scope>provided</scope>
</dependency>
```

>[!NOTE]
>
>The version entry for the SDK should match the version of AEM as a Cloud Service. You can see what version you are using by logging on to AEM. In the upper-right corner of the screen, go to the question mark and select **[!UICONTROL About Adobe Experience Manager]**.


## Refreshing a Local Project with a New SDK Version {#refreshing-a-local-project-with-a-new-skd-version}

When is it recommended to refresh the local project with a new SDK?

Adobe *recommends* refreshing it after a monthly maintenance release.

It is *optional* to refresh it after any daily maintenance release. Customers are informed when their production instance has been successfully upgraded to a new AEM version. For the daily maintenance releases, it is not expected that the new SDK has changed significantly, if at all. Still, it is recommended to occasionally refresh the local AEM developer environment with the latest SDK, then rebuild and test the custom application. The monthly maintenance release typically includes more impactful changes and thus developers should immediately refresh, rebuild, and test.

Below is the recommended procedure for refreshing a local environment:

1. Make sure that any useful content is either committed to the project in source control or available in a mutable content package for later import.
1. Local development test content must be stored separately so that it is not deployed as part of the Cloud Manager pipeline build. The reason is because it is only used for local development.
1. Stop the currently running quickstart.
1. Move the `crx-quickstart` folder to a different folder for safe keeping.
1. Note the new AEM version, which is noted in Cloud Manager (it is used to identify the new QuickStart Jar version to download further on).
1. Download the QuickStart JAR whose version matches the Production AEM version from the Software Distribution Portal.
1. Create a brand new folder and put the new QuickStart Jar inside.
1. Start the new QuickStart with the desired run modes (either renaming file or passing in run modes by way of `-r`).
   * Make sure there's no remnant of the old quickstart in the folder.
1. Build your AEM application.
1. Deploy your AEM application to local AEM by way of Package Manager.
1. Install any mutable content packages needed for local environment testing via Package Manager.
1. Continue development and deploy changes as needed.

If there is content that should be installed with each new AEM quickstart version, include it into a content package and in the project's source control. Then, install it each time.

The recommendation is to update the SDK frequently (for example, biweekly) and dispose full local state daily to not accidentally depend on stateful data in the application.

If you depend on CryptoSupport ([either by configuring the credentials of Cloud services or the SMTP Mail service in AEM or by using CryptoSupport API in your application](https://developer.adobe.com/experience-manager/reference-materials/cloud-service/javadoc/com/adobe/granite/crypto/CryptoSupport.html)), the encrypted properties are encrypted by a key. This key is autogenerated on the first start of an AEM environment. While the cloud setup takes care of automatically reusing the environment-specific CryptoKey, it is necessary to inject the cryptokey into the local development environment.

By default, AEM is configured to store the key data within the data folder of a folder, but for convenience of easier reuse in development, the AEM process can be initialized on first startup with "`-Dcom.adobe.granite.crypto.file.disable=true`". This process generates the encryption data at "`/etc/key`".

To be able to reuse content packages that contain the encrypted values, follow these steps:

* When you initially start up the local quickstart.jar, make sure to add the below parameter: "`-Dcom.adobe.granite.crypto.file.disable=true`". It is recommended, but optional, to always add it.
* The first time you started up an instance, create a package that contains a filter for the root "`/etc/key`". This package holds the secret to be reused across all environments for which you would want them to be reused.
* Export any mutable content containing secrets, or look up the encrypted values by way of `/crx/de` so you can add it to the package that is reused across installations.
* Whenever you spin up a fresh instance (either to replace with a new version or as multiple development environments should share the credentials for testing), install the package produced in step 2 and 3. Doing so lets you reuse the content without the need to manually reconfigure. The reason is because now the cryptokey is in synch.
