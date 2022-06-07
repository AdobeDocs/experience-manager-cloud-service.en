---
title: Integrate an Adaptive Form with Microsoft Power Automate
description: Integrate an Adaptive Form with Microsoft Power Automate.
hide: yes
hidefromtoc: yes
---

# Integrate an Adaptive Form with Microsoft Power Automate {#architecture}

You can configure an Adaptive Form to run a Microsoft® Power Automate Cloud Flow on submission. The configured Adaptive Form sends captured data, attachments, and Document Of Record to Power Automate Cloud Flow for processing. It helps you build custom data capture experience while harnessing the power of Microsoft® Power Automate to build business logics around captured data and automate customer workflows. Here are a few examples of what you can do after integrating an Adaptive Form with Microsoft Power Automate: 

* Use Adaptive Forms data in a Power Automate business processes
* Use Power Automate to send captured data to more than 500 data sources or any publicly available API  
* Peform complex calculations on captured data
* Save Adaptive Forms data to storage systems at a predefined schedule

Adaptive Forms editor provides the **Invoke a Microsoft Power Automate flow** submit action to send adaptive forms data, attachments, and Document Of Record are sent to Power Automate Cloud Flow.

## Prerequistes

* Microsoft Power Automate license: A separate Microsoft license is available for Experience Manager Forms customer to use MS Power Automate Flow.
* Microsoft Power Automate Application 
* Microsoft Power Automate flow to accept Adaptive Form submit data.
* Create a Power Automate user with Admin privileges
* Create Experience Manager users with Forms Author and Forms Admin privileges

## Create Microsoft Power Automate Application

1. Login to [Azure Portal](https://portal.azure.com/).
1. Select [!UICONTROL Azure Active Directory] from the left navigation.
1. On the Default directory page, select [!UICONTROL App registrations] from the left panel.
1. On the App registrations page, click New Registrations.
1. Specify Name, Supported account types, and Redirect URI on the page. In the Redirect URI, specify the following and click Save.
    * `https://[Forms as a Cloud Service Server]/libs/fd/powerautomate/content/dataverse/config.html`
    * `https://[Forms as a Cloud Service Server]/libs/fd/powerautomate/content/dataverse/config.html`

    ![Register a Power Automate Application](assets/power-automate-application.png)

    >[!NOTE]
    >You can also specify additonal Redirect URIs, if required, from the Authentication page.
    >

1. On the Authentication page, enable the following options, and click Save.

    * Access tokens (used for implicit flows)
    * ID tokens (used for implicit and hybrid flows)

1. On the API permissions page, click Add a permission. 
1. Under Microsft APIs, select the Flow Service, and select the following permissions. 
    * Flows.Manage.All
    * Flows.Read.All

    Click Add permissions to save the permissions.
1. On the API permissions page, click Add a permission. Select APIs my organization uses and search `DataVerse`.
1. Enable user_impersonation and Click Add permissions.
1. On the Certificates & secrets page, click New client secret. On the Add a Client Secret screen, provide a description and time peiod for the secret to expire, and click Add. A secret string is generated. 


 
