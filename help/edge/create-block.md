---
title: Creating Blocks Instrumented for use with the Universal Editor
description: Learn how to create new blocks instrumented for use with the Universal Editor in AEM authoring with Edge Delivery Services projects.
---

# Creating Blocks Instrumented for use with the Universal Editor {#create-block}

Learn how to create new blocks instrumented for use with the Universal Editor in AEM authoring with Edge Delivery Services projects.

{{aem-authoring-edge-early-access}}

## Prerequisites {#prerequisites}

This guide provides step-by-step instructions on how to create new blocks instrumented for Universal Editor in AEM authoring with Edge Delivery Services projects. It covers adding components, loading component definitions in Universal Editor, publishing pages, implementing block decoration and styles, bringing the changes to production, and verifying them. Following this guide you can effectively create and deploy a new blocks.

This guide necessarily requires existing knowledge of AEM authoring with Edge Delivery Services projects as well as the Universal Editor. Before beginning this guide, you should already have access to Edge Delivery Services and be familiar with its basics including:

* You have completed the [Edge Delivery Service tutorial.](/help/edge/developer/tutorial.md)
* You have access to an [AEM Cloud Service sandbox.](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md)
* You have [enabled the Universal Editor on the same sandbox environment.](/help/implementing/universal-editor/getting-started.md)
* You have completed the [Developer Getting Started Guide for AEM Authoring with Edge Delivery Services](/help/edge/edge-dev-getting-started.md) guide.

## Add a New Block to Your Project {#add-block}

1. Clone the GitHub project you created in the [Developer Getting Started Guide for AEM Authoring with Edge Delivery Services](/help/edge/edge-dev-getting-started.md) guide and open it in an editor of your choice.

   ![Cloning the project](assets/create-block/clone.png)

1. Edit the `component-definition.json` at the root of the project.

