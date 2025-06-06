---
title: Adobe Experience Manager as a Cloud Service Prerelease Channel
description: Learn how to use the prerelease channel to get a preview of upcoming features to AEM as a Cloud Service.
exl-id: cfc91699-0087-40fa-a76c-0e5e1e03a5bd
feature: Release Information
role: Admin
---

# Adobe Experience Manager as a Cloud Service Prerelease Channel {#prerelease-channel}

Learn how to use the prerelease channel to get a preview of upcoming features to AEM as a Cloud Service.

## Introduction {#introduction}

Adobe Experience Manager as a Cloud Service delivers new features on a regular cadence. The list of new and upcoming features for a given feature release is posted within the [release notes.](/help/release-notes/release-notes-cloud/release-notes-current.md)

Upcoming features generally are made available in one of two ways:

* As part of an early-adopter program
* As part of the prerelease channel

This document describes how to enable the prerelease channel. Please see the document [Release Notes for Adobe Experience Manager (AEM) as a Cloud Service](help/release-notes/home.md) for details on the AEM release schedule.

## Enable the Prerelease Channel to Access and Try Upcoming Features {#enable-prerelease}

The prerelease channel can be enabled on any development or sandbox environment. The prerelease channel can not be enabled on staging or production environments.

The prerelease channel can be accessed in two different ways:

* [Cloud environments](#cloud-environments)
* [Local SDK](#local-sdk)

### Cloud Environments {#cloud-environments}

To update a cloud environment to use the prerelease channel, you must add a new environment variable. You can do this either using the Cloud Manager UI or via CLI.

#### Add Environment Variable Using the UI {#add-with-ui}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Navigate to the program where you want to enable the prerelease channel.
 
1. Select the environment where you want to enable the prerelease channel and access its configuration via **Program** &gt; **Environment** &gt; **Environment Configuration**.

1. Add a new [environment variable](/help/implementing/cloud-manager/environment-variables.md)

    | Name | Value | Service Applied | Type |
    |------|-------|-----------------|------|
    | `AEM_RELEASE_CHANNEL` | `prerelease` | All | Variable|

1. Save the changes and the environment will refresh with the prerelease channel enabled.

    ![New environment variable](assets/env-configuration-prerelease.png)

#### Add Environment Variable Using the CLI {#add-with-cli}

You can also use the Cloud Manager API and CLI to update the environment variables.

* Using [Cloud Manager API's environment variables endpoint](https://developer.adobe.com/experience-cloud/cloud-manager/reference/api/#operation/patchEnvironmentVariables), set the `AEM_RELEASE_CHANNEL` environment variable to the value `prerelease`. 

    ```text
    PATCH /program/{programId}/environment/{environmentId}/variables
    [
            {
                    "name" : "AEM_RELEASE_CHANNEL",
                    "value" : "prerelease",
                    "type" : "string"
            }
    ]
    ```

* [The Cloud Manager CLI](https://github.com/adobe/aio-cli-plugin-cloudmanager#aio-cloudmanagerset-environment-variables-environmentid) can also be used

    ```shell
    aio cloudmanager:environment:set-variables <ENVIRONMENT_ID> --programId=<PROGRAM_ID> --variable AEM_RELEASE_CHANNEL "prerelease
    ```

The variable can be deleted if you want to restore the environment to standard behavior (non-prerelease channel).

### Local SDK {#local-sdk}

You can access upcoming features in the prerelease channel in your local Quickstart SDK and code against new APIs by configuring your Maven project to reference the prerelease channel `API Jar` located in Maven Central. You can also see access the prerelease channel in your local development environment by starting the regular Quickstart SDK in prerelease mode.

#### Start Quickstart SDK in Prerelease Mode {#prerelease-mode}

1. Download the SDK from software distribution and install as described in [Accessing the AEM as a Cloud Service SDK.](/help/implementing/developing/introduction/aem-as-a-cloud-service-sdk.md)
1. When launching the SDK Quickstart, include the argument `-r prerelease`.

The value is sticky so it can only be selected on the first startup. Reinstall the SDK to change the command-line option.

Since there may be multiple AEM maintenance releases between monthly feature releases, you can download these new SDKs and reference the new SDK API Jar versions in maven projects. The maintenance releases will not add additional prerelease features, but could include other smaller changes such as bug fixes, security fixes, and performance enhancements.
Javadocs are published to Maven Central.

#### Build Against the Prerelease SDK {#build-sdk}

1. Modify your maven project's `pom.xml` to reference a distinct prerelease SDK API jar, which is published to Maven Central. It contains any new Java API for the prerelease features and has a dependency on the SDK API jar. It uses the same version.

   As an example, here is a snippet from the parent pom's dependency management section referencing the regular API jar:

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

   To change to the prerelease SDK, simply change the dependency from `com.adobe.aem:aem-sdk-api` to `com.adobe.aem:aem-prerelease-sdk-api` as noted below:

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

1. Deploy to your local server.

1. If satisfied that it works as expected locally, commit code to a development branch and use a Cloud Manager non-production pipeline to deploy to an [environment that has the prerelease channel enabled.](#cloud-environments)

>[!CAUTION]
> 
> The `aem-prerelease-sdk-api` artifactId must never be used when deploying to stage or production. Always user the `aem-sdk-api` when deploying via the production pipeline. Similarly, code that references prerelease APIs should not be deployed via the production pipeline.  

The [AEM CS SDK build Analyzer maven plugin v1.0 and higher](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html#developing) will detect if the prerelease API is used in a project by inspecting the dependencies. If the analyzer finds it, it will use the prerelease SDK API to analyze the project.

## Considerations {#considerations}

There are a few items to note when using the prerelease channel.

* The prerelease channel does not necessarily contain all new features to be rolled out in the following release.
* Features in the prerelease are put through rigorous quality assurance and intended to be feature complete rather than beta quality. If you notice any issues, report them, just as you would do if you suspect bugs in features in a regular AEM release.  
* To determine if an environment is configured for the prerelease channel, go to the AEM console's **About** page and check if the AEM version number includes a `PRERELEASE` suffix such as `Adobe Experience Manager 2021.4.5226.20210427T070726Z-210429-PRERELEASE`.

![About](/help/release-notes/assets/about.png)
