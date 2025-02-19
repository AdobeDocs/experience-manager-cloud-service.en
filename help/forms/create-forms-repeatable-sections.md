---
title: How to create repeatable panels in Adaptive Form Core Components?
description: Learn to create repeatable section or fields in an Adaptive Form.
role: Architect, Developer, Admin, User
feature: Adaptive Forms, Core Components
exl-id: 02521bf3-83c1-40a0-8fe6-23af240727e9
---
# Create forms with repeatable sections (Core Components) {#repeat-panel}


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/creating-forms-repeatable-sections.html?lang=en)                  |
| AEM as a Cloud Service     | This article        |

A repeatable section refers to a part of a form that can be duplicated or repeated multiple times to collect information for multiple instances of the same data. 

For example, consider a form used to collect information about a person's work experience. You may have a repeatable section for capturing details of each previous job. The repeatable section would typically contain fields such as company name, job title, dates of employment, and job responsibilities. The user can add multiple instances of the repeatable section to enter information about each job they have held.

   ![Repeatability](/help/forms/assets/repeatable-adaptive-form-example.gif)

By the end of this article, you learn to:

* Create a repeatable section in an Adaptive Form
* Set minimum or maximum number of repetitions for an Adaptive Form component
* Use rule editor to configure addition or deletion actions for repeatable sections

You can use the [Panel](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel), [Accordion](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion.html), [Horizontal Tabs](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs.html), [Vertical Tabs](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs) or [Wizard](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard.html) components to make sections of an Adaptive Form repeatable. You can add child components to these components to create repeatable section in a form. 


Examples in this document are based on the [Panel](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) component. You can perform the identical steps to make the [Panel](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel-container.html), [Accordion](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion.html), [Horizontal Tabs](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs.html), [Vertical Tabs](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs) or [Wizard](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard.html) components repeatable.

## Add or delete repeatable sections in a form {#add-or-delete-repeatable-section-in-panel-container}

To repeat a panel in the form or remove repeatable panels, a form author uses a button component to add or remove instance of the panel. To add or delete repeatable sections (panels) in a form:

* [Make panel container repeatable](#make-panel-container-repeatable)
* [Add repeatable section](#add-repeatable-section-using-instance-manager-via-scripts)
* [Delete repeatable sections](#delete-repeatable-section-using-instance-manager-via-scripts)

### Make Panel Container repeatable {#make-panel-container-repeatable}

![Accessibility tab](/help/forms/assets/repeat-panel.png)

To make a panel repeatable, perform the following steps:
1. Select a panel container and select ![cmppr](/help/forms/assets/cmppr.png).
1. Click the **repeat panel** and switch on the toggle to **make panel repeatable**.
1. Set **minimum repetitions** as required for minimum repeatable sections, you can set **minimum repetitions** to zero for non-repition of panels or to remove the repeated panels. By default the value of minimum repetition is zero.
1. Set **maximum repetitions** to repeat the panel number of times required, by default the value is infinite.

   >[!NOTE]
   >
   > 
   > * Minimum repetition cannot be -ve value.
   > * To create a non-repeatable panel, set value of the maximum and minimum field to one.

### Add repeatable section using instance manager (via scripts) {#add-repeatable-section-using-instance-manager-via-scripts}

The parent of the panel which is to be repeated, should contain an add button to manage repeat instance of the panel. Perform the following steps to insert buttons to the parent and enable scripts on the buttons:

1. Add a **button component** to the parent of the panel. In the example video below, a button component with the label name **Add** and field name **AddPanel**, is used. Select the component and select ![edit-rules](/help/forms/assets/edit-rules.png). The rules of the button component open in the rule editor.
1. In the Rule Editor window, click **Create**.

    Select **Visual Editor** in the Form Objects and Functions row.

    1. In the rule area, under WHEN, select state **is clicked**.
    1. Under THEN, select **Add Instance**, and drag-drop the panel using ![toggle-side-panel](/help/forms/assets/toggle-side-panel.png) or select it using **Drop object or select here.**
    
    Select **Code Editor** in the Form Objects and Functions row. Click **Edit Rules** and in the code area:

    * To create an add panel button, specify `this.panel.instanceManager.addInstance()`
        
    Click **Done**.

>[!VIDEO](https://video.tv.adobe.com/v/3421052/adaptive-forms-repeatable-sections-repeat-sections/?quality=12&learn=on)


### Delete repeatable sections using instance manager (via scripts) {#delete-repeatable-section-using-instance-manager-via-scripts}

The parent of the panel should contain a delete button to delete instance of the repeatable panels. Perform the following steps to insert buttons to the parent and enable scripts on the buttons to delete repeatable panels:

1. Add a **button component** to the parent of the panel, In the video below, a button component with the label name **delete** and field name **DeletePanel** is used. Select the component and select ![edit-rules](/help/forms/assets/edit-rules.png). The rules of the button component open in the rule editor.
1. In the Rule Editor window, click **Create**.

    Select **Visual Editor** in the Form Objects and Functions row.

    1. In the rule area, under WHEN **DeletePanel**, select state **is clicked**.
    1. Under THEN, select **Remove Instance**, and drag-drop the panel using ![toggle-side-panel](/help/forms/assets/toggle-side-panel.png) or select it using **Drop object or select here.**

    Select **Code Editor** in the Form Objects and Functions row. Click **Edit Rules** and in the code area:

    * To create a delete panel button, specify `this.panel.instanceManager.removeInstance(this.panel.instanceIndex)`

    Click **Done**.

>[!VIDEO](https://video.tv.adobe.com/v/3421620/adaptive-forms-repeatable-sections)

>[!NOTE]
>
>If a field belongs to a repeatable panel, you cannot access it directly using its name in your scripts. To access the field, specify the repeatable instance to which the field belongs using the `instances` API in `InstanceManager`. The syntax to use the `instances` API in `InstanceManager` is:
>
>
>`<panelName>.instanceManager.instances[<instanceNumber>].<fieldname>`
>
>
>For example, you create an adaptive form with a repeatable panel having a text box. When you pre-fill the form with three repeatable text boxes, you need the xml below:
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
>

<!-- 
>For more information, see: Class: InstanceManager#instances in [AEM Forms Java API reference](https://adobe.com/go/learn_aemforms_documentation_63).      
-->

>[!NOTE]
>
> When all instances of a panel are removed from an adaptive form, to add an instance of the removed panel, use the _panelName syntax to capture the instance manager of the panel and the use the addInstance API of instance manager to add the deleted instance. For example, _panelName.addInstance(). It adds an instance of the removed panel.

<!--
![panel-repeatability-video](/help/adaptive-forms/assets/panel-repeatability-video.mp4)
-->

<!--

## Using the accordion layout for the parent panel &nbsp; {#using-the-accordion-layout-for-the-parent-panel-nbsp}

A panel has various layouts options. The Layout for accordian design option has out of the box support for repeatable panels. Perform the following steps to repeatable panel with Layout for accordian design option:

1. On the parent of panel to be repeated, select ![cmppr](assets/cmppr.png). You can see the properties in the sidebar. In the **Layout** drop-down, select **Accordion**.
1. On a panel, which is to be repeated, select ![cmppr](assets/cmppr.png). You can see the panel properties in the sidebar. Enable the **Make Panel Repeatable** tab, and specify value for the **Maximum** and **Minimum** fields.

   Now, you can use the plus (+) and delete ( ![delete-panel](assets/delete-panel.png)) buttons to add and remove the panels.

-->

## Using repeating subforms from Form Template (XDP/XSD) {#using-repeating-subforms-from-form-template-xdp-xsd}

Repeatable subform is similar to the repeatable panels in Adaptive Forms. In AEM Forms Designer, perform the following steps to create a repeating subform:

1. In the Hierarchy palette, select the parent subform of the subform you want to repeat.
1. In the Object palette, click the Subform tab, and in the Content list, select Flowed.
1. Select the subform to repeat.
1. In the Object palette, click the Subform tab and, in the Content list, select either Positioned or Flowed.
1. Click the Binding tab and select Repeat Subform For Each Data Item.
1. To specify the minimum number of repetitions, select Min Count and type a number in the associated box. If this option is set to 0 and no data is provided for the objects in the subform at data-merge time, the subform is not placed when the form is rendered.
1. To specify the maximum number of subform repetitions, select Max and type a number in the associated box. If you do not specify a value in the Max box, the number of subform repetitions are unlimited.
1. To specify a set number of subform repetitions, regardless of the quantity of data, select Initial Count and type a number in the associated box. If you select this option and either no data is available or fewer data entries exist than the specified Initial Count value, empty instances of the subform are still placed on the form.
1. Add two buttons in the parent subform- one for adding instance and another for deleting instance of repeatable subform. For detailed steps, see [Build an action](https://help.adobe.com/en_US/AEMForms/6.1/DesignerHelp/WS107c29ade9134a2c74572b5612a87ca2b56-8000.2.html#WS107c29ade9134a2c-1f74d86012a87d4fe55-8000.2).
1. Now, link the Form Template to the Adaptive form. For detailed steps, see [Create an adaptive form based on a template](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/creating-adaptive-form.html?lang=en#create-an-adaptive-form-based-on-an-xfa-form-template).
1. Use the buttons created in step 9 to add and remove subforms.

Attached .zip file contains a sample repeatable sub form.

[Get File](/help/forms/assets/samplerepeatablesubform.zip)

## Using repeat settings of an XML Schema (XSD) {#using-repeat-settings-of-an-xml-schema-xsd-br}

You can create repeatable panels from an XML Schema and from the minOccours & maxOccurs property of any complex type element. For detailed information about XML Schema, see [Create adaptive forms using XML Schema as Form Model](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-advanced-authoring/adaptive-form-xml-schema-form-model.html).

In the following code, the `SampleType`panel uses the minOccours & maxOccurs property.

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