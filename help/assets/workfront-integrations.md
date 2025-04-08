---
title: '[!DNL Experience Manager Assets] integration with [!DNL Adobe Workfront]'
description: Introduction to integration between [!DNL Assets] and [!DNL Workfront]
role: Admin, Leader, Architect
feature: Workfront Integrations and Apps
exl-id: 365de3dc-51db-4dcf-94e2-104b5a5d33a8
---
# [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] [!DNL Assets] integration with [!DNL Adobe Workfront] {#assets-integration-overview}

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

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/integrations/workfront-integrations.html)                  |
| AEM as a Cloud Service     | This article         |

[!DNL Adobe Workfront] is a work management application that helps you manage the entire lifecycle of work in one place. The integration between [!DNL Workfront] and [!DNL Adobe Experience Manager Assets] lets organizations improve content velocity and time-to-market by intrinsically connecting work and digital asset management. Within the context of managing their work in Workfront, users have access to the required documents and images.

Adobe offers to [integrate [!DNL Workfront] and [!DNL Adobe Experience Manager Assets] natively (supporting Assets Essentials and Assets as a Cloud Service)](https://experienceleague.adobe.com/docs/workfront/using/documents/wf-aem-integrations/wf-aem-essentials/aem-asset-integrations.html).

With the native Experience Manager integration, you can:

* Quickly set up the integration inside of Workfront.

* Automatically create folders linked between Workfront and Experience Manager.

* Easily sync metadata for existing linked assets.

* Automatically update project metadata when it's changed in Workfront.

* Smoothly connect several Experience Manager Assets repositories to one Workfront environment, or several Workfront environments to one Experience Manager Assets repository across Organization IDs.


## Adobe Workfront for Experience Manager enhanced connector {#enhanced-connector-information}


As of June 2022, Adobe released a new native integration for connecting Workfront with Adobe Experience Manager Assets as a Cloud Service. This integration has become the required method for connecting these two solutions. Any future new implementation of the enhanced connector (1.9.8 and later) to connect Workfront with AEM Assets as a Cloud Service is blocked. For more information on how to setup this integration, see [Configure the Experience Manager Assets as a Cloud Service integration](workfront-connector-configure.md).

>[!NOTE]
>
>Adobe does not support using the Workfront for Experience Manager enhanced connector and Experience Manager integration in parallel.

For installations prior to June 2022, the following are some points to note for the deployment and configuration of [!DNL Adobe Workfront for Experience Manager enhanced connector]:

* Adobe requires deployment and configuration of the [!DNL Adobe Workfront for Experience Manager enhanced connector] only via certified partners or [!DNL Adobe Professional Services]. If deployed and configured without a certified partner or [!DNL Adobe Professional Services], it is not supported by Adobe.
* Adobe may release updates to [!DNL Adobe Workfront] and [!DNL Adobe Experience Manager] that make this connector redundant; if this occurs, customers may be required to transition from the use of this connector.
* Adobe supports enhanced connector versions 1.7.4 and higher. Previous prerelease and custom versions are not supported. To check the enhanced connector version, see step 5(a) of [enhanced connector installation instructions](workfront-connector-install.md).
* See [Partner certification exam for Workfront for Experience Manager Assets enhanced connector](https://solutionpartners.adobe.com/solution-partners/home/applications/experience_cloud/workfront/journey/dev_core.html). For information about the exam, see [Exam Guide](https://express.adobe.com/page/Tc7Mq6zLbPFy8/).