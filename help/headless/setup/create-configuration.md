---
title: Create a Configuration - Headless Setup
description: Create a configuration as a first step to getting started with headless in AEM as a Cloud Service.
exl-id: 48801599-f279-4e55-8033-9c418d2af5bb
feature: Headless, Content Fragments,GraphQL API
role: Admin, Developer
---
# Create a Configuration - Headless Setup {#create-configuration}

As a first step to getting started with headless in AEM as a Cloud Service, you need to create a configuration.

## What is a Configuration? {#what-is-a-configuration}

The Configuration Browser provides a generic configuration API, content structure, resolution mechanism for configurations in AEM.

In the context of headless content management in AEM, think of a configuration as a workplace within AEM where you can create your Content Models, which define the structure of your future content and Content Fragments. You can have multiple configurations to separate these models.

If you are familiar with [page templates in a full-stack AEM implementation](/help/sites-cloud/authoring/page-editor/templates.md), the usage of configurations for the management of Content Models is similar.

## How to Create a Configuration {#how-to-create-a-configuration}

An administrator would only need to create a configuration once, or very seldomly when a new workspace is required for organizing your Content Models. For the purposes of this getting started guide, we only need to create one configuration.

For step-by-step details see [Enable Content Fragment Functionality in the Configuration Browser](/help/sites-cloud/administering/content-fragments/setup.md#enable-content-fragment-functionality-configuration-browser).

>[!NOTE]
>
>Configuration options in addition to **Content Fragment Models** and **GraphQL Persisted Queries** may be necessary depending on your implementation requirements.

## Next Steps {#next-steps}

Using this configuration, you can now move on to the second part of the getting started guide and [create Content Fragment Models](create-content-model.md).

>[!TIP]
>
>For complete details about the Configuration Browser, see the [Configuration Browser documentation](/help/implementing/developing/introduction/configurations.md).
