---
title: Using custom functions in an Adaptive Form
description: AEM Forms support custom functions, which allow users to create and use their own functions within the rule editor.
keywords: Add a custom function, use a custom function, create a custom function, use custom function in rule editor.
contentOwner: Ruchita Srivastav
content-type: reference
feature: Adaptive Forms, Core Components
exl-id: 24607dd1-2d65-480b-a831-9071e20c473d
role: User, Developer
---

# Introduction to Custom Functions for Adaptive Forms based on Core Components

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/en/docs/experience-manager-65/content/forms/adaptive-forms-core-components/create-and-use-custom-functions)                  |
| AEM as a Cloud Service     | This article         |

AEM Forms supports custom functions, allowing users to define JavaScript functions for implementing complex business rules. These custom functions extend the capabilities of forms by facilitating manipulation and processing of entered data to meet specified requirements. They enable dynamic alteration of form behavior based on predefined criteria. Custom functions also enable developers to enforce complex validation logic, perform dynamic calculations, and control the display or behavior of form elements based on user interactions or predefined criteria.

>[!NOTE]
>
> Ensure that the [core component](https://github.com/adobe/aem-core-forms-components) is set to the latest version to use the latest features.

## Uses of custom functions {#uses-of-custom-function}

Advantages of using custom functions in Adaptive Forms are:
* **Processing of data**: Custom functions help process data entered into the forms fields.
* **Validation of data**: Custom functions enable you to perform custom checks on form inputs and provide specified error messages.
* **Dynamic behavior**: Custom functions allow you to control the dynamic behavior of your forms based on specific conditions. For example, you can show/hide fields, modify field values, or adjust form logic dynamically.
* **Integration**: You can use custom functions to integrate with external APIs or services. It helps in fetching data from external sources, sending data to external Rest endpoints, or performing custom actions based on external events.

Custom functions are essentially client libraries that are added in the JavaScript file. Once you create a custom function, it becomes available in the rule editor for selection by the user in an Adaptive Form. The custom functions are identified by the JavaScript annotations in the rule editor. 

## Supported JavaScript annotations for custom function {#js-annotations}

JavaScript annotations are used to provide metadata for JavaScript code. It includes comments that start with specific symbols, for example, /** and @. The annotations provide important information about functions, variables, and other elements in the code. Adaptive Form supports the following JavaScript annotations for custom functions:

### Name

  The name is used to identify the custom function in the rule editor of an Adaptive Form. The following syntaxes are used to name a custom function:

  * `@name [functionName] <Function Name>`
  * `@function [functionName] <Function Name>`
  * `@func [functionName] <Function Name>`.
  `functionName` is the name of the function. Spaces are not allowed.
  `<Function Name>` is the display name of the function in the rule editor of an Adaptive Form.
    If the function name is identical to the name of the function itself, you can omit `[functionName]` from the syntax. 

### Parameter

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
      * scope: Represents the globals object, which contains read-only variables such as form instances, target field instances, and methods for performing form modifications within custom functions. It is declared as the last parameter in JavaScript annotations and is not visible in the rule editor of an Adaptive Form. The scope parameter accesses the object of the form or component to trigger the rule or event required for form processing. For further information on the Globals object and how to use it, [click here](/help/forms/custom-function-core-component-scope-function.md).
    
The parameter type is not case-sensitive and spaces are not allowed in the parameter name.
 
`<Parameter Description>` contains details about the purpose of the parameter. It can have multiple words.

#### Optional Parameters

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
    Ensure that the parameter type is enclosed in curly brackets {} and the parameter name is enclosed in square brackets. 

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
    
### Return Type

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

### Private

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

## Next Step

To create and use a custom function in your Adaptive Form, refer to the [Create a Custom Function for an Adaptive Form Based on Core Components](/help/forms/custom-function-core-component-create-function.md) article.

## See Also

{{see-also-rule-editor}}