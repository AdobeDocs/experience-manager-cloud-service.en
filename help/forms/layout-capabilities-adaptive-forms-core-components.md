---
title: What are the layout capabilities of Adaptive Forms based on core components?
description: Layout and appearances of Adaptive Forms on various devices are governed by the layout settings. Understand the various layouts and how to apply them.
feature: Adaptive Forms, Core Components
keywords: Layout of Adaptive Form based on core components, Different layouts for forms, Dynamic Form Layouts AEM, AEM Cloud Service Form Layouts, Form Layout Types in AEM Core Components, Adaptive Form layouts
role: User, Developer, Admin
exl-id: dcc01d84-0d39-4fa8-ac47-71a9aba91b1e
---
# Layout capabilities of Adaptive Forms based on Core Components 


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/layout-capabilities-adaptive-forms.html)                  |
| AEM as a Cloud Service (Foundation Components)    | [Click here](/help/forms/layout-capabilities-adaptive-forms.md)        |
| AEM as a Cloud Service (Core Components)    | This article         |

Adaptive Forms provides first-class components to layout and design the forms effectively. The layout controls how components are displayed in a form. Adaptive Forms support various layouts: panel, wizard, accordion, tabs on top/horizontal tabs, and tabs on left/vertical tabs.

<!-- ![Types of Layout](/help/forms/assets/generic-layout-hero-image.png){align="center"}-->

## Pre-requisite

Before exploring the various capabilities of a layout, ensure that core components are enabled for your environment. For detailed instructions on how to enable core components for your environment, [click here](/help/forms/enable-adaptive-forms-core-components.md).

## Adaptive Forms layout types

Adaptive Form based on Core Components supports the following types of layouts:
* **Panel layout**
* **Wizard layout**
* **Vertical layout**
* **Horizontal layout**
* **Accordion layout**

>[!BEGINTABS]

>[!TAB Panel Layout]

Panel layout is useful for organizing related fields in a way that makes it easier to navigate and find corresponding content. The panel layout arranges form components within distinct, sections or panels in an Adaptive Form. 

![Panel Layout](/help/forms/assets/panel-layout.png)

Panel Layout

You can use the [panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) to add the panel layout in a form. For detailed instructions on how to configure various properties of the panel component, refer to the [panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) article.

>[!TAB Wizard Layout]

The wizard layout helps simplifying a complex form by breaking it into distinct steps. Each step represents a different part of the process, and users navigate through the steps sequentially, often with **Next** and **Previous** buttons. You can use the wizard layout to create a form that involves multiple sections or steps.

![Wizard Layout](/help/forms/assets/wizard-layout-compare.gif)

Wizard Layout

You can use the [wizard component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) to add the wizard layout in a form. For detailed instructions on how to configure the various properties of the wizard component, refer to the [wizard component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) article.

>[!TAB Vertical Tabs Layout]

The vertical tabs layout is also known as tabs on the left layout. The vertical tabs layout organizes panels or sections along the left side of a form. It is a common layout for forms where panels/sections is stacked vertically for easy reading and navigation.

![Vertical Layout](/help/forms/assets/vertical-tab.gif)

Vertical Tabs Layout

You can use the [vertical tabs component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs) to add the vertical tabs layout in a form. For detailed instructions on how to configure the various properties of the vertical tabs component, refer to the [vertical tabs component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs) article.


>[!TAB Horizontal Tabs Layout]

The horizontal tabs layout is also known as Tabs on the top layout. The horizontal tabs layout arranges panels or sections side-by-side in a row. This layout presents the form sections in a linear manner across the width of the form or panel.


![Horizontal Layout](/help/forms/assets/horizontal-layout.gif)

Horizontal Tabs Layout

You can use the [horizontal tabs component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs) to add the horizontal tabs layout in a form. For detailed instructions on how to configure the various properties of the horizontal tabs component, refer to the [horizontal tabs component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs) article.


>[!TAB Accordion Layout]

The accordion layout displays content in collapsible sections or panels in an Adaptive Form. When a section is expanded, it displays the content within, while other sections remain collapsed. This layout is ideal for displaying large amounts of information in a compact form.

![Accordion Layout](/help/forms/assets/accordion-layout-compare.gif)

Accordion Layout

You can use the [accordion component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) to add the accordion layout in a form. For detailed instructions on how to configure the various properties of the accordion component, refer to the [accordion component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) article.

>[!ENDTABS]

To learn how to insert a layout and add form components to it, refer to the section titled [How to insert a layout and add form components to it?](#how-to-insert-a-layout-and-add-form-components-to-it)

### How to choose the right Adaptive Form layout?

It is important to select the right Adaptive Form layout to optimize user experience and form functionality. The table helps you to understand the different layout options available and guides you in selecting the most suitable layout based on your specific needs and use cases:

| Feature                  | Panel Layout | Wizard Layout                                      | Tabs on the Top/Vertical Tabs Layout                             | Tabs on the Left/Horizontal Tabs Layout                             | Accordion Layout                                      |
|--------------------------|-----------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------|--------|
| **Purpose**             | Groups related content into distinct sections | Guides users through a multi-step process or form | Allows switching between sections/views on the same page | Similar to top tabs but arranged vertically on the left | Organizes content into collapsible sections           |
| **Structure**         |  Distinct sections   | Sequential steps/pages                             | Horizontal tabs at the top                         | Vertical tabs on the left                           | Collapsible panels/sections                            |
| **Navigation**        |  Click on the panel headers to navigate| - Forward: “Next” button<br>- Backward: “Back” button<br>- Optional skipping steps |  Click on tabs to switch sections                  |  Click on tabs to switch sections                   |  Click headers to expand/collapse sections           |
| **User Experience**     | Organizes large amounts of content in a manageable way | Step-by-step guidance, reducing overwhelm          | Clear, accessible switching between views          | Efficient use of vertical space, always visible tabs| Compact view with expanded/collapsed sections         |
| **Use Case**            |Complex forms with categorized sections | Setup processes, complex forms                     | Organizing settings or content categories          | Dashboards, complex data views                      | FAQs, settings menus, detailed content sections       |


## How to insert a layout and add form components to it?

The below diagram displays the steps to insert a layout to a form and add form components to it:

![Workflow to add a layout and form components](/help/forms/assets/workflow-to-add-component-to-a-layout.png)

Consider the **IT Request Form** shown in the [Adaptive Forms Layout Types](#adaptive-forms-layout-types) section. The form gathers information from employees experiencing technical issues related to their network or laptop. It includes three panels:

* **Employee Details**: The panel collects information about the employee and contains three textboxes labeled Name, Email ID, and Department.

* **Problem Details**: The panel captures details about the issue. It includes a checkbox for the problem category with three options: Network, Computer, or Other. It also features two textboxes labeled Please Specify and Comments.

* **Attachments**: The panel allows users to upload supporting documents related to the problem. 

Let's explore the step-by-step process for inserting a layout and adding components to it. In this example, a horizontal tabs layout is inserted to a form.

### 1. Insert a layout component to a form

1. Log in to your [!DNL Experience Manager Forms] instance. 
1. In the upper-left corner, select **[!UICONTROL Adobe Experience Manager]** > **[!UICONTROL Forms]** > **[!UICONTROL Forms & Documents]**.
1. Open an existing Adaptive Form in an edit mode if it has already been created. 

    ![Open an Adaptive Form](/help/forms/assets/insert-layout.png)

    Alternatively, you can also [create new Adaptive Form](/help/forms/creating-adaptive-form-core-components.md).

1. Locate the section within the form editor that allows you to add a layout. 

    ![Form editor](/help/forms/assets/form-editor.png)
1. Click the **Add** icon. The icon is a plus sign (+) that signifies the option to add new components.

    ![Insert layout](/help/forms/assets/insert-layout-add-icon.png)
    
    Clicking the **Add** icon displays an **Insert New Component** dialog box that displays various components for insertion.

    >[!NOTE]
    >
    > Alternatively, you can also [drag and drop the layout component](#extra-bytes).

1. Browse the available components in the dialog box and select the desrired layout from the list. In our case, we select the Horizontal Tabs component to insert the horizontal tabs layout.

    ![Select horizontal tabs](/help/forms/assets/select-horizontal-tab.png)

    When you add the horizontal tabs component to your form, it initially consists of two empty panels, named Item1 and Item2, by default. You need to manually add form components to these panels. 

    ![Horizontal tabs](/help/forms/assets/insert-tabs-on-top.png)

1. Open the properties of the horizontal tabs component and specify the name for the component.
 For example, in this case, we add the name of the horizontal tabs component as IT Request Form.

    ![Add name for Horizontal tabs](/help/forms/assets/change-name-of-horizontal-tabs.png)

1. Click **Done**.

    ![Horizontal tabs](/help/forms/assets/tabs-on-top-rename-component.png)

Once the layout component is added in the form, modify the number of panels according to the requirements.

### 2. Add panels to the layout

Add new panel to the horizontal tabs component:  

1. Open the horizontal tabs component properties and click the **Items** tab.

    ![Item tab for Horizontal tabs](/help/forms/assets/tabs-on-top-items-tab.png)

1. Click the **Add** icon to add new panel.

    ![Add new panel](/help/forms/assets/tabs-on-top-add-panel.png)

    When you click the **Add** icon, the **Insert New Component** dialog box appears.

1. Select the panel component.

     ![Add new panel](/help/forms/assets/tabs-on-top-new-panel.png)

    When you select the panel component, the new panel is added in the horizontal layout.
    
    ![Add new panel](/help/forms/assets/tabs-on-top-add-new-panel.png)

    Provide a name for the new panel; otherwise, you cannot save the properties of the horizontal tabs component.

1. Specify the names of the panels as shown in the figure below:

    ![Panel names](/help/forms/assets/tabs-on-tops-panel-name.png)

1. Click **Done**.

    Once you click **Done**, the three panels appear side-by-side in a row. The panel names are displayed as headings for each panel, and you can add form components to each panel.

    ![Panel names](/help/forms/assets/tabs-on-top-initial-view.png)

    You can configure the properties of panel component. For example, the IT Request Form does not include panel titles, here are the steps to configure properties of panel component.

1. Open the properties of the first panel.

    ![Panel 1 Properties](/help/forms/assets/tabs-on-tops-panel1-properties.png)

1. Select the **Hide title** checkbox from the **Basic** tab.
    
     ![Hide title](/help/forms/assets/tabs-on-top-hide-panel.png)

1. Click **Done**.

Similarly, you can hide titles for the other two panels also. Once done, you can proceed with adding form components to each panel.

### 3. Add form components to the panel

<!-- You can employ one of the following method to add form components to the panel:
* [Add components to a layout's panel using the Add icon](#add-components-to-a-layouts-panel-using-the-add-icon)
* [Drag and drop components into a layout's panel](#drag-and-drop-components-into-a-layouts-panel) -->

1. Locate the section within the panel that allows you to add components. 
1. Click the **Add** icon. The icon is a plus sign (+) that signifies the option to add new components.
  ![Insert layout](/help/forms/assets/tabs-on-top-add-component.png)

    Clicking the **Add** icon displays an **Insert New Component** dialog box that displays various components for insertion.

    ![Insert New Component Dialog Box](/help/forms/assets/insert-new-component.png)

1. Browse the available components in the dialog box that appears and select the desired component. In our case, select the Text Box component.
1. Open the properties of the added component and specify its name. Let edit the properties of the added Text Box component and specify its name. 
    ![Insert layout](/help/forms/assets/tabs-on-top-textbox-component.png)
1. Similarly, add two more Text Box components and name added the components as Email ID and Department.   
    ![First Panel](/help/forms/assets/tabs-on-tops-first-panel.png)

    Now that the components in the first panel have been added, you can proceed with adding the components to the second panel. 

1. To switch the panel, click **Select Panel** from the toolbar. 

    ![Switch Panel](/help/forms/assets/tabs-on-top-select-panel.png)

    When you click the **Select Panel**, the list of the added panels in the Horizontal Tabs component appears.

    ![Switch Panel](/help/forms/assets/tabs-on-tops-panel2.png)

1. Select **2 Panel** from the panel list and the view changes from the first panel to the second panel.

    ![Second Panel](/help/forms/assets/tabs-on-top-panel2-component.png)

1. Repeat the steps outlined from Step 2 to Step 4 for adding the desired components in panel 2 as shown in the below figure:   

     ![Second Panel components](/help/forms/assets/panel-2-components.png)

1. Switch to the **3 Panel** by following the steps outlined in Step 6 and Step 7.

1. Repeat the steps outlined from Step 2 to Step 4 for adding the desired component in panel 3:

    ![Third Panel components](/help/forms/assets/panel-3-component.png)

1. Click **[!UICONTROL Preview]** in the top-right corner of your authoring environment.
    ![Horizontal Layout](/help/forms/assets/horizontal-layout.gif)

You can also [drag-and-drop the components](#extra-bytes) to add the form components to each panel. 


<!-- #### Drag and drop components into a layout's panel 

1. Locate the section within the panel that allows you to add components. 
2. Navigate to the left panel within your authoring environment and click **Components**.

    ![Component Panel](/help/forms/assets/add-new-component.png){width="200" align="center"}

    When you click the **Components** option, the list of the available components appears.   

    ![Component Panel](/help/forms/assets/add-new-component2.png){width="200" align="center"}

3. Browse the available components and select the Text Box component.

4. Drag the component by clicking and holding the selected component, then drag it over to the panel area to place it.

5. Drop the component into the panel by releasing the mouse. 

6. Open the properties of the added Text Box component and specify its name as Name.
    ![Insert layout](/help/forms/assets/tabs-on-top-textbox-component.png){width="200" align="center"}
7. Similarly, add two more Text Box components and name added the components as Email ID and Department.   
    ![First Panel](/help/forms/assets/tabs-on-tops-first-panel.png){width="200" align="center"}

    Now that the components in the first panel have been added, you can proceed with adding the components to the second panel. 

8. To switch the panel, click **Select Panel** from the toolbar. 

    ![Switch Panel](/help/forms/assets/tabs-on-top-select-panel.png){width="200" align="center"}

    When you click the **Select Panel**, the list of the added panels in the Horizontal Tabs component appears.

    ![Switch Panel](/help/forms/assets/tabs-on-tops-panel2.png){width="200" align="center"}

9. Select **2 Panel** from the panel list and the view changes from the first panel to the second panel.

    ![Second Panel](/help/forms/assets/tabs-on-top-panel2-component.png){width="200" align="center"}

10. Repeat the steps outlined from Step 2 to Step 6 for adding the desired components in panel 2 as shown in the below figure:   

     ![Second Panel components](/help/forms/assets/panel-2-components.png){width="200" align="center"}

11. Switch to the **3 Panel** by following the steps outlined in Step 8 and Step 9.

12. Repeat the steps outlined from Step 2 to Step 6 for adding the desired component in panel 3:

    ![Third Panel components](/help/forms/assets/panel-3-component.png){width="200" align="center"} 

    -->



You can also delete form component from the panel using the ![Delete icon](/help/forms/assets/Smock_Delete_18_N.svg) icon. 

![Deleting a component](/help/forms/assets/delete-component.png)

You can also add the required validations for the components as required. 

## How to replace an existing layout with a new layout?

You can replace a layout of a form with a new layout, which involves modifying how components are arranged and displayed within a form. 

Perform the following steps to replace the existing layout of a form:

1. Click the Replace icon from the toolbar of the layout component and the **[!UICONTROL Replace Component]** dialog box appears.

    ![Replace Layout](/help/forms/assets/replace-layout.png)

1. Select the desired layout from the **[!UICONTROL Replace Component]** dialog box.
     
   ![Replace Component dialog box](/help/forms/assets/replace-component.png)

    After selecting the layout, the arrangement of the components within the layout changes accordingly. For example, select the vertical tabs component from the **[!UICONTROL Replace Component]** dialog box; the arrangement of the panel changes to tabs on left:

    ![Vertical Layout](/help/forms/assets/vertical-tab.gif)

## Extra Bytes

To drag and drop components into the form editor, perform the following steps:

1. Locate the section that allows you to add components. 
1. Navigate to the left panel within your authoring environment and click **Components**.

    ![Component Panel](/help/forms/assets/add-new-component.png)

    When you click the **Components** option, the list of the available components appears.   

    ![Component Panel](/help/forms/assets/add-new-component2.png)

1. Browse the available components and select the desired component.

1. Drag the component by clicking and holding the selected component, then drag it over to the panel area to place it.

1. Drop the component into the panel by releasing the mouse. 

## Next Steps
 
Once you are familiar with the various layout capabilities for an Adaptive Form based on Core Components, you can move on to the next steps:

* [Create your first Adaptive Form based on Core Components](/help/forms/creating-adaptive-form-core-components.md)
* [Create and use Adaptive Form themes](/help/forms/using-themes-in-core-components.md)



## See Also

{{see-also}}
