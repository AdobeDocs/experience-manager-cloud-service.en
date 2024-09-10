---
title: Use rules to add dynamic behavior to a form
description: Edge Delivery Services for AEM Forms are built for peak performance, empowering you to envision the future of streamlined data collection and user engagement. Use rules to add dynamic behavior to your forms. 
feature: Edge Delivery Services
exl-id: 58042016-e655-446f-a2bf-83f1811525e3
role: Admin, Architect, Developer
---
# Use rules to add dynamic behavior to your forms

One of the powerful features of creating forms using a spreadsheet is the ability to use built-in spreadsheet functions to create rules, allowing you to conditionally display or hide form fields, automate calculations based on user input, and create a more dynamic user experience.

This article guides you through how to use various Adaptive Form Block properties mainly [`Visible`](#visible-property), [`Visibility Expression`](#visible-expression-property) and [`Value Expression`](#value-expression-property) properties along with [spreadsheet functions](#spreadsheet-functions-for-rules) to create effective rules for your forms. We'll also explore some examples to illustrate how these rules can be implemented in practice.

## Understanding the constructs of a rule

Rules are like instructions that tell us what to do in different situations. A rule generally has the following constructs:

* Conditions : These specify the circumstances under which the rule applies. Think of them as a question that needs to be answered (yes or no).

* Actions: These define what happens when the condition is met (true) or not met (false).


For example, to display an email box, when a checkbox is selected: 

* Condition: The "Do you like to subscribe for Magazine & Activities?" checkbox is selected. (Yes or no?). This condition is set in the `Visible` property of the form. 
* Action (True): The email box is displayed. (What happens if yes). The `Visibility Expression`  use the condition defined for the `visible` property to dynamically show fields. 
* Action (False): The email box is hidden. (What happens if no). The `Visibility Expression`  use the condition defined for the `Value` to dynamically hide fields. 

For detailed step-by-step instructions, see the [show/hide email field based on a condition](#example-1-conditional-email-field)


## Understanding the Value, Visible, Visibility Expression, and Value Expression Properties 

### Visible Property

Imagine a light switch for your form field. The `Visible` property is like that switch, controlling whether the field is initially visible on the form when it first loads.

* True (like the light switch being "on"): The field is shown on the form.
* False (like the light switch being "off"): The field is hidden on the form.

You can use SpreadSheet Formula (including the = tag) to write a formula using spreadsheet-like logic to determine the field's visibility. You can use the values from other fields in your form within this formula. For example, if a user selects "Individual" in a registration type field, you can hide the email field using a formula that checks that value.

### Visible Expression Property (Show/Hide a field)

The `Visible Expression` property allows you to use the rule added to `Visible` property to decide whether to show or hide the field based on user interactions.

Use the `=FORMULATEXT("Address of the corresponding Visible property)` to bring the formula mentioned in the `Visible` Property as a string to the `Visible Expression` property field. This is required to dynamically show/hide fields in a published form. 

![Forumaltext](/help/edge/assets/aem-forms-formulatext.png)

### Value Property (Set the Initial Data)

Imagine a pre-set value on a dimmer switch for a room's light. The `Value` property is similar, determining the initial state of the data a user sees in the field.  It sets or retrieves the current data displayed within the form field. 

When the form loads for the first time, the `Value` property dictates what the user sees in the field before they make any changes. Unlike `Visible` and `Visible Expression` properties that control visibility, the Value property directly affects the data itself. Users can modify this value by typing, selecting options (dropdown menus), or interacting with the field.

You can use Excel Formula (including the = tag) to write a formula using spreadsheet-like logic to determine the value shown in the field. You can use the values from other fields in your form within this formula. For example, you can calculate a discount automatically based on the order amount entered in another field.


### Value Expression Property (Calculate Values to be displayed in a field)

This property allows you to control the value displayed within a field based on a formula, similar to the Visible Expression. Imagine a calculator built into the field.

Use the `=FORMULATEXT("Address of the corresponding Value property)` to bring the formula mentioned in the `Value` Property as a string to the `Value Expression` property field. This is required to dynamically calculate and show calculated values in a published form.

![Forumaltext](/help/edge/assets/aem-forms-formulatext-value.png)

Here's an analogy to solidify these concepts:

* Visible: Imagine a form like a house. The "Visible" property is like the light switch for each room (field). You decide if the room is initially lit (visible) or dark (hidden) when someone enters the house (opens the form).
* Visible Expression: This is like a motion sensor light switch. The room (field) might be initially dark (hidden), but a formula (motion sensor) can turn it on (show the field) if someone walks by (changes the value in another field).
* Value: This is like a pre-set dimmer switch for the light (initial data in the field). Users can then adjust the brightness (modify the value).
* Value Expression: This is like a fancy calculator built into the price tag on a product in the house (form). The price tag (field) shows the final price based on a formula (for example, adding tax to the base price) that uses other information like the base price (value from another field).

By combining these properties with [spreadsheet functions](#spreadsheet-functions-for-rules), you can achieve a wide range of dynamic behaviors within your forms.

## Spreadsheet Functions for Rules

Adaptive Forms Block supports a variety of spreadsheet functions that can be used to create rules. Here are functions that are available out-of-the-box (OOTB):

### Logical Functions

* [NOT()](https://docs.oasis-open.org/office/v1.2/os/OpenDocument-v1.2-os-part2.html#__RefHeading__1018452_715980110): Reverses the logical state (TRUE becomes FALSE and vice versa).
* [AND()](https://docs.oasis-open.org/office/v1.2/os/OpenDocument-v1.2-os-part2.html#AND): Returns TRUE only if all conditions specified are TRUE.
* [OR()](https://docs.oasis-open.org/office/v1.2/os/OpenDocument-v1.2-os-part2.html#OR): Returns TRUE if at least one of the conditions specified is TRUE.

### Conditional Functions

* [IF()](https://docs.oasis-open.org/office/v1.2/os/OpenDocument-v1.2-os-part2.html#__RefHeading__1018446_715980110): Evaluates a condition and returns a specific value if TRUE, and another value if FALSE.

### Math Functions

* [SUM()](https://docs.oasis-open.org/office/v1.2/os/OpenDocument-v1.2-os-part2.html#SUM): Adds values from a specified range of cells.
* [ROUND()](https://docs.oasis-open.org/office/v1.2/os/OpenDocument-v1.2-os-part2.html#ROUND): Rounds a number to a specified number of decimal places.
* [MIN()](https://docs.oasis-open.org/office/v1.2/os/OpenDocument-v1.2-os-part2.html#MIN): Returns the smallest value from a specified range of cells.

## Creating a rule

Let's dive into some practical examples to illustrate how rules can be used to enhance your forms:

## Example 1: Conditional Email Field

This example shows how the checkbox acts as a condition. When it's selected (condition is true), the email box appears (action for true). If it's not selected (condition is false), the email box stays hidden (action for false).

Create a form with a checkbox and an email box, as displayed in the below image:

![Conditional Email Form](/help/edge/assets/aem-forms-conditional-email-form.png)


Here's how to use a rule to show the email field on the selection of a checkbox:

1. Set the `Value` property of the checkbox field to `TRUE`. 
1. Set the `Checked` property of the checkbox field to `FALSE`. This ensures that the checkbox is not selected, by default. 
1. Set the `Visible` property of the email field to `=[address of Checked property of the checkbox field] = true()`. For example `=Q11=TRUE()`. The formula evaluates, if the checkbox is selected or not. If the checkbox is selected, the formula evaluates to TRUE. If the checkbox is not selected, the formula evaluates to FALSE. 



    The `TRUE()` function, returns the logical value, when you set it to point to `Checked` property, if the `checked = false` it returns false. If `checked=true`, it returns `true`. This ensures that the email field is hidden, by default. 


1. Set the `Visible Expression` property of the checkbox field to `=FORMULATEXT ((address of Visible property of the checkbox field))`. For example, `=FORMULATEXT((G12))`. The FORMULATEXT() function takes a formula as input and returns the formula itself as a text string. It helps use the formula in the form. 

    ![Conditional Email Field](/help/edge/assets/aem-forms-visible-expression-formula-text.png)

1. Preview and publish your form. Now, on selecting the checkbox reveals the email field, while deselecting it hides the field, providing a dynamic user experience.

    ![Conditional Email](/help/edge/assets/aem-forms-coditional-email.gif)
 

## Example 2: Automatic Calculation

This example shows how a form automatically calculates Estimated Trip Cost on selecting trip dates in a form.

Create a form with a date field, room budget, Estimated Trip Cost fields as displayed below and an email box, as displayed in the below image:

![Conditional Email Form](/help/edge/assets/aem-forms-automatic-calculations-form.png)

Here's how to use a perform automatic calculation to show Estimated Trip Cost:

1. Set the `Value` property of the `amount` field to `=F6*DAYS(F3,F2)`. This formula calculates number of days from `Start Date`  and `End Date`, multiples number of days with room budget, and displays result in `Estimated Trip Cost` field. 

1. Set the `Value Expression` property of the `Estimated Trip Cost` field to `=FORMULATEXT ((address of value property of the amount field))`. For example, `=FORMULATEXT(F7)`. The FORMULATEXT() function takes a formula as input and returns the formula itself as a text string. It helps use the formula in the form. 

1. Preview and publish your form. Now, on specifying a `Start Date`, `End Date`, and Room Budget. The `Estimated Trip Cost` is auto calculated. 

## Spreadsheet functions examples


Here are some examples for the commonly used spreadsheet functions:

**Logical functions:**

* **NOT():** Reverses the logical state (TRUE becomes FALSE and vice versa).

    Example: Hiding a "Confirm Email" field if the email field is left blank.
    
    1. Set the `Visible` property of the "Confirm Email" field to `=NOT(if('address of email field'=""))`. 

        ![AEM Forms hide confirm email field](/help/edge/assets/aem-forms-not-function-hide-email-field.png)

    
    1. Set the visible expression of the "Confirm Email" field to `=FORMULATEXT ((address of visible property of the Confirm Email field))`

        ![AEM Forms visible expression formula](/help/edge/assets/aem-forms-visible-expression-formula-text.png)


* AND(): Returns TRUE only if all conditions specified are TRUE.

    * Example: Enabling a "submit" button only if all required fields are filled.

    1. Set the `Visible` property of the "submit" button to:

        

        ```JavaScript

        =AND(NOT(address of `value` property of the `name` field = ""), NOT(address of `value` property of the `email` field = ""), NOT(address of `value` property of the `phone` field))
       
        ```

        For example, 

        ```JavaScript

        =AND(NOT(F9=""), NOT(F12=""), NOT(F10=""))

        ```
    
    1. Set the visible expression of the "Confirm Email" field to 
    
        ```JavaScript
    
        =FORMULATEXT ((address of visible property of the Confirm Email field))

        ```

         For example, 

        ```JavaScript

        =FORMULATEXT(G14)

        ```

        This formula shows the "submit" button (TRUE) only if all fields (name, email, phone) are filled (NOT(()) returns TRUE for each), otherwise it hides the button (AND(multiple FALSES) = FALSE).

* OR(): Returns TRUE if at least one of the conditions specified is TRUE.

    * Example: Applying a discount if a user enters any of the applicable discount coupon code.

    1. Set the `Visible` property of the "final amount" field to:


     ```JavaScript

        =IF(OR(F14="BlackFridaySale", F14="NewYearDiscount"), (F6*DAYS(F3,F2)* 0.7) , (F6*DAYS(F3,F2)))

     ```

     1. Set the value expression of the "Confirm Email" field to 
    
        ```JavaScript
    
        =FORMULATEXT ((address of value property of the final amount field))

        ```

         For example, 

        ```JavaScript

        =FORMULATEXT(F7)

        ```

        This formula calculates a 30% discount, if the user enters a coupon code (couponCode = "NewYearDiscount") OR (couponCode = "BlackFridaySale"), otherwise it sets the discount to 0.

**Text functions:**

* IF(): Evaluates a condition and returns a specific value if TRUE, and another value if FALSE.

    * Example: Displaying a custom message based on a chosen product category.

    1. Set the `Value` property of the `message` field to `Only upto 7 kg check-in lagguage is allowed!`:

    1. Set the `Visible` property of the `message` field to:


        ```JavaScript

        =if(address of value property of chosen product category ="Economy", TRUE(), FALSE())

        ```

        For example, 

        ```JavaScript

        =if(F5="Economy", TRUE(), FALSE())

        ```

    1.  Set the value expression of the `message` field to 
    
        ```JavaScript
    
        =FORMULATEXT ((address of value property of the final amount field))

        ```

         For example, 

        ```JavaScript

        =FORMULATEXT(G15)

        ```

        This formula displays the message "Only up to 7 kg check-in luggage is allowed!" if the chosen class is "Economy", otherwise it leaves the message field blank.

**Math functions:**

* SUM(): Adds values from a specified range of cells.

    Example: Calculating the total cost of items in a shopping cart.

    In the value expression of the "total cost" field:
    SUM(price * quantity)

    This formula assumes you have separate fields for "price" and "quantity" of each item. It multiplies them and uses SUM() to add up the total cost for all items in the cart.

* ROUND(): Rounds a number to a specified number of decimal places.

    Example: Rounding a calculated discount amount to two decimal places.

    In the value expression of the "discount amount" field (assuming a discount is calculated elsewhere):
    ROUND(discount, 2)

    This formula rounds the discount value to two decimal places.

* MIN(): Returns the smallest value from a specified range of cells.

    Example: Finding the minimum required age for a signup form based on a selected country.

    In the value expression of a "minimum age" field:
    MIN(ageLimits["US"], ageLimits["UK"], ageLimits["France"])

    This formula assumes you have a table named "ageLimits" that stores minimum age requirements for different countries. It uses MIN() to find the smallest value among them.


In addition, Adaptive Forms Block lets you take full charge of your forms by creating [custom functions](#creating-custom-functions). Custom functions let you define your own rules and logic, giving you complete control over how your forms behave.


## Creating and deploying Custom Functions

The Out-of-the-Box (OOTB) Adaptive Forms block provides implementations for many [common spreadsheet functions](#spreadsheet-functions-for-rules). However, for more granular control over your forms, you can use any of the OOTB functions available in Microsoft&reg; Excel or Google Sheets within your Adaptive Forms blocks. Adaptive Forms block does not contain implementation for all the OOTB functions available in Microsoft&reg; Excel or Google Sheets. If you require any of such functions, you can develop a custom function with similar syntax to achieve the functionality provided by Microsoft&reg; Excel or Google Sheets. For example, you can implement the [Microsoft&reg; Excel's Year() function](https://support.microsoft.com/en-us/office/calculate-age-113d599f-5fea-448f-a4c3-268927911b37#) to calculate age from date of birth. 


### Create a custom function

Custom functions reside in the `[Adaptive form block]/functions.js` file. The creation process generally involves the following steps:

* Function Declaration: Define the function name and its parameters (the inputs that it accepts).
* Logic Implementation: Write the code that outlines the specific calculations or manipulations performed by the function.
* Function Export: Make the function accessible within your rules by exporting it from the relevant file.

### Example: Year Function

This example demonstrates two custom functions that mimic Microsoft&reg; Excel's YEAR() function to calculate age:


```JavaScript

/**
 * Get the current date and time
 * @name now
 * @returns {Date} The current date and time as a Date object
 */
function now() {
  const today = new Date();
  return today;
}

/**
 * Get the year from a Date object
 * @name year
 * @param {Date} date The date object
 * @throws {TypeError} If the input is not a Date object
 * @returns {number} The year as a number
 */
function year(date) {
  let inputDate = new Date(date)

  if (!(inputDate instanceof Date)) {
    throw new TypeError("Input must be a Date object");
  }

  const year = inputDate.getFullYear();

  return year;
}

// Make the function accessible for use in rules
export { now, year };


```

### Use a Custom Function in your form

To use the custom function in your form:

1. **Add the Function**: Include your custom function in the `[Adaptive form block]/functions.js` file. Remember to add it to the export statement within the file.
1. **Deploy the File**: Deploy the updated `functions.js` file to your GitHub project and verify a successful build.
1. **Function Usage**: Access the function within your form's spreadsheet using the `Value`, `Value Expression`, `Visible`, or `Visible Expression` properties, similar to any other spreadsheet function supported OOTB.
1. **Preview the Form**: Use AEM Sidekick to preview your form with the newly implemented function.     

