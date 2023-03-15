---
title: Build Engaging Forms Using Core Components and Headless
seo-title: Build Engaging Forms Using Core Components and Headless
description: Build Engaging Forms Using Core Components and Headless
seo-description: Build Engaging Forms Using Core Components and Headless
topic-tags: develop
hide: yes
hidefromtoc: yes
---

# Build Engaging Forms Using Core Components and Headless

## Lab Overview

In this hands-on lab, you learn:

How to use AEM Forms to easily create adaptive forms using the latest core components which are consistent with AEM Sites, enable omnichannel data capture experiences by delivering the adaptive forms as headless forms to web, mobile, and chat. You also learn best practices around styling, customizations, and front-end development.

## Key takeaways

*   **Business Agility**: As a business user, I can author Form experience for multiple channels easily.

*   **Power to frontend developer**: As a frontend developer, I can control the end-user experience using headless forms.

*   **Developer Velocity**: As a developer, I can easily and consistently customize Sites and Forms components.

## Prerequisites

AEM Forms as Cloud Service sandbox

## Lesson 1

### Objective

Familiarize yourself with AEM Forms as a Cloud Service environment.

### Lesson context

In this lesson, you familiarize yourself with AEM Forms as a Cloud Service environment by navigating the user interface.

### Exercise

1.  Open your browser and enter the URL of the Cloud Service author environment. For example:
    [https://author-p105303-e986623.adobeaemcloud.com/ui#/aem/aem/start.html](https://author-p105303-e986623.adobeaemcloud.com/ui%23/aem/aem/start.html)

1.  Log in to the Cloud Service author environment as per the credentials shared. For example:
    Username: [L716+001@summitlab.us](mailto:L716%2B001@summitlab.us) 
    Password: **Adobe123!**

1.  After you are logged in, navigate to the AEM Forms UI. Click **Forms**.

    ![](/help/forms/assets/screenshot2028113829.png)

1.  Click **Forms & Documents**. Dismiss any pop-ups related to preferences or information.

    ![](/help/forms/assets/screenshot2028113929.png)

    All the available forms are displayed.
    
    ![](/help/forms/assets/screenshot2028114029.png)

## Lesson 2

### Objective

Author an adaptive form using the latest core components, configure, and submit the form.

## Lesson context

In this lesson, as a business user, you will author an adaptive form for multiple channels like web, mobile, and chat using adaptive forms authoring with standardized OOTB core components for data capture.

## Exercise

1.  Create a submission endpoint for the form:

    1.  Open <https://requestbin.com/> in a new browser tab.
        ![](/help/forms/assets/screenshot2028114329.png)

    1.  Click **Create a public bin** and copy the endpoint URL.
        ![](/help/forms/assets/screenshot202023-03-0120at206.10.0020pm.png)

1.  Author an adaptive form using the Wizard interface:

    1.  In the browser tab used in Lesson 1, navigate to AEM Forms as Cloud Service web interface and navigate to Forms and Documents.
        ![](/help/forms/assets/screenshot2028114029.png)

    1.  Click **Create** and select Adaptive Form.
        ![](/help/forms/assets/screenshot2028114629.png)

    1.  Select the **Blank with Core Components** template from the template selection screen as shown below:
    ![](/help/forms/assets/screenshot202023-03-0120at206.09.1520pm.png)

    1.  Click the **Style** tab and select the **wknd-theme** theme as shown below:
    ![](/help/forms/assets/screenshot202023-03-0120at206.09.2320pm.png)

    1.  Click the **Submission** tab and select the **Submit to REST end-point** card and specify the public bin in the
    **URL for the POST request** field as shown below:
    ![](/help/forms/assets/screenshot202023-03-0120at206.09.5320pm.png)

    1.  Click **Create**. Specify a name and title to your form. For example, **contactus**. Click **Create**.
     ![](/help/forms/assets/screenshot2028123329.png)

    1.  The adaptive form editor opens. Dismiss any pop-ups or dialogs for preferences or information. Click the components browser on left rail and add the **Footer** component to the bottom of the blank form.
     ![](/help/forms/assets/screenshot2028121929.png)

    1.  Add the **Header** component to the top of the form.
     ![](/help/forms/assets/screenshot2028122029.png)

    1.  Add a **Title** component to the middle of the form.
     ![](/help/forms/assets/screenshot2028122129.png)

    1.  Add a **Text Input** component after the title component.
     ![](/help/forms/assets/screenshot2028122329.png)

    1.  Add a **Number Input** component.
     ![](/help/forms/assets/screenshot2028122429.png)

    1.  Add a **Submit Button** component to the form.
     ![](/help/forms/assets/screenshot2028122529.png)

    1.  Click the **Title** component so that **pop-up menu** is displayed. Click the **Edit icon** in the menu to edit the label.
     ![](/help/forms/assets/screenshot2028122629.png)

    1.  Enter `Contact Us` as the title text.
    ![](/help/forms/assets/screenshot2028122829.png)

    1.  Click the **Text Input** component so that the pop-up menu is displayed. Click the **Edit icon** in the menu to edit the label.
    ![](/help/forms/assets/screenshot2028122929.png)

    1.  Enter **Full Name** as field label.
    ![](/help/forms/assets/screenshot2028123029.png)

    1.  Click the **Number Input** component so that the pop-up menu is displayed. Click the **Edit icon** in the menu to edit the label.
    ![](/help/forms/assets/screenshot2028123129.png)

    1.  Enter the **Phone number** as the field label.
    ![](/help/forms/assets/screenshot2028123829.png)


1.  Add validations to form:

    1.  Click the **Phone number** component so that the pop-up menu is displayed. Click the **Wrench icon** in the menu to configure the field.
        ![](/help/forms/assets/screenshot2028123429.png)

    1.  Open the **validations tab**, mark the field **Required**, and click **Done**. The success message is displayed.
        ![](/help/forms/assets/screenshot2028123529.png)
        
        ![](/help/forms/assets/screenshot2028123629.png)

    1.  Click **Preview** to preview the form from an end-user perspective.
        ![](/help/forms/assets/screenshot2028125529.png)

    1.  Fill the form with dummy data
        ![](/help/forms/assets/screenshot2028125629.png)

    1.  Submit the form
        ![](/help/forms/assets/screenshot2028125729.png)

    1.  In the Request bin tab, check the submitted data.
        ![](/help/forms/assets/screenshot2028125829.png)

Now for purpose of the remaining exercise, use a pre-created registration form.

1.  Open AEM Forms management interface, for example, `https://author-p105303-e986623.adobeaemcloud.com/ui%23/aem/aem/forms.html/content/dam/formsanddocuments`, and select the registration form.
    
    ![](/help/forms/assets/screenshot2028115529.png)

1.  Click **Publish**.

    ![](/help/forms/assets/screenshot2028115629.png)
    
    The success message is displayed.

    ![](/help/forms/assets/screenshot2028115729.png)

    The publish URL of the form would be similar to `https://publish-p105303-e986623.adobeaemcloud.com/content/forms/af/registration.html`.

1.  To view the published form replace the program ID (pXXXXXX) and environment ID (eXXXXXX) in the above URL with ID's of your
    environment.

## Lesson 3

### Objective

Update styles using frontend development best practices.

### Lesson context

In this lesson, as a front-end developer, you learn how you can update styling for the previously created adaptive form easily.

### Exercise

Set up local repository of the theme:

1.  Open the Command Prompt or shell with administrator rights:

    ![](/help/forms/assets/screenshot2028115829.png)

1.  On the Command Prompt, use the following command to navigate to **c:\git** folder
    
    ```Shell
    
    cd c:\git
    
    ```

1.  Use the following command to clone the theme frontend code:
    
    ```Shell
    
    git clone -b WKND https://github.com/adobe/aem-forms-theme-canvas

    ```
    

1.  Use the following command in the listed order to navigate to the **aem-forms-theme-canvas** directory and open Visual Studio Code.
    
    ```Shell
    
    cd aem-forms-theme-canvas
    code .

    ```
    
    ![](/help/forms/assets/screenshot2028126029.png)

1.  Select **Trust the authors of all files in the parent folder** and click **Yes, I trust the authors**.

    ![](/help/forms/assets/screenshot2028116229.png)

1.  To render the form hosted on your cloud service publish environment, rename the `env_template` file.  To rename the file, right click the **env_template** file and select the **Rename** option.

    ![](/help/forms/assets/screenshot2028116429.png)

     </br>

    ![](/help/forms/assets/screenshot2028116529.png)

1.  Set the following values for the variables in .env file and save the file:

    *   **AEM_URL**: Specify your cloud service publish environment. For example, `https://publish-p105303-e986623.adobeaemcloud.com/`
    
    *   **AEM_ADAPTIVE_FORM**: Specify the path of the form. For example, if the form path is `/content/forms/af/registration`, the value of this variable would be `registration`.

    ![](/help/forms/assets/screenshot2028116429.png)
    

1.  In the Command Prompt window, run the following command:

    ```Shell

    npm install

    ```

    ![](/help/forms/assets/screenshot2028117029.png)

    >[!NOTE]
    >
    > * If you get a message asking to update npm via the `npm notice Run npm nstall -g npm@9.6.0`command, ignore the message.
    > * Do not run other npm commands unless instructed in the workbook.

1.  Now run the following command to preview the form.
    
    ```Shell
    
    npm run live
    
    ```
    
    ![](/help/forms/assets/screenshot2028117229.png)

    Once the above command is executed, wait for the `webpack compiled` message. The form is displayed in a browser tab.

    >[!NOTE]
    >
    >If you experience a blank screen in browser after executing the `npm run live` command for more than 3-4 minutes, change `localhost` in browser URL to 127.0.0.1 and hit **Enter**. 

    
    ![](/help/forms/assets/screenshot2028115129.png)


1.  In Visual Studio Code, open the `PROJECT\src\site\_variables.scss` file. Notice the `$error` color is a shade of RED.

    ![](/help/forms/assets/screenshot2028120729.png)

1.  In the browser, submit the form to see the Red color in the **First Name** field.

    ![](/help/forms/assets/screenshot2028120829.png)

1.  Set the **$error** color to **#5736eb** and save the file. 

    ![](/help/forms/assets/screenshot2028120729.png)

1.  Refresh the browser and submit the form. Notice error color on the first name field has changed accordingly.
    
    ![](/help/forms/assets/screenshot2028121129.png)

1.  In the Command Prompt, press **CTRL+C**, enter **Y**, and press **Enter** key to terminate the npm process. It is important to stop the npm server so it does not conflict with the next set of exercises.
1.  Close Visual Studio Code and Command Prompt windows.

## Lesson 4

### Objective

Render the form to web/mobile and other interfaces as a headless form.

### Lesson context

In this lesson, as a frontend developer, you will learn how you can render the adaptive form created previously as a headless form using react spectrum design framework.

### Exercise

Setup local repository using react starter project:

1.  Open the Command Prompt using administrator rights.

    ![](/help/forms/assets/screenshot2028115829.png)

1.  On the Command Prompt, use the following command to navigate to **c:\git** folder

    ```Shell
    
    cd c:\git

    ```

1.  Use the following command to clone the adaptive form react starter project:
    
    ```Shell
    
    git clone https://github.com/adobe/react-starter-kit-aem-headless-forms

    ```
    
    ![](/help/forms/assets/screenshot2028117329.png)

1.  Use the following commands in the listed order to navigate to the **react-starter-kit-aem-headless-forms** directory and open Visual Studio Code.

    ```Shell
    
    cd react-starter-kit-aem-headless-forms

    code .

    ```
    
    ![](/help/forms/assets/screenshot2028117529.png)
    

    The Visual Studio Code window opens.

    ![](/help/forms/assets/screenshot2028117429.png)

To render the form hosted on your cloud service publish environment:

1.  Rename the env_template file to .env file. To rename, right-click the **env_template** file and select the **Rename** option. 
    
    ![](/help/forms/assets/screenshot2028117629.png)
    
    ![](/help/forms/assets/screenshot2028117729.png)

1.  Set the following values for the variables in the .env file. After updating variables, save the file.

    *   **AEM_URL**: Specify the URL of the cloud service publish environment. For example, `https://publish-p105303-e986623.adobeaemcloud.com`

    *   **AEM_FORM_PATH**: Specify the path of the adaptive form created in the previous lesson. For example, `/content/forms/af/registration/`

        ![](/help/forms/assets/screenshot202023-03-0820at202.49.1820pm.png)

1.  Open the command window, ensure you are at the react-starter-kit-aem-headless-forms directory, and run the following command:

    ```Shell
    
    npm install
    
    ```

    ![](/help/forms/assets/screenshot2028118029.png)


1.  In the Command Prompt window, run the following command:
    
    ```Shell

    npm start
    
    ```

    ![](/help/forms/assets/screenshot2028118129.png)

    The above command starts a local development server which would render the form definition fetched from AEM in a headless way using the react-spectrum frontend library.

    >[!NOTE]
    >
    > 
    > If you experience a blank screen in browser after executing the `npm start` command for more than 3-4 minutes, change `localhost` in browser URL to 127.0.0.1 and hit **Enter**. 

    ![](/help/forms/assets/screenshot2028118229.png)

Let's check the execution of rules in this headless form:

1.  Select the **Check the box to receive 5% off** option. The subsequent option for applying credit card is disabled.

    ![](/help/forms/assets/screenshot2028126229.png)

1.  Uncheck **Check the box to receive 5% off** to enable the credit card option.

    ![](/help/forms/assets/screenshot2028126329.png)

Let's make changes on the form on the server as a business user and view changes reflected in the headless form automatically.

1.  Open the AEM Forms management interface in the browser. For example, [https://author-p105303-e986623.adobeaemcloud.com/ui#/aem/aem/forms.html/content/dam/formsanddocuments](https://author-p105303-e986623.adobeaemcloud.com/ui%23/aem/aem/forms.html/content/dam/formsanddocuments).

1.  Select the **registration** form and click **Edit.** It opens the form in the adaptive forms editor.

    ![](/help/forms/assets/screenshot2028118529.png)

1.  Select the **Phone number** field and click the **Edit icon (Pencil icon)** in the toolbar. If you are not able to see the pop up toolbar, switch to Edit mode by clicking **Edit** button in top right, left to **Preview** button.

    ![](/help/forms/assets/screenshot2028119629.png)

1.  Change the label to Mobile Number. Click any empty space in the form and the changes made to the form are saved.

      ![](/help/forms/assets/screenshot2028119729.png)

Let's publish the updated form to propagate the changes to publish environment.

1.  In the AEM Forms management interface tab, select the registration form, and click **Unpublish**. If you do not see the **Unpublish** button, skip to step 3 to publish the changes directly.

      ![](/help/forms/assets/screenshot2028119829.png)

1.  Click **Unpublish**. Click **Close** in respective dialog.
    
    ![](/help/forms/assets/screenshot2028119929.png)

    ![](/help/forms/assets/screenshot2028120029.png)


1.  After the browser refreshes, select the registration form and click **Publish**.

    ![](/help/forms/assets/screenshot2028120129.png)


1.  Click **Publish**. Click **Close** in the respective dialog.

    ![](/help/forms/assets/screenshot2028120329.png)
    
    ![](/help/forms/assets/screenshot2028120429.png)

1.  Refresh the browser tab with the headless form displayed. Notice, the Phone number label has changed to Mobile number.

    ![](/help/forms/assets/screenshot2028120529.png)

1.  Open the Command Prompt window that is used to start the **react-starter-kit-aem-headless-forms** project, press **CTRL+C**, then
    enter **Y** and press Enter key to terminate the npm process. It is important to stop the npm server so it does not conflict with the next set of exercises.

1.  Close Visual Studio Code and Command Prompt windows.


## Lesson 5

### Objective

Render the form as a headless form using Google Material UI

### Lesson context

In this lesson, as a front-end developer, you learn how to render the adaptive form created previously as a headless form using Google Material UI.

### Exercise

Setup local repository using Material UI starter project:

1.  Open the Command Prompt using administrator rights.
    
    ![](/help/forms/assets/screenshot2028115829.png)


1.  On the Command Prompt, use the following command to navigate to **c:\git** folder:

    ```Shell

    cd c:\git

    ```

1.  Run the following commands in the listed order to create a folder named mui and navigate to the mui folder using following commands: 

    ```Shell

    mkdir mui

    cd mui
    
    ```

1.  Use the following command to clone the adaptive form react starter project: 

    ```Shell

    git clone -b mui https://github.com/adobe/react-starter-kit-aem-headless-forms

    ```

    ![](/help/forms/assets/screenshot2028126529.png)

1.  Use the following command in the listed order to navigate to the **react-starter-kit-aem-headless-forms** folder and open the code in Visual Studio Code:

    ```Shell

    cd react-starter-kit-aem-headless-forms

    code .

    ```

    ![](/help/forms/assets/screenshot2028126829.png)

To render the form hosted on your cloud service publish environment:

1.  Rename the **env_template** file to **.env** file. To rename, right-click the **env_template** file and select **Rename**.

    ![](/help/forms/assets/screenshot2028126629.png)

1.  Set the following values for the variables in the .env file. After updating variables, save the file. Use the **CTRL + S** switch combination to save the file. 

    *   **AEM_URL**: Specify the URL of the cloud service publish environment. For example, [https://publish-p105303-e986623.adobeaemcloud.com](https://publish-p105303-e986623.adobeaemcloud.com/)

    *   **AEM_FORM_PATH**: Specify the path of the adaptive form created in the previous lesson. For example, /content/forms/af/registration/

        ![](/help/forms/assets/screenshot2028126929.png) 

1.  Open the command window, ensure you are at the **react-starter-kit-aem-headless-forms** directory, and run the following command:

    ```Shell
    
    npm install
    
    ```

    ![](/help/forms/assets/screenshot2028127029.png)

1.  In the Command Prompt window, run the following command:
    
    ```Shell

    npm start
    
    ```

    ![](/help/forms/assets/screenshot2028127129.png)
    
    The command starts a local development server and renders the form definition fetched from AEM in a headless way using the Google
    Material UI frontend library.

    >[!NOTE]
    >
    >If you experience a blank screen in browser after executing the `npm start` command for more than 3-4 minutes, change `localhost` in browser URL to 127.0.0.1 and hit **Enter**. 

    ![](/help/forms/assets/screenshot2028127229.png)

1.  To evaluate the execution of the same business logic in this form rendition: 

    Select **Check the box to receive 5% off**. The subsequent option **Would you like to apply for We.Finance Corporate Credit Card Form?** gets disabled.

    ![](/help/forms/assets/screenshot2028127329.png)

## Lesson 6

### Objective

Create an alternate look and feel of the headless form using Material UI component variations

### Lesson context

In this lesson, as a front-end developer, you learn how to create an alternate representation of different components using Material UI for the adaptive form created previously by the business user.

### Exercise

Update the variation of components in the headless project. To change the variant of the material UI text input component to `OutlinedInput`: 

1.  In Visual Code, navigate to the text input component by opening the `index.tsx` file at `src/components/textinput/index.tsx`.

1.  Add `//` at the beginning of the code line 103. It converts the line to a comment. 

    ```Shell

    //const Cmp = \'outlined\' === appliedCssClassNames ? OutlinedInput: Input;

    ```

1.  Add the following at line 104 to use a different variant of component and save the file. Use the **CTRL + S** switch combination to save the file. 

    ```Shell
    
    const Cmp = OutlinedInput;

    ```

    ![](/help/forms/assets/screenshot2028127629.png)

    It is essential to use correct capitalization for 'OutlinedInput' variant else compilation would fail. The local development environment compilation begins automatically in Command Prompt. Wait until you see the following message

    `webpack 5.75.0 compiled with 3 warnings in 6659 ms` 
    `inside proxy req`
    `setting new origin header`

1.  Refresh the browser, if it does not refresh automatically, to see text input component use a different variant.

    ![](/help/forms/assets/screenshot2028127729.png)

    
    This change happens for end users without any change to form definition at AEM Forms Server and is specific for the headless
    channel under consideration. For example, web channel in this lab.
    
    ![](/help/forms/assets/screenshot2028127529.png)


1.  Close Visual Studio Code and Command Prompt Windows.

## Frequently Asked Questions (FAQs)

+++ Is Adaptive Form wizard available publicly?  

Yes, it available with AEM Forms as Cloud Service.

+++


+++ Are core components available publicly?  

Yes, Adaptive Forms core components are available with AEM Forms as Cloud Service.

+++

+++ Are Headless forms available publicly?  

Yes, Headless forms are available with AEM Forms as Cloud Service.

+++

+++ Do Headless forms require a separate license?  

No, Headless forms use the same licensing value metric, number of form submissions.

+++

+++ Are Core components and Headless forms available with AEM 6.5 Forms?  

Yes, both adaptive forms core components and headless forms are available with AEM Forms 6.5 Service Pack 16 and onwards. 

+++


## Next steps

Now that you have learned how to build adaptive forms and deliver them to multiple channels using headless forms, you should try to put your new skills in action. Have fun and go ahead by creating and delivering exceptional data capture experiences to your end users, where they are, at scale!

## Resources

*   [Adaptive Form core components introduction](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html)

*   [Create adaptive form using core components](https://experienceleague.corp.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/creating-adaptive-form-core-components.html)

*   [Update styling for core component-based AF](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-core-components/create-an-adaptive-form-on-forms-cs/using-themes-in-core-components.html?lang=en)

*   [Headless adaptive forms](https://experienceleague.adobe.com/docs/experience-manager-headless-adaptive-forms/using/overview.html?lang=en)

*   [Using Headless React starter kit](https://experienceleague.adobe.com/docs/experience-manager-headless-adaptive-forms/using/get-started/create-and-publish-a-headless-form.html?lang=en)


