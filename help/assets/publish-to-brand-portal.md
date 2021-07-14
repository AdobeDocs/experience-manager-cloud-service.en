---
title: Publish assets, folders, and collections to Brand Portal
description: Publish assets, folders, and collections to Brand Portal.
contentOwner: Vishabh Gupta
feature: Brand Portal,Asset Distribution,Configuration
role: User
exl-id: 1cc438bc-8cad-4421-af03-c1f6d750e0a8
---
# Publish assets to Brand Portal {#publish-assets-to-brand-portal}

As an Adobe Experience Manager (AEM) Assets administrator, you can publish assets, folders, and collections to the AEM Assets Brand Portal instance. Also, you can schedule the publish workflow of an asset or folder to a later date or time. Once published, the Brand Portal users can access and further distribute the assets, folders, and collections to other users. 

However, you must first configure AEM Assets with Brand Portal. For details, see [Configure AEM Assets with Brand Portal](configure-aem-assets-with-brand-portal.md). 

If you make subsequent modifications to the original asset, folder, or collection in AEM Assets, the changes are not reflected in Brand Portal until you republish from AEM Assets. This feature ensures that work-in-progress changes are not available in Brand Portal. Only approved changes that are published by an administrator are available in Brand Portal.

* [Publish assets to Brand Portal](#publish-assets-to-bp)
* [Publish folders to Brand Portal](#publish-folders-to-brand-portal)
* [Publish collections to Brand Portal](#publish-collections-to-brand-portal)

>[!NOTE]
>
>Adobe recommends staggered publishing, preferably during non-peak hours, so that the AEM author does not occupy excess resources.

## Publish assets to Brand Portal {#publish-assets-to-bp}

Following are the steps to publish assets from AEM Assets to Brand Portal:

1. From the Assets console, open the parent folder and select all the assets that you want to publish and click **[!UICONTROL Quick Publish]** option from the toolbar.

   ![publish2bp-2](assets/publish2bp.png)

1. Following are the two ways publish assets:
    * [Publish now](#publish-to-bp-now) (Publish assets immediately)
    * [Publish later](#publish-to-bp-later) (Schedule publishing assets)

### Publish assets now {#publish-to-bp-now}

To publish the selected assets to Brand Portal, do either of the following:

* From the toolbar, select **[!UICONTROL Quick Publish]**. Then from the menu, click **[!UICONTROL Publish to Brand Portal]**.

* From the toolbar, select **[!UICONTROL Manage Publication]**.

  1. From **[!UICONTROL Action]**, select **[!UICONTROL Publish to Brand Portal]**. 
  
     From **[!UICONTROL Scheduling]**, select **[!UICONTROL Now]**. 
     
     Click **[!UICONTROL Next]**.

  2. Confirm your selection in **[!UICONTROL Scope]** and click **[!UICONTROL Publish to Brand Portal]**.

A message appears stating that the assets have been queued up for publishing to Brand Portal. Login to the Brand Portal interface to see the published assets.

### Publish assets later {#publish-to-bp-later}

To schedule publishing the assets to Brand Portal to a later date or time:

1. Select the assets that you want to schedule for publishing and click **[!UICONTROL Manage Publication]** from the tool bar at the top.
  
1. On **[!UICONTROL Manage Publication]** page, select **[!UICONTROL Publish to Brand Portal]** from **[!UICONTROL Action]**.

   Select **[!UICONTROL Later]** from **[!UICONTROL Scheduling]**.

    ![publishlaterbp-1](assets/publishlaterbp-1.png)

1. Select an **[!UICONTROL Activation date]** and specify time. Click **[!UICONTROL Next]**.

1. Select an **Activation date** and specify time. Click **Next**.

1. Specify a **[!UICONTROL Workflow title]** in **[!UICONTROL Workflows]**. Click **[!UICONTROL Publish Later]**.

    ![publishworkflow](assets/publishworkflow.png)

Login to the Brand Portal interface to see the published assets (depending on your scheduled date or time).

   ![bp_landingpage](assets/bp_landingpage.png)


## Publish folders to Brand Portal {#publish-folders-to-brand-portal}

You can publish or unpublish asset folders immediately, or schedule to a later date or time.

### Publish folders to Brand Portal {#publish-folders-to-bp}

1. From the Assets console, select the folders that you want to publish and click **[!UICONTROL Quick Publish]** option from the toolbar.

   ![publish2bp](assets/publish2bp.png)

1. **Publish folders now**

   To publish the selected folders to Brand Portal, do either of the following:

    * From the toolbar, select **[!UICONTROL Quick Publish]**. 
    
      From the menu, select **[!UICONTROL Publish to Brand Portal]**.

    * From the toolbar, select **[!UICONTROL Manage Publication]**.

      1. From **[!UICONTROL Action]**, select **[!UICONTROL Publish to Brand Portal]**.
      
         From **[!UICONTROL Scheduling]**, select **[!UICONTROL Now]**.
         
         Click **Next.**

      1. Confirm your selection in **[!UICONTROL Scope]** and click **[!UICONTROL Publish to Brand Portal]**.

   A message appears stating that the folder has been queued up for publishing to Brand Portal. Login to your Brand Portal interface to see the published folder.

1. **Publish folders later**

   To schedule the publishing the asset folders to a later date or time:

    1. Select the folders that you want to schedule for publishing, select **[!UICONTROL Manage Publication]** from the tool bar at the top.
    1. From **[!UICONTROL Action]**, select **[!UICONTROL Publish to Brand Portal]**.
    
       From **[!UICONTROL Scheduling]**, select **[!UICONTROL Later]**.

   1. Select an **[!UICONTROL Activation date]** and specify time. Click **[!UICONTROL Next]**.

       ![publishlaterbp](assets/publishlaterbp.png)
    
    1. Confirm your selection in **[!UICONTROL Scope]**. Click **[!UICONTROL Next]**.

    1. Specify a Workflow title under **[!UICONTROL Workflows]**. Click **[!UICONTROL Publish Later]**.

       ![manageschedulepub](assets/manageschedulepub.png)

### Unpublish folders from Brand Portal {#unpublish-folders-from-brand-portal}

You can remove any asset folder published to Brand Portal by unpublishing it from AEM Assets instance. After you unpublish the original folder, its copy is no longer available to Brand Portal users.

You can unpublish asset folders from Brand Portal immediately, or schedule to a later date and time. 

To unpublish asset folders from Brand Portal:

1. From the Assets console, select the asset folders that you want to upublish and click **[!UICONTROL Manage Publication]** option from the toolbar. 

   ![publish2bp-1](assets/publish2bp.png)

1. **Unpublish asset folders now**

   To immediately unpublish the selected asset folder from Brand Portal:

    1. From the toolbar, select **[!UICONTROL Manage Publication]**.

    1. From **[!UICONTROL Action]** select **[!UICONTROL Unpublish from Brand Portal]**. 
    
       From **[!UICONTROL Scheduling]**, select **[!UICONTROL Now]**.
       
       Click **[!UICONTROL Next]**.

    1. Confirm your selection in **[!UICONTROL Scope]** and click **[!UICONTROL Unpublish from Brand Portal]**.

       ![confirm-unpublish](assets/confirm-unpublish.png)

1. **Unpublish asset folders later**

   To schedule unpublishing of an asset folder to a later date and time:

    1. From the toolbar, select **[!UICONTROL Manage Publication]**.
    
    1. From **[!UICONTROL Action]**, select **[!UICONTROL Unpublish from Brand Portal]**.
    
       From **[!UICONTROL Scheduling]**, select **[!UICONTROL Later]**.

    1. Select an **[!UICONTROL Activation date]** and specify the time. Click **[!UICONTROL Next]**.

    1. Confirm your selection in **[!UICONTROL Scope]** and click **[!UICONTROL Next]**.

    1. Specify a **[!UICONTROL Workflow title]** in **[!UICONTROL Workflows]**. Click **[!UICONTROL Unpublish Later]**.

       ![unpublishworkflows](assets/unpublishworkflows.png)

## Publish collections to Brand Portal {#publish-collections-to-brand-portal}

You can publish or unpublish collections from your AEM Assets cloud instance.

>[!NOTE]
>
>Content fragments cannot be published to the Brand Portal. Therefore, if you select content fragment(s) in AEM Assets, then **[!UICONTROL Publish to Brand Portal]** action is not available.
>
>If collections containing content fragments are published from AEM Assets to Brand Portal, then all the contents of the folder except content fragments is replicated to the Brand Portal interface.

### Publish collections {#publish-collections}

Following are the steps to publish collections from AEM Assets to Brand Portal:

1. In the AEM Assets UI, click AEM logo. 

1. From **Navigation** page, go to **[!UICONTROL Assets]** > **[!UICONTROL Collections]**.

1. From the **Collections** console, select the collections that you want to publish to Brand Portal.

   ![select_collection](assets/select_collection.png)

1. From the toolbar, click **[!UICONTROL Publish to Brand Portal]**.

1. In the confirmation dialog, click **[!UICONTROL Publish]**.

1. Close the confirmation message.

   Login to Brand Portal as an administrator. The published collection is available in the Collections console.

   ![published collection](assets/published_collection.png)

### Unpublish collections {#unpublish-collections}

You can remove any collection published to Brand Portal by unpublishing it from your AEM Assets instance. After you unpublish the original collection, its copy is no longer available to the Brand Portal users.

Following are the steps to unpublish a collection:

1. From the **Collections** console of your AEM Assets instance, and select the collection that    you want to unpublish.

   ![select_collection](assets/select_collection-1.png)

1. From the toolbar, click **[!UICONTROL Remove from Brand Portal]** icon.
1. In the dialog, click **[!UICONTROL Unpublish]**.
1. Close the confirmation message. The collection is removed from the Brand Portal interface.

In addition to the above, you can also publish metadata schemas, image presets, search facets, and tags from AEM Assets to Brand Portal. 

* [Publish presets, schemas, and facets to Brand Portal](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/publish/publish-schema-search-facets-presets.html)
* [Publish tags to Brand Portal](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/publish/brand-portal-publish-tags.html)


See, [Brand Portal documentation](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/home.html) for more information.


<!--
   Comment Type: draft

   <li> </li>
   -->

   <!--
   Comment Type: draft

   <li>Step text</li>
   -->
