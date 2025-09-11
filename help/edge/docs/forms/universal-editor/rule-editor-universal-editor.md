---
title: Rule Editor for Edge Delivery Services Forms
description: Create dynamic, intelligent forms using the Rule Editor in Universal Editor. Add conditional logic, calculations, and interactive behaviors without coding.
feature: Edge Delivery Services
role: Admin, Architect, Developer
level: Intermediate
exl-id: 846f56e1-3a98-4a69-b4f7-40ec99ceb348
---

# Rule Editor for Edge Delivery Services Forms

The Rule Editor allows authors to turn static forms into responsive, intelligent experiences without writing code. You can conditionally show fields, perform calculations, validate data, guide users through flows, and integrate business logic that adapts as people type.

## What you'll learn

By the end of this guide, you will be able to:

- Understand how rules work and when to use different rule types
- Enable and access the Rule Editor in Universal Editor
- Create conditional logic to show or hide fields dynamically
- Implement automated calculations and data validation
- Build custom functions for complex business rules
- Apply best practices for performance, maintainability, and UX

## Why use the Rule Editor?

- **Conditional logic**: Show relevant fields only when needed to reduce noise and cognitive load.
- **Dynamic calculations**: Compute values automatically (totals, rates, tax) as users type.
- **Data validation**: Prevent errors early with real-time checks and clear messages.
- **Guided experiences**: Lead users through logical steps (wizards, branching).
- **No-code authoring**: Configure powerful behavior through a visual interface.

Common scenarios include tax calculators, loan and premium estimators, eligibility flows, multi-step applications, and surveys with conditional questions.

## How rules work

A rule defines what should happen when a condition is met. Conceptually, a rule has two parts:

- **Condition**: A statement that evaluates to true or false.
  - Examples: "Income > 50,000," "Coverage = 'Yes'," "Field is empty"
- **Action**: What occurs when the condition is true (and optionally, when it is false).
  - Examples: Show/Hide a field, Set/Clear a value, Validate input, Enable/Disable a button

+++ Rule logic patterns

- **Condition → Action (When/Then)**
  
  ```text
  WHEN Gross Salary > 50000
  THEN Show "Additional Deduction"
  ```

  Best for conditional visibility and progressive disclosure.

- **Action ← Condition (Set If/Only if)**

  ```text
  SET Taxable Income = Gross Salary - Deductions
  IF Deductions are applicable
  ```

  Best for calculations and data transformations.

- **If → Then → Else (Alternate action)**

  ```text
  IF Income > 50000
  THEN Show "High Income" fields
  ELSE Show "Standard Income" fields
  ```

  Best for branching logic and mutually exclusive flows.

+++

+++ Real-world example

- **Condition**: "Gross salary exceeds $50,000"
- **Primary action**: Show "Additional Deduction"
- **Alternate action**: Hide "Additional Deduction"
- **Result**: Users see only the fields that apply to them

+++

## Prerequisites


+++ Access requirements

**Essential permissions and setup**:

- **AEM as a Cloud Service**: Authoring access with form editing permissions
- **Universal Editor**: Installed and configured on your environment
- **Rule Editor extension**: Enabled via [Extension Manager](/help/implementing/developing/extending/extension-manager.md)
- **Form editing permissions**: Ability to create and modify form components in Universal Editor

**Verification steps**:

1. Confirm you can access Universal Editor from your AEM Sites console
2. Verify you can create and edit form components
3. Check that the Rule Editor icon ![edit-rules](/help/forms/assets/edit-rules-icon.svg) appears when selecting form components

+++

+++ Technical requirements

**Required knowledge and skills**:

- **Universal Editor proficiency**: Experience creating forms with text inputs, dropdowns, and basic field properties
- **Business logic understanding**: Ability to define conditional requirements and validation rules for your specific use case
- **Form component familiarity**: Knowledge of field types (text, number, dropdown), properties (required, visible, read-only), and form structure

**Optional for advanced usage**:

- **JavaScript fundamentals**: Required only for creating custom functions (data types, functions, basic syntax)
- **JSON understanding**: Helpful for complex data manipulation and API integrations

**Assessment questions**:

- Can you create a basic form with text inputs and a submit button in Universal Editor?
- Do you understand when fields should be required vs optional in your business context?
- Can you identify which form elements need conditional visibility in your use case?

+++

+++ Enable the Rule Editor extension

**Important**: The Rule Editor extension is not enabled by default in Universal Editor environments.

**Activation steps**:

1. Navigate to the [Extension Manager](/help/implementing/developing/extending/extension-manager.md) in your AEM environment
2. Locate the "Rule Editor" extension in the available extensions list
3. Click **Enable** and confirm the activation
4. Wait for the system to refresh (may take 1-2 minutes)

**Verification**:

- After enabling, the Rule Editor icon appears when you select a form component: ![edit-rules](/help/forms/assets/edit-rules-icon.svg)

![Universal Editor rule editor](/help/edge/docs/forms/assets/universal-editor-rule-editor.png)
Figure: Rule Editor icon appears when you select form components

To open the Rule Editor:

1. Select a form component in Universal Editor.
2. Click the Rule Editor icon.
3. The Rule Editor opens in a side panel.

![Rule Editor user interface](/help/edge/docs/forms/assets/rule-editor-for-field.png)
Figure: Rule Editor interface for editing component rules

>[!NOTE]
>
> Throughout this article, "form component" and "form object" refer to the same elements (for example, inputs, buttons, panels).

## Rule Editor interface overview

![Rule Editor user Interface](/help/edge/docs/forms/assets/rule-editor-interface.png)
Figure: Complete Rule Editor interface with numbered components

1. **Component title and rule type**: Confirms the selected component and active rule type.
2. **Form Objects and Functions panel**:
   
     - Form Objects: hierarchical view of fields and containers for referencing in rules
     - Functions: built-in math, string, date, and validation helpers

3. **Panel toggle**: Show/hide the objects and functions panel to increase workspace
4. **Visual rule builder**: Drag-and-drop, dropdown-driven rule composer
5. **Controls**: Done (save), Cancel (discard). Always test rules before saving.

+++

+++ Managing existing rules

When a component already has rules, you can:

- **View**: See rule summaries and logic
- **Edit**: Modify conditions and actions
- **Reorder**: Change execution order (top to bottom)
- **Enable/Disable**: Toggle rules for testing
- **Delete**: Remove rules safely

>[!TIP]
>
> Put specific rules before general ones. Execution is top-to-bottom.

+++

## Available rule types

Choose the rule type that best matches your intent.

+++ Conditional logic

- **When**: Primary rule for complex conditional behavior (Condition → Action ± Else)
- **Hide/Show**: Controls visibility based on a condition (progressive disclosure)
- **Enable/Disable**: Controls whether a field is interactive (for example, disable Submit until required fields are valid)

+++

+++ Data manipulation

- **Set Value Of**: Auto-populate values (for example, dates, totals, copies)
- **Clear Value Of**: Remove data when conditions change
- **Format**: Transform display formatting (currency, phone, date) without altering stored values

+++

+++ Validation

- **Validate**: Custom validation logic, including cross-field checks and business rules

+++

+++ Calculation

- **Mathematical Expression**: Compute values in real time (totals, tax, ratios)

+++

+++ User interface

- **Set Focus**: Move focus to a specific field (use sparingly)
- **Set Property**: Modify component properties dynamically (placeholder, options, etc.)

+++

+++ Form control

- **Submit Form**: Programmatically submit the form (only after validations pass)
- **Reset Form**: Clear and reset to initial state (confirm before use)
- **Save Form**: Save as draft for later (long forms, multi-session)

+++

+++ Advanced

- **Invoke Service**: Call external APIs/services (handle loading and errors)
- **Add/Remove Instance**: Manage repeatable sections (for example, dependents, addresses)
- **Navigate To**: Route to other forms/pages (preserve data before navigation)
- **Navigate Among Panels**: Control wizard step navigation and skipping
- **Dispatch Event**: Trigger custom events for integrations or analytics

+++

## Step-by-step tutorial: Build a smart tax calculator

+++ Tutorial overview

This example demonstrates conditional visibility and automatic calculations.

![Screenshot of the Rule Editor interface showing the creation of a conditional rule with When-Then logic for form field visibility](/help/edge/docs/forms/assets/rule-editor-1.png)
Figure: Tax calculation form with intelligent conditional fields

You will build a form that:

1. Adapts to user input by showing relevant fields
2. Calculates values in real time
3. Validates data to improve accuracy

+++

+++ Form structure

| Field Name              | Type          | Purpose                        | Behavior                                |
|-------------------------|---------------|--------------------------------|-----------------------------------------|
| Gross Salary            | Number Input  | User's annual income           | Triggers conditional logic               |
| Additional Deduction    | Number Input  | Extra deductions (if eligible) | Visible only when Salary > $50,000       |
| Taxable Income          | Number Input  | Calculated value               | Read-only, updates on change             |
| Tax Payable             | Number Input  | Calculated value               | Read-only, computed at a flat rate       |

+++

+++ Business logic

- **Rule 1: Conditional display**

  ```text
  WHEN Gross Salary > 50,000
  THEN Show "Additional Deduction"
  ELSE Hide "Additional Deduction"
  ```

- **Rule 2: Taxable Income calculation**

  ```text
  SET Taxable Income = Gross Salary - Additional Deduction
  (Only when Additional Deduction applies)
  ```

- **Rule 3: Tax Payable calculation**

  ```text
  SET Tax Payable = Taxable Income × 10%
  (Simplified flat rate)
  ```

+++

+++ Step 1: Create the form

**Objective**: Build the base form with all fields and initial settings.

1. **Open Universal Editor**:
   - Navigate to AEM Sites console, select your page, click **Edit**
   - Ensure you have the [Universal Editor](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/introduction.html) properly configured

2. **Add form components in this order**:
   - Title (H2): "Tax Calculation Form"
   - Number Input: "Gross Salary" (Required: Yes, Placeholder: "Enter annual salary")
   - Number Input: "Additional Deduction" (Required: No, Placeholder: "Enter additional deductions")
   - Number Input: "Taxable Income" (Read-only: Yes)
   - Number Input: "Tax Payable" (Read-only: Yes)
   - Submit button: "Calculate Tax"

3. **Configure initial field properties**:
   - Hide "Additional Deduction" (set Visible: No in Properties panel)
   - Set "Taxable Income" and "Tax Payable" to Read-only: Yes

![Screenshot of a tax calculation form with input fields for gross salary, marital status, and dependent children, demonstrating the form structure before rules are applied](/help/edge/docs/forms/assets/rule-editor2.png)
Figure: Initial form structure with basic components configured

**Checkpoint**: You should have a form with all required fields where "Additional Deduction" is hidden and calculated fields are read-only.

+++

+++ Step 2: Add conditional visibility rule

**Goal**: Show "Additional Deduction" field only when Gross Salary exceeds $50,000.

1. **Select the Gross Salary field** and click the Rule Editor icon ![edit-rules](/help/forms/assets/edit-rules-icon.svg)
2. **Create a new rule**:
   - Click **Create**
   - Change rule type from "Set Value Of" to **"When"**
3. **Configure the condition**:
   - Select **"is greater than"** from the dropdown
   - Enter `50000` in the number field
4. **Set the Then action**:
   - Choose **"Show"** from the Select Action dropdown
   - Drag or select **"Additional Deduction"** field from Form Objects
5. **Add the Else action**:
   - Click **"Add Else Section"**
   - Choose **"Hide"** from the Select Action dropdown
   - Select **"Additional Deduction"** field
6. **Save the rule**: Click **Done**

>[!NOTE]
>
> Alternative approach: You can achieve the same result by creating a Show/Hide rule directly on the "Additional Deduction" field instead of a When rule on "Gross Salary."

+++

+++ Step 3: Add calculation rules

**Goal**: Automatically compute "Taxable Income" and "Tax Payable" based on user input.

**Configure Taxable Income calculation**:

1. **Select "Taxable Income" field** and open Rule Editor
2. **Create Mathematical Expression**:
   - Click **Create** → Select **"Mathematical Expression"**
   - Build expression: **Gross Salary − Additional Deduction**
   - Drag "Gross Salary" to first field
   - Select **"Minus"** operator
   - Drag "Additional Deduction" to second field
3. **Save**: Click **Done**

**Configure Tax Payable calculation**:

1. **Select "Tax Payable" field** and open Rule Editor
2. **Create Mathematical Expression**:
   - Click **Create** → Select **"Mathematical Expression"**
   - Build expression: **Taxable Income × 10 ÷ 100**
   - Drag "Taxable Income" to first field
   - Select **"Multiplied by"** operator
   - Enter `10` as number
   - Click **"Extend Expression"**
   - Select **"divided by"** operator
   - Enter `100` as number
3. **Save**: Click **Done**

+++

+++ Step 4: Test the form

**Verify your implementation by testing the complete flow**:

1. **Preview the form**: Click the preview mode in Universal Editor
2. **Test the conditional logic**:
   - Enter Gross Salary = `30000` → "Additional Deduction" should remain hidden
   - Enter Gross Salary = `60000` → "Additional Deduction" should appear
3. **Test calculations**:
   - With Gross Salary = `60000`, enter Additional Deduction = `5000`
   - Verify Taxable Income = `55000` (60000 - 5000)
   - Verify Tax Payable = `5500` (55000 × 10%)

![Preview a form](/help/edge/docs/forms/assets/rule-editor-form.png)
Figure: Completed tax calculator with conditional fields and automatic calculations

**Success criteria**: The form should dynamically show/hide fields and calculate values in real-time as users type.


+++

## Advanced: Custom functions

For complex business logic beyond built-in capabilities, you can create custom JavaScript functions that integrate seamlessly with the Rule Editor.

+++ When to use custom functions

**Ideal scenarios for custom functions**:

- **Complex calculations**: Multi-step computations not easily expressed in the Mathematical Expression rule
- **Business-specific validations**: Custom validation logic specific to your organization or industry
- **Data transformations**: Format conversions, string manipulations, or data parsing
- **External integrations**: Calls to internal APIs or third-party services (with limitations)

**Benefits of custom functions**:

- **Reusability**: Write once, use across multiple forms and rules
- **Maintainability**: Centralized logic that's easier to update and debug
- **Performance**: Optimized JavaScript execution compared to complex rule chains
- **Flexibility**: Handle edge cases and complex scenarios not addressed by standard rules

+++

+++ Creating and implementing custom functions

**File location**: All custom functions must be defined in `/blocks/form/functions.js` in your Edge Delivery Services project.

**Development workflow**:

1. **Function design**
   - Use descriptive, action-oriented function names
   - Define clear parameter types and return values
   - Handle edge cases and invalid inputs gracefully

2. **Implementation**
   - Write clean, well-commented JavaScript
   - Include input validation and error handling
   - Test functions independently before integration

3. **Documentation**
   - Add comprehensive JSDoc comments
   - Include usage examples and parameter descriptions
   - Document any limitations or dependencies

4. **Deployment**
   - Export functions using named exports
   - Deploy to your project repository
   - Verify build completion before testing

**Example implementation**:

```javascript
/**
 * Concatenates first and last name with proper formatting
 * @name getFullName
 * @description Combines first and last name, handles edge cases like missing values
 * @param {string} firstName - The person's first name
 * @param {string} lastName - The person's last name  
 * @returns {string} Formatted full name or empty string if both inputs are invalid
 */
function getFullName(firstName, lastName) {
  // Handle null, undefined, or empty string inputs
  const first = (firstName || '').toString().trim();
  const last = (lastName || '').toString().trim();
  
  return `${first} ${last}`.trim();
}

/**
 * Calculates the number of days between two dates
 * @name days
 * @description Computes absolute difference in days, handles various date input formats
 * @param {Date|string} endDate - End date (Date object or ISO string)
 * @param {Date|string} startDate - Start date (Date object or ISO string)
 * @returns {number} Number of days between dates, 0 if inputs are invalid
 */
function days(endDate, startDate) {
  // Convert string inputs to Date objects
  const start = typeof startDate === 'string' ? new Date(startDate) : startDate;
  const end = typeof endDate === 'string' ? new Date(endDate) : endDate;

  // Validate date objects
  if (Number.isNaN(start.getTime()) || Number.isNaN(end.getTime())) {
    return 0;
  }

  // Calculate absolute difference in milliseconds, then convert to days
  const diffInMs = Math.abs(end.getTime() - start.getTime());
  return Math.floor(diffInMs / (1000 * 60 * 60 * 24));
}

// Export functions for use in Rule Editor
export { getFullName, days };
```

![Adding custom Function](/help/edge/docs/forms/assets/create-custom-function.png)
Figure: Adding custom functions to the functions.js file

+++

+++ Using custom functions in Rule Editor

**Integration steps**:

1. **Add function to project**
   - Create or edit `/blocks/form/functions.js` in your project
   - Include your function in the export statement

2. **Deploy and build**
   - Commit changes to your repository
   - Ensure the build process completes successfully
   - Allow time for CDN cache updates

3. **Access in Rule Editor**
   - Open Rule Editor for any form component  
   - Select **"Function Output"** in the **Select Action** dropdown
   - Choose your custom function from the available functions list
   - Configure function parameters using form fields or static values

4. **Test thoroughly**
   - Preview the form to verify function behavior
   - Test with various input combinations including edge cases
   - Verify performance impact on form loading and interaction

![Custom Function in Rule Editor](/help/edge/docs/forms/assets/custom-function-rule-editor.png)
Figure: Selecting and configuring custom functions in the Rule Editor interface

>![NOTE]
>
> The enhancements to the Rule Editor, including custom event-based rules, support for dynamic variables, and API integration, are also available for Edge Delivery Services Forms. To learn more about these enhancements and how to use them, see the [Rule Editor Enhancements and Use Cases](/help/forms/rule-editor-enhancements-use-cases.md) article. 

**Best practices for function usage**:

- **Error handling**: Always include fallback behavior for function failures
- **Performance**: Profile functions with realistic data volumes  
- **Security**: Validate all inputs to prevent security vulnerabilities
- **Testing**: Create test cases covering normal and edge cases

+++


### Static Imports for Custom Functions

The Universal Editor's Rule Editor supports static imports, enabling you to organize reusable logic across multiple files and forms. Instead of keeping all custom functions in a single file (/blocks/form/functions.js), you can import functions from other modules. 
For example: Importing Functions from an External File
Consider the following folder structure:

```
      form
      ┣ commonLib
      ┃ ┗ functions.js
      ┣ rules
      ┃ ┗ _form.json
      ┣ form.js
      ┗ functions.js
```

You can import functions from `commonLib/functions.js` into your main `functions.js` file as shown below:

```
`import {days} from './commonLib/functions';
/**
 * Get Full Name
 * @name getFullName Concats first name and last name
 * @param {string} firstname in String format
 * @param {string} lastname in String format
 * @return {string}
 */
function getFullName(firstname, lastname) {
  return `${firstname} ${lastname}`.trim();
}

// Export multiple functions for use in Rule Editor
export { getFullName, days};
```

### Organizing Custom Functions Across Different Forms

You can create different sets of functions in separate files or folders and export them as required:
 
- If you want certain functions to be available only in specific forms, you can provide the path to the functions file in the form configuration.

- If the textbox for the path is left blank, the Rule Editor defaults to loading functions from `/blocks/form/functions.js`

![Custom Function in UE](/help/forms/assets/custom-function-in-ue.png){width=50%}

In the screenshot above, the path of the custom function is added in the Custom Function Path textbox. The custom functions for this form are loaded from the specified file (`cc_function.js`). 

This allows flexibility by sharing functions across multiple forms or keeping them isolated per form.

## Best practices for rule development


+++ Performance optimization

- Minimize rule complexity; split large logic into small, focused rules
- Order rules by frequency (most common first)
- Keep rule sets per component manageable
- Prefer reusable custom functions over duplicating logic

+++

+++ User experience

- Provide clear validation and inline feedback
- Avoid jarring visual changes; use show/hide thoughtfully
- Test across devices and layouts

+++

+++ Development hygiene

- Test with edge cases and known values
- Verify across browsers
- Document intent behind complex rules, not just mechanics
- Maintain a rule inventory for large forms
- Use consistent naming for components and rules
- Version custom functions and test in non-production environments

+++

## Troubleshooting common issues


+++ Rules not triggering

- Verify component names and references
- Check execution order (top to bottom)
- Validate conditions with known values
- Inspect browser console for blocking errors

+++

+++ Incorrect behavior

- Review operators and grouping (AND/OR)
- Test expression fragments individually
- Confirm data types (numbers vs strings)

+++

+++ Performance issues

- Simplify deeply nested conditions
- Profile custom functions
- Minimize external calls inside rules
- Use specific selectors and references

+++

+++ Custom function issues

- Confirm file path: `/blocks/form/functions.js`
- Ensure named exports are correct
- Confirm the build includes your changes
- Clear browser cache after deployment
- Validate parameter types and error handling

+++

+++ Universal Editor integration

- Confirm the Rule Editor extension is enabled
- Select a supported component
- Use a supported browser (Chrome, Firefox, Safari)
- Verify you have required permissions

## Important limitations

>[!IMPORTANT]
>
> Custom function constraints:
>
> - Static/dynamic imports are not supported
> - All logic must reside in `/blocks/form/functions.js`
> - Functions must be synchronous (no async/await or Promises)
> - Browser API access is limited

>[!WARNING]
>
> Production considerations:
>
> - Test thoroughly in staging
> - Monitor performance post-deploy
> - Have a rollback plan for rule issues
> - Consider slow networks and low-spec devices

## Summary

The Rule Editor in Universal Editor transforms static forms into intelligent, responsive experiences that adapt to user input in real-time. By leveraging conditional logic, automated calculations, and custom business rules, you can create sophisticated form workflows without writing application code.

**Key capabilities you've learned**:

- **Conditional logic**: Show and hide fields based on user input to create focused, relevant experiences
- **Dynamic calculations**: Automatically compute values (taxes, totals, rates) as users interact with the form
- **Data validation**: Implement real-time validation with clear, actionable feedback messages
- **Custom functions**: Extend capabilities with JavaScript for complex business logic and integrations
- **Performance optimization**: Apply best practices for maintainable, efficient rule development

**Value delivered**:

- **Enhanced user experience**: Reduce cognitive load with progressive disclosure and intelligent form flows
- **Reduced errors**: Prevent invalid submissions through real-time validation and guided input
- **Improved efficiency**: Automate calculations and data entry to minimize user effort
- **Maintainable solutions**: Create reusable, well-documented rules that scale across your organization

**Business impact**:

Forms become powerful tools for data collection, lead qualification, and user engagement. The Rule Editor enables non-technical authors to implement sophisticated business logic, reducing development costs while improving form completion rates and data quality.

+++

## Next steps

**Recommended learning path**:

1. **Start with basics**: Create simple show/hide rules to understand the core concepts
2. **Practice with tutorials**: Use the tax calculator example as a foundation for your own forms
3. **Expand gradually**: Add mathematical expressions and validation rules as your confidence grows
4. **Implement custom functions**: Develop JavaScript functions for specialized business requirements
5. **Optimize and scale**: Apply performance best practices and maintain rule documentation

**Additional resources**:

- [Universal Editor documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/universal-editor/introduction.html) for broader context
- [Extension Manager guide](/help/implementing/developing/extending/extension-manager.md) for enabling additional capabilities
- [Edge Delivery Services forms](/help/edge/docs/forms/overview.md) for comprehensive form development guidance

