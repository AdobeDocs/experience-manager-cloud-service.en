---
title: How to use asynchronous function calls in Visual rule Editor?
description: Asynchronous function calls in Visual rule editor
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
exl-id: a240ba26-a6d8-4643-8acb-1d8812dac61f
---
# Using asynchronous functions in an Adaptive Form based on Core Components

The [rule editor in Adaptive Forms](/help/forms/rule-editor-core-components.md) supports asynchronous functions, allowing you to integrate and manage operations that require waiting for external processes or data retrieval without interrupting the user's interaction with the form.

## What factors determine the use of asynchronous or synchronous functions?

Managing the user interaction effectively is crucial for creating a smooth experience. Two common approaches for handling operations are synchronous and asynchronous functions. 

**Synchronous functions** execute tasks one after another, causing the application to wait for each operation to complete before proceeding. This can lead to delays and a less engaging user experience, especially when tasks involve waiting for external resources, like file uploads or data fetching.

For example, consider a scenario where a user uploads an image, the entire form halts, waiting for the upload to complete. This pause leaves the user unable to interact with other fields, causing frustration and delays. As they wait for the image to process, any information entered may be lost if they navigate away or lose patience, making the experience cumbersome and inefficient.

**Asynchronous functions**, on the other hand, allow tasks to run concurrently. This means users can continue interacting with the application while background processes are executed. Asynchronous operations enhance responsiveness, making it possible for users to receive immediate feedback and maintain engagement without interruptions.

Conversely, with an asynchronous approach, users can upload images in the background while continuing to fill out the rest of the form seamlessly. The interface remains responsive, allowing for real-time updates and immediate feedback as the upload progresses. It enhances user engagement, ensuring a smooth experience without interruptions.

![Asynchronous and synchronous functions](/help/forms/assets/sync-async.png){align=center}

## Implementing asynchronous functions for Adaptive Forms

You can implement the asynchronous functions for Adaptive Forms using the following rule types in the rule editor:

* [Async Function call](#using-asynchronous-function-calls-in-the-visual-rule-editor)
* [Function output](#how-to-use-function-output-rule-type)

## How to use the Async Function Call rule type?

<span class="preview"> This is a pre-release feature and accessible through our [pre-release channel](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features). </span>

You can write the [custom functions](/help/forms/custom-function-core-component-create-function.md) for asynchronous operations and configure the asynchronous functions using the **[!UICONTROL Async Function Call]** rule type in the rule editor.

### Exploring the Async Function Call rule type through a use case

Consider a registration form on a website where users enter a one-time password (OTP). The panel for adding user details appears only after entering the correct OTP. If the OTP is incorrect, the panel stays hidden and an error message appears on screen.

![Login-form](/help/forms/assets/rule-editor-login-form.png) {width-50%}

In a registration form, when the user clicks the **Confirm** button, the `matchOTP()` function is called asynchronously to verify the entered OTP. The `matchOTP()` function is implemented as a [custom function](/help/forms/custom-function-core-component-create-function.md). Using the **[!UICONTROL Async Function Call]** rule type in the rule editor, you can configure the `matchOTP()` function in the rule editor of an Adaptive Form. You can also implement the success and failure callbacks in the rule editor. 

The following figure illustrates the steps to use the **[!UICONTROL Async Function Call]** rule type to invoke asynchronous functions for Adaptive Forms:

![Workflow to add asynchronous functions](/help/forms/assets/workflow-to-add-async-func.png){width=50%, align=center}

### 1. Write a custom function for the asynchronous operation in the JS file

>[!NOTE]
>
> * The rule editor of a form displays only functions with a return type of `Promise` when you select the **Async Function Call** rule type.
> * To learn how to create a custom function, refer to the article titled [Create a Custom Function for an Adaptive Form Based on Core Components](/help/forms/custom-function-core-component-create-function.md).

The `matchOTP()` function is implemented as a custom function. The below code is added in the JS file of the custom function:

```JavaScript
/**
 * generates the otp for success use case
 * @param {string} otp
 * @return {PROMISE}
 */
function matchOTP(otp) {
     return new Promise((resolve, reject) => {
        // Perform some asynchronous operation here
         asyncOperationForOTPMatch(otp, (error, result) => {
            if (error) {
                // On failure, call reject(error)
                reject(error);
            } else {
                // On success, call resolve(result)
                resolve(result);
            }
        });
    });
}

/**
 * generates the otp
 */
function asyncOperationForOTPMatch(otp, callback) {
    setTimeout(() => {
        if(otp === '111') {
            callback( null, {'valid':'true'});    
        } else {
            callback( {'valid':'false'}, null);
        }
    }, 1000);
}
```

The code defines a function `matchOTP()` that generates a promise to validate a one-time password (OTP) asynchronously. It uses a function `asyncOperationForOTPMatch()` to simulate the OTP matching process. The function checks if the provided OTP is equal to `111`. If the entered OTP is correct, it calls the callback with null for the error and an object indicating the OTP is valid `({'valid':'true'})`.If the OTP is not valid, it calls the callback with an error object `({'valid':'false'})` and null for the result.

### 2. Configure the asynchronous function in the rule editor

Perform the following steps to configure asynchronous function in rule editor:

1. [Create a rule to use asynchronous function using the Async Function call rule type](#21-create-a-rule-to-use-asynchronous-function-using-the-async-function-call-rule-type)
1. [Implement the callbacks for the asynchronous function](#22-implement-the-callbacks-for-asynchronous-function)

#### 2.1 Create a rule to use  asynchronous function using the Async Function call rule type

To create a rule to use asynchronous operation use the **[!UICONTROL Async Function Call]** rule type, perform the following steps:

1. Open an Adaptive Form in authoring mode, select a form component and select **[!UICONTROL Rule Editor]** to open the rule editor.
1. Select **[!UICONTROL Create]**.
1. Create a condition in the **When** section of the rule for a click of button. For example, **When[Confirm]** is clicked. 
1. In the **Then** section, select **[!UICONTROL Async Function call]** from the **Select Action** drop-down list.
When you select **[!UICONTROL Async Function call]** and the functions with the `Promise` return type appears.
1. Select the asynchronous function from the list. For example, select the `matchOTP()` function and its callbacks as `Add success callback` and `add failure callback` appears.
1. Now, select the **[!UICONTROL Input]** bindings. For example, select **[!UICONTROL Input]** as `Form Object` and compare it to the `OTP` field.

The below screenshot displays the rule:

![rule type](/help/forms/assets/asyn-function-rule-type.png)

Now, you can proceed with the implementation of the callbacks: `Success` and `Failure` for the `matchOTP` function.

#### 2.2 Implement the callbacks for the asynchronous function

Implement the success and failure callback methods for the asynchronous function using the visual rule editor.

**Create a rule for `Add Success callback` method**

Let's create a rule to display the `userdetails` panel, if the OTP matches the value `111`.

1. Click **[!UICONTROL Add success callback]**.
1. Click **[!UICONTROL Add Statement]** to create the rule.
1. Create a condition in the **When** section of the rule.
1. Select the **[!UICONTROL Function Output]** > **[!UICONTROL Get Event Payload]**.

    >[!NOTE]
    >
    > The **[!UICONTROL Get Event Payload]** function retrieves data associated with a specific event to manage user interactions dynamically.

1. Select its corresponding bindings from the **Input** section. For example, select **[!UICONTROL String]** and enter `valid`. Compare the entered string to `true`. 
1. In the **Then** section, select **[!UICONTROL Show]** from the **Select Action** drop-down list. For example, show the `userdetails` panel.
1. Click **[!UICONTROL Add Statement]**.
1. Select **[!UICONTROL Hide]** from the **Select Action** drop-down list. For example, hide the `error message` textbox.
1. Click **[!UICONTROL Done]**.

![Success call](/help/forms/assets/rule-editor-success-callback.png){width=50%, height=50%}

Refer to the screenshot below, where the user enters the OTP as `111`, and the `User Details` panel appears when the `Confirm` button is clicked.

![Success](/help/forms/assets/success.gif)

**Create a rule for `Add Failure callback` method**

Let's create a rule to display a failure message if the OTP do not match the value `111`.

1. Click **[!UICONTROL Add failure callback]**.

1. Click **[!UICONTROL Add Statement]** to create the rule.
1. Create a condition in the **When** section of the rule. 
1. Select the **[!UICONTROL Function Output]** > **[!UICONTROL Get Event Payload]**.
1. Select its corresponding bindings from the **Input** section. For example, select **[!UICONTROL String]** and enter `valid`. Compare the entered string to `false`.
1. In the **Then** section, select **[!UICONTROL Show]** from the **Select Action** drop-down list. For example, show the `error message` textbox.
1. Click **[!UICONTROL Add Statement]**.
1. Select **[!UICONTROL Hide]** from the **Select Action** drop-down list. For example, hide the `userdetails` panel.
1. Click **[!UICONTROL Done]**.

![Failure callback method](/help/forms/assets/rule-editor-failure-callback.png){width=50%, height=50%}

Refer to the screenshot below, where the user enters the OTP as `123`, and the error message appears when the `Confirm` button is clicked.

![Failure](/help/forms/assets/failure.gif)

The screenshot below displays the complete rule for using **[!UICONTROL Async Function Call]** to implement an asynchronous function:

![Rule for async function call](/help/forms/assets/rule-editor-async-callbacks.png)

You can also edit the callbacks by clicking **[!UICONTROL Edit success callback]** and **[!UICONTROL Edit failure callback]**.

## How to use Function Output rule type?

You can also call the asynchronous functions indirectly using the synchronous functions. The synchronous functions are executed using the **[!UICONTROL Function Output]** rule type in the rule editor of an Adaptive Form. 

Look at the code below to see how to invoke asynchronous functions using the **[!UICONTROL Function Output]** rule type:

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

To see its working, let's add a button and create a rule for the button that invokes the asynchronous function upon a button click.

 ![creating rule for async function](/help/forms/assets/rule-for-async-funct.png){width=50%}

Refer to the screenshot of the console window below to demonstrate that when the user clicks the `Fetch` button, the custom function `callAsyncFunction` is invoked, which in turn calls an asynchronous function `asyncFunction`. Inspect the console window to view the response to the button click:

 ![Console window](/help/forms/assets/async-custom-funct-console.png)

## See Also

{{see-also-rule-editor}}
