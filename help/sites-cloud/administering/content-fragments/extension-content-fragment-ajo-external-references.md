---
title: Using the Content Fragments AJO External References Extension
description: Learn about the Content Fragment AJO External References Extension
feature: Content Fragments
role: User, Developer, Architect
solution: Experience Manager Sites
---

# The Content Fragment AJO External References Extension {#content-fragment-external-references-extension}

To preview experiences from AEM on another Adobe product, you can enable the UI extension:

* **AJO External References** 

The AJO External References extension functions by fetching references to Content Fragment from all organizations and sandboxes associated with predefined tags. The extension then shows details. 

For example, for an integration with Adobe Journey Optimizer (AJO) the details are dependent on whether the reference is a Campaign, a Journey or a Template.

>[!NOTE]
>
>For details of how to enable the extension, see [Extension Manager in AEM Experience Manager.](https://developer.adobe.com/uix/docs/extension-manager/)

For example, to use the extension with AJO:

>[!NOTE]
>
>See also [AJO Integration](https://experienceleague.adobe.com/en/docs/journey-optimizer/using/integrations/aem-fragments).

1. Open the [Content Fragments Console](/help/sites-cloud/administering/content-fragments/overview.md#content-fragments-console).

1. Navigate to your Content Fragment - the fragment that was created and used across various AJO channels.

1. Open your Content Fragment in the [editor](/help/sites-cloud/administering/content-fragments/managing.md#editing-the-content-of-your-fragment).

1. The AJO External References extension is available as a tab in the right panel. Select the tab to open the extension:

   ![AJO External References extension](/help/sites-cloud/administering/content-fragments/assets/cf-ajo-fragment-external-references-extension.png)

   Once a reference type is selected the extension displays the corresponding external references as a table with the columns: 

   * **Name**: the name of the reference where the Content fragment is used
   * **Preview** select this link to start the preview
   * **Status**: the status of the reference

1. You can select the **Reference Type** from the drop-down to switch between three reference types: 

   * **Campaign**
     * Displays a list of all Campaigns with links to the current Content Fragment. 
     * You can then preview a selected Campaign.
     * Default
   * **Journey**
     * Displays the latest Journey. 
     * You can then select and preview a selected Journey.
   * **Template** 
     * Displays Templates related to the Content Fragment.
     * You can then select and preview a selected Template.