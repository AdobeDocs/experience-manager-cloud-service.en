---
title: Troubleshoot Persisted GraphQL queries
description: Learn how to troubleshoot issues with persisted GraphQL queries in Adobe Experience Manager as a Cloud Service.
feature: "Headless, Content Fragments,GraphQL API"
exl-id: 71bd1f68-ca96-4c78-a936-abed250ecec1
role: "Admin, Developer"
---
# Troubleshoot Persisted GraphQL Queries {#troubleshoot-persisted-graphql-queries}

The [Actions Center](/help/operations/actions-center.md) includes the **GraphQL persisted query error** alert. This means that you are informed whenever one of your GraphQL persisted queries throws an error.

To help you troubleshoot and resolve such problems, this page covers the *most common* causes of failures, and steps on how to fix them.

## Changes to the Content Fragment model {#changes-to-content-fragment-model}

A GraphQL persisted query can fail when it is based on GraphQL types that are obsolete, often due to a change in the underlying Content Fragment models.

Such errors can happen for a variety of reasons. Examples include (the list is not exhaustive), when the author of a Content Fragment Model:

* removes or renames a field
* updates the **Model Type** that defines the models allowed for the fragment reference
* un-publishes a model that is referenced by other models

To address such errors, you should either:

* update the persisted query that is failing to accommodate the changes made to the Content Fragment Model 
* revert the change on the model that introduced the problem

## GraphQL endpoint not configured {#graphql-endpoint-not-configured}

When persisted queries return the `404` error code, together with the information `No suitable endpoint found`, this means that no GraphQL endpoint is configured on the AEM environment. 

To correct this, follow the steps for enabling and publishing your endpoint from [Manage GraphQL endpoints in AEM](/help/headless/graphql-api/graphql-endpoint.md).

## Missing path in the GraphQL persisted query URL {#missing-path-query-url}

If persisted queries return the `400` error code with the information `Suffix: '/' does not contain a path`, the GraphQL servlet is being called without a path suffix. 

The pattern should be `/graphql/execute.json/thePath`.

## Blocked due to IP allow list {#blocked-due-to-ip-allow-list}

In such a case, the query returns the `405` error code.

Such an error is not something specific to GraphQL. See the KB article [405 Error Not Allowed](https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-20824).

## Blocked by dispatcher {#blocked-dispatcher}

If the GraphQL endpoint returns the `404` error on publish for `POST` requests, it means the GraphQL queries are blocked at the dispatcher level and the endpoint needs to be manually enabled.

This should not be the case by default, but a custom dispatcher configuration might cause this issue. See more under [Dispatcher - Endpoint configuration with AEM Headless](/help/headless/deployment/dispatcher.md).
