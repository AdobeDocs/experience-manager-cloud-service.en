---
title: What are the layout capabilities of Adaptive Forms based on core components?
description: Layout and appearances of Adaptive Forms on various devices are governed by the layout settings. Understand the various layouts and how to apply them.
feature: Adaptive Forms, Core Components
keywords: Layout of Adaptive Form based on core components, Different layouts for forms, Dynamic Form Layouts AEM, AEM Cloud Service Form Layouts, Form Layout Types in AEM Core Components, Adaptive Form layouts
role: User, Developer, Admin
---

# Layout capabilities of Adaptive Forms based on Core Components 


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/layout-capabilities-adaptive-forms.html)                  |
| AEM as a Cloud Service (Foundation Components)    | [Click here](/help/forms/layout-capabilities-adaptive-forms.md)        |
| AEM as a Cloud Service (Core Components)    | This article         |

[!DNL Adobe Experience Manager] forms provide layouts as first-class components to structure and design the forms effectively. The layout controls how components are displayed in a form. Adaptive Forms support various layouts: panel, wizard, accordion, tabs on top, and tabs on the left.

## Pre-requisite

Before exploring the various capabilities of a layout, ensure that core components are enabled for your environment. For detailed instructions on how to enable core components for your environment, [click here](/help/forms/enable-adaptive-forms-core-components.md).

##  Adaptive Forms layout types

Adaptive Form based on Core Components supports the following types of layouts:
* **Panel layout**
* **Wizard layout**
* **Vertical layout**
* **Horizontal layout**
* **Accordion layout**

>[!BEGINTABS]

>[!TAB Panel Layout]

Panel layouts are useful for organizing large amounts of information in a way that makes it easier to navigate and find specific content. The panel layout arranges form components within distinct, sections or panels in an Adaptive Form. 

![Panel Layout](/help/forms/assets/panel-layout.png){width="250" align="center"}

Panel Layout

You can use the [panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) to add the panel layout in a form. For detailed instructions on how to configure the properties available in the **Configure Dialog** of the panel component, refer to the [panel component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) article.

>[!TAB Wizard Layout]

The wizard layout simplifies complex processes by breaking them into manageable steps. Each step represents a different part of the process, and users navigate through the steps sequentially, often with **Next** and **Previous** buttons. It helps the users to create forms that require multiple steps.

![Wizard Layout](/help/forms/assets/wizard-layout-compare.gif){width="250" align="center"}

Wizard Layout

You can use the [wizard component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) to add the wizard layout in a form. For detailed instructions on how to configure the properties available in the **Configure Dialog** of the wizard component, refer to the [wizard component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) article.

>[!TAB Vertical Tabs Layout]

The vertical tabs layout is also known as Tabs on the left layout. The vertical tabs layout organizes panels or sections along the left side of a form. It is a common layout for forms where panels/sections is stacked vertically for easy reading and navigation.

![Vertical Layout](/help/forms/assets/vertical-tab.gif){width="250" align="center"}

Vertical Tabs Layout

You can use the [vertical tabs component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs) to add the vertical tabs layout in a form. For detailed instructions on how to configure the properties available in the **Configure Dialog** of the vertical tabs component, refer to the [vertical tabs component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tabs) article.


>[!TAB Horizontal Tabs Layout]

The horizontal tabs layout is also known as Tabs on the top layout. The horizontal tabs layout arranges panels or sections side-by-side in a row. This layout is used for navigation menus, toolbars, or any content that should be presented in a linear manner across the width of the form or panel.


![Horizontal Layout](/help/forms/assets/horizontal-layout.gif){width="250" align="center"}

Horizontal Tabs Layout

You can use the [horizontal tabs component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs) to add the horizontal tabs layout in a form. For detailed instructions on how to configure the properties available in the **Configure Dialog** of the horizontal tabs component, refer to the [horizontal tabs component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs) article.


>[!TAB Accordion Layout]

An Accordion layout displays content in collapsible sections or panels in an Adaptive Form. When a section is expanded, it displays the content within, while other sections remain collapsed. This layout is ideal for displaying large amounts of information in a compact form.

![Accordion Layout](/help/forms/assets/accordion-layout-compare.gif){width="250" align="center"}

Accordion Layout

You can use the [accordion component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) to add the accordion layout in a form. For detailed instructions on how to configure the properties available in the **Configure Dialog** of the accordion component, refer to the [accordion component](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) article.

>[!ENDTABS]

To learn how to insert a layout and add form components to it, refer to the section titled [How to insert a layout and add form components to it?](#how-to-insert-a-layout-and-add-form-components-to-it).

### How to choose the right Adaptive Form layout?

It is important to select the right Adaptive Form layout to optimize user experience and form functionality. The table helps you to understand the different layout options available and guides you in selecting the most suitable layout based on your specific needs and use cases:

| Feature                  | Panel Layout | Wizard Layout                                      | Tabs on the Top/Vertical Tabs Layout                             | Tabs on the Left/Horizontal Tabs Layout                             | Accordion Layout                                      |
|--------------------------|-----------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------|--------|
| **Purpose**             | Groups related content into distinct sections | Guides users through a multi-step process or form | Allows switching between sections/views on the same page | Similar to top tabs but arranged vertically on the left | Organizes content into collapsible sections           |
| **Structure**         |  Distinct sections   | Sequential steps/pages                             | Horizontal tabs at the top                         | Vertical tabs on the left                           | Collapsible panels/sections                            |
| **Navigation**        |  Click on panel headers to navigate| - Forward: “Next” button<br>- Backward: “Back” button<br>- Optional skipping steps |  Click on tabs to switch sections                  |  Click on tabs to switch sections                   |  Click headers to expand/collapse sections           |
| **User Experience**     | Organizes large amounts of content in a manageable way | Step-by-step guidance, reducing overwhelm          | Clear, accessible switching between views          | Efficient use of vertical space, always visible tabs| Compact view with expanded/collapsed sections         |
| **Use Case**            |Complex forms with categorized sections | Setup processes, complex forms                     | Organizing settings or content categories          | Dashboards, complex data views                      | FAQs, settings menus, detailed content sections       |


## How to insert a layout and add form components to it?

Consider the **IT Request Form** shown in the [Adaptive Forms Layout Types](#adaptive-forms-layout-types) section. The form gathers information from employees experiencing technical issues related to their network or laptop. It includes three panels:

* **Employee Detail**: The panel collects information about the employee and contains three textboxes labeled Name, Email ID, and Department.

* **Problem Detail**: The panel captures details about the issue. It includes a checkbox for the problem category with three options: Network, Computer, or Other. It also features two textboxes labeled Please Specify and Comments.

* **Attachment**: The panel allows for the upload of supporting documents related to the problem. 

Let's explore the step-by-step process for inserting a layout and adding components to it. In this example, a horizontal tabs layout is inserted to a form.

### Open an Adaptive Form

1. Log in to your [!DNL Experience Manager Forms] instance. 
1. In the upper-left corner, select **[!UICONTROL Adobe Experience Manager]** > **[!UICONTROL Forms]** > **[!UICONTROL Forms & Documents]**.
1. Open an existing Adaptive Form in an edit mode if it has already been created. 

    ![Open an Adaptive Form](/help/forms/assets/insert-layout.png){width="250" align="center"}

Alternatively, you can also [create new Adaptive Form](/help/forms/creating-adaptive-form-core-components.md).

### Insert a layout

1. Locate the section within the form editor that allows you to add a layout. 

    ![Form editor](/help/forms/assets/form-editor.png){width="200" align="center"}
1. Click the **Add** icon. The icon is typically represented by a plus sign (+) that signifies the option to add new components.

    ![Insert layout](/help/forms/assets/insert-layout-add-icon.png){width="200" align="center"}
    
    Clicking the **Add** icon displays an **Insert New Component** dialog box that displays various components for insertion.

1. Browse the available components in the dialog box that appears and select Horizontal Tabs component to insert horizontal tabs layout.

    ![Select horizontal tabs](/help/forms/assets/select-horizontal-tab.png){width="200" align="center"}

    When you add the horizontal tabs component to your form, it initially consists of two empty panels, named Item1 and Item2, by default. You need to manually add form components to these panels. 

    ![Horizontal tabs](/help/forms/assets/insert-tabs-on-top.png){width="200" align="center"}

1. Open the properties of the horizontal tabs component and specify the name for the component.

    ![Add name for Horizontal tabs](/help/forms/assets/change-name-of-horizontal-tabs.png){width="200" align="center"}

1. Click **Done**.

    ![Horizontal tabs](/help/forms/assets/tabs-on-top-rename-component.png){width="200" align="center"}

Once the layout component is added in the form, modify the number of panels according to the requirements. As the IT Request Form consists of three panels, let's go over the steps to add new panel to the horizontal tabs component.  

### Add new panel in the horizontal tabs component

1. Open the horizontal tabs component properties and click the **Items** tab.

    ![Item tab for Horizontal tabs](/help/forms/assets/tabs-on-top-items-tab.png){width="200" align="center"}

1. Click the **Add** icon to add new panel.

    ![Add new panel](/help/forms/assets/tabs-on-top-add-panel.png){width="200" align="center"}

    When you click the **Add** icon, the **Insert New Component** dialog box appears.

1. Select the panel component.

     ![Add new panel](/help/forms/assets/tabs-on-top-new-panel.png){width="200" align="center"}

    When you select the panel component, the new panel is added in the horizontal layout.
    
    ![Add new panel](/help/forms/assets/tabs-on-top-add-new-panel.png){width="200" align="center"}

    You must provide a name for the new panel; otherwise, you cannot save the properties of the horizontal tabs component.

1. Specify the names of the panels as shown in the figure below:

    ![Panel names](/help/forms/assets/tabs-on-tops-panel-name.png){width="200" align="center"}

1. Click **Done**.

    Once you click **Done**, the three panels appear side-by-side in a row. The panel names are displayed as headings for each panel, and you can add form components to each panel.

    ![Panel names](/help/forms/assets/tabs-on-top-initial-view.png){width="200" align="center"}

As the IT Request Form does not include panel titles, here are the steps to hide the panel title.

### Hide the title of the panels

1. Open the Configuration Dialog for the first panel.

    ![Panel 1 Properties](/help/forms/assets/tabs-on-tops-panel1-properties.png){width="200" align="center"}

1. Select the **Hide title** checkbox from the **Basic** tab.
    
     ![Hide title](/help/forms/assets/tabs-on-top-hide-panel.png){width="200" align="center"}

1. Click **Done**.

Similarly, you can hide titles for the other two panels also. Once done, you can proceed with adding form components to each panel.

### Add form components to each panel

You can employ one of the following method to add form components to the panel:
  - [Add components to a layout's panel using the Add icon](#add-components-to-a-layouts-panel-using-the-add-icon)
  - [Drag and drop components into a layout's panel](#drag-and-drop-components-into-a-layouts-panel)

#### Add components to a layout's panel using the Add icon

1. Locate the section within the panel that allows you to add components. 
1. Click the **Add** icon. The icon is typically represented by a plus sign (+) that signifies the option to add new components.
  ![Insert layout](/help/forms/assets/tabs-on-top-add-component.png){width="200" align="center"}

    Clicking the **Add** icon displays an **Insert New Component** dialog box that displays various components for insertion.

    ![Insert New Component Dialog Box](/help/forms/assets/insert-new-component.png){width="200" align="center"}

1. Browse the available components in the dialog box that appears and select Text Box component.
1. Open the properties of the added Text Box component and specify its name as Name.
    ![Insert layout](/help/forms/assets/tabs-on-top-textbox-component.png){width="200" align="center"}
1. Similarly, add two more Text Box components and name added the components as Email ID and Department.   
    ![First Panel](/help/forms/assets/tabs-on-tops-first-panel.png){width="200" align="center"}

    Now that the components in the first panel have been added, you can proceed with adding the components to the second panel. 

4. To switch the panel, click **Select Panel** from the toolbar. 

    ![Switch Panel](/help/forms/assets/tabs-on-top-select-panel.png){width="200" align="center"}

    When you click the **Select Panel**, the list of the added panels in the Horizontal Tabs component appears.

    ![Switch Panel](/help/forms/assets/tabs-on-tops-panel2.png){width="200" align="center"}

5. Select **2 Panel** from the panel list and the view changes from the first panel to the second panel.

    ![Second Panel](/help/forms/assets/tabs-on-top-panel2-component.png){width="200" align="center"}

6. Repeat the steps outlined from Step 2 to Step 5 for adding the desired components in panel 2 as shown in the below figure:   

     ![Second Panel components](/help/forms/assets/panel-2-components.png){width="200" align="center"}

7. Similarly, repeat the steps outlined from Step 2 to Step 5 for adding the desired component in panel 3:

    ![Third Panel components](/help/forms/assets/panel-3-component.png){width="200" align="center"}

You can also drag-and-drop the components to add the form components to each panel, as explained in the [next section](#drag-and-drop-components-into-a-layouts-panel). 

#### Drag and drop components into a layout's panel

1. Locate the section within the panel that allows you to add components. 
1. Navigate to the left panel within your authoring environment and click **Components**.

    ![Component Panel](/help/forms/assets/add-new-component.png){width="200" align="center"}

    When you click the **Components** option, the list of the available components appears.   

    ![Component Panel](/help/forms/assets/add-new-component2.png){width="200" align="center"}

2. Browse the available components and select Text Box component.

3. Drag the component by clicking and holding the selected component, then drag it over to the panel area to place it.

4. Drop the component into the panel by releasing the mouse. 

5. Open the properties of the added Text Box component and specify its name as Name.
    ![Insert layout](/help/forms/assets/tabs-on-top-textbox-component.png){width="200" align="center"}
6. Similarly, add two more Text Box components and name added the components as Email ID and Department.   
    ![First Panel](/help/forms/assets/tabs-on-tops-first-panel.png){width="200" align="center"}

    Now that the components in the first panel have been added, you can proceed with adding the components to the second panel. 

7. To switch the panel, click **Select Panel** from the toolbar. 

    ![Switch Panel](/help/forms/assets/tabs-on-top-select-panel.png){width="200" align="center"}

    When you click the **Select Panel**, the list of the added panels in the Horizontal Tabs component appears.

    ![Switch Panel](/help/forms/assets/tabs-on-tops-panel2.png){width="200" align="center"}

8. Select **2 Panel** from the panel list and the view changes from the first panel to the second panel.

    ![Second Panel](/help/forms/assets/tabs-on-top-panel2-component.png){width="200" align="center"}

9. Repeat the steps outlined from Step 2 to Step 6 for adding the desired components in panel 2 as shown in the below figure:   

     ![Second Panel components](/help/forms/assets/panel-2-components.png){width="200" align="center"}

10. Similarly, repeat the steps outlined from Step 2 to Step 6 for adding the desired component in panel 3:

    ![Third Panel components](/help/forms/assets/panel-3-component.png){width="200" align="center"}

    >[!NOTE]
    > You can also delete form component from the panel using the ![Delete icon](/help/forms/assets/Smock_Delete_18_N.svg) icon. 
    > 
    > ![Deleting a component](/help/forms/assets/delete-component.png){width="200" align="center"}

### Preview the Form

1. Click **[!UICONTROL Preview]** in the top-right corner of your authoring environment.

    ![Horizontal Layout](/help/forms/assets/horizontal-layout.gif){width="250" align="center"}

You can add the required validations for 

## How to replace an existing layout with a new layout?

You can replace a layout of a form with a new layout which involves modifying how components are arranged and displayed within a form. 

Perform the following steps to replace the existing layout of a form:

1. Open an Adaptive Form for editing 
2. Click on the properties icon of the layout.
3. Click the Replace icon and the **[!UICONTROL Replace Component]** dialog box appears.

    ![Replace Layout](/help/forms/assets/replace-layout.png){width="200" align="center"}

4. Select the desired layout from the **[!UICONTROL Replace Component]** dialog box.
     
   ![Replace Component dialog box](/help/forms/assets/replace-component.png){width="200" align="center"}

After selecting the layout, the arrangement of the components within the layout changes accordingly.

## Next Steps
 
Once you are familiar with the various layout capabilities for an Adaptive Form based on Core Components, you can move on to the next steps:

* [Create your first Adaptive Form based on Core Components](/help/forms/creating-adaptive-form-core-components.md)
* [Create and use Adaptive Form themes](/help/forms/using-themes-in-core-components.md)



## See Also

{{see-also}}