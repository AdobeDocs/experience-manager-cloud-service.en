Introduction
AEM CS delivers new features on a monthly cadence according to the schedule at https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/update-releases-roadmap.html?lang=en#aem-as-cloud-service. In order to become familiar with the features scheduled to go live the following month, customers can subscribe to the prerelease channel, which is accessible by appropriately configuring in standard program dev environments or any sandbox program environment. Customers can preview changes to the author UI console, as well as build code against any new prerelease APIs.

The list of prerelease features for a given month will be posted alongside the release notes https://experienceleague.adobe.com/docs/experience-manager-cloud-service/release-notes/release-notes/release-notes-current.html?lang=en#release-date

How to enable the prerelease
The prerelease features can be experienced in different ways:

Cloud environments (standard program dev environments or any sandbox program environment type)
Local SDK
Cloud envs
See new features in the Author console on cloud devs envs as well as the result of any project customizations.

Using the Cloud Manager API's environment variables endpoint (https://www.adobe.io/apis/experiencecloud/cloud-manager/api-reference.html#/Variables/patchEnvironmentVariables), set the AEM_RELEASE_CHANNEL environment variable to the value prerelease. 

PATCH /program/{programId}/environment/{environmentId}/variables
[
        {
                "name" : "AEM_RELEASE_CHANNEL",
                "value" : "prerelease",
                "type" : "string"
        }
]

The Cloud Manager CLI can also be used, as described at:
The form would be as follows, per the CLI instructions at https://github.com/adobe/aio-cli-plugin-cloudmanager#aio-cloudmanagerset-environment-variables-environmentid
 aio cloudmanager:set-environment-variables <ENVIRONMENT_ID> --variable AEM_RELEASE_CHANNEL "prerelease"

Can set back to empty value if you want the env to be restored to the behavior of the regular (non-prerelease) channel
Local SDK
See new features in the author console in the local Quickstart SDK and code against new APIs in the prerelease by having your maven project reference the prerelease API Jar located in Maven Central.

Customers can also see these prerelease features on their local computer by starting the regular Quickstart SDK in prerelease mode. 
First, download the SDK from the software distribution portal and install as described at https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/aem-as-a-cloud-service-sdk.html?lang=en#accessing-the-aem-as-a-cloud-service-sdk. 
When launching the SDK Quickstart, include the argument -r prerelease
The value is "sticky" so it can only be selected on the first startup. Reinstall the SDK to change the command line option.
Since there may be multiple AEM maintenance releases between monthly feature releases, customers can download those new SDKs and reference the new SDK API Jar versions in maven projects. The maintenance releases will not add additional prerelease features, but could include other smaller changes such as bug fixes, security fixes, and performance enhancements.
Javadocs are published toMaven Central.
To build against the prerelease SDK:

modify your maven project's pom.xml to reference a distinct prerelease sdk api jar, which is published to Maven central. It contains any new Java api for the prerelease features and has a dependency on the sdk api jar. It uses the same version.

As an illustration, we have a snippet from the parent pom's dependency management section referencing the regular API Jar:

<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.adobe.aem</groupId>
            <artifactId>aem-sdk-api</artifactId>
            <version>${aem.sdk.api}</version>
            <scope>provided</scope>
        </dependency>
And then the usage in a module:

<dependencies>
     <dependency>
         <groupId>com.adobe.aem</groupId>
         <artifactId>aem-sdk-api</artifactId>
     </dependency>


In order to change to the prerelease SDK, simply change the dependency from com com.adobe.aem:aem-sdk-api to  com.adobe.aem:aem-prerelease-sdk-api as noted below:

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

As usual, individual project can use the dependency.

Deploy to your local server
If satisfied that it works as expected locally, commit code to a development branch and use a Cloud Manager non-production pipeline to deploy to an environment that subscribes to the prerelease channel

Caution note: The aem-prerelease-sdk-api artifactId must never be used when deploying to Stage or Production. Always user the aem-sdk-api when deploying via the Production Pipeline. Similarly, code referencing prerelease APIs should not be deployed via the Production Pipeline.  

The AEM CS SDK build Analyzer maven plugin v1.0 and higher (https://experienceleague.adobe.com/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin.html?lang=en#developing) will detect if the prerelease api is used in a project by inspecting the dependencies. If the analyzer finds it, it will use the prerelease sdk api to analyze the project.



Considerations
Some features that will be rolled out in the next month release may not be included in the prerelease channel.
features in the prerelease are put through rigorous quality assurance and intended to be feature complete rather than beta quality. If you notice any issues, report them, just as you might if you suspect bugs in features in a regular AEM release.  
To determine if an environment is configured for the prerelease channel, go to the AEM Console's About page and check if the AEM version number includes a "prerelease" suffix such as Adobe Experience Manager 2021.4.5226.20210427T070726Z-210429-PRERELEASE.
