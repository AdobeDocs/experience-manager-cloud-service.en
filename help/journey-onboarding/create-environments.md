---
title: Create Environments
description: Lean how to use Cloud Manager to create your first environments.
role: Admin, User, Developer
---

# Create Environments {#create-environments}

Lean how to use Cloud Manager to create your first environments.

## Objective {#objective}

* Understand what an environment is
* Know the difference between the different environments
* Be able to create your own environment

## What is an environment? {#environments}

Environments sit below programs within the hierarchy of Cloud Manager. While programs allow you to organize your solution and grant access to particular team members to those programs, environments belong to specific programs and are individual instances of the Adobe solutions within those programs used for a specific purpose such as authoring content or testing new developments.

If you recall the example of the theoretical WKND Travel and Adventure Enterprises, who is a tenant that focuses on travel-related media, they might have two programs: one Sites program for its WKND Magazine division and one Assets program for WKND Media division. Each program would likely have a couple of environments such as one production environment which serves the actual traffic of the site and one development environment for testing new application code.

There are three different types of environments:

* **Production and Stage** - The production and staging environments are available as a pair and are used for production and testing purposes, respectively.
* **Development** - A development environment can be created for development as well as testing purposes and can be associated with non-production pipelines only.

For the purposes of this onboarding journey, we will create a development environment.

## Create Environments {#create-environments}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click on the program for which you want to add an environment.

1. From the **Program Overview** page, click on **Add Environment** on the **Environments** card to add an environment.

   ![Environments card](/help/implementing/cloud-manager/assets/no-environments.png)

   * The **Add Environment** option is also available on the **Environments** tab.

     ![Environments tab](/help/implementing/cloud-manager/assets/environments-tab.png)

   * The **Add Environment** option may be disabled due to lack of permissions or depending on the licensed resources.
   
1. In the **Add environment** dialog that appears:
   
   * Select an **Environment type**.
     * The number of available/used environments is displayed in parenthesis behind the Development environment type.
   * Provide an **Environment name**.
   * Provide an **Environment description**.
   * Select a **Cloud Region**.

   ![Add environment dialog](/help/implementing/cloud-manager/assets/add-environment2.png)

1. Click **Save** to add the specified environment.

Once the environment is available, members of your organization assigned to the **Developer** product profile can login to Cloud Manager and manage Cloud Manager git repositories.

## What’s Next {#whats-next}

Now that your cloud resources have been created and are ready to be accessed by your team, as the system administrator you must assign your team members to AEM as a Cloud Service product profiles from Adobe Admin Console in order for them to access those resources.

You should continue your onboarding journey by next reviewing the document [Assigning Team Members to AEM as a Cloud Service Product Profiles](assign-profiles-aem.md) where you will learn how to grant your team members the rights they need to access your new environments.

## Additional Resources {#additional-resources}

Follow the additional resources to learn about:

* [Program types and adding a program](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/programs.html)
* [Environment types and adding an environment](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-manager/environments.html) 
* [Managing Cloud Manager Git](/help/implementing/cloud-manager/managing-code/accessing-repos.md)
* [Configuring access to AEM as a Cloud Service from Admin Console](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/accessing/overview.html#adobe-ims-users)