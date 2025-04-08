---
title: AEM Quick Site Creation Journey
description: Start here for a guided journey through the easy-to-use AEM Quick Site Creation tool to streamline the front-end development of your AEM Site and quickly customize your site with no AEM backend knowledge.
exl-id: b8218232-0298-4b16-9dab-fa59be592a24
solution: Experience Manager Sites
feature: Developing
role: Admin, Developer
---
# AEM Quick Site Creation Journey {#quick-site-creation-journey}

Start here for a guided journey through the easy-to-use AEM Quick Site Creation tool to streamline the front-end development of your AEM Site and quickly customize your site with no AEM backend knowledge.

## Introduction {#introduction}

AEM Sites is a powerful tool set for creating and managing digital experiences. Content authors can easily create digital experiences using the sites editor and organize the content using the sites console, all while being able to see the content live as it is delivered by AEM to your audiences across channels.

The AEM Quick Site Creation tool allows non-developers to quickly create a site from scratch by using site templates. Once created, the Quick Site Creation tool also enables fast customization of the theme and styling of the AEM site (JavaScript, CSS, and static resources). This allows the front-end developer, who need zero knowledge of AEM, to work separately from and parallel to the content creators. The AEM administrator simply downloads the site theme and provides it to the front-end developer who customizes it using their favorite tools and then commits the changes to the AEM code repository, which is then deployed.

By eliminating any developer knowledge for site creation, eliminating AEM knowledge requirements for front end development, and allowing theme development to proceed in parallel with content creation, the AEM Quick Site Creation tool greatly accelerates your site's time-to-value and increases your site customization and deployment agility.

## Video Overview {#video-overview}

For a quick overview of this feature in action, [you can watch this five minute introduction](https://www.youtube.com/watch?v=NQeQ1jZ7ZBw).

This documentation journey will take you through all the features in the video  step-by-step and in detail so you understand the workflow and can recreate the process in your own environment.

## AEM Documentation Journeys {#documentation-journeys}

[A Documentation Journey](/help/journey-documentation/documentation-journeys.md) ties together many different, complicated topics and features by providing a narrative that helps the reader, who can be new to AEM, understand and solve a business problem from beginning to end, while assuming minimal prior topic or AEM knowledge.

Documentation Journeys are designed around best practices principles, informed by Adobe's latest research, proven implementation experience from Adobe consultants, and feedback from customer projects.

If you want to know how Adobe recommends how to solve sites business cases with AEM, AEM Sites Journeys are where to start.

## Audience {#audience}

This journey lays out the requirements, steps, and approach to customize AEM Sites themes. Its primary audience is the front-end developer, who needs no knowledge of AEM. However, to illustrate the entire process, the journey involves administrators, who are assumed to have basic AEM Sites and Cloud Manager knowledge. In practice, multiple people can serve multiple roles and this journey supports perspectives from both admins and front-end developers.

|Persona|Description|Role in Journey|
|---|---|---|
|Front-End Developer|Customizes the site theme|Takes theme provided by the AEM administrator and customizes it so that is can be deployed to the AEM site.|
|Content Author|Creates and manages content that is delivered as sites|Content Authors create content on AEM that is rendered with the theme customized by the front-end developer.|
|AEM Administrator|Creates a new AEM site|The AEM administrator creates a new site based on a template and then provides the front-end developer with a theme to customize.|
|Cloud Manager Administrator|Creates pipelines and grants access|The Cloud Manager Administrator creates the front-end pipeline and grants access to the front-end developer to be able commit customizations to the AEM git repository.|

## The AEM Quick Site Creation Journey {#the-journey}

You will explore many topics in this journey. The following articles give you foundational knowledge of creating and customizing AEM sites using the Quick Site Creation tool and link out to detailed technical documentation.

|#|Article|Description|Responsible Role|
|---|---|---|--|
|0|AEM Quick Site Creation Journey|This document|AEM & Cloud Manager Administrators|
|1|[Understand Cloud Manager and the Quick Site Creation Workflow](cloud-manager.md)|Learn about Cloud Manager and how it ties together the new Quick Site Creation process.|AEM Administrator|
|2|[Create site from template](create-site.md)|Learn how to quickly create an AEM site using a site template.|AEM Administrator|
|3|[Set up your pipeline](pipeline-setup.md)|Create a front-end pipeline to manage the customization of your site's theme.|Cloud Manager Administrator|
|4|[Grant access to the front-end developer](grant-access.md)|Onboard the front-end developers into Cloud Manager so they have access to your AEM site git repository and pipeline.|Cloud Manager Administrator|
|5|[Retrieve git repository access information](retrieve-access.md)|Learn how the front-end developer uses Cloud Manager to access git repository information.|Front-End Developer|
|6|[Customize the site theme](customize-theme.md)|Learn how a site theme is built, how to customize it, and how to test it using live AEM content.|Front-End Developer|
|7|[Deploy your customized theme](deploy-theme.md)|Learn how to deploy the site theme using the pipeline.|Front-End Developer|

## What's Next {#what-is-next}

You are now ready to get started on your Adobe Quick Site Creation journey.

* If you are an AEM or Cloud Manager administrator, or if you serve both front-end developer and administrator roles, or if you simply want to understand the end-to-end process in AEM, start at the beginning of the journey with [Understand Cloud Manager](cloud-manager.md) as laid out below.
* If you are only responsible for front-end development and will interact with the AEM and Cloud Manager administrators, you can skip directly to [Retrieve git repository access information](retrieve-access.md) to get access to the AEM git repository and start customizing.
* If you already understand AEM Sites and Cloud Manager work together and want to start directly with configuration, you can [skip directly to creating a site from a template](create-site.md).

## Additional Resources {#additional-resources}

Check out these additional resources for more information on how AEM's powerful features work together.

* [AEM as a Cloud Service technical documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service.html) - If you already have a firm understanding of AEM, you may want to directly consult the in-depth technical docs.
* [Site Administration Documentation](/help/sites-cloud/administering/site-creation/create-site.md) - Check out the technical docs on site creation for more details on the Quick Site Creation tool's features.
