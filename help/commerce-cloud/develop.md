---
title: Develop AEM Commerce for AEM as a Cloud Service
description: Learn how to generate a commerce-enabled AEM project using the AEM project archetype. Learn how to build and deploy the project to a local development environment using the AEM as a Cloud Service SDK.
topics: Commerce, Development
feature: Commerce Integration Framework
version: Experience Manager as a Cloud Service
doc-type: tutorial
kt: 5826
thumbnail: 39476.jpg
exl-id: 6f28a52b-52f8-4b30-95cd-0f9cb521de62
role: Admin
---
# Develop AEM Commerce for AEM as a Cloud Service {#develop}

Developing AEM Commerce projects, based on Commerce Integration Framework (CIF) for AEM as a Cloud Service, follows the same rules and best practices like other AEM Projects on AEM as a Cloud Service. Review the following first:

- [AEM Project Structure](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/aem-project-content-package-structure.html)
- [AEM as a Cloud Service SDK](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/aem-as-a-cloud-service-sdk.html)
- [AEM as a Cloud Service Development Guidelines](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/development-guidelines.html)

## Local Development with AEM as a Cloud Service SDK {#local}

>[!VIDEO](https://video.tv.adobe.com/v/39476/?quality=12&learn=on)

A local development environment is recommended to work with CIF projects. The CIF Add-On provided for AEM as a Cloud Service is available for local development as well. It can be downloaded from the [Software Distribution portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html).

The CIF Add-On is provided as a Sling Feature archive. The zip file available on the Software Distribution portal includes two Sling Feature archive files, one for AEM author and one for AEM publish instances.

**New to AEM as a Cloud Service?** Check out [a more detailed guide to setting up a local development environment using the AEM as a Cloud Service SDK](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/overview.html).

### Required Software

The following should be installed locally:

- [AEM as a Cloud Service SDK](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/aem-runtime.html#download-the-aem-as-a-cloud-service-sdk)
- [Java&trade; 11](https://downloads.experiencecloud.adobe.com/content/software-distribution/en/general.html)
- [Apache Maven](https://maven.apache.org/) (3.3.9 or newer)
- [Node.js v10+](https://nodejs.org/en)
- [npm 6+](https://www.npmjs.com/)
- [Git](https://git-scm.com/)

### Accessing the CIF add-on

The CIF add-on can be downloaded as a zip file from the [Software Distribution portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html). The zip file contains the CIF add-on as **Sling Feature archive**, it is not an AEM package. SDK listings are accessible with an AEM as a Cloud Service license.

>[!TIP]
>
>Make sure you always use the latest CIF Add-On version.

### Local Setup

For local CIF Add-on development using the AEM as a Cloud Service SDK following steps:

1. Get the latest AEM as a Cloud Service SDK
1. Unpack the AEM .jar so you can create the `crx-quickstart` folder, run:

    ```bash
    java -jar <jar name> -unpack
    ```

1. Create a `crx-quickstart/install` folder
1. Copy the correct Sling Feature archive file of the CIF add-on into the `crx-quickstart/install` folder.

    The CIF add-on zip file contains two Sling Feature archive `.far` files. Make sure to use the correct one for AEM Author or AEM Publish, depending on how you plan to run the local AEM as a Cloud Service SDK.

1. Create a local OS environment variable named `COMMERCE_ENDPOINT` holding the Adobe Commerce GraphQL endpoint.

    Example macOS X:

    ```bash
    export COMMERCE_ENDPOINT=https://<yourcommercesystem>/graphql
    ```

    Example Windows:

    ```bash
    set COMMERCE_ENDPOINT=https://<yourcommercesystem>/graphql
    ```

    This variable is used by AEM to connect to your commerce system. Also, the CIF add-on includes a local reverse proxy to make the Commerce GraphQL endpoint available locally. This proxy is used by the CIF authoring tools (product console and pickers) and for the CIF client-side components doing direct GraphQL calls.

    This variable must be set up for the AEM as a Cloud Service environment as well. For more information on variables, see [Configuring OSGi for AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-osgi.html#local-development).

1. (Optional) To enable staged catalog features, you must create an integration token for your Adobe Commerce instance. Follow the steps at [Getting Started](./getting-started.md#staging) to create the token.

    Set an OSGi secret  with the name `COMMERCE_AUTH_HEADER` to the following value:

    ```xml
    Authorization: Bearer <Access Token>
    ```

    For more information on secrets, see [Configuring OSGi for AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/deploying/configuring-osgi.html#local-development).

1. Start the AEM as a Cloud Service SDK

>[!NOTE]
>
>Make sure you start AEM as a Cloud Service SDK in the same terminal window the environment variable was set in step 5. If you start it in a separate terminal window, or by double-clicking the .jar file, make sure that the environment variable is visible.

Verify the setup via OSGI console: `http://localhost:4502/system/console/osgi-installer`. The list should include the CIF add-on related bundles, content-package, and OSGI configurations as defined in the feature model file.

## Project Setup {#project}

There are two ways to Bootstrap your CIF project for AEM as a Cloud Service.

### Use AEM Project Archetype

The [AEM Project Archetype](https://github.com/adobe/aem-project-archetype) is the main tool to Bootstrap a preconfigured project to get started with CIF. CIF Core Components and all the required configurations can be included in a generated project with one additional option.

>[!TIP]
>
>Always use the latest version of the [AEM Project Archetype](https://github.com/adobe/aem-project-archetype/releases) so you can generate the project.

See AEM Project Archetype [usage instructions](https://github.com/adobe/aem-project-archetype#usage) on how to generate an AEM project. To include CIF into the project, use the `includeCommerce` option.

For example:

```bash
mvn -B org.apache.maven.plugins:maven-archetype-plugin:3.2.1:generate \
 -D archetypeGroupId=com.adobe.aem \
 -D archetypeArtifactId=aem-project-archetype \
 -D archetypeVersion=35 \
 -D appTitle="My Site" \
 -D appId="mysite" \
 -D groupId="com.mysite" \
 -D includeCommerce=y
```

CIF Core Components can be used in any project by either including the provided `all` package or individually using the CIF content package and related OSGI bundles. To manually add CIF Core Components to a project, use the following dependencies:

```java
<dependency>
    <groupId>com.adobe.commerce.cif</groupId>
    <artifactId>core-cif-components-apps</artifactId>
    <type>zip</type>
    <version>x.y.z</version>
</dependency>
<dependency>
    <groupId>com.adobe.commerce.cif</groupId>
    <artifactId>core-cif-components-config</artifactId>
    <type>zip</type>
    <version>x.y.z</version>
</dependency>
<dependency>
    <groupId>com.adobe.commerce.cif</groupId>
    <artifactId>core-cif-components-core</artifactId>
    <version>x.y.z</version>
</dependency>
<dependency>
    <groupId>com.adobe.commerce.cif</groupId>
    <artifactId>graphql-client</artifactId>
    <version>x.y.z</version>
</dependency>
<dependency>
    <groupId>com.adobe.commerce.cif</groupId>
    <artifactId>magento-graphql</artifactId>
    <version>x.y.z</version>
</dependency>
```

### Use AEM Venia Reference Store

A second option to start a CIF project is to clone and use the [AEM Venia Reference Store](https://github.com/adobe/aem-cif-guides-venia). The AEM Venia Reference Store is a sample reference storefront application that demonstrates the usage of CIF Core Components for AEM. It is intended as a best-practice set of examples and a potential starting point to develop your own functionality.

To get started with the Venia Reference Store, clone the Git repository and start customizing the project according to your needs.

>[!NOTE]
>
>The Venia Reference Store project contains two build profiles for AEM as a Cloud Service and AEM 6.5. Check [project readme.md](https://github.com/adobe/aem-cif-guides-venia/blob/main/README.md) so you can see how they are used.

## Additional Resources

- [AEM Project Archetype](https://github.com/adobe/aem-project-archetype)
- [AEM Venia Reference Store](https://github.com/adobe/aem-cif-guides-venia)
- [Software Distribution portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html)
