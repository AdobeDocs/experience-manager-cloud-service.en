---
title: AEM Headless Content Author Journey
description: An introduction to the powerful, and flexible, headless features of Adobe Experience Manager as a Cloud Service, and how to author content for your project.
---

# Authoring for Headless with AEM - An Introduction {#author-headless-introduction}

In this part of the [AEM Headless Content Author Journey](overview.md), you can learn the (basic) concepts and terminology necessary to understand authoring content for headless content delivery with Adobe Experience Manager (AEM) as a Cloud Service.

## Objective {#objective}

* **Audience**: Beginner
* **Objective**: Introduce the concepts and terminology for Headless Authoring.

## Content Management System (CMS) {content-management-system}

What is a Content Management System?

A Content Management System (CMS) is just what it says it is - a computer system used to manage content. That's a bit general, so to be more precise, it is (typically) used for managing content that you want to make available on your website(s).

## Headless CMS {#headless-cms}

Headless is a term used to describe systems that effectively detach the content from the manner of displaying that content on the web. 

In other words, a single content-set can now be accessed by one, or more, applications. The "traditional" relationship of having one application (the CMS itself) responsible for rendering the content has been loosened.

This means that your content can be delivered to any device, in a wide range of formats. This makes the whole process much more flexible, and means that you do not need to worry about layout and formatting.

>[!NOTE]
>If you want to learn more about the technical details of Headless CMS you can read more at Learn About CMS Headless Development.

## Adobe Experience Manager as a Cloud Service {#aem-cloud-service}

AEM can be used as a:

* Headless CMS
  * Content can be authored as Content Fragments. These are self-contained items of content that can be directly accessed by a range of applications. These means your content can reach a wide range of devices, in a wide range of formats and with a wide selection of functionality.
  And as a double-whammy, these fragments can also be used when constructing AEM web pages.

* "Traditional" CMS
  * Content is authored for web pages, using a range of components that define how the content will be rendered on your website. Even here AEM is extremely flexible as your project team can develop customized components.

## Data Modeling {#data-modeling}

So data modeling is another technical term - why should it interest you as an author?

For the headless applications to be able to access your content, and do something with it, your content really needs to have a predefined structure. It would be possible to have your content as free-form, but it would make life very complicated for the applications.

Basically the process of defining the structure for your content involves designing a model - and this is called data modeling. 

For AEM a Content Architect will perform the data modeling to design a range of Content Fragment Models that you then use as a basis for your Content Fragments.

## What's Next {#whats-next}

Now that you have learned the concepts and terminology, the next step is to [Learn the basics of authoring Content Fragments](basics.md). This will introduce the basic handling of AEM together with how to author Content Fragments.

## Additional Resources {#additional-resources}

* AEM Headless Developer Journey
  * [Learn About CMS Headless Development](/help/journey-headless/developer/learn-about.md)
  * [Learn how to Model Your Content](/help/journey-headless/developer/model-your-content.md)