---
title: Creating and using themes
description: You can use themes to stylize and provide a visual identity to an Adaptive Form using core components. You can share a theme across any number of Adaptive Forms.
exl-id: 11c52b66-dbb1-4c47-a94d-322950cbdac1
---
# Themes in Adaptive Forms (Core Components) {#themes-for-af-using-core-components}

You can create and apply themes to stylize an Adaptive Form using core components. A theme contains styling details for the components and panels. Styles include properties such as background colors, state colors, transparency, alignment, and size. When you apply a theme, the specified style reflects on the corresponding components. Theme is managed independently without a reference to an Adaptive Form.

When you [create an Adaptive Form](/help/forms/creating-adaptive-form.md) using core components, the Out-of-the-Box themes appear under the **Style** tab. By default, only the **Canvas** theme is available. 

>[!NOTE]
>
>An Adaptive Form theme should not be confused with [Adaptive Form templates.](/help/forms/template-editor.md) Adaptive Form themes only contain the styling information for an Adaptive Form. Adaptive Form templates define form structure and initial content and contain a theme to allow for the creation of new [Adaptive Form.](/help/forms/creating-adaptive-form.md)

## Using Canvas theme in Adaptive Forms using core components {#using-theme-in-adaptive-form}

Steps to apply theme to an Adaptive Form are:

1. Log in to your AEM Forms author instance. 

1. Tap **Adobe Experience Manager** > **Forms** > **Forms & Documents**.

1. Click **Create** > **Adaptive Forms**. The wizard for creating Adaptive Form opens.

1. Select the core component template in the **Source** tab.

    >[!NOTE]
    >
    > When you create an Adaptive Form with core components, you see the Canvas theme under the Style tab. This is the only Out-of-the-Box theme available right now. But you can change the theme to your liking and save it for future use by setting up a frontend pipeline.

1. Select the Canvas theme in the **Style** tab.
1. Click **Create**.

Adaptive Form themes are used as part of an Adaptive Form template to define styling while creating an Adaptive Form.

## Customize the theme {#customizing-theme}

To customize a theme, 

* [set up a Pipeline in Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline) 
* Configure a user with the [contributor role](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/assign-profiles-aem.html).
* You should have a [basic knowledge of Git](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#accessing-git) and Cloud Service Git repositories.

To customize a Canvas theme:

1. [Clone the Canvas theme](#1-download-canvas-theme-download-canvas-theme)
1. [Understand the structure of the theme](#2-understand-structure-of-the-canvas-theme-structure-of-canvas-theme)
1. [Change name in package.json and package_lock.json](#changename-packagelock-packagelockjson) 
1. [Create the `.env` file in the theme folder](#3-create-the-env-file-in-a-theme-folder-creating-env-file-theme-folder)
1. [Start the local proxy server](#4-start-a-local-proxy-server-starting-a-local-proxy-server)
1. [Customize the theme](#customize-the-theme-customizing-theme)
1. [Commit the changes](#6-committing-the-changes-committing-the-changes)
1. [Deploy the pipeline](#7-deploying-the-customized-theme-deploy-customized-theme)

### 1. Clone the Canvas theme {#download-canvas-theme}

Open command prompt and run the following command to clone the canvas theme:

```
git clone https://github.com/adobe/aem-forms-theme-canvas

```

 >[!NOTE]
 >
 > The Style tab of Form Creation Wizard displays the same theme name as in the package.json file.

### 2. Understand the structure of the theme {#structure-of-canvas-theme}

An Adaptive Form theme is a package containing the CSS, JavaScript, and static resources that define the styling of your form and complies with the structure of an Adaptive Form theme. An Adaptive Form theme has the following structure typical of a front-end project:

* `src/components`: JavaScript & CSS files specific to AEM core components
* `src/resources`: Static files like icons, logos, and fonts
* `src/site`: JavaScript & CSS files that apply to the entire AEM Sites page
* `src/theme.ts`: The main entry point of your JavaScript & CSS theme
* `src\theme.scss`: JavaScript & CSS files that apply to the entire theme 

The `src/components` folder has JavaScript and CSS files specific for all AEM core components such as button, checkbox, container, footer etc. You can style button or checkbox by editing the CSS file specific to the AEM component. 

   ![Editing the theme](/help/forms/assets/theme_structure.png)

To customize the theme, you can start the local proxy server to see the theme customizations in real time based on actual AEM content.

### 3. Change name in package.json and package_lock.json of Canvas theme {#changename-packagelock-packagelockjson} 

Update the name and version of Canvas theme in the `package.json` and `package_lock.json` files.

>[!NOTE]
>
> Names should not have `@aemforms` tag. It should be simple text as user-provided name. 

![Canvas Theme Pic](/help/forms/assets/changename_canvastheme.png)

### 4. Create the .env file in a theme folder {#creating-env-file-theme-folder}

Create a `.env` file in the theme folder and add the following parameters:

* **AEM url**
AEM_URL=https://[author-instance] 

* **AEM site name**
AEM_ADAPTIVE_FORM=Form_name

* **AEM proxy port**
AEM_PROXY_PORT=7000


![Canvas Theme Structure](/help/forms/assets/env-file-canvas-theme.png)

### 5. Start a local proxy server {#starting-a-local-proxy-server}

1. From the command line, navigate to the root of the theme on your local machine.
1. Execute `npm install` and npm retrieves dependencies and installs the project.
1. Execute `npm run live` and the proxy server starts.

   ![npm run live](/help/forms/assets/theme_proxy.png)

 
1. Tap or click **SIGN IN LOCALLY (ADMIN TASKS ONLY)** and sign in with the proxy user credentials provided to you by the AEM administrator.

   ![Sign in locally](/help/forms/assets/local_signin.png)

   >[!NOTE]
   >
   > * Create a local user to login locally. Provide contributor role for the theme designer.
   > * If you specify the AEM URL as `http://localhost:[port]/` in the `.env` file of Canvas theme, you are directly redirected to the browser. 

1. Once signed in, change the URL in the browser to point to the path to the sample content that the AEM administrator provided to you.

   * For example, if the path provided was `/content/formname.html?wcmmode=disabled`, change the URL to `http://localhost:[port]/content/forms/af/formname.html?wcmmode=disabled`

   ![Proxied sample content](/help/forms/assets/sample_af.png) 

Navigate to an Adaptive Form to see Canvas theme applied to an Adaptive Form. 

### 6. Customize the theme {#customize-theme}

1. In your editor, open the file `<your-theme-sources>/src/site/_variables.scss`.

    >[!NOTE]
    >
    > You can style all the Adaptive Form components in a Site directly by editing the `site/_variables.scss` file.

1. Edit the variable for the `font colour` to `red`.

    ![Edit theme](/help/forms/assets/edit_theme.png)

    **Style the different AEM components** 

    You can style the different components of an Adaptive Form by changing its CSS file in editor. There are different CSS folders for each Adaptive Form core component in the Canvas Theme folder.

    ![Core component](/help/forms/assets/theme-component.png)

    To specify styles for a specific component in theme editor, you can edit the CSS in a theme folder. For example, if you want to change the border color of a text box field, open the CSS file in editor and change its border color. 

    ![Edit Textbox CSS](/help/forms/assets/edit_color_textbox.png)

1. When you save the file, the proxy server recognizes the change via the line `[Browsersync] File event [change]`.

   ![Proxy browsersync](/help/forms/assets/browser_sync.png)

1. Switching back to your browser of the local proxy server, the change is immediately visible.

   ![change AF theme](/help/forms/assets/edit_theme_af.png)

  The theme designer previews the changes in the local proxy server and customizes the theme according to the requirements for different AEM components.

Before committing the changes into the AEM Git repository, you need to access your [Git repository information](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git).

### 7. Commit the Changes {#committing-the-changes}

After making changes to the theme and testing it with a local proxy server, commit the changes to the Git repository of your AEM Forms Cloud Service. It makes the customized theme available in your Forms Cloud Service environment  for Adaptive Forms authors to use. 

Before you commit changes to the Git repository of your AEM Forms Cloud Service, you require a clone of the repository on your local machine. To clone the repository:

1. Create a new theme repository by clicking the **[!UICONTROL Repositories]** option. 

   ![create new theme repo](/help/forms/assets/createrepo_canvastheme.png)

1. Click **[!UICONTROL Add Repository]** and specify the **Repository Name** in the **Add Repository** dialog box. Click **[!UICONTROL Save]**.

   ![Add Canvas Theme Repo](/help/forms/assets/addcanvasthemerepo.png)

1. Click **[!UICONTROL Copy Repository URL]** to copy the URL of the created repository.  

   ![Canvas theme URL](/help/forms/assets/copyurl_canvastheme.png)

1. Open the command prompt and clone the above created cloud repository.
 
    ```
    git clone https://git.cloudmanager.adobe.com/aemforms/Canvasthemerepo/

    ```
   
1. Move the files of theme repository that you are editing into the cloud repository with a command similar to
   `cp -r [source-theme-folder]/* [destination-cloud-repo]`
   For example, use this command `cp -r [C:/cloned-git-canvas/*] [C:/cloned-repo]` 
1. In the directory of the cloud repository, commit the theme files that you moved into with the following commands.

   ```text
   git add .
   git commit -a -m "Adding theme files"
   git push
   ```

1. The customizations are pushed to the Git repository.

   ![Changes committed](/help/forms/assets/cmd_git_push.png)

Your customizations are now safely stored in the Git repository.    


### 8. Run the frontend pipeline {#deploy-pipeline}

1. Create the front-end pipeline to deploy the customized theme. Learn [how to set up a frontline pipeline to deploy customized theme](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline). 
1. Run the created frontend pipeline to deploy customized theme folder under the **[!UICONTROL Style]** tab of an Adaptive Form creation wizard. 

>[!NOTE]
>
>In future if you make any modifications in the Canvas theme folder, you need to rerun the above pipeline again. Hence, it is necessary to remember the name of the pipeline.

## Example to customize the theme {#example-to-customize-a-theme}

1. Log in to your AEM Forms author instance. 
1. Open an Adaptive Form created using core components.
1. Start the local proxy server using the command prompt and click **SIGN IN LOCALLY (ADMIN TASKS ONLY)**.
1. Once signed in, you are redirected to the browser and see the applied theme. 
1. Download the [Canvas theme](https://github.com/adobe/aem-forms-theme-canvas) and extract the downloaded zip folder.
1. Open the extracted zip folder in your preferred editor.
1. Create a `.env` file in the theme folder and add parameters: **AEM URL**, **AEM_ADAPTIVE_FORM** and **AEM_PROXY_PORT**.
1. Open the CSS file of the textbox in the Canvas theme folder and change its border color to say `red` color and save the changes.
1. Reopen the browser again and you see the changes are reflected immediately in an Adaptive Form. 
1. Move the canvas theme folder in your cloned repository.
1. Commit the changes and run the fronend pipeline.

Once the pipeline is executed, the theme is available under the Style tab. 

## Best practices {#best-practices}

* **Avoiding assets from another theme**

  When you edit a theme, you can browse and add assets (such as images) from other themes. For example, you are editing the background of a page. For example, when you select **[!UICONTROL Page]** ![edit-button](assets/edit-button.png)&gt; **[!UICONTROL Background]** &gt; **[!UICONTROL Add]** &gt; **[!UICONTROL Image]**, you see a dialog that lets you browse and add images in other theme.

   You can face issues with your current theme if an asset is added from another theme, and the other theme is moved or deleted. It is recommended that you avoid browsing and adding assets from other themes.

* **Changing container panel layout width**

  Changing container panel layout width is not recommended. When you specify width of a container panel, it becomes static and does not adapt to different displays.

* **Using form editor or theme editor for working with header and footer**

  Use theme editor if you want to style header and footer using styling options such as font style, background, and transparency.
  If you want to provide information such as a logo image, company name in header, and copyright information in the footer, use the form editor options.
