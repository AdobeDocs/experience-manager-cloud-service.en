---
title: Getting Started with Edge Delivery Services for AEM Forms in Universal Editor - Developer Tutorial
description: This tutorial helps get you up-and-running with a new Adobe Experience Manager Forms (AEM) project. In ten to twenty minutes, you will have created your own Edge Delivery Services Forms in Universal Editor.
feature: Edge Delivery Services
role: Admin, Architect, Developer
hide: yes
hidefromtoc: yes
exl-id: 24a23d98-1819-4d6b-b823-3f1ccb66dbd8
---
# Getting Started with Edge Delivery Services for AEM Forms using Universal Editor (WYSIWYG) 

In today's digital age, user-friendly forms are essential for all organizations. Edge Delivery Services Forms are created using the Universal Editor, which offers WYSIWYG (what-you-see-is-what-you-get) capabilities. It provides a modern, intuitive interface for efficient form authoring.

AEM Forms provide a block, known as the Adaptive Forms Block, to help you easily create Edge Delivery Services Forms to capture and store data. You can [create a new AEM Project pre-configured with the Adaptive Forms Block](#create-a-new-aem-project-pre-configured-with-adaptive-forms-block) or [add the Adaptive Forms Block to an existing AEM Project](#add-adaptive-forms-block-to-your-existing-aem-project).

This tutorial guides you through creating, previewing, and publishing your own form with a new or existing Adobe Experience Manager Site project using Universal Editor's WYSIWYG authoring.


## Prerequisites

* You have a GitHub account, and understand Git basics.
* You have a Google or Microsoft SharePoint account.
* You understand the basics of HTML, CSS, and JavaScript.
* You have Node/npm installed for local development.

## Create a new AEM project pre-configured with Adaptive Forms Block

The AEM Forms Boilerplate template gets you started quickly with an AEM project pre-configured with the Adaptive Forms Block. It is the quickest and easiest way to follow AEM best practices and jump right into building your forms.

### Get started with the AEM Forms boilerplate repository template

1. Create a GitHub repository for your AEM Project. To create repository:  
    1. Go to [https://github.com/adobe-rnd/aem-boilerplate-forms](https://github.com/adobe-rnd/aem-boilerplate-forms). 

        ![AEM Forms Boilerplate](/help/edge/docs/forms/assets/eds-form-boilerplate.png)
    1. Click the **Use this template** option and select the **Create a new repository** option. 

        ![Create new repository using AEM Forms Boilerplate](/help/edge/docs/forms/assets/use-eds-form-template.png)
    
        The **Create a new repository** screen opens.  

    1. On the **Create a new repository** screen, select the **owner**, and specify **Repository name** . Adobe recommends to set the repository to **Public**. So, select the **public** option, and click **Create Repository**. 

        ![Set the repository to public](/help/edge/docs/forms/assets/name-eds-repo.png)

1. Install the AEM Code Sync GitHub App on your repository. To install:
    1. Go to [https://github.com/apps/aem-code-sync/installations/new](https://github.com/apps/aem-code-sync/installations/new).
    1. On the **Install AEM Code Sync** screen, select the **Only select Repositories** option and select your newly created repository. Click **Save**.

    ![Set the repository to public](/help/edge/docs/forms/assets/aem-code-sync-up.png)
    
1. Now link the GitHub repository you created using AEM Forms Boilerplate to your AEM Project authoring environment. To connect:

    1. Go to the GitHub repository that you created eariler using AEM Forms Boilerplate.
    1. Open the **fstab.yaml** file for editing.

        ![open fstab.yaml file](/help/edge/docs/forms/assets/open-fstab.png)

    1. Edit the **fstab.yaml** file to update the mount point of your project. Replace the URL with the URL of your AEM as a Cloud Service authoring instance.
        `https://<aem-author>/bin/franklin.delivery/<owner>/<repository>/main`

        ![edit fstab.yaml file](/help/edge/docs/forms/assets/edit-fstab-file.png)

    1. Commit the updated **fstab.yaml** file, once you have updated the reference and everything looks good. 

        ![commit the changes](/help/edge/docs/forms/assets/commit-fstab-changes.png)
   
        If you encounter any build issues, see [Troubleshooting GitHub build issues](#troubleshooting-github-build-issues).

### Create a new AEM Project

Now that you have a GitHub project, you can proceed to create and publish a new AEM Project at the AEM as a Cloud Service authoring instance.
1. To create a new AEM Project:

   1. Login to AEM as a Cloud Service authoring instance and select **Sites**.

        ![select sites](/help/edge/assets/select-sites.png)

   1. Click **Create** > **Site from template**.

        ![create-sites](/help/edge/docs/forms/assets/create-sites.png)

   1. Select the Edge Delivery Services Site template and click **Next**.

        ![select-site-template](/help/edge/docs/forms/assets/select-site-template.png)
    
        >[!NOTE]
        >
        > * If the Edge Delivery Services Site template is not available on your authoring instance, click the Import button to upload the template. 
        > * You can download the Edge Delivery Services Site templates from [GitHub](https://github.com/adobe-rnd/aem-boilerplate-xwalk/releases). 

   1. Enter the following details to create a new AEM Project:
       * **Site title** - Add a descriptive title for the site.
       * **Site title** - Use the `site-name` that you defined in the previous step.
       * **GitHub URL** - Use the URL of the GitHub project you created in the previous step.

        ![create AEM Site](/help/edge/docs/forms/assets/create-aem-site.png)

   1. The **Create Site** dialog appears, click **Okay**.

         ![click ok](/help/edge/docs/forms/assets/click-ok-aem-site.png)

       In just a few minutes, your new AEM Project is created.

   1. Navigate to your newly-created AEM project in the Sites console and click **Edit**. 
   In this case, the `index.html` page is used for illustration.

        ![edit AEM Site](/help/edge/docs/forms/assets/edit-site.png)

        The AEM Project opens in the Universal Editor in a new tab, enabling WYSIWYG authoring. You can now edit your AEM Project. 

        ![Site opens in Universal Editor](/help/edge/docs/forms/assets/site-in-universal-editor.png)

1. Publish your created AEM Project    

    Once you finish editing your AEM Project, publish it. To publish:

   1. On the Sites console, select all of the AEM Project pages and click **Quick Publish**.

        ![publish AEM Sites Project](/help/edge/docs/forms/assets/publish-sites.png)

   1. The **Quick Publish** confirmation dialog appears, click **Publish** to start the publishing process.

        ![Quick Publish confirmation dialog](/help/edge/docs/forms/assets/quick-publish.png)

        Alternatively, you can publish your AEM Project pages directly from the Universal Editor user interface.

        ![Quick Publish confirmation dialog](/help/edge/docs/forms/assets/qui.png)

    Congratulations! You have a new website running on `https://<branch>--<repo>--<owner>.aem.page/content/<site-name>/`. 

      * `<branch>` refers to the branch of your GitHub repository. 
      * `<repository>` denotes your GitHub repository. 
      * `<owner>` refers to username of your GitHub account that hosts your GitHub repository.
      * `<site-name>` refers to the name of your created site name.

    For example, if the branch name is `main`, repository is `edsforms`, owner is `wkndforms` and the `site-name` is `eds-forms`, the website would be up and running at `https://main--edsforms--wkndforms.aem.page/content/eds-forms/`

    >[!NOTE]
    >
    > * To view the `index.html` page of the AEM Project, use the URL: `https://<branch>--<repo>--<owner>.aem.page/content/<site-name>/`
    > * To view pages other than the `index page` of the AEM Project, use the URL: `https://<branch>--<repo>--<owner>.aem.page/content/<site-name>/<site-page-name>`

Now, you can start [creating and adding forms to your AEM Project](#add-edge-delivery-services-forms-to-aem-project).

## Add Adaptive Forms Block to your existing AEM Project

If you have an existing AEM Project, you can integrate the Adaptive Forms Block into your current project to get started on form creation. 

>[!NOTE]
>
>
> This step applies to projects built with the [AEM Boilerplate](https://github.com/adobe-rnd/aem-boilerplate-xwalk). If you created your AEM project using the [AEM Forms Boilerplate](https://github.com/adobe-rnd/aem-boilerplate-forms), you can skip this step.

To Integrate:

1. Clone the Adaptive Forms Block GitHub repository: [https://github.com/adobe-rnd/aem-boilerplate-forms](https://github.com/adobe-rnd/aem-boilerplate-forms) to your computer. 
1. Inside the downloaded folder, find the `blocks/form` folder and copy this folder.
1. Clone your AEM Project GitHub repository to your computer.  
1. Now, navigate to the `blocks` folder in your local AEM Project repository and paste the copied form folder there.
1. Commit and push these changes to your AEM Project repository on GitHub.

That's it! The Adaptive Forms Block is now part of your AEM Project. You can [start creating and adding forms to your AEM Project](#add-edge-delivery-services-forms-to-aem-site-project).

## Author AEM Forms using WYSIWYG

You can open your AEM Project in the Universal Editor for WYSIWYG authoring, where you can edit the project and add the Adaptive Form section to include Edge Delivery Services forms on AEM Project pages.

1. Add the Adaptive Form section to your AEM Project page. To add:
   1. Navigate to your AEM Project in the Sites console and click **Edit**. The AEM Project page opens in Universal Editor for editing. 
   In this case, the `index.html` page is used for illustration.
   1. Open the Content tree and navigate to the location where you want to add the Adaptive Form section.
   1. Click the **[!UICONTROL Add]** icon and select the **[!UICONTROL Adaptive Form]** component from the component list.

    ![content tree](/help/edge/docs/forms/assets/add-adaptive-form-block.png)

    The Adaptive Form section is added at the specified location. You can now begin adding form components to the AEM Project page.

1. Add form components to the added Adaptive Form section. To add form components: 
    1. Navigate to the added Adaptive Form section in the Content tree.
   
        ![adaptive form block added](/help/edge/docs/forms/assets/adative-form-block.png)


    1. Click the **[!UICONTROL Add]** icon and add the desired components from the **Adaptive Form Components** list. 
   
        ![add component](/help/edge/docs/forms/assets/add-component.png)

        You can also drag and drop the required Adaptive Forms components, as the Universal Editor offers an intuitive drag-and-drop feature.

    1. Select the added Adaptive Form component to update its properties using **[!UICONTROL Properties]**.
 
        ![open properties](/help/edge/docs/forms/assets/component-properties.png)

        The screenshot below displays the form authored in the AEM Project using WYSIWYG authoring:

        ![added form](/help/edge/docs/forms/assets/added-form-aem-sites.png)

    >[!NOTE]
    >
    > It is important to publish your AEM Project page again after making changes; otherwise, the updates are not visible in the browser.

1. Re-publish the AEM Project page. 

   1. Click **Publish** to publish the AEM Project page again after adding the form.

        ![publish form](/help/edge/docs/forms/assets/publish-form.png)

   1. The **Publish** confirmation dialog appears on screen, click **Publish** to start publishing.

        ![publish form1](/help/edge/docs/forms/assets/publish-form1.png)

        Once you click the **Publish** button, the `Publish started successfully` message appears.

        ![publish form2](/help/edge/docs/forms/assets/publish-form2.png)

    You can now view the AEM Project page with the added Edge Delivery Services Form at the following URL:
    `https://<branch>--<repo>--<owner>.aem.page/content/<site-name>/`.

    For example, if the branch name is `main`, the repository is `edsforms`, the owner is `wkndforms`, and the site-name is `eds-forms`, the URL would be:
    `https://main--edsforms--wkndforms.aem.page/content/eds-forms/`

    ![index page](/help/edge/docs/forms/assets/publish-index-page.png)

You can style the Edge Delivery Services Forms by editing the `.css` and `.js` files in the Adaptive Forms Block and [setting up a local AEM development environment](#set-up-local-aem-development-environment) to view the changes instantly in your browser.

## Set up local AEM development environment

You can set up a local AEM development environment for developing custom styles and components locally. To be up and running with a local AEM development environment:

1. **Install the AEM CLI**: The AEM CLI simplifies development tasks. Let's install it globally using npm:

    ```Bash
        npm install -g @adobe/aem-cli
    ```

1. **Clone your GitHub project**: Clone your AEM Project repository from GitHub using the following command, replacing <owner> with the repository owner and <repo> with the repository name:

    ```

    git clone https://github.com/<owner>/<repo>

    ```

1. **Start Your Local Environment**: Navigate to your project directory and start your local AEM instance with a single command:

    ```  
    cd <repo>
    aem up
    ```

You can make local changes in the Adaptive Forms Block `blocks/form` folder for styling and coding for your forms! Edit the `.css` or `.js` files within this directory, and you can see that the changes reflected instantly in your browser.

Once you have completed your changes, use Git commands to commit and push them. This updates your preview and production environments, accessible at the following URLs (replace placeholders with your project details):

Preview: `https://<branch>--<repo>--<owner>.aem.page/content/<site-name>`

Production: `https://<branch>--<repo>--<owner>.aem.live/content/<site-name>`


## Troubleshooting GitHub build issues 

Ensure a smooth GitHub build process by addressing potential issues:

* **Handle Linting Errors:**
    Should you come across any linting errors, you can bypass them. Open the [EDS Project]/package.json file and modify the "lint" script from `"lint": "npm run lint:js && npm run lint:css"` to `"lint": "echo 'skipping linting for now'"`. Save the file and commit the changes to your GitHub project.

<!-- * **Resolve Module Path Error:**
    If you encounter the error "Unable to resolve path to module "'../../scripts/lib-franklin.js'", navigate to the [EDS Project]/blocks/forms/form.js file. Update the import statement by replacing the lib-franklin.js file with the aem.js file. -->

