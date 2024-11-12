---
title: AEM Assets View UI Extensibility
description: Learn about the UI Extensibility capability of AEM Assets View. AEM Assets View UI enables adding custom UI components to meet specific business needs.   
feature: UI Extensibility
role: User, Developer
---
# AEM Assets View UI Extensibility{#AEM-Assets-View-UI-Extensibility}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

AEM Assets View has UI Extensibility capability. This capability enables users to add custom UI components to Assets View UI to meet specific business needs that the AEM Assets View's out-of-the-box functionalities don't meet. This extensibility feature enhances the flexibility of AEM Assets View that enables organizations to adapt the interface for specific workflows and requirements.
This capability is created using technologies such as Micro Frontends (MFEs) and Single-Page Applications (SPAs). These technologies create a modular design of Assets View. In this modular architecture of Assets View UI, Assets View is the host that manages core services and interactions, while custom extensions are independent components that communicate through defined APIs.  
Extensions add at **Asset level** and **Collection level**. To add the extension, navigate to the **Asset Details page** or **Collections Details page** and click **Behold a ToolTip** quick access element in the toolbar. This displays the **Behold a Title!** panel. This panel is the extensibility area for adding extensions.  
Extensions communicate with AEM Assets View through defined APIs, enabling seamless integration and customization. AEM Assets View UI Extensibility is available with [Assets Ultimate](/help/assets/assets-ultimate-overview.md).

## Where to add the UI Extensibility Component on Assets View? {#ui-extensibility-panel-assets-view}

Add your UI Extensibility component to the **Behold a Title!** panel on Assets View UI. Access this panel from Asset Details page and Collections Details Page. 

### Access from Asset Details page

1. [Navigate to Assets View](#1) 
1. Open the Asset details page and click ![Behold a ToolTip](/help/assets/assets/behold-tooltip.svg)(Behold a ToolTip!)  to display the **Behold a Title!** panel. Add your extension to this panel. See [Adding UI Extensibility Component on Assets View UI](#Adding-UI-Extensibility-Component-on-Assets-View) for information on how to add the component.
![extensibility panel](/help/assets/assets/extensibility-panel.png) 

### Access from Collections Details page:

1. [Navigate to Assets View](#1) 
1. Open the Collections details page and click ![Behold a ToolTip](/help/assets/assets/behold-tooltip.svg)(Behold a ToolTip!)  to display the **Behold a Title!** panel. Add your extension to this panel. See [Adding UI Extensibility Component on Assets View UI](#Adding-UI-Extensibility-Component-on-Assets-View) for information on how to add the component.
![extensibility panel at folder level](/help/assets/assets/extensibility-panel-folder-level.png)

>[!NOTE]
>
> AEM Assets View UI Extensibility is available to you as a Beta release. You can provide documentation feedback by expanding Detailed Feedback options and clicking Report an issue.

## Prerequisites for Adding the Extensibility Component 

* Access to Assets View. For more information, see the [Access Assets View](/help/assets/assets-view-introduction.md#access-assets-view) page.
* Access to the [Adobe app builder](https://developer.adobe.com/app-builder/docs/overview/), which is included in the [Assets Ultimate](/help/assets/assets-ultimate-overview.md) by default. 
* Entitled to Developer of System Admin role within the Organization. See [this](https://developer.adobe.com/uix/docs/guides/get-access/) for more information.
* Adobe IO command line tool (AIO CLI) must be installed on your local machines. This tool is essential for creating and deploying extension projects. See [this](https://developer.adobe.com/app-builder/docs/getting_started/#local-environment-set-up) for more information.
* Good understanding of JavaScript, Node.js, and React technologies.

## Adding UI Extensibility Component on Assets View UI{#Adding-UI-Extensibility-Component-on-Assets-View}

1. <a id="1"></a> Navigate to Assets View. Access the Assets view in the following ways:
![access-assets-view-ui](/help/assets/assets/access-assets-view.jpg)
1. See [Common Concepts in Creating Extensions](https://developer.adobe.com/uix/docs/services/aem-assets-view/api/commons/) to understand the fundamentals required to develop an extension for the AEM Assets View.
1. Add custom side panels to the interface. The host application(Assets View) manages these panels to handle UI interactions such as toggling and deep linking. Extensions use the `aem/assets/details/1` extension point to integrate custom panels that specifies properties, such as panel ID, title, and content URL. Developers register custom panels with the `getPanels()` method and build routes to display custom content. For detailed implementation, including API references and code examples, see [Details View](https://developer.adobe.com/uix/docs/services/aem-assets-view/api/details-view/).
1. Set up your local environment and Experience the process of developing UI extensions firsthand by creating your first UI extension. See [Step-by-step AEM Assets View Extension Development](https://developer.adobe.com/uix/docs/services/aem-assets-view/extension-development/) for more details.
1. Set up your app using the AIO CLI to generate the basic extension structure and required code. See [Code Generation for AEM Assets View](https://developer.adobe.com/uix/docs/services/aem-assets-view/code-generation/) for detailed information.
1. Test your extensions locally to ensure that they work as expected before deployment. Run your extension in a fully isolated environment or with partial isolation and connect your extension to the production AEM Assets View for testing. See [Troubleshooting - AEM Assets View Extensibility](https://developer.adobe.com/uix/docs/services/aem-assets-view/debug/) for detailed information.

See [Guides](https://developer.adobe.com/uix/docs/guides/) for general information regarding UI Extensibility, including local environment setup, local preview, publishing, and management.