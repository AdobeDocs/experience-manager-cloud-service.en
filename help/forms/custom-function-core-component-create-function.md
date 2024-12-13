---
title: Create and add custom functions in an Adaptive Form
description: AEM Forms support custom functions, which allow users to create and use their own functions within the rule editor.
keywords: Add a custom function, use a custom function, create a custom function, use custom function in rule editor.
feature: Adaptive Forms, Core Components
role: User, Developer
exl-id: e7ab4233-2e91-45c6-9377-0c9204d03ee9
---
# Create a Custom Function for an Adaptive Form based on Core Components

Adaptive Forms based on Core Components offer dynamic user experiences by adjusting content and behavior based on user input. Custom functions allow developers to extend functionality, ensuring that forms can meet specific requirements. By integrating custom functions, developers can implement complex logic, automate processes, and introduce unique interactions that align with specific business requirements or user expectations. It ensures that the forms not only adapt to varying conditions but also provide a more precise and effective solution for diverse use cases.
This article guides you through the steps of creating custom functions for Adaptive Forms using core components.

## Considerations

* The `parameter type` and `return type` do not support `None`.

* The functions that are not supported in the custom function list are:
  * Generator functions
  * Async/Await functions 
  * Method definitions
  * Class methods
  * Default parameters
  * Rest parameters 

## Prerequisites to create a custom function

Before you begin adding a custom function to your Adaptive Forms, ensure you have the following:

**Software:**

* **Plain Text Editor (IDE)**: While any plain text editor can work, an Integrated Development Environment (IDE) like Microsoft Visual Studio Code offers advanced features for easier editing.

* **Git:** This version control system is required for managing code changes. If you do not have it installed, download it from https://git-scm.com.


## Create a custom function

Create a client library to call custom functions in the rule editor. For more information, see [Using Client-Side Libraries](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/full-stack/clientlibs.html#developing).

Steps to create custom functions are:
1. [Create a client library](#create-client-library)
1. [Add client library to an Adaptive Form](#use-custom-function)

### Create a client library {#create-client-library}

You can add custom functions by adding a client library. To create a client library, perform the following steps:

**Clone the Repository**

Clone your [AEM Forms as a Cloud Service Repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#accessing-git):

1. Open your command line or terminal window.

1. Navigate to the desired location on your machine where you want to store the repository.

1. Run the following command to clone the repository:

    `git clone [Git Repository URL]`

This command downloads the repository and creates a local folder of the cloned repository on your machine. Throughout this guide, we refer to this folder as the [AEMaaCS project directory].

**Add a Client Library Folder**

To add new client library folder to the [AEMaaCS project directory], follow these steps:

1. Open the [AEMaaCS project directory] in an editor.

    ![custom fuction folder structure](/help/forms/assets/custom-library-folder-structure.png)

1. Locate `ui.apps`.
1. Add new folder. For example, add a folder named as `experience-league`.
1. Navigate to `/experience-league/` folder and add a `ClientLibraryFolder`. For example, create a client library folder named as `customclientlibs`.

   `Location is: [AEMaaCS project directory]/ui.apps/src/main/content/jcr_root/apps/`

**Add files and folders to the Client Library folder**

Add the following to the added client library folder:
    
* .content.xml file
* js.txt file
* js folder 

`Location is: [AEMaaCS project directory]/ui.apps/src/main/content/jcr_root/apps/experience-league/customclientlibs/` 

1. In the `.content.xml` add the following lines of code:
    
    ```javascript
    <?xml version="1.0" encoding="UTF-8"?>
    <jcr:root xmlns:cq="http://www.day.com/jcr/cq/1.0" xmlns:jcr="http://www.jcp.org/jcr/1.0"
    jcr:primaryType="cq:ClientLibraryFolder"
    categories="[customfunctionscategory]"/>
    ```

   >[!NOTE]
   >
   > You can choose any name for `client library folder` and `categories` property.

1. In the `js.txt` add the following lines of code:
   
    ```javascript
          #base=js
        function.js
    ```
1. In the `js` folder, add the javascript file as `function.js` which includes the custom functions:

   ```javascript
    /**
        * Calculates Age
        * @name calculateAge
        * @param {object} field
        * @return {string} 
    */

    function calculateAge(field) {
    var dob = new Date(field);
    var now = new Date();

    var age = now.getFullYear() - dob.getFullYear();
    var monthDiff = now.getMonth() - dob.getMonth();

    if (monthDiff < 0 || (monthDiff === 0 && now.getDate() < dob.getDate())) {
    age--;
    }

    return age;
    }

    ```
1. Save the files.

 ![custom fuction folder structure](/help/forms/assets/custom-function-added-files.png)

**Include the new folder in filter.xml**:

1. Navigate to the `/ui.apps/src/main/content/META-INF/vault/filter.xml` file in your [AEMaaCS project directory].

1. Open the file and add the following line at the end:

    `<filter root="/apps/experience-league" />`
1. Save the file.

![custom fuction filter xml](/help/forms/assets/custom-function-filterxml.png)

**Deploy the newly created Client library folder to your AEM environment**

Deploy the AEM as a Cloud Service, [AEMaaCS project directory], to your Cloud Service environment. To deploy to your Cloud Service environment:

1. Commit the changes

   1.  Add, commit, and push the changes in the repository using the below commands:
         
    ```javascript

        git add .
        git commit -a -m "Adding custom functions"
        git push
    ```

1. Deploy the updated code:

    1. Trigger a deployment of your code through the existing full-stack pipeline. This automatically builds and deploys the updated code.

If you haven't already set up a pipeline, refer to the guide on [how to set up a pipeline for AEM Forms as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline).

Once the pipeline is executed successfully, the custom function added in the client library becomes available in your [Adaptive Form rule editor](/help/forms/rule-editor-core-components.md). 

### Add client library to an Adaptive Form{#use-custom-function}

Once you have deployed your client library to your Forms CS environment, use its capabilities in your Adaptive Form. To add the client library in your Adaptive Form

1. Open your form in edit mode. To open a form in edit mode, select a form and select **[!UICONTROL Edit]**.
1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens.  
1. Open the **[!UICONTROL Basic]** tab and select the name of the **[!UICONTROL client library category]** from the drop-down list (in this case, select `customfunctionscategory`).

   ![Adding the custom function client library](/help/forms/assets/clientlib-custom-function.png)

   >[!NOTE]
   >
   > Multiple categories can be added by specifying a comma-separated list within the **[!UICONTROL Client library category]** field.

1. Click **[!UICONTROL Done]**.

You can use the custom function in the [rule editor of an Adaptive Form](/help/forms/rule-editor-core-components.md) using the [JavaScript annotations](##js-annotations).

## Using a custom function in an Adaptive Form

In an Adaptive Form, you can use [custom functions within the rule editor](/help/forms/rule-editor-core-components.md). Let us add the following code to the JavaScript file (`Function.js` file) to calculate age based on the Date of Birth(YYYY-MM-DD). Create a custom function as `calculateAge()` which takes the date of birth as input and returns age:

```javascript
    /**
        * Calculates Age
        * @name calculateAge
        * @param {object} field
        * @return {string} 
    */

    function calculateAge(field) {
    var dob = new Date(field);
    var now = new Date();

    var age = now.getFullYear() - dob.getFullYear();
    var monthDiff = now.getMonth() - dob.getMonth();

    if (monthDiff < 0 || (monthDiff === 0 && now.getDate() < dob.getDate())) {
    age--;
    }

    return age;
    }

```

In the above example, when the user enters the date of birth in the format (YYYY-MM-DD), the custom function `calculateAge` is invoked and returns the age. 

![Calcualte Agae custom function in Rule Editor](/help/forms/assets/custom-function-calculate-age.png)

Let's preview the form to observe how the custom functions are implemented through the rule editor:

![Calculate Agae custom function in Rule Editor Form Preview](/help/forms/assets/custom-function-age-calculate-form.png)

>[!NOTE]
>
> You can refer to the following [custom function](/help/forms/assets//customfunctions.zip) folder. Download and install this folder in your AEM instance using the [Package Manager](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/developer-tools/package-manager).

## Features of Custom Functions

Custom functions in AEM forms offer a robust solution for extending and personalizing the functionality of your forms. You can use th custom functions to meet your organization’s specific needs.

These functions support various capabilities, including working with specific fields, using global fields, and asynchronous operations, as well as incorporating caching mechanisms. This flexibility ensures that forms can adapt to complex requirements and deliver an efficient, tailored user experience. By leveraging these advanced features, you can enhance form interactions and optimize performance, making your AEM forms both more functional and responsive.

Let's dive into the features of custom functions.

### Asynchronous support in custom functions {#support-of-async-functions}

You can implement asynchronous functions in the rule editor using custom functions. For guidance on how to do this, refer to the article [Using asynchronous functions in an Adaptive Form](/help/forms/using-async-funct-in-rule-editor.md).

### Field and Global scope objects support in custom functions {#support-field-and-global-objects}

Field objects refer to the individual components or elements within a form, such as text fields, checkboxes. The Globals object contains read-only variables such as form instance, target field instance and methods to do form modifications within custom functions. 

>[!NOTE]
>
> The `param {scope} globals` has to be the last parameter and it is not displayed in the rule editor of an Adaptive Form.

For more information on scope objects, see the [Scope objects in custom functions](/help/forms/custom-function-core-component-scope-function.md) article.

### Caching support in custom function

Adaptive Forms implement caching for custom functions to enhance response time while retrieving the custom function list in the rule editor. A message as `Fetched following custom functions list from cache` appears in the `error.log` file. 

![custom function with cache support](/help/forms/assets/custom-function-cache-error.png)

In case the custom functions are modified, the caching becomes invalidated, and it is parsed.  

## Troubleshooting

* If the JavaScript file containing code for custom functions has an error, the custom functions are not listed in the rule editor of an Adaptive Form. To check the custom function list, you can navigate to the `error.log` file for the error. In case of an error, the custom function list appears empty:

    ![error log file](/help/forms/assets/custom-function-list-error-file.png)

    In case of there is no error, the custom function are fetched and appear in the `error.log` file. A message as `Fetched following custom functions list` appears in the `error.log` file: 

    ![error log file with proper custom function](/help/forms/assets/custom-function-list-fetched-in-error.png)

## Next step

Let us now see various [examples of custom functions for an Adaptive Form based on Core Components](/help/forms/custom-function-core-components-use-cases.md).

## See Also

{{see-also-rule-editor}}
