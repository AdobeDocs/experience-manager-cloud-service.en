---
title: Create and add custom functions in an Adaptive Form
description: AEM Forms support custom functions which allow users to create and use their own functions within the rule editor.
keywords: Add a custom function, use a custom function, create a custom function, use custom function in rule editor.
contentOwner: Ruchita Srivastav
content-type: reference
feature: Adaptive Forms, Core Components
exl-id: 24607dd1-2d65-480b-a831-9071e20c473d
---
# Custom functions in Adaptive Forms (Core Components)

## Introduction

AEM Forms support custom functions, allowing users to define JavaScript functions for implementing complex business rules. These custom functions extend the capabilities of forms by facilitating manipulation and processing of entered data to meet specified requirements. They also enable dynamic alteration of form behavior based on predefined criteria. 
In Adaptive Forms, you can use custom functions within the [rule editor of an Adaptive Form](/help/forms/rule-editor-core-components.md) to create specific validation rules for form fields.

Let us understand use of custom function where users enter the email address, and you want to ensure that the entered email address follows a specific format (it contains an "@" symbol and a domain name). Create a custom function as "ValidateEmail" which takes the email address as input and returns true if it is valid and false otherwise.

```javascript
function ValidateEmail(inputText)
{
    var email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if(inputText.value.match(email))
        {
            alert("Valid email address!");
            return true;
        }
    else
    {
        alert("Invalid email address!");
        return false;
    }
}

```

In the above example, when the user tries to submit the form, the custom function "ValidateEmail" is invoked to check if the email address entered is valid. 

### Uses of custom functions {#uses-of-custom-function}

Advantages of using custom functions in Adaptive Forms are:

* **Manipulation of data**: Custom functions manipulate and process data entered into the forms fields.
* **Validation of data**: Custom functions enable you to perform custom checks on form inputs and provide specified error messages.
* **Dynamic behavior**: Custom functions allow you to control the dynamic behavior of your forms based on specific conditions. For example, you can show/hide fields, modify field values, or adjust form logic dynamically.
* **Integration**: You can use custom functions to integrate with external APIs or services. It helps in fetching data from external sources, sending data to external Rest endpoints, or performing custom actions based on external events.

## Supported JS annotations

Ensure that the custom function you write is accompanied by the `jsdoc` above it.

Supported `jsdoc` tags:

* **Private**
  Syntax: `@private`
  A private function is not included as a custom function.

* **Name**
  Syntax: `@name funcName <Function Name>`
  Alternatively `,` you can use: `@function funcName <Function Name>` **or** `@func` `funcName <Function Name>`.
  `funcName` is the name of the function (no spaces allowed).
  `<Function Name>` is the display name of the function.

* **Parameter**
  Syntax: `@param {type} name <Parameter Description>`
  Alternatively, you can use: `@argument` `{type} name <Parameter Description>` **or** `@arg` `{type}` `name <Parameter Description>`.
  Shows parameters used by the function. A function can have multiple parameter tags, one tag for each parameter in the order of occurrence.
  `{type}` represents parameter type. Allowed parameter types are:

    1. string
    2. number
    3. boolean
    4. scope
    5. string[]
    6. number[]
    7. boolean[]
    8. date
    9. date[]
    10. array
    11. object

   `scope` refers to a special globals object which is provided by forms runtime. It must be the last parameter and is not be visible to the user in the rule editor. You can use scope to access readable form and field proxy object to read properties, event which triggered the rule and a set of functions to manipulate the form.

   `object` type is used to pass readable field object in parameter to a custom function instead of passing the value.

   All parameter types are categorized under one of the above. None is not supported. Ensure that you select one of the types above. Types are not case-sensitive. Spaces are not allowed in the parameter name.  Parameter description can have multiple words.

* **Optional Parameter**
Syntax: `@param {type=} name <Parameter Description>` 
Alternatively, you can use: `@param {type} [name] <Parameter Description>`
By default all parameters are mandatory. You can mark a parameter optional by adding `=` in type of the parameter or by putting param name in square brackets.
For example, let us declare `Input1` as optional parameter:
    * `@param {type=} Input1`
    * `@param {type} [Input1]`
   
* **Return Type**
  Syntax: `@return {type}`
  Alternatively, you can use `@returns {type}`.
  Adds information about the function, such as its objective.
  {type} represents the return type of the function. Allowed return types are:

    1. string
    2. number
    3. boolean
    4. string[]
    5. number[]
    6. boolean[]
    7. date
    8. date[]
    9. array
    10. object

All other return types are categorized under one of the above. None is not supported. Ensure that you select one of the types above. Return types are not case-sensitive.

## Considerations while creating custom functions {#considerations}

To list the custom functions in the rule editor, you can declare them in any one of the following formats:

* **Function statement with or without jsdoc comments**

You can create a custom function with or without jsdoc comments. 

```javascript
    function functionName(parameters) 
        {
            // code to be executed
        }
```
<!--

* **Arrow function with mandatory jsdoc comment**

Some of the examples to create Arrow functions are:
```javascript
    /**
    * test function
    * @name testFunction test function
    * @param {string} a some parameter description
    * @param {string} b another parameter description
    * @return {string}
    */
    testFunction = (a, b) => {
    return a + b;
    };
```

    * @param {string=} b another parameter description
      /** */
    testFunction1=(a) => (return a)
    /** */
    testFunction2 = a => a + 100;-->

* **Function expression with mandatory jsdoc comment**

To list custom functions in the rule editor of an Adaptive Form, create custom functions in the following format:

```javascript
    /**
    * test function
    * @name testFunction test function
    * @param {string} input1 parameter description
    * @param {string} input2 another parameter description
    * @return {string}
    */
    testFunction = function(input1,input2)
        {
            // code to be executed
        }
```

<!--
* @param {string=} input2 another parameter description
The functions that are not supported in the custom function list are:
* Generator functions
* Async/Await functions 
* Method definitions
* Class methods
* Default parameters
* Rest parameters -->

>[!NOTE]
>
> You can check the `error.log` file for any errors, such as custom functions not getting listed in the rule editor.

<!--The `error.log` file also displays the methods and parameters that are not supported for custom functions. -->


## Create a custom function {#create-custom-function}

Create a client library to call custom functions in the rule editor. For more information, see [Using Client-Side Libraries](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/developing/full-stack/clientlibs.html#developing).

Steps to create custom functions are:
1. [Create a client library](#create-client-library)
1. [Add client library in an Adaptive Form](#use-custom-function)

### Create a client library {#create-client-library}

You can add custom functions by adding client library. To create a client library, perform the following steps:

1. [Clone your AEM Forms as a Cloud Service Repository](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#accessing-git).
1. Create a folder under the `[AEM Forms as a Cloud Service repository folder]/apps/` folder. For example, create a folder named as `experience-league`.
1. Navigate to `[AEM Forms as a Cloud Service repository folder]/apps/[AEM Project Folder]/experience-league/` and create a `ClientLibraryFolder`. For example, create a client library folder as `customclientlibs`.
1. Add a property `categories` with string type value. For example, assign the value `customfunctionscategory` to the `categories` property for the `customclientlibs` folder.

   >[!NOTE]
   >
   > You can choose any name for `client library folder` and `categories` property.

1. Create a folder named `js`.
1. Navigate to the `[AEM Forms as a Cloud Service repository folder]/apps/[AEM Project Folder]/customclientlibs/js` folder.
1. Add a JavaScript file, for example, `function.js`. The file comprises the code for custom function.

    >[!NOTE]
    >
    > If the JavaScript file containing code for custom functions has an error, then the custom functions are not listed in the rule editor of an Adaptive Form. You can also check the `error.log` file for the error.
    
    <!-- 
    >* AEM Adaptive Form supports the caching of custom functions. If the JavaScript is modified, the caching becomes invalidated, and it is parsed. You can see a message as `Fetched following custom functions list from cache` in the `error.log` file.  -->

1. Save the `function.js` file.
1. Navigate to the `[AEM Forms as a Cloud Service repository folder]/apps/[AEM Project Folder]/customclientlibs/js` folder.
1. Add a text file as `js.txt`. The file contains:
  
    ```javascript
        #base=js
        functions.js
    ```

1. Save the `js.txt` file. 
1. Add, commit, and push the changes in the repository using the below commands:
         
    ```javascript

        git add .
        git commit -a -m "Adding custom functions"
        git push
    ```

1. [Run the pipeline.](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline)

Once the pipeline is executed successfully, the custom function added in client library becomes available in your [Adaptive Form rule editor](/help/forms/rule-editor-core-components.md). 

### Add client library in an Adaptive Form{#use-custom-function}

Once you have deployed your client library to your Forms CS environment, use its capabilities in your Adaptive Form. To add the client library in your Adaptive Form

1. Open your form in edit mode. To open a form in edit mode, select a form and select **[!UICONTROL Edit]**.
1. Open the Content browser, and select the **[!UICONTROL Guide Container]** component of your Adaptive Form. 
1. Click the Guide Container properties ![Guide properties](/help/forms/assets/configure-icon.svg) icon. The Adaptive Form Container dialog box opens.  
1. Open the **[!UICONTROL Basic]** tab and select the name of the **[!UICONTROL client library category]** from the drop-down list (in this case, select `customfunctionscategory`).

   ![Adding the custom function client library](/help/forms/assets/clientlib-custom-function.png)

1. Click **[!UICONTROL Done]** .

Now, you can create a rule to use custom functions in the rule editor. 

<!--

Create a rule to use custom function in the rule editor. 

### Support for the optional parameters in custom functions{#support-for-optional-parameter}

AEM supports including optional parameters in JSDocs. These parameters are displayed as optional in the rule editor. There are two ways to add optional parameters in JSDocs:
*  `@param {string=abc} b -- some description for b which is optional`

    In the above line of code, `b` is an optional parameter with the default value set to `abc`. 
    Alternatively, you can define `b` as an optional parameter without assigning any default value as `@param {string=} b -- some description for b which is optional`

* `@param {array} [z=[def,xyz]] - - some description for z which is optional`

    In the above line of code, `z` is an optional parameter of array type with the default value set to `[def , xyz]`. 
    Alternatively, you can define `z` as an optional parameter without assigning any default value as `@param {array} [z=] - - some description for z which is optional`

>[!NOTE]
>
> Ensure that the parameter name is enclosed in square brackets [] and the parameter type is enclosed in curly brackets {}. 

To learn more about how to define optional parameters in JSDocs, [click here](https://jsdoc.app/tags-param).

In the rule editor of an Adaptive Form, the parameters are displayed as `required`. By default the parameters are `required`, if not defined as optional in JSDocs.

  ![Optional or required parameters](/help/forms/assets/optional-default-params.png) 

  You can save the rule without specifying a value for required parameters, but the rule is not executed and displays a warning message as:

  ![incomplete rule warning message](/help/forms/assets/incomplete-rule.png) 
  
  The rule is executed even if you do not specify a value for optional parameters. Undefined values are passed for optional parameters on executing the rule.

  ### Support for field and globals objects in custom functions {#support-field-and-global-objects}

  needs to be discussed

  -->

## See Also {#see-also}

{{see-also}}
