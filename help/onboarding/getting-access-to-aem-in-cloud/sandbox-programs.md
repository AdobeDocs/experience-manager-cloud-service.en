---
title: Sandbox Programs - Cloud Service
description: Sandbox Programs - Cloud Service
---

# Sandbox Programs {#sandbox-programs}

## Introduction {#introduction}

A Sandbox program is one of the two types of programs available in AEM Cloud Service, the other being a Regular program. 

A Sandbox is typically created to serve the purposes of training, running demos, enablement, or Proof of Concept (POC)s. They are not meant to carry live traffic. They are not subject to the [AEM as a Cloud Service Commitments](https://www.adobe.com/legal/service-commitments.html).

The environments created in a Sandbox are not configured for auto-scaling. Therefore, they are not suitable for performance or load testing.

Sandbox programs include Sites and Assets and are auto-populated with a Git repository, a Development environment, and a non-production pipeline.  The Git repository is populated with a sample project based on the AEM Project archetype.

Refer to [Understanding Programs and Program Types](/help/onboarding/getting-access-to-aem-in-cloud/understand-program-types.md) to learn more about the Program Types.

### Attributes of Sandbox Programs {#attributes-sandbox}

Sandbox Programs have the following attributes:

1. **Program Creation:** The Sandbox program creation includes automatic:
   * setup of project with sample code and content
   * creation of development environment
   * creation of non-production pipeline deploying to development environment (master branch deploying to development environment)
 
1. **Solutions:** Sandbox programs include AEM Sites and Assets.

1. **AEM Updates:** AEM updates can be applied manually to environments in a Sandbox program, and are not automatically pushed.

1. **Hibernation:** Environments in a Sandbox program are automatically hibernated if no activity is detected for a certain period of time. Hibernated environments can be manually de-hibernated.

### Creating a Sandbox Program {#creating-sandbox-program}

A program creation wizard lets you create a Sandbox Program.

To learn how to create a Sandbox Program, refer to [Creating a Sandbox Program](/help/onboarding/getting-access-to-aem-in-cloud/creating-a-program.md#create-sandbox-program) for more details.

### Creating Sandbox Environments {#creating-sandbox-environments}

Sandbox Programs are delivered to a development environment at the time of program creation in an auto-created manner. The development environment includes an author and a publish tier by default.

The Production-Stage environment set can be manually added to the Sandbox Program, when the user is ready to setup a production pipeline. 

To learn how to manually create an environment, refer to [Adding Environment](/help/implementing/cloud-manager/manage-environments.md) for more details.

### Deleting Sandbox Environments {#deleting-sandbox-environments}

User with the requisite permissions can delete a Development or Production/Stage environment  or sets. 

To delete an environment, refer to [Deleting Environment](/help/implementing/cloud-manager/manage-environments.md#deleting-environment) for more details.


## Hibernating and De-hibernating Sandbox Environments {#hibernating-introduction}

Sandbox Program environments enter a *hibernation mode* if no activity is detected for a certain period of time.

>[!NOTE]
>Hibernation is unique to Sandbox Program environments. Regular program environments do not hibernate.

### Hibernation {#hibernation-introduction}

Hibernation can occur either automatically or manually. It may take up to a few minutes for Sandbox Program environments to enter a *hibernation mode*. Data is preserved during hibernation.

Hibernation is categorized as:

* **Automatic**  Sandbox Program environments are automatically hibernated after eight hours of inactivity, meaning that neither the author nor publish services receive requests.

* **Manual**: As a user you may manually hibernate a Sandbox Program environment, although there is no requirement to do so since hibernation will occur automatically after a certain period (eight hours) of inactivity.

>[!CAUTION]
>In the latest release, linking to the Developer Console directly from Cloud Manager will not give you the option to hibernate a Sandbox Program environment. The workaround is once at the Developer Console, add the following pattern to the end of the url `#release-cm-p1234-e5678 where 1234` 1234 is your *Program ID* and 5678 is your *Environment ID*.

#### Using Manual Hibernation {#using-manual-hibernation}

You can manually hibernate your Sandbox Program from the Developer Console in two different ways, using:

* Environment detail screen 
* Environment listing screen 

>[!NOTE]
>Access to Developer Console for a Sandbox Program is available to any user of Cloud Manager.

Follow the steps below to manually hibernate your Sandbox Program environments:

1. Navigate to the **Developer Console**. 
Refer to [Accessing Developer Console](/help/implementing/cloud-manager/manage-environments.md#accessing-developer-console) to learn how to access the **Developer Console** from the **Environments** card.
   >[!IMPORTANT]
   >Linking to the **Developer Console** directly from Cloud Manager will not give you the option to hibernate a Sandbox Program environment. The workaround is once at the Developer Console, add the following pattern to the end of the url `#release-cm-p1234-e5678 where 1234` 1234 is your *Program ID* and 5678 is your *Environment ID*.  

1. Click **Hibernate**, as shown in the figure below:

   ![](assets/hibernate-1.png)

   Or,

   Click the **Environments** link in top left to view the environments listing and then click **Hibernate**, as shown in the figure below:

   ![](assets/hibernate-1b.png)

1. Click **Hibernate** to confirm the step.

   ![](assets/hibernate-2.png)

1. When the hibernation is successful, you will see the hibernation process complete notification for your environment in the **Developer Console** screen.

   ![](assets/hibernate-4.png)


### De-hibernation {#de-hibernation-introduction}

1. Navigate to the **Developer Console**. 
Refer to [Accessing Developer Console](/help/implementing/cloud-manager/manage-environments.md#accessing-developer-console) to learn how to access the **Developer Console** from the **Environments** card.

   >[!IMPORTANT]
   >Linking to the **Developer Console** directly from Cloud Manager will not give you the option to de-hibernate a Sandbox Program environment. The workaround is once at the Developer Console, add the following pattern to the end of the url `#release-cm-p1234-e5678 where 1234` 1234 is your *Program ID* and 5678 is your *Environment ID*.

   >[!NOTE]
   >Alternatively, you can navigate to the **Developer Console** to de-hibernate by trying to access the author or publish service of an already hibernated environment; in that case, a landing page will appear with a link to the Developer Console. See the Accessing a Hibernated Environment section below.

   >[!IMPORTANT]
   >Access to the Developer Console is defined by the **Cloud Manager - Developer Role** in the **Admin Console**. A user with a developer role permission can de-hibernate a Sandbox Program environment.

1. Click on **De-hibernate**, as shown in the figure below:

    ![](assets/de-hibernation-img1.png)

    Or,

    Click the **Environments** link in top left to view the environments listing and then click **De-hibernate**, as shown in the figure below
 
    ![](assets/de-hibernate-1b.png)


1. Click **De Hibernate** to confirm the step.

   ![](assets/de-hibernation-img2.png)

1. You will receive the notification that the de-hibernation process has started and you will be updated with the progress.
   
   ![](assets/de-hibernation-img3.png)
   
1. Once the process completes, the Sandbox Program environment is active again.
 
   ![](assets/de-hibernation-img4.png)

#### Permissions to De-hibernate {#permissions-de-hibernate}

Any user with a product profile giving them access to AEM as a Cloud Service should be able to access the **Developer Console**, allowing them to de-hibernate the environment. 

#### Accessing a Hibernated Environment {#accessing-hibernated-environment}

When making any browser requests against either the author or publish tier of a hibernated environment, the user will encounter a landing page describing the hibernated status of the environment, as shown in the figure below:

![](assets/de-hibernation-img5.png)

### Important Considerations {#important-considerations}

Few key considerations related to hibernated and de-hibernated environments are:

* A user may use a pipeline to deploy custom code to hibernated environments. The environment will remain hibernated and the new code will appear in the environment once de-hibernated.

* AEM upgrades can be applied to hibernated environments, which customers can manually trigger from Cloud Manager. The environment will remain hibernated and the new release will appear in the environment once de-hibernated.

>[!NOTE]
>Currently, Cloud Manager does not indicate whether an environment is hibernated.

## AEM Updates to Sandbox Environments {#aem-updates-sandbox}

Refer to [AEM version updates](/help/implementing/deploying/aem-version-updates.md) for more details.

A user can manually apply AEM updates to the environments in a Sandbox Program.

Refer to [Updating Environment](/help/implementing/cloud-manager/manage-environments.md#updating-dev-environment) to learn how to update an environment.

>[!NOTE]
>* A manual update can only be run when the targeted environment has a properly configured pipeline. 
>* A manual update to either *Production* or *Stage* environment will automatically update the other. The Production+Stage environment set must be on the same AEM release. 





