---
title: Navigating the Cloud Manager UI
description: Learn how the Cloud Manager UI is organized and how to navigate to manage your programs and environments.
exl-id: 3f3d7631-2bc9-440b-9888-50f6529bcd42
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Navigating the Cloud Manger UI {#navigation}

Learn how the Cloud Manager UI is organized and how to navigate to manage your programs and environments.

The Cloud manage UI is primarily composed of two graphical interfaces:

* [The My Programs console](#my-programs-console) where you can view and manage all of your programs.
* [The Program Overview window](#program-overview) where you can see the detail of and manage an individual program.

>[!TIP]
>
>Also check out the [onboarding documentation journey](/help/journey-onboarding/overview.md) for a complete overview of how to get up-and-running with AEM as a Cloud Service using Cloud Manager.

## My Programs Console {#my-programs-console}

When you log into Cloud Manager at at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization, you arrive at the **My Programs** console.

![My Programs console](assets/my-programs-console.png)

The My Programs console provides an overview of all programs to which you have access in the selected organization. It is made up of several parts.

1. [Toolbars](#toolbars-my-programs-toolbars) for organization selection, alerts, and account settings
1. [Tabs] that default on the home view with an overview of all programs and giving access to your [License Dashboard.](/help/implementing/cloud-manager/license-dashboard.md)
   * Note that the tabs default to closed and can be revealed using the hamburger menu in the [Cloud Manager header.](#cloud-manager-header)
1. [Statistics and call-to-action](#statistics) for an overview of your recent activity
1. [Quick links](#quick-links-section) to easily access related resources

>[!TIP]
>
>Please see the document [Programs and Program Types](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md) for details on programs.

### Toolbars {#my-programs-toolbars}

There are two toolbars on top of each other. 

#### Cloud Manager Header {#cloud-manager-header}

The first is the Cloud Manager header, which is persistent as you navigate Cloud Manager. It is an anchor that gives you access to settings and information that apply across Cloud Manager programs.

![The Experience Cloud header](assets/experience-cloud-header.png)

1. The hamburger menu giving access to tabs that can take you to specific parts of a in individual program or switch between the [License Dashboard](/help/implementing/cloud-manager/license-dashboard.md) and the **[My Programs](#my-programs-console)** console depending on context.
1. The Cloud Manager button will take you back to the My Programs console of Cloud Manager no matter where you are in Cloud Manager.
1. Tap or click the Feedback button to provide feedback to Adobe about Cloud Manager.
1. The organization selector displays the organization you are currently signed into (in this example, Foundation Internal). Tap or click to switch to another organization if your Adobe ID is associated with multiple.
1. Tapping or clicking the solutions switcher lets you quickly jump to other Experience Cloud solutions.
1. The help icon provides quick access to learning and support resources.
1. The notifications icon is badged with the number of currently assigned incomplete [notifications.](/help/implementing/cloud-manager/notifications.md)
1. Select the icon representing your user to access your user settings. If you do not have a user picture configured, an icon is randomly assigned.

#### Program Toolbar {#program-toolbar}

The program toolbar provides links to switch between Cloud Manager programs and actions appropriate to the context.

![Program toolbar](assets/program-toolbar.png)

1. The program selector opens up into a dropdown where you can quickly select other programs or take context-appropriate actions such as creating a new program
1. The getting started link gives you access to the [onboarding documentation journey](/help/journey-onboarding/overview.md) to get you up-and-running with Cloud Manager.
1. The action button offers context-appropriate actions such as creating a new program.

### Statistics and Call-to-Actions {#statistics}

The statistics and call-to-action section provides aggregate data for your organization, for example, if you have successfully set up your programs, statistics of your activities over the past 90 days might show, including:

* Number of [deployments](/help/implementing/cloud-manager/deploy-code.md)
* Number of [code quality issues](/help/implementing/cloud-manager/code-quality-testing.md) identified
* Number of builds

Or if you are just beginning the setup of your org, there might be tips on next steps or documentation resources.

### My Programs Section {#my-programs-section}

The main content of the **My Programs** console is the list of programs in the **My Programs** section.

The **My Programs** section lists cards representing each program. Tap or click on a card to access the **Program Overview** page of the program for details about the program.

>[!NOTE]
>
>Depending on your privileges you may not be able to select certain programs.

Use the sorting options to better find the program you need.

![Sorting options](/help/implementing/cloud-manager/assets/my-programs-sorting.png)

* Sort by
  * Date Created (default)
  * Program Name
  * Status
* Ascending (default) / Descending
* Grid View (default)
* List View

Every program is represented by a card (or row in a table), providing an overview of the program and quick links to take action.

![Program card](assets/program-card.png)

* Program image (if configured)
* Program name
* Service type: **Experience Manager Cloud** for AEM as a * Cloud Service programs or [**Experience Manager** for AMS programs](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-manager/content/introduction)
* [Program type](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md): Sandbox or production
* Status
* Configured solutions
* Creation date

Depending on the options chosen when creating the program, a production program might be badged to show additional features.

* [HIPAA](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#security)

  ![HIPAA badge](assets/hipaa.png)

* [WAF-DDOS protection](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#security)

  ![WAF-DDOS badge](assets/waf-ddos-protection.png)

* [99.99% SLA](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md#sla)

  ![99.99% SLA badge](assets/9999-sla.png)

The information icon also gives quick access to additional information about the program (useful in list view).

![Information](assets/information-list-view.png)

The ellipsis icon gives you access additional actions you can take on the program.

![Ellipsis button for programs](assets/program-ellipsis.png)

* Navigate to a particular [environment](/help/implementing/cloud-manager/manage-environments.md) of the program
* Open the [program overview](#program-overview)
* [Edit the program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md#editing)
* [Delete a sandbox program](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md#delete-sandbox-program)

>[!TIP]
>
>For more information about programs and creating and managing programs, please see the following documents.
>
>* [Programs and Program Types](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/program-types.md)
>* [Creating Sandbox Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-sandbox-programs.md)
>* [Creating Production Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/creating-production-programs.md)

### Quick Links Section {#quick-links-section}

The quick links section give you access to commonly-used, related resources.

## Program Overview Window {#program-overview}

Once you select a program in the **[My Programs](#my-programs-console)** console, you are taken to the **Program Overview** window.

![Program overview](assets/program-overview.png)

The program overview gives you access to all details of a Cloud Manager program. Like the **My Programs** console, it is made of several parts.

1. [Toolbars](#program-overview-toolbar) to quickly jump back to the My Programs console as well as navigate the program
1. [Tabs](#program-tabs) to switch between different aspects of the program
1. A [call-to-action](#cta) based on the last actions of the program
1. An [overview of the environments](#environments) of the program
1. An [overview of the pipelines](#pipelines) of the program
1. An [overview of the performance](#performance) of the program
1. Links to [useful resources](#useful-resources)

### Toolbars {#program-overview-toolbar}

The toolbars for the program overview are very similar to those of the [My Programs console.](#my-programs-toolbars) Only the differences are illustrated here.

#### Cloud Manager Header {#cloud-manager-header-2}

The Cloud Manager header has a hamburger menu that automatically opens to show the navigable tabs of the program overview.

![Cloud Manager hamburger menu](assets/cloud-manager-hamburger.png)

Tap or click the hamburger menu icon to hide the tabs.

#### Program Toolbar {#program-toolbar-2}

The program toolbar still gives you access to quickly switch to other programs, but additionally gives access to context-appropriate actions such as adding and editing the program.

![Program toolbar](assets/cloud-manager-program-toolbar.png)

Additionally, the toolbar always provides which tab you are on if you have chosen to hidden the tabs using the hamburger menu.

### Program Tabs {#program-tabs}

Each program has a lot of options and data associated with it. These data are gathered into tabs to make navigating the program simpler. The tabs give you access to:

* Overview - The program overview as described in the current document
* [Activity](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#activity) - The history of pipeline runs of the program
* [Pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#pipelines) - All pipelines configured for the program
* [Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md) - All repositories configured for the program
* [Reports](/help/implementing/cloud-manager/sla-reporting.md) - Metrics such as SLA data
* [Environments](/help/implementing/cloud-manager/manage-environments.md) - All environments configured for the program
* [Domain Settings](/help/implementing/cloud-manager/custom-domain-names/introduction.md) - Manage custom domain names for the program
* [SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction.md) - Manage SSL certificates for the program
* [IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/introduction.md) - Define allow lists for certain IP addresses
* [Content Sets](/help/implementing/developing/tools/content-copy.md) - Sets of content created for copy purposes
* [Copy Content Activity](/help/implementing/developing/tools/content-copy.md) - Content copy activities
* [Network Infrastructures](/help/security/configuring-advanced-networking.md) - Manage advanced networking options for the program
* Learning Paths - Additional learning resources about Cloud Manager

By default, when you open a program you arrive on the **Overview** tab. The current tab is highlighted. Select another tab to show its details.

Use the hamburger menu in the [Cloud Manager header](#cloud-manager-header-2) to hide the tabs.

### Call-to-Action {#cta}

The call-to-action section will give you helpful information depending on the status of your program. For a new program you may see next steps offered as well as a reminder of a go-live date, [set during program creation.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md)

![Call-to-action for a new program](/help/implementing/cloud-manager/assets/info-banner-new-program.png)

For a live program, the status of your last deployment with links for details and starting a new deployment.

![Call-to-action](/help/implementing/cloud-manager/assets/info-banner.png)

### Environments Card {#environments}

The **Environments** card gives you an overview of your environments as well as links for quick actions.

The **Environments** card only lists three environments. Click **Show All** to see all environments of the program.

Please see the document [Managing Environments](/help/implementing/cloud-manager/manage-environments.md) for details on how to manage your environments.

### Pipelines Card {#pipelines}

The **Pipelines** card gives you an overview of your pipelines as well as links for quick actions.

The **Pipelines** card only lists three pipelines. Click **Show All** to see all pipelines of the program.

Please see the document [Managing Pipelines](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md) for details on how to manage your pipelines.

### Performance Card {#performance}

The **Performance** card gives an overview of the **[CDN Dashboard.](/help/implementing/cloud-manager/cdn-performance.md)**

![Performance card](/help/implementing/cloud-manager/assets/cdn-performance-dashboard.png)

### Useful Resources {#useful-resources}

The **Useful Resources** section provides links to additional learning resources for Cloud Manager.
