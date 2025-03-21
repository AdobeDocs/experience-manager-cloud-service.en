---
title: AEM Assets View UI Extensibility
description: Learn about the UI Extensibility capability of AEM Assets View. AEM Assets View UI enables adding custom UI components to meet specific business needs.
feature: App Builder
role: User, Developer
exl-id: a11f7043-17cf-4331-b76c-d3db099c2411
---
# AEM Assets View UI Extensibility{#AEM-Assets-View-UI-Extensibility}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

AEM Assets View has UI Extensibility capability. This capability enables users to add custom UI components to Assets View UI to meet specific business needs that the AEM Assets View's out-of-the-box functionalities do not meet. This extensibility feature enhances the flexibility of AEM Assets View that enables organizations to adapt the interface for specific workflows and requirements. 
You can add your Extensions to Asset, Folder and Collection level. The added extension displays within a dedicated panel on the Asset, Collection, or Folder Details page.

>[!IMPORTANT]
>
> * AEM Assets View UI Extensibility is available with [Assets Ultimate](/help/assets/assets-ultimate-overview.md).
> * To get access to Assets view UI extensibility, [create and submit an Adobe Customer Support case](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).
> * You can provide documentation feedback by expanding Detailed Feedback options and clicking Report an issue.

## <a id="1"></a> How to access Assets View

Access the Assets view in the following ways:
![access-assets-view-ui](/help/assets/assets/access-assets-view.jpg)

## Where does UI Extensions display on the Assets View UI? {#ui-extensibility-panel-assets-view}

Within Assets View, navigate to the Details page of an asset, folder or a collection. This Details page has a dedicated panel that displays the added UI Extension.
![my workspace](/help/assets/assets/my-workspace-assets-view3.png)


## Prerequisites for Adding the Extensibility Component 

* [Access to Assets View](#1).
* Access to the [Adobe app builder](https://developer.adobe.com/app-builder/docs/overview/). 
* Entitled to Developer of System Admin role within the Organization. See [this](https://developer.adobe.com/uix/docs/guides/get-access/) for more information.
* Adobe IO command line tool (AIO CLI) must be installed on your local machines. This tool is essential for creating and deploying extension projects. See [this](https://developer.adobe.com/app-builder/docs/getting_started/#local-environment-set-up) for more information.
* Good understanding of JavaScript, Node.js, and React technologies.

## Adding UI Extensibility Component on Assets View UI{#Adding-UI-Extensibility-Component-on-Assets-View}

1. See [Getting Started](https://developer.adobe.com/uix/docs/getting-started/) for essential information on UI Extensions and the Adobe App Builder framework. Learn how UI Extensibility enables integration of custom logic and UI within Adobe Experience Cloud services and understand the architecture and workflow for implementing UI Extensions.
1. See [Guides](https://developer.adobe.com/uix/docs/guides/) for general information regarding UI Extensibility, including local environment setup, local preview, publishing, and management.
1. See [Common Concepts in Creating Extensions](https://developer.adobe.com/uix/docs/services/aem-assets-view/api/commons/) to understand the fundamentals required to develop a UI extension for the AEM Assets View.
1. Add custom side panels to the Assets View interface. The host application(Assets View) manages these panels to handle UI interactions such as toggling and deep linking. Extensions use the `aem/assets/details/1` extension point to integrate custom panels that specifies properties, such as panel ID, title, and content URL. Developers register custom panels with the `getPanels()` method and build routes to display custom content. For detailed implementation, including API references and code examples, see [Details View](https://developer.adobe.com/uix/docs/services/aem-assets-view/api/details-view/).
1. Set up your local environment and Experience the process of developing UI extensions in Assets view firsthand by creating your first UI extension. See [Step-by-step AEM Assets View Extension Development](https://developer.adobe.com/uix/docs/services/aem-assets-view/extension-development/) for more details.
1. Set up your app using the AIO CLI to generate the basic extension structure and required code. See [Code Generation for AEM Assets View](https://developer.adobe.com/uix/docs/services/aem-assets-view/code-generation/) for detailed information.
1. Test your extensions locally to ensure that they work as expected before deployment. Run your extension in a fully isolated environment or with partial isolation and connect your extension to the production AEM Assets View for testing. See [Troubleshooting - AEM Assets View Extensibility](https://developer.adobe.com/uix/docs/services/aem-assets-view/debug/) for detailed information.
