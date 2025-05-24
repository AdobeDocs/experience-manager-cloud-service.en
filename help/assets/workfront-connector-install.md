---
title: Install [!DNL Workfront for Experience Manager enhanced connector]
description: Install [!DNL Workfront for Experience Manager enhanced connector]
role: Admin
feature: Workfront Integrations and Apps
exl-id: 2907a3b2-e28c-4194-afa8-47eadec6e39a
---
# Install [!DNL Workfront for Experience Manager enhanced connector] {#assets-integration-overview}

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
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/integrations/workfront-connector-install.html)                  |
| AEM as a Cloud Service     | This article         |

A user with administrator access in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] installs the enhanced connector. Before you install, review the platform support and other [prerequisites for the connector](https://one.workfront.com/s/csh?context=2467&pubname=the-new-workfront-experience).

>[!IMPORTANT]
>
>As of June 2022, Adobe released a new native integration for connecting Workfront with Adobe Experience Manager Assets as a Cloud Service. This integration has become the required method for connecting these two solutions. Any future new implementation of the enhanced connector (1.9.8 and later) to connect Workfront with AEM Assets as a Cloud Service is blocked. For more information on how to setup this integration, see [Configure the Experience Manager Assets as a Cloud Service integration](workfront-connector-configure.md).

>[!IMPORTANT]
>
>* Adobe requires deployment and configuration of the [!DNL Adobe Workfront for Experience Manager enhanced connector] only via certified partners or [!DNL Adobe Professional Services]. If deployed and configured without a certified partner or [!DNL Adobe Professional Services], it is not supported by Adobe.
>
>* Adobe may release updates to [!DNL Adobe Workfront] and [!DNL Adobe Experience Manager] that make this connector redundant; if this occurs, customers may be required to transition from the use of this connector.
>
>* Adobe supports enhanced connector versions 1.7.4 and higher. Previous prerelease and custom versions are not supported. To check the enhanced connector version, see step 5(a) of [enhanced connector installation instructions](workfront-connector-install.md). 
>
>* See [Partner certification exam for Workfront for Experience Manager Assets enhanced connector](https://solutionpartners.adobe.com/solution-partners/home/applications/experience_cloud/workfront/journey/dev_core.html). For information about the exam, see [Exam Guide](https://express.adobe.com/page/Tc7Mq6zLbPFy8/).

Before you install the connector, follow these pre-installation steps:

1. If your AEM as a Cloud Service Program has configured Advanced Networking and enabled IP Allow-Listing, then you need to add the Workfront IPs to this allow-list to permit Event Subscriptions and various API calls to pass through into AEM.

   * [Workfront Cluster IPs](https://experienceleague.adobe.com/docs/workfront/using/administration-and-setup/get-started-administration/configure-your-firewall.html?lang=en#ip-addresses-to-allow-for-clusters-1-2-3-5-7-8-and-9). To know the IP cluster in [!DNL Workfront], navigate to **[!UICONTROL Setup]** > **[!UICONTROL System]** > **[!UICONTROL Customer Info]**.

   * [Workfront Event Subscription API IPs](https://experienceleague.adobe.com/docs/workfront/using/adobe-workfront-api/event-subscriptions/event-subs-api.html)

   >[!IMPORTANT]
   >
   >* If you have Advanced Networking configured for your program and are using IP Allow Listing, then due to a limitation with the Enhanced Workfront Connector architecture you also need to add the program egress IP to the allow-list in Cloud Manager.
   >
   >* p{PROGRAM_ID}.external.adobeaemcloud.com
   >
   >* To find the IP of your program, open a terminal window and run a command, such as:
   >
   >    ```
   >    dscacheutil -q host -a name p{PROGRAM_ID}.external.adobeaemcloud.com
   >
   >    ```

1. Ensure that the following overlays do not exist in [!DNL Experience Manager] repository. If you have pre-existing overlays on these paths you either need to remove the overlays, or merge the delta of changes between the two:

   * `/apps/dam/gui/coral/components/admin/schemaforms/formbuilder`
   * `/apps/dam/gui/coral/components/admin/folderschemaforms/formbuilder`
   * `/apps/dam/gui/content/foldermetadataschemaeditor`
   * `/apps/dam/cfm/models/editor/components/datatypeproperties`
   * `/apps/settings/dam/cfm/models/formbuilderconfig`
   * `/apps/dam/gui/content/assets/jcr:content/actions/secondary/create/items/fileupload`

1. This installation requires the knowledge to set a Maven project in [!DNL Experience Manager] as a [!DNL Cloud Service]. Use the following resources to understand how to include a third-party package in your Maven project:

   * [Include third-party package in your Maven project](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/overview.html#including-third-party).
   * [Deploy with [!DNL Cloud Manager]](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/deploy-code.html).

To install the add-on in [!DNL Experience Manager] as a [!DNL Cloud Service], follow these steps:

1. Download the enhanced connector from [Adobe Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aem.html?package=/content/software-distribution/en/details.html/content/dam/aem/public/adobe/packages/cq650/product/assets/workfront-tools.ui.apps.zip).

1. [Access](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/managing-code/accessing-repos.html?lang=en) and clone your AEM as a Cloud Service repository from Cloud Manager.

1. Open the cloned AEM as a Cloud Service repository using an IDE of your choice.

1. Place the enhanced connector zip file downloaded in Step 1 at the following path:

   ```TXT
      /ui.apps/src/main/resources/<zip file>
   ```

   >[!NOTE]
   >
   >If the `resources` folder does not exist, create the folder.


1. Add `pom.xml` dependencies:

   1. Add a dependency in parent `pom.xml`.

      ```XML
      <dependency>
         <groupId>digital.hoodoo</groupId>
         <artifactId>workfront-tools.ui.apps</artifactId>
         <type>zip</type>
         <version>enhanced connector version number</version>
         <scope>system</scope>
         <systemPath>${project.basedir}/ui.apps/src/main/resources/workfront-tools.ui.apps.zip</systemPath>
      </dependency>
      ```

       >[!NOTE]
       >
       >Ensure to update the enhanced connector version number before copying the dependency to the parent `pom.xml`.

   1. Add a dependency in `all module pom.xml`.

      ```XML
         <dependency>
            <groupId>digital.hoodoo</groupId>
            <artifactId>workfront-tools.ui.apps</artifactId>
            <type>zip</type>
            <scope>system</scope>
            <systemPath>${project.basedir}/../ui.apps/src/main/resources/workfront-tools.ui.apps.zip</systemPath>
         </dependency>
      ```


1. Add `pom.xml` embeds. Add the [!DNL Workfront for Experience Manager enhanced connector] packages to `embeddeds` section of the `pom.xml` of all your subproject. Needs it embedded in the all module `pom.xml`.

      ```XML
      <!-- Workfront Tools -->
      <embedded>
         <groupId>digital.hoodoo</groupId>
         <artifactId>workfront-tools.ui.apps</artifactId>
         <type>zip</type>
         <target>/apps/<path-to-project-install-folder>/install</target>
      </embedded>
      ```

   The target of the embedded section is set to `/apps/<path-to-project-install-folder>/install`. This JCR path `/apps/<path-to-project-install-folder>` must be included in the filter rules in the `all/src/main/content/META-INF/vault/filter.xml` file. The filter rules for the repository are usually derived from the program name. Use the name of the folder as the target in the existing rules.

1. Push the changes to the repository.

1. Run the pipeline to [deploy the changes to Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/deploy-code.html).

1. To create a system user configuration, create `wf-workfront-users` in [!DNL Experience Manager] User Group and assign the permission `jcr:all` to `/content/dam`. A system user `workfront-tools` is automatically created and the required permissions are managed automatically. All users from [!DNL Workfront] who use the enhanced connector are automatically added as a part of this group.

For information to update the [!DNL Workfront for Experience Manager enhanced connector] from a previous version to the latest version, click [here](update-workfront-enhanced-connector.md).

## Configure the connection between [!DNL Experience Manager] as a [!DNL Cloud Service] and [!DNL Workfront] {#configure-connection}

To create a connection with [!DNL Workfront], follow these steps:

1. In [!DNL Experience Manager], select **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** > **[!UICONTROL Workfront Tools Configuration]**.

1. Select `workfront-tools` in the left panel and select **[!UICONTROL Create]** option in the upper-right area of the page.

1. In the **[!UICONTROL Workfront Connection]** dialog, provide the required details of your [!DNL Workfront] deployment, and select **[!UICONTROL Connect to Workfront]** option. Once successfully connected, the [!DNL Workfront] document custom integration is auto-created in the [!DNL Workfront] environment.

   ![Connect [!DNL Experience Manager] and [!DNL Workfront]](/help/assets/assets/wf-connection-config.png)

1. Navigate to the **[!UICONTROL Advanced]** tab and select the option **[!UICONTROL Is the Server AEM as a Cloud Service]**.
