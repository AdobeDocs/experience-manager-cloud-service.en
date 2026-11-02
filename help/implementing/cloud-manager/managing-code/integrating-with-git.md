---
title: Use Git with Cloud Manager
description: Learn how to use Cloud Manager's git repositories and how to integrate your own on-premise customer-managed git repository with Cloud Manager.
exl-id: 57e71b8a-4546-4d7f-825c-a1637d08e608
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: a01bfd36-4ab8-4bf8-9dc0-5b45b890552e
    internal-label: APIs
subfeature_v2:
  - id: d9eb3b3e-9447-4ed4-bf4a-96c7b245cb27
    internal-label: Cloud Manager APIs
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Use Git with Cloud Manager {#git-integration}

Adobe Cloud Manager comes provisioned with a single Git repository that is used to deploy code using Cloud Manager's CI/CD pipelines. 

You can use Cloud Manager's Git repository as provided, but you also have the option of integrating a customer-managed Git repository with Cloud Manager.

## Git integration overview {#git-integration-overview}

This video series explores several use cases when integrating a customer-managed Git repository with Cloud Manager, including: 

* [Initial Sync](#initial-sync)
* [Basic Branching Strategy](#branching-strategy)
* [Feature Branch Development](#feature-development)
* [Production Deployment](#production-deployment)
* [Synchronizing Release Tags](#sync-tags)

The video series requires a foundational knowledge of Git and source control management. See the [additional resources below](#additional-resources) for more details on Git.

>[!VIDEO](https://video.tv.adobe.com/v/28710/)

The steps and naming conventions outlined in this video series represent some best practices for working with a customer-managed Git repository in Cloud Manager. It is expected that the conventions and workflows depicted are adapted for individual use cases.

## Initial sync {#initial-sync}

In this video, learn the first steps for synchronizing a customer-managed Git repository with Cloud Manager's Git repository.

>[!VIDEO](https://video.tv.adobe.com/v/28711/?quality=12)

## Basic branching strategy {#branching-strategy}

In this video, learn basic branching strategies.

>[!VIDEO](https://video.tv.adobe.com/v/28712/?quality=12)

## Feature branch development {#feature-development}

Use a feature branch to isolate code changes in a customer-managed Git repository and synchronize with Cloud Manager's Git repository to use a non-production pipeline for code quality and validation testing.

>[!VIDEO](https://video.tv.adobe.com/v/28723/?quality=12)

## Production deployment {#production-deployment}

Prepare code for a production release in a customer-managed Git repository and synchronize with Cloud Manager's Git repository to deploy to stage and production environments.

>[!VIDEO](https://video.tv.adobe.com/v/28724/?quality=12)

## Synchronize release tags {#sync-tags}

To provide visibility into what code has been deployed to staging and production environments, synchronize release tags from a Cloud Manager Git repository into a customer-managed Git repository.

>[!VIDEO](https://video.tv.adobe.com/v/28725/?quality=12)

## Additional resources {#additional-resources}

* [GitHub resources](https://docs.github.com/en/get-started/getting-started-with-git/set-up-git)
* [Atlassian Git tutorials](https://www.atlassian.com/git/tutorials/what-is-version-control)
* [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
