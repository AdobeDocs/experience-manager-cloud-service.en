---
title: Sandbox Programs - Cloud Service
description: Sandbox Programs - Cloud Service
---

# Sandbox Programs {#sandbox-programs}

## Introduction {#introduction}

A Sandbox program is one of the two types of programs available in AEM Cloud Service, the other being a Regular program. 

A Sandbox is typically created to serve the purposes of training, running demos, enablement, or POCs. They are not meant to carry live traffic.

Sandbox programs include Sites and Assets and will be delivered auto-populated with a Git branch that includes sample code, a Development environment, and a non-production pipeline.

For more information about program types, refer to [Understanding Programs and Program Types](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/onboarding/getting-access/understand-program-types.html).

### Attributes of Sandbox Programs {#attributes-sandbox}

Sandbox Programs have the following attributes:

1. **Program creation:** The Sandbox program creation includes automatic:
   * setup of project with sample code and content
   * creation of development environment
   * creation of non-production pipeline deploying to development environment (master branch deploying to Development environment)
 
1. **Solutions included:** Sandbox programs include Sites and Assets.

1. **AEM updates:** AEM updates can be applied manually to environments in a Sandbox program, and are not automatically pushed.

1. **Hibernation:** Environments in a Sandbox program will be automatically hibernated if no activity is detected for a certain period of time. Hibernated environments can be manually de-hibernated.

### Creating a Sandbox program {#creating-sandbox-program}

A program creation wizard will ask the user to submit details.

For information about how to create a sandbox program, refer to [Creating a Sandbox Program](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/onboarding/getting-access/creating-a-program.html#create-demo-program).

### Creating Sandbox Environments {#creating-sandbox-environments}

Sandbox programs will be delivered a development environment at the time of program creation in an auto-created manner. The development environment comes with an author and a publish tier by default.

The Production-Stage environment set can be manually added to the Sandbox program, when the user is ready to setup a production pipeline. 

For information on how to manually create an environment, refer to [Adding Environments](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html#adding-environments).

### Deleting Sandbox Environments  {#deleting-sandbox-environments}

User with the requisite permissions will be able to delete a Development or Production/Stage environment/sets. 

For information about how to delete an environment, refer to [Deleting Environments](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/using-cloud-manager/manage-environments.html#deleting-environment).


## Hibernating and De-hibernating Sandbox Environments {#hibernating-introduction}

Sandbox program environments will enter a *hibernation mode* after a period of inactivity. 

>[!NOTE]
>Hibernation is unique to sandbox program environments. Regular program environments will not be hibernated.

### Hibernation {#hibernation-introduction}

Hibernation can occur either automatically or manually. It may take up to a few minutes for an environment to be hibernated. Data is preserved during hibernation.

Hibernation is categorized as:

* **Automatic**  Sandbox program environments are automatically hibernated after eight hours of inactivity, meaning that neither the author or publish services receive request.

* **Manual**: Customers may manually hibernate a sandbox program environment, although there is no requirement to do so since hibernation will occur automatically after a period of inactivity.

#### Using Manual Hibernation {#using-manual-hibernation}


Manual hibernation can be accomplished from either of two screens in the developer console. 

Follow the steps below to manually hibernate your program environments:

1. Navigate to the Developer Console.
1. Click Hibernate
1. Click Hibernate to confirm.
1. When the hibernation is successful, you will see the following screen.
1. At the environment listings screen, which is illustrated below and which is accessible by clicking the Environments link from the environment detail screen, the Hibernate button can be clicked in the row of the intended environment. A confirmation screen will then appear.

### De-hibernation {#de-hibernation-introduction}

>[!IMPORTANT]
>Access to the Developer Console is defined by the "Cloud Manager - Developer Role" in the Admin Console. With that permission, a user can de-hibernate an environment.

### Accessing a Hibernated Environment {#accessing-hibernated-environment}

When making any browser requests against either the author or publish tier of a hibernated environment, the user will encounter a landing page describing the hibernated status of the environment, as illustrated below:

A user with the "Cloud Manager - Developer Role" can click on the Developer Console button to access the developer console and de-hibernate the environment. Information about setting roles can be found in Cloud Manager Documentation.

If a user in an organization cannot click the Developer Console button to be brought to the Developer Console, it's likely that they need to be given the "Cloud Manager - Developer Role".




## AEM updates to Sandbox environments {#aem-updates-sandbox}


Refer to [AEM version updates](https://docs.adobe.com/content/help/en/experience-manager-cloud-service/implementing/deploying/overview.html#version-updates).

User can manually apply AEM updates to the environments in a Sandbox program (see figure below). This can be done when the status displayed is UPDATE AVAILABLE. Update option will be available from the dropdown menu on the Environments Card. It can also be selected from the Manage menu from the ENVIRONMENTS screen. 

>[!NOTE]
>A non-production pipeline deploying to the development environment of interest must be configured in order for a manual update pipeline to be initiated. 

>[!NOTE]
>A production pipeline must be configured in order for a manual update pipeline to Production+Stage environment set to be initiated. 

>[!NOTE] 
>Manual update to either Production or Stage environment will automatically update the other. The Production+Stage environment set must be on the same AEM release. 





