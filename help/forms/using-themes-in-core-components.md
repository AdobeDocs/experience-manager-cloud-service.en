---
title: Creating and using themes
description: You can use themes to stylize and provide a visual identity to an Adaptive Form using core components. You can share a theme across any number of Adaptive Forms.
seo-description: You can create a new theme by customizing the available theme. The themes are customized and deployed using frontend pipeline.
keywords: create new theme, customize theme, upload new theme, use theme in forms, customize theme using frontend pipeline
exl-id: 11c52b66-dbb1-4c47-a94d-322950cbdac1
---
# Themes in Adaptive Forms {#themes-for-af-using-core-components}

You can create and apply themes to stylize an Adaptive Form. A theme contains styling details for the components and panels. Styles include properties such as background colors, state colors, transparency, alignment, and size. When you apply a theme, the specified style reflects on the corresponding components. Theme is managed independently without a reference to an Adaptive Form.

When you [create an Adaptive Form using core components](/help/forms/creating-adaptive-form-core-components.md), the three reference themes appear under the **Style** tab:

* [Canvas](https://github.com/adobe/aem-forms-theme-canvas) 
* [wknd](https://github.com/adobe/aem-forms-theme-wknd)
* [easel](https://github.com/adobe/aem-forms-theme-easel)

You can download the themes from the Git repositories, make customizations and save them for future use.

You can choose to perform one of the following actions with a theme:

* **Use a theme**: 
 In AEM, themes play a crucial role in styling and customizing Adaptive Forms. A theme is a predefined set of design and layout elements that can be applied to Adaptive Forms, making it easier to maintain consistent visual appearance and branding across the forms.

* **Create/customize a theme**:
AEM provides some reference themes that serve as a boilerplate for creating other themes by customizing them. Themes are personalized to make them unique and align with an organization's style.

* **Deploy a theme**:
A theme is a Git repository which is deployed to your AEM cloud service repository using the front-end pipeline. Uploading a theme enables you to apply a customized design to your web applications and Adaptive Forms.

## Using a theme in Adaptive Forms {#using-theme-in-adaptive-form}

Steps to apply theme to an Adaptive Form are:

1. Log in to your AEM Forms author instance. 

1. Tap **Adobe Experience Manager** > **Forms** > **Forms & Documents**.

1. Click **Create** > **Adaptive Forms**. The wizard for creating Adaptive Form opens.

1. Select the core component template in the **Source** tab.
1. Select the theme in the **Style** tab.
1. Click **Create**.

Adaptive Form themes are used as part of an Adaptive Form template to define styling while creating an Adaptive Form.

## Prerequisites to customize a theme {#prerequisites}

Before you start with the process of customizing a theme, you should:

* [Enable Adaptive Forms Core Components for your environment.](/help/forms/enable-adaptive-forms-core-components.md)
* Have basic knowledge on how to [set up a pipeline in Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline) 
* Have basic knowledge on how to [configure a user with the contributor role](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/assign-profiles-aem.html).
* Install the latest release of [Apache Maven.](https://maven.apache.org/download.cgi)
* Install a plain text editor. For example, Microsoft&reg; Visual Studio Code.

## Steps to customize a theme {#steps-to-customize-a-theme}

![Workflow of theme customization](/help/forms/assets/workflow-of-customization-of-theme.png)

To understand how to use and customize a theme, take the **Canvas** theme as an example.

### 1. Clone the Git repository of a theme {#download-canvas-theme}

Open a command prompt and run the following command to clone a theme (in this case, as we are taking Canvas theme as an example):

   ```
      git clone https://github.com/adobe/aem-forms-theme-canvas

   ```

Once the command is successfully executed, a local copy of the theme is available on your local machine. You can now make customizations in your local repository and deploy the changes using frontend pipeline. 


### 2. Understand the structure of a theme {#structure-of-theme}

An Adaptive Form theme is a package containing the CSS resources that define the styling of your Adaptive Form or Site. An Adaptive Form theme is organized into:

* [Component-based folders specific to Adaptive Forms.](#component-based-folder-af)
* [Files/folders applicable to AEM Site's Page](#folders-applicable-site).

#### Component-based folders specific to Adaptive Forms {#component-based-folder-af}

These folders comprise the CSS files for each component related to Adaptive Forms. They help you structure and manage the CSS and other static resources to define the styling and behavior of your Adaptive Forms. 

* `src/components`: The CSS files are designed for specific AEM core components. Each folder dedicated to a specific component includes a `.scss` file that is used to style that particular component in an Adaptive Form.

   ![adaptive form based theme structure](/help/forms/assets/theme_structure.png)

#### Files/folders applicable to AEM Site's Page {#folders-applicable-site}

These folders are relevant and applicable to the AEM Site's Page. They provide a structure to include assets, resources, and other elements that contribute to the overall appearance and functionality of AEM Site's pages. The various folders are:

* `src/resources`: This folder contains static files such as icons, logos, and fonts. These files are used to enhance the visual elements and overall design of your theme. 

* `src/site`: This folder includes CSS files that are applied to the entire AEM Site's page. These files contain code and styles that impact the overall functionality and layout of your AEM Site's page. Any modifications made here is reflected across all pages of your Site.

* `src/theme.scss`: This folder includes the CSS file that impacts the entire theme. It provides a central place to define and manage the styling and behavior of your theme. By editing this file, you can make changes that are applied throughout the theme, affecting the appearance and functionality of your Adaptive Forms and AEM Site's Page.

![Canvas Theme Structure](/help/forms/assets/site-based-theme-structure.png)

### 3. Change name in package.json and package_lock.json {#changename-packagelock-packagelockjson} 

Update the name and version of a theme in the `package.json` and `package_lock.json` files.

![Canvas Theme Pic](/help/forms/assets/changename_canvastheme.png)

>[!NOTE]
>
> * Update the name to a simple text as a user-provided name.
> * The **Style** tab of **Form Creation Wizard** displays the same theme name as present in the `package.json` file. 

### 4. Rename the env_template file {#creating-env-file-theme-folder}

Rename the `env_template` file to `.env` file in the theme folder and add the following parameters:

* **AEM url**
AEM_URL=https://[author-instance] 

* **AEM site name**
AEM_ADAPTIVE_FORM=Form_name

* **AEM proxy port**
AEM_PROXY_PORT=7000


![Canvas Theme Structure](/help/forms/assets/env-file-canvas-theme.png)


### 5. Make changes in a theme {#customize-theme}

Customization of a theme is possible at two levels:

* [Theme customization for AEM Site's page.](#theme-customization-aem-site)
* [Component-based customization specific to Adaptive Forms.](#component-based-af)

#### Theme customization for entire AEM Site's page {#theme-customization-aem-site}

The `src/site` folder includes CSS files that are applied to the entire AEM Site's page. Modify the **variable.scss** file to customize or update a theme for an entire AEM Site's page. Modify the font of all the components in an AEM Site by updating the value of font color in the `variable.scss` file.

To customize a theme, you can start the local proxy server to see the theme customizations in real time based on the actual AEM content.

1. In your text editor, open the file `<your-theme-sources>/src/site/_variables.scss`.

    >[!NOTE]
    >
    > You can style all the Adaptive Form components in a Site directly by editing the `site/_variables.scss` file.

1. Edit the variable for the `font colour` to `red`.

    ![Edit theme](/help/forms/assets/edit_theme.png)

1. When you save the file, the proxy server recognizes the change via the line `[Browsersync] File event [change]`.

   ![Proxy browsersync](/help/forms/assets/browser_sync.png)

1. Switching back to your browser of the local proxy server, the change is immediately visible.

   ![change AF theme](/help/forms/assets/edit_theme_af.png)

Similary, you can make changes in theme folder at the component level of an Adaptive Form and start a local proxy to see the changes. 

#### Component-based customization specific to Adaptive Forms {#component-based-af}

The `src/components/[component-folder]` folder has the CSS files specific for all AEM core components, for example button, checkbox, container, footer. You can style button or checkbox by editing the CSS file specific to the AEM component to make it unique and align with your organization's style. Modify the **text.scss** file to customize or update a theme at a component level, by changing the font color of the text to `grey` color.

   ![Edit Textbox CSS](/help/forms/assets/edit_color_textbox.png)

   To view the changes in the theme folder, start a local proxy. 

### 6. Test a theme {#test a theme}

The theme designers test a theme using a local proxy server. They preview the changes in the local proxy server and customize the theme according to the requirements for different AEM components.

1. From the command line, navigate to the root of the theme on your local machine.
1. Execute `npm install` and npm retrieves dependencies and installs the project.
1. Execute `npm run live` and the proxy server starts.

   ![npm run live](/help/forms/assets/theme_proxy.png)

 
1. Tap or click **SIGN IN LOCALLY (ADMIN TASKS ONLY)** and sign in with the proxy user credentials provided to you by the AEM administrator.

   ![Sign in locally](/help/forms/assets/local_signin.png)

   >[!NOTE]
   >
   > Create a local user to login locally. Provide contributor role for the theme designer.

1. Once signed in, change the URL in the browser to point to the path to the sample content that the AEM administrator provided to you.

   * For example, if the path provided was `/content/formname.html?wcmmode=disabled`, change the URL to `http://localhost:[port]/content/forms/af/formname.html?wcmmode=disabled`

   ![Proxied sample content](/help/forms/assets/sample_af.png) 

Navigate to an Adaptive Form to see theme applied without any customizations. 


### 7. Create and clone a new repository for theme {#create-a-new-theme-repo}

To save the changes, create a new repository for theme. Login to your [AEM Cloud Manager repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git) and add a new repository for your theme.

1. Create a new repository for theme by clicking the **[!UICONTROL Repositories]** option. 

   ![create new theme repo](/help/forms/assets/createrepo_canvastheme.png)
   
1. Click **[!UICONTROL Add Repository]** and specify the **Repository Name** in the **Add Repository** dialog box. Click **[!UICONTROL Save]**.

   ![Add Canvas Theme Repo](/help/forms/assets/addcanvasthemerepo.png)

   Once the new repository for theme is added to your AEM Cloud Manager repository, clone it to your local machine.


1. Click **[!UICONTROL Copy Repository URL]** to copy the URL of the created repository for theme.  

   ![Canvas theme URL](/help/forms/assets/copyurl_canvastheme.png)
   
1. Open the command prompt and clone the above created repository for theme.
 
    ```
      git clone https://git.cloudmanager.adobe.com/aemforms/Canvasthemerepo/

    ```

>[!NOTE]
> 
> One theme repository can be used for multiple themes, but the front-end pipeline configuration should be updated accordingly.


### 8. Commit the changes {#committing-the-changes}

Now, commit the changes to the theme repository of your AEM Forms Cloud Service. It makes the customized theme available in your AEM Forms Cloud Service environment for Adaptive Forms authors to use. 

1. Move the files of theme repository that you are editing into the cloned theme repository with a command similar to
   `cp -r [source-theme-folder]/* [destination-cloud-repo]`
   For example, use this command `cp -r [C:/cloned-git-canvas/*] [C:/cloned-theme-repo]` 
1. In the directory of the theme repository, commit the theme files that you moved into with the following commands.

   ```text
   git add .
   git commit -a -m "Adding theme files"
   git push
   ```

The customizations are pushed to the theme repository.

   ![Changes committed](/help/forms/assets/cmd_git_push.png)

Your customizations are now safely stored in the repository.    


### 9. Deploy a theme {#deploy-theme}

The theme is deployed using a front end pipleline.

1. Create the front-end pipeline to deploy the customized theme. Learn [how to set up a pipeline to deploy customized theme](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline). 
1. Run the created frontend pipeline to deploy customized theme folder under the **[!UICONTROL Style]** tab of an Adaptive Form creation wizard. 

>[!NOTE]
>
>In future if you make any modifications in a theme folder, you need to rerun the above pipeline again. Hence, it is necessary to remember the name of the pipeline.

Once the pipeline is successfully executed, the theme is available under the **Style** tab. Now, you [use the deployed theme for styling an Adaptive Form](#using-theme-in-adaptive-form). 

## Best practices {#best-practices}

* **Avoiding assets from another theme**

  When you edit a theme, you can browse and add assets (such as images) from other themes. For example, you are editing the background of a page. For example, when you select **[!UICONTROL Page]** ![edit-button](assets/edit-button.png)&gt; **[!UICONTROL Background]** &gt; **[!UICONTROL Add]** &gt; **[!UICONTROL Image]**, you see a dialog that lets you browse and add images in other theme.

   You can face issues with your current theme if an asset is added from another theme, and the other theme is moved or deleted. It is recommended that you avoid browsing and adding assets from other themes.

* **Changing container panel layout width**

  Changing container panel layout width is not recommended. When you specify width of a container panel, it becomes static and does not adapt to different displays.

* **Using form editor or theme editor for working with header and footer**

  Use theme editor if you want to style header and footer using styling options such as font style, background, and transparency.
  If you want to provide information such as a logo image, company name in header, and copyright information in the footer, use the form editor options.
