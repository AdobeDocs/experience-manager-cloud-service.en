---
title: How to enable Adaptive Forms Core Components on AEM Forms as a Cloud Service and local development environment?
description: Learn how to enable Adaptive Forms Core Components on AEM Forms as a Cloud Service.
contentOwner: Khushwant Singh
docset: CloudService
role: Admin, Developer, User
feature: Adaptive Forms, Core Components
exl-id: 32a574e2-faa9-4724-a833-1e4c584582cf
---
# Enable Adaptive Forms Core Components {#enable-headless-adaptive-forms-on-aem-forms-cloud-service}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-core-components/enable-adaptive-forms-core-components.html)                |
| AEM as a Cloud Service     | This article        |

Enabling Adaptive Forms Core Components on AEM Forms as a Cloud Service, lets you start creating, publishing, and delivering Core Components based Adaptive Forms and Headless Forms using your AEM Forms Cloud Service instances to multiple channels. You require Adaptive Forms Core Components enabled environment to use Headless Adaptive Forms.

## Considerations 

*   When you create a fresh AEM Forms as a Cloud Service program, [Adaptive Forms Core Components and Headless Adaptive Forms are already enabled for your environment](#are-adaptive-forms-core-components-enabled-for-my-environment).

*   If you have an older Forms as a Cloud Service program where Core Components are [not enabled](#enable-components), you can [add Adaptive Forms Core Components dependencies](#enable-headless-adaptive-forms-for-an-aem-forms-as-a-cloud-service-environment) to your AEM as a Cloud Service repository and deploy the repository to your Cloud Service environments to enable Headless Adaptive Forms.

*   If your existing Cloud Service environment provides option to [create Core Components-based Adaptive Forms](creating-adaptive-form-core-components.md), Adaptive Forms Core Components and Headless Adaptive Forms are already enabled for your environment and you can serve Core Component based Adaptive Forms as headless forms to channels such as mobile, web, native apps, and services that require a headless representation of Adaptive Forms.


## Enable Adaptive Forms Core Components and Headless Adaptive Forms {#enable-headless-forms}

Perform the following steps, in the listed order, to enable Adaptive Forms Core Components and Headless Adaptive Forms for an AEM Forms as a Cloud Service environment


![Enable core components and headless adaptive forms](/help/forms/assets/enable-headless-adaptive-forms-on-aem-forms-cloud-service.png)


## 1. Clone your AEM Forms as a Cloud Service Git Repository {#clone-git-repository} 
    
1.  Log in to [Cloud Manager](https://my.cloudmanager.adobe.com/) and select your organization and program.

1.  Navigate to the **Pipelines** card from your **Program Overview** page, click the **Access Repo Info** button to access and manage your Git Repository. The page includes the following information:

    * URL to the Cloud Manager Git Repository.
    * Credentials of the Git Repository (Username and Password) Git username.

    Click **Generate Password** to view or generate the password. 
    
1.  Open terminal or command prompt on your local computer and run the following command:

    ```Shell 

    git clone [Git Repository URL]

    ```

    When prompted, provide the credentials. The repository is cloned to your local computer.  

    
## 2. Add Adaptive Forms Core Components dependencies to your Git Repository {#add-adaptive-forms-core-components-dependencies}

1.  Open your Git Repository folder in a plain text code editor. For example, VS Code.
1.  Open the `[AEM Repository Folder]\pom.xml` file for editing.
1.  Replace versions of the `core.forms.components.version`, `core.forms.components.af.version` and `core.wcm.components.version` components with versions specified in [core components documentation](https://github.com/adobe/aem-core-forms-components). If the component does not exist, add these components. 
        
    ```XML

    <!-- Replace the version with the latest released version at https://github.com/adobe/aem-core-forms-components/tags -->

    <properties>
        <core.wcm.components.version>2.22.10</core.wcm.components.version>
        <core.forms.components.version>2.0.18</core.forms.components.version>
        <core.forms.components.af.version>2.0.18</core.forms.components.af.version>
    </properties>

    ```
     
    ![Mention latest version of Forms Core Components](/help/forms/assets/latest-forms-component-version.png)

1.  In the dependencies section of the `[AEM Repository Folder]\pom.xml` file, add the following dependencies, and save the file.

    ```XML

        <!-- WCM Core Component Examples Dependencies -->
            <dependency>
                <groupId>com.adobe.cq</groupId>
                <artifactId>core.wcm.components.examples.ui.apps</artifactId>
                <type>zip</type>
                <version>${core.wcm.components.version}</version>
            </dependency>
            <dependency>
                <groupId>com.adobe.cq</groupId>
                <artifactId>core.wcm.components.examples.ui.content</artifactId>
                <type>zip</type>
                <version>${core.wcm.components.version}</version>
            </dependency>
            <dependency>
                <groupId>com.adobe.cq</groupId>
                <artifactId>core.wcm.components.examples.ui.config</artifactId>
                <version>${core.wcm.components.version}</version>
                <type>zip</type>
            </dependency>    
            <!-- End of WCM Core Component Examples Dependencies -->
            <!-- Forms Core Component Dependencies -->
            <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-core</artifactId>
                <version>${core.forms.components.version}</version>
            </dependency>
            <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-apps</artifactId>
                <version>${core.forms.components.version}</version>
                <type>zip</type>
            </dependency>
            <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-af-core</artifactId>
                <version>${core.forms.components.version}</version>
            </dependency>
            <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-af-apps</artifactId>
                <version>${core.forms.components.version}</version>
                <type>zip</type>
            </dependency>
            <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-examples-apps</artifactId>
                <type>zip</type>
                <version>${core.forms.components.version}</version>
            </dependency>
            <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-examples-content</artifactId>
                <type>zip</type>
                <version>${core.forms.components.version}</version>
            </dependency>
    <!-- End of AEM Forms Core Component Dependencies -->

    ```

1.  Open the `[AEM Repository Folder]/all/pom.xml` file for editing. Add the following dependencies in the `<embeddeds>` section and save the file.

    ```XML

    <!-- WCM Core Component Examples Dependencies -->

    <!-- inside plugin config of filevault-package-maven-plugin -->  
    <!-- embed wcm core components examples artifacts -->

    <embedded>
        <groupId>com.adobe.cq</groupId>
        <artifactId>core.wcm.components.examples.ui.apps</artifactId>
        <type>zip</type>
        <target>/apps/${appId}-vendor-packages/content/install</target>
    </embedded>
    <embedded>
        <groupId>com.adobe.cq</groupId>
        <artifactId>core.wcm.components.examples.ui.content</artifactId>
        <type>zip</type>
        <target>/apps/${appId}-vendor-packages/content/install</target>
    </embedded>
    <embedded>
        <groupId>com.adobe.cq</groupId>
        <artifactId>core.wcm.components.examples.ui.config</artifactId>
        <type>zip</type>
        <target>/apps/${appId}-vendor-packages/content/install</target>
    </embedded>
    <!-- embed forms core components artifacts -->
    <embedded>
        <groupId>com.adobe.aem</groupId>
        <artifactId>core-forms-components-af-apps</artifactId>
        <type>zip</type>
        <target>/apps/${appId}-vendor-packages/application/install</target>
    </embedded>
    <embedded>
        <groupId>com.adobe.aem</groupId>
        <artifactId>core-forms-components-af-core</artifactId>
        <target>/apps/${appId}-vendor-packages/application/install</target>
    </embedded>
    <embedded>
        <groupId>com.adobe.aem</groupId>
        <artifactId>core-forms-components-examples-apps</artifactId>
        <type>zip</type>
        <target>/apps/${appId}-vendor-packages/content/install</target>
    </embedded>
    <embedded>
        <groupId>com.adobe.aem</groupId>
        <artifactId>core-forms-components-examples-content</artifactId>
        <type>zip</type>
        <target>/apps/${appId}-vendor-packages/content/install</target>
    </embedded>

    ```

    >[!NOTE]
    >
    >
    >  Replace `${appId}` with your appId. 
    >
    >  To find your `${appId}`, in the `[AEM Repository Folder]/all/pom.xml` file, search the `-packages/application/install` term. The text before the `-packages/application/install` term is your `${appId}`. For example, the following code, `myheadlessform` is `${appId}`. 
    >
    >   ``` 
    >        <embedded>
    >            <groupId>com.myheadlessform</groupId>
    >            <artifactId>myheadlessform.ui.apps<artifactId>
    >            <type>zip</type>
    >           <target>/apps/myheadlessform-packages/application install</target>
    >        </embedded>
    >   ```

1.  In the `<dependencies>` section of the `[AEM Repository Folder]/all/pom.xml` file, add the following dependencies, and save the file:

    ```XML

            <!-- Other existing dependencies -->
            <!-- wcm core components examples dependencies -->
            <dependency>
                <groupId>com.adobe.cq</groupId>
                <artifactId>core.wcm.components.examples.ui.apps</artifactId>
                <type>zip</type>
            </dependency>
            <dependency>
                <groupId>com.adobe.cq</groupId>
                <artifactId>core.wcm.components.examples.ui.config</artifactId>
                <type>zip</type>
                </dependency>
            <dependency>
                <groupId>com.adobe.cq</groupId>
                <artifactId>core.wcm.components.examples.ui.content</artifactId>
                <type>zip</type>
            </dependency>
                <!-- forms core components dependencies -->
            <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-af-apps</artifactId>
                <type>zip</type>
            </dependency>
            <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-examples-apps</artifactId>
                <type>zip</type>
            </dependency>
                <dependency>
                <groupId>com.adobe.aem</groupId>
                <artifactId>core-forms-components-examples-content</artifactId>
                <type>zip</type>
            </dependency>

    ```

1.  Open the `[AEM Repository Folder]/ui.apps/pom.xml` for editing. Add the `af-core bundle` dependency, and save the file.
    
    ```XML

        <dependency>
        <groupId>com.adobe.aem</groupId>
        <artifactId>core-forms-components-af-core</artifactId>
        </dependency>

    ```

    >[!NOTE]
    >
    >Ensure that the following Adaptive Forms Core Components artifacts are not included in your project.
    >
    > `<dependency>`
    >
    >   `<groupId>com.adobe.aem</groupId>` 
    >   `<artifactId>core-forms-components-apps</artifactId>`
    >
    > `</dependency>`
    >
    > and
    >
    > `<dependency>`
    >
    >   `<groupId>com.adobe.aem</groupId>`
    >   `<artifactId>core-forms-components-core</artifactId>`
    >
    > `</dependency>`


1.  Save and close the file. 

## 3. Build and deploy the updated code 

Deploy the updated code to your local development and Cloud Service environments to enable the Core Components on both the environments:

*   [Build and deploy updated code on a local development environment (AEM as a Cloud Service SDK)](#core-components-on-aem-forms-local-sdk)

*   [Build and deploy updated code on an AEM Forms as a Cloud Service environment](#core-components-on-aem-forms-cs)

### Build and deploy updated code on a local development environment {#core-components-on-aem-forms-local-sdk}

1.  Open the command prompt or terminal.

1.  Navigate to the root directory of your Git Repository project. 

1.  Run the following command to build the package for your environment: 

    ```Shell
            
        mvn clean install
        
    ```



    After the package is successfully built, you can find it at [Git Repository Folder]\all\target\[appid].all-[version].zip

1.  Use the [Package Manager](https://experienceleague.adobe.com/docs/experience-manager-65/administering/contentmanagement/package-manager.html?lang=en) to deploy the [AEM Archetype Project Folder]\all\target\[appid].all-[version].zip package on local development environment.


### Build and deploy updated code on an AEM Forms as a Cloud Service environment {#core-components-on-aem-forms-cs}

1.  Open the terminal or command prompt. 
1.  Navigate to your `[AEM Repository Folder]` and run the following commands in the listed order

    ```Shell
    
     git add pom.xml
     git add all/pom.xml
     git add ui.apps/pom.xml
     git commit -m "Added dependencies for Adaptive Forms Core Components"
     git push origin
    
    ```

1.  After the files are committed to Git Repository, [Run the pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/deploying-code.html).  

    After pipeline run is successful, Adaptive Forms Core Components are enabled for the corresponding environment. Also, an Adaptive Forms (Core Components) template and Canvas 3.0 theme are added to your Forms as a Cloud Service environment, providing you with options to customize and create Core Components based Adaptive Forms. 


## Frequently Asked Questions {#faq}

### What are core components? {#core-components}

The [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html) are a set of standardized Web Content Management (WCM) components for AEM to speed up development time and reduce maintenance cost of your websites.

### What all capabilities are added on enabling core components? {#core-components-capabilities}

When the  Adaptive Forms Core Components are enabled for your environment, a blank Core Components based Adaptive Form template and Canvas 3.0 theme are added to your environment. After enabling Adaptive Forms Core Components for your environment, you can:

* [Create Core Components based Adaptive Forms](/help/forms/creating-adaptive-form-core-components.md).
* [Create Core Components based Adaptive Form templates](/help/forms/template-editor.md).
* [Create custom themes for Core Components based Adaptive Form templates](/help/forms/using-themes-in-core-components.md).
* [Serve Core Component based Adaptive Form's JSON representations to channels such as mobile, web, native apps, and services that require a form's headless representation](https://experienceleague.adobe.com/docs/experience-manager-headless-adaptive-forms/using/overview.html).

### Are Adaptive Forms Core Components enabled for my environment? {#enable-components}

To check that Adaptive Forms Core Components are enabled for your environment:

1.  [Clone your AEM Forms as a Cloud Service repository](#1-clone-your-aem-forms-as-a-cloud-service-git-repository). 

1.  Open the `[AEM Repository Folder]/all/pom.xml` file of your AEM Forms Cloud Service Git Repository. 

1.  Search for the following dependencies:
    
    * core-forms-components-af-core
    * core-forms-components-core
    * core-forms-components-apps
    * core-forms-components-af-apps
    * core-forms-components-examples-apps
    * core-forms-components-examples-content
    
    ![locate the core-forms-components-af-core artifact in all/pom.xml](/help/forms/assets/enable-headless-adaptive-forms-on-aem-forms-cloud-service-locate-core-af-artifact.png)

    If the dependencies exist, Adaptive Forms Core Components are enabled for your environment.

>[!MORELIKETHIS]
>
>* [Create an Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)
