---
title: What is a Headless CMS?
description: Learn about Headless CMS. How do they work? What are the alternatives and differences? Why would you want to use a Headless CMS?
exl-id: 53f24f69-ad49-4b8e-9a91-36cd64c1f2b9
---
# What is a Headless CMS? {#what-is-a-headless-cms}

Headless content management is a key development for today's web design that decouples the frontend, client-side applications from the backend, content management system. A headless CMS is therefore responsible for the (backend) content management services, together with the mechanisms allowing the (frontend) applications to access that content.

But what does the term really mean? Here we offer a (very quick) introduction to the key concepts.

## What is a Content Management System (CMS)? {#content-management-system}

Let's start with the basics - what is a Content Management System?

A content management system (CMS) stores, manages and delivers the content used to provide your online experiences. 

## Traditional CMS {#traditional-cms}

Traditionally a CMS has included both the backend functionality for content storage and delivery, together with the frontend technology used to render the markup for an experience that your browser will display (the presentation layer). 

Very powerful, giving you full control of the content and formatting, but missing some of the flexibility needed in today's fast-moving environment; for example, when interfacing with external apps.

## Headless CMS {#headless-cms}

With a headless content management system, backend and frontend are now decoupled. 

The headless part is the content backend, as a headless Content Management System (CMS) is a back-end only content management system, designed and built explicitly as a content repository that makes content accessible via an API, for display on any device.

The frontend, which is developed and maintained independently, fetches content from the headless backend using a Content Delivery API, typically in JSON format. For example, this could be as a React or Angular application (Single Page Application (SPA)).

A headless CMS backend usually requires the content to be structured, based on a model or schema. This facilitates client applications requesting the right content for rendering an experience. Some CMS can expose both structured and unstructured content in JSON format. 

A key characteristic of this topology is that content served by the headless CMS in JSON format is pure content, without design or layout information. In a headless CMS implementation all formatting and layout is maintained by the decoupled frontend application. 

A key benefit of a headless CMS topology is the ability to reuse content across multiple channels, which may use different client-side frontend implementations. This can make the frontend development process more efficient. But it also means the frontend experience development process can become very code and IT-centric, with IT essentially owning the experience. 

## Content Delivery APIs {#content-delivery-apis}

A headless CMS can provide one, or multiple, ways of exposing content to client-side applications. Most commonly HTTP REST APIs, GraphQL APIs, or both.

While a REST API may often seem an easier way of requesting content (for example, by providing JSON for all content that matches a criteria), they typically deliver too much content to a client application. This can result in the client having to parse and filter out the content that is actually needed for rendering. 

GraphQL by contrast is a more focused mechanism for allowing client applications to query for exactly the content that is needed to render an experience. 

## Full-Stack CMS {#fullstack-cms}

A Full-Stack CMS commonly represents the traditional topology for content management and delivery, by including the content backend and frontend technology for rendering experiences. Content delivery in full-stack CMS commonly happens over internal content delivery API's. The frontend functionality is typically specific to the fullstack CMS. This coupling of frontend technology with content backend allows for what-you-see-is-what-you-get (WYSIWYG) experience authoring as a key benefit. 

## Hybrid CMS {#hybrid-cms}

A modern evolution of the full-stack CMS can be a hybrid CMS. This aims to combine the best of both worlds:

* efficient frontend development across channels using modern frontend tools, 
* while retaining WYSIWYG experience authoring to empower non-technical users, and to avoid IT becoming a bottleneck for cross-organizational content and experience management. 

This is achieved by embracing modern frontend frameworks such as React but maintaining an essential minimum of coupling with the content backend. 

## Decoupled CMS {#decoupled-cms}

While the term decoupled CMS is sometimes used independently, it essentially describes a headless CMS backend by emphasizing its key characteristic of being decoupled from the client-side frontend application. 

## Headful CMS {#headful-cms}

This is another term for a traditional CMS.

## Further Reading {#further-reading}

You can read more about using AEM in a headless CMS topology here: 

* [Introduction to Adobe Experience Manager as a Headless CMS](/help/headless/introduction.md)
