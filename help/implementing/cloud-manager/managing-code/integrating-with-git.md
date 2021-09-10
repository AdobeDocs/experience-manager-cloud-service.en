---
title: Integrating with Git
description: Integrating with Git - Cloud Services
exl-id: 57e71b8a-4546-4d7f-825c-a1637d08e608
---
# Integrating Git with Adobe Cloud Manager {#git-integration}

Adobe Cloud Manager comes provisioned with a single git repository that is used to deploy code using Cloud Manager's CI/CD pipelines. Customers can use the Cloud Manager's git repository out of the box. Customers also have the option of integrating an on-premise or **customer-managed** git repository with Cloud Manager.

## Git Integration Overview {#git-integration-overview}

>[!VIDEO](https://video.tv.adobe.com/v/28710/)

This video series explores several use cases when it comes to integrating a customer-managed git repository with Cloud Manager, including:

* [Initial Sync](#initial-sync)
* [Basic Branching Strategy](#branching-strategy)
* [Feature Branch Development](#feature-development)
* [Production Deployment](#production-deployment)
* [Synchronizing Release Tags](#sync-tags)

The video series assumes a basic knowledge of git and source control management. See the [additional resources below](#additional-resources) for more details on git.

>[!NOTE]
>
>The steps and naming conventions outlined in this video series represent some best practices for working with a customer-managed git repository and Cloud Manager. It is expected that the conventions and workflows depicted would be adapted for individual development teams.

## Initial Sync {#initial-sync}

First steps for synchronizing a customer-managed Git repository with Cloud Manager's Git repository.

>[!VIDEO](https://video.tv.adobe.com/v/28711/?quality=12)

## Basic Branching Strategy {#branching-strategy}

Follow the video below to learn the basic branching strategies.

>[!VIDEO](https://video.tv.adobe.com/v/28712/?quality=12)

## Feature Branch Development {#feature-development}

Use a feature branch to isolate code changes in a customer-managed git repository and synchronize with Cloud Manager's git repository in order to use a non-production pipeline for code quality and validation testing.

>[!VIDEO](https://video.tv.adobe.com/v/28723/?quality=12)

## Production Deployment {#production-deployment}

Prepare code for a production release in a customer-managed git repository and synchronize with Cloud Manager's git repository in order to deploy to stage and production environments.

>[!VIDEO](https://video.tv.adobe.com/v/28724/?quality=12)

## Synchronizing Release Tags {#sync-tags}

Synchronize release tags from a Cloud Manager git repository into a customer-managed git repository in order to provide visibility as to what code has been deployed to stage and production environments.

>[!VIDEO](https://video.tv.adobe.com/v/28725/?quality=12)

## Additional Resources {#additional-resources}

* [GitHub Resources](https://try.github.io)
* [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials/what-is-version-control)
* [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
