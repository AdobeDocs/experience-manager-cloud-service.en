---
title: AEM as a Cloud Service SDK
description: An overview of the AEM as a Cloud Service Software Development Kit
exl-id: 06f3d5ee-440e-4cc5-877a-5038f9bd44c6
---
# The AEM as a Cloud Service SDK {#aem-as-a-cloud-service-sdk}

The AEM as a Cloud Service SDK is comprised of the following artifacts:

* **Quickstart Jar** - The AEM runtime used for local development
* **Java API Jar** - The Java Jar/Maven Dependency that exposes all allowed Java APIs that can be used to develop against AEM as as Cloud Service. Formerly referred to as the Uberjar
* **Javadoc Jar** - The javadocs for the Java API Jar
* **Dispatcher Tools** - The set of tools used to develop against Dispatcher locally. Separate artifacts for unix and windows

In addition, some customers who were previously deployed with AEM 6.5 or earlier versions will use the artifacts below. If local compilation is not working with the Quickstart jar and you suspect it is due to interfaces that have been removed from AEM deployed as a Cloud Service, reach out to Customer Support to determine if you need access. This will require changes in the backend.

* **6.5 Deprecated Java API Jar** - an additional set of interfaced that have been removed since AEM 6.5
* **6.5 Deprecated Javadoc Jar** - the Javadocs for the additional set of interfaced

## Building for the SDK {#building-for-the-sdk}

The AEM as a Cloud Service SDK is used to build and deploy custom code. For further details, reference the [AEM Project Archetype documentation](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/using.html?lang=en). At a high level, the following steps are performed:

* **Compile code**. As expected, source code is compiled, generating the resulting content packages
* **Build artifacts**. Artifacts are built during this process
* **Analyze bundles**. Bundles are analyzed using the Maven analyzer plugin, which looks for problems in the Maven project such as missing dependencies
* **Deploy artifacts**. Artifacts are deployed to the local server.

The same steps are executed by Cloud Manager when deploying to Cloud Environments. Performing builds locally allows for local development and testing so developers can efficiently discover code or structural issues well before committing to source control and triggering Cloud Manager deployments, which can take longer.

## Accessing the AEM as a Cloud Service SDK {#accessing-the-aem-as-a-cloud-service-sdk}

* You can check the AEM Admin Console's **About Adobe Experience Manager** icon to find out the version of AEM you are running on production.
* The quickstart jar and Dispatcher Tools can be downloaded as a zip file from the [Software Distribution portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html). Note that access to the SDK listings is limited to those with AEM Managed Services or AEM as a Cloud Service environments.
* The Java API Jar and Javadoc Jar can be downloaded through maven tooling, either command line or with your preferred IDE.
* The maven project poms should reference the following API Jar package. This dependency should also be referenced in any subpackage poms.

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
>The version entry for the SDK should match the version of AEM as a Cloud Service. You can see what version you are using by logging in to AEM, then going to the question mark in the top right corner of the screen and selecting **[!UICONTROL About Adobe Experience Manager]**


## Refreshing a Local Project with a New SDK Version {#refreshing-a-local-project-with-a-new-skd-version}

When is it recommended to refresh the local project with a new SDK?

It is *recommended* to refresh it at least after a monthly maintenance release.

It is *optional* to refresh it after any daily maintenance release. Customers will be informed when their production instance has been successfully upgraded to a new AEM version. For the daily maintenance releases, it is not expected that the new SDK will have changed significantly, if at all. Still, it is recommended to occasionally refresh the local AEM developer environment with the latest SDK, then rebuild and test the custom application. The monthly maintenance release will typically include more impactful changes and thus developers should immediately refresh, rebuild, and test.

Below is the recommended procedure for refreshing a local environment:

1. Make sure that any useful content is either committed to the project in source control or available in a mutable content package for later import
1. Local development test content needs to be stored separately so that it is not deployed as part of the Cloud Manager pipeline build. This is because it only needs to be used for local development
1. Stop the currently running quickstart
1. Move the `crx-quickstart` folder to a different folder for safe keeping
1. Note the new AEM version, which is noted in Cloud Manager (this will be used to identify the new QuickStart Jar version to download further on)
1. Download the QuickStart JAR whose version matches the Production AEM version from the Software Distribution Portal
1. Create a brand new folder and put the new QuickStart Jar inside
1. Start the new QuickStart with the desired runmodes (either renaming file or passing in runmodes via `-r`).
   * Make sure there's no remnant of the old quickstart in the folder.
1. Build your AEM application
1. Deploy your AEM application to local AEM via PackageManager
1. Install any mutable content packages needed for local environment testing via PackageManager
1. Continue development and deploy changes as needed

If there is content that should be installed with each new AEM quickstart version, include it into a content package and in the project's source control. Then, install it each time.

The recommendation is to update the SDK frequently (for example biweekly) and dispose full local state daily to not accidentally depend on stateful data in the application.

In case you depend on CryptoSupport ([either by configuring the credentials of Cloudservices or the SMTP Mail service in AEM or by using CryptoSupport API in your application](https://docs.adobe.com/content/help/en/experience-manager-cloud-service-javadoc/com/adobe/granite/crypto/CryptoSupport.html)), the encrypted properties will be encrypted by a key that is autogenerated on the first start of an AEM environment. While the cloudsetup takes care of automatically reusing the environment-specific CryptoKey, it is necessary to inject the cryptokey into the local development environment.

By default AEM is configured to store the key data within the data folder of a folder, but for convenience of easier reuse in development, the AEM process can be initialized on first startup with "`-Dcom.adobe.granite.crypto.file.disable=true`". This will generate the encryption data at "`/etc/key`".

To be able to reuse content packages containing the encrypted values you need to follow these steps:

* When you initially start up the local quickstart.jar, make sure to add the below parameter: "`-Dcom.adobe.granite.crypto.file.disable=true`". It is recommended, but optional, to always add it.
* The very first time you started up an instance create a package that contains a filter for the root "`/etc/key`". This will hold the secret to be reused across all environments for which you would want them to be reused
* Export any mutable content containing secrets, or look up the encrypted values via `/crx/de` to add it to the package that will be reused across installations
* Whenever you spin up a fresh instance (either to replace with a new version or as multiple dev environments should share the credentials for testing), install the package produced in step 2 and 3 in order to be able to reuse the content without the need to manually reconfigure. This is because now the cryptokey is in synch.
