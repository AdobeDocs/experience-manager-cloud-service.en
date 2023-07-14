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

### Customize a theme {#steps-to-customize-a-theme-core-components}

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

Customization of a theme is possible at two levels:

* [Theme customization at a global level](#theme-customization-global-level)

* [Component-based customization specific to Adaptive Forms](#component-based-customization)

##### Theme customization at a global level{#theme-customization-global-level}

Modify the `variable.scss` file to customize a theme for all the Adaptive Form components at global level. Perform the following steps to change the `$dark-gray` colour in the theme folder: 

1. In your text editor, open the file `<your-theme-sources>/src/site/_variables.scss`.

1. Edit the variable for the `$dark-gray` colour to `red`.
1. Save the changes.

    ![Edit theme](/help/forms/assets/edit_theme.png)

##### Component-based customization specific to Adaptive Forms {#component-based-customization}

You can also change font, color, size, and other CSS properties for all Adaptive Form core components, for example button, checkbox, container, footer, and more. You can style button or checkbox by editing the CSS file of the specific component to align it with your organization's style. For example, To change the font color of button component, by modifying the `button.scss` file:

1. Open the file `<your-theme-sources>/src/components/button/button.scss`, in your text editor,.
1. Modify the `button.scss` file to customize or update a theme at a component level, by changing the label color for the button component to `white` color.
1. Save the changes.

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

When you save the `_variables.scss` and `button.scss` files, the proxy server recognizes the changes via the line `[Browsersync] File event [change]`.

   ![Proxy browsersync](/help/forms/assets/browser_sync.png)

You are directly redirected to a browser, which displays the customized changes in an Adaptive Form:

   ![change AF theme](/help/forms/assets/edit_theme_af.png)

The theme customizations perform changes at both the global level and the component level. The font colour and the border colour of an Adaptive Form changed to `red` colour by updating the `_variables.scss` file in a theme folder. The label colour for the button component is customized to `white` colour by modifying the `button.scss` file.  

Once, you are satisfied with the modifications done in a theme folder, deploy the theme to your Cloud Service environment using the front-end pipeline. 

>[!NOTE]
>
> In case, you want to test your AEM cloud service instance, consider the following points before executing the `npm run live` command:
>
> * Specify the `AEM URL` as `http://[author-instance]/` in the `.env` file of a theme folder.
> * Click `SIGN IN LOCALLY (ADMIN TASKS ONLY)`.
> * Ensure that user is a member of the `forms-users` group.

#### 5. Deploy the theme {#deploy-the-theme}

To deploy the theme to your Cloud Service environment using the front-end pipeline:
5.1 [Create and clone a new repository for theme](#create-a-new-theme-repo)
5.2 [Commit and push the changes](#committing-the-changes)
5.3 [Run a frontend pipeline](#run-a-frontend-pipeline)

##### 5.1 Create and clone a new repository for theme on your Cloud Service environment{#create-a-new-theme-repo}

To save the changes, create a new repository for theme. Login to your [AEM Cloud Manager repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#accessing-git) and add a new repository for your theme.

1. Create a new repository for theme by clicking the **[!UICONTROL Repositories]** option. 

   ![create new theme repo](/help/forms/assets/createrepo_canvastheme.png)
   
1. Click **[!UICONTROL Add Repository]** and specify the **Repository Name** in the **Add Repository** dialog box. Click **[!UICONTROL Save]**.

   ![Add Canvas Theme Repo](/help/forms/assets/addcanvasthemerepo.png)

   Once the new repository for theme is added to your AEM Cloud Manager repository, now clone it to your local machine.


1. Click **[!UICONTROL Copy Repository URL]** to copy the URL of the created repository for theme.  

   ![Canvas theme URL](/help/forms/assets/copyurl_canvastheme.png)

1. Open the command prompt or terminal window on your local development environment.

1. Run the `git clone` command to clone a theme. 

   ```
      git clone [Path of created Git Repository for theme]
   ```

   Replace the [Path of created Git Repository for theme] with the  actual URL of the corresponding Git Repository for a theme.

   For example, to clone the repository, execute the following  command:

      ```
          git clone https://git.cloudmanager.adobe.com/aemforms/Canvasthemerepo/
      ```

   After executing the command successfully, you have a local  copy of the repository created for theme is available on your machine.
   
   >[!NOTE]
   > 
   > One theme repository can be used for multiple themes, but the front-end pipeline configuration should be updated accordingly.


##### 5.2. Commit and push the changes {#committing-the-changes}

Now, commit the changes to the theme repository of your AEM Forms Cloud Service. It makes the customized theme available in your AEM Forms Cloud Service environment for Adaptive Forms authors to use. 

1. Open the command prompt or terminal window on your local development environment.

1. Move the files of theme repository that you are editing into the cloned repository of an AEM cloud service with a command:
   * For Linux/Unix:
   `cp -r [source-theme-folder]/* [destination-cloud-repo]`
   For example, use this command `cp -r [C:/cloned-git-canvas/*] [C:/cloned-theme-repo]`

   * For Windows:
   `xcopy [source-theme-folder]\* [destination-cloud-repo]`
   For example, use this command `xcopy [C:\cloned-git-canvas\*] [C:\cloned-theme-repo]`

1. Navigate to the directory of the theme repository.
1. Commit and push the theme files that you moved into with the following commands.

   ```text
   git add .
   git commit -a -m "Adding theme files"
   git push
   ```

The customizations are pushed to the AEM cloud service theme repository.

   ![Changes committed](/help/forms/assets/cmd_git_push.png)

Your customizations are now safely stored in the AEM cloud service repository.    


##### 5.3 Run frontend pipeline {#run-a-frontend-pipeline}

The theme is deployed using a front end pipleline.

1. Create the front-end pipeline to deploy the customized theme. Learn [how to set up a pipeline to deploy customized theme](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline). 
1. Run the created frontend pipeline to deploy customized theme folder under the **[!UICONTROL Style]** tab of an Adaptive Form creation wizard. 

>[!NOTE]
>
>In future if you make any modifications in a theme folder, you need to rerun the above pipeline again. Hence, it is necessary to remember the name of the pipeline.

Once the pipeline is successfully executed, the theme is available under the **Style** tab. Now, you can [use the deployed theme for styling an Adaptive Form](#using-theme-in-adaptive-form). 

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


<!--

#### Understand the structure of the theme {#understand-the-structure-of-the-theme}

To explain, how to customize a theme, the documen

![Workflow of theme customization](/help/forms/assets/workflow-of-customization-of-theme.png)

To understand how to use and customize a theme, take the **Canvas** theme as an example.


You can clone the corresponding Git repositories or [create an AEM ArchType 43 or later based project](setup-local-development-environment.md) to get these themes.  

You can [create and deploy an AEM ArchType 43 or later based project](setup-local-development-environment.md#) or download these directly from corresponding Git repositories.




When you [create an Adaptive Form using core components](/help/forms/creating-adaptive-form-core-components.md), the three themes appear under the **Style** tab:

* [Canvas](https://github.com/adobe/aem-forms-theme-canvas) 
* [Reference wknd](https://github.com/adobe/aem-forms-theme-wknd)
* [Reference easel](https://github.com/adobe/aem-forms-theme-easel)

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

Once the command is successfully executed, a local copy of the theme is available on your local machine. You can now make customizations in your local repository and deploy the changes using the [frontend pipeline.](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline) 


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


### 3. Change name in package.json {#changename-packagelock} 

Change the name and version of a theme in the `package.json` file.

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

### 5. Start a local proxy server {#start-a-local-proxy-server}

The theme designers preview the changes in the local proxy server and customize the theme according to the requirements for different AEM components.

1. From the command line, navigate to the root of the theme on your local machine.
1. Execute `npm install` and npm retrieves dependencies and installs the project.
1. Execute `npm run live` and the proxy server listens to file change and updates them in browser.

   ![npm run live](/help/forms/assets/theme_proxy.png)

 
1. Click **SIGN IN LOCALLY (ADMIN TASKS ONLY)** and sign in with the proxy user credentials provided to you by the AEM administrator.

   ![Sign in locally](/help/forms/assets/local_signin.png)

   >[!NOTE]
   >
   > * Create a local user to login locally. Provide contributor role for the theme designer.
   > * If you specify the AEM URL as http://localhost:[port]/ in the`.env` file of a theme, you are directly redirected to the browser.

1. Once signed in, change the URL in the browser to point to the path to the sample content that the AEM administrator provided to you.

   * For example, if the path provided was `/content/formname.html?wcmmode=disabled`, change the URL to `http://localhost:[port]/content/forms/af/formname.html?wcmmode=disabled`

   ![Proxied sample content](/help/forms/assets/sample_af.png) 

Navigate to an Adaptive Form to see theme applied without any customizations. 

### 6. Make changes in a theme {#customize-theme}

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

1. Move the files of theme repository that you are editing into the cloned repository of an AEM cloud service with a command similar to
   `cp -r [source-theme-folder]/* [destination-cloud-repo]`
   For example, use this command `cp -r [C:/cloned-git-canvas/*] [C:/cloned-theme-repo]` 
1. In the directory of the theme repository, commit the theme files that you moved into with the following commands.

   ```text
   git add .
   git commit -a -m "Adding theme files"
   git push
   ```

The customizations are pushed to the AEM cloud service theme repository.

   ![Changes committed](/help/forms/assets/cmd_git_push.png)

Your customizations are now safely stored in the AEM cloud service repository.    


### 9. Deploy a theme {#deploy-theme}

The theme is deployed using a front end pipleline.

1. Create the front-end pipeline to deploy the customized theme. Learn [how to set up a pipeline to deploy customized theme](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html#setup-pipeline). 
1. Run the created frontend pipeline to deploy customized theme folder under the **[!UICONTROL Style]** tab of an Adaptive Form creation wizard. 

>[!NOTE]
>
>In future if you make any modifications in a theme folder, you need to rerun the above pipeline again. Hence, it is necessary to remember the name of the pipeline.

Once the pipeline is successfully executed, the theme is available under the **Style** tab. Now, you can [use the deployed theme for styling an Adaptive Form](#using-theme-in-adaptive-form). 

-->