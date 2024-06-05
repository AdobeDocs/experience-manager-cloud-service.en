---
title: Using Content Transformer
description: Learn how to transform your content structure in preparation for migrating to AEM as a Cloud Service.
exl-id: 40516ff7-5686-42e6-bdd1-c9c6de432b09
feature: Migration
role: Admin
---
# Using Content Transformer {#using-ct}

## Important Considerations for Using Content Transformer {#imp-considerations-ct}

Follow the section below to understand the important considerations for using the Content Transformer (CT):

* To use the Content Transformer, you must first run the Best Practices Analyzer on your Adobe Experience Manager (AEM) environment. 
* Although you can run the Content Transformer on your Production environment, it is recommended that you run the Content Transformer on a clone of your Production environment. More importantly, you need to ensure that the BPA and the CT are run on the same environment.
* You need to be an admin on the environment where you want to run the Content Transformer.
* Any operation that can change the source content ( move/remove/rename ) will by default create a backup package of the source paths under `/etc/packages/content-transformation` before the transformation. Although each operation dialog has an option to disable/enable backup package creation, it is strictly recommended to always have the enable package creation selected.
* Each page in the Content Transformer is configured to list a maximum of 50 findings, hence at a time a maximum of 50 findings can be transformed. This is done to provide a timeliness response on the UI. 

## Availability {#availability-ct}

The Content Transformer is bundled with the [Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/getting-started-content-transfer-tool.md) that can be downloaded as a zip file from the Software Distribution Portal. You can install the package via Package Manager on your source AEM instance.

>[!NOTE]
>The Content Transformer is available with Content Transfer Tool v2.0.20  or higher.

## Opening the Content Transformer {#opening-ct}

1. Log in to the source AEM instance as an administrator and go to the start page: https://host:port/aem/start.html.
1. Navigate to Tools > Operations > Content Migration

   ![image](/help/journey-migration/content-transformer/assets/ct-1.png)

   >[!NOTE]
   > Ensure that you have run the BPA report before, and verify it with the URL http://host:port/apps/best-practices-analyzer/content/BestPracticesReport.html

1. Click the card with title **Content Transformer for BPA report**

   ![image](/help/journey-migration/content-transformer/assets/ct-2.png)

   Below is an example of how the Content Transformer Overview page will look like if the creation of the BPA report was successful and if it found content related issues.

   The expiration time left for the BPA report is shown on the side rail. It is recommended to run the Content transformer with the latest BPA report to avoid missing any content-related findings. 

   ![image](/help/journey-migration/content-transformer/assets/ct-3.png)

1. You can filter the issues based on `Pattern Code`, `Subtype`, `Importance`, and `Source`.

   ![image](/help/journey-migration/content-transformer/assets/ct-4.png)

1. You can select all or specific issues and move, remove, or rename to resolve them. Custom paths can also be added using **Add Paths** button on the top-right corner.

   >[!NOTE]
   > When using the move operation, it is recommended to move all the paths to only one folder (for example, under `/etc/packages/content-transformation/paths`), so when the backup packages are installed to bring the instance back to the original state, the folder (`/etc/packages/content-transformation/paths`) can be deleted using remove operation to reduce the repository size.

   ![image](/help/journey-migration/content-transformer/assets/ct-5.png)
   ![image](/help/journey-migration/content-transformer/assets/ct-6.png)

   >[!NOTE]
   > Any operation that can change the source content (`move`/`remove`/`rename`) will by default create a backup package of the source paths under `/etc/packages/content-transformation` before the transformation. Although each operation dialog has an option to disable/enable backup package creation, it is strictly recommended to always have the enable package creation selected.

1. An example of a backup package created for the move operation of the paths is shown below, click install to bring back the source paths. The installation only brings the source paths back to their original location and not delete the paths where they were moved during transformation. To delete the paths in the moved location, click **Add Paths** button to add the location (for example, `/etc/packages/content-transformation/paths`), select the location and click **Remove**. 

   >[!CAUTION]
   > Do not delete `/etc/packages/content-transformation` as this is the location where the backup packages reside. Only when you are sure that you do not need these packages anymore, you can delete this location to reduce the repository size.

   ![image](/help/journey-migration/content-transformer/assets/ct-7.png)
   ![image](/help/journey-migration/content-transformer/assets/ct-8.png)
