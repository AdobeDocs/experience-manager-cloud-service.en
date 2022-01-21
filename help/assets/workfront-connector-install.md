---
title: Install [!DNL Workfront for Experience Manager enhanced connector]
description: Install [!DNL Workfront for Experience Manager enhanced connector]
role: Admin
feature: Integrations
exl-id: 2907a3b2-e28c-4194-afa8-47eadec6e39a
---
# Install [!DNL Workfront for Experience Manager enhanced connector] {#assets-integration-overview}

A user with administrator access in [!DNL Adobe Experience Manager] as a [!DNL Cloud Service] installs the enhanced connector. Before you install, review the platform support and other [prerequisites for the connector](https://one.workfront.com/s/csh?context=2467&pubname=the-new-workfront-experience).

>[!IMPORTANT]
>
>Adobe requires deployment and configuration of the [!DNL Adobe Workfront for Experience Manager enhanced connector] only via certified partners or [!DNL Adobe Professional Services]. If deployed and configured without a certified partner or [!DNL Adobe Professional Services], it is not supported by Adobe.
>
>Adobe may release updates to [!DNL Adobe Workfront] and [!DNL Adobe Experience Manager] that make this connector redundant; if this occurs, customers may be required to transition from the use of this connector.

Before you install the connector, follow these pre-installation steps:

1. [Configure the firewall](https://one.workfront.com/s/document-item?bundleId=the-new-workfront-experience&topicId=Content%2FAdministration_and_Setup%2FGet_started-WF_administration%2Fconfigure-your-firewall.html). To know the IP cluster in [!DNL Workfront], navigate to [!UICONTROL Setup] > [!UICONTROL System] > [!UICONTROL Customer Info].

1. On the dispatcher, allow HTTP headers named `authorization`, `username`, and `apikey`. Allow `GET`, `POST`, and `PUT` requests to `/bin/workfront-tools`.

1. Ensure that the following paths do not exist in [!DNL Experience Manager] repository:

   * `/apps/dam/gui/coral/components/admin/schemaforms/formbuilder`
   * `/apps/dam/gui/coral/components/admin/folderschemaforms/formbuilder`
   * `/apps/dam/gui/content/foldermetadataschemaeditor`
   * `/apps/dam/cfm/models/editor/components/datatypeproperties`
   * `/apps/settings/dam/cfm/models/formbuilderconfig`

1. This installation requires the knowledge to set a Maven project in [!DNL Experience Manager] as a [!DNL Cloud Service]. Use the following resources to understand how to include a third-party package in your Maven project:

   * [Include third-party package in your Maven project](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/overview.html#including-third-party).
   * [Deploy with [!DNL Cloud Manager]](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/deploy-code.html).

To install the add-on in [!DNL Experience Manager] as a [!DNL Cloud Service], follow these steps:

1. Add `pom.xml` dependencies:

   1. Add a dependency in parent `pom.xml`.

      ```XML
      <dependency>
         <groupId>digital.hoodoo</groupId>
         <artifactId>workfront-tools.ui.apps</artifactId>
         <type>zip</type>
         <version>1.7.4</version>
      </dependency>
      ```

   1. Add a dependency in all module [!DNL pom.xml].

      ```XML
         <dependency>
            <groupId>digital.hoodoo</groupId>
            <artifactId>workfront-tools.ui.apps</artifactId>
            <type>zip</type>
         </dependency>
      ```

1. Add `pom.xml` authentication. 

   1. Include the below repository configuration in the pom.xml within adobe-public profile, so the connector dependencies (above) can be resolved at build time (both locally, and by Cloud Manager). Credentials for repository access will be provided upon the purchase of a license. The credentials will need to be added to the settings.xml file in the servers section.

      ```XML
      <repository>
         <id>hoodoo-maven</id>
         <name>Hoodoo Repository</name>
         <url>https://gitlab.com/api/v4/projects/12715200/packages/maven</url>
      </repository>
      ```

   1. Create a file named `./cloudmanager/maven/settings.xml` in the project root. To support a password-protected Maven repository, see [how to set up your project](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/setting-up-project.md). Additionally, an example `settings.xml` file for reference. Lastly, update your local `settings.xml` to compile locally.

      ```XML
         <server>
            <id>hoodoo-maven</id>
            <configuration>
               <httpHeaders>
                     <property>
                        <name>Deploy-Token</name>
                        <value>xxxxxxxxxxxxxxxx</value>
                     </property>
               </httpHeaders>
            </configuration>
         </server>
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

1. To create a system user configuration, create `wf-workfront-users` in [!DNL Experience Manager] User Group and assign the permission `jcr:all` to `/content/dam`. A system user `workfront-tools` is automatically created and the required permissions are managed automatically. All users from [!DNL Workfront] who use the enhanced connector are automatically added as a part of this group.

## Configure the connection between [!DNL Experience Manager] as a [!DNL Cloud Service] and [!DNL Workfront] {#configure-connection}

To create a connection with [!DNL Workfront], follow these steps:

1. In [!DNL Experience Manager], select **[!UICONTROL Tools]** > **[!UICONTROL Cloud Services]** > **[!UICONTROL Workfront Tools Configuration]**.

1. Select `workfront-tools` in the left panel and select **[!UICONTROL Create]** option in the upper-right area of the page.

1. In the **[!UICONTROL Workfront Connection]** dialog, provide the required details of your [!DNL Workfront] deployment, and select **[!UICONTROL Connect to Workfront]** option. Once successfully connected, the [!DNL Workfront] document custom integration is auto-created in the [!DNL Workfront] environment.

   ![Connect [!DNL Experience Manager] and [!DNL Workfront]](/help/assets/assets/wf-connection-config.png)

1. Navigate to the **[!UICONTROL Advanced]** tab and select the option **[!UICONTROL Is the Server AEM as a Cloud Service]**.
