---
title: This article outlines various use cases for the rule editor in an Adaptive Form based on Core Components.
description: This article explores various use cases for the rule editor in an Adaptive Form based on Core Components. It also highlights how custom functions can be used to create tailored rules for forms.
feature: Adaptive Forms, Core Components
role: User, Developer
level: Beginner, Intermediate
---
# Rule Editor Enhancements and Use Cases

This article introduces the latest enhancements to the rule editor in Adaptive Forms. These updates are designed to help you define form behavior more easily, without writing custom code, and to create more dynamic, responsive, and personalized form experiences.

The table below lists recent enhancements to the rule editor in Adaptive Forms, along with a brief description and the key advantages of each feature.:

| Enhancement    | Description     | Advantages|
|---|----|---|
| **Validation using the `validate()` method**     | Available in the function list to validate individual fields, panels, or the entire form.            | - Granular validation at panel, field, or form level  <br> - Better user experience with targeted error messaging <br> - Prevents progression with incomplete data <br> - Reduces form submission errors |
| **Download DOR**                                 | Out-of-the-box function available in the rule editor to download the Document of Record (DoR).        | - No custom development required for downloading DoR <br> - Consistent download experience across forms <br> - Supports various file types and dynamic URLs <br> - Integrated with form workflow |
| **Dynamic variables**                            | Create rules using variables that change based on user input or other conditions.                     | - Enables flexible rule conditions <br> - Reduces need for duplicate logic <br> - Improves maintainability |
| **Custom event-based rules**                     | Define rules that respond to custom events beyond the standard triggers.                              | - Supports advanced use cases <br> - Greater control over when and how rules are executed <br> - Enhances interactivity |
| **Context-aware repeatable panel execution**     | Rules now execute in the correct context for each repeated panel, instead of only the last instance.  | - Accurate rule application for each repeat instance <br> - Reduces errors in dynamic sections <br> - Improves user experience with repeated content |
| **Support for query string, UTM, and browser parameters** | Create rules that adapt form behavior based on URL parameters or browser-specific values.        | - Enables personalization based on source or environment <br> - Useful for marketing or tracking-specific flows <br> - No need for extra scripting or customization |

Let's now explore each method in detail with specific use cases to help you understand how these features can be used to deliver a personalized experience for users
 
## Validate Method in Function List

Enhanced validation capabilities allowing the validate() method to be used in the function list to validate panels, fields, or entire forms. For example, in a multi-step loan application form, you need to validate different sections before allowing users to proceed to the next step.

**Scenario:** A financial institution offers a multi-step loan application form where users must complete different sections such as:

* Personal Details
* Employment Information
* Loan Details
* Review & Submit

Before a user moves from one step to the next, the form must validate only the fields within the current section. For example, the user should not be allowed to proceed to "Employment Information" unless all required fields in "Personal Details" are correctly filled.

**Implementation using validate() in the Rule Editor**

A **Next** button in each panel triggers a rule using the **validate()** method. The rule checks if all fields in the current panel are valid. If validation passes, the form navigates to the next panel. If not, error messages are displayed, guiding the user to correct the input.




## DownloadDor as OOTB fuction in Rule Editor

Using the  DownloadDor() out-of-the-box (OOTB) function in the Rule Editor, allows user to download the Document pf Record , if the form is configured to generate Document pf Recored. 

**Scenario**: A government agency provides a digital application form for issuing certificates. After submitting the form, applicants often require a copy of the completed form for their records or to share with another department. To improve the user experience, the agency wants to give applicants the option to download a Document of Record (DoR) immediately after submission or at any stage before final submission.

**Implementation using DownloadDor() in the Rule Editor**

A Download button is added to the confirmation panel. Using the Rule Editor, a rule is configured to trigger the **DownloadDor()** function when the button is clicked.

If the form is configured for DoR generation, this function generates and downloads the PDF instantly, without requiring any custom function.

##  Support for Dynamic Variables in Rules

Enhanced rule editor supporting dynamic variables that can be created, modified, and used throughout the form lifecycle.

### Use Case Scenario
Creating complex calculations and conditional logic that depend on multiple form inputs and external data sources.

### Adaptive Form Example
**Scenario:** E-commerce order form with dynamic pricing, taxes, and shipping calculations.

**Rule Implementation:**
```javascript
// Rule: Initialize dynamic variables
When: Form loads
Then:
  Create variable "basePrice" = 0
  Create variable "taxRate" = 0.08
  Create variable "shippingCost" = 0
  Create variable "totalAmount" = 0

// Rule: Calculate dynamic pricing
When: NumericField "Quantity" value changes OR DropDown "ProductType" value changes
Then:
  Set variable "basePrice" = NumericField "Quantity" * getProductPrice(DropDown "ProductType")
  Set variable "shippingCost" = calculateShipping(DropDown "ShippingMethod", variable "basePrice")
  Set variable "totalAmount" = variable "basePrice" + (variable "basePrice" * variable "taxRate") + variable "shippingCost"
  Set value of NumericField "TotalAmount" = variable "totalAmount"
```

**Advanced Example:**
```javascript
// Rule: Dynamic discount calculation
When: TextField "PromoCode" value changes
Then:
  Set variable "discountPercent" = validatePromoCode(TextField "PromoCode")
  If variable "discountPercent" > 0
    Set variable "discountAmount" = variable "basePrice" * (variable "discountPercent" / 100)
    Set variable "totalAmount" = variable "totalAmount" - variable "discountAmount"
    Show(TextField "DiscountApplied")
    Set value of TextField "DiscountApplied" = "Discount: $" + variable "discountAmount"
```

**Benefits:**
- Complex calculations without multiple hidden fields
- Improved form performance
- Reusable variables across multiple rules
- Dynamic content generation

---

## 4. Custom Event Based Rules Support

### Description
Support for custom events allowing developers to create and trigger custom events that can be used as conditions in rule editor.

### Use Case Scenario
Integration with external systems and creation of complex form workflows that respond to custom business events.

### Adaptive Form Example
**Scenario:** Job application form that integrates with external HR systems and responds to custom approval workflows.

**Rule Implementation:**
```javascript
// Rule: Custom event for background check completion
When: Custom event "backgroundCheckComplete" is triggered
Then:
  If eventData.status == "passed"
    Show(Panel "FinalApproval")
    Set value of TextField "BackgroundStatus" = "✓ Background Check Passed"
    Set property of TextField "BackgroundStatus".style = "color: green"
  Else
    Show(Panel "AdditionalDocuments")
    Set value of TextField "BackgroundStatus" = "⚠ Additional Documentation Required"
```

**Integration Example:**
```javascript
// Rule: Custom event for real-time validation
When: Custom event "creditScoreUpdated" is triggered
Then:
  Set variable "creditScore" = eventData.score
  If variable "creditScore" >= 700
    Show(Panel "PremiumOptions")
    Set value of TextField "LoanStatus" = "Pre-approved for premium rates"
  Else If variable "creditScore" >= 600
    Show(Panel "StandardOptions")
  Else
    Show(Panel "AlternativeOptions")
    Trigger custom event "requireCosigner"
```

**Benefits:**
- Real-time integration with external systems
- Event-driven form behavior
- Improved user experience with instant feedback
- Flexible workflow management

---

## 5. Context-Based Repeatable Panel Rules Execution

### Description
Enhanced rule execution for repeatable panels that considers the context of each panel instance rather than defaulting to the last panel instance.

### Use Case Scenario
Order forms with multiple line items where each item has its own calculation rules and validation logic.

### Adaptive Form Example
**Scenario:** Purchase order form where users can add multiple products, each with independent pricing and availability rules.

**Rule Implementation:**
```javascript
// Rule: Product-specific calculations for each repeatable panel instance
When: NumericField "Quantity" value changes in Panel "ProductLine[context]"
Then:
  // Context-aware rule execution for current panel instance
  Set variable "unitPrice" = getProductPrice(DropDown "Product[context]")
  Set variable "lineTotal" = NumericField "Quantity[context]" * variable "unitPrice"
  Set value of NumericField "LineTotal[context]" = variable "lineTotal"
  
  // Check inventory for this specific product
  If NumericField "Quantity[context]" > getInventory(DropDown "Product[context]")
    Show(TextField "InventoryWarning[context]")
    Set value of TextField "InventoryWarning[context]" = "Only " + getInventory(DropDown "Product[context]") + " items available"
  Else
    Hide(TextField "InventoryWarning[context]")
```

**Advanced Context Example:**
```javascript
// Rule: Dynamic shipping calculation per product line
When: DropDown "ShippingMethod" value changes in Panel "ProductLine[context]"
Then:
  Set variable "productWeight" = getProductWeight(DropDown "Product[context]")
  Set variable "shippingCost[context]" = calculateShipping(
    DropDown "ShippingMethod[context]", 
    variable "productWeight", 
    NumericField "Quantity[context]"
  )
  Set value of NumericField "ShippingCost[context]" = variable "shippingCost[context]"
  
  // Update total shipping cost
  Trigger custom event "updateTotalShipping"
```

**Benefits:**
- Accurate calculations for each repeatable instance
- Independent validation per panel instance
- Improved data integrity
- Better user experience with contextual feedback

---

## 6. Query/UTM/Browser Parameter Based Rules Support

### Description
Support for creating rules based on URL query parameters, UTM parameters, and browser parameters, enabling dynamic form behavior based on external context.

### Use Case Scenario
Marketing campaign forms that adapt their content and behavior based on traffic source, campaign parameters, and user context.

### Adaptive Form Example
**Scenario:** Lead generation form that customizes content based on marketing campaign source and user referral data.

**Rule Implementation:**
```javascript
// Rule: Campaign-specific form customization
When: Form loads
Then:
  Set variable "campaignSource" = getURLParam("utm_source")
  Set variable "campaignMedium" = getURLParam("utm_medium")
  Set variable "referralCode" = getURLParam("ref")
  
  If variable "campaignSource" == "google"
    Set value of TextField "WelcomeMessage" = "Welcome Google visitor! Special offer inside."
    Show(Panel "GoogleSpecialOffer")
  Else If variable "campaignSource" == "facebook"
    Set value of TextField "WelcomeMessage" = "Facebook friends get exclusive benefits!"
    Show(Panel "SocialMediaDiscount")
  
  If variable "referralCode" != null
    Show(Panel "ReferralBonuses")
    Set value of TextField "ReferralMessage" = "Thanks for the referral from: " + variable "referralCode"
```

**Browser-Based Rules:**
```javascript
// Rule: Device-specific form optimization
When: Form loads
Then:
  Set variable "userAgent" = getBrowserParam("userAgent")
  Set variable "screenWidth" = getBrowserParam("screenWidth")
  
  If variable "screenWidth" < 768
    Hide(Panel "DetailedInstructions")
    Show(Panel "MobileOptimizedInstructions")
    Set property of Button "Submit".text = "Submit"
  Else
    Set property of Button "Submit".text = "Submit Application"
  
  If variable "userAgent".contains("Mobile")
    Set property of FileUpload "Documents".accept = "image/*"
    Show(TextField "MobileUploadTip")
```

**UTM Tracking Integration:**
```javascript
// Rule: UTM parameter tracking and form pre-population
When: Form loads
Then:
  Set variable "utmCampaign" = getURLParam("utm_campaign")
  Set variable "utmContent" = getURLParam("utm_content")
  
  // Pre-populate hidden fields for analytics
  Set value of HiddenField "TrackingCampaign" = variable "utmCampaign"
  Set value of HiddenField "TrackingContent" = variable "utmContent"
  
  // Customize form based on campaign
  If variable "utmCampaign" == "summer2024"
    Show(Panel "SummerPromotion")
    Set value of NumericField "DiscountPercent" = 15
  Else If variable "utmCampaign" == "blackfriday"
    Show(Panel "BlackFridayDeal")
    Set value of NumericField "DiscountPercent" = 25
```

**Benefits:**
- Personalized form experiences based on traffic source
- Automatic campaign tracking and attribution
- Dynamic content based on external parameters
- Improved conversion rates through targeted messaging
- Better analytics and marketing insights

---



These six enhancements significantly expand the capabilities of the Adaptive Forms Rule Editor, providing developers with powerful tools to create more dynamic, interactive, and intelligent forms. Each enhancement addresses specific business needs while maintaining the ease-of-use that makes the Rule Editor accessible to both technical and non-technical users.

The combination of these features enables the creation of sophisticated form experiences that can adapt to user context, integrate with external systems, and provide rich interactive functionality without requiring extensive custom development.
