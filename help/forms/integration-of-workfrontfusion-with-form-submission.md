---
title: Integration of Adobe Workfront Fusion with AEM Forms Submission
description: Adobe Workfront Fusion allows you to focus on new tasks rather than focusing on repetitive tasks. You can connect Adobe Workfront Fusion to an Adaptive Form using Form Submission.
keywords: Integration of Adobe Workfront Fusion with AEM Forms Submission, Adobe Workfront Fusion with AEM Forms, Workfront Fusion with AEM Forms, Connect Workfront Fusion to AEM Forms, AEM Forms and Workfront Fusion, How to connect Workfront Fusion with AEM Forms?, Connect Workfront Fusion to a Form
topic-tags: author, developer
hide: yes
hidefromtoc: yes
---

# Integrate Adobe Workfront Fusion with AEM Forms Submission

Adobe Workfront Fusion automates the process of repeating the same tasks, allowing you to focus on new tasks instead of recurring ones. Workfront Fusion connects AEM Forms using services to create scenarios that automatically transfer data. A scenario consists of series of modules which executes data transfer between applications and web services. In a scenario, you orchestrate various modules to automate tasks.

For example, using Workfront Fusion, you can create a scenario to monitor new data in an application using a module in an AEM Form. A subsequent module uses the gathered data to create a new record in a table. Once a scenario is set up, Workfront Fusion automatically executes the tasks whenever a user fills out a new form, updating the database seamlessly.

## Advantages of using Adobe Workfront Fusion{#advatages-of-workfront-fusion}

Some of the advantages of using Adobe Workfront Fusion are:

- Automating tasks which are less prone to errors.
- Customizing requirements specific to an organization that are not directly included in Workfront.
- Handling simple logics and straightforward decisions, for example, if/then statements.

## Prerequisites to integrate AEM Forms with Adobe Workfront Fusion {#prerequisites}

You can integrate AEM Forms with Workfront Fusion using Form Submission. Some prerequisites required to connect Workfront Fusion to AEM Forms:

- Ensure user have a valid [Workfront Fusion license](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-fusion/get-started-with-workfront-fusion/license-automation-vs-integration.html).
- Ensure user acquire access to the [Dev Console](https://my.cloudmanager.adobe.com/) and [retrieve the service credentials](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html).

## Integrate AEM Forms with Adobe Workfront Fusion

To connect [Workfront fusion](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-fusion/get-started-with-workfront-fusion/workfront-fusion-overview.html) to a form, perform the following steps:

1. Create a [Workfront Scenario](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-fusion/scenarios-in-fusion/scenario-overview.html) 

    To create a Workfront scenario:
    1. Click Scenarios ![Share icon](/help/forms/assets/Smock_ShareAndroid_18_N.svg) in the left panel. 
    1. Click **[!UICONTROL Create a new scenario]** in the upper-right corner of the page.
    1. Click **New scenario** in the upper-left corner and type a proper name for the scenario.
    1. Click the question mark, to add the first module to the scenario.
    1. 

    * Add a Web hook
    * Connect a web hook to a Workfront Scenario
1. Configure Submit action of an Adaptive Form for Workfront Fusion

## Best Practices {#best-practices}

* During testing or development of Workfront, add the Author URL to the instance URL. However, when deploying Workfront Fusion in a production environment, it is recommended to update the Author URL with the Publish URL.

* It is recommended to choose your web hook name carefully, as there is no way to get the scenario name at the AEM instance. In case, you change the web hook name in future it is not reflected at the AEM Forms submit action drop-down list.
* A scenario can have multiple web hook links but at a time only one web hook link is active. It is recommended to delete the unlinked web hooks, so that it does not appear in AEM Forms submit action drop-down list.





 
