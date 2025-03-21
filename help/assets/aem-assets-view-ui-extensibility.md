---
title: Enable UI extensibility in [!DNL AEM Assets View] 
description: Learn about the UI Extensibility capability of [!DNL AEM Assets View]. [!DNL AEM Assets View] UI enables adding custom UI components to meet specific business needs.
feature: App Builder
role: User, Developer
exl-id: a11f7043-17cf-4331-b76c-d3db099c2411
---
# Enable UI extensibility in [!DNL AEM Assets View] {#AEM-Assets-View-UI-Extensibility}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

[!DNL AEM Assets View] supports UI extensibility enabling you to add custom UI components to your [!DNL Assets View] UI for specific workflows and business requirements that are not met by the out-of-the-box capabilities of [!DNL AEM Assets View]. This UI extensibility capability of [!DNL AEM Assets View] enhances its flexibility, enabling organizations to adapt the interface for specific workflows and requirements.  
You can add your extensions to **Asset**, **Folder** and **Collection** level. The added extension displays on a dedicated panel on the **Asset**, **Collection**, or **Folder** **[!UICONTROL Details]** page.

>[!IMPORTANT]
>
> * [!DNL AEM Assets View] UI extensibility is available with [[!DNL Assets Ultimate]](/help/assets/assets-ultimate-overview.md).
> * To get access to [!DNL Assets view] UI extensibility, [create and submit an [!DNL Adobe] Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).
> * You can provide documentation feedback by expanding **[!UICONTROL Detailed Feedback options]** and clicking **[!UICONTROL Report an issue]**.

## <a id="1"></a> Access the Assets View{#add-UI-Extensibility-in-AEM-Assets-View}

Follow the steps mentioned in the below image to access the [!DNL Assets View]:
![access-assets-view-ui](/help/assets/assets/access-assets-view.jpg)

## View UI extensions in [!DNL Assets View] {#ui-extensibility-panel-assets-view}

Within [!DNL Assets View], navigate to the **[!UICONTROL Details]** page of an asset, folder or a collection. The **[!UICONTROL Details]** page displays the added UI extension on a dedicated panel.
![my workspace](/help/assets/assets/my-workspace-assets-view3.png)

## Prerequisites for adding the extensibility component{#assets-view-ui-extensibility}

Fulfil the following requirements to start adding the extensibility component on your [!DNL Assets View UI]:

* [Access to [!DNL Assets View]](#1).
* Access to the [[!DNL Adobe app builder]](https://developer.adobe.com/app-builder/docs/overview/). 
* Entitlement to developer of system admin role within the organization. See [this documentation](https://developer.adobe.com/uix/docs/guides/get-access/) for more information.
* [!DNL Adobe IO command line tool (AIO CLI)] is installed on your local machines. This tool is essential for creating and deploying extension projects. See [this documentation](https://developer.adobe.com/app-builder/docs/getting_started/#local-environment-set-up) for more information.
* Good understanding of [!DNL JavaScript], [!DNL Node.js], and [!DNL React] technologies.

## Add the UI extensibility component to [!DNL Assets View] {#ui-extensibility-in-assets-view}

1. See [Getting Started](https://developer.adobe.com/uix/docs/getting-started/) for essential information on UI Extensions and the [!DNL Adobe App Builder] framework. Learn how UI Extensibility enables integration of custom logic and UI within [!DNL Adobe Experience Cloud services] and understand the architecture and workflow for implementing UI Extensions.
1. See [Guides](https://developer.adobe.com/uix/docs/guides/) for general information regarding UI Extensibility, including local environment setup, local preview, publishing, and management.
1. See [Common concepts in creating extensions](https://developer.adobe.com/uix/docs/services/aem-assets-view/api/commons/) to understand the fundamentals required to develop a UI extension for the [!DNL AEM Assets View].
1. Add custom side panels to the [!DNL Assets View] interface. The host application ([!DNL Assets View]) manages these panels to handle UI interactions such as toggling and deep linking. Extensions use the `aem/assets/details/1` extension point to integrate custom panels that specifies properties, such as panel ID, title, and content URL. Developers register custom panels with the `getPanels()` method and build routes to display custom content. For detailed implementation, including API references and code examples, see [Details View](https://developer.adobe.com/uix/docs/services/aem-assets-view/api/details-view/).
1. Set up your local environment and create your first UI extension to take a firsthand experience of the process of developing UI extensions in [!DNL Assets View]. See [Step-by-step AEM Assets View Extension Development](https://developer.adobe.com/uix/docs/services/aem-assets-view/extension-development/) for more details.
1. Set up your application using the AIO CLI to generate the basic extension structure and required code. See [code generation for [!DNL AEM Assets View]](https://developer.adobe.com/uix/docs/services/aem-assets-view/code-generation/) for detailed information.
1. Test your extensions locally to ensure that they work as expected before deployment. Run your extension in a fully isolated environment or with partial isolation and connect your extension to the production [!DNL AEM Assets View] for testing. See [Troubleshooting - [!DNL AEM Assets View] extensibility](https://developer.adobe.com/uix/docs/services/aem-assets-view/debug/) for detailed information.
