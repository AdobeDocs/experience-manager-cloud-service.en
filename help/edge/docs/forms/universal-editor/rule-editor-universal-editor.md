---
title: Rule Editor for Dynamic Forms in Universal Editor
description: Create dynamic, intelligent forms using the Rule Editor in Universal Editor. Add conditional logic, calculations, and interactive behaviors without coding.
feature: Edge Delivery Services
role: Admin, Architect, Developer
level: Intermediate
exl-id: 846f56e1-3a98-4a69-b4f7-40ec99ceb348
---

# Rule Editor for Dynamic Forms in Universal Editor

The Rule Editor in Universal Editor enables you to create intelligent, dynamic forms that respond to user input in real time. You can transform static forms into interactive experiences with conditional field visibility, automated calculations, and complex business logic—all without writing code.


## What You'll Learn

By the end of this guide, you will:

- Understand how rules work and when to use different rule types
- Enable and access the Rule Editor in Universal Editor
- Create conditional logic to show or hide form fields dynamically
- Implement automated calculations and data validation
- Build custom functions for complex business rules
- Apply best practices for optimal form performance

## Why Use the Rule Editor?

**Transform Static Forms into Smart Experiences:**

- **Conditional Logic**: Show relevant fields based on user selections
- **Dynamic Calculations**: Automatically compute values as users type
- **Data Validation**: Provide real-time feedback and prevent errors
- **Improved UX**: Reduce form complexity and guide users through logical flows
- **No Coding Required**: Visual interface accessible to non-developers

**Common Use Cases:**

- Tax calculation forms with conditional deductions
- Multi-step wizards with branching paths
- Insurance forms with rate calculations
- Survey forms with conditional questions
- E-commerce forms with dynamic pricing

## How Rules Work

Rules are automated instructions that make your forms intelligent and responsive. They specify what should happen when certain conditions are met.

### **Rule Components**

**Condition**: A logical test that evaluates to true or false.

- "Is the user's income greater than $50,000?"
- "Has the user selected 'Yes' for insurance coverage?"
- "Is the form field empty?"

**Action**: The outcome that occurs when the condition is met.

- Show or hide form fields
- Calculate values automatically
- Display validation messages
- Enable or disable components

### **Rule Logic Patterns**

**1. Condition-Action (When-Then)**

```
WHEN gross salary > 50000
THEN show "Additional Deduction" field
```

*Best for:* Conditional field visibility, dynamic content

**2. Action-Condition (Set-If)**

```
SET taxable income = gross salary - deductions
IF deductions are applicable
```

*Best for:* Calculations, data transformations

**3. Action-Condition-Alternate (If-Then-Else)**

```
IF income > 50000
THEN show "High Income" fields
ELSE show "Standard Income" fields
```

*Best for:* Branching logic, mutually exclusive options

### **Real-World Example**

**Scenario**: Tax calculation form

- **Condition**: "Gross salary exceeds $50,000"
- **Primary Action**: Show "Additional Deduction" field
- **Alternate Action**: Hide "Additional Deduction" field
- **Result**: Users only see relevant fields based on their income level

## Prerequisites

Before you begin working with the Rule Editor, make sure you have the following:

### **Access Requirements**

- Authoring access to **AEM as a Cloud Service**
- **Universal Editor** with the Rule Editor extension enabled
- Form editing permissions in your AEM environment

### **Technical Requirements**

- **Basic form design knowledge**: Familiarity with form components and their properties
- **Business logic familiarity**: Ability to define conditional requirements
- **Basic JavaScript knowledge** (only required for custom functions)

### **Enable Rule Editor Extension**

The Rule Editor extension is not enabled by default in Universal Editor. You can enable it from the [Extension Manager](/help/implementing/developing/extending/extension-manager.md).

**After enabling the extension:**
The ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon appears in the upper-right corner when you select form components.

![Universal Editor rule editor](/help/edge/docs/forms/assets/universal-editor-rule-editor.png)
*Figure: Rule Editor icon appears when you select form components*

**To access the Rule Editor:**

1. Select any form component in Universal Editor.
2. Click the ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon that appears.
3. The Rule Editor interface opens in a new panel.

![Rule Editor user interface](/help/edge/docs/forms/assets/rule-editor-for-field.png)
*Figure: Rule Editor interface for editing component rules*

>[!NOTE]
>
> Throughout this article, "form component" and "form object" refer to the same elements (such as input fields, buttons, panels, etc.).

## Rule Editor Interface Overview

The Rule Editor offers a user-friendly visual interface for creating and managing rules:

![Rule Editor user Interface](/help/edge/docs/forms/assets/rule-editor-interface.png)
*Figure: Complete Rule Editor interface with numbered components*

### **Interface Components**

**1. Component Title & Rule Type**

- **Purpose**: Displays the name of the selected component and the current rule type.
- **Example**: "Enter Gross Salary" (Text Input) with the "When" rule selected.
- **Tip**: Always confirm that you are editing the correct component.

**2. Form Objects and Functions Panel**

- **Form Objects Tab**: Provides a hierarchical view of all form components.
  - Use for: Referencing other fields in your rules.
  - Navigation: Expand or collapse to locate specific components.
- **Functions Tab**: Contains built-in mathematical and logical functions.
  - Use for: Performing complex calculations and data manipulations.
  - Categories: Math, String, Date, and Validation functions.

**3. Panel Toggle Button**

- **Purpose**: Shows or hides the objects and functions panel.
- **Tip**: Toggle off the panel to increase the rule editing workspace.
- **Keyboard shortcut**: Useful when working with complex rules.

**4. Visual Rule Builder**

- **Purpose**: The main area for constructing rule logic.
- **Features**: Drag-and-drop interface and dropdown selectors.
- **Workflow**: Select rule type → Define conditions → Set actions.

**5. Control Buttons**

- **Done**: Saves the rule and closes the editor.
- **Cancel**: Discards changes and closes the editor without saving.
- **Tip**: Always test your rules before clicking Done.

### **Rule Management**

When you open the Rule Editor for a component that already has rules:

![show the available rules of form object](/help/edge/docs/forms/assets/rule-editor15.png)
*Figure: Managing existing rules for a form component*

**Available Actions:**

- **View**: Review rule summaries and logic.
- **Edit**: Modify existing rule conditions or actions.
- **Reorder**: Change the execution order of rules (rules run from top to bottom).
- **Enable/Disable**: Temporarily turn rules on or off for testing purposes.
- **Delete**: Permanently remove rules.

>[!TIP]
>
> **Rule Execution Order Matters**: Rules are executed from top to bottom. Place more specific conditions before general ones.

## Available Rule Types

The Rule Editor offers a comprehensive set of rule types organized by functionality. Select the appropriate type based on your specific use case:

### **Conditional Logic Rules**

**When**

- **Purpose**: Serves as the primary conditional rule for implementing complex logic.
- **Use case**: For example, "When user selects 'Married', show spouse information fields."
- **Logic pattern**: Condition → Action (with an optional alternate action)

**Hide/Show**

- **Purpose**: Controls field visibility based on specified conditions.
- **Use case**: Hide irrelevant sections or enable progressive disclosure.
- **Best practice**: Use to create a clean, focused user experience.

**Enable/Disable**

- **Purpose**: Controls whether a field can be interacted with, based on conditions.
- **Use case**: Disable the submit button until all required fields are completed.
- **Best practice**: Provide clear visual feedback to users.

### **Data Manipulation Rules**

**Set Value Of**

- **Purpose**: Automatically populates field values.
- **Use case**: Set today's date, calculate totals, or copy values between fields.
- **Best practice**: Use to reduce user effort and ensure accuracy.

**Clear Value Of**

- **Purpose**: Removes data from fields when conditions change.
- **Use case**: Clear dependent fields when a parent selection changes.
- **Best practice**: Maintain data integrity and prevent orphaned values.

**Format**

- **Purpose**: Transforms how values are displayed.
- **Use case**: Format currency, phone numbers, or dates.
- **Best practice**: Improve readability without altering the underlying data.

### **Validation Rules**

**Validate**

- **Purpose**: Implements custom validation logic.
- **Use case**: Enforce complex business rules or cross-field validation.
- **Best practice**: Provide clear and actionable error messages.

### **Calculation Rules**

**Mathematical Expression**

- **Purpose**: Performs automated calculations.
- **Use case**: Tax calculations, totals, or percentages.
- **Best practice**: Update calculations in real time as users type.

### **User Interface Rules**

**Set Focus**

- **Purpose**: Directs user attention to specific fields.
- **Use case**: Focus on error fields or guide users through wizard steps.
- **Best practice**: Use sparingly to avoid disrupting the user flow.

**Set Property**

- **Purpose**: Dynamically modifies component properties.
- **Use case**: Change placeholder text or modify options in a dropdown.
- **Best practice**: Enhance the user experience with contextual changes.

### **Form Control Rules**

**Submit Form**

- **Purpose**: Triggers form submission programmatically.
- **Use case**: Auto-submit after specific conditions are met.
- **Best practice**: Always validate the form before submission.

**Reset Form**

- **Purpose**: Clears all form data and resets the form to its initial state.
- **Use case**: "Start Over" functionality.
- **Best practice**: Confirm the action with the user before resetting.

**Save Form**

- **Purpose**: Saves the form as a draft for later completion.
- **Use case**: Useful for long forms or multi-session workflows.
- **Best practice**: Provide clear feedback on the save status.

### **Advanced Rules**

**Invoke Service**

- **Purpose**: Calls external APIs or services.
- **Use case**: Address lookup, real-time validation, or data enrichment.
- **Best practice**: Handle loading states and error scenarios appropriately.

**Add/Remove Instance**

- **Purpose**: Dynamically manages repeatable sections.
- **Use case**: Add family members or multiple addresses.
- **Best practice**: Provide clear controls for adding or removing instances.

**Navigate To**

- **Purpose**: Redirects users to other forms or pages.
- **Use case**: Multi-form workflows or conditional routing.
- **Best practice**: Preserve form data before navigation.

**Navigate Among Panels**

- **Purpose**: Controls navigation in wizard-style forms.
- **Use case**: Multi-step forms or conditional step skipping.
- **Best practice**: Display clear progress indicators.

**Dispatch Event**

- **Purpose**: Triggers custom events for advanced integrations.
- **Use case**: Analytics tracking or third-party integrations.
- **Best practice**: Use only for non-blocking actions.


## Step-by-Step Tutorial: Building a Smart Tax Calculator

This section provides a practical example to demonstrate the capabilities of the Rule Editor. The example guides you through building a tax calculation form that uses conditional logic and automated calculations.

![Screenshot of the Rule Editor interface showing the creation of a conditional rule with When-Then logic for form field visibility](/help/edge/docs/forms/assets/rule-editor-1.png)
*Figure: Tax calculation form with intelligent conditional fields*

### **Tutorial Overview**

In this tutorial, you will create a form that:

1. **Adapts to user input**: Displays relevant fields based on the income level.
2. **Calculates automatically**: Computes tax liability in real time.
3. **Validates data**: Ensures accurate calculations and data entry.

### **Form Structure**

| Field Name | Type | Purpose | Behavior |
|------------|------|---------|----------|
| **Gross Salary** | Number Input | User enters annual income | Triggers conditional logic |
| **Additional Deduction** | Number Input | Extra deductions (if applicable) | Displays when salary > $50,000 |
| **Taxable Income** | Number Input | Calculated automatically | Updates on input changes |
| **Tax Payable** | Number Input | Final tax amount | Calculates at 10% rate |

### **Business Logic to Implement**

**Rule 1: Conditional Field Display**

```
WHEN Gross Salary > 50,000
THEN Show "Additional Deduction" field
ELSE Hide "Additional Deduction" field
```

**Rule 2: Taxable Income Calculation**

```
SET Taxable Income = Gross Salary - Additional Deduction
(When Additional Deduction is applicable)
```

**Rule 3: Tax Calculation**

```
SET Tax Payable = Taxable Income × 10%
(Simplified flat rate for demonstration)
```

### **Implementation Steps**

Follow these steps to build your intelligent tax form:



+++ 1: Create the Foundation Form

**Objective**: Build the basic form structure with all required components

To create your tax calculation form in Universal Editor:

1. **Open Universal Editor**
   - Navigate to your AEM Sites console
   - Select the page where you want to add the form
   - Click **Edit** to open Universal Editor

2. **Add Form Components**
   
   Add these components in order:
   
   | Component | Type | Label | Settings |
   |-----------|------|-------|----------|
   | Title | Title | "Tax Calculation Form" | Heading level H2 |
   | Number Input | Number Input | "Gross Salary" | Required: Yes, Placeholder: "Enter annual salary" |
   | Number Input | Number Input | "Additional Deduction" | Required: No, Placeholder: "Enter additional deductions" |
   | Number Input | Number Input | "Taxable Income" | Required: No, Read-only: Yes |
   | Number Input | Number Input | "Tax Payable" | Required: No, Read-only: Yes |
   | Submit Button | Submit | "Calculate Tax" | Type: Submit |

3. **Configure Initial Settings**
   
   - **Hide the Additional Deduction field**: 
     - Select the "Additional Deduction" component
     - In the Properties panel, set **Visible** to **No**
     - This field will be shown conditionally based on rules
   
   - **Make calculated fields read-only**:
     - Select "Taxable Income" and "Tax Payable" fields
     - Set **Read Only** to **Yes** in Properties
   
      ![Screenshot of a tax calculation form with input fields for gross salary, marital status, and dependent children, demonstrating the form structure before rules are applied](/help/edge/docs/forms/assets/rule-editor2.png)
*Figure: Initial form structure with basic components configured*

**Checkpoint**: You should now have a form with all required fields, where "Additional Deduction" is hidden and calculated fields are read-only.

+++

+++ 2. Add a conditional rule for a form field

  Once you have authored the form, write the first rule to show the `Additional Deduction` field only if the gross salary exceeds $50,000. To add a conditional rule:

  1. Open a form in Universal Editor for editing and select the **[!UICONTROL Gross Salary]** field in the content tree and select ![edit-rules](/help/forms/assets/edit-rules-icon.svg). Alternatively, you can select **[!UICONTROL Gross Salary]** field directly from the **[!UICONTROL Forms Object]** pane.
    ![Rule Editor example1](/help/edge/docs/forms/assets/rule-editor3.png)
  The visual Rule Editor interface appears.
  1. Click **[!UICONTROL Create]** to create rules.
   ![Rule Editor example2](/help/edge/docs/forms/assets/rule-editor4.png)
  By default, the `Set Value Of` rule type is selected. While you cannot change or modify the selected object, you can use the rule drop-down to select another rule type.  
  ![Rule Editor example3](/help/edge/docs/forms/assets/rule-editor5.png)
  1. Open the rule type drop-down list and select **[!UICONTROL When]** rule type.
  ![Rule Editor example4](/help/edge/docs/forms/assets/rule-editor6.png)
  1. Select **[!UICONTROL Select State]** drop-down and select **[!UICONTROL is greater than]**. The **[!UICONTROL Enter a Number]** field appears.
  ![Rule Editor example5](/help/edge/docs/forms/assets/rule-editor7.png)
  1. Enter `50000` in the **[!UICONTROL Enter a Number]** field in the rule.
  ![Rule Editor example6](/help/edge/docs/forms/assets/rule-editor8.png)
  You have defined the condition as `When Gross Salary is greater than 50000`. Next, define the action to perform if this condition is `True`.
  1. In the `Then` statement, select **[!UICONTROL Show]** from the **[!UICONTROL Select Action]** drop-down.
  ![Rule Editor example7](/help/edge/docs/forms/assets/rule-editor9.png)
  1. Drag-drop the **[!UICONTROL Additional Deduction]** field from the Form Objects tab on the **[!UICONTROL Drop object or select here]** field. Alternatively, select the **[!UICONTROL Drop object or select here]** field and select the **[!UICONTROL Additional Deduction]** field from the pop-up menu, which lists all form objects in the form.
  ![Rule Editor example8](/help/edge/docs/forms/assets/rule-editor10.png)
  1. Click **[!UICONTROL Add Else Section]** to add another condition for the **[!UICONTROL Gross Salary]** field, in case you enter salary less than `50000`.
  ![Rule Editor example9](/help/edge/docs/forms/assets/rule-editor11.png)
  1. Select **[!UICONTROL Hide]** from the **[!UICONTROL Select Action]** drop-down in the `Else` statement.
  ![Rule Editor example10](/help/edge/docs/forms/assets/rule-editor12.png)
  1. Drag-drop the **[!UICONTROL Additional Deduction]** field from the Form Objects tab on the **[!UICONTROL Drop object or select here]** field. Alternatively, select the **[!UICONTROL Drop object or select here]** field and select the **[!UICONTROL Additional Deduction]** field from the pop-up menu, which lists all form objects in the form.
  ![Rule Editor example11](/help/edge/docs/forms/assets/rule-editor13.png)
  1. Select **[!UICONTROL Done]** to save the rule.
  The rule appears as follows in the Rule Editor.
  ![Rule Editor example12](/help/edge/docs/forms/assets/rule-editor14.png)

  >[!NOTE]
  >
  > Alternatively, you can write a Show rule on the Additional Deduction field, instead of a When rule on the Gross Salary field, to implement the same behavior.

+++

+++ 3. Add calculation rules for the form fields

  Next, write a rule to compute the `Taxable Income`, which is the difference between `Gross Salary` and `Additional Deduction` (if applicable). To add calculation rule on the **[!UICONTROL Taxable Income]** field, perform the following steps:
  
  1. In authoring mode, select the **[!UICONTROL Taxable Income]** field and select ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon. Alternatively, you can select **[!UICONTROL Taxable Income]** field directly from the **[!UICONTROL Forms Object]** pane.
  1. Next, select **[!UICONTROL Create]** to create the rule.
    ![Rule Editor example13](/help/edge/docs/forms/assets/rule-editor16.png)
  1. Select **[!UICONTROL Select Option]** and select **[!UICONTROL Mathematical Expression]**. A field to write mathematical expression opens.
    ![Rule Editor example14](/help/edge/docs/forms/assets/rule-editor17.png)

  1. In the mathematical expression field:
  
      - Select or drag-drop from the Forms Object tab the **[!UICONTROL Gross Salary]** field in the first **[!UICONTROL Drop object or select here]** field.
  
      - Select **[!UICONTROL Minus]** from the **[!UICONTROL Select Operator]** field.
  
      - Select or drag-drop from the Forms Object tab the **[!UICONTROL Additional Deduction]** field in the other **[!UICONTROL Drop object or select here]** field.
      ![Rule Editor example15](/help/edge/docs/forms/assets/rule-editor18.png)

  1. Select **[!UICONTROL Done]** to save the rule.  
      
      Now, add a rule for the `Tax Payable ` field, which is determined by multiplying the taxable income by the tax rate. For simplicity, assume a fixed tax rate of `10%`.

  1. In authoring mode, select the **[!UICONTROL Tax Payable]** field and select ![edit-rules](/help/forms/assets/edit-rules-icon.svg) icon. Next, select **[!UICONTROL Create]** to create rules.
  ![Rule Editor example16](/help/edge/docs/forms/assets/rule-editor19.png)
  1. Select **[!UICONTROL Select Option]** and select **[!UICONTROL Mathematical Expression]**. A field to write mathematical expression opens.
  ![Rule Editor example17](/help/edge/docs/forms/assets/rule-editor20.png)
  1. In the mathematical expression field:
  
      - Select or drag-drop from the Forms Object tab the **[!UICONTROL Taxable Income]** field in the first **[!UICONTROL Drop object or select here]** field.
  
      - Select **[!UICONTROL Multiplied by]** from the **[!UICONTROL Select Operator]** field.
  
      - Select **Number** from the  **[!UICONTROL Select Option]** field  and enter the value as `10` in the **[!UICONTROL Enter a Number]** field.
      ![Rule Editor example18](/help/edge/docs/forms/assets/rule-editor21.png)
  1. Next, select in the highlighted area around the expression field and select **[!UICONTROL Extend Expression]**.
    ![Rule Editor example19](/help/edge/docs/forms/assets/rule-editor22.png)
  1. In the extended expression field, select **[!UICONTROL divided by]** from the **[!UICONTROL Select Operator]** field and **[!UICONTROL Number]** from the **[!UICONTROL Select Option]** field. Then, specify `100` in the number field.
    ![Rule Editor example20](/help/edge/docs/forms/assets/rule-editor23.png)
  1. Select **[!UICONTROL Done]** to save the rule. 

+++

+++ 4. Preview a form

Now, when you preview the form and enter the **Gross Salary** as `60,000`, the **Additional Deduction** field appears, and the **Taxable Income** and **Tax Payable** are calculated accordingly.

![Preview a form](/help/edge/docs/forms/assets/rule-editor-form.png)

+++

Apart from built-in functions like Sum and Average, you can create custom functions to implement complex business logic tailored to your specific requirements.

## Advanced: Custom Functions

**When to Use Custom Functions:**

- For complex calculations that go beyond the capabilities of built-in functions
- To implement business-specific validation rules
- For data transformations and formatting
- To integrate with external systems or APIs

**Benefits:**

- **Reusability**: Write the function once and use it across multiple forms and rules
- **Maintainability**: Centralized logic that is easy to update
- **Performance**: Optimized JavaScript execution
- **Flexibility**: Ability to handle complex scenarios not addressed by standard rules

### **Creating Custom Functions**

**File Location**: `/blocks/form/functions.js` in your AEM project

**Development Workflow:**

1. **Function Declaration**
   - Define clear and descriptive function names and parameters
   - Use names that indicate the function's purpose
   - Document parameters and return types

2. **Logic Implementation**
   - Write clean and efficient JavaScript code
   - Handle edge cases and error scenarios
   - Follow coding best practices

3. **Function Export**
   - Export functions to make them available in the Rule Editor
   - Use named exports for better organization
   - Test functions before deployment

4. **Documentation**
   - Add JSDoc comments for function documentation
   - Include usage examples
   - Specify parameter types and return values

The following example demonstrates two custom functions: `getFullName` and `days`.

```JavaScript

/**
 - Get Full Name
 - @name getFullName Concats first name and last name
 - @param {string} firstname in Stringformat
 - @param {string} lastname in Stringformat
 - @return {string}
 */
function getFullName(firstname, lastname) {
  return `${firstname} ${lastname}`.trim();
}

/**
 - Calculate the number of days between two dates.
 - @param {*} endDate
 - @param {*} startDate
 - @name days Calculates the numebr of days between two dates
 - @returns {number} returns the number of days between two dates
 */
function days(endDate, startDate) {
  const start = typeof startDate === 'string' ? new Date(startDate) : startDate;
  const end = typeof endDate === 'string' ? new Date(endDate) : endDate;

  // return zero if dates are valid
  if (Number.isNaN(start.getTime()) || Number.isNaN(end.getTime())) {
    return 0;
  }

  const diffInMs = Math.abs(end.getTime() - start.getTime());
  return Math.floor(diffInMs / (1000 * 60 * 60 * 24));
}

// eslint-disable-next-line import/prefer-default-export
export { getFullName, days };

```

![Adding custom Function](/help/edge/docs/forms/assets/create-custom-function.png)

### Use a Custom Function in Rule Editor

To use a custom function in the Rule Editor:

1. **Add the Function**: Add your custom function to the `../[blocks]/form/functions.js` file. Ensure that you include it in the `export` statement within the file.
2. **Deploy the File**: Deploy the updated `functions.js` file to your GitHub project and confirm that the build completes successfully.
3. **Function Usage**: In your form's Rule Editor, access the function by selecting the `Function Output` option in the **[!UICONTROL Select Action]** field.

    ![Custom Function in Rule Editor](/help/edge/docs/forms/assets/custom-function-rule-editor.png)

4. **Preview the Form**: Preview your form to verify that the newly implemented function works as expected.

## Best Practices for Rule Development

### **Performance Optimization**

**Minimize Rule Complexity**

- Keep individual rules simple and focused.
- Break complex logic into multiple smaller rules.
- Avoid deeply nested conditions when possible.

**Optimize Rule Execution**

- Place the most frequently triggered rules first.
- Use specific conditions to reduce unnecessary evaluations.
- Consider the impact of rules on form loading time.

**Resource Management**

- Limit the number of rules per form component.
- Use custom functions for repeated logic instead of duplicating rules.
- Test performance with realistic data volumes.

### **User Experience Guidelines**

**Provide Clear Feedback**

- Use validation messages that guide users toward correct input.
- Show loading indicators for rules that involve external services.
- Implement progressive disclosure to reduce cognitive load.

**Maintain Form Responsiveness**

- Avoid rules that cause abrupt visual changes.
- Implement smooth transitions for show/hide operations.
- Test rules across different devices and screen sizes.

**Error Handling**

- Provide fallback behavior when rules fail.
- Display user-friendly error messages.
- Log errors for debugging while maintaining a positive user experience.

### **Development Best Practices**

**Testing Strategy**

- Test rules with edge cases and boundary values.
- Verify rule behavior across different browsers.
- Test form functionality both with and without JavaScript enabled.

**Documentation**

- Document the business logic behind complex rules.
- Maintain a rule inventory for large forms.
- Use consistent naming conventions for components and rules.

**Version Control**

- Track changes to custom functions in version control.
- Test rules in a development environment before production.
- Maintain backup copies of working rule configurations.

## Troubleshooting Common Issues

### **Rule Execution Problems**

**Rules Not Triggering**

- **Check component names**: Ensure referenced components exist and have correct names.
- **Verify rule order**: Rules execute from top to bottom; reorder if needed.
- **Validate conditions**: Test conditions with known values to verify logic.
- **Browser console**: Check for JavaScript errors that might block execution.

**Incorrect Rule Behavior**

- **Review logic operators**: Confirm AND/OR conditions are correctly structured.
- **Test with sample data**: Use known values to isolate issues.
- **Check data types**: Ensure numeric comparisons use numbers, not strings.
- **Validate expressions**: Test mathematical expressions separately.

### **Performance Issues**

**Slow Form Response**

- **Reduce rule complexity**: Simplify complex conditional logic.
- **Optimize custom functions**: Profile and optimize JavaScript code.
- **Limit external calls**: Minimize service invocations in rules.
- **Use efficient selectors**: Ensure form object references are specific.

**Memory Usage**

- **Clean up event listeners**: Remove unused rule bindings.
- **Optimize custom functions**: Avoid memory leaks in JavaScript code.
- **Limit rule scope**: Use targeted rules instead of global conditions.

### **Custom Function Issues**

**Functions Not Available**

- **Check file path**: Verify `functions.js` is in the correct location: `/blocks/form/functions.js`.
- **Verify exports**: Ensure functions are properly exported.
- **Build process**: Confirm the project build includes the updated functions file.
- **Cache clearing**: Clear the browser cache after deploying new functions.

**Function Errors**

- **Parameter validation**: Check that function parameters match expected types.
- **Error handling**: Add try-catch blocks to handle exceptions gracefully.
- **Console logging**: Use console.log for debugging function execution.
- **JSDoc validation**: Ensure function documentation matches the implementation.

### **Universal Editor Integration**

**Rule Editor Not Appearing**

- **Extension enabled**: Verify the Rule Editor extension is activated.
- **Component selection**: Ensure you have selected a supported form component.
- **Browser compatibility**: Test in supported browsers (Chrome, Firefox, Safari).
- **Access permissions**: Confirm the user has the necessary AEM permissions.

**Interface Issues**

- **Panel visibility**: Use the toggle button to show or hide the form objects panel.
- **Rule saving**: Ensure rules are saved before closing the editor.
- **Browser zoom**: Reset browser zoom to 100% for optimal interface display.

## Important Limitations

>[!IMPORTANT]
>
> **Custom Function Restrictions**:
>
> - Static and dynamic imports are not supported in custom function scripts.
> - All code must be included directly in the `/blocks/form/functions.js` file.
> - Functions must be synchronous (no async/await or Promises).
> - Access to browser APIs is limited for security reasons.

>[!WARNING]
>
> **Production Considerations**:
>
> - Test all rules thoroughly in a staging environment.
> - Monitor form performance after deploying complex rules.
> - Have a rollback plan for rule-related issues.
> - Consider the impact on users with slow network connections.

## Summary

The Rule Editor in Universal Editor enables you to create intelligent, dynamic forms that provide exceptional user experiences. By implementing conditional logic, automated calculations, and custom business rules, you can:

**Transform Static Forms**:

- Add conditional field visibility for cleaner, more focused interfaces.
- Implement real-time calculations and data validation.
- Create sophisticated business logic without coding.

**Improve User Experience**:

- Guide users through logical form flows.
- Reduce errors with intelligent validation.
- Provide immediate feedback and assistance.

**Enhance Efficiency**:

- Automate repetitive calculations and data entry.
- Streamline complex workflows with smart routing.
- Reduce support burden with self-service capabilities.

### **Next Steps**

Now that you understand the Rule Editor fundamentals:

1. **Start Simple**: Begin with basic show/hide rules before advancing to complex calculations.
1. **Practice with Examples**: Use the tax calculator tutorial as a foundation.
1. **Explore Advanced Features**: Experiment with custom functions for specialized requirements.
1. **Test Thoroughly**: Always validate rules across different scenarios and devices.
1. **Monitor Performance**: Ensure rules enhance rather than hinder user experience.
