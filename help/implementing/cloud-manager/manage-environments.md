---
title: Managing Environments
description: Learn about the types of environments you can create and how to create them for your Cloud Manager project.
exl-id: 93fb216c-c4a7-481a-bad6-057ab3ef09d3
---
# Managing Environments {#managing-environments} 

Learn about the types of environments you can create and how to create them for your Cloud Manager project.

## Environment Types {#environment-types}

A user with the requisite permissions can create the following environment types (within the bounds of what is available to the specific tenant). 

* **Production and Stage** - The production and staging environments are available as a pair and are used for production and testing purposes, respectively.

* **Development** - A development environment can be created for development as well as testing purposes and can be associated with non-production pipelines only.
   
This table summarizes environment types and their attributes.

|Environment|Available on Author Tier?|Available on Publish Tier?|User-Creatable?|User-Deletable?|Pipeline that can be associated|
|--- |--- |--- |--- |---|---|
|Production |Yes |Yes, if Sites included |Yes |No|Production pipeline|
|Stage |Yes |Yes, if Sites included |Yes |No|Production pipeline|
|Development |Yes |Yes, if Sites included |Yes |Yes|Non-production pipeline|

>[!NOTE]
>
>Production and staging environments are only created as a pair. You can not create only a staging or only a production environment.

## Adding an Environment {#adding-environments}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click on the program for which you want to add an environment.

1. From the **Program Overview** page, click on **Add Environment** on the **Environments** card to add an environment.

   ![Environments card](assets/no-environments.png)

   * The **Add Environment** option is also available on the **Environments** tab.

     ![Environments tab](assets/environments-tab.png)

   * The **Add Environment** option may be disabled due to lack of permissions or depending on the licensed resources.
   
1. In the **Add environment** dialog that appears, select an **Environment type** and provide an **Environment name** and **Environment description**.

   ![](assets/add-environment2.png)

   >[!NOTE]
   >When creating an environment, one or more *integrations* are created in Adobe I/O. These are visible to customer users who have access to the Adobe I/O Console and must not be deleted. This is disclaimed in the description in the Adobe I/O Console.

   ![](assets/add-environment-image1.png)

1. Click **Save** to add an environment with the populated criteria.  Now the *Overview* screen  displays the card from where you can set up  your pipeline.

   >[!NOTE]
   >In case, you have not yet set up your non-production pipeline, the *Overview* screen  displays the card from where you can create your non-production pipeline.

## Environment Details {#viewing-environment}

The **Environments** card on the Overview page lists up to three environments. 

1. Select the **Show All** button to navigate to the **Environment** summary page to view a table with a complete list of environments.

   ![](/help/implementing/cloud-manager/assets/environment-showall.png)

1. The **Environments** page displays the list of all the existing environments.

   ![](assets/environment-view-2.png)

1. Select any one of the environments from the list to view the environment details.
   
   ![](assets/environ-preview1.png)


### Accessing Preview Service {#access-preview-service}

Preview Service feature delivers an additional Preview (publish) Service to each AEM as a Cloud Service environment via Cloud Manager. 

Preview a website's final experience before it reaches the publish environment and is available publicly. A few pointers before you you can see and use Preview Service:

1. **AEM Version**: Your environment must be on AEM version `2021.05.5368.20210529T101701Z` or higher. Make sure an update pipeline has successfully run on your environment to accomplish this. 

1. **Default IP Allow List Lock**: Upon creation, the Preview Service will have a default IP Allow List applied to it, labeled `Preview Default [Env ID]`.

   >[!NOTE]
   >Upon first creation, you must actively unapply the default IP Allow List from the Preview Service in your environment in order to enable access.

   A user with requisite permissions must do one of the following in order to *unlock* access to Preview Service and provide the desired access:

   * Create an appropriate IP Allow List and apply it to the Preview Service. Follow this immediately by unapplying `Preview Default [Env ID] IP Allow List` from the Preview Service. Refer to [UnApplying an IP Allow List](/help/implementing/cloud-manager/ip-allow-lists/unapply-ip-allow-list.md) for more details.

      *OR*,

   * Use the update IP Allow List workflow to remove the default IP and add IP(s) as appropriate. Refer to [Viewing and Updating an IP Allow List](/help/implementing/cloud-manager/ip-allow-lists/view-update-ip-allow-list.md) to learn more. 

      >[!NOTE]
      >The above steps must be done in advance of sharing the preview service URL with any of your teams in order to ensure the appropriate members of your team are able to access the preview URL.

      Once access to preview service is unlocked, the lock icon (as shown in the figure below) will no longer be displayed.

      ![](/help/implementing/cloud-manager/assets/preview-service1.png)

1. **Publish Content to Preview**: You can publish content to the Preview Service by using the Manage Publication UI inside AEM. Refer to [Previewing Content](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/sites/authoring/fundamentals/previewing-content.html?lang=en) for more details.

## Updating Environment {#updating-dev-environment}

Updates of Stage and Production environments are automatically managed by Adobe. 

Updates to Development environments are managed by users of the program. When an environment is not running the latest publicly available AEM release, the status on Environments Card on the Home Screen will show **UPDATE AVAILABLE**.

![](assets/environ-update.png)


The **Update** option is available from the **Environments** Card. 
This option is also available, if you click on **Details** from the **Environments** card. The **Environments** page opens and once you select the Development environment, click on **...** and select **Update**, as shown in the figure below:

![](assets/environ-update2.png)

Selecting this option will allow a Deployment Manager to update the pipeline associated with this environment to the latest release and then execute the pipeline. 

If the pipeline has already been updated, the user is prompted to execute the pipeline.

## Deleting Environment {#deleting-environment}

User with the requisite permissions will be able to delete a Development environment. 

The **Delete** option is available from the dropdown menu in the **Environments** Card. Click on **...** for a Development environment you want to delete.

![](assets/environ-delete.png)

The delete option is also available, if you click on **Details** from the **Environments** card. The **Environments** page opens and once you select the Development environment, click on **...** and select **Delete**, as shown in the figure below:

![](assets/environ-delete2.png)


>[!NOTE]
>This feature is not available for Production/Stage environment set in a Production program set up for production purposes. The feature is, however, available for Production/Stage environments in a Sandbox program.

## Managing Access {#managing-access}

Select **Manage Access** from the dropdown menu in the **Environments** Card. You can navigate to the author instance directly and manage access for your environment.

![](assets/environ-access.png)


## Accessing Developer Console {#accessing-developer-console}

Select **Developer Console** from the dropdown menu in the **Environments** Card. This will open a new tab in your browser with the login page to **Developer Console**. 

Only a user in the Developer role will have access to **Developer Console**. The exception being for Sandbox Programs, where any user with access to the Cloud Manager Sandbox Program will have access to **Developer Console**.

Refer to [Hibernating and De-hibernating Sandbox Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/getting-access/cloud-service-programs/sandbox-programs.html#hibernating-introduction) for more details.


![](assets/environ-devconsole.png)

This option is also available, if you click on **Details** from the **Environments** card. The **Environments** page opens and once you select an environment, click on **...** and select **Developer Console**.

## Login Locally {#login-locally}

Select **Local Login** from the dropdown menu in the **Environments** Card to login locally to Adobe Experience Manager. 

![](assets/environ-login-locally.png)

Additionally, you can login locally from the **Environments** summary page.

![](assets/environ-login-locally-2.png)


## Managing Custom Domain Names {#manage-cdn}

Navigate to the **Environments** details page from the Environments Summary page. 

>[!NOTE]
>Custom Domain Names are now supported in Cloud Manager for Sites programs for both Publish and Preview Services. Each Cloud Manager Environment can host up to a maximum of 250 custom domains per environment. 

The following actions can be performed on the Publish service for your environment  as described below: 

1. [Adding a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md)

1. [Viewing and Updating a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/view-update-replace-custom-domain-name.md)

1. [Deleting a Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/delete-custom-domain-name.md)

1. [Checking Status of Custom Domain Name](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md#pre-existing-cdn) or an [SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/check-status-ssl-certificate.md#pre-existing-cdn).

1. [Checking Status of an IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/check-ip-allow-list-status.md#pre-existing-cdn)


## Managing IP Allow Lists {#manage-ip-allow-lists} 

Navigate to the Environment details page from the Environments Summary page. You can perform the following actions on the Publish and/or Author service(s) for your environment here.

>[!NOTE]
>IP Allow List feature is now supported in Cloud Manager for Author, Publish, and Preview Services (available in Sites programs).

### Applying an IP Allow List {#apply-ip-allow-list}

Applying an IP Allow List is the process by which all IP ranges included in the definition of the Allow-List are associated with an Author or Publish service in an environment. A user in the Business Owner or Deployment Manager role must be logged in in order to be able to apply an IP Allow List.

>[!NOTE]
>The IP Allow List must exist in Cloud Manager in order to apply it to an environment-service. To learn more about IP Allow Lists in Cloud Manager navigate to [Introduction to IP Allow Lists in Cloud Manager](/help/implementing/cloud-manager/ip-allow-lists/introduction.md).

Follow the steps below to apply an IP Allow List:

   1. Navigate to the specific environment from the **Environments** details page and navigate to the **IP Allow Lists** table.
   1. Use the input fields at the top of the IP Allow List table to select the IP Allow List and the Author or Publish service you wish to apply it to. 
   1. Click on **Apply** and confirm your submission.

### Unapplying an IP Allow List {#unapply-ip-allow-list}

Unapplying an IP Allow List is the process by which all IP ranges included in the definition of the Allow  List are disassociated from an Author or Publisher service in an environment. A user in the Business Owner or Deployment Manager role must be logged in in order to be able to Unapply an IP Allow List.

Follow the steps below to unapply an IP Allow List:

1. Navigate to the specific **Environments** details page from Environments screen and navigate to the **IP Allow Lists** table.
1. Identify the row where the IP Allow List rule you wish to unapply is listed.
1. Select the **...** menu from the far right end of the row.
1. Select the **Unapply** option and confirm your submission.
