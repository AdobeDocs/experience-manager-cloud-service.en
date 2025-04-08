---
title: How can we create and use themes in Adaptive Forms?
description: You can use themes to style and provide a visual identity to an Adaptive Form using Core Components. You can share a theme across any number of Adaptive Forms.
keywords: adaptive forms styling Core Components. using theme in Core Components, styling adaptive form, customizing themes
feature: Adaptive Forms, Core Components
role: User, Developer
exl-id: 11c52b66-dbb1-4c47-a94d-322950cbdac1
---
# Use themes to style Core Components based Adaptive Forms{#themes-for-af-using-core-components}

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-core-components/create-or-customize-themes-for-adaptive-forms-core-components.html)                  |
| AEM as a Cloud Service     | This article         |

You can create and apply themes to style an Adaptive Form. A theme contains styling details for the components and panels. Styles include properties such as background colors, state colors, transparency, alignment, and size. When you apply a theme, the specified style reflects on the corresponding components. A theme is managed independently without a reference to an Adaptive Form and can be reused across multiple Adaptive Forms. 

In this article, we understand how to design custom looks for Core Component based Adaptive Forms using themes.

## Available themes for styling Core Components

Forms as Cloud Service provides, the below listed themes for Core Components based Adaptive Forms:  

* [Canvas theme](https://github.com/adobe/aem-forms-theme-canvas)
* [WKND theme](https://github.com/adobe/aem-forms-theme-wknd)
* [EASEL theme](https://github.com/adobe/aem-forms-theme-easel)

## Understanding the structure of the themes

A theme is a package that includes styling components such as CSS file, JavaScript files, and resources (like icons) that define the style of your Adaptive Forms. An Adaptive Form theme follows a specific organization, consisting of the following components:

* `src/theme.scss`: This folder includes the CSS file that has a broad impact on the entire theme. It serves as a centralized location to define and manage the styling and behavior of your theme. By making edits to this file, you can make changes that are applied universally throughout the theme, influencing the appearance and functionality of both your Adaptive Forms and AEM Sites Pages.

* `src/site`: This folder contains CSS files that are applied to an entire AEM Site's page. These files consist of code and styles that affect the overall functionality and layout of your AEM Site's page. Any modifications made here is reflected across all pages of your Site. [When to use it?]

* `src/components`: The CSS files in this folder are designed for individual AEM core components. Each dedicated folder for a component includes a `.scss` file that styles that particular component within an Adaptive Form. For instance, the /src/components/accordion/_accordion.scss file contains style information for the Adaptive Forms Accordion component.  

   ![adaptive form based theme structure](/help/forms/assets/theme_structure.png)

* `src/resources`: This folder contains static files such as icons, logos, and fonts. These resources are used to enhance the visual elements and overall design of your theme.

## Create a theme 

Forms as Cloud Service provides, the below listed Adaptive Form styling themes for Core Components based Adaptive Forms.  

* [Canvas theme](https://github.com/adobe/aem-forms-theme-canvas)
* [WKND theme](https://github.com/adobe/aem-forms-theme-wknd)
* [EASEL theme](https://github.com/adobe/aem-forms-theme-easel)

You can [customize any of these themes to create new theme](#customize-a-theme-core-components). 

![Workflow of theme customization](/help/forms/assets/workflow-of-customization-of-theme.png)

## Customize a theme {#customize-a-theme-core-components}

Customizing a theme refers to the process of modifying, styling and personalizing the appearance of a theme. When you customize a theme, you change its design elements, layout, colors, typography, and sometimes the underlying code. It lets you create a unique and tailored look for your website or application while maintaining the basic structure and functionality provided by the theme.

### Prerequisites {#prerequisites-to-customize}

* Familiarize yourself with [setting up a pipeline in Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline) and having basic knowledge of how to set up a pipeline helps you efficiently manage and deploy your theme customizations. 
* Learn how to [configure a user with the contributor role](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/assign-profiles-aem.html). Understanding how to configure a user with the contributor role lets you grant the necessary permissions for theme customization.
* Install the latest release of [Apache Maven](https://maven.apache.org/download.cgi). Apache Maven is a build automation tool commonly used for Java&trade; projects. Installing the latest release ensures you have the necessary dependencies for theme customization.
* Install a plain text editor. For example, Microsoft&reg; Visual Studio Code. Using a plain text editor such as Microsoft&reg; Visual Studio Code provides a user-friendly environment for editing and modifying theme files.

### Set up your environment

* [Enable Adaptive Forms Core Components](/help/forms/enable-adaptive-forms-core-components.md)  for your local development and Cloud Service environment. 
* Configure a [front-end deployment pipeline](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/enable-frontend-pipeline-devops/create-frontend-pipeline.html) for your Cloud Service environment. Alternatively, you can configure the pipeline later, giving you the flexibility to prioritize testing and refining the theme before setting up the deployment pipeline.

<!-- 
To deploy your themes to a Forms as a Cloud Service environment, first test theme on a local development environment to address any issues. Once the theme is tested, configure the front-end deployment pipeline, which is responsible for deploying the themes.

These themes are deployed to a Forms as a Cloud Service environment via the front-end pipeline. You can configure the pipeline later also, after testing the theme on a local development environment. 

-->

After learning the pre-requisites and configuring the development environment, you are well prepared to start customizing or styling your theme according to your specific requirements.

### Customize a theme {#steps-to-customize-a-theme-core-components}

Customizing a theme is a multi-step process. To customize the theme, perform the steps in listed order:

1. [Clone a theme](#download-a-theme-core-components) 
1. [Set name of a theme](#set-name-of-theme)
1. [Customize a theme](#customize-the-theme)
1. [Test a theme](#test-the-theme)
1. [Deploy a theme](#deploy-the-theme)

The examples provided in the document are based on the **Canvas** theme, but it is important to note that you can clone any theme and customize it using the same instructions. These instructions are applicable to any theme, allowing you to modify themes according to your specific needs.

Let us start with a process to create a branded experience for your Core Component based Adaptive Forms using themes?

#### 1. Clone a theme {#download-a-theme-core-components}

To clone a theme for Core Components based Adaptive Forms, choose one of the following themes:

* [Canvas theme](https://github.com/adobe/aem-forms-theme-canvas)
* [WKND theme](https://github.com/adobe/aem-forms-theme-wknd)
* [EASEL theme](https://github.com/adobe/aem-forms-theme-easel)

To clone a theme, perform the following instructions: 

1. Open the command prompt or terminal window on your local development environment.

1. Run the `git clone` command to clone a theme. 

   ```
      git clone [Path of Git Repository of the theme]
   ```

   Replace the [Path of the Git Repository of the theme] with the actual URL of the corresponding Git Repository of the theme

   For example, to clone the Canvas theme, execute the following command:

      ```
         git clone https://github.com/adobe/aem-forms-theme-canvas
      ```

   After executing the command successfully, you have a local copy of the theme available on your machine in the  `aem-forms-theme-canvas` folder.


#### 2. Set name of a theme {#set-name-of-theme}

1. Open the theme folder in your IDE. For example, to open the `aem-forms-theme-canvas` folder in Visual Studio Code editor.
   
1. Navigate to the `aem-forms-theme-canvas` folder.
   
1. Run the following command:

   ```
      code .
   ```

      ![Open the theme folder in a plain text editor](/help/forms/assets/aem-forms-theme-folder-in-vs-code.png)

      The folder opens in the Visual Studio Code. 

1. Open the `package.json` file for editing. 

1. Set the values for the `name` and `version` attributes. 

    ![Canvas Theme name change image](/help/forms/assets/changename_canvastheme.png)

      >[!NOTE]
      >
      > * The name attribute is used to uniquely identify the theme, and the specified name is displayed in the **Style** tab of the **Form Creation Wizard**. 
      > * You have the option to select a name for your theme according to your choice, for example, `mytheme` or `customtheme`. However, for this case, we have specified the name as `aem-forms-wknd-theme`. 

1. Open the `package-lock.json` file for editing.
1. Set the values for the `name` and `version` attributes. Ensure that the values for the `name` and `version` attributes in the `Package-lock`.json file match those in the `Package.json` file.
   
    ![Canvas Theme name change image](/help/forms/assets/changename_canvastheme-package-lock.png)

1. (Optional) Open the `ReadMe` file for editing and update the name of the theme. 
   
      ![Canvas Theme name change image](/help/forms/assets/changename_canvastheme-readme-file.png)

1. Save and close the files. 

**Considerations while setting the name of the theme**

   * It is mandatory to remove the `@aemforms` from the theme name in `Package.json` file and `Package-lock.json` file. In case, you fail to remove `@aemforms` from your customized theme name, it results in the failure of the frontend pipeline during the theme deployment.
   * It is recommended to update the theme `version` in `Package.json` file and `Package-lock.json` file to accurately reflect changes and enhancements over time for your theme.
   * For the important information about the usage, installation instructions, and other relevant details, it is recommended to update the name of the theme in the `ReadMe` file.

#### 3. Customize a theme {#customize-the-theme}

You can customize individual components or make theme level changes using global variables of a theme. Any changes made to global variables impact all the individual components. For example, you can use Global variables to change the border color of all the components of an Adaptive Form and a bright fill color to set CTA (Call to action) using button component:

* [Set theme level styles](#theme-customization-global-level)

* [Set component level styles](#component-based-customization)

##### Set theme level styles{#theme-customization-global-level}

The `variable.scss` file contains the global variables of theme. By updating these variables, you can make style-related changes at the theme level. To apply theme-level styles, follow these steps:

1. Open the `<your-theme-sources>/src/site/_variables.scss` file for editing.
1. Change the value of any property. For example, the default error color is `red`. To change the error color from `red` to `blue`, change the color hex code of the `$errorvariable`. For example, `$error: #196ee5`.
1. Save and close the file.

   ![Edit theme](/help/forms/assets/edit_theme.png)

Similarly, you can use the `variable.scss` file to set font family and type, theme and font colors, font size, theme spacing, error icon, theme border styles, and more variable that impact multiple Adaptive Form components.

##### Set component level styles {#component-based-customization}

You can also change the font, color, size, and other CSS properties of a specific Adaptive Form core component. For example, button, checkbox, container, footer, and more. You can style a button or checkbox by editing the CSS file of the specific component to align it with your organization's style. To customize a style of a component:

1. Open the file `<your-theme-sources>/src/components/<component>/<component.scss>` for editing. For example, to change the font color of the button component, open the `<your-theme-sources>/src/components/button/button.scss`, file.
1. Change the value of any as per your requirements. For example, to change the color of the button component on mouse hover to `green`, change the value of the `color: $white` property in the `cmp-adaptiveform-button__widget:hover` class to hex code `#12B453` or any other shade of `green`. The final code looks like the following:

   ```
   .cmp-adaptiveform-button__widget:hover {
   background: $dark-gray;
   color: #12B453;
   }
   ```

1. Save and close the file.

   ![Edit Textbox CSS](/help/forms/assets/edit_color_textbox.png)
   
   >![NOTE]
   >
   > When a style is defined both at the theme and component level, the style defined at the component level takes priority. 

#### 4. Test a customized theme {#test-the-theme}

To preview and test the changes in the local environment and customize the theme according to the requirements for different AEM components, perform the following steps:

* 4.1 [Configure a local environment for testing](#rename-env-file-theme-folder)
* 4.2 [Test the theme using the local environment](#start-a-local-proxy-server)

##### 4.1. Configure a local environment for testing {#rename-env-file-theme-folder}

1. Open the theme folder in your IDE. For example, open the `aem-forms-theme-canvas` folder in Visual Studio Code editor.
1. Rename the `env_template` file to `.env` file in the theme folder and add the following parameters:

      ```
      * **AEM url**
      AEM_URL=https://[author-instance] 

      * **AEM Adaptive form name**
      AEM_ADAPTIVE_FORM=Form_name

      * **AEM proxy port**
      AEM_PROXY_PORT=7000

      ```

   For example, the URL of the form is `http://localhost:4502/editor.html/content/forms/af/contactusform.html`. So, the values of:

   * AEM_URL = `http://localhost:4502/`
   * AEM_ADAPTIVE_FORM = `contactusform`

1. Save the file.

   ![Canvas Theme Structure](/help/forms/assets/env-file-canvas-theme.png)

##### 4.2 Test the theme using a local environment {#start-a-local-proxy-server}

1. Navigate to the root of the theme folder. In this case, the theme folder name is `aem-forms-theme-canvas`.
1. Open the command prompt or terminal.
1. Run `npm install` to install the dependencies.
1. Run `npm run live` to preview the form with the updated theme in your local browser.

   >[!NOTE]
   >
   > If an error occurs during the execution of the `npm run live` command, execute the following commands prior `npm run live` command:
   >
   > * `npm install parcel --save-dev`
   > * `npm i @parcel/transformer-sass`

This is a hot deployment. So, whenever you make any changes and save the `_variables.scss` and `button.scss` files, the server automatically picks the changes and previews the latest output. The line `[Browsersync] File event [change]` signifies that server has recognized the latest changes and it is deploying the changes at the local environment. 

   ![Proxy browsersync](/help/forms/assets/browser_sync.png)

Having followed the examples for styling an Adaptive Form (core components) at both the theme level and component level for theme customizations, the error messages of an Adaptive Form are changed to the `blue` color, while the label color for the button component changes to `green` upon hovering.

**Previewing theme level style**

![Example: Error color set to blue](/help/forms/assets/theme-level-changes.png)

**Previewing component level style**

   ![Example: Hover color set to green](/help/forms/assets/button-customization.png)

Customizing a theme helps in designing the custom looks for Core Component based Adaptive Forms as per the organizational requirements.

###### Test the theme for forms hosted on a Cloud Service environment

You can also test the theme for the Adaptive Form hosted on your AEM Forms as a Cloud Service instance. To configure and set the local environment for the testing the themes with the Adaptive Forms hosted on the cloud instance, perform the following steps:

1. Open the theme folder in your IDE. For example, open the `aem-forms-theme-canvas` folder in Visual Studio Code editor. 
1. Rename the `env_template` file to `.env` file and add the following parameters:
   
      ```
      * **AEM url**
      AEM_URL=https://[author-instance] 

      * **AEM Adaptive form name**
      AEM_ADAPTIVE_FORM=Form_name

      * **AEM proxy port**
      AEM_PROXY_PORT=7000

      ```
   
   For example, the URL of the form at the cloud environment is `https://author-XXXX.adobeaemcloud.com/editor.html/content/forms/af/contactusform.html`. So, the values of:
      
      * AEM_URL = `https://author-XXXX-cmstg.adobeaemcloud.com/`
      * AEM_ADAPTIVE_FORM = `contactusform`
1. Save the file.
1. Create a local user. 

   >[!NOTE]
   >
   > To create a local user:
   >
   > * Go to **[!UICONTROL AEM Home]** > **[!UICONTROL Tools]** > **[!UICONTROL Security]** > **[!UICONTROL Users]** .
   > * Ensure that user is a member of the `forms-users` group.

1. Navigate to the root of the theme folder. In this case, the theme folder name is `aem-forms-theme-canvas`.
1. Run `npm run live` and you are redirected to a local browser.
1. Click `SIGN IN LOCALLY (ADMIN TASKS ONLY)` and login using the local user's credentials.

You can preview the Adaptive Form with the latest changes. Once, you are satisfied with the modifications done in a theme folder, deploy the theme to your AEM Cloud Service environment using the front-end pipeline. 

#### 5. Deploy a theme {#deploy-the-theme}

To deploy the theme to your Cloud Service environment using the front-end pipeline:

* 5.1 [Create a repository for theme](#create-a-new-theme-repo)
* 5.2 [Push the changes to the repository](#committing-the-changes)
* 5.3 [Run the frontend pipeline](#run-a-frontend-pipeline)

##### 5.1 Create a repository for theme{#create-a-new-theme-repo}

You require a repository to deploy the theme. Log in to your [AEM Cloud Manager repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git) and add new repository for your theme.

1. Create new repository for a theme by clicking the **[!UICONTROL Repositories]** > **[!UICONTROL Add Repository]**. 

   ![create new theme repo](/help/forms/assets/createrepo_canvastheme.png)

   
1. Specify the **Repository Name** in the **Add Repository** dialog box. For example, the name provided is `custom-canvas-theme-repo`.
1. Click **[!UICONTROL Save]**.

   ![Add Canvas Theme Repo](/help/forms/assets/addcanvasthemerepo.png)

1. Click **[!UICONTROL Copy Repository URL]** to copy the URL of the repository.  

   ![Canvas theme URL](/help/forms/assets/copyurl_canvastheme.png)
   
   >[!NOTE]
   > 
   > * You can use single repository for multiple themes. 
   > * To deploy different themes, you have to create separate front-end pipelines. 
   >* For example, you can use same repository, as `custom-canvas-theme-repo`, for Canvas theme, WKND theme, and EASEL theme. However, to deploy the themes, you need to create separate front-end pipelines. Future customizations for a specific theme are deployed using the corresponding front-end pipeline.

##### 5.2. Push the changes to the repository {#committing-the-changes}

Now, push the changes to the theme repository of your AEM Forms Cloud Service.

1. Navigate to the root of the theme folder.  In this case, the theme folder name is `aem-forms-theme-canvas`. 
1. Open the command prompt or terminal.
1. Run the following command in the listed order:

   ``` 
   git remote add [alias-name-for-repository] [URL of repository]
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

   ![Changes committed](/help/forms/assets/cmd_git_push.png)



##### 5.3 Run the frontend pipeline {#run-a-frontend-pipeline}

The theme is deployed using the [front-end pipeline](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/enable-frontend-pipeline-devops/create-frontend-pipeline.html). To deploy theme, perform the following steps:

1. Log in to your AEM Cloud Manager repository.
1. Click the **[!UICONTROL Add]** button from the **[!UICONTROL Pipelines]** section.
1. Select **[!UICONTROL Add Non-Production Pipeline]** or **[!UICONTROL Add Production Pipeline]** based on the Cloud Service environment. For example, here the **[!UICONTROL Add Production Pipeline]** option is selected. 
1. In the **[!UICONTROL Add Production Pipeline]** dialog as part of the **[!UICONTROL Configuration]** steps, specify the name for your pipeline. For example, the name of the pipeline is `customcanvastheme`.
1. Click **[!UICONTROL Continue]**.
1. Select the **[!UICONTROL Targeted Deployment]** > the **[!UICONTROL Front-end code]** options, in 
 the **[!UICONTROL Source Code]** steps. 
1. Select the **[!UICONTROL Repository]** and the **[!UICONTROL Git Branch]** values that have your latest changes. For example, here the selected repository name is `custom-canvas-theme-repo` and the Git branch is `main`. 
1. Select the **[!UICONTROL Code Location]** as `/`, if your changes are present at the root folder.
1. Click **[!UICONTROL Save]**.
   ![create front-endpipeline](/help/forms/assets/canvas-theme-frontendpipeline.gif)

   After the pipeline setup is complete, the call-to-action card is updated.

1. Right-click the created pipeline.
1. Click **[!UICONTROL Run]** .
    
    ![run-a-pipleine](/help/forms/assets/canvas-theme-run-pipeline.png)

Once the build is complete, the theme becomes available at the author instance for the use. It appears under the **[!UICONTROL Style]** tab in the Adaptive Form creation wizard, while creating an Adaptive Form. 

   ![custom theme available under style tab](/help/forms/assets/custom-theme-style-tab.png)

The customized theme helps in creating a branded experience for Core Component based Adaptive Forms.

## Apply a theme to an Adaptive Form {#using-theme-in-adaptive-form}

Steps to apply a theme to an Adaptive Form are:

1. Log in to your AEM Forms author instance. 

1. Select **Adobe Experience Manager** > **Forms** > **Forms & Documents**.

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

## Frequently asked questions {#faq} 

**Q:** Which customization takes priority when making customizations in a theme folder at both the global level and component level?

**Ans:** When customizations are made at both the global level and component level, the customization at the component level takes priority.  

<!--

## See next

* [Set layout of forms for different screen sizes and device types](/help/sites-cloud/authoring/page-editor/responsive-layout.md)
* [Generate Document of Record for Adaptive Forms (Core Components](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md)
* [Create an Adaptive Forms with Repeatable sections](/help/forms/create-forms-repeatable-sections.md)
* [Sample themes templates and form data models](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/sample-themes-templates-form-data-models-core-components.html)


>[!MORELIKETHIS]
>
>* [Enable Adaptive Forms Core Components on AEM Forms as a Cloud Service and local development environment](/help/forms/enable-adaptive-forms-core-components.md)

-->


## See Also {#see-also}

{{see-also}}
* [Set layout of forms for different screen sizes and device types](/help/sites-cloud/authoring/page-editor/responsive-layout.md)
* [Generate Document of Record for Adaptive Forms (Core Components](/help/forms/generate-document-of-record-for-non-xfa-based-adaptive-forms.md)
* [Create an Adaptive Forms with Repeatable sections](/help/forms/create-forms-repeatable-sections.md)
* [Sample themes templates and form data models](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/sample-themes-templates-form-data-models-core-components.html)
* [Enable Adaptive Forms Core Components on AEM Forms as a Cloud Service and local development environment](/help/forms/enable-adaptive-forms-core-components.md)
