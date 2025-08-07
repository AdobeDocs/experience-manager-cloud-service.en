---
title: This article outlines various use cases for the rule editor in an Adaptive Form based on Core Components.
description: This article explores various use cases for the rule editor in an Adaptive Form based on Core Components. It also highlights how custom functions can be used to create tailored rules for forms.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
---
# Rule Editor Enhancements and Use Cases

<span class="preview"> These are pre-release features available through our <a href="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/release-notes/prerelease.html#new-features">pre-release channel</a>.

This article introduces the latest enhancements to the rule editor in Adaptive Forms. These updates are designed to help you define form behavior more easily, without writing custom code, and to create more dynamic, responsive, and personalized form experiences.

The table below lists recent enhancements to the rule editor in Adaptive Forms, along with a brief description and the key advantages of each feature.:

| Enhancement    | Description     | Advantages|
|---|----|---|
| **Validation using the `validate()` method**     | Available in the function list to validate individual fields, panels, or the entire form.            | - Granular validation at panel, field, or form level  <br> - Better user experience with targeted error messaging <br> - Prevents progression with incomplete data <br> - Reduces form submission errors |
| **Download DOR**                                 | Out-of-the-box function available in the rule editor to download the Document of Record (DoR).        | - No custom development required for downloading DoR <br> - Consistent download experience across forms |
| **Dynamic variables**                            | Create rules using variables that change based on user input or other conditions.                     | - Enables flexible rule conditions <br> - Reduces need for duplicate logic <br> - Eliminates requirement to create hidden fields  |
| **Custom event-based rules**                     | Define rules that respond to custom events beyond the standard triggers.                              | - Supports advanced use cases <br> - Greater control over when and how rules are executed <br> - Enhances interactivity |
| **Context-aware repeatable panel execution**     | Rules now execute in the correct context for each repeated panel, instead of only the last instance.  | - Accurate rule application for each repeat instance <br> - Reduces errors in dynamic sections <br> - Improves user experience with repeated content |
| **Support for query string, UTM, and browser parameters** | Create rules that adapt form behavior based on URL parameters or browser-specific values.        | - Enables personalization based on source or environment <br> - Useful for marketing or tracking-specific flows <br> - No need for extra scripting or customization |

Let's now explore each method in detail with specific use cases to help you understand how these features can be used to deliver a personalized experience for users
 
## Validate Method in Function List

Enhanced validation capabilities allowing the **validate()** method to be used in the function list to validate panels, fields, or entire forms. For example, in a multi-step loan application form, you need to validate different sections before allowing users to proceed to the next step.

**Scenario:** A financial institution offers a multi-step loan application form where users must complete different sections such as:

* Personal Details
* Employment Details
* Loan Details
* Review & Submit

Before a user moves from one step to the next, the form must validate only the fields within the current section. For example, the user should not be allowed to proceed to "Employment Details" unless all required fields in "Personal Details" are correctly filled.

**Implementation using validate() in the Rule Editor**

A **Next** button in each panel triggers a rule using the **validate()** method. The rule checks if all fields in the current panel are valid. If validation passes, the form navigates to the next panel. If not, error messages are displayed, guiding the user to correct the input.

The screenshot below displays the rule applied to the **Next** button:

![Validate Next Button](/help/forms/assets/validate-next.png)

In the above rule, the **Next** button checks whether the fields in the **Personal Details** section are valid. If the details are not valid, the focus moves to the **Name** field in the **Personal Details** panel.

![output](/help/forms/assets/valid-output.png)

>[!NOTE]
>
> You can use the **validate()** method on forms, fragments, or individual fields. When a fragment is included in a form, both the form and the fragment appear as options in the validation context. In this case, the fragment refers to the fields within it, while the form refers to the parent form where the fragment is embedded.

## DownloadDor as OOTB fuction in Rule Editor

Using the  **DownloadDor()** out-of-the-box (OOTB) function in the Rule Editor, allows user to download the Document of Record , if the form is configured to generate Document of Recored. 

>[!NOTE]
>
> If the form is not configured for Document of Record, an error message is displayed when the rule using the **downloadDoR()** function is applied to the button.

**Scenario**: A government agency provides a digital application form for issuing certificates. After submitting the form, applicants often require a copy of the completed form for their records or to share with another department. To improve the user experience, the agency wants to give applicants the option to download a Document of Record (DoR) immediately after submission or at any stage before final submission.

**Implementation using DownloadDor() in the Rule Editor**

A **Download** button is added to form using the Rule Editor, a rule is configured to trigger the **DownloadDor()** function when the button is clicked.

The screenshot below displays the rule applied to the **Download** button:

![Download Button rule](/help/forms/assets/download-button-rule.png)

>[!NOTE]
>
> The **Input** field allows the user to specify the file name for a downloadable document. This is an optional parameter.

If the form is configured for DoR generation, this function generates and downloads the PDF instantly, without requiring any custom function.

![Document of Record](/help/forms/assets/download-dor-output.png)

## Support for Dynamic Variables in Rules

The enhanced rule editor now supports the creation and use of dynamic (temporary) variables. These variables can be set and retrieved throughout the form's lifecycle using the built-in **Set Variable Value** and **Get Variable Value** functions.
These variables:

* Are not submitted with the form data.
* Can hold intermediate or calculated values.
* Can be used in conditional logic and actions.

**Scenario**: An e-commerce company provides an order form where users can select a product and a preferred shipping method. While product price is captured through a form field, shipping cost is determined dynamically based on the selected method and the country chosen.

To keep the form structure clean and avoid adding unnecessary hidden fields, the business wants to handle shipping cost as a temporary value that supports real-time calculation of the total amount.

**Implementation using Set Variable Value and Get Variable Value functions in the Rule Editor**

A rule is configured to set a temporary variable named **extracharge** using the **Set Variable Value** function. The value of this variable depends on the selected country. For example, if the user selects "United States," the value is set to 50. For any other country, it is set to 100.

![Set variable value](/help/forms/assets/setvalue.png)

Later, when calculating the total shipment cost, the **Get Variable Value** function retrieves the **extracharge** value based on the selected country. 

![Get variable value](/help/forms/assets/getvalue.png)

This value is then added to the product's shipping cost, and the result is displayed in the **Total Shipment Cost** field.

![output](/help/forms/assets/getsetvalue-output.png)

This approach allows you to calculate and display additional charges dynamically without storing them in a visible field, enabling a clean, responsive, and code-free user experience.


## Custom Event Based Rules Support

The enhanced rule editor supports custom event handling using the **Dispatch Event** and **On Trigger Event** functions. These functions allow different parts of the form to communicate by emitting and listening to custom events, enabling cleaner, modular logic without tightly coupling actions to specific fields.

**Scenario**: A job application form is integrated with an external HR system that performs background verification. Once the check is complete, the system updates the form with the **Background Verification Complete!** message. The form must dynamically adjust what the applicant sees based on this result.

Instead of binding logic directly to the field receiving the status, the form uses a custom event-based approach to improve modularity and maintainability.

**Implementation using Dispatch Event and On Trigger Event**

When the background check status is updated, a rule uses **Dispatch Event** to emit a custom event as **bgvmsg** along with the status outcome. A separate rule listens for this event using **On Trigger Event**.

The screenshots below display the rules applied to the "Is Background Verification Complete?" radio button and the "bgvmsg" text field.

![dispatch event](/help/forms/assets/dispatch-event-rule.png)

![on trigger event](/help/forms/assets/trigger-event-rule.png)

When the event is detected, it checks the status and updates the form accordingly. For example:

* If the background check is passed, the form displays a confirmation message.
* If additional documents are needed, the form displays a section asking the applicant to upload the required information, along with an alert message.

![Dispatch event output](/help/forms/assets/dispatch-trigger-output.png)

Support for custom events allowing developers to create and trigger custom events that can be used as conditions in rule editor.

## Context-Based Rule Execution for Repeatable Panels

Adaptive Forms support context-aware rule execution for repeatable panels. This allows rules to apply specifically to the panel instance where the user interacts, rather than affecting all instances or defaulting to the last one.

**Scenario**: A product order form lets users add multiple products in separate panels. Each panel includes a **Number of Product** field and a **Total Cost** field. When a user updates the quantity for a product, the form should recalculate the total price, but only for that specific panel, not for all others.

**Implementation using Context-Aware Rules in the Rule Editor**

A rule is configured on the **Number of Product** field inside the repeatable product panel. 

The below screenshot displays the rule for the **Number of Product** field inside the repeatable product panel:

![number of product rule](/help/forms/assets/number-of-product-rule.png)

When the quantity is changed, the rule fetches the unit price of the selected product and calculates the total cost for that panel only. 

![Context aware rule output](/help/forms/assets/context-aware-rule-output.png)

## URL and Browser Parameter-Based Rules in Adaptive Forms

Adaptive Forms support dynamic rule execution using external parameters passed through the form URL or derived from the user's browser environment. This enables personalized and context-aware form experiences based on where the visitor came from or what device they're using.

## Allowed Parameter Types

| Parameter Type    | Supported Options   | Description  | Example Value |
| --- | --- | --- | ---|
| Query Parameter   | `ref` (only string values)                                          | Generic key-value pair in the URL after `?`         | `?ref=partner123`                          |
| UTM Parameter     | UTM Source<br>UTM Medium<br>UTM Campaign<br>UTM Term<br>UTM Content | Special query parameters used for campaign tracking | `?utm_source=google&utm_medium=email`      |
| URL Parameter     | Host name<br>Path                                                   | Extracts structural components of the form URL      | `hostname=www.example.com`, `path=/signup` |
| Browser Parameter | Browser Agent<br>Browser Language<br>Browser Platform               | Values derived from the user's browser or device    | `Browser Agent=Mozilla`, `Language=en-US`  |

**Scenario**: A lead generation form needs to tailor its welcome message depending on the traffic source. When a user lands on the form through a Google ad campaign (using utm_source=google in the URL), the form should show a custom greeting.

**Implementation using UTM Parameter**

A rule is configured on a text field that displays custom message to Google users and it uses **utm_source** parameter. 

The below screenshot displays the rule configured on text message:

![rule on text message](/help/forms/assets/utm-param-rule.png)

If the **utm_source** parameter value equals "google", a custom message as "Hello Google users, welcome to the Campaign Ad!" is shown.

![utm-param-output](/help/forms/assets/utm-param-output.png)

This allows marketers to deliver relevant content to users based on the campaign that brought them to the form without requiring manual field input or custom scripting.

These enhancements significantly expand the capabilities of the Adaptive Forms Rule Editor, providing developers with powerful tools to create more dynamic, interactive, and intelligent forms. Each enhancement addresses specific business needs while maintaining the ease-of-use that makes the Rule Editor accessible to both technical and non-technical users.