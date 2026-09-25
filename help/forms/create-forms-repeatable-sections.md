---
title: How to create repeatable panels in Adaptive Form Core Components?
description: Learn to create repeatable section or fields in an Adaptive Form.
role: Developer, Developer, Admin, User
feature: Adaptive Forms, Core Components
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 02521bf3-83c1-40a0-8fe6-23af240727e9
---
# Create forms with repeatable sections (Core Components) {#repeat-panel}


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/creating-forms-repeatable-sections.html?lang=en)                  |
| AEM as a Cloud Service     | This article        |

A **repeatable section** is a part of a form that a user duplicates multiple times to collect information for multiple instances of the same data. In an Adobe Experience Manager (AEM) **Adaptive Form**, repeatable sections let a single component pattern be reused dynamically at runtime, so the form grows to accommodate as many entries as the user needs.

For example, consider a form used to collect information about a person's work experience. The form includes a repeatable section for capturing the details of each previous job. The repeatable section typically contains fields such as **company name**, **job title**, **dates of employment**, and **job responsibilities**. The user adds multiple instances of the repeatable section to enter information about each job they have held. This eliminates the need to predefine a fixed number of fields, because the form expands on demand to match the exact number of data entries required.

   ![Repeatability](/help/forms/assets/repeatable-adaptive-form-example.gif)

By the end of this article, you learn to:

* Create a repeatable section in an Adaptive Form
* Set minimum or maximum number of repetitions for an Adaptive Form component
* Use rule editor to configure addition or deletion actions for repeatable sections

You can use the [**Panel**](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel), [**Accordion**](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion.html), [**Horizontal Tabs**](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs.html), [**Vertical Tabs**](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs) or [**Wizard**](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard.html) components to make sections of an Adaptive Form repeatable. Form authors add child components to these container components to create a repeatable section within a form. Because each of these components acts as a container, any fields placed inside them repeat together as a single logical unit.


Examples in this document are based on the [**Panel**](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) component. You can perform the identical steps to make the [**Panel**](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel), [**Accordion**](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion.html), [**Horizontal Tabs**](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs.html), [**Vertical Tabs**](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs) or [**Wizard**](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard.html) components repeatable.

## Add or delete repeatable sections in a form {#add-or-delete-repeatable-section-in-panel-container}

A **repeatable section**, also called a **repeatable panel** or **panel container**, is a group of form fields that a user can duplicate or remove at runtime, allowing a single form to collect a variable number of similar entries. This capability is essential whenever the number of entries is not known in advance—for example, when a user must enter multiple addresses, list several dependents, add line items to an order, or provide details for an unlimited set of similar records.

To create this behavior, a form author makes a panel repeatable and adds a **button component** that adds or removes an **instance** of the panel directly within the form. Each added instance reproduces the panel's fields as an independent, separately captured section, while a delete action removes a selected instance. This gives end users full control over how many copies of the section appear, ensuring the form adapts to their specific data without requiring the author to predefine a fixed number of fields.

To add or delete repeatable sections (panels) in a form:

* [Make panel container repeatable](#make-panel-container-repeatable)
* [Add repeatable section](#add-repeatable-section-using-instance-manager-via-scripts)
* [Delete repeatable sections](#delete-repeatable-section-using-instance-manager-via-scripts)

### Make Panel Container repeatable {#make-panel-container-repeatable}

![Accessibility tab](/help/forms/assets/repeat-panel.png)

A repeatable panel container lets users add multiple instances of the same set of fields within a form, which is useful when the number of entries is not fixed—such as listing multiple dependents, addresses, or line items. To make a panel repeatable, perform the following steps:

1. Select a panel container and select ![cmppr](/help/forms/assets/cmppr.png).
1. Click the **repeat panel** and switch on the toggle to **make panel repeatable**.
1. Set **minimum repetitions** to define the minimum number of repeatable sections that must appear in the form. Setting **minimum repetitions** to **zero** means the panel does not repeat by default and allows the repeated panels to be removed entirely, so the panel behaves as non-repeating unless the user adds an instance. By default, the value of **minimum repetitions** is **zero**.
1. Set **maximum repetitions** to control the highest number of times the panel can repeat. This caps how many instances a user can add, preventing unlimited entries when a fixed upper limit is required. By default, the value is **infinite**, allowing the panel to repeat without restriction.

   >[!NOTE]
   >
   >
   > * Minimum repetition cannot be a negative value.
   > * To create a non-repeatable panel, set the value of both the maximum and minimum fields to **one**.

### Add repeatable section using instance manager (via scripts) {#add-repeatable-section-using-instance-manager-via-scripts}

The parent panel of the repeatable panel must contain an **Add** button to manage the repeat instances of the panel. The **instance manager** is the object that controls how many copies (instances) of a panel appear in the form, allowing users to dynamically add sections at runtime. Perform the following steps to insert buttons into the parent panel and attach scripts to those buttons, so that clicking a button triggers the addition of a new panel instance:

1. Add a **button component** to the parent of the panel. In the example video below, a button component with the label name **Add** and field name **AddPanel** is used. Select the component and select ![edit-rules](/help/forms/assets/edit-rules.png). The rules of the button component open in the rule editor.
1. In the Rule Editor window, click **Create**. The Rule Editor provides two authoring modes—**Visual Editor** and **Code Editor**—which let you define the button behavior either visually or through scripting.

    Select **Visual Editor** in the Form Objects and Functions row.

    1. In the rule area, under **WHEN**, select the state **is clicked**. This defines the trigger event for the rule.
    1. Under **THEN**, select **Add Instance**, and drag-drop the panel using ![toggle-side-panel](/help/forms/assets/toggle-side-panel.png) or select it using **Drop object or select here.** This binds the click event to the action of adding a new instance of the specified panel.

    Alternatively, select **Code Editor** in the Form Objects and Functions row. Click **Edit Rules** and in the code area:

    * To create an add panel button, specify `this.panel.instanceManager.addInstance()`. This call invokes the **instanceManager** of the target panel and appends a new instance each time the button is clicked, which is what makes the section repeatable.

    Click **Done** to save and apply the rule.

>[!VIDEO](https://video.tv.adobe.com/v/3421052/adaptive-forms-repeatable-sections-repeat-sections/?quality=12&learn=on)

### Delete repeatable sections using instance manager (via scripts) {#delete-repeatable-section-using-instance-manager-via-scripts}

The parent of the panel should contain a delete button to delete an instance of the repeatable panels. The **Instance Manager** governs how repeatable panels are added and removed, so every deletion action routes through its methods. Perform the following steps to insert buttons to the parent and enable scripts on the buttons to delete repeatable panels:

1. Add a **button component** to the parent of the panel. In the video below, a button component with the label name **delete** and field name **DeletePanel** is used. Select the component and select ![edit-rules](/help/forms/assets/edit-rules.png). The rules of the button component open in the rule editor.
1. In the Rule Editor window, click **Create**.

    Select **Visual Editor** in the Form Objects and Functions row.

    1. In the rule area, under WHEN **DeletePanel**, select state **is clicked**.
    1. Under THEN, select **Remove Instance**, and drag-drop the panel using ![toggle-side-panel](/help/forms/assets/toggle-side-panel.png) or select it using **Drop object or select here.**

    Select **Code Editor** in the Form Objects and Functions row. Click **Edit Rules** and in the code area:

    * To create a delete panel button, specify `this.panel.instanceManager.removeInstance(this.panel.instanceIndex)`. This calls the **removeInstance** method on the panel's Instance Manager, passing the current `instanceIndex` so that the specific clicked instance is removed rather than any other repeated copy.

    Click **Done**.

>[!VIDEO](https://video.tv.adobe.com/v/3421620/adaptive-forms-repeatable-sections)

>[!NOTE]
>
>If a field belongs to a repeatable panel, you cannot access it directly using its name in your scripts, because each repeated copy shares the same field name. To access the field, specify the repeatable instance to which the field belongs using the **`instances`** Application Programming Interface (API) in **`InstanceManager`**. The Instance Manager tracks every repeated copy of a panel as an indexed instance, and the `instances` API returns the array of those copies. The syntax to use the `instances` API in `InstanceManager` is:
>
>
>`<panelName>.instanceManager.instances[<instanceNumber>].<fieldname>`
>
>
>For example, you create an adaptive form with a repeatable panel having a text box. When you pre-fill the form with three repeatable text boxes, you need the Extensible Markup Language (XML) below:
>
>
>`<panel1><textbox1>AA1</panel1></textbox1>`
>
>
>`<panel1><textbox1>AA2</panel1></textbox1>`
>
>
>`<panel1><textbox1>AA3</panel1></textbox1>`
>
>
>To read AA1 data, specify:
>
>
>`Panel1.instanceManager.instances[0].textbox.value`
>
>
>To read AA2 data, specify:
>
>
>`Panel1.instanceManager.instances[1].textbox.value`
>
>
>Because the index is zero-based, instance `[0]` returns the first repeated copy and instance `[1]` returns the second.
>
>

>[!NOTE]
>
> When all instances of a panel are removed from an adaptive form, you can no longer reference the panel by its live instance, so to add an instance of the removed panel you must use the **`_panelName`** syntax to capture the Instance Manager of the panel. As a result, once the Instance Manager is captured, use the **`addInstance`** API of the Instance Manager to add the deleted instance back. For example, `'_panelName.addInstance()'` adds an instance of the removed panel.

## Using repeating subforms from Form Template (XDP/XSD) {#using-repeating-subforms-from-form-template-xdp-xsd}

A repeating subform in a Form Template functions similarly to repeatable panels in Adaptive Forms, allowing a defined block of fields to render once for each matching data item. Form Templates are authored in **XML Data Package (XDP)** or **XML Schema Definition (XSD)** formats. In AEM Forms Designer, perform the following steps to create a repeating subform:

1. In the Hierarchy palette, select the parent subform of the subform you want to repeat.
1. In the Object palette, click the Subform tab, and in the Content list, select **Flowed**. This ensures the parent subform can dynamically expand to accommodate repeated instances.
1. Select the subform to repeat.
1. In the Object palette, click the Subform tab and, in the Content list, select either **Positioned** or **Flowed**.
1. Click the Binding tab and select **Repeat Subform For Each Data Item**. This binds the subform to the data structure so that one instance renders for every matching data entry.
1. To specify the minimum number of repetitions, select **Min Count** and type a number in the associated box. When Min Count is set to 0 and no data is provided at data-merge time, the subform is omitted entirely from the rendered form.
1. To specify the maximum number of subform repetitions, select **Max** and type a number in the associated box. Leaving the Max box empty allows unlimited subform repetitions, because no upper bound constrains the number of instances rendered.
1. To specify a set number of subform repetitions, regardless of the quantity of data, select **Initial Count** and type a number in the associated box. If you select this option and either no data is available or fewer data entries exist than the specified Initial Count value, empty instances of the subform are still placed on the form.
1. Add two buttons in the parent subform- one for adding an instance and another for deleting an instance of the repeatable subform. For detailed steps, see [Build an action](https://help.adobe.com/en_US/AEMForms/6.1/DesignerHelp/WS107c29ade9134a2c74572b5612a87ca2b56-8000.2.html#WS107c29ade9134a2c-1f74d86012a87d4fe55-8000.2).
1. Now, link the Form Template to the Adaptive Form (built on an XFA form template). For detailed steps, see [Create an adaptive form based on a template](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/creating-adaptive-form.html?lang=en#create-an-adaptive-form-based-on-an-xfa-form-template).
1. Use the buttons created in step 9 to add and remove subforms.

The attached .zip file contains a sample repeatable subform for reference and testing.

[Get File](/help/forms/assets/samplerepeatablesubform.zip)

## Using repeat settings of an XML Schema (XSD) {#using-repeat-settings-of-an-xml-schema-xsd-br}

An **XML Schema Definition (XSD)** lets you create repeatable panels in adaptive forms using the **minOccurs** and **maxOccurs** properties of any complex type element that defines occurrence constraints. These two attributes control how many times an element can repeat within a form:

- **minOccurs** — the minimum number of times an element must appear. A value of **0** makes the element optional.
- **maxOccurs** — the maximum number of times an element can appear. A value such as **10** allows the corresponding panel to repeat up to ten times, while `unbounded` permits an unlimited number of repetitions.

Because these properties map directly to repeatable panels, the form author does not need to manually configure repetition logic — the panel inherits its repeat behavior from the schema definition itself. For detailed information about XML Schema, see [Create adaptive forms using XML Schema as Form Model](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-advanced-authoring/adaptive-form-xml-schema-form-model.html).

In the following code, the `SampleType` panel uses the **minOccurs** and **maxOccurs** properties to define a repeatable element:

```xml
<?xml version="1.0" encoding="utf-8" ?>
    <xs:schema targetNamespace="https://adobe.com/sample.xsd"
                    xmlns="https://adobe.com/sample.xsd"
                    xmlns:xs="https://www.w3.org/2001/XMLSchema"
                >

        <xs:element name="sample" type="SampleType"/>

        <xs:complexType name="SampleType">
            <xs:sequence>
                <xs:element name="leaderName" type="xs:string" default="Enter Name"/>
                <xs:element name="assignmentStartDate" type="xs:date"/>
                <xs:element name="gender" type="GenderEnum"/>
                <xs:element name="noOfProjectsAssigned" type="IntType"/>
                <xs:element name="assignmentDetails" type="AssignmentDetails"
                                            minOccurs="0" maxOccurs="10"/>
            </xs:sequence>
        </xs:complexType>

        <xs:complexType name="AssignmentDetails">
            <xs:attribute name="name" type="xs:string" use="required"/>
            <xs:attribute name="durationOfAssignment" type="xs:unsignedInt" use="required"/>
            <xs:attribute name="numberOfMentees" type="xs:unsignedInt" use="required"/>
             <xs:attribute name="descriptionOfAssignment" type="xs:string" use="required"/>
             <xs:attribute name="financeRelatedProject" type="xs:boolean"/>
       </xs:complexType>
  <xs:simpleType name="IntType">
            <xs:restriction base="xs:int">
            </xs:restriction>
        </xs:simpleType>
  <xs:simpleType name="GenderEnum">
            <xs:restriction base="xs:string">
                <xs:enumeration value="Female"/>
                <xs:enumeration value="Male"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:schema>
```

In this example, the `SampleItem` element is optional (`minOccurs="0"`) and can repeat up to ten times (`maxOccurs="10"`). As a result, the generated adaptive form renders `SampleType` as a repeatable panel, allowing end users to add or remove instances of the panel within the configured range.

## See Also {#see-also}

{{see-also}}

<!--

>[!MORELIKETHIS]
>
>* [Create an Adaptive Form](creating-adaptive-form-core-components.md)
>* [Create style or themes for your forms](using-themes-in-core-components.md)
>* [Add dynamic behavior to forms using the rule editor](rule-editor.md)
>* [Set layout of forms for different screen sizes and device types](/help/sites-cloud/authoring/features/console-layout.md)

-->
