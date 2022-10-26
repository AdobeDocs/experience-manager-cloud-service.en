---
title: '[!DNL Experience Manager Assets] integration with [!DNL Adobe Workfront]'
description: Introduction to integration between [!DNL Assets] and [!DNL Workfront]
role: Admin,Leader,Architect
feature: Integrations
exl-id: 365de3dc-51db-4dcf-94e2-104b5a5d33a8
---
# [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] [!DNL Assets] integration with [!DNL Adobe Workfront] {#assets-integration-overview}

[!DNL Adobe Workfront] is a work management application that helps you manage the entire lifecycle of work in one place. The integration between [!DNL Workfront] and [!DNL Adobe Experience Manager Assets] lets organizations improve content velocity and time-to-market by intrinsically connecting work and digital asset management. Within the context of managing their work in Workfront, users have access to the required documents and images.

Adobe offers to [integrate [!DNL Workfront] and [!DNL Adobe Experience Manager Assets] natively (supporting Assets Essentials and Assets as a Cloud Service), using the Workfront for AEM connector, or using the Workfront for Experience Manager enhanced connector](https://experienceleague.adobe.com/docs/workfront/using/documents/wf-aem-integrations/wf-aem-essentials/aem-asset-integrations.html). In case of a native integration, you do not need a connector to integrate the two solutions.

>[!NOTE]
>
>Adobe does not support using the legacy or enhanced connectors and Experience Manager integration in parallel.

With the native Experience Manager integration and [!DNL Workfront for Experience Manager enhanced connector], you can:

|Native [!DNL Adobe Experience Manager Assets] features |[!DNL Workfront for Experience Manager enhanced connector] features |
|---|---|
| <ul><li>Quickly set up the integration inside of Workfront.</li><li>Automatically create folders linked between Workfront and Experience Manager.</li><li>Easily sync metadata for existing linked assets.</li><li>Automatically update project metadata when it's changed in Workfront.</li><li>Smoothly connect several Experience Manager Assets repositories to one Workfront environment, or several Workfront environments to one Experience Manager Assets repository across Organization IDs.</li> |<ul><li>Auto-create linked Experience Manager folders in Workfront and organize the folders based on Workfront Portfolios, Programs, and Projects.</li><li>Synchronize Workfront project metadata with linked Experience Manager folders.</li><li>Experience Manager metadata updates with new versions.</li><li>Set Workfront object statuses based on configurable conditions using Experience Manager workflows.</li><li>Publish assets to Experience Manager publish environment or to Brand Portal.</li> |

See the [supported features below for a comparison](#feature-parity-matrix) between native integration or an integration using connectors between the two solutions.



See the platform support and [prerequisites for the enhanced connector](https://one.workfront.com/s/csh?context=2467&pubname=the-new-workfront-experience).

>[!IMPORTANT]
>
>* Adobe requires deployment and configuration of the [!DNL Adobe Workfront for Experience Manager enhanced connector] only via certified partners or [!DNL Adobe Professional Services]. If deployed and configured without a certified partner or [!DNL Adobe Professional Services], it is not supported by Adobe.
>
>* Adobe may release updates to [!DNL Adobe Workfront] and [!DNL Adobe Experience Manager] that make this connector redundant; if this occurs, customers may be required to transition from the use of this connector.
>
>* Adobe supports enhanced connector versions 1.7.4 and higher. Previous prerelease and custom versions are not supported. To check the enhanced connector version, see step 5(a) of [enhanced connector installation instructions](workfront-connector-install.md). 
>
>* See [Partner certification exam for Workfront for Experience Manager Assets enhanced connector](https://solutionpartners.adobe.com/solution-partners/home/applications/experience_cloud/workfront/journey/dev_core.html). For information about the exam, see [Exam Guide](https://express.adobe.com/page/Tc7Mq6zLbPFy8/).

## Compare different integrations between [!DNL Assets] and [!DNL Workfront] {#feature-parity-matrix}

The following are the details of the functionalities available through various types of integrations between [!DNL Assets] and [!DNL Workfront].

| Feature   |Description  | [!DNL Workfront] and [!DNL Assets Essentials] *No Connector (OOTB)* | [!DNL Workfront] for [!DNL AEM] connector *Requires Connector*| [!DNL Workfront for Experience Manager enhanced connector] *Requires Connector*| Workfront and [!DNL Experience Manager as a Cloud Service] *No Connector (OOTB)*|
|----|----|----|------|-----|-----|
| Deployment methods   | Appropriate for which [!DNL Assets] offering. | Assets Essentials| Cloud Service, Adobe Managed Services, On-premise | Cloud Service, Adobe Managed Services, On-premise| Cloud Service, Adobe Managed Services, On-premise|
| **General** |
| Send digital files from [!DNL Workfront] to [!DNL Assets]| Latest version of a WF document can be uploaded to AEM Assets which will be linked as a new version of the document.  | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Manually Link AEM Folders to Workfront Objects| Existing AEM folders can be linked as a Workfront folder and its child assets are linked as new Workfront documents.  | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Link [!DNL Assets] to Workfront Objects | Existing assets in AEM can be linked to a new Workfront document or as a new version of an existing document. | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Assets added to linked folders are automatically sent to AEM| If document is added to a linked folder, the associated asset is automatically uploaded to AEM Assets as a new asset. | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Download Linked AEM Assets from within Workfront   | When an asset is linked in Workfront, the user can download the bytes of the asset. | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Search for AEM Assets from within Workfront| The AEM Assets selector in Workfront allows for full-text searches for assets. | &#10003; | &#10003;   | &#10003;  | &#10003; |
|Search for AEM Folders from within Workfront | The AEM Assets selector in Workfront allows for full-text searches for folders. | &#10003; | No   | &#10003;  | &#10003; |
| View and Navigate AEM Folder Hierarchy from within Workfront   | The AEM Assets selector in Workfront allows for browsing of the AEM Assets hierarchy limited by the   user's associated access controls and permissions set in AEM.  | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Track Asset versions in AEM timelines| Maintain document version history between Workfront and AEM. | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Unlink Assets from AEM Assets in Workfront | An existing linked asset from AEM can be unlinked from the associated Workfront document. This does not delete the original asset inside of AEM.| &#10003; | &#10003;   | &#10003;  | &#10003; |
| Add Newly Versioned Asset to AEM Assets from Workfront  | When a newly added version is added on a document in Workfront, a user can send the new version to AEM to replace the existing version.   | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Assets Linked in Workfront when Clicked Direct User to AEM| Users are directed to AEM to preview a linked asset from within Workfront.| &#10003; | &#10003;   | &#10003; | Upcoming |
| Automatically Create Linked AEM Folders in Workfront    | Automatically create linked AEM folders in Workfront using project statuses. Automatically, configure AEM folders based on Workfront Portfolios, Programs, and Projects.   | No  | No    | &#10003;  | No |
| Navigate directly to AEM repositories from Workfront| Allow users to navigate to available AEM repositories configured within Workfront. | &#10003; | No   | No  | &#10003; |
| Automatically create linked AEM folders in Workfront| Automatically create linked AEM folders in Workfront using the option available in the Documents tab. | &#10003; | No   | No  | &#10003; |
| Comment Syncing| Automatically sync comments for assets from [!DNL Workfront] to [!DNL Assets]| No  | &#10003;   | &#10003;  | No |
| Support multiple Workfront environments connecting to a single AEM environment| Users from multiple Workfront environments can connect to a single AEM environment. | &#10003; | No   | No  | &#10003; |
| Support multiple AEM environments connecting to a single Workfront environment| Users within a single Workfront environment can send or link assets between multiple AEM environments. | &#10003; | &#10003;   | &#10003;  | &#10003; |
| **Metadata** |
| Map Workfront Asset Metadata to AEM Assets | Workfront object and custom form properties may be mapped to AEM asset metadata properties. Values will be pushed on initial upload/link.    | &#10003; | &#10003;   | &#10003;  | &#10003; |
| Automatically Create Document Custom Forms in Workfront | Attach custom forms to Workfront documents, tasks, and issues using AEM workflows.| No  | Manually add the custom form, then automated syncing works | &#10003;  | No |
| Bi-directional Automatic Updating of Metadata between AEM Assets and Workfront   | Automatically update metadata between AEM Assets and Workfront. The asset must be initially pushed from Workfront to AEM and the Workfront asset metadata must be mapped to AEM assets for bi-directional metadata updates to work appropriately.| No  | &#10003;   | &#10003;  | No |
|Real-time view in Workfront for mapped metadata to AEM | View the updated mapped metadata to AEM within Workfront Document Details and Document Summary panels.  | &#10003; | No   | No  | &#10003; |
| Real-time push of updated Workfront metadata to AEM| Automatically update the mapped Workfront metadata to AEM without repushing an asset or a new version of an asset. | &#10003; | No   | No  | &#10003; |
| Map Workfront Metadata to AEM Assets Folders | Sync Workfront project metadata with linked AEM folders.| No  | No    | &#10003;  | &#10003; |
| AEM Metadata Updates with New Versions| A configuration in AEM can be made to determine whether a newly versioned asset in Workfront also pushes with any changes made to its metadata.  | No  | No    | &#10003;  | No |
| Automatically Update AEM Metadata on Changes to Custom Forms in Workfront| AEM allows you to subscribe to the updates to the document forms in Workfront. As a result, any updates to the Workfront document custom form metadata modifies the values for the mapped AEM metadata fields.     | No  | &#10003;   | &#10003;  | No |
| **Workflows (Out-of-the-box)** |
| Create New Proof Version on Linked Assets  | Upon linking an asset in Workfront a proof can be automatically generated.| No  | &#10003;   | Custom| No |
| Set Status on Workfront Objects  | Set Workfront object statuses based configurable conditions using AEM workflows| No  | No    | &#10003;  | Upcoming |
| Publish Assets to AEM Publish Environment or Brand Portal| Give Workfront users the option to automatically publish linked assets to an AEM Publish environment or Brand Portal. | No  | No    | &#10003;  | Upcoming |
