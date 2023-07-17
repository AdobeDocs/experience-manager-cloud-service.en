---
title: Creating and using themes
description: You can use themes to stylize and provide a visual identity to an Adaptive Form using core components. You can share a theme across any number of Adaptive Forms.
seo-description: You can create a new theme by customizing the available theme. The themes are customized and deployed using frontend pipeline.
keywords: create new theme, customize theme, upload new theme, use theme in forms, customize theme using frontend pipeline
exl-id: 11c52b66-dbb1-4c47-a94d-322950cbdac1
---
# Themes in Adaptive Forms {#themes-for-af-using-core-components}

You can create and apply themes to style an Adaptive Form. A theme contains styling details for the components and panels. Styles include properties such as background colors, state colors, transparency, alignment, and size. When you apply a theme, the specified style reflects on the corresponding components. A theme is managed independently without a reference to an Adaptive Form and can be reused across multiple Adaptive Forms.

## Available reference themes

Forms as Cloud Service provides, the below listed reference themes for Core Components based Adaptive Forms:  

* [Canvas theme](https://github.com/adobe/aem-forms-theme-canvas)
* [WKND theme](https://github.com/adobe/aem-forms-theme-wknd)
* [EASEL theme](https://github.com/adobe/aem-forms-theme-easel)

## Understanding structure of the themes

A theme is a package that encompasses the CSS file, JavaScript files, and resources (like icons) that define the style of your Adaptive Forms. An Adaptive Form theme follows a specific organization, consisting of the following components:

* `src/theme.scss`: This folder includes the CSS file that has a broad impact on the entire theme. It serves as a centralized location to define and manage the styling and behavior of your theme. By making edits to this file, you can make changes that are applied universally throughout the theme, influencing the appearance and functionality of both your Adaptive Forms and AEM Sites Pages.

* `src/site`: This folder contains CSS files that are applied to an entire AEM Site's page. These files consist of code and styles that affect the overall functionality and layout of your AEM Site's page. Any modifications made here is reflected across all pages of your Site. [When to use it?]

* `src/components`: The CSS files in this folder are specifically designed for individual AEM core components. Each dedicated folder for a component includes a .scss file that styles that particular component within an Adaptive Form. For instance, the /src/components/accordion/_accordion.scss file contains style information for the Adaptive Forms Accordion component.  

   ![adaptive form based theme structure](/help/forms/assets/theme_structure.png)

* `src/resources`: This folder contains static files such as icons, logos, and fonts. These resources are used to enhance the visual elements and overall design of your theme.

## Create a theme 

Forms as Cloud Service provides, the below listed reference themes for Core Components based Adaptive Forms.  

* [Canvas theme](https://github.com/adobe/aem-forms-theme-canvas)
* [WKND theme](https://github.com/adobe/aem-forms-theme-wknd)
* [EASEL theme](https://github.com/adobe/aem-forms-theme-easel)

You can [customize any of these reference themes to create a new theme](#customize-a-theme-core-components). 

## Customize a theme {#customize-a-theme-core-components}

Customizing a theme refers to the process of modifying and personalizing the appearance of a theme. When you customize a theme, you make changes to its design elements, layout, colors, typography, and sometimes the underlying code. This allows you to create a unique and tailored look for your website or application while maintaining the basic structure and functionality provided by the theme.

### Prerequisites {#prerequisites-to-customize}

* Familiarize yourself with [setting up a pipeline in Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline) and having basic knowledge of how to set up a pipeline helps you efficiently manage and deploy your theme customizations. 
* Learn how to [configure a user with the contributor role](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/assign-profiles-aem.html). Understanding how to configure a user with the contributor role allows you to grant the necessary permissions for theme customization.
* Install the latest release of [Apache Maven.](https://maven.apache.org/download.cgi) Apache Maven is a build automation tool commonly used for Java projects. Installing the latest release ensures you have the necessary dependencies for theme customization.
* Install a plain text editor. For example, Microsoft&reg; Visual Studio Code. Using a plain text editor such as Microsoft&reg; Visual Studio Code provides a user-friendly environment for editing and modifying theme files.

### Setup your environment

* [Enable Adaptive Forms Core Components](/help/forms/enable-adaptive-forms-core-components.md)  for your local development and Cloud Service environment. 
* Configure [front-end deployment pipeline](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/enable-frontend-pipeline-devops/create-frontend-pipeline.html?lang=en) for your Cloud Service environment. Alternatively, you can configure the pipeline later, giving you the flexibility to prioritize testing and refining the theme before setting up the deployment pipeline.

<!-- 
To deploy your themes to a Forms as a Cloud Service environment, first test theme on a local development environment to address any issues. Once the theme is tested, configure the front-end deployment pipeline, which is responsible for deploying the themes.

These themes are deployed to a Forms as a Cloud Service environment via the front-end pipeline. You can configure the pipeline later also, after testing the theme on a local development environment. 

-->

After learning the pre-requisites and configuring the development environment, you are well-prepared to start customizing your theme according to your specific requirements.

### Steps to customize a theme {#steps-to-customize-a-theme-core-components}

Customzing a theme is a multi-step process. Perform the steps in listed order to customize the theme:

1. [Clone a reference theme](#download-a-theme-core-components) 
1. [Set name of the theme](#set-name-of-theme)
1. [Customize the theme](#customize-the-theme)
1. [Test the theme](#test-the-theme)
1. [Deploy the theme](#deploy-the-theme)

The examples provided in the document are based on the **Canvas** theme, but it is important to note that you can clone any theme and customize it using the same instructions. These instructions are applicable to any theme, allowing you to modify themes according to your specific needs.


#### 1. Clone a reference theme {#download-a-theme-core-components}

To clone a reference theme for Core Components based Adaptive Forms, choose one of the following reference themes:

* [Canvas theme](https://github.com/adobe/aem-forms-theme-canvas)
* [WKND theme](https://github.com/adobe/aem-forms-theme-wknd)
* [EASEL theme](https://github.com/adobe/aem-forms-theme-easel)

Perform the following instructions to clone a reference theme: 

1. Open the command prompt or terminal window on your local development environment.

1. Run the `git clone` command to clone a theme. 

   ```
      git clone [Path of Git Repository of the theme]
   ```

   Replace the [Path of Git Repository of the theme] with the  actual URL of the corresponding Git Repository of the theme

   For example, to clone the Canvas theme, execute the following  command:

      ```
         git clone https://github.com/adobe/aem-forms-theme-canvas
      ```

   After executing the command successfully, you have a local  copy of the theme available on your machine in the  `aem-forms-theme-canvas` folder.


#### 2. Set name of the theme {#set-name-of-theme}

1. Open the theme folder in a plain text editor. For example, to open the `aem-forms-theme-canvas` folder in Visual Studio Code editor, 
   
   1. Navigate to the `aem-forms-theme-canvas` folder.
   
   1. Run the following command:

       ```
         code .
       ```

      ![Open the theme folder in a plain text editor](/help/forms/assets/aem-forms-theme-folder-in-vs-code.png)

      The folder opens in the Visual Studio Code. 

1. Open the `package.json` file for editing. 

1. Set the values for the `name` and `description` attributes. 

      The name attribute is used to uniquely identify the theme, such as "wknd-travellers-theme" and displayed in the **Style** tab of **Form Creation Wizard**. The description attribute provides additional details about the theme, including its purpose and the scenarios it is designed for. You can also specify the version, description, and license for the theme.

1. Save and close the file. 

![Canvas Theme name change image](/help/forms/assets/changename_canvastheme.png)

>[!NOTE]
>
> * Update the name to a simple text as a user-provided name.


#### 3. Customize the theme {#make-changes-in-the-theme}

You can customize individual components or make theme level changes using global variables of a theme. Any changs made to global variables impacts all the individual components. For example, you can use Global variables to change the border color of all the components of an Adaptive Form and a bright fill color to set CTA (Call to action) using button components:

* [Set theme level styles](#theme-customization-global-level)

* [Set component level styles](#component-based-customization)

##### Set theme level styles{#theme-customization-global-level}

The `variable.scss` file contains the global of theme. You can update these variables bring theme level style related changes. To set a theme level style:

1. Open the `<your-theme-sources>/src/site/_variables.scss` file for editing.
1. Change the value of any property. For example, the default error color is `red`. To change the error color from `red` to `blue`, change the color hex code of the `$errorvariable`. For example, `$error: #196ee5`.
1. Save and close the file.

Similarly, you can use the variable.scss file to set font family and type, theme and font colors, font size, theme spacing, error icon, theme border styles, and more variable that impact multiple Adaptive Form components.

   ![Edit theme](/help/forms/assets/edit_theme.png)

##### Set component level styles {#component-based-customization}

You can also change font, color, size, and other CSS properties of a specific Adaptive Form core component. For example button, checkbox, container, footer, and more. You can style button or checkbox by editing the CSS file of the specific component to align it with your organization's style. To customize a style of a component:

1. Open the file `<your-theme-sources>/src/components/<component>/<component.scss>` for editing. For example, to change the font color of the button component, open the `<your-theme-sources>/src/components/button/button.scss`, file .
1. Change the value of any as per your requirements. For example, to change the color of the button component on mouse hover to `green`, change the value of the `color: $white` property in the `cmp-adaptiveform-button__widget:hover` class to hex code `#12B453` or any other shade of `green`. The final code looks like the following:

   ```
   .cmp-adaptiveform-button__widget:hover {
   background: $dark-gray;
   color: #12B453;
   }
   ```

1. Save and close the file.

   ![Edit Textbox CSS](/help/forms/assets/edit_color_textbox.png)


#### 4. Test the customized theme {#test-the-theme}

The theme customizations are tested on a local environment. You can preview the changes in the local proxy server and customize the theme according to the requirements for different AEM components. To test the customized theme and see the customizations in real time, perform the following steps:
4.1 [Rename the env_template file](#rename-env-file-theme-folder)
4.2 [Start a local proxy server](#start-a-local-proxy-server)

##### 4.1. Rename the env_template file {#rename-env-file-theme-folder}

1. Open the theme folder in a plain text editor. 
1. Rename the `env_template` file to `.env` file in the theme folder and add the following parameters:

      ```
      * **AEM url**
      AEM_URL=https://[author-instance] 

      * **AEM site name**
      AEM_ADAPTIVE_FORM=Form_name

      * **AEM proxy port**
      AEM_PROXY_PORT=7000

      ```

1. Save the file.

   ![Canvas Theme Structure](/help/forms/assets/env-file-canvas-theme.png)

##### 4.2 Start a local proxy server {#start-a-local-proxy-server}

1. From the command line, navigate to the root of the `aem-forms-theme-canvas` theme folder, in which you are making customizations, on your local machine.
1. Execute `npm install` and npm retrieves dependencies and installs the project.
1. Execute `npm run live` and the proxy server listens to file change and updates them in browser.

   >[!NOTE]
   >
   > If an error occurs during the execution of the `npm run live` command, execute the following commands prior to running the `npm run live` command:
   >
   > * `npm install parcel --save-dev`
   > * `npm i @parcel/transformer-sass`

When you save the `_variables.scss` and `button.scss` files, the proxy server recognizes the changes via the line `[Browsersync] File event [change]`.

   ![Proxy browsersync](/help/forms/assets/browser_sync.png)

You are directly redirected to a browser, which displays the customized changes in an Adaptive Form at global level by editing the `_variables.scss` file:

![change AF theme](/help/forms/assets/canvas_edit_theme.gif)

You can also view changes at the component level using local proxy server by modifying the `button.scss`:

   ![change AF theme](/help/forms/assets/canvas_component-level-theme-change.gif)

The theme customizations perform changes at both the global level and the component level. The error messages of an Adaptive Form changed to `blue` colour by updating the `_variables.scss` file in a theme folder. The label colour for the button component for hovering action is customized to `green` colour by modifying the `button.scss` file.  

Once, you are satisfied with the modifications done in a theme folder, deploy the theme to your Cloud Service environment using the front-end pipeline. 

>[!NOTE]
>
> In case, you want to test your AEM cloud service instance, consider the following points before executing the `npm run live` command:
>
> * Specify the `AEM URL` as `http://[author-instance]/` in the `.env` file of a theme folder.
> * Click `SIGN IN LOCALLY (ADMIN TASKS ONLY)`.
> * Ensure that the user is a member of the `forms-users` group. To create local user: Go to **[!UICONTROL AEM Home]** > **[!UICONTROL Tools]** > **[!UICONTROL Security]** > **[!UICONTROL Users]** 

#### 5. Deploy the theme {#deploy-the-theme}

To deploy the theme to your Cloud Service environment using the front-end pipeline:
5.1 [Create a new repository for theme](#create-a-new-theme-repo)
5.2 [Push the changes](#committing-the-changes)
5.3 [Run a frontend pipeline](#run-a-frontend-pipeline)

##### 5.1 Create a new repository for theme on your Cloud Service environment{#create-a-new-theme-repo}

To save the changes, create a new repository for theme. Login to your [AEM Cloud Manager repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git) and add a new repository for your theme.

1. Create a new repository for theme by clicking the **[!UICONTROL Repositories]** > **[!UICONTROL Add Repository]**. 

   ![create new theme repo](/help/forms/assets/createrepo_canvastheme.png)

   
1. Specify the **Repository Name** in the **Add Repository** dialog box. Click **[!UICONTROL Save]**.

   ![Add Canvas Theme Repo](/help/forms/assets/addcanvasthemerepo.png)

1. Click **[!UICONTROL Copy Repository URL]** to copy the URL of the created repository for theme.  

   ![Canvas theme URL](/help/forms/assets/copyurl_canvastheme.png)
   
   >[!NOTE]
   > 
   > * Make note of the copied URL for future.
   > * One theme repository is used for multiple themes, but the front-end pipeline configuration should be updated accordingly.


##### 5.2. Push the changes in the created repository {#committing-the-changes}

Now, push the changes to the theme repository of your AEM Forms Cloud Service. It makes the customized theme available in your AEM Forms Cloud Service environment for Adaptive Forms authors to use. 

1. From the command line, navigate to the root of the `aem-forms-theme-canvas` theme folder, in which you are making customizations, on your local machine. 

1. Open the command prompt or terminal window on your local development environment and execute the following command.

   ``` 
   git remote add [name-for-createdrepository] [URL of created repository]
   git add .
   git commit
   git push [name-for-createdrepository]

   ```

   For example: 

   ```
   git remote add canvascloudthemerepo https://git.cloudmanager.adobe.com/stage-aemformsdev/customcanvastheme/
   git add .
   git commit
   git push canvascloudthemerepo 

   ```

The customizations are pushed to the AEM cloud service theme repository.

   ![Changes committed](/help/forms/assets/cmd_git_push.png)

Your customizations are now safely stored in the AEM cloud service repository.    


##### 5.3 Run the frontend pipeline {#run-a-frontend-pipeline}

The theme is deployed using a front end pipleline.

1. Create the front-end pipeline to deploy the customized theme. Learn [how to set up a pipeline to deploy customized theme](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline). 

   ![create front-endpipeline](/help/forms/assets/canvas-theme-frontendpipeline.gif)

1. Run the created frontend pipeline to deploy customized theme folder under the **[!UICONTROL Style]** tab of an Adaptive Form creation wizard. 

Once the pipeline is successfully executed, the theme is available under the **Style** tab. Now, you can [use the deployed theme for styling an Adaptive Form](#using-theme-in-adaptive-form). 

![custom theme available under style tab](/help/forms/assets/custom-theme-style-tab.png)

## Apply a theme to an Adaptive Form {#using-theme-in-adaptive-form}

Steps to apply a theme to an Adaptive Form are:

1. Log in to your AEM Forms author instance. 

1. Tap **Adobe Experience Manager** > **Forms** > **Forms & Documents**.

1. Click **Create** > **Adaptive Forms**. The wizard for creating Adaptive Form opens.

1. Select the core component template in the **Source** tab.
1. Select the theme in the **Style** tab.
1. Click **Create**.

Adaptive Form themes are used as part of an Adaptive Form template to define styling while creating an Adaptive Form.

## Best practices {#best-practices}

* **Avoiding assets from another theme**

  When you edit a theme, you can browse and add assets (such as images) from other themes. For example, you are editing the background of a page. For example, when you select **[!UICONTROL Page]** ![edit-button](assets/edit-button.png)&gt; **[!UICONTROL Background]** &gt; **[!UICONTROL Add]** &gt; **[!UICONTROL Image]**, you see a dialog that lets you browse and add images in other theme.

   You can face issues with your current theme if an asset is added from another theme, and the other theme is moved or deleted. It is recommended that you avoid browsing and adding assets from other themes.

* **Changing container panel layout width**

  Changing container panel layout width is not recommended. When you specify width of a container panel, it becomes static and does not adapt to different displays.

* **Using form editor or theme editor for working with header and footer**

  Use theme editor if you want to style header and footer using styling options such as font style, background, and transparency.
  If you want to provide information such as a logo image, company name in header, and copyright information in the footer, use the form editor options.

## Frequently asked questions {#faq} 

1. Which customization takes priority when making customizations in a theme folder at both the global level and component level?

   * When customizations are made at both the global level and component level, the customization at the component level takes priority.  

