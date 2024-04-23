---
title: Navigating the Cloud Manager UI
description: Learn how the Cloud Manager UI is organized and how to navigate to manage your programs and environments.
---

# Navigating the Cloud Manger UI {#navigation}

Learn how the Cloud Manager UI is organized and how to navigate to manage your programs and environments.

## My Programs Console {#my-programs}

When you log into Cloud Manager at at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization, you arrive at the **My Programs** console.

![My Programs console](assets/my-programs-console.png)

The My Programs console provides an overview of all programs to which you have access in the selected organization. It is made up of several parts.

1. [Toolbars](#toolbars-my-programs-toolbars) for organization selection, alerts, and account settings
1. [Chat AEM](#chat-aem) to guide you in your next steps and answer questions
1. [Statistics and call-to-action](#statistics) for an overview of your recent activity
1. [Programs and License](#programs-license) to understand your current license status and manage your programs
1. [Quick Links](#quick-links) to easily access related resources

### Toolbars {#my-programs-toolbars}

There are two toolbars on top of each other. 

#### Cloud Manager Header {#cloud-manager-header}

The first is the Cloud Manager header, which is persistent as you navigate Cloud Manager. It is an anchor that gives you access to settings and information that apply across Cloud Manager programs.

![The Experience Cloud header](assets/experience-cloud-header.png)

1. The Cloud Manager button will take you back to the My Programs console of Cloud Manager no matter where you are in Cloud Manager.
1. Tap or click the Feedback button to provide feedback to Adobe about Cloud Manager.
1. The organization selector displays the organization you are currently signed into. Tap or click to switch to another organization if your Adobe ID is associated with multiple.
1. Tapping or clicking the solutions switcher lets you quickly jump to other Experience Cloud solutions.
1. The help icon provides quick access to learning and support resources.
1. The notifications icon is badged with the number of currently assigned incomplete [notifications.](/help/implementing/cloud-manager/notifications.md)
1. Select the icon representing your user to access your user settings. If you do not have a user picture configured, an icon is randomly assigned.

#### Program Toolbar {#program-toolbar}

The program toolbar provides links to switch between Cloud Manager programs and actions appropriate to the context.

![Program toolbar](assets/program-toolbar.png)

1. The program selector opens up into a dropdown where you can quickly select other programs or create a new program
1. The getting started link gives you access to the [onboarding documentation journey](/help/journey-onboarding/overview.md) to get you up-and-running with Cloud Manager.
1. The action button offers context-appropriate actions such as creating a new program.

### Chat AEM {#chat-aem}

Chat AEM is a chatbot you can ask questions about your Cloud Manger experience, including links to frequent discussion topics.

### Statistics {#statistics}

The statistics section provides aggregate data for your organization, for example, if you have successfully set up your programs, statistics of your activities over the past 90 days might show, including:

* Number of [deployments](/help/implementing/cloud-manager/deploy-code.md)
* Number of [code quality issues](/help/implementing/cloud-manager/code-quality-testing.md) identified
* Number of builds

Or if you are just beginning the setup of your org, there might be tips on next steps or documentation resources.

### Programs and License {#programs-license}

The main content of the My Programs console is the list of programs and status of your license.

#### Programs Tab {#programs}

The **Programs** tab lists cards representing each program to which you have access. Tap or click on a card to access the **Program Overview** page of the program for details about the program.

Use the sorting options to better find the program you need.

![Sorting options](/help/implementing/cloud-manager/assets/my-programs-sorting.png)

* Sort by
  * Date Created (default)
  * Program Name
  * Status
* Ascending (default) / Descending
* Grid View (default)
* List View

#### License Tab {#license-tab}

The **License** tab gives you quick access to the [License Dashboard.](/help/implementing/cloud-manager/license-dashboard.md)

### Quick Links {#quick-links}

The quick links section give you access to commonly-used, related resources.

## Program Overview {#program-overview}

Once you select a program in the My Programs console, you are taken to the Program Overview.

![Program overview](assets/program-overview.png)

The program overview gives you access to all details of a Cloud Manager program. Like the My Programs console, it is made of several parts.

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

The program toolbar still gives you access to quickly switch to other programs, but additionally gives access to edit the program.

![Program toolbar](assets/cloud-manager-program-toolbar.png)

Please see the document [Managing and Editing Programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/editing-programs.md) for details.

Additionally, the toolbar always provides which tab you are on if you have chosen to hidden the tabs using the hamburger menu.

### Program Tabs {#program-tabs}

Each program has a lot of options and data associated with it. These data are gathered into tabs to make navigating the program simpler. The tabs give you access to:

* Overview - The program overview as described in the current document
* Activity - 
* Pipelines
* Repositories
* Reports
* Environments
* Content Sets
* Copy Content Activity
* Learning Paths

By default, when you open a program you arrive on the Overview tab. The current tab is highlighted. Select another tab to show its details.

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

