---
title: How can we improve the performance of large forms with lazy loading?
description: Learn about how to improve performance of large forms with lazy loading. Lazy loading significantly improves the performance of large and complex Adaptive Forms by deferring initialization and loading of form fragments until they are visible.
feature: Adaptive Forms, Foundation Components
role: User, Developer
level: Intermediate
exl-id: 0cd38edb-2201-4ca6-8b84-6b5b7f76bd90
---
# Improve performance of large forms with lazy loading{#improve-performance-of-large-forms-with-lazy-loading}

>[!NOTE]
>
> Adobe recommends using the modern and extensible data capture [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) for [creating new Adaptive Forms](/help/forms/creating-adaptive-form-core-components.md) or [adding Adaptive Forms to AEM Sites pages](/help/forms/create-or-add-an-adaptive-form-to-aem-sites-page.md). These components represent a significant advancement in Adaptive Forms creation, ensuring impressive user experiences. This article describes older approach to author Adaptive Forms using foundation components.

| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-advanced-authoring/lazy-loading-adaptive-forms.html)                  |
| AEM as a Cloud Service     | This article        |


## Introduction to lazy loading {#introduction-to-lazy-loading}

When form become large and complex with hundreds and thousands of fields, end users experience long response time when rendering forms at runtime. To minimize the response time, Adaptive Forms lets you break forms into logical fragments and configure to defer initialization or loading of fragments until the fragment must be visible. It is referred to as lazy loading. In addition, the fragments configured for lazy loading are unloaded once user navigates to other sections in the form and the fragments are no longer visible.

Let's first understand the requirements and preparatory steps before you configure lazy loading.

## Preparing to configure lazy loading {#preparing-to-configure-lazy-loading}

Before you configure lazy loading of fragments in your Adaptive Form, it is important you define strategies to create fragments, identify values that are used in scripts or referred in other fragments, and define rules to control visibility of fields in lazily loaded fragments.

* **Identify and create fragments** 
  You can configure only Adaptive Form Fragments for lazy loading. A fragment is a stand-alone segment that resides outside an Adaptive Form and can be reused across forms. So, the first step toward implementing lazy loading is to identify logical sections in a form and convert them into fragments. You can create a fragment from scratch or save an existing form panel as fragment.  
  
  <!--For more information about creating fragments, see [Adaptive Form Fragments](adaptive-form-fragments.md).-->

* **Identify and mark global values** 
  Forms-based transactions involve dynamic elements to capture relevant data from users and process it to simplify form filling experience. For example, your form has field A in fragment X whose value determines the validity of field B in another fragment. In this case, if fragment X is marked for lazy loading, the value of field A must be available to validate field B even when fragment X is not loaded. To achieve this, you can mark field A as global, which ensures that its value is available for validating field B when fragment X is not loaded.  
  
  For information about how to make a field value global, see [Configuring lazy loading](lazy-loading-adaptive-forms.md#p-configuring-lazy-loading-p).

* **Write rules to control visibility of fields** 
  Forms include some fields and sections that are not applicable to all users and in all conditions. Forms authors and developers use visibility or show-hide rules to control their visibility based on user inputs. For example, the Office Address field is not shown to the users who choose Unemployed in the Employment Status field in a form. For more information about writing rules, see [Using rule editor](rule-editor.md).  
  
  You can use visibility rules in the lazily loaded fragments so that conditional fields are shown only when they are required. Also, mark the conditional field global to refer to it in the visibility expression of the lazily loaded fragment.

## Configuring lazy loading {#configuring-lazy-loading}

Perform the following steps to enable lazy loading on an Adaptive Form Fragment:

1. Open the Adaptive Form in authoring mode that contains the fragment you want to enable for lazy loading.
1. Select the Adaptive Form Fragment and select ![configure](assets/configure-icon.svg).
1. In the sidebar, enable **[!UICONTROL Load fragment lazily]** and select **Done**.

   ![Enable lazy loading for the Adaptive Form Fragment](assets/lazy-loading-fragment.png)

   The fragment is now enabled for lazy loading.

You can mark the values of objects in the lazily loaded fragment as global so that they are available for use in scripts when the containing fragment is not loaded. Do the following:

1. Open the Adaptive Form Fragment in authoring mode.
1. Select the field whose value you want to mark as global, and then select ![configure](assets/configure-icon.svg).
1. In the sidebar, enable **[!UICONTROL Use value during lazy loading]**.

   ![Lazy loading field in sidebar](assets/enable-lazy-loading.png)

   The value is now marked as global and is available for use in scripts even when the containing fragment is unloaded.

## Considerations and best practices for configuring lazy loading {#considerations-and-best-practices-for-configuring-lazy-loading}

Some limitations, recommendations, and important points to keep in mind when working with lazy loading are as follows:

* Adobe recommends using XSD schema-based Adaptive Forms over XFA-based Adaptive Forms for configuring lazy loading on large forms. The performance gain due to lazy loading implementation in XFA-based Adaptive Forms is relatively less than gain in XSD-based Adaptive Forms.
* Do not configure lazy loading on fragments in an Adaptive Form that use **[!UICONTROL Responsive -everything on one page without navigation]** layout for the root panel. As a result of the Responsive layout configuration, all fragments load simultaneously in an Adaptive Form. It can also result in degraded performance.
* It is recommended not to configure lazy loading on fragments in the first panel that renders on loading the Adaptive Form.
* Lazy loading is supported up to two levels in the fragment hierarchy.
* Ensure that fields marked as global are unique across an Adaptive Form.
* Consider writing visibility rules for fragments that should show or hide based on a condition. For example, you can show or hide the Spouse Details fragment based on the marital status specified by a user. 
* File attachment and Terms and conditions components are not supported in lazily loaded fragments.

### Scripting best practices for configuring lazy loading {#scripting-best-practices-for-configuring-lazy-loading}

Important points to keep in mind while developing scripts for lazy loading panels are as follows:

* Ensure that initialize and calculate scripts used on the fields of a lazy loaded fragment are idempotent in nature. Idempotent scripts are those which have same effect even after multiple executions.
* Use the globally available property of fields to make value of fields located in a lazy loading panel available to all other panels of a form.
* Do not forward reference value of a field inside a lazy panel irrespective of field being marked globally across fragments or not.
* Use panel reset feature to reset everything visible on the panel by using the following click expression.  
  guideBridge.resolveNode(guideBridge.getFocus({"focusOption": "navigablePanel"})).resetData()


## See Also {#see-also}

{{see-also}}