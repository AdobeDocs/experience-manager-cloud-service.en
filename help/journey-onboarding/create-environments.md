---
title: Create Environments
description: Lean how to use Cloud Manager to create your first environments.
role: Admin, User, Developer
exl-id: 31940e1e-fe27-4c5f-b67f-41affebea63a
feature: Onboarding
---
# Create environments {#create-environments}

In this part of the [onboarding journey](overview.md), you learn how to use Cloud Manager to create your first environments.

## Objective {#objective}

After reading the previous document in this onboarding journey, [Creating Programs](create-program.md), you now have your own Cloud Manager program. Now, you can lean how to use Cloud Manager to create your first environments for that program.

After reading this document, you will:

* Understand what an environment is.
* Know the difference between the different environments.
* Be able to create your own environment.

## What is an environment? {#environments}

Environments sit below programs within the hierarchy of Cloud Manager. While programs allow you to organize your solution and grant access to particular team members to those programs, environments belong to specific programs and are individual instances of the Adobe solutions within those programs. Environments are used for a specific purpose such as authoring content or testing new developments. Cloud Manager's CI/CD pipelines facilitate the deployment of code to these environments from Git repositories.

If you recall the example of the theoretical WKND Travel and Adventure Enterprises, they are a tenant that focuses on travel-related media. They might have two programs. That is, one Sites program for its WKND Magazine division, and one Assets program for the WKND Media division. Each program would likely have a couple of environments such as one production environment which serves the actual traffic of the site and one development environment for testing new application code.

There are five different types of environments:

* **Production and Stage** - The production and staging environments are available as a pair and are used for production and testing purposes, respectively.
* **Development** - A development environment can be created for development and testing purposes and can be associated with non-production pipelines only.
* **Rapid Development** - A rapid development environment (RDE) lets a developer deploy and review changes swiftly. It minimizes the amount of time to test features that are proven to work in a local development environment.
* **Specialized Testing Environment** - Provides a dedicated space to validate features under near-production conditions, ideal for stress testing and advanced pre-deployment checks.

For the purposes of this onboarding journey, to get you started with a minimal, you create a development environment that you can use to explore AEM as a Cloud Service's capabilities.

## Create an environment {#creating-environments}

>[!NOTE]
>
>The system records the user who creates an environment as its creator. Because deleted users can sometimes be restored, choose the environment creator carefully.

**To create an environment:**

1. Log on to Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Select the program for which you want to add an environment.

1. To add an environment, from the **Program Overview** page, on the **Environments** card, select the **Add Environment** option.

   ![Environments card](/help/implementing/cloud-manager/assets/no-environments.png)

   * The **Add Environment** option is also available on the **Environments** tab.

     ![Environments tab](/help/implementing/cloud-manager/assets/environments-tab.png)

   * The **Add Environment** option may be disabled due to lack of permissions or depending on the licensed resources.
   
1. In the **Add environment** dialog box, do the following:
   
   * Select an **Environment type**.
     * The number of available/used environments is displayed in parentheses behind the Development environment type.
   * Provide an **Environment name**.
   * Provide an **Environment description**.
   * Select a **Cloud Region**.

   ![Add environment dialog](/help/implementing/cloud-manager/assets/add-environment2.png)

1. Click **Save** to add the specified environment.

Once the environment is available, members of your organization assigned to the **Developer** product profile can log in to Cloud Manager and manage Cloud Manager Git repositories.

## What's next {#whats-next}

Now that you have read this part of the onboarding journey, you should:

* Understand what an environment is.
* Know the difference between the different environments.
* Be able to create your own environment.

Your team can now access the cloud resources that you created. As the system administrator, you must first assign your team members to product profiles in AEM as a Cloud Service from the Adobe Admin Console so they can access those resources.

Therefore, you should continue your onboarding journey by next reviewing the document [Assigning Team Members to AEM as a Cloud Service Product Profiles](assign-profiles-aem.md). In that document, you learn how to grant your team members rights to your new environments.

## Additional resources {#additional-resources}

The following are additional, optional resources if you would like to go beyond the content of the onboarding journey.

* [Managing Environments](/help/implementing/cloud-manager/manage-environments.md) - Learn about the types of environments that you can create and how to create them for your Cloud Manager project
* [Using Adobe Cloud Manager - Environments](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/cloud-manager/environments) - Cloud Manager environments are composed of AEM authoring, publishing, and Dispatcher services. Learn how different environments support roles and can be engaged using different CI/CD pipelines.
* [Rapid Development Environments](/help/implementing/developing/introduction/rapid-development-environments.md) - See this documentation for details about how to use an RDE
<!-- ERROR: Not Found (HTTP error 404) FIND AN ALTERNATE RESOURCE? * [AEM Champion Tips and Tricks - Cloud Manager Environment Types](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/expert-resources/aem-champions/environment-types.md) - Watch this video for an overview of Cloud Manager environment types from an AEM champion. -->

