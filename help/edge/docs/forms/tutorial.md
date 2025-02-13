---
title: Getting Started with Edge Delivery Services for AEM Forms - Developer Tutorial
description: This tutorial helps get you up-and-running with a new Adobe Experience Manager Forms (AEM) project. In ten to twenty minutes, you will have created your own forms.s
feature: Edge Delivery Services
exl-id: bb7e93ee-0575-44e1-9c5e-023284c19490
role: Admin, Architect, Developer
---
# Getting Started - Developer Tutorial 

In today's digital age, creating user-friendly forms is essential for any organization. Edge Delivery Services for AEM Forms (EDS) lets you create forms using familiar tools like Google Docs and Microsoft Office. 

These forms submit data directly to a Microsoft Excel or Google Sheets file, enabling you to use vibrant ecosystem and robust APIs of Google Sheets, Microsoft Excel, and Microsoft SharePoint to easily process submitted data or to initiate an existing business workflow.

AEM Forms provide a block, known as Adaptive Forms Block, to help you easily create forms to capture and store captured data. You can [create a new AEM project pre-configured with Adaptive Forms Block](#create-a-new-aem-project-pre-configured-with-adaptive-forms-block) <!--or [add the Adaptive Forms Block to an existing AEM project](#add-adaptive-forms-block-to-your-existing-aem-project)-->. 

This AEM Forms tutorial guides you through creating, previewing, and publishing your own custom form with a new Adobe Experience Manager (AEM) Forms project.

## Prerequisites

* You have a GitHub account, and understand Git basics.
* You have a Google or Microsoft SharePoint account.
* You understand the basics of HTML, CSS, and JavaScript.
* You have Node/npm installed for local development.

**Heads up!** This tutorial uses macOS, Chrome, and Visual Studio Code. While the steps can be adapted for other setups, the screenshots and specific UI elements might differ based on your chosen operating system, browser, and code editor.


## Create a new AEM project pre-configured with Adaptive Forms Block

The AEM Forms Boilerplate template gets you started quickly with an AEM project pre-configured with the Adaptive Forms Block. It's the quickest and easiest way to follow AEM best practices and jump right into building your forms.

### Get started with the AEM Forms boilerplate repository template

1. Create a GitHub repository for your AEM Project. To create repository:  
    1. Go to [https://github.com/adobe-rnd/aem-boilerplate-forms](https://github.com/adobe-rnd/aem-boilerplate-forms). 

        ![AEM Forms Boilerplate](/help/edge/assets/aem-forms-boilerplate.png)
    1. Click the **Use this template** option and select the **Create a new repository** option. The create a new repository screen opens.  

        ![Create new repository using AEM Forms Boilerplate](/help/edge/assets/create-new-repository-using-aem-forms-boilerplate.png)
    
    1. On the create a new repository screen, select the **owner**, and specify **Repository name** . Adobe recommends that the repository is set to **Public**. So, select the **public** option, and click **Create Repository**. 

    ![Set the repository to public](/help/edge/assets/create-a-new-repo-keep-it-public.png)


1. Install the AEM Code Sync GitHub App on your repository. To install:
    1. Go to [https://github.com/apps/aem-code-sync/installations/new](https://github.com/apps/aem-code-sync/installations/new).
    1. On the Install AEM Code Sync screen, select the **Only select Repositories** option and select your newly created repository. Click Save.

    ![Set the repository to public](/help/edge/assets/install-aem-code-sync-app-for-your-repo.png)
    
    >[!NOTE]
    >
    >
    > If you are using GitHub Enterprise with IP filtering, you can add the following IP to the allowlist: 3.227.118.73

    Congratulations! You have a new website running on `https://<branch>--<repo>--<owner>.aem.page/`. 

    * `<branch>` refers to the branch of your GitHub repository. 
    * `<repository>` denotes your GitHub repository. 
    * `<owner>` refers to username of your GitHub account that hosts your GitHub repository.

    For example, if the branch name is `main`, repository is `wefinance`, and owner is `wkndforms`, the website would be up and running at `https://main--wefinance--wkndforms.aem.page`
    <!--(https://main--wefinance--wkndform.aem.page)-->

### Link your own content source

<!--Your newly created GitHub repository points to [example content stored in a Google Drive folder](https://drive.google.com/drive/folders/1bvjfi6TqpYA7DvbX6kKc-m7FgHuJ4RUQ). This read-only content provides a great starting point for your forms. Feel free to copy it into your own Google Drive and customize it to fit your needs.

![Sample Content on Google Drive](/help/edge/assets/folder-with-sample-content.png)-->

To copy the sample content to your own content folder and point your GitHub repository to your own content folder:  

1. Create a new folder specifically for your AEM content in Google Drive or Microsoft SharePoint. This document uses a folder created on Microsoft SharePoint.

1. Share the folder with the Adobe Experience Manager user (forms@adobe.com).

    ![Use Manage Access option to share folder with AEM User - SharePoint](/help/edge/assets/share-folder-with-aem-user.png)

    ![Use Manage Access option to share folder with AEM User - Google Drive](/help/edge/assets/share-google-drive-folder.png)


    Ensure that you have provided editing rights on the folder to the Adobe Experience Manager user. 

    ![Share folder with AEM User, provide editing rights-SharePoint](/help/edge/assets/share-folder-with-aem-user-provide-editing-access.png){width=50%}

    ![Share folder with AEM User, provide editing rights- Google Drive](/help/edge/assets/add-aem-user-google-folder.png){width=50%}

1. Copy the [example content](/help/edge/assets/wefinance1.zip) to your folder. To copy:

    1. Unzip the downloaded folder and copy the content. 

        ![Download Sample Content](/help/edge/assets/download-sample-content.png)

        The `nav` and `footer` files  define the basic layout of your pages and rarely change throughout a project. They also have a specific structure that's different from most other content files. By examining these files, you'll get a feel for how content is organized in AEM Projects.
        

    1. Upload these files to Microsoft SharePoint or Google Drive folder. 

        ![Sample Content on Google Drive](/help/edge/assets/upload-sample-files-to-your-content-folder.png)

        Ensure that you copy the  `enquiry` sheet from the sample content to your folder on Google Drive or Microsoft SharePoint. It contains structure for a sample form.      

1. Now that you have your content folder set up, it's time to link it to your project on GitHub that you created using AEM Forms Boilerplate earlier. To connect: 

    1. Go to the GitHub repository that you created eariler using AEM Forms Boilerplate.
    1. Open the `fstab.yaml` for editing.
    1. Replace the existing reference with the path to the folder that you shared with the AEM user (forms@adobe.com).

        ![Sample Content on Google Drive](/help/edge/assets/replace-path-in-fstab-yaml-with-your-content-folder.png)


        If you use the Microsoft SharePoint, the  folder path uses the following format:

        ```HTML

        https://<tenant>.SharePoint.com/sites/<sp-site>/Shared%20Documents/<folder-name>

        ```

        For example, 

        ```HTML

        https://adobe.SharePoint.com/sites/wkndforms/Shared%20Documents/wefinance

        ```

        For more information on managing files with Microsoft SharePoint, see [How to use Adobe SharePoint](https://www.aem.live/docs/setup-customer-sharepoint).  

      
    1. Commit the updated `fsatb.yaml` file, once you've updated the reference and everything looks good. If you encounter any build issues, see [Troubleshooting GitHub build issues](#troubleshooting-github-build-issues). 
    
        ![Commit updated fsatab.yaml file](/help/edge/assets/commit-updated-fstab-yaml.png)

        This connects your content folder to your website. After updating the reference, you might experience "404 Not Found" errors initially. This is because your content is not been previewed yet. The next section explains how to start authoring and previewing your content.



### Preview and publish your content

After completing the last step, your new content source isn't empty, but it won't be visible on your website until it's promoted to the preview or live stages. Currently, this might cause 404 errors.

To preview unpublished content: 

1. Install the Chrome extension called [AEM Sidekick](https://chrome.google.com/webstore/detail/helix-sidekick-beta/ccfggkjabjahcjoljmgmklhpaccedipo). 

    ![Install AEM SideKick](/help/edge/assets/install-aem-sidekick.png)

    After installing the extension to Chrome, don't forget to pin it, this makes it easier to find it.

    ![Pin AEM Sidekick](/help/edge/assets/pin-aem-sidekick.png)

1. To set up the Sidekick Chrome extension, go to your previously shared Google Drive or Microsoft SharePoint folder and right-click the extension icon in the browser toolbar and select `Add this project`. 

    ![AEM Sidekick - Add a project](/help/edge/assets/aem-sidekick-add-a-project.png)

    When the extension is installed and your project is added, you are ready to preview and publish your content from your Google Drive.

1. Select all the documents in the Microsoft SharePoint or Google Drive folder. You can choose multiple documents by holding down the Ctrl key (Windows/Linux) or Cmd key (Mac) while clicking.

    ![Select all the files](/help/edge/assets/select-all-files.png)

1. Click the AEM Sidekick icon pinned to your Chrome extension bar. A toolbar appears on your screen. You can choose to preview or publish your content.
    
    If you copied over `index`, `nav`, `footer` and `enquiry` files, all these are separate documents with their own preview and publish cycles, so make sure you preview (and publish) all of them.

    Upon previewing the files, new browser tabs display the documents. To preview the sample form, go to the following URL:
    

    ```HTML

    https://<branch>--<repository>--<owner>.aem.live
       
    ```

    * `<branch>` refers to the branch of your GitHub repository. 
    * `<repository>` denotes your GitHub repository. 
    * `<owner>` refers to username of your GitHub account that hosts your GitHub repository.

    
    `https://<branch>--<repo>--<owner>.aem.page/enquiry` URL. 

    For example, if your project's repository is named "wefinance", it's located under the account owner "wkndform", and you're using the "main" branch and form name as `enquiry`, the URL is: `https://main--wefinance--wkndform.aem.live/enquiry`.
    <!--(https://main--wefinance--wkndform.aem.live/enquiry).-->

### Create a form

The sample content includes an "enquiry" sheet that serves as a template for the "enquiry" form. Each row of the sheet represents a [form field](/help/edge/docs/forms/form-components.md#available-components), and the column headers define the [field properties](/help/edge/docs/forms/form-components.md#available-components). This sample form gives you a head start on building your form. 

![Enquiry form](/help/edge/docs/forms/assets/enquiry-form-microsoft-sharepoint.png)

Let's start with updating a field label. Open the 'enquiry' sheet for editing, change the label of submit button to `Let's Talk` and use AEM Sidekick to preview and publish the file. 

 ![Enquiry form](/help/edge/assets/enquiry-form-preview-publish.png)

 When you preview or publish the file, a JSON version of the file appears in a new tab. Copy the preview (.aem.page) or publish (.aem.live) URL of the file. 

 ![JSON of the form spreadsheet](/help/edge/assets/preview-and-publish-enquiry-form.png)

 Open the `enquiry` file, and replace the URL in the form block with URL of file copied in the previous step. Ensure that the URL is a hyper link. 

 ![Enquiry file with the .json URL of URL of spreadsheet](/help/edge/assets/enquiry-doc-to-embed-form.png)

 Use AEM Sidekick to preview and publish the enquiry document. 

![Enquiry file with the .json URL of URL of spreadsheet](/help/edge/assets/preview-and-publish-enquiry-document.png)


To preview the updated enquiry form go to the following URL:
    

```HTML

    https://<branch>--<repository>--<owner>.aem.page/enquiry
       
``` 

The label of the submit button is updated to `Let's Talk`. 

![Enquiry form](/help/edge/assets/updated-form.png)

<!--(https://main--wefinance--wkndform.aem.live/enquiry)-->

URL: `https://main--wefinance--wkndform.aem.live/enquiry` 
<!--(https://main--wefinance--wkndform.aem.live/enquiry)-->


For detailed information about creating and publishing a new form, head over to the [create a form](/help/edge/docs/forms/create-forms.md) guide.

### Start developing styling and functionality


To be up and running with a local AEM development environment in no time:

1. Install the AEM CLI: The AEM CLI simplifies development tasks. Let's install it globally using npm:

    ```Bash

        npm install -g @adobe/aem-cli

    ```

1. Clone your GitHub project: Clone your project repository from GitHub using the following command, replacing <owner> with the repository owner and <repo> with the repository name:

    ```

    git clone https://github.com/<owner>/<repo>

    ```

1. Start Your Local Environment: Navigate to your project directory and fire up your local AEM instance with a single command:

    ```
        
    cd <repo>
    aem up

    ```

The Adaptive Forms Block `blocks/form` folder is your playground for styling and code for your forms! Edit any `.css` or `.js` files within this directory, and you'll see the changes reflected instantly in your browser.

Ready to showcase your creation? Use Git to commit and push your changes. This updates your preview and production environments accessible at these URLs (replace placeholders with your project details):

Preview: `https://<branch>--<repo>--<owner>.aem.page/`
Production: `https://<branch>--<repo>--<owner>.aem.live/`

Congratulations! You've successfully set up your local development environment and deployed your changes.


<!--
## Add Adaptive Forms Block to your existing AEM project


>[!VIDEO](https://video.tv.adobe.com/v/3427789)

If you have an existing AEM Project, you can integrate the Adaptive Forms Block into your current project to get started on form creation. 

>[!NOTE]
>
>
> This step applies to projects built with the [AEM Boilerplate](https://github.com/adobe/aem-boilerplate). If you created your AEM project using the [AEM Forms Boilerplate](https://github.com/adobe-rnd/aem-boilerplate-forms), you can skip this step.

To Integrate:

1. **Add required files and folders**
   1. Copy and paste the following folders and files from the [AEM Forms Boilerplate](https://github.com/adobe-rnd/aem-boilerplate-forms) into your AEM Project:

      * [form block](https://github.com/adobe-rnd/aem-boilerplate-forms/tree/main/blocks/form)  folder
       * [form-common](https://github.com/adobe-rnd/aem-boilerplate-forms/tree/main/models/form-common)  folder
       * [form-components](https://github.com/adobe-rnd/aem-boilerplate-forms/tree/main/models/form-components) folder
       * [form-editor-support.js](https://github.com/adobe-rnd/aem-boilerplate-forms/blob/main/scripts/form-editor-support.js) file
       * [form-editor-support.css](https://github.com/adobe-rnd/aem-boilerplate-forms/blob/main/scripts/form-editor-support.css) file

1. **Update component definitions and models files**
    1. Navigate to the `../models/_component-definition.json` file in your AEM Project and update it with the changes from the [_component-definition.json file in the AEM Forms Boilerplate](https://github.com/adobe-rnd/aem-boilerplate-forms/blob/main/models/_component-definition.json#L39-L48).
    
    1. Navigate to the `../models/_component-models.json` file in your AEM Project and update it with the changes from the [_component-models.json file in the AEM Forms Boilerplate](https://github.com/adobe-rnd/aem-boilerplate-forms/blob/main/models/_component-models.json#L24-L26)

1. **Add Form Editor in editor script**
    1. Navigate to the `../scripts/editor-support.js` file in your AEM Project and update it with the changes from the [editor-support.js file in the AEM Forms Boilerplate](https://github.com/adobe-rnd/aem-boilerplate-forms/blob/main/scripts/editor-support.js#L105-L106)
1. **Update ESLint configuration file**
    1. Navigate to the `../.eslintignore` file in your AEM Project and add the following line of codes to prevent errors related to the Form Block rule engine:
        ```
            blocks/form/rules/formula/*
            blocks/form/rules/model/*
        ```

1. Commit and push these changes to your AEM Project repository on GitHub.

That's it! The Adaptive Forms Block is now part of your AEM project. You can start creating and adding forms to your AEM pages.
-->

## Troubleshooting GitHub build issues 

Ensure a smooth GitHub build process by addressing potential issues:

* **Resolve Module Path Error:**
    If you encounter the error "Unable to resolve path to module "'../../scripts/lib-franklin.js'", navigate to the [EDS Project]/blocks/forms/form.js file. Update the import statement by replacing the lib-franklin.js file with the aem.js file.

* **Handle Linting Errors:**
    Should you come across any linting errors, you can bypass them. Open the [EDS Project]/package.json file and modify the "lint" script from `"lint": "npm run lint:js && npm run lint:css"` to `"lint": "echo 'skipping linting for now'"`. Save the file and commit the changes to your GitHub project.


## See also

{{see-more-forms-eds}}
