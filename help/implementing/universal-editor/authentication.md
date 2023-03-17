---
title: Universal Editor Authentication
description: Learn how the Universal Editor authenticates.
---

# Universal Editor Authentication {#authentication}

Learn how the Universal Editor authenticates.

## Options {#options}

The Universal Editor uses Adobe's Identity Management System (IMS) authentication, which is provided via the Unified Shell.

All applications/remote pages are responsible for authentication to required backend systems. The Universal Editor service needs this authentication to backend systems to perform CRUD operations as it is a standalone service.

Depending on how you are using the Universal Editor, there are different options of implementation.

* [Standard Flow](#standard-flow) - For AEM as a Cloud Service or AMS using IMS
* [Third-Party Flow](#third-party-flow) - For AEM on-premise or AMS without IMS

## Standard Flow {#standard-flow}

This is the solution for AEM as a Cloud Service and AMS using IMS to use the Universal editor.

To use the Universal Editor, the user must be logged into the Unified Shell which authenticates against IMS. The provided IMS token is stored in the users session store.

Whenever a user performs a CRUD operation, a call is sent to the Universal Editor service with the IMS bearer token in the HTTP header. The Universal Editor service then uses the bearer token to authenticate the request against the AEM backend system to execute operations in the user's name.

![Standard authentication flow](assets/standard-flow.png)

## Additional Resources {#additional-resources}

To learn more about the Universal Editor, see these documents.

* [Universal Editor Introduction](introduction.md) - Learn how the Universal Editor enables editing any aspect of any content in any implementation in order to deliver exceptional experiences, increase content velocity, and provide a state-of-the-art developer experience.
* [Authoring Content with the Universal Editor](authoring.md) - Learn how easy and intuitive it is for content authors to create content using the Universal Editor.
* [Getting Started with the Universal Editor in AEM](getting-started.md) - Learn how to get access to the Universal Editor and how to start instrumenting your first AEM app to use it.
* [Universal Editor Architecture](architecture.md) - Learn about the architecture of the Universal Editor and how data flows between its services and layers.
* [Attributes and Types](attributes-types.md) - Learn about the data attributes and types that the Universal Editor requires.
