---
title: How to use asynchronous function calls in Visual rule Editor?
description: Asynchronous function calls in Visual rule editor
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
---

# Using asynchronous functions in an Adaptive Form

The rule editor in Adaptive Forms supports asynchronous functions, allowing you to integrate and manage operations that require waiting for external processes or data retrieval without interrupting the user's interaction with the form.

## What factors determine the use of asynchronous or synchronous functions?

In web development, managing user interactions effectively is crucial for creating a smooth experience. Two common approaches to handling operations are synchronous and asynchronous functions. 

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

You can write the [custom functions](/help/forms/custom-function-core-component-create-function.md) for asynchronous operations and configure the asynchronous functions using the **[!UICONTROL Async Function Call]** rule type in the rule editor.

### Exploring the Async Function Call rule type through a use case

Consider a login form for a website where users enter the username and password to access the account along with an OTP. If the user enters a correct OTP, the login attempt is successful; however, if the OTP is incorrect, the login is unsuccessful. 

In a login form, when the user clicks the **Confirm** button, the `getOTP()` function is called asynchronously to verify the entered OTP. The `getOTP()` function is implemented as a [custom function](/help/forms/custom-function-core-component-create-function.md). Using the **[!UICONTROL Async Function Call]** rule type in the rule editor, you can configure the `getOTP()` function in the rule editor of an Adaptive Form. You can also implement the success and failure callback methods in the rule editor. 

The following figure illustrates the steps to use the **[!UICONTROL Async Function Call]** rule type to invoke asynchronous functions for Adaptive Forms:

![Workflow to add asynchronous functions](/help/forms/assets/workflow-to-add-async-func.png){width=50%, align=center}

### 1. Write a custom function for the asynchronous operation in the JS file

The `getOTP()` function is implemented as a custom function. The below code is added in the JS file of the custom function:

```JavaScript
/**
 * generates the otp
 * @param {object} username
 * @param {object} password
 * @return {PROMISE}
 */
function getOTP() {
     return new Promise((resolve, reject) => {
        // Perform some asynchronous operation here
        asyncOperation((error, result) => {
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
function asyncOperation(callback) {
    setTimeout(() => {
        const result = {
            key1: 'value1',
            key2: 'value2',
            key3: 'value3'
        };
        callback(null, result);
    }, 1000);
}
```

The `getOTP()` function handles the asynchronous `asyncOperation()` function in a `Promise`. It manages the asynchronous task to verify the entered OTP and provides a way to handle success and failure using the `resolve()` and `reject()` methods of the Promise.

>[!NOTE]
>
> * The rule editor of a form displays only functions with a return type of `Promise` when you select the **Async Function Call** rule type.
> * To learn how to create a custom function, refer to the article titled [Create a Custom Function for an Adaptive Form Based on Core Components](/help/forms/custom-function-core-component-create-function.md).

### 2. Configure the asynchronous function in the rule editor

Perform the following steps to configure asynchronous function in rule editor:

1. [Create a rule to use asynchronous function using the Async Function call rule type](#21-create-a-rule-to-use-asynchronous-function-using-the-async-function-call-rule-type)
2. [Implement the callback methods for the asynchronous function](#22-implement-the-callback-methods-for-asynchronous-function)

#### 2.1 Create a rule to use  asynchronous function using the Async Function call rule type

To create a rule to use asynchronous operation use the **[!UICONTROL Async Function Call]** rule type, perform the following steps:

1. Open an Adaptive Form in authoring mode, select a form component and select **[!UICONTROL Rule Editor]** to open the rule editor.
2. Select **[!UICONTROL Create]**.
3. Create a condition in the **When** section of the rule for a click of button. For example, **When[Confirm]** is clicked and **When[OTP]** is equal to the value say `111`. 
4. In the **Then** section, select **[!UICONTROL Async Function call]** from the **Select Action** drop-down list.
When you select **[!UICONTROL Async Function call]** and the functions with the `Promise` return type appears.
1. Select the asynchronous function from the list. For example, select the `getOTP()` function and its callback methods as `Add success callback` and `add failure callback` appears.

Now, you can proceed with the implementation of the callback methods: `Success` and `Failure` for the `getOTP` function.

#### 2.2 Implement the callback methods for the asynchronous function

Implement the success and failure callback methods for the asynchronous function using the visual rule editor.

**Create a rule for `Add Success callback` method**

Let's create a rule to display a success message if the OTP matches the value `111` as defined in the `asyncOperation` function.

1. Click **[!UICONTROL Add Statement]** to create the rule.
1. Create a condition in the **When** section of the rule. For example, **When[Get Event Payload]**.  

    >[!NOTE]
    >
    > The **[!UICONTROL Get Event Payload]** function retrieves data associated with a specific event to manage user interactions dynamically.

1. Select its corresponding bindings from the **Input** section. For example, to validate OTP, select **otp** in the **Input** section.
1. In the **Then** section, select **[!UICONTROL Show]** from the **Select Action** drop-down list. For example, show the text with the success message in case the entered OTP is equal to `111`. 
1. Click **[!UICONTROL Done]**.


Refer to the screenshot below, where the user enters the OTP as `111`, and the success message appears when the button is clicked.




**Create a rule for `Add Failure callback` method**

Let's create a rule to display a failure message if the OTP do not match the value `111` as defined in the `asyncOperation` function.

1. Click **[!UICONTROL Add Statement]** to create the rule.
1. Create a condition in the **When** section of the rule. For example, **When[Get Event Payload]**. 
1. Select its corresponding bindings from the **Input** section. For example, to validate OTP, select **key1** in the **Input** section.
1. In the **Then** section, select **[!UICONTROL Show]** from the **Select Action** drop-down list. For example, show the text with the failure message in case the entered OTP is not equal to `111`. 
1. Click **[!UICONTROL Done]**.


Refer to the screenshot below, where the user enters the OTP as `123`, and the failure message appears when the button is clicked.


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
