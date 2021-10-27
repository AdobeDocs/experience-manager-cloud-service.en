---
title: AEM Quick Site Creation Journey
description: Start here for a guided journey through the simple-to-use AEM Quick Site Creation tool to streamline the front-end development of your AEM Site and quickly customize your site with no AEM backend knowledge.
index: no
hide: yes
hidefromtoc: yes
---

# AEM Quick Site Creation Journey {#quick-site-creation-journey}

Start here for a guided journey through the simple-to-use AEM Quick Site Creation tool to streamline the front-end development of your AEM Site and quickly customize your site with no AEM backend knowledge.

>[!CAUTION]
>
>The Quick Site Creation tool is currently a tech preview. It is made available for testing and evaluation purposes and is not intended for production use unless agreed with Adobe Support.

## Introduction {#introduction}

AEM Sites is a powerful tool set for creating and managing digital experiences. Content authors can easily create digital experiences using the sites editor and organize the content using the sites console, all while being able to see the content live as it will be delivered by AEM to your audiences across channels.

The AEM Quick Site Creation tool allows for simple and fast customization of the theme and styling of AEM sites, allowing the front-end developer to work separately from and parallel to the content creators with zero knowledge of how AEM works. The AEM administrator simply downloads the site theme and provides it to the front-end developer who customizes it using their favorite tools and then commits the changes to the AEM code repository, which is then deployed.

By eliminating any knowledge requirements of AEM and allowing theme development to proceed in parallel with content creation, the AEM Quick Site Creation tool greatly accelerates your site's time-to-value and increases your customization and deployment agility.

## AEM Documentation Journeys {#documentation-journeys}

[A Documentation Journey](/help/journey-documentation/home.md) ties together many different and perhaps complicated topics and features by providing a narrative that helps the reader, who can be new to AEM, understand and solve a business problem from beginning to end, while assuming minimal prior topic or AEM knowledge.

Documentation Journeys are designed around best practices principles, informed by Adobe's latest research, proven implementation experience from Adobe consultants, and feedback from customer projects.

If you want to know how Adobe recommends how to solve sites business cases with AEM, AEM Sites Journeys are where to start.

## Audience {#audience}

This journey lays out the requirements, steps, and approach to customize AEM Sites themes. Its primary audience is the front-end developer, who needs no knowledge of AEM. However, in order to illustrate the entire process, the journey involves the administrator, who is assumed to have basic AEM Sites and Cloud Manager knowledge. In practice, the same person may serve both roles and this journey supports both perspectives.

|Persona|Description|Role in Journey|
|---|---|---|
|Front-End Developer|Customizes the site theme|Takes theme provided by the administrator and customizes it so that is can be deployed to the AEM site.|
|Content Author|Creates and manage content that is delivered as sites|Content Authors create content on AEM that is customized by the theme developed by the front-end developer.|
|Administrator|Manages the base setup and configuration of AEM including the deployment pipeline and source repository|The administrator provides the front-end developer with credentials to access the source repository for the project and deploy the customized themes.|

## The AEM Quick Site Creation Journey {#the-journey}

You will explore many topics in this journey. The following articles give you foundational knowledge of creating and customizing AEM sites using the Quick Site Creation tool and link out to detailed technical documentation.

|#|Article|Description|Target Audience|
|---|---|---|--|
|0|AEM Quick Site Creation Journey|This document|Administrator|
|1|[Understand Cloud Manager and the Quick Site Creation Workflow](cloud-manager.md)|Learn about Cloud Manager and how it ties together the new Quick Site Creation process.|Administrator|
|2|[Create site from template](create-site.md)|Learn how to quickly create a new AEM site using a site template.|Administrator|
|3|[Set up your pipeline](pipeline-setup.md)|Create a front-end pipeline to manage the customization of your site's theme.|Administrator|
|4|[Grant access to the front-end developer](grant-access.md)|Onboard the front-end developers into Cloud Manager so they have access to your AEM site git repository and pipeline.|Administrator|
|5|[Retrieve git repository access information](retrieve-access.md)|Learn how the front-end developer uses Cloud Manager to access git repository information.|Front-End Developer|
|6|[Customize the site theme](customize-theme.md)|Learn how a site theme is built, how to customize it, and how to test it using live AEM content.|Front-End Developer|
|7|[Deploy your customized theme](deploy-theme.md)|Learn how to deploy the site theme using the pipeline.|Front-End Developer|

## What's Next {#what-is-next}

You are now ready to get started on your Adobe Quick Site Creation journey.

* If you serve both front-end developer and administrator roles or simply want to understand the end-to-end process in AEM, please start at the beginning of the journey with [Understand Cloud Manager](cloud-manager.md) as laid out below.
* If you are only responsible for front-end development and will interact with the administrator, you can skip directly to [Retrieve git repository access information](retrieve-access.md) to get access to the AEM git repository and start customizing.

## Additional Resources {#additional-resources}

Check out these additional resources for more information on how AEM's powerful features work together.

* [AEM as a Cloud Service technical documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service.html) - If you already have a firm understanding of AEM, you may want to directly consult the in-depth technical docs.
