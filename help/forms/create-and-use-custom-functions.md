---
title: Create and add custom functions in an Adaptive Form
description: AEM Forms support custom functions, which allow users to create and use their own functions within the rule editor.
keywords: Add a custom function, use a custom function, create a custom function, use custom function in rule editor.
contentOwner: Ruchita Srivastav
content-type: reference
feature: Adaptive Forms, Core Components
exl-id: 24607dd1-2d65-480b-a831-9071e20c473d
---

<span class="preview"> This article contains `Override form submission success and error handlers` as a pre-release feature. The pre-release feature is accessible only through our [pre-release channel](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features).

# Custom functions in Adaptive Forms (Core Components)

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/forms/adaptive-forms-core-components/create-and-use-custom-functions)                  |
| AEM as a Cloud Service     | This article         |

## Introduction

AEM Forms supports custom functions, allowing users to define JavaScript functions for implementing complex business rules. These custom functions extend the capabilities of forms by facilitating manipulation and processing of entered data to meet specified requirements. They also enable dynamic alteration of form behavior based on predefined criteria. 

>[!NOTE]
>
> Ensure that the [core component](https://github.com/adobe/aem-core-forms-components) is set to the latest version to use the latest features.

### Uses of custom functions {#uses-of-custom-function}

Advantages of using custom functions in Adaptive Forms are:
* **Processing of data**: Custom functions help process data entered into the forms fields.
* **Validation of data**: Custom functions enable you to perform custom checks on form inputs and provide specified error messages.
* **Dynamic behavior**: Custom functions allow you to control the dynamic behavior of your forms based on specific conditions. For example, you can show/hide fields, modify field values, or adjust form logic dynamically.
* **Integration**: You can use custom functions to integrate with external APIs or services. It helps in fetching data from external sources, sending data to external Rest endpoints, or performing custom actions based on external events.

Custom functions are essentially client libraries that are added in the JavaScript file. Once you create a custom function, it becomes available in the rule editor for selection by the user in an Adaptive Form. The custom functions are identified by the JavaScript annotations in the rule editor. 

### Supported JavaScript annotations for custom function {#js-annotations}

JavaScript annotations are used to provide metadata for JavaScript code. It includes comments that start with specific symbols, for example, /** and @. The annotations provide important information about functions, variables, and other elements in the code. Adaptive Form supports the following JavaScript annotations for custom functions:

#### Name

  The name is used to identify the custom function in the rule editor of an Adaptive Form. The following syntaxes are used to name a custom function:

  * `@name [functionName] <Function Name>`
  * `@function [functionName] <Function Name>`
  * `@func [functionName] <Function Name>`.
  `functionName` is the name of the function. Spaces are not allowed.
  `<Function Name>` is the display name of the function in the rule editor of an Adaptive Form.
    If the function name is identical to the name of the function itself, you can omit `[functionName]` from the syntax. 

#### Parameter

 The parameter is a list of arguments used by custom functions. A function can support multiple parameters. The following syntaxes are used to define a parameter in a custom function:

   * `@param {type} name <Parameter Description>`
   * `@argument` `{type} name <Parameter Description>` 
   * `@arg` `{type}` `name <Parameter Description>`.
    `{type}` represents the parameter type.  The allowed parameter types are:
    
      * string: Represents a single string value.
      * number: Represents a single numeric value.
      * boolean: Represents a single boolean value (true or false).
      * string[]: Represents an array of string values.
      * number[]: Represents an array of numeric values.
      * boolean[]: Represents an array of boolean values.
      * date: Represents a single date value.
      * date[]: Represents an array of date values.
      * array: Represents a generic array containing values of various types.
      * object: Represents form object passed to a custom function instead of passing its value directly.
      * scope: Represents the globals object, which contains read-only variables such as form instances, target field instances, and methods for performing form modifications within custom functions. It is declared as the last parameter in JavaScript annotations and is not visible in the rule editor of an Adaptive Form. The scope parameter accesses the object of the form or component to trigger the rule or event required for form processing. For further information on the Globals object and how to use it, [click here](/help/forms/create-and-use-custom-functions.md#support-field-and-global-objects).
    
The parameter type is not case-sensitive and spaces are not allowed in the parameter name.
 
`<Parameter Description>` contains details about the purpose of the parameter. It can have multiple words.

**Optional Parameters**
By default, all parameters are mandatory. You can define a parameter as optional by either adding `=` after the parameter type or enclosing the parameter name in  `[]`. Parameters defined as optional in JavaScript annotations are displayed as optional in the rule editor. 
To define a variable as an optional parameter, you can use any of the following syntaxes:
  
* `@param {type=} Input1`

In the above line of code, `Input1` is an optional parameter without any default value. To declare optional parameter with default value:
`@param {string=<value>} input1`
        
`input1` as an optional parameter with the default value set to `value`. 

* `@param {type} [Input1]`

In the above line of code, `Input1` is an optional parameter without any default value. To declare optional parameter with default value:
`@param {array} [input1=<value>]`
    `input1` is an optional parameter of array type with the default value set to `value`. 
    Ensure that the parameter type is enclosed in curly brackets {} and the parameter name is enclosed in square brackets []. 

Consider the following code snippet, where input2 is defined as an optional parameter:

```javascript

        /**
         * optional parameter function
         * @name OptionalParameterFunction
         * @param {string} input1 
         * @param {string=} input2 
         * @return {string}
        */
        function OptionalParameterFunction(input1, input2) {
        let result = "Result: ";
        result += input1;
        if (input2 !== null) {
            result += " " + input2;
        }
        return result;
        }
```

The following illustration displays using the `OptionalParameterFunction` custom function in the rule editor:

![Optional or required parameters ](/help/forms/assets/optional-default-params.png) 

You can save the rule without specifying a value for the required parameters, but the rule is not executed and displays a warning message as:

![incomplete rule warning](/help/forms/assets/incomplete-rule.png)

When the user leaves the optional parameter empty, then the "Undefined" value is passed to the custom function for the optional parameter.

To learn more about how to define optional parameters in JSDocs, [click here](https://jsdoc.app/tags-param).
    
#### Return Type

  The return type specifies the type of value that the custom function returns after execution. The following syntaxes are used to define a return type in a custom function:

  * `@return {type}`
  * `@returns {type}`
    `{type}` represents the return type of the function. The allowed return types are:
      * string: Represents a single string value.
      * number: Represents a single numeric value.
      * boolean: Represents a single boolean value (true or false).
      * string[]: Represents an array of string values.
      * number[]: Represents an array of numeric values.
      * boolean[]: Represents an array of boolean values.
      * date: Represents a single date value.
      * date[]: Represents an array of date values.
      * array: Represents a generic array containing values of various types.
      * object: Represents form object instead of its value directly.

    The return type is not case-sensitive.

#### Private

  The custom function declared as private, does not appear in the list of custom functions in the rule editor of an Adaptive form. By default, custom functions are public. The syntax to declare custom function as private is `@private`.


## Guidelines while creating custom functions

To list the custom functions in the rule editor, you can use any one of the following formats:

### Function statement with or without jsdoc comments

You can create a custom function with or without jsdoc comments. 

```javascript
    function functionName(parameters) 
        {
            // code to be executed
        }
```
If the user does not add any JavaScript annotations to the custom function, it is listed in the rule editor by its function name. However, it is recommended to include JavaScript annotations for improved readability of the custom functions.

### Arrow function with mandatory JavaScript annotations or comment

You can create a custom function with an arrow function syntax:

```javascript
    /**
    * test function
    * @name testFunction 
    * @param {string} a parameter description
    * @param {string=} b parameter description
    * @return {string}
    */
    testFunction = (a, b) => {
    return a + b;
    };
    /** */
    testFunction1=(a) => (return a)
    /** */
    testFunction2 = a => a + 100;
    
```

If the user does not add any JavaScript annotations to the custom function, the custom function is not listed in the rule editor of an Adaptive Form.

### Function expression with mandatory JavaScript annotations or comment

To list custom functions in the rule editor of an Adaptive Form, create custom functions in the following format:

```javascript
    /**
    * test function
    * @name testFunction 
    * @param {string} input1 parameter description
    * @param {string=} input2 parameter description
    * @return {string}
    */
    testFunction = function(input1,input2)
        {
            // code to be executed
        }
```

If the user does not add any JavaScript annotations to the custom function, the custom function is not listed in the rule editor of an Adaptive Form.

## Create a custom function {#create-custom-function}

Create a client library to call custom functions in the rule editor. For more information, see [Using Client-Side Libraries](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/full-stack/clientlibs.html#developing).

Steps to create custom functions are:
1. [Create a client library](#create-client-library)
1. [Add client library to an Adaptive Form](#use-custom-function)


### Prerequisites to create a custom function
Before you begin adding a custom function to your Adaptive Forms, ensure you have the following:

**Software:**

* **Plain Text Editor (IDE)**: While any plain text editor can work, an Integrated Development Environment (IDE) like Microsoft Visual Studio Code offers advanced features for easier editing.

* **Git:** This version control system is required for managing code changes. If you don't have it installed, download it from https://git-scm.com.

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

To add new client library folder to [AEMaaCS project directory], follow these steps:

1. Open the [AEMaaCS project directory] in an editor.

    ![custom fuction folder structure](/help/forms/assets/custom-library-folder-structure.png)

1. Locate `ui.apps`.
   
    `Location is: [AEMaaCS project directory]/ui.apps/src/main/content/jcr_root/apps/`

1. Add new folder. For example, add a folder named as `experience-league`.
1. Navigate to `/experience-league/` folder and add a `ClientLibraryFolder`. For example, create a client library folder named as `customclientlibs`.

**Add files and folders in Client Library Folder**

Add the following in an added client libray folder:
    
* .content.xml file
* js.txt file
* js folder 

`Location is: [AEMaaCS project directory]/ui.apps/src/main/content/jcr_root/apps/experience-league/customclientlibs/` 

1. In the `.content.xml` add the folloiwng lines of code:
    
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
1. In the `js` folder add a javascript file as `function.js` which includes the custom functions:

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

    1. Trigger a deployment of your code through the existing full-stack pipeline. This automatically builds and deploys the updated code with the new locale support.

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


### Set the dropdown list options using custom functions

Rule Editor in Core Components does not support the **Set Options of** property to set the dropdown list options at runtime. However, you can set the dropdown list options using custom functions.

Look at the code below to see how we can set the dropdown list options using custom functions:

```javascript
    /**
    * @name setEnums
    * @returns {string[]}
    **/
    function setEnums() {
    return ["0","1","2","3","4","5","6"];   
    }

    /**
    * @name setEnumNames
    * @returns {string[]}
    **/
    function setEnumNames() {
    return ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    }

```

In the above code, `setEnums` is used to set the `enum` property and `setEnumNames` is used to set the `enumNames` property of dropdown.

Let's create a rule for the `Next` button, which sets the value of dropdown list option when the user clicks the `Next` button:

![Drop-down list options](/help/forms/assets/drop-down-list-options.png)

Refer to the illustration below to demonstrate where the options of the dropdown list are set upon clicking the Display button:

![Drop down options in rule Editor](/help/forms/assets/drop-down-option-rule-editor.png)



### Support for asynchronous functions in custom functions {#support-of-async-functions}

Asynchronous custom functions do not appear in the rule editor list. However, it is possible to invoke asynchronous functions within custom functions created using synchronous function expressions.

 ![Sync and async custom function](/help/forms/assets/workflow-for-sync-async-custom-fumction.png)

>[!NOTE]
>
> The advantage of calling asynchronous functions in custom functions is that asynchronous functions allow concurrent execution of multiple tasks, with the result of each function used within the custom functions.

Look at the code below to see how we can invoke asynchronous functions using custom functions:

```javascript
    
    async function asyncFunction() {
    const response = await fetch('https://petstore.swagger.io/v2/store/inventory');
    const data = await response.json();
    return data;
    }

    /**
    * callAsyncFunction
    * @name callAsyncFunction callAsyncFunction
    */
    function callAsyncFunction() {
    asyncFunction()
        .then(responseData => {
        console.log('Response data:', responseData);
        })
        .catch(error => {
         console.error('Error:', error);
    });
}

```

In the above example, the asyncFunction function is an `asynchronous function`. It performs an asynchronous operation by making a `GET` request to `https://petstore.swagger.io/v2/store/inventory`. It waits for the response using `await`, parses the response body as JSON using the `response.json()`, and then returns the data. The `callAsyncFunction` function is a synchronous custom function that invokes the `asyncFunction` function and displays the response data in the console. Although the `callAsyncFunction` function is synchronous, it calls the asynchronous asyncFunction function and handles its result with `then` and `catch` statements.

To see its working, let us add a button and create a rule for the button that invokes the asynchronous function upon a button click.

 ![creating rule for async function](/help/forms/assets/rule-for-async-funct.png)

Refer to the illustration of the console window below to demonstrate that when the user clicks the `Fetch` button, the custom function `callAsyncFunction` is invoked, which in turn calls an asynchronous function `asyncFunction`. Inspect the console window to view the response to the button click:

 ![Console window](/help/forms/assets/async-custom-funct-console.png)

Let's dive into the features of custom functions.

## Various features for Custom Functions
  
You can use custom functions to add personalized features to forms. These functions support various abilities such as working with specific fields, using global fields, or caching. This flexibility allows you to customize forms according to your organization's requirements.

### Field and Global scope objects in custom functions {#support-field-and-global-objects}

Field objects refer to the individual components or elements within a form, such as text fields, checkboxes. The Globals object contains read-only variables such as form instance, target field instance and methods to do form modifications within custom functions. 

>[!NOTE]
>
> The `param {scope} globals` has to be the last parameter and it is not displayed in the rule editor of an Adaptive Form.

<!-- Let us look at the following code snippet:

```JavaScript
   
    /**
    * updateDateTime
    * @name updateDateTime
    * @param {object} field
    * @param {scope} globals
    */
    function updateDateTime(field, globals) {
    // Accessing the Date object from the global scope
    var currentDate = new Date();
    // Formatting the date and time
    var formattedDateTime = currentDate.toLocaleString();
    // Updating the field value with the formatted date and time using setProperty.
    globals.functions.setProperty(field, {value: formattedDateTime});
    }
```

In the above code snippet, a custom function named `updateDateTime` takes parameters such as a field object and a global object. The field represents the textbox object where the formatted date and time value is displayed within the form. -->

Let's learn how custom functions use field and global objects with the help of a `Contact Us` form using different use cases.

![Contact Us Form](/help/forms/assets/contact-us-form.png)

+++ **Use Case**: Show a panel using the `SetProperty` rule

Add the following code in the custom function as explained in the [create-custom-function ](#create-custom-function) section, to set the form field as `Required`.

```javascript
    
    /**
    * enablePanel
    * @name enablePanel
    * @param {object} field1
    * @param {object} field2
    * @param {scope} globals 
    */

    function enablePanel(field1,field2, globals)
    {
       if(globals.functions.validate(field1).length === 0)
       {
       globals.functions.setProperty(field2, {visible: true});
       }
    }
```

>[!NOTE]
>
> * You can configure the field properties using the available properties located in `[form-path]/jcr:content/guideContainer.model.json`.
> * Modifications made to the form using the `setProperty` method of the Globals object are asynchronous in nature and are not reflected during the execution of the custom function.

In this example, validation of the `personaldetails` panel occurs upon clicking the button. If no errors are detected in the panel, another panel, the `feedback` panel, becomes visible upon button click.

Let's create a rule for the `Next` button, which validates the `personaldetails` panel and makes the `feedback`  panel visible when the user clicks the `Next` button.

![Set Property](/help/forms/assets/custom-function-set-property.png)

Refer to the illustration below to demonstrate where the `personaldetails` panel is validated upon clicking the `Next` button. In case all the fields within the `personaldetails` are validated, the `feedback` panel becomes visible.

![Set Property Form Preview](/help/forms/assets/set-property-form-preview.png)

If errors are present in the fields of the `personaldetails` panel, they are displayed at the field level upon clicking the `Next` button, and the `feedback` panel remains invisible.

![Set Property Form Preview](/help/forms/assets/set-property-panel.png)

+++

+++ **Use Case**: Validate the field.

Add the following code in the custom function as explained in the [create-custom-function ](#create-custom-function) section, to validate the field.

```javascript

    /**
    * validateField
    * @name validateField
    * @param {object} field
    * @param {scope} globals
    */
    function validateField(field,globals)
    {
    
        globals.functions.validate(field);
    
    }   
```

>[!NOTE]
>
> If no argument is passed in the `validate()` function, it validates the form.

In this example, a custom validation pattern is applied to the `contact` field. Users are required to input a phone number starting with `10` followed by `8` digits. If the user enters a phone number that does not start with `10` or contains more or less than `8` digits, a validation error message appears upon the button click:

![Email Address Validation Pattern](/help/forms/assets/custom-function-validation-pattern.png)

Now, next step is to create a rule for the `Next` button that validates the `contact` field on the button click.

![Validation Pattern](/help/forms/assets/custom-function-validate.png)

Refer to the illustration below to demonstrate that if the user enters a phone number that does not start with `10`, an error message appears at the field level:

![Email Address Validation Pattern](/help/forms/assets/custom-function-validate-error-message.png)

If the user enters a valid phone number and all fields in the `personaldetails` panel are validated, the `feedback` panel appears on the screen:

![Email Address Validation Pattern](/help/forms/assets/validate-form-preview-form.png)

+++

+++ **Use Case**: Reset a panel

Add the following code in the custom function as explained in the [create-custom-function ](#create-custom-function) section, to reset the panel.

```javascript
    /**
    * resetField
    * @name  resetField
    * @param {string} input1
    * @param {object} field
    * @param {scope} globals 
    */
    function  resetField(field,globals)
    {
    
        globals.functions.reset(field);
    
    }
```

>[!NOTE]
>
> If no argument is passed in the `reset()` function, it validates the form.

In this example, the `personaldetails` panel resets upon clicking the `Clear` button. Next step is to create a rule for the `Clear` button that resets the panel on the button click.

![Clear button](/help/forms/assets/custom-function-reset-field.png)

See the illustration below to display that if the user clicks the `clear` button, the `personaldetails` panel resets:

![Reset Form](/help/forms/assets/custom-function-reset-form.png)

+++

+++ **Use Case**: To display a custom message at the field level and marking the field as invalid

You can use the `markFieldAsInvalid()` function to define a field as invalid and set custom error message at a field level. The `fieldIdentifier` value can be `fieldId`, or `field qualifiedName`, or `field dataRef`. The value of the object named `option` can be `{useId: true}`, `{useQualifiedName: true}`, or `{useDataRef: true}`. 
The syntaxes used to mark a field as invalid and set a custom message are:

* `globals.functions.markFieldAsInvalid(field.$id,"[custom message]",{useId: true});`
* `globals.functions.markFieldAsInvalid(field.$qualifiedName, "[custom message]", {useQualifiedName: true});`
* `globals.functions.markFieldAsInvalid(field.$dataRef, "[custom message]", {useDataRef: true});`

Add the following code in the custom function as explained in the [create-custom-function ](#create-custom-function) section, to enable a custom message at the field level.

```javascript

    /**
    * customMessage
    * @name customMessage
    * @param {object} field
    * @param {scope} globals 
    */
    function customMessage(field, globals) {
    const minLength = 15;
    const comments = field.$value.trim();
    if (comments.length < minLength) {
        globals.functions.markFieldAsInvalid(field.$id, "Comments must be at least 15 characters long.", { useId: true });
    }
}
```

In this example, if the user enters less than 15 characters in the comments textbox, a custom message appears at the field level.

Next step is to create a rule for the `comments` field:

![Mark field as Invalid](/help/forms/assets/custom-function-invalid-field.png)

See the demonstration below to display that entering negative feedback in the `comments` field triggers the display of a custom message at the field level:

![Mark field as Invalid Preview form](/help/forms/assets/custom-function-invalidfield-form.png)

If the user enters more than 15 characters in the comments textbox, the field gets validated and the form is submitted:

![Mark field as valid Preview form](/help/forms/assets/custom-function-validfield-form.png)

+++

+++ **Use Case**: Submit altered data to the server

The following line of code: 
`globals.functions.submitForm(globals.functions.exportData(), false);` is used to submit the form data after manipulation. 
* The first argument is the data to be submitted. 
* The second argument represents whether the form is to be validated before submission. It is `optional` and set as `true` by default. 
* The third argument is the `contentType` of the submission, which is also optional with the default value as `multipart/form-data`. The other values can be `application/json` and `application/x-www-form-urlencoded`.
  
Add the following code in the custom function as explained in the [create-custom-function ](#create-custom-function) section, to submit the manipulated data at the server:

```javascript

    /**
    * submitData
    * @name submitData
    * @param {object} field
    * @param {scope} globals 
    */
    function submitData(globals)
    {
    
    var data = globals.functions.exportData();
    if(!data.comments) {
    data.comments = 'NA';
    }
    console.log('After update:{}',data);
    globals.functions.submitForm(data, false);
    }

```

In this example, if the user leaves the `comments` textbox empty, the `NA` is submitted to the server at form submission.

Now, create a rule for the `Submit` button that submits data:

![Submit data](/help/forms/assets/custom-function-submit-data.png)

Refer to the illustration of the `console window` below to demonstrate that if the user leaves the `comments` textbox empty, then the value as `NA` is submitted at the server:

![Submit data at the console window](/help/forms/assets/custom-function-submit-data-form.png)

You can also inspect the console window to view the data submitted to the server:

![Inspect data at the console window](/help/forms/assets/custom-function-submit-data-console-data.png)

+++

+++ **Use Case**: Override form submission success and error handlers 

Add the following line of code as explained in the [create-custom-function ](#create-custom-function) section, to customize the submission or failure message for form submissions and display the form submission messages in a modal box:

```javascript
/**
 * Handles the success response after a form submission.
 *
 * @param {scope} globals - This object contains a read-only form instance, target field instance, triggered event, and methods for performing form modifications within custom functions.
 * @returns {void}
 */
function customSubmitSuccessHandler(globals) {
    var event = globals.event;
    var submitSuccessResponse = event.payload.body;
    var form = globals.form;

    if (submitSuccessResponse) {
        if (submitSuccessResponse.redirectUrl) {
            window.location.href = encodeURI(submitSuccessResponse.redirectUrl);
        } else if (submitSuccessResponse.thankYouMessage) {
            showModal("success", submitSuccessResponse.thankYouMessage);
        }
    }
}

/**
 * Handles the error response after a form submission.
 *
 * @param {string} customSubmitErrorMessage - The custom error message.
 * @param {scope} globals - This object contains a read-only form instance, target field instance, triggered event, and methods for performing form modifications within custom functions.
 * @returns {void}
 */
function customSubmitErrorHandler(customSubmitErrorMessage, globals) {
    showModal("error", customSubmitErrorMessage);
}
function showModal(type, message) {
    // Remove any existing modals
    var existingModal = document.getElementById("modal");
    if (existingModal) {
        existingModal.remove();
    }

    // Create the modal dialog
    var modal = document.createElement("div");
    modal.setAttribute("id", "modal");
    modal.setAttribute("class", "modal");

    // Create the modal content
    var modalContent = document.createElement("div");
    modalContent.setAttribute("class", "modal-content");

    // Create the modal header
    var modalHeader = document.createElement("div");
    modalHeader.setAttribute("class", "modal-header");
    modalHeader.innerHTML = "<h2>" + (type === "success" ? "Thank You" : "Error") + "</h2>";

    // Create the modal body
    var modalBody = document.createElement("div");
    modalBody.setAttribute("class", "modal-body");
    modalBody.innerHTML = "<p class='" + type + "-message'>" + message + "</p>";

    // Create the modal footer
    var modalFooter = document.createElement("div");
    modalFooter.setAttribute("class", "modal-footer");

    // Create the close button
    var closeButton = document.createElement("button");
    closeButton.setAttribute("class", "close-button");
    closeButton.innerHTML = "Close";
    closeButton.onclick = function() {
        modal.remove();
    };

    // Append the elements to the modal content
    modalFooter.appendChild(closeButton);
    modalContent.appendChild(modalHeader);
    modalContent.appendChild(modalBody);
    modalContent.appendChild(modalFooter);

    // Append the modal content to the modal
    modal.appendChild(modalContent);

    // Append the modal to the document body
    document.body.appendChild(modal);
}
```

In this example, when the user uses the `customSubmitSuccessHandler` and `customSubmitErrorHandler` custom functions, the success and failure messages are displayed in a modal. The JavaScript function `showModal(type, message)` is used to dynamically create and display a modal dialog box on a screen.

Now, create a rule for successful form submission:

![Form submission success](/help/forms/assets/form-submission-success.png)

Refer to the illustration below to demonstrate that when the form is submitted successfully, the success message is displayed in a modal:

![Form submission success message](/help/forms/assets/form-submission-success-message.png )
 
Similarly, let us create a rule for failed form submissions:

![Form submission fail](/help/forms/assets/form-submission-fail.png)

Refer to the illustration below to demonstrate that when the form submission fails, the error message is displayed in a modal:

![Form submission fail message](/help/forms/assets/form-submission-fail-message.png )

To display form submission success and failure in a default manner, the `Default submit Form Success Handler` and `Default submit Form Error Handler` functions are available out of the box.

In case, the custom submission handler fails to perform as expected in existing AEM Projects or forms, refer to the [troubleshooting](#troubleshooting) section.

+++

+++ **Use Case**:  Perform actions in a specific instance of the repeatable panel 

Rules created using the visual rule editor on a repeatable panel apply to the last instance of the repeatable panel. To write a rule for a specific instance of the repeatable panel, we can use a custom function.

Let us create another form to collect information about travelers heading to a destination. A traveler panel is added as a repeatable panel, where the user can add details for 5 travelers using the `Add Traveler` button.

![Traveler Info](/help/forms/assets/traveler-info-form.png)

Add the following line of code as explained in the [create-custom-function](#create-custom-function) section, to perform actions in a specific instance of the repeatable panel, other than the last one:

```javascript

/**
* @name hidePanelInRepeatablePanel
* @param {scope} globals
*/
function hidePanelInRepeatablePanel(globals)
{    
    var repeatablePanel = globals.form.travelerinfo;
    // hides a panel inside second instance of repeatable panel
    globals.functions.setProperty(repeatablePanel[1].traveler, {visible : false});
}  

```
 
In this example, the `hidePanelInRepeatablePanel` custom function performs an action in a specific instance of the repeatable panel. In the above code, `travelerinfo` represents the repeatable panel. The `repeatablePanel[1].traveler, {visible: false}` code hides the panel in the second instance of the repeatable panel.

Let us add a button labeled `Hide` and add a rule to hide the second instance of a repeatable panel.

![Hide Panel rule](/help/forms/assets/custom-function-hidepanel-rule.png)

Refer to the video below to demonstrate that when the `Hide` is clicked, the panel in the second repeatable instance hides:

>[!VIDEO](https://video.tv.adobe.com/v/3429554?quality=12&learn=on)

+++

+++ **Usecase**: Pre-fill the field with a value when the form loads

Add the following line of code, as explained in the [create-custom-function](#create-custom-function) section, to load the pre-filled value in a field when the form is initialized:

```javascript
/**
 * Tests import data
 * @name testImportData
 * @param {scope} globals
 */
function testImportData(globals)
{
    globals.functions.importData(Object.fromEntries([['amount','10000']]));
} 
```

In the aforementioned code, the `testImportData` function prefills the `Booking Amount` textbox field when the form loads. Let us assume that the booking form requires the minimum booking amount to be `10,000`.

Let's create a rule at form initialization, where the value in the `Booking Amount` textbox field is prefilled with a specified value when the form loads:

![Import Data Rule](/help/forms/assets/custom-function-import-data.png)

Refer to the screenshot below, which demonstrates that when the form loads, the value in the `Booking Amount` textbox is pre-filled with a specified value:

![Import Data Rule Form](/help/forms/assets/custom-function-prefill-form.png)

+++

+++ **Usecase**: Set focus on the specific field

Add the following line of code, as explained in the [create-custom-function](#create-custom-function) section, to set focus on the specified field when the `Submit` button is clicked.:

```javascript
/**
 * @name testSetFocus
 * @param {object} emailField
 * @param {scope} globals
 */
    function testSetFocus(field, globals)
    {
        globals.functions.setFocus(field);
    }


```

Let us add a rule to the `Submit` button to set focus on the `Email ID` textbox field when it is clicked:

![Set Focus Rule](/help/forms/assets/custom-function-set-focus.png)

Refer to the screenshot below, which demonstrates that when the `Submit` button is clicked, the focus is set on the `Email ID` field:

![Set Focus Rule](/help/forms/assets/custom-function-set-focus-form.png)

>[!NOTE]
>
> You can use the optional `$focusOption` parameter, if you want to focus on the next or previous field relative to the `email` field.

+++

+++ **Usecase**: Add or delete repeatable panel using the `dispatchEvent` property

Add the following line of code, as explained in the [create-custom-function](#create-custom-function) section, to add a panel when the `Add Traveler` button is clicked using the `dispatchEvent` property:

```javascript
/**
 * Tests add instance with dispatchEvent
 * @name testAddInstance
 * @param {scope} globals
 */
function testAddInstance(globals)
{
    var repeatablePanel = globals.form.traveler;
    globals.functions.dispatchEvent(repeatablePanel,'addInstance');
}

```

Let us add a rule to the `Add Traveler` button to add the repeatable panel when it is clicked:

![Add Panel Rule](/help/forms/assets/custom-function-add-panel.png)

Refer to the gif below, which demonstrates that when the `Add Traveler` button is clicked, the panel is added using the `dispatchEvent` property:

![Add Panel](/help/forms/assets/custom-function-add-panel.gif)

Similarly, add the following line of code, as explained in the [create-custom-function](#create-custom-function) section, to delete a panel when the `Delete Traveler` button is clicked using the `dispatchEvent` property:

```javascript

/**
 
 * @name testRemoveInstance
 * @param {scope} globals
 */
function testRemoveInstance(globals)
{
    var repeatablePanel = globals.form.traveler;
    globals.functions.dispatchEvent(repeatablePanel, 'removeInstance');
} 
```

Let us add a rule to the `Delete Traveler` button to delete the repeatable panel when it is clicked:

![Delete Panel Rule](/help/forms/assets/custom-function-delete-panel.png)

Refer to the gif below, which demonstrates that when the `Delete Traveler` button is clicked, the traveler panel is deleted using the `dispatchEvent` property:

![Delete Panel](/help/forms/assets/custom-function-delete-panel.gif)


## Caching support for custom function

Adaptive Forms implement caching for custom functions to enhance response time while retrieving the custom function list in the rule editor. A message as `Fetched following custom functions list from cache` appears in the `error.log` file. 

![custom function with cache support](/help/forms/assets/custom-function-cache-error.png)

In case the custom functions are modified, the caching becomes invalidated, and it is parsed.  

## Troubleshooting {#troubleshooting}

* If the custom submission handler fails to perform as expected in existing AEM Projects or forms, perform the following steps:
  * Ensure that the [core components version is updated to 3.0.18 and later](https://github.com/adobe/aem-core-forms-components). However, for existing AEM Projects and forms, there are additional steps to follow:

  * For the AEM project, the user should replace all instances of `submitForm('custom:submitSuccess', 'custom:submitError')` with `submitForm()` and deploy the project through the Cloud Manager pipeline.

  * For existing forms, if the custom submission handlers are not functioning correctly, the user needs to open and save the `submitForm` rule on the **Submit** button using the Rule Editor. This action replaces the existing rule from `submitForm('custom:submitSuccess', 'custom:submitError')` with `submitForm()` in the form.


* If the JavaScript file containing code for custom functions has an error, the custom functions are not listed in the rule editor of an Adaptive Form. To check the custom function list, you can navigate to the `error.log` file for the error. In case of an error, the custom function list appears empty:

    ![error log file](/help/forms/assets/custom-function-list-error-file.png)

    In case of there is no error, the custom function are fetched and appear in the `error.log` file. A message as `Fetched following custom functions list` appears in the `error.log` file: 

    ![error log file with proper custom function](/help/forms/assets/custom-function-list-fetched-in-error.png)

## Considerations

* The `parameter type` and `return type` do not support `None`.

* The functions that are not supported in the custom function list are:
  * Generator functions
  * Async/Await functions 
  * Method definitions
  * Class methods
  * Default parameters
  * Rest parameters 

## See Also {#see-also}

{{see-also}}


