---
title: What is a Headless CMS?
description: Learn about Headless CMS. How do they work? What are the alternatives and differences? Why would you want to use a Headless CMS?
---

# What is a Headless CMS? {#what-is-headless}

Headless Content Management is a key development for today's web design that aims to decouple frontend development of client-side applications from backend systems. 

But what does the term really mean? Here we offer a (very quick) introduction to the key concepts.

## What is a Content Management System (CMS)? {#content-management-system}

Let's start with the basics - what is a Content Management System?

A Content Management System (CMS) stores and manages content for your online experiences, and it has traditionally included both backend functionality for content storage and delivery, and frontend technology to render the markup for an experience that your browser will display, i.e. the presentation layer. 

## Headless CMS {#headless-cms}

When implementing a headless content management system, backend and frontend are now decoupled. The headless part is the content backend.  

* "*A headless content management system, or headless CMS, is a back-end only content management system (CMS) built from the ground up as a content repository that makes content accessible via an API for display on any device.*

  See [Wikipedia](https://en.wikipedia.org/wiki/Headless_content_management_system).

The frontend, which is developed and maintained independently, e.g. as a React or Angular application (SPA, Single Page Application), fetches content from the headless backend using a Content Delivery API, typically in JSON format. 

A headless CMS backend commonly stores content as structured content that is based on a model or schema, to facilitate client applications requesting the right content for rendering an experience. Some CMS, such as Adobe Experience Manager, can expose both structured and unstructred content in JSON format. 

A key characteristic of this topology is that content served by the headless CMS in JSON format is pure content, without design or layout information, which in a headless CMS implementation is specified in the decoupled frontend application. 

A key benefit of a headless CMS topology is the ability to reuse content across multiple channels which may use different client-side frontend implemenations. This can make the frontend development process more efficient. But it also means the frontend experience development process can become very code and IT centric, and IT essentially "owning" the experience. 

## Content Delivery APIs {#content-delivery-apis}

Headless CMS can provide one or various ways of exposing content to client-side applications - most commonly HTTP REST API's or GraphQL API's, or both. While a REST API may often seem like an easier way of requesting content, by e.g. providing JSON for all content that matches a criteria, they typically overdeliver content to a client application, resulting in the client having to parse and filter out the content that is actually needed for rendering. GraphQL by contrast is a more modern way of allowing client applications to query for exactly the content that is needed for rendering an experience. 

## Full-Stack CMS {#fullstack-cms}

A Full-Stack CMS commonly represents the traditional topology for content management and delivery, by including the content backend and frontend technology for rendering experiences. Content delivery in fullstack CMS commonly happens over internal content delivery API's. The frontend technoogy is typically specific to the fullstack CMS. This coupling of frontend technology with content backend however allows for what-you-see-is-what-you-get (WYSIWYG) experience authoring as a key benefit. 

## Hybrid CMS {#hybrid-cms}

A modern evolution of a fullstack CMS can be a hybrid CMS that aims to combine the best of both worlds - efficient frontend development across channels using modern frontend tools, but retaining wysiwyg experience authoring to also empower non-technical users, and to help avoid IT becoming a bottleneck for cross-orginazational content and experience management. This is achieved by embracing modern frontend frameworks such as React but maintaining an essential minimum of coupling with the content backend. 

## Decoupled CMS {#decoupled-cms}

While the term decoupled CMS is sometimes used independently, it essentially describes a headless CMS backend by emphasizing its key characteristic of being decoupled from the clientside frontend application. 


## Further Reading {#further-reading}

You can read more about using AEM in a headless CMS topology here: 

* [Introduction to Adobe Experience Manager as a Headless CMS](help/headless/introduction.md)
