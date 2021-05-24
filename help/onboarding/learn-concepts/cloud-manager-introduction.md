---
title: Learn what is Cloud Manager
description: Follow this page to learn about Cloud Manager, Cloud Manager Programs, and Environments.
---

# Introduction to Cloud Manager {#intro-cloud-manager}

Cloud Manager is an essential component of AEM as a Cloud Service and serves as the single entry point for your team.

To support customers with enterprise development setups, AEM as a Cloud Service fully integrates with Cloud Manager and its purpose-built CI/CD pipelines, which are equipped to ensure thorough testing and highest code quality to deliver exceptional experiences.

To ensure customers can start quickly with AEM as a Cloud Service, Cloud Manager provides everything required to get started in a self-service manner including the ability to create your cloud resources and environments. In this manner, your AEM developers can access the Git repository via Cloud Manager. Using Cloud Manager, development teams can work towards committing changes frequently in a self-service manner.

Your System Administrator will be responsible to setting up your Cloud Manager team which will include individuals that will create your cloud resources and developers. Refer to [Enterprise Team Development Setup for AEM as a Cloud Service](/help/implementing/cloud-manager/enterprise-team-dev-setup.md) to learn how Cloud Manager supports in Enterprise Team Development Setup.

## Cloud Manager Programs {#cloud-manager-programs}

Cloud Manager Programs represent sets of Cloud Manager environments supporting logical sets of business initiatives, typically corresponding to a purchased Service Level Agreement (SLA). For example, one Program may represent the AEM resources to support the global public Web sites, while another Program represents an internal Central DAM. Watch this video to learn more.

A user can create a **Sandbox** or a **Production** program. 

* A *Production Program* is created to enable live traffic at the appropriate time in the future.
   Refer to [Introduction to Production Programs](/help/onboarding/getting-access-to-aem-in-cloud/introduction-production-programs.md) for more details.

* A *Sandbox Program* is typically created to serve the purposes of training, running demo’s, enablement, POC’s, or documentation. It is not meant to carry live traffic and will have restrictions that a Production program will not. It will include Sites and Assets and will be delivered auto-populated with a Git branch that includes sample code, a Dev environment, and a non-production pipeline.
   Refer to [Introduction to Sandbox Programs](/help/onboarding/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md) for more details.

## Navigating to Cloud Manager {#navigate-cloud-manager}

Once your System Administrator grants you access to Cloud Manager, you will receive an email that will take you to [Adobe Experience Cloud](https://experience.adobe.com) Home page.

>[!NOTE]
>You must be added as a user and must be assigned at least to one Cloud Manager Role (Product Profile in Admin Console) by your System Administrator. 

1. From your welcome email click on **Get started**, as shown in the figure below.
    ![](/help/onboarding/what-is-required/assets/get-started-email.png)

   >[!NOTE]
   >Alternatively, you can also navigate directly to Cloud Manager login page from [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/). Depending on the roles assigned in [!UICONTROL Cloud Manager] and the state of the application, you will see different screens while using [!UICONTROL Cloud Manager] UI. Refer to the section below, [Cloud Manager Landing page](#cloud-manager-landing) for more details.

1. Select **Experience Manager**.
   ![](/help/onboarding/getting-access-to-aem-in-cloud/assets/landing-page1.png)
   
1. Click on **Launch** from the Cloud Manager card. Once you have successfully logged in to [!UICONTROL Cloud Manager], you are ready to use the User Interface (UI).
   ![](/help/onboarding/getting-access-to-aem-in-cloud/assets/landing-page2.png)
  

### Cloud Manager Landing Page {#cloud-manager-landing}

Upon successful login, you will be directed to the landing page of Cloud Manager.

>[!NOTE]
>Depending on the roles assigned in [!UICONTROL Cloud Manager] and the state of the application, you will see different screens while using [!UICONTROL Cloud Manager] UI.

You will see one of the three options, described below:

* **When No Programs exist in Cloud Manager**

   If no programs exist in your Organization, then your landing page directs you to create your first program, as shown in the figure below.
   ![](/help/onboarding/getting-access-to-aem-in-cloud/assets/first_timelogin0.png)

* **When Programs already exist in Cloud Manager**

   If program(s) already exist in your Organization, then your landing page directs you to add another program and displays all your existing programs too, as shown in the figure below.

   ![](/help/onboarding/getting-access-to-aem-in-cloud/assets/first_timelogin1.png)

* **When a Program exists and user is System Administrator**

   If program(s) already exist in your Organization, and you are a System Administrator, then your landing page displays **Manage Access** button along with **Add Program** option, as shown in the figure below.

   ![](/help/onboarding/getting-access-to-aem-in-cloud/assets/admin-console-4.png)

From here, a user with the right permissions, such as a Business Owner role in Cloud Manager is able to select **Add Program** to launch the [Add Program wizard](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/production-programs/creating-production-program.html?lang=en#getting-access).

## Cloud Manager Environments {#cloud-manager-environments}

Cloud Manager Environments typically have one Production environment, one Stage environment, and one Development environment. Different environments support roles and can be engaged using different CI/CD Pipelines. 

The CI/CD Pipelines in Cloud Manager are composed of services such as:

* [AEM Author](#author-services)
* [AEM Publish](publish-services)
* [Dispatcher](#dispatcher-services)

   >[!NOTE]
   > Refer to the video [Using Adobe Cloud Manager Environments](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html?lang=en#cloud-manager) to learn more about the available environments.

### AEM Author Service {#author-services}

Environment where site content and digital assets are created, managed and updated. Typically only internal users have access to the Author Service and is behind a login screen. The Authoring Service is designed both as an authoring and preview environment.

### AEM Publish Service {#publish-services}

Environment that hosts the end-user experience, like a web site. This is the service that site visitors will view and interact with. Typically, the Publish Service is publicly available.

### AEM Dispatcher Service {#dispatcher-services}

The Dispatcher is an Apache HTTP Web server module that provides a security and performance layer that sits in front of the AEM Publish Service.