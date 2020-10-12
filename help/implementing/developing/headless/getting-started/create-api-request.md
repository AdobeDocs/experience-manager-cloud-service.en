---
title: Accessing and Delivering Content Fragments
description: The Assets REST API allows managing Content Fragments and the GraphQL API allows simple headless delivery of Content Fragment content.
---

# Accessing and Delivering Content Fragments {#accessing-delivering-content-fragments}

The Assets REST API allows managing Content Fragments and the GraphQL API allows simple headless delivery of Content Fragment content.

## What are the Assets REST and GraphQL APIs? {#what-are-the-apis}

[Now that you have created some content fragments,](create-content-fragment.md) you can use AEM's APIs to deliver them headlessly.

* The Assets REST API allows you to create and modify Content Fragments (and other assets).
* The GraphQL API allows you to create requests to access and deliver Content Fragments.

The remainder of this guide will focus on GraphQL access.

## How to Deliver a Content Fragment Using GraphQL {#how-to-deliver-a-content-fragment}

Information architects will need to design queries for their channel endpoints in order to deliver content. These queries will generally only needed to be considered once per endpoint per model. For the purposes of this getting started guide we will will only need to create one.

## Next Steps {#next-steps}

That's it! You now have a basic understanding of headless content management in AEM. Of course there are many more resources where you can dive deeper for a comprehensive understanding of the features available.

* Configuration Manager - For details about the AEM Configuration Manager
* [Content Fragments](/help/assets/content-fragments/content-fragments.md) - For details about creating and managing Content Fragments
* [Content Fragments Support in AEM Assets HTTP API](/help/assets/content-fragments/assets-api-content-fragments.md) - For details on accessing AEM content directly over the HTTP API, via CRUD operations (Create, Read, Update, Delete)
* GraphQL API - For details on how to deliver Content Fragments headlessly
