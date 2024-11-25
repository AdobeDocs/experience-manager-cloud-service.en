---
title: This article outlines various use cases for a custom function in an Adaptive Form based on core components.
description: The article outlines various use cases for a custom function in an Adaptive Form based on core components. Custom functions are used in the rule editor to create custom rules for the form.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
exl-id: df92b91e-f3b0-4a08-bd40-e99edc9a50a5
---
# Examples of developing and using custom function

The article provides the detailed examples of custom functions for an Adaptive Form based on core components, offering valuable insights into their effective implementation across various scenarios. Custom functions are used in the rule editor of an AEM Forms, enable developers to define and control the logic that governs form behavior. 
This article explores different implementations of custom functions, showcasing how they can be used to tailor forms to meet specific requirements and enhance overall functionality.

## Populate the dropdown list options using custom functions

The Rule Editor in Core Components does not support the **Set Options** property to populate dropdown list options dynamically at runtime. However, you can populate dropdown list options using custom functions, which allow you to retrieve options based on specific logic. Custom functions provide greater flexibility and control over how and when the dropdown options are populated, enhancing the user experience.

To populate the dropdown list options using a custom function, add the following code as described in the [create-custom-function ](/help/forms/custom-function-core-component-create-function.md) section:


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

## Show a panel using the `SetProperty` rule

Let's learn how custom functions use field and global objects with the help of a `Contact Us` form.

![Contact Us Form](/help/forms/assets/contact-us-form.png)

Add the following code in the custom function as explained in the [create-custom-function ](/help/forms/custom-function-core-component-create-function.md) section, to set the form field as `Required`.

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

## Validate the field

Let's learn how custom functions use field and global objects to validate the field with the help of a `Contact Us` form.

Add the following code in the custom function as explained in the [create-custom-function ](/help/forms/custom-function-core-component-create-function.md) section, to validate the field.

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

## Reset a panel

Let's learn how custom functions use field and global objects to reset the field with the help of a `Contact Us` form.

Add the following code in the custom function as explained in the [create-custom-function ](/help/forms/custom-function-core-component-create-function.md) section, to reset the panel.

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

## To display a custom message at the field level and marking the field as invalid

Let's learn how custom functions use field and global objects to display a custom message at the field level and marking the field as invalid with the help of a `Contact Us` form.

You can use the `markFieldAsInvalid()` function to define a field as invalid and set custom error message at a field level. The `fieldIdentifier` value can be `fieldId`, or `field qualifiedName`, or `field dataRef`. The value of the object named `option` can be `{useId: true}`, `{useQualifiedName: true}`, or `{useDataRef: true}`. 
The syntaxes used to mark a field as invalid and set a custom message are:

* `globals.functions.markFieldAsInvalid(field.$id,"[custom message]",{useId: true});`
* `globals.functions.markFieldAsInvalid(field.$qualifiedName, "[custom message]", {useQualifiedName: true});`
* `globals.functions.markFieldAsInvalid(field.$dataRef, "[custom message]", {useDataRef: true});`

Add the following code in the custom function as explained in the [create-custom-function ](/help/forms/custom-function-core-component-create-function.md) section, to enable a custom message at the field level.

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

## Submit altered data to the server

Let's learn how custom functions use field and global objects to submit manipulated data at the server with the help of a `Contact Us` form.

The following line of code: 
`globals.functions.submitForm(globals.functions.exportData(), false);` is used to submit the form data after manipulation. 
* The first argument is the data to be submitted. 
* The second argument represents whether the form is to be validated before submission. It is `optional` and set as `true` by default. 
* The third argument is the `contentType` of the submission, which is also optional with the default value as `multipart/form-data`. The other values can be `application/json` and `application/x-www-form-urlencoded`.
  
Add the following code in the custom function as explained in the [create-custom-function ](/help/forms/custom-function-core-component-create-function.md) section, to submit the manipulated data at the server:

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

## Override form submission success and error handlers 

Let's learn how custom functions use field and global objects to override submission handlers with the help of a `Contact Us` form.

Add the following line of code as explained in the [create-custom-functionas](/help/forms/custom-function-core-component-create-function.md) section, to customize the submission or failure message for form submissions and display the form submission messages in a modal box:

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

## Perform actions in a specific instance of the repeatable panel 

Rules created using the visual rule editor on a repeatable panel apply to the last instance of the repeatable panel. To write a rule for a specific instance of the repeatable panel, we can use a custom function.

Let us create another form as `Booking Form` to collect information about travelers heading to a destination. A traveler panel is added as a repeatable panel, where the user can add details for 5 travelers using the `Add Traveler` button.

![Traveler Info](/help/forms/assets/traveler-info-form.png)

Add the following line of code as explained in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section, to perform actions in a specific instance of the repeatable panel, other than the last one:

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

## Pre-fill the field with a value when the form loads

Let's learn how custom functions use field and global objects to prefill field with the help of a `Booking Form`.

Add the following line of code, as explained in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section, to load the pre-filled value in a field when the form is initialized:

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

## Set focus on the specific field

Let's learn how custom functions use field and global objects to set focus on specific field with the help of a `Booking Form`.

Add the following line of code, as explained in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section, to set focus on the specified field when the `Submit` button is clicked.:

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

## Add or delete repeatable panel using the `dispatchEvent` property

Let's learn how custom functions use field and global objects to add or delete repeatable panel using the `dispatchEvent` property with the help of a `Booking Form`.

Add the following line of code, as explained in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section, to add a panel when the `Add Traveler` button is clicked using the `dispatchEvent` property:

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


## Troubleshooting

* If the custom submission handler fails to perform as expected in existing AEM Projects or forms, perform the following steps:
  * Ensure that the [core components version is updated to 3.0.18 and later](https://github.com/adobe/aem-core-forms-components). However, for existing AEM Projects and forms, there are additional steps to follow:

  * For the AEM project, the user should replace all instances of `submitForm('custom:submitSuccess', 'custom:submitError')` with `submitForm()` and deploy the project through the Cloud Manager pipeline.

  * For existing forms, if the custom submission handlers are not functioning correctly, the user needs to open and save the `submitForm` rule on the **Submit** button using the Rule Editor. This action replaces the existing rule from `submitForm('custom:submitSuccess', 'custom:submitError')` with `submitForm()` in the form.

## See Also

{{see-also-rule-editor}}
