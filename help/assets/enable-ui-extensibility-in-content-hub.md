---
title: Enable UI extensibility in [!DNL Content Hub]
description: Learn about the UI extensibility capability of [!DNL Content Hub]. Extend Content Hub by integrating custom business workflows using Adobe App Builder.
feature: App Builder
role: User, Developer
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets."
exl-id:
---

# Enable UI extensibility in [!DNL Content Hub] {#content-hub-ui-extensibility}

[!DNL Content Hub] supports UI extensibility, enabling organizations to integrate custom business workflows directly into the Content Hub experience. Using Adobe App Builder, developers can add custom UI components that enable users to perform business-specific actions without leaving Content Hub.

You can add custom extensions to different areas of the [!DNL Content Hub] interface. [!DNL Content Hub] supports the following extension points:

* **Asset Card**
* **Collection Card**
* **Asset Details**
* **Bulk Action Bar**

>[!IMPORTANT]
>
>* Adobe App Builder is required to build and deploy UI extensions for Content Hub.
>* The App Builder skills for AI coding assistants support [!DNL Content Hub] UI extensions. You can use them to scaffold, build, test, and deploy extensions for all the extension points listed above.

To learn how to get started with UI extensibility and build custom extensions, see [Add UI extensions to Content Hub](#add-ui-extensibility-content-hub).

## View UI extensions in [!DNL Content Hub] {#view-ui-extensions}

Within [!DNL Content Hub], UI extensions can be added to the following extension points.

### Asset Card

On an asset card, select the [!UICONTROL More] (...) menu, then select [!UICONTROL Asset label] to open the custom dialog.

![Asset card showing the Asset label option](assets/asset-label.png)

The custom dialog displays the resource type and resource ID for the selected resource.

### Collection Card

On a collection card, select the [!UICONTROL More] (...) menu, then select [!UICONTROL Collection label] to open the custom dialog.

![Collection card showing the Collection label option](assets/collection-label.png)

### Asset Details

Open an asset and navigate to the Asset Details page. Select the **Asset Details Extension Tab** icon to open the UI extension.

![Asset Details page showing the Asset Details Extension Tab](assets/asset-details-extension-tab.png)

### Bulk Action Bar

Select one or more assets to display the Bulk Action Bar, then select [!UICONTROL Custom label] to open the custom dialog.

![Bulk Action Bar showing the Custom label option](assets/selection-bar-custom-label.png)

The custom dialog displays the custom logic you configured in the Extension App.

## Use cases for UI extensibility {#content-hub-ui-extensibility-use-cases}

Organizations can use [!DNL Content Hub] UI extensibility to integrate business-specific workflows into the asset distribution experience.

### Extend asset expiry

Organizations can implement an **Extend Expiry** workflow that allows users to request an extension for assets approaching expiration or that have already expired. Users submit the request through a custom extension panel, and the configured backend workflow routes it to the appropriate approvers.

After submitting the request, users see a confirmation message.

![Confirmation message](assets/configured-message.png)

### Send assets for printing

Organizations can implement a custom **Send to Print** workflow that allows users to initiate print fulfillment directly from [!DNL Content Hub]. Users can select an asset and trigger the custom action from the asset card or select multiple assets and initiate the workflow from the Bulk Action Bar. The configured backend can then process the request according to the organization's print fulfillment process.

## Prerequisites for adding the extensibility component {#content-hub-prerequisites}

Fulfil the following requirements before building UI extensions for [!DNL Content Hub]:

* Access to [!DNL Content Hub].
* Access to Adobe App Builder.
* Entitlement to Developer or System Administrator role within the organization.
* Adobe I/O command line tool (AIO CLI) installed on your local machine. This tool is essential for creating and deploying extension projects.
* Good understanding of JavaScript, Node.js, and React technologies.

## Add the UI extensibility component to [!DNL Content Hub] {#add-ui-extensibility-content-hub}

You can get started with UI extensibility in [!DNL Content Hub] in either of the following ways:

* **Through Adobe Support:** Contact [Adobe Support](https://helpx.adobe.com/business/enterprise.html) for assistance with UI extensibility in [!DNL Content Hub].
* **Using App Builder skills:** Use an AI coding assistant to guide you through building, testing, and deploying UI extensions. For details, see [Build the extension with App Builder skills](#build-with-app-builder-skills).

### Build the extension with App Builder skills {#build-with-app-builder-skills}

[!DNL Content Hub] UI extensions are supported by the App Builder skills. The skills guide your AI coding assistant through creating, testing, and deploying an extension that uses the `aem/assets/contenthub/1` extension point. This single extension point covers the Asset Card, Collection Card, Asset Details, and Bulk Action Bar extension points.

1. Install the App Builder skills from the [Adobe Skills repository](https://github.com/adobe/skills). For the installation options, see the repository README.

2. Describe the extension you want to build. For example: "Build a Content Hub extension that adds an Extend Expiry panel to Asset Details."

3. The skills scaffold the project from the [!DNL Content Hub] sample app by running `aio app init --repo adobe/aem-uix-examples/aem-assets-contenthub-sample`, and then customize it for your use case:
   * Set the extension ID.
   * Restrict the extension to specific delivery repositories by populating `allowedRepos`.
   * Keep only the extension points you need

4. Run `aio app run` to start the extension locally. Open the following URL in your browser to test it in [!DNL Content Hub], replacing `<delivery-repo>` with your [!DNL Content Hub] delivery host:

   `https://experience.adobe.com/?devMode=true&ext=https://localhost:9080&repoId=<delivery-repo>#/assets/contenthub/`

5. Deploy the extension to the Stage or Production workspace. To make the extension available to your organization, submit it for approval in Adobe Developer Console. An organization administrator then approves it in MyExchange.