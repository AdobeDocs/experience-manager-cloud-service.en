---
title: Upgrade Experience Manager enhanced connector for Workfront
description: Upgrade Experience Manager enhanced connector for Workfront
---
# Upgrade enhanced connector for Workfront {#upgrade-enhanced-connector-for-workfront}

Experience Manager Assets enables you to upgrade the enhanced connector for Workfront from a previous version to the latest version. 

To upgrade the enhanced connector for Workfront to the latest version:

1. Download the latest version of the enhanced connector from [Adobe Software Distribution](https://experience.adobe.com/#/downloads/content/software-distribution/en/aem.html?package=/content/software-distribution/en/details.html/content/dam/aem/public/adobe/packages/cq650/product/assets/workfront-tools.ui.apps.zip).

1. [Access](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/managing-code/accessing-repos.html?lang=en) and clone your AEM as a Cloud Service repository from Cloud Manager.

1. Open the cloned AEM as a Cloud Service repository using an IDE of your choice.

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

1. [Remove the dependencies on Hoodoo distribution points](remove-external-dependencies.md), if any.

1. Push the changes to the repository.

1. Run the pipeline to [deploy the changes to Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/deploy-code.html).
