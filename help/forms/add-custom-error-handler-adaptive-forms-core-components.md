---
title: Add a custom error handler in Adaptive Forms based on Core Components for AEM Adaptive Forms
description: AEM Forms provides out-of-the-box success and error handlers for a form using the REST endpoint configured to invoke an external service. You can add a default error handler and custom error handler in an AEM Adaptive Form.
keywords: Add a custom error handler, add a default error handler, add a error handler in form, use rule editor's invoke service to add a custom error handler, configure rule editor to add a custom error handler , add custom error handler using rule editor
contentOwner: Ruchita Srivastav
content-type: reference
feature: Adaptive Forms, Core Components
exl-id: 4496c4cc-a5d7-4f34-91f9-13eded77b362
---
# Error Handlers for Adaptive Form based on Core Components {#error-handlers-in-adaptive-form}


| Version | Article link |
| -------- | ---------------------------- |
| AEM as a Cloud Service |   This article                |
| AEM 6.5     | [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-core-components/add-custom-error-handler-adaptive-forms-core-components.html)      |

AEM Forms provides out-of-the-box success and error handlers for form submissions. It also provides feature to customize error handler functions. For example, you can invoke a custom workflow in the backend for specific error codes or inform the customer that the service is down. Handlers are client-side functions that execute based on the server response. When an external service is invoked using APIs, the data is transmitted to the server for validation, which returns a response to the client with information about the success or error event for the submission. The information is passed as parameters to the relevant handler to execute the function. An error handler helps to manage and display errors or validation issues encountered. 

![error handler workflow to understand how to add custom error handler in forms](/help/forms/assets/error-handler-workflow.png)

The Adaptive Form validates the inputs that you provide in fields based on pre-set validation criteria and checks for various errors returned by the REST endpoint configured to invoke an external service. You can set the validation criteria based on the data source that you use with the Adaptive Form. For example, if you use RESTful web services as the data source, you can define the validation criteria in a Swagger definition file.

If the input values meet the validation criteria, the values are submitted to the data source else, the Adaptive Form displays an error message using an error handler. Similar to this approach, Adaptive Forms integrate with custom error handlers to perform data validations. If the input values do not meet the validation criteria, the error messages display at a field level in the Adaptive Form. This occurs when the validation error message returned by the server is in the standard message format.


## Uses of error handlers {#uses-of-error-handler}

Error handlers are used for various purposes. Some of the uses of error handler functions are listed below:

* **Perform validation**:  The error handling starts with validating user inputs against predefined rules or criteria. As users fill out an Adaptive Form, the error handler validates the input to ensure it meets the required format, length, or any other constraints.

* **Provide real-time feedback**: When any error is detected, the error handler displays immediate feedback to the user, such as inline error messages below the corresponding form fields. This feedback helps users to identify and correct errors without having to submit the form and wait for a response.


* **Display error messages**: When an Adaptive Form submission encounters any validation error, the error handler displays an appropriate error message. The error messages should be clear, concise, and highlight the specific fields that require attention. 

* **Highlights the erroneous field**: To draw the user's attention to the specific incorrect fields, the error handler highlights or visually differentiates the corresponding fields. It is performed by changing the background color, adding an icon or border, or any other visual cue that helps users quickly locate and address the errors.


## Failure/Error response format {#failure-response-format}

An Adaptive Form displays the errors at a field level if the server validation error messages are in the following standard format.
The below code illustrates the existing failure response structure: 

```javascript
   {
    errorCausedBy : "SERVER_SIDE_VALIDATION/SERVICE_INVOCATION_FAILURE"
    errors : [
        {
             errorMessage / errorMessages : <validationMsg> / [<validationMsg>, <validationMsg>]
        }
    ]
    originCode : <target error Code>
    originMessage : <unstructured error message returned by service>
    }
```


Where:

* `errorCausedBy` describes the reason for failure.
* `errors` mention the expression of the fields that failed the validation criteria along with the validation error message.
* `originCode` field added by AEM and contains the http status code returned by the external service.
* `originMessage` field added by AEM and contains the raw error data returned by the external service.

With the improvements in features and subsequent updates in the versions of AEM Forms, the existing failure response structure changed into new format based on RFC7807, which is backward compatible with the existing failure response structure:

```javascript
    {
        "type": "SERVER_SIDE_VALIDATION/FORM_SUBMISSION/SERVICE_INVOCATION/FAILURE/VALIDATION_ERROR", (required)
        "title": "Server side validation failed/Third party service invocation failed", (optional)
        "detail": "", (optional)
        "instance": "", (optional)
        "validationErrors" : [ (required)
            {
                "fieldName":"<qualified fieldname of the field whose data sent is invalid>",
                "dataRef":<JSONPath (or XPath) of the data element which is invalid>
                "details": ["Error Message(s) for the field"] (required)
    
            }
        ],
        "originCode": <Origin http status code>, (optional - in case of SERVER_SIDE_VALIDATION)
        "originMessage" : "<unstructured error message returned by service>" (optional - in case of SERVER_SIDE_VALIDATION)
    }
```


>[!NOTE]
>
> * Ensure that the error response structure includes either **fieldName** or **dataRef**.
> * Ensure that the **ContentType** header is **application/problem+json**.

Where:
* `type (required)` specifies the type of failure. It can be one of the following values:
    * `SERVER_SIDE_VALIDATION` indicates a failure due to server-side validation.
    * `FORM_SUBMISSION` indicates a failure during form submission
    * `SERVICE_INVOCATION` indicates a failure during a third-party service invocation.
    * `FAILURE` indicates a general failure.
    * `VALIDATION_ERROR` indicates a failure due to a validation error.

* `title (optional)` provides a title or brief description of the failure. 
* `detail (optional)` provides additional details about the failure if necessary. 
* `instance (optional)` represents an instance or identifier associated with the failure and helps in tracking or identifying the specific occurrence of the failure.
* `validationErrors (required)` contains information about validation errors. It includes the following fields:
    * `fieldname` mentions the qualified fieldname of the fields that failed the validation criteria.
    * `dataRef` represents the JSON path or XPath of the fields that failed the validation.
    * `details` contain the validation error message with the erroneous field. 
* `originCode (optional)` field added by AEM and contains the http status code returned by the external service
* `originMessage (optional)` field added by AEM and contains the raw error data returned by the external service.

### Sample error response format {#sample-error-response-format}

Some of the options to display the error responses are:

+++  Based on the Adaptive Form fieldName property


* **`Header:`** `content-type:application/problem+json`
* **`Response:`**

    ```javascript
            {
                "type": "VALIDATION_ERROR",
                "validationErrors": [
                {
                "fieldName": "$form.PetId",
                "dataRef": "",
                "details": [
                "Invalid ID supplied. Provided value is not correct!"
            ]
            }
            ]}
    ```

+++


+++ Based on the Adaptive Form Bind Reference property

* **`Header:`** `content-type:application/problem+json`
* **`Response:`**

    ```javascript
        {
            "type": "VALIDATION_ERROR",
            "validationErrors": [
            {
                "fieldName": "",
                "dataRef": "$.Pet.id",
                "details": [
                "Invalid ID supplied. Provided value is not correct!"
                ]
                }
        ]}
    ```

You can view the value of dataRef in the **[!UICONTROL Properties]** window of a form component.

+++

## Requirements to add error handler using Rule Editor's Invoke service {#before-you-start-to-add-error-handler}

Before you add an error handler using the Rule Editor's Invoke service:

* [Enable Adaptive Forms Core Components for your AEM Cloud Service environment](enable-adaptive-forms-core-components.md). 

* Learn how to [create custom functions](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/add-rules-and-use-expressions-in-an-adaptive-form/rule-editor.html?lang=en#write-rules).

 
## Add error handler using Rule Editor {#add-error-handler-using-rule-editor}

Using the [Rule Editor's Invoke Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/add-rules-and-use-expressions-in-an-adaptive-form/rule-editor.html#invoke) action, you define the validation criteria based on the data source that you use with the Adaptive Form. In case, you use RESTful web services as the data source, you can define the validation criteria in a Swagger definition file. By using the error handler functions and Rule Editor in Adaptive Forms, you can effectively manage and customize error handling. You define the conditions using Rule Editor and configure the desired actions to be performed when the rule is triggered. Adaptive Form validates the inputs that you enter in fields based on pre-set validation criteria. In case, the input values do not meet the validation criteria, the error messages are displayed at the field level in an Adaptive Form. 

>[!NOTE]
>
> * To use error handlers with the Rule Editor's Invoke service action, configure Adaptive Forms with a form data model (FDM). 
> * A default error handler is provided to display error messages on fields if the error response is in the standard schema. You can also call the default error handler from the custom error handler function. 

Using Rule Editor, you can:
* [Add default error handler function](#add-default-errror-handler)
* [Add custom error handler function](#add-custom-errror-handler)


### Add default error handler function {#add-default-errror-handler}

A default error handler is supported to display error messages on fields if the error response is in standard schema or in server-side validation failure. 
To understand how to use a default error handler using the [Rule Editor's Invoke Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/add-rules-and-use-expressions-in-an-adaptive-form/rule-editor.html?lang=en#invoke) action, take an example of a simple Adaptive Form with two fields, **Pet ID** and **Pet Name** and use a default error handler at the **Pet ID** field to check for various errors returned by the REST endpoint configured to invoke an external service, for example, `200 - OK`,`404 - Not Found`, `400 - Bad Request`. To add a default error handler using the Rule Editor's Invoke Service action, execute the following steps:

1. Open an Adaptive Form in authoring mode, select a form component and select **[!UICONTROL Rule Editor]** to open the rule editor.
1. Select **[!UICONTROL Create]**.
1. Create a condition in the **When** section of the rule. For example, **When[Name of Pet ID field]** is changed. Select is changed from the **Select State** drop-down list.
1. In the **Then** section, select **[!UICONTROL Invoke Service]** from the **Select Action** drop-down list.
1. Select a **Post service** and its corresponding data bindings from the **Input** section. For example, to validate **Pet ID**, select a **Post service** as **GET /pet/{petId}** and select **Pet ID** in the **Input** section.
1. Select the data bindings from the **Output** section. Select **Pet Name** in the **Output** section.
1. Select **[!UICONTROL Default Error Handler]** from the **Error Handler** section. 
1. Click **[!UICONTROL Done]**.

 ![add a default error handler for a field validation checks in a form](/help/forms/assets/default-error-handler.png)

As a result of this rule, the values you enter for **Pet ID** checks validation for **Pet Name** using external service invoked by REST endpoint. If the validation criteria based on the data source fail, the error messages are displayed at the field level.

 ![display the default error message when you add a default error handler in a form to handle error responses](/help/forms/assets/default-error-message.png)

### Add custom error handler function {#add-custom-errror-handler}

You can add a custom error handler function to perform some of the actions like:

* handle error responses that use non-standard or standard error responses. It is important to note that these non-standard error responses do not comply with the [standard schema of error responses](#failure-response-format).
* send analytics events to any analytics platforms. For example, Adobe Analytics.
* display modal dialog with error messages.

In addition to the mentioned actions, the custom error handlers can be used to execute customized functions that meet specific user requirements.

The custom error handler is a function (Client Library) designed to respond to errors returned by an external service and deliver a customized response to end users. Any Client Library with annotation `@errorHandler` is considered as a custom error handler function. This annotation helps to identify the error handler function specified in the `.js` file. 
To understand how to create and use a custom error handler using the [Rule Editor's Invoke service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/add-rules-and-use-expressions-in-an-adaptive-form/rule-editor.html?lang=en#invoke) action, let's take an example of Adaptive Form with two fields, **Pet ID** and **Pet Name** and use a custom error handler at the **Pet ID** field to check for various errors returned by the REST endpoint configured to invoke an external service, for example, `200 - OK`,`404 - Not Found`, `400 - Bad Request`.  

To add and use a custom error handler in an Adaptive Form, perform the following steps:
1. [Create a custom error handler](#create-custom-error-message) 
1. [Use the Rule Editor to configure custom error handler](#use-custom-error-handler)

#### 1. Create a custom error handler {#create-custom-error-message}

To create a custom error function, perform the following steps:

To create a custom error function, perform the following steps:

1. [Clone your AEM Forms as a Cloud Service Repository.](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#accessing-git). 
1. Create a folder under the `[AEM Forms as a Cloud Service repository folder]/apps/` folder. For example, create a folder named as `experience-league`
1. Navigate to `[AEM Forms as a Cloud Service repository folder]/apps/[AEM Project Folder]/experience-league/` and create a `ClientLibraryFolder` as `clientlibs`.
1. Create a folder named `js`.
1. Navigate to the `[AEM Forms as a Cloud Service repository folder]/apps/[AEM Project Folder]/clientlibs/js` folder.
1. Add a JavaScript file, for example, `function.js`. The file comprises the code for custom error handler.
Let's add the following code to the JavaScript file to display the response and headers, received from the REST service endpoint, in the browser console.

    ```javascript
        /** 
        Custom Error handler
        * @name customErrorHandler Custom Error Handler Function
        * @errorHandler
        */
        function customErrorHandler(response, headers, globals)
    {
        console.log("Custom Error Handler processing start...");
        console.log("response:"+JSON.stringify(response));
        console.log("headers:"+JSON.stringify(headers));
        alert("CustomErrorHandler - Enter valid PetId.")
        console.log("Custom Error Handler processing end...");
        return true; // true - call default error handler, false - don't call default error handler.
    }
    ```
    In the code above, `return true` invokes the default error handler automatically. To prevent the default error handler from being called by default, include `return false`.

    >[!NOTE]
    >
    > In the `.content.xml` file, add `categories = [custom-errorhandler-name]`. For example, in this case, [custom-errorhandler-name] is provided as `customfunctionsdemoV2`.


1. Save the `function.js` file.
1. Navigate to the `[AEM Forms as a Cloud Service repository folder]/apps/[AEM Project Folder]/clientlibs/js` folder.
1. Add a text file as `js.txt`. The file contains:
  
    ```javascript
        #base=js
        functions.js
    ```

1. Save the `js.txt` file.    
The created folder structure looks like:

    ![Created Client Library Folder Structure](/help/forms/assets/customclientlibrary_folderstructure.png) 

    >[!NOTE]
    >
    > To learn more about how to create custom functions, click [custom functions in the Rule Editor](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/forms/adaptive-forms-authoring/authoring-adaptive-forms-foundation-components/add-rules-and-use-expressions-in-an-adaptive-form/rule-editor.html?lang=en#write-rules).


1. Add, commit, and push the changes in the repository using the below commands:
         
    ```javascript

        git add .
        git commit -a -m "Adding error handling files"
        git push
    ```

1. [Run the pipeline.](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/onboarding/journey/developers.html?lang=en#setup-pipeline)

Once the pipeline is executed successfully, the custom error handler becomes available in your Adaptive Form rule editor. Now, let's understand how to configure and use a custom error handler using the Rule Editor's Invoke service in AEM Forms.

#### 2. Use the Rule Editor to configure custom error handler {#use-custom-error-handler}

Before implementing the custom error handler in an Adaptive Form, ensure that the client library name in the **[!UICONTROL Client Library Category]** aligns with the name specified in the categories option of the `.content.xml` file.

 ![Adding the name of the client library in the Adaptive Form Container configuration](/help/forms/assets/client-library-category-name-core-component.png)

To use a custom error handler using the **[!UICONTROL Rule Editor's Invoke Service]** action:

1. Open an Adaptive Form in authoring mode, select a form component and select **[!UICONTROL Rule Editor]** to open the rule editor.
1. Select **[!UICONTROL Create]**.
1. Create a condition in the **When** section of the rule. For example, When **[Name of Pet ID field]** is changed, select **is changed** from the **Select State** drop-down list.
1. In the **Then** section, select **[!UICONTROL Invoke Service ]** from the **Select Action** drop-down list.
1. Select a **Post service** and its corresponding data bindings from the **Input** section. For example, to validate **Pet ID**, select a **Post service** as **GET /pet/{petId}** and select **Pet ID** in the **Input** section.
1. Select the data bindings from the **Output** section. For example, Select **Pet Name** in the **Output** section.
1. Select **[!UICONTROL Custom Error Handler]** from the **[!UICONTROL Error Handler]** section. 
1. Click **[!UICONTROL Done]**.

 ![add custom error handler in a form to handle error responses](/help/forms/assets/custom-error-handler.png)s


As a result of this rule, the values you enter for **Pet ID** checks validation for **Pet Name** using external service invoked by REST endpoint. If the validation criteria based on the data source fail, the error messages are displayed at the field level.

 ![add a custom error handler in a form to handle error responses](/help/forms/assets/custom-error-handler-message-core-component.png)

Open the browser console and check the response and header, received from the REST service endpoint, for the validation error message. 


The custom error handler function is responsible for executing additional actions such as displaying a modal dialog or sending an analytics event, based on the error response. A custom error handler function provides the flexibility to tailor error handling to the specific user requirements. 

<!-- 

## Configure Adaptive Form submission to add custom handlers {#configure-adaptive-form-submission}

If the server validation error message does not display in the standard format, you can enable asynchronous submission and add a custom error handler on Adaptive Form submission to convert the message into a standard format.

### Configure asynchronous Adaptive Form submission {#configure-asynchronous-adaptive-form-submission}

Before adding custom handler, you must configure the adaptive form for asynchronous submission. Execute the following steps:

1. In adaptive form authoring mode, select the Form Container object and select ![adaptive form properties](assets/configure_icon.png) to open its properties.
1. In the **[!UICONTROL Submission]** properties section, enable **[!UICONTROL Use asynchronous submission]**.
1. Select **[!UICONTROL Revalidate on server]** to validate the input field values on server before submission.
1. Select the Submit Action:

    * Select **[!UICONTROL Submit using Form Data Model]** and select the appropriate data model, if you are using RESTful web service based [form data model](work-with-form-data-model.md) as the data source.
    * Select **[!UICONTROL Submit to REST Service endpoint]** and specify the **[!UICONTROL Redirect URL/Path]**, if you are using RESTful web services as the data source.

    ![adaptive form submission properties](assets/af_submission_properties.png)

1. Select ![Save](assets/save_icon.png) to save the properties.

### Add custom error handler on Adaptive Form submission {#add-custom-error-handler-af-submission}

AEM Forms provides out-of-the-box success and error handlers for form submissions. Handlers are client-side functions that execute based on the server response. When an Adaptive Form is submitted, the data is transmitted to the server for validation, which returns a response to the client with information about the success or error event for the submission. The information is passed as parameters to the relevant handler to execute the function.

Execute the following steps to add custom error handler on Adaptive Form submission:

1. Open an Adaptive Form in authoring mode, select any form object, and select  to open the rule editor.
1. Select **[!UICONTROL Form]** in the Form Objects tree and select **[!UICONTROL Create]**.
1. Select **[!UICONTROL Error in Submission]** from the Event drop-down list.
1. Write a rule to convert custom error structure to the standard error structure and select **[!UICONTROL Done]** to save the rule.

The following is a sample code to convert a custom error structure to the standard error structure:

```javascript
var data = $event.data;
var som_map = {
    "id": "guide[0].guide1[0].guideRootPanel[0].Pet[0].id_1[0]",
    "name": "guide[0].guide1[0].guideRootPanel[0].Pet[0].name_2[0]",
    "status": "guide[0].guide1[0].guideRootPanel[0].Pet[0].status[0]"
};

var errorJson = {};
errorJson.errors = [];

if (data) {
    if (data.originMessage) {
        var errorData;
        try {
            errorData = JSON.parse(data.originMessage);
        } catch (err) {
            // not in json format
        }

        if (errorData) {
            Object.keys(errorData).forEach(function(key) {
                var som_key = som_map[key];
                if (som_key) {
                    var error = {};
                    error.somExpression = som_key;
                    error.errorMessage = errorData[key];
                    errorJson.errors.push(error);
                }
            });
        }
        window.guideBridge.handleServerValidationError(errorJson);
    } else {
        window.guideBridge.handleServerValidationError(data);
    }
}
```

The `var som_map` lists the SOM expression of the Adaptive Form fields that you want to transform into the standard format. You can view the SOM expression of any field in an adaptive form by tapping the field and selecting **[!UICONTROL View SOM Expression]**.

Using this custom error handler, the adaptive form converts the fields listed in `var som_map` to standard error message format. As a result, the validation error messages display at field-level in the adaptive form.

 -->

## Additional information {#additional-information}

* [Create a standalone Core Components based Adaptive Form](/help/forms/creating-adaptive-form-core-components.md)
* [Create style or themes for your forms](/help/forms/using-themes-in-core-components.md)
* [Create or add an Adaptive Form to AEM Sites page](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md)

## See Also {#see-also}

{{see-also}}

