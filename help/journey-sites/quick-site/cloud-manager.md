---
title: Understand Cloud Manager and the Quick Site Creation Workflow
description: Learn about Cloud Manager and how it ties together the new Quick Site Creation process.
index: no
hide: yes
hidefromtoc: yes
---

# Understand Cloud Manager and the Quick Site Creation Workflow {#understand-cloud-manager}

Learn about Cloud Manager and how it ties together the new Quick Site Creation process.

>[!CAUTION]
>
>The Quick Site Creation tool is currently a tech preview. It is made available for testing and evaluation purposes and is not intended for production use unless agreed with Adobe Support.

>[!TIP]
>
>If your role is exclusively front end development, you can skip to the article [Customize the Site Theme](customize-theme.md) in this journey.
>
>If you are an administrator, responsible for both front end development and administrator tasks, or would simply like to understand the end-to-end process in AEM for front end development, continue reading the current article.

## Objective {#objective}

This document helps you understand how the AEM Quick Site Creation tool works and gives you an overview of the end-to-end flow. After reading you should:

* Understand how AEM Sites and the Cloud Manager work together to facilitate front end development
* See how the front end customization step is entirely decoupled from AEM and requires no AEM knowledge.

## Requirements and Prerequisites {#requirements-prerequisites}

There are a number of requirements before you begin creating and customizing sites using the Quick Site Creation tool.

Because this journey is intended for both front end developers, administrators, and combinations of both roles, the requirements for both are listed here.

It is important to understand that for the front end developer, no AEM access or knowledge is necessary.

### Knowledge {#knowledge}

|Knowledge|Role|
|---|---|
|Understanding of the standard tools and processes of front end development|Front end developer|
|Basic knowledge of how to create and manage sites in AEM|Administrator|
|Basic knowledge of Cloud Manager|Administrator|

Note that for the front end developer, no AEM knowledge is necessary.

### Tools {#tools}

|Tool|Role|
|---|---|
|Preferred front end development environment|Front end developer|
|npm|Front end developer|
|webpack|Front end developer|
|Access to Cloud Manager|Administrator|
|Be a member of the **Deployment Manager** role in Cloud Manager|Administrator|
|Preferred front end development environment|Front end developer|
|npm|Front end developer|
|webpack|Front end developer|

Note that for the front end developer, no use of AEM is necessary.

## Cloud Manager {#cloud-manager}

Cloud Manager is an essential component of AEM as a Cloud Service and serves as the single entry point for the platform.

To support customers with enterprise development setups, AEM as a Cloud Service fully integrates with Cloud Manager and its purpose-built CI/CD pipelines. The Quick Site Creation tool extends these features to support dedicated front end development pipelines.

## Front End Development Flow {#flow}

The overall flow is simple and intuitive even if you do not yet have extensive experience with Cloud Manager.

1. The administrator creates a front end pipeline in Cloud Manager. The pipeline orchestrates the deployment of code from a git repository to an AEM environment.
1. The administrator creates a new site using a site theme.
1. The administrator exports the theme and provides it to the front end developer along with credentials for the git repository.
1. The front end developer customizes the theme, testing it using actual content from the site using a proxy.
1. The front end developer commits the changes to the git repository.
1. The administrator executes the pipeline to deploy the customizations.

The major advantage of using the Quick Site Creation tool is that the pure front end developer is only responsible for a single step in this process: the actual customization. The front end developer has no interaction with AEM or needs any knowledge of the system.

## What's Next {#what-is-next}

Now that you have completed this part of the AEM Quick Site Creation journey you should:

* Understand how AEM Sites and the Cloud Manager work together to facilitate front end development
* See how the front end customization step is entirely decoupled from AEM and requires no AEM knowledge.

Build on this knowledge and continue your AEM Quick Site Creation journey by next reviewing the document [Setup Your Pipeline,](pipeline-setup.md) where you will learn how to configure your Cloud Manager pipeline for front end deployment.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the Quick Site Creation journey by reviewing the document [[Setup Your Pipeline,](pipeline-setup.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the journey.

* [Cloud Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/onboarding/onboarding-concepts/cloud-manager-introduction.html) - If you would like more details on Cloud Manager's features, you may want to directly consult our in-depth technical docs.
* [npm](https://www.npmjs.com) - AEM themes used to quickly build sites are based on npm.
* [webpack](https://webpack.js.org) - AEM themes used to quickly build sites rely on webpack.
