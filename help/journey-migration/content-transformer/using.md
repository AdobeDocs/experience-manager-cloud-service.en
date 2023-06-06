---
title: Using Content Transformer
description: Using Content Transformer
---
# Using Content Transformer {#using-ct}

## Important Considerations for Using Content Transformer {#imp-considerations-ct}

Follow the section below to understand the important considerations for using the Content Transformer (CT):

* To use the Content Transformer, you must first run the Best Practices Analyzer on your AEM environment. 
* Although you can run the Content Transformer on your Production environment, it is recommended that you run the Content Transformer on a clone of your Production environment. More importantly, you need to ensure that the BPA and the CT are run on the same environment.
* You need to be an admin on the environment where you want to run the Content Transformer.
* Any operation that can change the source content ( move/remove/rename ) will by default create a backup package of the source paths under `/etc/packages/content-transformation` before the transformation. Although each operation dialog has an option to disable/enable backup package creation, it is strictly recommended to always have the enable packag creation selected.
* Each page in the CT is configured to list a maximum of 50 findings hence at a time a maximum of 50 findings can be transformed. This is done to provide a timeliness response on the UI. 

## Availability {#availability-ct}

The Content Transformer is bundled with the [Content Transfer Tool](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/getting-started-content-transfer-tool.md) that can be downloaded as a zip file from the Software Distribution Portal. You can install the package via Package Manager on your source Adobe Experience Manager (AEM) instance.

>[!NOTE]
>The Content Transformer is available with CTT version vXX.xx or higher.
