---
title: Update [!DNL Workfront for Experience Manager enhanced connector]
description: Update [!DNL Workfront for Experience Manager enhanced connector]
exl-id: 09276b4d-a7c8-4927-8c0a-40eda48e55a7
feature: Workfront Integrations and Apps
role: Admin
---
# Update [!DNL Workfront for Experience Manager enhanced connector] {#update-enhanced-connector-for-workfront}

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

[!UICONTROL Experience Manager Assets as a Cloud Service] enables you to update the [!DNL Workfront for Experience Manager enhanced connector] from a previous version to the latest version.

>[!TIP]
>
>Are you searching for [!DNL Workfront for Experience Manager enhanced connector] update documentation for AEM 6.5? Click [here](https://experienceleague.adobe.com/docs/experience-manager-65/assets/integrations/workfront-connector-install.html?lang=en##update-enhanced-connector-for-workfront).


To update the [!DNL Workfront for Experience Manager enhanced connector] to the latest version:

1. Download the latest version of the enhanced connector from [Adobe Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aemcloud.html?package=/content/software-distribution/en/details.html/content/dam/aemcloud/public/workfront-tools.ui.apps.zip).

1. [Access](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/managing-code/accessing-repos.html?lang=en) and clone your AEM as a Cloud Service repository from Cloud Manager.

1. Open the cloned Experience Manager as a Cloud Service repository using an IDE of your choice.

1. Place the enhanced connector zip file downloaded in Step 1 at the following path:

   ```TXT
      /ui.apps/src/main/resources/<zip file>
   ```

   >[!NOTE]
   >
   >If the `resources` folder does not exist, create the folder.

1. Update the enhanced connector version in parent `pom.xml`.

   ```XML
      <dependency>
         <groupId>digital.hoodoo</groupId>
         <artifactId>workfront-tools.ui.apps</artifactId>
         <type>zip</type>
         <version> updated enhanced connector version number</version>
         <scope>system</scope>
         <systemPath>${project.basedir}/ui.apps/src/main/resources/workfront-tools.ui.apps.zip</systemPath>
      </dependency>
   ```

1. Update the dependency in `all module pom.xml`.

      ```XML
         <dependency>
            <groupId>digital.hoodoo</groupId>
            <artifactId>workfront-tools.ui.apps</artifactId>
            <type>zip</type>
            <scope>system</scope>
            <systemPath>${project.basedir}/../ui.apps/src/main/resources/workfront-tools.ui.apps.zip</systemPath>
         </dependency>
      ```

   >[!NOTE]
   >
   >Ensure that you add `<scope>` and `<systemPath>` to the dependencies in step 5 and step 6.

1. Update `pom.xml` embeds. Add the [!DNL Workfront for Experience Manager enhanced connector] packages to `embeddeds` section of the `pom.xml` of all your subproject. Incorporate the updates in all module `pom.xml`.

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

1. [Remove the dependencies on Hoodoo distribution points](remove-external-dependencies.md), if any.

1. Push the changes to the repository.

1. Run the pipeline to [deploy the changes to Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/deploy-code.html).
