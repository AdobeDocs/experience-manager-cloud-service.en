---
title: [!DNL Adobe Experience Manager] as a Cloud Service Prerelease Channel
description: [!DNL Adobe Experience Manager] as a Cloud Service Prerelease Channel
---

# [!DNL Adobe Experience Manager] as a Cloud Service Prerelease Channel {#prerelease-channel}


## Introduction {#introduction}

[!DNL Adobe Experience Manager] as a Cloud Service delivers new features on a monthly cadence, according to the schedule on [Experience Manager releases roadmap](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html?lang=en#aem-as-cloud-service). In order to become familiar with the features scheduled to go live the following month, customers can subscribe to the prerelease channel, which is accessible by appropriately configuring in standard program development environments or any sandbox program environments. Customers can preview changes to the Sites console, as well as build code against any new prerelease APIs.

The list of prerelease features for a given month are posted within the [monthly release notes](/help/release-notes/release-notes-cloud/release-notes-current.md).

## How to Enable the Prerelease {#enable-prerelease}

The prerelease features can be experienced in different ways:

* Cloud environments (standard program dev environments or any sandbox program environment type)
* Local SDK

### Cloud Environments {#cloud-environments}

To see new features in the Sites console on cloud dev environments as well as the result of any project customizations:

* Using the [Cloud Manager API's environment variables endpoint](https://www.adobe.io/apis/experiencecloud/cloud-manager/api-reference.html#/Variables/patchEnvironmentVariables), set the **AEM_RELEASE_CHANNEL** environment variable to the value **prerelease**. 

```
PATCH /program/{programId}/environment/{environmentId}/variables
[
        {
                "name" : "AEM_RELEASE_CHANNEL",
                "value" : "prerelease",
                "type" : "string"
        }
]
```

The Cloud Manager CLI can also be used, as per the instructions at [https://github.com/adobe/aio-cli-plugin-cloudmanager#aio-cloudmanagerset-environment-variables-environmentid](https://github.com/adobe/aio-cli-plugin-cloudmanager#aio-cloudmanagerset-environment-variables-environmentid)
 ```aio cloudmanager:environment:set-variables <ENVIRONMENT_ID> --programId=<PROGRAM_ID> --variable AEM_RELEASE_CHANNEL “prerelease”```
 

The variable can be deleted or set back to a different value if you want the environment to be restored to the behavior of the regular (non-prerelease) channel

### Local SDK {#local-sdk}

You can see new features in the Sites console in the local Quickstart SDK and code against new APIs in the prerelease by having your maven project reference the prerelease `API Jar` located in Maven Central. You can also see these prerelease features on your local computer by starting the regular Quickstart SDK in prerelease mode:

* Download the SDK from the software distribution portal and install as described in [Accessing the AEM as a Cloud Service SDK](/help/implementing/developing/aem-as-a-cloud-service-sdk.md#accessing-the-aem-as-a-cloud-service-sdk.)
* When launching the SDK Quickstart, include the argument `-r prerelease`.
* The value is *sticky* so it can only be selected on the first startup. Reinstall the SDK to change the command line option.

Since there may be multiple AEM maintenance releases between monthly feature releases, you can download these new SDKs and reference the new SDK API Jar versions in maven projects. The maintenance releases will not add additional prerelease features, but could include other smaller changes such as bug fixes, security fixes, and performance enhancements.
Javadocs are published to Maven Central.

To build against the prerelease SDK:

1. modify your maven project's pom.xml to reference a distinct prerelease sdk api jar, which is published to Maven central. It contains any new Java api for the prerelease features and has a dependency on the sdk api jar. It uses the same version.

   As an example, here is a snippet from the parent pom's dependency management section referencing the regular API Jar:

   ```
   <dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.adobe.aem</groupId>
            <artifactId>aem-sdk-api</artifactId>
            <version>${aem.sdk.api}</version>
            <scope>provided</scope>
        </dependency>
   ```
        
   And then the usage in a module:

   ```
    <dependencies>
     <dependency>
         <groupId>com.adobe.aem</groupId>
         <artifactId>aem-sdk-api</artifactId>
     </dependency>
   ```

   In order to change to the prerelease SDK, simply change the dependency from `com.adobe.aem:aem-sdk-api` to `com.adobe.aem:aem-prerelease-sdk-api` as noted below:

   ```
   <dependencyManagement>
    <dependencies>
      <dependency>
            <groupId>com.adobe.aem</groupId>
            <artifactId>aem-prerelease-sdk-api</artifactId>
            <version>${aem.sdk.api}</version>
            <scope>provided</scope>
      </dependency>
   <dependencies>
      <dependency>
         <groupId>com.adobe.aem</groupId>
         <artifactId>aem-prerelease-sdk-api</artifactId>
      </dependency>
   ```

   As usual, individual projects can use the dependency.

1. Deploy to your local server
1. If satisfied that it works as expected locally, commit code to a development branch and use a Cloud Manager non-production pipeline to deploy to an environment that subscribes to the prerelease channel

>[!CAUTION]
> 
> The `aem-prerelease-sdk-api` artifactId must never be used when deploying to Stage or Production. Always user the aem-sdk-api when deploying via the Production Pipeline. Similarly, code referencing prerelease APIs should not be deployed via the Production Pipeline.  

The [AEM CS SDK build Analyzer maven plugin v1.0 and higher](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html?lang=en#developing) will detect if the prerelease api is used in a project by inspecting the dependencies. If the analyzer finds it, it will use the prerelease sdk api to analyze the project.

## Considerations {#considerations}

There are a few things to note when it comes to the prerelease channel:

* Some features that will be rolled out in the next month release may not be included in the prerelease channel.
* Features in the prerelease are put through rigorous quality assurance and intended to be feature complete rather than beta quality. If you notice any issues, report them, just as you would do if you suspect bugs in features in a regular AEM release.  
* To determine if an environment is configured for the prerelease channel, go to the AEM Console's **About** page and check if the AEM version number includes a *prerelease* suffix such as ```Adobe Experience Manager 2021.4.5226.20210427T070726Z-210429-PRERELEASE```.

![about](/help/release-notes/assets/about.png)
