---
title: AEM as a Cloud Service on Unified Shell
description: Learn about the benefits of AEM as a Cloud Service on Unified Shell
exl-id: ea739307-dc99-4621-a239-dbe60ab6b52e
feature: Release Information
role: Admin
---
# AEM as a Cloud Service on Unified Shell {#aem-as-a-cloud-service-on-unified-shell}

## Overview {#overview}

AEM as a Cloud Service (Author Service) is integrated with Unified Shell to improve the user experience and unify it with all the other Experience Cloud applications. The impact of this integration can be seen in the top-header of the application as shown below.

![image](/help/overview/assets/unifiedshell_header.png)

The benefits of this are:

* Single Sign-on across all Experience Cloud applications
* Easy switching between organizations or switching to a different application
* Improved product help
* Easy in-product feedback button to report issues or share ideas with Adobe
* Access to global product announcements and notifications in addition to notifications specific to AEM as a Cloud Service

## Disabling Unified Shell {#disabling-unified-shell}

Out of the box, AEM as a Cloud Service has unified shell enabled. However, in case the top-header has been customized, it is recommended to disable unified shell to avoid any issues with the customizations. To disable unified shell, follow the steps below:

>[!NOTE]
>Unified Shell can be disabled only by an account with administrative privileges.

1. Click **Tools > Cloud Services**. 

   An admin user sees the Unified Shell Configuration card as shown below:

   ![image](/help/overview/assets/unifiedshell2.png)

1. Click **Unified Shell Configuration**. Then, deselect the checkbox shown below to disable Unified Shell:

   ![image](/help/overview/assets/unifiedshell3.png)

>[!NOTE]
>
>Unified Shell can also be disabled from your project code. See [Structure of the AEM UI - Unified Shell](/help/implementing/developing/introduction/ui-structure.md#unified-shell).

## Changing to Dark Theme {#changing-to-dark-theme}

To change to the dark theme, click your profile icon. This action displays a popover as shown below. You can use the toggle to switch to a dark theme for the Unified Shell.

>[!INFO]
>
>The dark theme applies to Unified Shell (the top bar) only.

![image](/help/overview/assets/unifiedshell4.png)

## Identifying the AEM as a Cloud Service environment {#identify-aemaacs-environment}

AEM as a Cloud Service provides three types of environments: Production, Stage, and Development. See [Environment Types](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/manage-environments.html) for more details. With this integration with Unified Shell, the type of environment that the user is logged into on the Author service is displayed on the top-header via a label as shown below.

![image](/help/overview/assets/unifiedshell_header_label.png)

## Accessing the AEM Inbox {#accessing-the-aem-inbox}

The AEM Inbox can be accessed by clicking the bell icon in the unified shell. 

>[!INFO]
>
> The number indicated on the bell icon includes unread notifications across all solutions within that IMS Org and tasks listed in the AEM Inbox.

![image](/help/overview/assets/unifiedshell5.png)

Click the Inbox button in the popover so you can go to your AEM Inbox:

![image](/help/overview/assets/unifiedshell6.png)

