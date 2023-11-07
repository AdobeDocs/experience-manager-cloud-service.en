---
title: Creating Production Programs 
description: Learn how to use Cloud Manager to create your own production program to host live traffic.
exl-id: 4ccefb80-de77-4998-8a9d-e68d29772bb4
---

# Creating Production Programs {#create-production-program}

A production program is intended for a user who is familiar with AEM and Cloud Manager and is ready to start writing, building, and testing code with the objective of deploying it to host live traffic.

Learn more about program types in the document [Understanding Program and Program Types.](program-types.md)

## Create a Production Program {#create}

Follow these steps to create a production program.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click on **Add Program** from the top-right corner of the screen.

   ![Cloud manager landing page](assets/log-in.png) 

1. Select **Set up for Production** in the Create Program wizard to create a production program and provide a program name.

   ![Creating program wizard](assets/create-production-program.png)

1. Optionally, you can add an image to the program by dragging and dropping an image file to the **Add a program image** target or clicking it to select an image from a file browser. Tap or click **Continue**.

1. If you have the necessary entitlements, the **Security** tab will be shown and provide the option to activate **HIPAA** and/or **WAF-DDOS Protection** for your production program. If required for the program you are creating, check the applicable option(s) and then tap or click **Continue**.

   * HIPAA can not be enabled or disabled after program creation.
      * [Learn more](https://www.adobe.com/go/hipaa-ready) about Adobe's HIPAA ready solution implementation.
   * Once activated, WAF-DDOS protection can then be configured by setting up a [non-production pipeline.](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md)
   
   {{waf-limited-release}}

   ![Security options](assets/create-production-program-security.png)

1. On the **Solutions &amp; Add-ons** tab, select the solutions to include in the program.

   * If you are not sure if you need one or more programs for the various solutions you have available, select the one most of interest to you. You can activate additional solutions by [editing the program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md) later. See the [Introduction to Production Programs document](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-production-programs.md) for more program setup recommendations.
   * If you selected the **Enable Enhanced Security** previously, you are allowed to select only as many solutions for which HIPAA entitlements are available.

   ![Select solutions](assets/setup-prod-select.png)

1. Click on the chevron before the solution names to reveal optional add-ons such as selecting the **Commerce** add-on option under **Sites**.

   ![Select add-ons](assets/setup-prod-commerce.png)

1. With your solutions and add-ons selected, click **Continue**.

1. On the **Go-Live Date** tab, enter the date you plan your production program to go live.

   ![Define planned go-live date](assets/setup-go-live.png)

   * This date can be edited at any time.
   * This date is for informational use only and triggers the Go Live widget on the program overview page to provide in-product links to AEM as a Cloud Service best practice documentation in a timely manner to align with your journey culminating in a successful and smooth Go Live experience.

1. Click **Create**.

Your program is created by Cloud Manager and is displayed and selectable on the landing page.

![Cloud manager overview](assets/navigate-cm.png)

## Access Your Program {#accessing}

1. Once you see your program card on the landing page, select the ellipsis button to view the menu options available to you.

   ![Program overview](assets/program-overview.png)

1. Select **Program Overview** to navigate to the Cloud Manager's **Overview** page.  

1. The main call-to-action card on the overview page will guide you through creating an environment, a non-production pipeline, and finally a production pipeline.

   ![Program overview](assets/set-up-prod5.png)

If at any time you need to switch to another program or return to the overview page to create another program, click on your program name in the top-left of the screen to reveal the **Navigate to** option.

![Navigate to](assets/create-program-a1.png)

>[!NOTE]
>
>Unlike a [sandbox program,](introduction-sandbox-programs.md#auto-creation) a production program will require the user in the appropriate Cloud Manager role to create the project and add an environment through the self-service UI.
