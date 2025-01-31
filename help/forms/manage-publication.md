---
title: How to publish or unpublish forms on preview or publish instances?
description: Learn publishing or unpublishing forms from the AEM author environment to preview or publish instances. Whether you are testing your forms on a staging environment or deploying them live for end-users, AEM provides streamlined tools to manage this process efficiently.
Keywords: Manage publication, Forms Manage publication, AF Manage publication, Adaptive Forms Manage publication, Cloud Manage publication
feature: Adaptive Forms
feature-set: Experience Manager Assets,Experience Manager Sites,Experience Manager, Experience Manager Forms, Experience Manager Cloud Manager
role: User, Developer
level: Intermediate
---

# ​Manage Publication in Experience Manager Forms

As an Adobe Experience Manager Forms administrator, you can publish forms from your author instance to Experience Manager Forms. You can schedule to publish a form or folder at a later date or time. Once published, the users can access and fill the forms. 

In the Experience Manager Forms interface, you can publish a form using the:
* [Publish option](#publish-forms-using-the-publish-option) 
* [Manage Publication option](#publish-forms-using-the-manage-publication-option)

If you make subsequent modifications to the original forms or folder in Experience Manager Forms, the changes are not reflected in the **Publish** instance until you republish from Experience Manager Forms. It ensures that work-in-progress changes are not available in the **Publish** instance. Only changes that are published by an administrator are available in the **Publish** instance.

## Publish forms using the Publish option 

The **Publish** option lets you immediately publish a form. To publish an Experience Manager Form using the **Publish** button on the toolbar. To publish forms using the Publish option are:

1. From the Experience Manager Forms console, navigate to the parent folder and select a form that you want to publish. 
1. Click **Publish** option from the toolbar, take a look at all the reference assets that would be published with form.
1. Click **[!UICONTROL Publish]**. 

    ![Publish and Unpublish form](/help/edge/docs/forms/assets/publish-form-option.png)

    Once the form and its related assets are successfully published, a **Success** dialog appears. Click **Close** to close the dialog box.

    ![Success dialog](/help/forms/assets/publish-success.png)

### Unpublish the form

After successfully publishing the form using the **Publish** option and its related assets, you can even unpublish them using the **[!UICONTROL Unpublish]** button on the toolbar. To unpublish form:

1. To unpublish the form and its related assets, select the form and click **[!UICONTROL Unpublish]** from the toolbar

    When you click the **[!UICONTROL Unpublish]** button, the **Unpublish Asset** dialog appears. 
1. Click **[!UICONTROL Unpublish]** to start the unpublishing process

    ![Unplish dialog](/help/forms/assets/unpublish-asset.png)

    Once the form and its related assets are successfully unpublished, a **Success** dialog appears. Click **Close** to close the dialog box.

    ![unpublish successful](/help/forms/assets/unpublishing-start.png)

## Publish forms using the Manage Publication option

Manage publication lets you publish or unpublish content to and from the selected destination, add content to the publishing list from across the forms & documents folder, select references to publish, and schedule publishing to a later date or time.  To publish forms using the Manage Publication option are:

1. From the Experience Manager Forms console, navigate to the parent folder and select a form that you want to publish. 
1. Click **[!UICONTROL Manage Publication]** option from the toolbar.  

    ![Manage Publication option](/help/forms/assets/manage-publication-option.png) 

    The **Manage Publication** interface appears:

    ![Manage publication](/help/forms/assets/manage-publication.png)

    The following options are available in the **Manage Publication** interface:

      * **Actions** 

        * **Publish**: Publish forms to the selected destination 
        * **Unpublish**: Unpublish forms from the destination 

      * **Destination** 

         * **Publish**: Publish forms to Experience Manager Forms (AEM) Publish instance.  
         * **Preview**: Publish forms to Experience Manager Forms (AEM) preview instance. 

      * **Scheduling** 

         * **Now**: Publish forms immediately 
         * **Later**: Publish forms based on the **Activation date** or time 

1. Click **Next** to continue. 
1. In the **Scope** tab, use the [Add Content](#add-content) option to add more content for publishing. For example, you can add more Forms or Document of Record files. 

    ![scope tab](/help/forms/assets/scope-tab.png)

1. Click **[UICONTROL Publish]** to publish the forms and related assets and successful message appears.

    ![publish successful message](/help/forms/assets/publish-successful.png)


### Add content 

Publishing to Experience Manager Forms lets you further add more content (forms and folders) to the publishing list. You can add more forms or folders to the list from the `formsanddocuments` folder. But you cannot add forms from multiple folders at a time. To add more forms for publishing:

1. Click **Add Content** button to add more content. 

    ![Add content](/help/forms/assets/add-content.png)

1. Select the form from the **Select Path** screen. You can add multiple forms from a folder or add multiple folders at a time. But you cannot add forms from multiple folders at a time. 

    ![Add content](/help/forms/assets/add-assets.png)

1. To configure the references to publish or not publish for a form, select the form and click **[!UICONTROL Published References]**.  

    ![published references](/help/forms/assets/published-references.png)

1. In the **Published References** dialog box, uncheck the assets you plan to not-publish and click **[!UICONTROL Done]**. 
    ![published references dialog](/help/forms/assets/published-references-dialog.png)

<!--
### Include Folder Settings
By default, publishing a folder to Experience Manager Forms publishes all the assets, subfolders, and their references. To filter the folder for publishing:

1. Click **[Include Folder Settings]** to filter the folder.

    ![Include folder](/help/forms/assets/include-folder.png)

    The **[UICONTROL Include Folder Settings]** dialog appears. 
    
    ![Include folder dialog](/help/forms/assets/include-folder-dialog.png)
    
    The **[UICONTROL Include Folder Settings]** includes following options:

    * **[!UICONTROL Include folder contents]** checkbox. 
        * If selected, all forms and assets in the chosen folder, its subfolders (including all forms and assets within them), and references are published.
        * If not selected, only the forms and assets in the selected folder are published, while subfolder forms and assets are not.

    * **[!UICONTROL Include only immediate folder contents]** checkbox
        Selecting the **[!UICONTROL Include folder contents]** checkbox enables the **[!UICONTROL Include only immediate folder contents]** checkbox for selection.

        * If you select both options, all the forms and assets of the selected folder, subfolders (empty), and references are published. The forms and assets of the subfolders are not published.
        * -->


### Publish or unpublish a form later 

Along with allowing you to publish or unpublish forms at a later date and time, the publish or unpublish later option also allows to configure a workflow. The forms are published or unpublished after completion of the workflow. To schedule a form for publishing or unpublishing: 

1. From the Experience Manager Forms console, navigate to the parent folder and select the form that you want to schedule for publishing. 
1. Click **[!UICONTROL Manage Publication]** option from the toolbar. 

    ![Manage publication](/help/forms/assets/manage-publication.png)

1. Click **Publish** or **Unpublish** from **[!UICONTROL Action]**, and then select the **[!UICONTROL Destination]** where you want to publish or unpublish the content.  
    * **Preview**: Use the **Preview** option to publish or unpublish to an Experience Manager Forms preview environment. The Experience Manager Forms preview environments are used to test under development forms.  
    * **Publish**: Use the Experience Manager Forms Publish option to send the form to Experience Manager Forms publish environment after the form is ready to use in a production environment.  
 
1. Select **[!UICONTROL Later]** from Scheduling. 

    ![Manage Publication later](/help/forms/assets/manage-publication-later.png)

1. Select an **[!UICONTROL Activation date]** and specify the date and time. 
1. Click **[!UICONTROL Next]**. 
1. In the **Scope** tab, **[!UICONTROL Add Content]** (if necessary). 
    ![Manage Publication add content later](/help/forms/assets/publish-later-add-content.png)
1. Click **[!UICONTROL Next]**. 
1. (Optional) In the **Workflows** tab, specify a **[!UICONTROL Workflow title]**. 
1. Click **[!UICONTROL Publish Later]**. 

     ![Manage Publication workflow](/help/forms/assets/manage-publication-workflows.png)

## Determining publication status 

There are multiple ways to determine the publishing status: 

* Log in to the destination instance to verify the published forms and other assets (depending upon the scheduled date or time). 

* Use the timeline view to determine the publication status. 

* Use the page information menu in Adaptive Forms editor.  
