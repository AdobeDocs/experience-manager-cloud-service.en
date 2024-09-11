---
title: Use Git with Cloud Manager
description: Learn how to use Cloud Manager's git repositories and how to integrate your own on-premise customer-managed git repository with Cloud Manager.
exl-id: 57e71b8a-4546-4d7f-825c-a1637d08e608
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Use Git with Cloud Manager {#git-integration}

Adobe Cloud Manager comes provisioned with a single git repository that is used to deploy code using Cloud Manager's CI/CD pipelines. 

You can use Cloud Manager's git repository out of the box, but you also have the option of integrating a customer-managed git repository with Cloud Manager.

## Git integration overview {#git-integration-overview}

This video series explores several use cases when integrating a customer-managed git repository with Cloud Manager, including: 

* [Initial Sync](#initial-sync)
* [Basic Branching Strategy](#branching-strategy)
* [Feature Branch Development](#feature-development)
* [Production Deployment](#production-deployment)
* [Synchronizing Release Tags](#sync-tags)

The video series assumes a basic knowledge of git and source control management. See the [additional resources below](#additional-resources) for more details on git.

>[!VIDEO](https://video.tv.adobe.com/v/28710/)

The steps and naming conventions outlined in this video series represent some best practices for working with a customer-managed git repository in Cloud Manager. It is expected that the conventions and workflows depicted are adapted for individual use cases.

## Initial sync {#initial-sync}

In this video, learn the first steps for synchronizing a customer-managed Git repository with Cloud Manager's Git repository.

>[!VIDEO](https://video.tv.adobe.com/v/28711/?quality=12)

## Basic branching strategy {#branching-strategy}

In this video, learn basic branching strategies.

>[!VIDEO](https://video.tv.adobe.com/v/28712/?quality=12)

## Feature branch development {#feature-development}

Use a feature branch to isolate code changes in a customer-managed git repository and synchronize with Cloud Manager's git repository to use a non-production pipeline for code quality and validation testing.

>[!VIDEO](https://video.tv.adobe.com/v/28723/?quality=12)

## Production deployment {#production-deployment}

Prepare code for a production release in a customer-managed git repository and synchronize with Cloud Manager's git repository to deploy to stage and production environments.

>[!VIDEO](https://video.tv.adobe.com/v/28724/?quality=12)

## Synchronize release tags {#sync-tags}

Synchronize release tags from a Cloud Manager git repository into a customer-managed git repository to provide visibility for what code has been deployed to staging and production environments.

>[!VIDEO](https://video.tv.adobe.com/v/28725/?quality=12)

## Additional resources {#additional-resources}

* [GitHub Resources](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)
* [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials/what-is-version-control)
* [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
