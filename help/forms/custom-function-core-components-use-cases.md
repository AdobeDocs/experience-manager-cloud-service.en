---
title: This article outlines various use cases for a custom function in an Adaptive Form based on core components.
description: The article outlines various use cases for a custom function in an Adaptive Form based on core components. Custom functions are used in the rule editor to create custom rules for the form.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: df92b91e-f3b0-4a08-bd40-e99edc9a50a5
---
# Examples of developing and using custom function

This article provides detailed examples of **custom functions** for an Adaptive Form based on core components, offering practical insights into their effective implementation across common form-building scenarios such as validation, calculation, and dynamic field behavior. **Custom functions** are used in the **rule editor** of an Adobe Experience Manager (AEM) Forms environment, enabling developers to define and control the logic that governs form behavior.

## What Custom Functions Do

Custom functions extend the capabilities of the AEM Forms **rule editor** by allowing developers to encapsulate reusable business logic that would otherwise be difficult to express through out-of-the-box rules alone. Because the rule editor exposes these functions directly to form authors, teams can standardize complex logic once and apply it consistently across multiple forms. This reduces duplication, improves maintainability, and ensures that specialized behavior—such as custom validation or data transformation—remains centralized and easy to update.

This article explores different implementations of custom functions, demonstrating how they can be used to tailor Adaptive Forms to meet specific business requirements and improve overall form functionality.

## Common Use Cases for Custom Functions

Custom functions are typically applied to solve targeted form logic challenges. Key use cases include:

- **Custom validation** — enforce business-specific rules that go beyond standard field constraints, ensuring submitted data meets required conditions.
- **Calculations and data transformation** — compute derived values, format inputs, or aggregate data across multiple fields.
- **Dynamic field behavior** — show, hide, enable, or populate fields based on conditional logic driven by user input.
- **Reusable logic across forms** — define a function once in the rule editor and reuse it consistently across many Adaptive Forms.
- **Integration with external data** — process or map values retrieved from services and data sources into the form model.

By centralizing this logic in custom functions, developers create Adaptive Forms that are more adaptable, easier to maintain, and better aligned with specific organizational requirements.

## Populate the dropdown list options using custom functions

The Rule Editor in Core Components does not support the **Set Options** property to populate dropdown list options dynamically at runtime. However, you can populate dropdown list options using **custom functions**, which retrieve options based on specific business logic at runtime. Custom functions provide greater flexibility and control over how and when the dropdown options are populated, enhancing the user experience.

### Add the custom function code

To populate the dropdown list options using a custom function, complete the following steps:

1. Add the following code as described in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section:

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

    ![Drop-down list options](/help/forms/assets/drop-down-list-options.png)

    In the above code, `setEnums` sets the `enum` property and `setEnumNames` sets the `enumNames` property of the dropdown. The `enum` property defines the underlying stored values (`"0"` through `"6"`), while the `enumNames` property defines the corresponding display labels shown to the user (`"Sunday"` through `"Saturday"`). Because the two arrays are positionally paired, each index in `setEnums` maps directly to the label at the same index in `setEnumNames` — for example, the stored value `"0"` displays as **Sunday**. This separation of stored values from display labels ensures the form captures machine-readable data while presenting human-readable options.

2. To populate the dropdown list, create a rule for the `Next` button that sets the dropdown list options when the user clicks the `Next` button. The rule binds the `enum` and `enumNames` properties of the dropdown to the values returned by the `setEnums` and `setEnumNames` custom functions, so the options are generated at the moment the button is clicked rather than being hard-coded at design time.

    **Create a rule to invoke the custom function**

    ![Drop down options in rule Editor](/help/forms/assets/drop-down-option-rule-editor.png)

    Refer to the illustration below, which demonstrates where the options of the dropdown list are set upon clicking the button. Once the rule is applied, the dropdown is populated with the seven day-of-week options at runtime, confirming that the custom function has successfully supplied both the stored values and their display labels.

## Show a panel using the `SetProperty` rule

Custom functions use field and global objects to control form behavior, as demonstrated below with a `Contact Us` form.

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
> * Modifications made to the form using the **`setProperty`** method of the Globals object are asynchronous in nature and are not reflected during the execution of the custom function.

### How the panel visibility logic works

In this example, clicking the button triggers validation of the **`personaldetails`** panel. When the panel contains no errors, the **`feedback`** panel becomes visible. This ensures the **`feedback`** panel appears only when the **`personaldetails`** panel is error-free.

### Create a rule for the `Next` button

![Set Property](/help/forms/assets/custom-function-set-property.png)

Create a rule for the **`Next`** button that validates the **`personaldetails`** panel and reveals the **`feedback`** panel. The rule performs the following actions when the user clicks the **`Next`** button:

1. Validates every field within the **`personaldetails`** panel.
2. If all fields pass validation, sets the **`feedback`** panel to visible.

   ![Set Property Form Preview](/help/forms/assets/set-property-form-preview.png)

3. If any field fails validation, keeps the **`feedback`** panel hidden.

### Expected behavior

![Set Property Form Preview](/help/forms/assets/set-property-panel.png)

Refer to the illustration below. It demonstrates where the **`personaldetails`** panel is validated upon clicking the **`Next`** button. When all fields within the **`personaldetails`** panel are validated successfully, the **`feedback`** panel becomes visible.

When errors are present in the fields of the **`personaldetails`** panel, those errors are displayed at the field level upon clicking the **`Next`** button. As a result, the **`feedback`** panel remains invisible until the user corrects the errors and the panel validates without issues.

## Validate the field

Custom functions validate a field by operating on two runtime objects: the **field object**, which represents the specific form field being checked, and the **globals object**, which exposes built-in form functions such as `validate()`. This section demonstrates how these objects work together to validate a field, using a **`Contact Us`** form as the example.

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

The `globals.functions.validate(field)` call invokes the platform's built-in validation on the passed **`field`** object. This evaluates the field against its configured constraints and, when the input fails those constraints, triggers the associated error message at the field level.

>[!NOTE]
>
> If no argument is passed in the `validate()` function, it validates the form.

![Email Address Validation Pattern](/help/forms/assets/custom-function-validation-pattern.png)

In this example, a custom validation pattern is applied to the **`contact`** field. The field enforces a strict phone-number format:

- The phone number **must start with `10`**.
- The digits following `10` **must be exactly `8` digits** — no more and no less.

![Validation Pattern](/help/forms/assets/custom-function-validate.png)

Because these rules are enforced together, any input that violates either condition fails validation. If the user enters a phone number that does not start with **`10`**, or that contains more or fewer than **`8`** digits, the field fails validation and displays a validation error message the moment the button is clicked.

The next step is to create a rule for the **`Next`** button that validates the **`contact`** field on the button click. This rule ties the validation logic to the user action, ensuring the field is checked before the form advances.

![Email Address Validation Pattern](/help/forms/assets/custom-function-validate-error-message.png)

Refer to the illustration below, which demonstrates the field-level behavior: when the user enters a phone number that does not start with **`10`**, validation fails and an error message appears directly at the field level.

![Email Address Validation Pattern](/help/forms/assets/validate-form-preview-form.png)

When the user enters a valid phone number and all fields in the **`personaldetails`** panel pass validation, the **`feedback`** panel appears on the screen. This confirms that successful validation of every required field in the panel is the condition that unlocks the next stage of the form.

## Reset a panel

Custom functions reset a panel by using the **field** and **global** objects, as demonstrated here with a `Contact Us` form. The **field** object represents the specific form component being acted upon, while the **global** object (`globals`) provides access to the form's built-in functions, including the reset operation.

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

The `globals.functions.reset(field)` call clears the values of the specified `field`, restoring the targeted panel to its initial, empty state. Passing the `field` argument tells the reset function exactly which component to clear, which is why the panel — rather than the entire form — is reset.

>[!NOTE]
>
> If no argument is passed in the `reset()` function, it validates the form. In other words, the behavior depends on the argument: **passing a specific field resets that field**, while **omitting the argument triggers form validation instead**.

![Clear button](/help/forms/assets/custom-function-reset-field.png)

In this example, the **`personaldetails` panel** resets upon clicking the **`Clear` button**. This occurs because the `resetField` function receives the `personaldetails` panel as its `field` argument and passes it to `globals.functions.reset()`.

### Create a rule for the Clear button

![Reset Form](/help/forms/assets/custom-function-reset-form.png)

The next step is to create a rule for the `Clear` button that resets the panel on the button click. This rule binds the button-click event to the `resetField` custom function, ensuring the reset action executes each time the user selects the `Clear` button.

See the illustration below to display that when the user clicks the `Clear` button, the `personaldetails` panel resets:

## To display a custom message at the field level and marking the field as invalid

Custom functions use the field and global objects to display a custom message at the field level and mark the field as invalid, as demonstrated here with a `Contact Us` form. The **field object** represents the individual form field being validated, while the **global object** (`globals`) exposes built-in helper functions such as validation utilities.

The **`markFieldAsInvalid()`** function defines a field as invalid and sets a custom error message at the field level. It accepts a field identifier, a custom message, and an option object that specifies how the field is identified.

**Field identifier (`fieldIdentifier`)** — pass one of the following values:

* `fieldId`
* `field qualifiedName`
* `field dataRef`

**Option object (`option`)** — pass the matching option that corresponds to the chosen identifier:

* `{useId: true}`
* `{useQualifiedName: true}`
* `{useDataRef: true}`

### Syntax to mark a field as invalid

Use one of the following syntaxes to mark a field as invalid and set a custom message:

* `globals.functions.markFieldAsInvalid(field.$id,"[custom message]",{useId: true});`
* `globals.functions.markFieldAsInvalid(field.$qualifiedName, "[custom message]", {useQualifiedName: true});`
* `globals.functions.markFieldAsInvalid(field.$dataRef, "[custom message]", {useDataRef: true});`

### Custom function code

Add the following code in the custom function as explained in the [create-custom-function ](/help/forms/custom-function-core-component-create-function.md) section to enable a custom message at the field level:

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

![Mark field as Invalid](/help/forms/assets/custom-function-invalid-field.png)

In this example, if the user enters fewer than **15 characters** in the comments textbox, a custom message appears at the field level. This enforces a minimum input length, because the function trims the entered value and compares its length against the `minLength` threshold of **15**, marking the field invalid whenever the requirement is not met.

### Field validation behavior

The next step is to create a rule for the `comments` field that invokes the `customMessage` custom function, binding it to the field so the validation runs when the user provides input.

![Mark field as Invalid Preview form](/help/forms/assets/custom-function-invalidfield-form.png)

As demonstrated, entering short or negative feedback of fewer than 15 characters in the `comments` field triggers the display of the custom message at the field level, flagging the entry as invalid.

![Mark field as valid Preview form](/help/forms/assets/custom-function-validfield-form.png)

When the user enters **15 or more characters** in the comments textbox, the field passes validation and the form is submitted successfully.

## Submit altered data to the server

Custom functions submit manipulated form data to the server by combining field and global objects, as demonstrated here with a `Contact Us` form. The core method is `globals.functions.submitForm()`, which submits form data after any manipulation is applied.

The following line of code submits the form data after manipulation:

`globals.functions.submitForm(globals.functions.exportData(), false);`

### Understanding the submitForm arguments

The `submitForm` method accepts three arguments that control what is submitted and how:

* **First argument (data):** The data to be submitted to the server. In this example, it is supplied by `globals.functions.exportData()`, which returns the current form data.
* **Second argument (validation):** Determines whether the form is validated before submission. This argument is **optional** and set to **`true`** by default. Passing `false` submits the data without triggering form validation.
* **Third argument (contentType):** Specifies the `contentType` of the submission. This argument is also **optional**, with the default value **`multipart/form-data`**. The other accepted values are **`application/json`** and **`application/x-www-form-urlencoded`**, allowing the submission format to match the server endpoint's expectations.

### Example: Submitting a default value for empty fields

Add the following code in the custom function, as explained in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section, to submit the manipulated data to the server:

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

![Submit data](/help/forms/assets/custom-function-submit-data.png)

In this example, if the user leaves the `comments` textbox empty, the value `NA` is submitted to the server at form submission. This substitution ensures the server always receives a defined value for the `comments` field, preserving data integrity and preventing empty or undefined entries in the submitted payload.

### Binding the function to the Submit button

Next, create a rule for the `Submit` button that invokes the `submitData` custom function. This rule connects the button's submit action to the function, so that whenever the user selects `Submit`, the manipulated data — including the default `NA` value for empty comments — is sent to the server.

![Submit data at the console window](/help/forms/assets/custom-function-submit-data-form.png)

To confirm the behavior, refer to the illustration of the `console window`. When the user leaves the `comments` textbox empty, the console output shows the updated data object with the value `NA` substituted for the `comments` field before submission, demonstrating that the default value is applied at the server.

![Inspect data at the console window](/help/forms/assets/custom-function-submit-data-console-data.png)

You can also inspect the console window to view the exact data submitted to the server. The logged output, produced by the `console.log('After update:{}', data)` statement, reflects the final data object after manipulation, allowing you to verify that the expected values — including any default substitutions — are present before the data reaches the server.

## Override form submission success and error handlers

Custom functions use field and global objects to override the default submission handlers in Adobe Experience Manager (AEM) Forms. This example uses a `Contact Us` form to demonstrate how to customize the success message, the failure message, and how to display those form submission messages in a **modal dialog box**.

Add the following line of code, as explained in the [create-custom-functionas](/help/forms/custom-function-core-component-create-function.md) section, to customize the submission or failure message for form submissions and display the form submission messages in a modal dialog box:

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

### How the custom handlers work

In this example, the `customSubmitSuccessHandler` and `customSubmitErrorHandler` custom functions display the success and failure messages in a modal dialog box. The `customSubmitSuccessHandler` reads the submission response from `globals.event.payload.body`, then either redirects the user to a `redirectUrl` or shows a `thankYouMessage` in a modal. The `customSubmitErrorHandler` receives the custom error message and passes it directly to the modal.

The JavaScript function `showModal(type, message)` dynamically creates and displays a modal dialog box on the screen. It first removes any existing modal to prevent duplicates, then constructs the modal header, body, footer, and a **Close** button before appending the completed dialog to the document body. This ensures that only one modal is shown at a time and that both success and error responses reuse the same rendering logic.

### Create submission rules

After adding the custom functions, create rules that invoke them at the appropriate points in the form submission flow:

1. **Create a rule for successful form submission.** Configure the rule to call `customSubmitSuccessHandler` so that, when the form is submitted successfully, the success message is displayed in a modal dialog box. Refer to the accompanying illustration for the expected result.

   ![Form submission success](/help/forms/assets/form-submission-success.png)

   ![Form submission success message](/help/forms/assets/form-submission-success-message.png )

2. **Create a rule for failed form submissions.** Configure the rule to call `customSubmitErrorHandler` so that, when the form submission fails, the error message is displayed in a modal dialog box. Refer to the accompanying illustration for the expected result.

   ![Form submission fail](/help/forms/assets/form-submission-fail.png)

   ![Form submission fail message](/help/forms/assets/form-submission-fail-message.png )

### Default submission handlers

To display form submission success and failure in a default manner, the **`Default submit Form Success Handler`** and **`Default submit Form Error Handler`** functions are available out of the box. These built-in handlers provide standard behavior without requiring any custom code, so you only need the custom handlers above when you want tailored messaging or a modal experience.

If the custom submission handler fails to perform as expected in existing Adobe Experience Manager (AEM) projects or forms, refer to the [troubleshooting](#troubleshooting) section.

## Perform actions in a specific instance of the repeatable panel

**Rules created using the visual rule editor on a repeatable panel apply only to the last instance of the repeatable panel.** Because the visual rule editor targets only the **last instance**, a **custom function** is required to perform actions on any other specific instance of a repeatable panel.

Consider a `Booking Form` created to collect information about travelers heading to a destination. A traveler panel is added as a repeatable panel, allowing the user to add details for up to **5 travelers** using the `Add Traveler` button.

### Add the custom function

![Traveler Info](/help/forms/assets/traveler-info-form.png)

Add the following code, as explained in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section, to perform actions in a specific instance of the repeatable panel other than the last one:

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

### How the custom function works

The `hidePanelInRepeatablePanel` custom function performs an action in a specific instance of the repeatable panel. The code operates as follows:

- **`travelerinfo`** represents the repeatable panel and is assigned to the `repeatablePanel` variable.
- **`repeatablePanel[1]`** references the **second instance** of the repeatable panel. Instances follow **zero-based** array indexing, so index `0` is the first instance, index `1` is the second, and so on. This is why `[1]` targets the second traveler, not the first.
- **`{visible : false}`** applied through `setProperty` hides the `traveler` panel. As a result, the panel inside the second instance of the repeatable panel is hidden when the function runs.

### Trigger the rule with a button

![Hide Panel rule](/help/forms/assets/custom-function-hidepanel-rule.png)

Add a button labeled `Hide` and attach a rule that calls the custom function to hide the second instance of the repeatable panel.

Refer to the video below, which demonstrates that clicking the `Hide` button hides the panel in the second repeatable instance:

>[!VIDEO](https://video.tv.adobe.com/v/3429554?quality=12&learn=on)

## Pre-fill the field with a value when the form loads

Custom functions use field and global objects to prefill a field, as demonstrated here with a **Booking Form**. When the **Booking Form** loads, the **Booking Amount** textbox is automatically populated with a specified value — in this example, the form requires a minimum booking amount of **10,000**, so the field is pre-filled with `10,000` at initialization.

### How the custom function prefills the field

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

In this code, the `testImportData` function prefills the **Booking Amount** textbox field when the form loads. The function achieves this through the `globals.functions.importData()` method:

1. `Object.fromEntries([['amount','10000']])` constructs a data object that maps the `amount` field to the value `10000`.
2. This object is passed to `importData()`, which imports the supplied data into the form.
3. As a result, the **Booking Amount** field is populated with **10,000** the moment the form is initialized, before any user interaction takes place.

![Import Data Rule](/help/forms/assets/custom-function-import-data.png)

Because the function runs at form initialization, the value is present as soon as the form renders, ensuring the minimum booking amount requirement is satisfied by default.

### Create a rule at form initialization

![Import Data Rule Form](/help/forms/assets/custom-function-prefill-form.png)

The **Booking Form** requires a minimum booking amount of **10,000**. To enforce this, create a rule at form initialization so that the value in the **Booking Amount** textbox is prefilled with the specified value when the form loads. Binding the `testImportData` custom function to the form's initialization event triggers the prefill automatically, without requiring the user to enter the value manually.

Refer to the screenshot below, which demonstrates that when the form loads, the value in the **Booking Amount** textbox is pre-filled with the specified value of **10,000**. This confirms that the custom function executed successfully at initialization and that the field reflects the intended default booking amount as soon as the form is displayed.

## Set focus on the specific field

Custom functions use the **field** and **global** objects to set focus on a specific field. The following example demonstrates this behavior using a **Booking Form**.

The **`setFocus`** function programmatically moves the input cursor to a designated form field, directing the user's attention to that field and streamlining data entry. This is particularly useful for guiding users through required fields or highlighting the next field they need to complete.

### Step 1: Define the custom function

Add the following line of code, as explained in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section, to set focus on the specified field when the **`Submit`** button is clicked:

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

In this function, **`globals.functions.setFocus(field)`** invokes the built-in focus method, passing the target **`field`** object so the cursor moves to that field at runtime. The **`globals`** object provides access to the form-level functions, while the **`field`** parameter identifies which field receives focus.

### Step 2: Attach the rule to the Submit button

![Set Focus Rule](/help/forms/assets/custom-function-set-focus.png)

Add a rule to the **`Submit`** button so that focus is set on the **`Email ID`** textbox field when the button is clicked. To do this:

1. Select the **`Submit`** button in the form.
2. Add a rule that triggers the **`testSetFocus`** custom function when the button is clicked.
3. Pass the **`Email ID`** field as the target field so that focus is applied to it.

### Step 3: Verify the focus behavior

![Set Focus Rule](/help/forms/assets/custom-function-set-focus-form.png)

Refer to the screenshot below, which demonstrates the result: when the **`Submit`** button is clicked, the focus moves directly to the **`Email ID`** field, placing the cursor there and readying it for input.

>[!NOTE]
>
> You can use the optional **`$focusOption`** parameter if you want to focus on the next or previous field relative to the **`email`** field. This gives you finer control over navigation between adjacent fields.

## Add or delete repeatable panel using the `dispatchEvent` property

The **`dispatchEvent`** property lets custom functions add or delete a **repeatable panel** by firing the **`addInstance`** and **`removeInstance`** events on a panel object. Learn how custom functions use field and global objects to control repeatable panels through the **`dispatchEvent`** property, demonstrated with a `Booking Form`.

A **repeatable panel** is a form section that can be duplicated at runtime, allowing a single layout—such as a traveler's details—to be repeated as many times as needed. The **`dispatchEvent`** function programmatically triggers panel-level events, so calling it with **`addInstance`** creates a new copy of the panel, and calling it with **`removeInstance`** removes one.

### Add a repeatable panel with `addInstance`

Add the following line of code, as explained in the [create-custom-function](/help/forms/custom-function-core-component-create-function.md) section, to add a panel when the `Add Traveler` button is clicked using the **`dispatchEvent`** property. The **`addInstance`** event instructs the form to repeat the `traveler` panel, producing a fresh instance each time it is dispatched:

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

![Add Panel Rule](/help/forms/assets/custom-function-add-panel.png)

Add a rule to the `Add Traveler` button to add the repeatable panel when the button is clicked.

![Add Panel](/help/forms/assets/custom-function-add-panel.gif)

Refer to the gif below. Because the rule invokes **`dispatchEvent`** with **`addInstance`**, clicking the `Add Traveler` button adds a new traveler panel to the form:

### Delete a repeatable panel with `removeInstance`

Similarly, add the following line of code, as explained in the [create-custom-function](#create-custom-function) section, to delete a panel when the `Delete Traveler` button is clicked using the **`dispatchEvent`** property. The **`removeInstance`** event instructs the form to remove one instance of the repeated `traveler` panel:

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

![Delete Panel Rule](/help/forms/assets/custom-function-delete-panel.png)

Add a rule to the `Delete Traveler` button to delete the repeatable panel when the button is clicked.

![Delete Panel](/help/forms/assets/custom-function-delete-panel.gif)

Refer to the gif below. Because the rule invokes **`dispatchEvent`** with **`removeInstance`**, clicking the `Delete Traveler` button deletes the traveler panel from the form:

## Known Issue

**Custom functions do not support JavaScript regular expression literals.** Any regular expression written using **literal syntax** (delimited by forward slashes, such as `/^abc$/`) is unsupported inside custom functions. As a result, using a **regex literal** in a custom function directly causes errors during execution. To create regular expressions reliably, use the **RegExp constructor** instead.

### Affected Code Pattern

The following literal syntax is **not supported** and triggers an execution error:

```
const pattern = /^abc$/;
```

Because custom functions do not recognize regular expression literals, this line fails at runtime rather than compiling and executing successfully.

### Recommended Workaround

To ensure compatibility, replace every regular expression literal with an equivalent expression built through the **RegExp constructor**. The `RegExp` constructor accepts the pattern as a string argument and produces the same regular expression object that the literal would otherwise create.

1. **Identify** each regular expression written in literal form (for example, `/^abc$/`).
2. **Convert** the literal into the constructor form by passing the pattern as a string:

   ```
   const pattern = new RegExp("^abc$");
   ```

3. **Apply** any flags—such as case-insensitivity—as a second string argument to the constructor when needed.

### Why This Matters

Refactoring regular expressions to use the **RegExp constructor** ensures consistent and reliable execution within custom functions. In JavaScript, the literal syntax and the `RegExp` constructor are two equivalent ways to define the same pattern; however, only the constructor form is supported here. Standardizing on the constructor form prevents the runtime errors caused by unsupported literal syntax and produces predictable, portable behavior across custom functions.

## Troubleshooting

If the custom submission handler fails to perform as expected in existing Adobe Experience Manager (AEM) Projects or forms, the resolution begins with a version update followed by project- and form-specific corrective steps.

**First, update the AEM core components to [version 3.0.18 or later](https://github.com/adobe/aem-core-forms-components).** This version alignment is required because the custom submission handler behavior changed in the newer core components, and existing projects and forms built against earlier versions retain the outdated `submitForm('custom:submitSuccess', 'custom:submitError')` signature that no longer resolves correctly. Updating the core components is necessary but not sufficient — existing AEM Projects and forms require the additional steps below.

### Resolution for AEM Projects

For an existing AEM project, the developer must migrate the deprecated submission call:

1. Locate all instances of **`submitForm('custom:submitSuccess', 'custom:submitError')`** in the project source.
2. Replace each instance with the simplified **`submitForm()`** call, which is the supported signature in **core components 3.0.18 and later**.
3. Deploy the updated project through the **Cloud Manager pipeline** so the corrected code is built and promoted to the target environment. Deployment through the pipeline ensures the change is compiled and propagated consistently rather than applied ad hoc, which is why a full pipeline deployment—not a manual patch—resolves the handler failure.

### Resolution for Existing Forms

For existing forms where the custom submission handlers are not functioning correctly, the change is applied through the Rule Editor rather than through code:

1. Open the form and navigate to the **Submit** button.
2. Open the **`submitForm`** rule associated with the Submit button in the **Rule Editor**.
3. Save the rule without further modification.

Re-saving the rule regenerates it against the updated core components, which **replaces the outdated `submitForm('custom:submitSuccess', 'custom:submitError')` rule with `submitForm()`** in the form. As a result, the form is realigned with the current submission handler behavior, and the custom handlers resume functioning correctly. This works because the Rule Editor rewrites the rule definition on save, so simply opening and saving is enough to migrate the form without manually editing the underlying rule.

## See Also

{{see-also-rule-editor}}
