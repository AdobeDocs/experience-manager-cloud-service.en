---

title: Getting started with Adaptive Forms.
description: Learn how to create mobile-responsive Adaptive Forms with our step-by-step tutorial. These forms adapt seamlessly across devices, ensuring a smooth experience.
keywords: Adaptive Forms, Responsive Forms, HTML5 Forms
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner
hide: yes
hidefromtoc: yes

---

# Create an Adaptive Form (Core Components) - Tutorial 

In this day and age, users expect a mobile-friendly experience across all their interactions, and forms are no exception. Adaptive forms can help you create forms that are not only mobile-friendly but also improve user engagement and reduce the time it takes to complete them.

This tutorial provides a step-by-step guide to creating an adaptive form. It is broken down into a use case and several guides, each of which will teach you how to add a new feature to your adaptive form. 

By the end of the tutorial, you will be able to:

* Create an adaptive form and its data model
* Style your adaptive form
* Build business rules using the adaptive form rule editor
* Pre-fill adaptive form fields 
* Add e-signatures to your form
* Protect your form from bots using Google reCAPTCHA
* Localize your adaptive form for different languages
* Configure your form to produce structured data
* Set up your form to submit data to a REST endpoint
* Publish your adaptive form


## Why create a Core Components based forms? 

AEM Forms provides Foundation Components and Core Components to create forms experiences. Core Components is the modern and recommended approach to create any new forms experience. Why use Core Components? These components are lightweight, open-source (available on github), offer great Google Lighthouse and web vitals score, accessibility compliant, and bring all the familiar features of AEM Sites (like versioning and localization). In addition, these components are easier to style, you can easily customize their appearance as per the branding guidelines of your organization. These have no third-party dependencies, any developer with knowledge of JavaScript and CSS can easily customize these components. 

![Why create Core Components based Adaptive Forms? These components are lightweight, easier to style, offer high lighthouse score, support accessiblity standards, easily customizable, open-sources, availble on github, no dependency on thirdparty libraries, and have almost no learning curve for AEM developers and AEM Authors On top tof it AEM Forms Core Components have all the features of AEM WCM Core Components.](/help/forms/assets/cc-core-components-benefits.png)

## Use Case: Streamlined Home Loan Pre-Qualification with Adaptive Forms

In this tutorial, you build an adaptive form for a large bank. The use case is: 

Potential home buyers visit the bank's website or branch to explore home loan options. The traditional application process is lengthy and overwhelming, often requiring documentation upfront. This deters some buyers from starting the process, hindering both the bank's lead generation and the buyer's ability to confidently search for their dream home.

You are tasked to develop an interactive home loan pre-qualification form. This form would gather basic information, pre-qualify the borrower based on their input, offering estimated loan amounts, potential down payment needs, and interest rates based on different loan types. Pre-qualified users would be able to initiate a full loan application directly from the pre-qualification form.

The form would be built using adaptive forms. This allows for a personalized experience while collecting the necessary financial data for accurate home loan pre-qualification. 

On-completion of the tutorial, your form would look and work like the following form:

![Add a working form here](/help/forms/assets/cc-tutorial-final-form.png)

## Setup a development environment

You can build and test the Adaptive Form directly on your local machine, before deploying it to a Cloud Service environment. Adobe provides an AEM SDK to for local development that lets you

* Create, customize, and testing forms locally. 
* Design forms themes and build configurations locally, 
* Easily deploy your finished assets to the cloud. 

Local development with AEM SDK saves you time and simplifies the development process


**Ready to Begin?**

1. [Set up development tools for AEM Projects](/help/forms/setup-local-development-environment.md#set-up-development-tools-for-aem-projects): Download and install the latest release of [Java 11&trade;](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/development-tools.html?lang=en#local-development-environment-set-up), [Git](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/development-tools.html?lang=en#install-git), [Node.js (npm)](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/development-tools.html?lang=en#node-js), and [Maven](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/development-tools.html?lang=en#install-maven). Also install a plain-text editor, the examples in this tutorial are based on Visual Studio Code. 

1. [Install the AEM SDK](/help/forms/setup-local-development-environment.md#set-up-local-experience-manager-environment-for-development): Download and install the latest version of the AEM SDK. This provides the essential tools for AEM development. Note down the version of AEM SDK. 

    ![Software-Distribution](/help/forms/assets/software-distribution.png)

    ![install AEM SDK](/help/forms/assets/start-aem-sdk.png)

1. [Add the AEM Forms Add-on](/help/forms/setup-local-development-environment.md#add-forms-archive-to-local-author-and-publish-instances-and-configure-forms-specific-users): Download and install the AEM Forms add-on matching to the version of your AEM SDK from the [Software Distribution](https://experience.adobe.com/#/downloads) Portal. 
    ![install-aem-forms-add-on](/help/forms/assets/install-aem-forms-add-on.png)

    +++Install AEM Forms Add-on

        To install AEM Forms Add-on, stop AEM SDK, add AEM Forms add-on (.far) file to the `AEM SDK/crx-quickstart/install` folder, and restart AEM SDK.

    +++

1. [Configure user permissions](/help/forms/setup-local-development-environment.md#configure-users-and-permissions): Create users with development, authoring, and other permissions and add these users to pre-defined forms groups. 


1. [Add Adaptive Forms templates](/help/forms/setup-local-development-environment.md#set-up-a-development-project-for-forms-based-on-experience-manager-archetype): Use AEM Archetypes 48 or later to create a new AEM project and deploy it to your AEM SDK. The project adds Adaptive Forms templates to your AEM SDK. 

    +++Add Adaptive Forms templates

    1. Run the below command to create an AEM project.

        ```
    
        mvn -B org.apache.maven.plugins:maven-archetype-plugin:3.2.1:generate -D archetypeGroupId=com.adobe.aem -D archetypeArtifactId=aem-project-archetype -D archetypeVersion="48" -D appTitle=securbank -D appId=securbank -D groupId=com.securbank -D includeFormsenrollment="y" -D aemVersion="cloud"

        
        ```

        ![AEM-Archetyoe-Project](/help/forms/assets/aem-archetype-project.png) 

    1. Deploy the project to your local development environment. You can use the following command to deploy to your local development environment

        ```
    
        cd securbank
        
        mvn -PautoInstallPackage clean install
        
        ```

    +++

    After deploying the AEM project, you can see Adaptive Forms templates in your environment. 

    ![Adaptive Form Templates](/help/forms/assets/adaptive-forms-templates.png)

For a step-by-step guide on setting up your local AEM Forms development environment, refer [setup local development environment for AEM Forms](/help/forms/setup-local-development-environment.md)



## Next Step

After configuring the development environment, you are ready to create an adaptive form. In the next article, you learn to

* Create an adaptive form from the blank template  
* Layout fields to display and easily accept information.
* Preview the form.

<!-- 

### Step 2: Create Form Data Model

A form data model lets you connect an adaptive form to disparate data sources. For example, AEM user profile, RESTful web services, SOAP-based web services, OData services, and relational databases. You can use the form data model with an adaptive form to retrieve, update, delete, and add data to connected data sources.

Goals of article:

* Create the form data model using Rest endpoint.
* Add data model objects so you can form the data model.
* Configure read and write services for the form data model.
* Test form data model and configured services with test data.

### Step 4: Apply rules to adaptive form fields

AEM Forms provide an editor to write rules on adaptive form objects. These rules define actions to trigger on form objects based on preset conditions, user inputs, and user actions on the form. It helps ensure accuracy and speeds up the form-filling experience.

Goals:

* Create and apply rules to adaptive form fields.
* Use rules to trigger form data model services to update the data to database.

### Step 5: Style your adaptive form

Adaptive forms provide OOTB themes and allows you to customize an existing theme to make a brand specific theme. 


A theme contains styling details for components and panels, and you can reuse a theme in different forms. Styles include properties such as background colors, state colors, transparency, alignment, and size. When you apply the theme to your form, the specified style reflects on corresponding components of your form.

Goals:

* Apply an out of the box theme to an adaptive form.
* Create your brand specific theme.


### Step 6: Publish your adaptive form

You can publish adaptive forms as a stand-alone form (single page application), include in AEM Sites page, or include in a non-AEM Sites page.

Goals:

* Publish the adaptive form as an AEM Page.
* Embed the adaptive form in an AEM Sites Page.
* Embed the adaptive form in an external webpage (a non-AEM webpage hosted outside AEM).

--> 