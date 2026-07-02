---
title: Enable UI extensibility in [!DNL Content Hub]
description: Learn about the UI extensibility capability of [!DNL Content Hub]. Extend Content Hub by integrating custom business workflows using Adobe App Builder.
feature: App Builder
role: User, Developer
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets."
exl-id: 
---

# Enable UI extensibility in [!DNL Content Hub] {#content-hub-ui-extensibility}

[!DNL Content Hub] supports UI extensibility, enabling organizations to integrate custom business workflows directly into the Content Hub experience. Powered by Adobe App Builder, UI extensibility allows developers to add custom panels that enable users to perform business-specific actions without leaving Content Hub.

You can add custom extensions to the **Asset Details** page. The added extension appears as a dedicated panel where users can perform custom workflows on the selected asset.

>[!IMPORTANT]
>
>* UI extensibility for [!DNL Content Hub] is generally available (GA).
>* Adobe App Builder is required to build and deploy Content Hub extensions.
>* You can provide documentation feedback by expanding **[!UICONTROL Detailed Feedback options]** and selecting **[!UICONTROL Report an issue]**.

## Access Content Hub {#access-content-hub}

Follow the steps shown in the following image to access [!DNL Content Hub].

![Placeholder - Access Content Hub](assets/content-hub-access.png)

## View UI extensions in Content Hub {#view-ui-extensions}

Open an asset in [!DNL Content Hub] and navigate to the **[!UICONTROL Asset Details]** page. If a custom extension is installed and configured, it appears as a dedicated panel within the Asset Details interface.

![Placeholder - Content Hub Asset Details](assets/content-hub-details-panel.png)

## Prerequisites {#prerequisites}

Ensure that the following prerequisites are met before developing UI extensions for [!DNL Content Hub]:

* Access to [!DNL Content Hub].
* Access to Adobe App Builder.
* Developer or System Administrator permissions within your organization.
* Adobe I/O CLI (AIO CLI) installed on your local machine.
* Working knowledge of JavaScript, Node.js, and React.

## Add the UI extensibility component to Content Hub {#add-ui-extensibility-content-hub}

1. See **Getting Started** for an overview of Adobe App Builder and the UI extensibility framework.

1. See **Guides** for information about local development, preview, deployment, and extension management.

1. See **Common concepts** to understand the fundamentals required to build Content Hub extensions.

1. Add a custom panel to the **Asset Details** page. The custom panel enables users to perform business-specific actions directly within Content Hub. For implementation details, API references, and code examples, see the developer documentation.

1. Set up your local development environment and build your extension.

1. Deploy the extension to your target workspace and verify that it is available within Content Hub.

## Extend Content Hub workflows {#extend-content-hub-workflows}

UI extensibility enables organizations to bring business workflows directly into Content Hub. Instead of switching between multiple applications, users can complete workflow-specific actions from within the Content Hub interface.

For example, organizations can implement an **Extend Expiry** workflow that allows users to request an extension for assets approaching expiration. Users submit the request from the extension panel, while the configured backend workflow processes the request and routes it for approval.

![Placeholder - Extend Expiry workflow](assets/content-hub-extend-expiry.png)

>[!NOTE]
>
>Implementation details, architecture, APIs, local development, deployment, and troubleshooting are covered in the developer documentation.