---
title: Creating Production Programs 
description: Learn how to use Cloud Manager to create your own production program to host live traffic.
exl-id: 4ccefb80-de77-4998-8a9d-e68d29772bb4
---

# Creating Production Programs {#create-production-program}

A production program is intended for a user who is familiar with AEM and Cloud Manager and is ready to start writing, building, and testing code with the objective of deploying it to host live traffic.

Learn more about program types in the document [Understanding Program and Program Types.](program-types.md)

## Video Tutorials {#video-tutorials}

You can watch these two tutorial videos to learn how to create a program in Cloud Manager or [follow our documented instructions.](#create)

>[!VIDEO](https://video.tv.adobe.com/v/334953)

>[!VIDEO](https://video.tv.adobe.com/v/334954)

## Create a Production Program {#create}

Follow these steps to create a production program.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click on **Add Program** from the top-right corner of the screen.

   ![Cloud manager landing page](assets/first_timelogin1.png) 

1. Select **Set up for Production** in the Create Program wizard to create a production program. You can accept the default program name or edit it before clicking **Continue**.

   ![Creating program wizard](assets/create-prod1.png)

1. On the **Solutions &amp; Add-ons** tab, select the solutions to include in the program.

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

## Access Your Program {#acessing}

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
