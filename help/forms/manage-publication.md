---
title: How to publish or unpublish forms on preview or publish instances?
description: Learn publishing or unpublishing forms from the AEM author environment to preview or publish instances. Whether you are testing your forms on a staging environment or deploying them live for end-users, AEM provides streamlined tools to manage this process efficiently.
Keywords: Manage publication, Forms Manage publication, AF Manage publication, Adaptive Forms Manage publication, Cloud Manage publication
feature: Adaptive Forms
feature-set: Experience Manager Assets,Experience Manager Sites,Experience Manager, Experience Manager Forms, Experience Manager Cloud Manager
role: User, Developer
level: Intermediate
exl-id: 6ade40f1-bad5-4f5e-aa0e-84b7c6a82e02
---
# ​Manage Publication in Experience Manager Forms

As an Adobe Experience Manager (AEM) Forms administrator, you can publish forms from your author instance to Experience Manager Forms. You also have the option to schedule the publication of a form or folder for a later date or time. Once published, users can access and fill out the forms.

In Experience Manager Forms, you can publish a form using one of the following methods:
* [Publish option](#publish-forms-using-the-publish-option) 
* [Manage Publication option](#publish-forms-using-the-manage-publication-option)

## Things to keep in mind

* Only members of the `forms-users` group can use the **Manage Publication** option to publish the forms.
* Changes made to forms or folders in Experience Manager Forms do not appear in the **Publish** instance until republished. This ensures that work-in-progress updates remain unavailable in the **Publish** instance. Only changes explicitly published by an administrator are reflected in the **Publish** instance.

## Publish forms using the Publish option 

The **Publish** option lets you immediately publish a form. To publish an Experience Manager Form using the **Publish** button on the toolbar. To publish forms using the Publish option are:

1. From the Experience Manager Forms console, navigate to the parent folder and select a form that you want to publish. 
1. Click **Publish** option from the toolbar, take a look at all the reference assets that would be published with form.
1. Click **[!UICONTROL Publish]**. 

    ![Publish and Unpublish form](/help/edge/docs/forms/assets/publish-form-option.png)

    Once the form and its related assets are successfully published, a **Success** dialog appears. 
1. Click **Close**.

    ![Success dialog](/help/forms/assets/publish-success.png)

### Unpublish the form

After successfully publishing the form using the **Publish** option and its related assets, you can even unpublish them using the **[!UICONTROL Unpublish]** button available on the toolbar. To unpublish form:

1. To unpublish the form and its related assets, select the form and click **[!UICONTROL Unpublish]** from the toolbar

    When you click the **[!UICONTROL Unpublish]** button, the **Unpublish Asset** dialog appears. 
1. Click **[!UICONTROL Unpublish]** to start the unpublishing process

    ![Unplish dialog](/help/forms/assets/unpublish-asset.png)

    Once the form and its related assets are successfully unpublished, a **Success** dialog appears. 
1. Click **Close**.

    ![unpublish successful](/help/forms/assets/unpublishing-start.png)

## Publish forms using the Manage Publication option

Manage publication lets you publish or unpublish content to and from the selected destination, add content to the publishing list from across the `forms&documents` folder, select references to publish, and schedule publishing to a later date or time.  To publish forms using the **Manage Publication** option are:

1. From the Experience Manager Forms console, navigate to the parent folder and select a form that you want to publish. 
1. Click **[!UICONTROL Manage Publication]** option from the toolbar.  

    ![Manage Publication option](/help/forms/assets/manage-publication-option.png) 

    The **Manage Publication** UI appears:

    ![Manage publication](/help/forms/assets/manage-publication.png)

    The following options are available in the **Manage Publication** UI:

      * **Actions** 

        * **Publish**: Publish forms to the selected destination 
        * **Unpublish**: Unpublish forms from the destination 

      * **Destination** 

         * **Publish**: Publish forms to Experience Manager Forms (AEM) Publish instance.  
         * **Preview**: Publish forms to Experience Manager Forms (AEM) Preview instance. 

      * **Scheduling** 

         * **Now**: Publish forms immediately 
         * **Later**: Publish forms based on the **Activation date** or time 

1. Click **Next** to continue. 
1. (Optional) In the **Scope** tab, use the [Add Content](#add-content) option to add more content for publishing. For example, you can add more Forms or Document of Record files. 
    ![scope tab](/help/forms/assets/scope-tab.png)
1. Click **[!UICONTROL Publish]** to publish the forms and related assets and successful message appears.
    ![publish successful message](/help/forms/assets/publish-successful.png)

### Add content 

Publishing to Experience Manager Forms lets you further add more content (forms) to the publishing list. 
To add more forms for publishing:

1. Click **Add Content** button to add more content. 

    ![Add content](/help/forms/assets/add-content.png)

2. Select the form from the **Select Path** screen.

    ![Add content](/help/forms/assets/add-assets.png)

    >[!NOTE]
    >
    > You can add more forms or folders to the list from the `formsanddocuments` folder. But you cannot add forms from multiple folders at a time.

3. To configure the references to publish or not publish for a form, select the form and click **[!UICONTROL Published References]**.  

    ![published references](/help/forms/assets/published-references.png)

4. In the **Published References** dialog box, uncheck the assets you plan to not-publish and click **[!UICONTROL Done]**. 
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

Along with allowing you to publish or unpublish forms at a later date and time, the publish or unpublish later option also allows to configure a workflow. The forms are published or unpublished after completion of the workflow. 

To schedule a form for publishing or unpublishing: 

1. From the Experience Manager Forms console, navigate to the parent folder and select the form that you want to schedule for publishing. 
1. Click **[!UICONTROL Manage Publication]** option from the toolbar. 

    ![Manage publication](/help/forms/assets/manage-publication.png)

1. Click **Publish** or **Unpublish** from **[!UICONTROL Action]**.
1. Select the **[!UICONTROL Destination]** where you want to publish or unpublish the content.  
    * **Preview**: Use the **Preview** option to publish or unpublish to an Experience Manager Forms preview environment. The Experience Manager Forms preview environments are used to test under development forms.  
    * **Publish**: Use the Experience Manager Forms **Publish** option to send the form to Experience Manager Forms publish environment after the form is ready to use in a production environment.  
 
1. Select **[!UICONTROL Later]** from **Scheduling**. 

    ![Manage Publication later](/help/forms/assets/manage-publication-later.png)

1. Select an **[!UICONTROL Activation date]** and specify the date and time. 
1. Click **[!UICONTROL Next]**. 
1. (Optional) In the **Scope** tab, add content using **[!UICONTROL Add Content]** . 
    ![Manage Publication add content later](/help/forms/assets/publish-later-add-content.png)
1. Click **[!UICONTROL Next]**. 
1. In the **Workflows** tab, specify a **[!UICONTROL Workflow title]**. 
1.  Click **[!UICONTROL Publish Later]**. 

     ![Manage Publication workflow](/help/forms/assets/manage-publication-workflows.png)

## Determining publication status 

There are multiple ways to determine the publishing status: 

* Log in to the destination instance to verify the published forms and other assets (depending upon the scheduled date or time). 

* Use the timeline view to determine the publication status. 

* Use the page information menu in Adaptive Forms editor.
