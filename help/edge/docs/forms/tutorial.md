---
title: Getting Started with AEM Forms Edge Delivery Services - Developer Tutorial 
description: This tutorial helps get you up-and-running with a new Adobe Experience Manager Forms (AEM) project. In ten to twenty minutes, you will have created your own forms.s
feature: Edge Delivery Services
hide: yes
hidefromtoc: yes
---

# Getting Started - Developer Tutorial 

In today's digital age, creating user-friendly forms is essential for any organization. AEM Forms Edge Delivery Services (EDS) lets you create forms using familiar tools like Google Docs and Microsoft Office. 

These forms submit data directly to a Microsoft Excel or Google Sheets file, enabling you to use vibrant ecosystem and robust APIs of Google Sheets, Microsoft Excel, and Microsoft Sharepoint to easily process submitted data or to initiate an existing business workflow.

AEM Forms provide a block, known as Adaptive Form Block, to help you easily create forms to capture and store captured data. 

This AEM Forms tutorial guides you through creating, previewing, and publishing your own custom form with a new Adobe Experience Manager (AEM) Forms project. You will also learn to add Adaptive Forms Block to an existing AEM project.  

* **[Create a new AEM project pre-equipped with Adaptive Forms block](#create-a-new-eds-project-pre-equipped-with-adaptive-forms-block)**  
* **[Add Adaptive Forms Block to an Existing AEM  project](#add-adaptive-forms-block-to-an-existing-eds-project)** 



## Prerequisites

* You have a GitHub account, and understand Git basics.
* You have a Google or Microsoft SharePoint account.
* You understand the basics of HTML, CSS, and JavaScript.
* You have Node/npm installed for local development.

**Heads up!** This tutorial uses macOS, Chrome, and Visual Studio Code. While the steps can be adapted for other setups, the screenshots and specific UI elements might differ based on your chosen operating system, browser, and code editor.


## Create a new AEM project pre-equipped with Adaptive Forms block

The AEM Forms Boilerplate template gets you started quickly with an AEM project pre-configured with the Adaptive Form Block. It's the quickest and easiest way to follow AEM best practices and jump right into building your forms.

### Get started with the AEM Forms boilerplate repository template

1. Login to your Github account.
1. Go to [https://github.com/adobe-rnd/aem-boilerplate-forms](https://github.com/adobe-rnd/aem-boilerplate-forms). 

    ![AEM Forms Boilerplate](/help/edge/assets/aem-forms-boilerplate.png)
1. Click **Use this template** and select the **Create a new repository** option, and select where you want to create this repository.
    ![Create new repository using AEM Forms Boilerplate](/help/edge/assets/create-new-repository-using-aem-forms-boilerplate.png)
    
    Adobe recommends that the repository is set to public. On the Create a new repository screen, select the **public** option. 

    ![Set the repository to public](/help/edge/assets/create-a-new-repo-keep-it-public.png)


1. Install the AEM Code Sync GitHub App on your repository. To install:
    1. Go to [https://github.com/apps/aem-code-sync/installations/new](https://github.com/apps/aem-code-sync/installations/new).
    1. On the Install AEM Code Sync screen, select the **Only select Repositories** option and select your newly created repository. Click Save.

    ![Set the repository to public](/help/edge/assets/install-aem-code-sync-app-for-your-repo.png)
    
         >[!NOTE]
         >
         >
         > If you are using Github Enterprise with IP filtering, you can add the following IP to the allow list: 3.227.118.73

    Congratulations! You have a new website running on `https://<branch>--<repo>--<owner>.hlx.page/`. In the example above that's [https://main--wefinance--wkndforms.hlx.page/](https://main--wefinance--wkndforms.hlx.page/).

    * `<branch>` refers to the branch of your GitHub repository. 
    * `<repository>` denotes your GitHub repository. 
    * `<owner>` refers to username of your GitHub account that hosts your GitHub repository.


### Link your own content source using Google Drive

Your forked Boilerplate repository from GitHub points to some [example content stored in a Google Drive folder](https://drive.google.com/drive/folders/17LSiMZC77N8tCJRW45TnHHGcG8V3SLG_). This read-only content provides a great starting point for your forms. Feel free to copy it into your own Google Drive and customize it to fit your needs. 

![Sample Content on Google Drive](/help/edge/assets/folder-with-sample-content.png)

To link your own content, 

1. Create a new folder specifically for your AEM content in Google Drive or Microsoft SharePoint. This document uses a folder created on Microsoft SharePoint.

1. Share the folder with the Adobe Experience Manager user (helix@adobe.com).

    ![Use Manage Access option to share folder with AEM User](/help/edge/assets/share-folder-with-aem-user.png)

    Ensure that you have provided editing rights on the folder to the Adobe Experience Manager user. 

    ![Share folder with AEM User, provide editing rights](/help/edge/assets/share-folder-with-aem-user-provide-editing-access.png)

1. Copy the [example content stored in the Google Drive folder](https://drive.google.com/drive/folders/17LSiMZC77N8tCJRW45TnHHGcG8V3SLG_) to your folder. To copy:

    1. Download the files together or download individual files. 

        ![Download Sample Content](/help/edge/assets/download-sample-content.png)

        The `index`, `nav`, and `footer` files  define the basic layout of your pages and rarely change throughout a project. They also have a specific structure that's different from most other content files. By examining these files, you'll get a feel for how content is organized in AEM projects.
        

    1. Upload these files to Microsoft SharePoint or Google Drive folder. 

        ![Sample Content on Google Drive](/help/edge/assets/upload-sample-files-to-your-content-folder.png)

        Ensure that you copy the  `enquiry` sheet from the sample content to your folder on Google Drive or Microsoft SharePoint. It contains structure for a sample form.      

1. Now that you have your content folder set up, it's time to link it to your project on GitHub that you created using AEM Forms Boilerplate earlier. To connect: 

    1. Login to your Github Account.
    1. Go to the GitHub repository that you created eariler using AEM Forms Boilerplate.
    1. Open the `fstab.yaml` for editing.
    1. Replace the existing reference with the path to the folder you shared with the AEM user (helix@adobe.com).

        ![Sample Content on Google Drive](/help/edge/assets/replace-path-in-fstab-yaml-with-your-content-folder.png)


        If you use the Microsoft SharePoint, the  folder path uses the following format:

        ```HTML

        https://<tenant>.sharepoint.com/sites/  <sp-site>/Shared%20Documents/<folder-name>

        ```

        For example, 

        ```HTML

        https://adobe.sharepoint.com/sites/wkndforms/Shared%20Documents/wefinance

        ```

        For more information on managing files with within Microsoft SharePoint, refer to [How to use Adobe Sharepoint](https://www.aem.live/docs/setup-customer-sharepoint).  
 

      
    1. Commit the updated 'fsatb.yaml file, once you've updated the reference and everything looks good. This will save your work and connect your  content folder to your website.

        ![Commit updated fsatab.yaml file](/help/edge/assets/commit-updated-fstab-yaml.png)


        >[!NOTE]
        >
        >
        >After updating the reference, you might experience "404 Not Found" errors initially. This is because your content is not been previewed yet. The next section explains how to start authoring and previewing your content.
    


### Preview and publish your content

After completing the last step, your new content source isn't empty, but it won't be visible on your website until it's promoted to the preview or live stages. Currently, this might cause 404 errors.

To preview unpublished content: 

1. Install the Chrome extension called [ AEM Sidekick](https://chrome.google.com/webstore/detail/helix-sidekick-beta/ccfggkjabjahcjoljmgmklhpaccedipo). 

    ![Install AEM SideKick](/help/edge/assets/install-aem-sidekick.png)

    After installing the extension to Chrome, don't forget to pin it, this makes it easier to find it.

    ![Pin AEM Sidekick](/help/edge/assets/pin-aem-sidekick.png)

1. To setup the Sidekick Chrome extension, go to your previously shared Google Drive or Microsoft SharePoint folder and right-click the extension icon in the browser toolbar and select `Add this project`. 

    ![AEM Sidekick - Add a project](/help/edge/assets/aem-sidekick-add-a-project.png)

    As soon as the extension is installed and your project is added, you are ready to preview and publish your content from your Google Drive.

1. Select all the documents in the Microsoft SharePoint or Google Drive folder. You can choose multiple documents by holding down the Ctrl key (Windows/Linux) or Cmd key (Mac) while clicking.

    ![Select all the files](/help/edge/assets/select-all-files.png)

1. Click on the AEM Sidekick icon pinned to your Chrome extension bar. A toolbar appears on your screen. You can choose to preview or publish your content.
    
    If you copied over `index`, `nav`, `footer` and `enquiry` files, all these are separate documents with their own preview and publish cycles, so make sure you preview (and publish) all of them.

    Upon previewing the files, new browser tabs display the documents. To preview the sample form go to the following URL:
    

    ```JSON

        https://<branch>--<repository>--<owner>.hlx.live/<form-path>/<form-file-name>.json
       
    ```

    * `<branch>` refers to the branch of your GitHub repository. 
    * `<repository>` denotes your GitHub repository. 
    * `<owner>` refers to username of your GitHub account that hosts your GitHub repository.

    
    `https://<branch>--<repo>--<owner>.hlx.page/enquiry` URL. 

    For example, if your project's repository is named "wefinance", it's located under the account owner "wkndforms", and you're using the "main" branch, the URL is: 
    
    

    [https://main--wefinance--wkndforms.hlx.page/enquiry](https://main--wefinance--wkndforms.hlx.page/enquiry).  


### Start developing styling and functionality


To be up and running with a local AEM development environment in no time:

1. Install the AEM CLI: The AEM CLI simplifies development tasks. Let's install it globally using npm:

    ```Bash

        npm install -g @adobe/aem-cli

    ```

1. Clone your Github project: Clone your project repository from GitHub using the following command, replacing <owner> with the repository owner and <repo> with the repository name:

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

Preview: `https://<branch>--<repo>--<owner>.hlx.page/`
Production: `https://<branch>--<repo>--<owner>.hlx.live/`
Congratulations! You've successfully set up your local development environment and deployed your changes.



## Add Adaptive Forms Block to your existing AEM project


>[!VIDEO](https://video.tv.adobe.com/v/3427789)

If you have an existing AEM Project, you can integrate the Adaptive Form Block into your current project to get started on form creation. To Integrate:

1. Clone the Adaptive Form Block repository: https://github.com/adobe-rnd/aem-boilerplate-forms to your computer. 

1. Inside the downloaded folder, find the `blocks/form` folder. Copy this folder. Now, navigate to your AEM project's local `blocks` folder and paste the copied form folder here.

1. Commit and push these changes to your AEM project on GitHub.


That's it! The Adaptive Forms Block is now part of your AEM project. You can start creating and adding forms to your AEM pages.


### Troubleshooting GitHub build issues 

Ensure a smooth GitHub build process by addressing potential issues:

* **Resolve Module Path Error:**
    If you encounter the error "Unable to resolve path to module "'../../scripts/lib-franklin.js'", navigate to the [EDS Project]/blocks/forms/form.js file. Update the import statement by replacing the lib-franklin.js file with the aem.js file.

* **Handle Linting Errors:**
    Should you come across any linting errors, you can bypass them. Open the [EDS Project]/package.json file and modify the "lint" script from "lint": "npm run lint:js && npm run lint:css" to "lint": "echo 'skipping linting for now'". Save the file and commit the changes to your GitHub project.





