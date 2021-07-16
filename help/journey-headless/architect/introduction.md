---
title: AEM Headless Content Architect Journey
description: An introduction to the powerful, and flexible, headless features of Adobe Experience Manager as a Cloud Service, and how to model content for your project.
---

# Content Modeling for Headless with AEM - An Introduction {#architect-headless-introduction}

In this part of the [AEM Headless Content Architect Journey](overview.md), you can learn the (basic) concepts and terminology necessary to understand content modeling for headless content delivery with Adobe Experience Manager (AEM) as a Cloud Service.

## Objective {#objective}

* **Audience**: Beginner
* **Objective**: Introduce the concepts and terminology relevant to Headless Content Modeling.

## Content Management System (CMS) {#content-management-system}

What is a Content Management System?

A Content Management System (CMS) is just what it says it is - a computer system used to manage content. That's a bit general, so to be more precise, it is (typically) used for managing content that you want to make available on your website(s).

## Headless CMS {#headless-cms}

Headless is a term used to describe systems that effectively detach the content from the manner of displaying that content on the web. 

Traditionally you would manage your content in a CMS, and the same CMS would be responsible for rendering that content on your webpages.

Now headless means that the content-set can be managed in the CMS and then accessed by one, or more, (independent) applications. 

This means that the content can be delivered to any device, in a wide range of formats. This makes the whole process much more flexible, and also means that authors do not need to worry about layout and formatting.

>[!NOTE]
>
>If you want to learn more about the technical details of Headless CMS you can read more at Learn About CMS Headless Development.

## Adobe Experience Manager as a Cloud Service {#aem-cloud-service}

So what is AEM?

First and foremost, AEM is a Content Management System with a wide range of features that can also be customized to meet your requirements. 

This all means that it can be used as a:

* Headless CMS
  * For headless, content can be authored as **Content Fragments**. 
  These are self-contained items of content that can be directly accessed by a range of applications, as they have a predefined structure, based on **Content Fragment Models**.
  This means the content can reach a wide range of devices, in a wide range of formats and with a wide selection of functionality.
  (And as a double-whammy, these fragments can also be used when constructing AEM web pages - if you want.)

* "Traditional" CMS
  * Content is authored for web pages, using a range of components that define how the content will be rendered on your website. Even here AEM is extremely flexible as your project team can develop customized components.

## Content Modeling {#content-modeling}

Content Modeling (also known as data modeling) is your specialty, so what needs to be considered when modeling for headless?

For the headless applications to be able to access your content, and do something with it, the content really needs to have a predefined structure. It would be possible to have your content as free-form, but it would make life *very* complicated for the applications.

For AEM you, as a Content Architect, will perform the content modeling to design a range of **Content Fragment Models**. These define the structure used when your content authors create the **Content Fragments** that hold the content.

### Accessing the Content {#access-content}

This is more of a development detail - but it might interest you, just to complete the story.

Once you've created the Content Fragment Models, and your authors have used them to generate the content, the headless applications will need to access this content. 

Adobe Experience Manager (AEM) as a Cloud Service, can selectively access your Content Fragments using the AEM GraphQL API, to return only the content that is needed. Using the API a developer can formulate queries that select specific content.This selection process is based on *your* Content Fragment Models. 

This means your project can realize headless delivery of structured content for use in your applications.

## What's Next {#whats-next}

Now that you have learned the concepts and terminology, the next step is to [Learn the basics of modeling with Content Fragment Models](basics.md). 

## Additional Resources {#additional-resources}

* AEM Headless Developer Journey
  * [Learn About CMS Headless Development](/help/journey-headless/developer/learn-about.md)
  * [Learn how to Model Your Content](/help/journey-headless/developer/model-your-content.md)
