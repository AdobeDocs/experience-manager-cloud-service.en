---
title: Using the GraphiQL IDE in AEM
description: Learn how to use the GraphiQL IDE in Adobe Experience Manager.
feature: Content Fragments,GraphQL API
---

# Using the GraphiQL IDE {#graphiql-ide}

An implementation of the standard [GraphiQL](https://graphql.org/learn/serving-over-http/#graphiql) IDE is available for use with AEM GraphQL. This can be [installed with AEM](#installing-graphiql-ide).

>[!NOTE]
>
>GraphiQL is bound the global endpoint (and does not work with other endpoints for specific Sites configurations).

The GraphiQL tool allows you to directly input, test, and debug queries. GraphiQL also provides easy access to the documentation, making it easy to learn and understand what methods are available.

For example: 

* `http://localhost:4502/content/graphiql.html`

This provides features such as syntax-highlighting, auto-complete, auto-suggest, together with a history and online documentation:

![GraphiQL Interface](assets/cfm-graphiql-interface.png "GraphiQL Interface")

## Installing the AEM GraphiQL IDE {#installing-graphiql-ide}

The GraphiQL IDE is a development tool and needed only on lower-level environments like a development or local instance. Therefore it is not included in the AEM project, but comes as a separate package that can be installed on an ad-hoc basis.

1. Navigate to the **[Software Distribution Portal](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html)** > **AEM as a Cloud Service**.
1. Search for "GraphiQL" (be sure to include the **i** in **GraphiQL**.
1. Download the latest **GraphiQL Content Package v.x.x.x**
1. From the **AEM Start** menu navigate to **Tools** > **Deployment** > **Packages**.
1. Click **Upload Package** and choose the package downloaded in the prior step. Click **Install** to install the package.

