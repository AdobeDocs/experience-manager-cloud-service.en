---
title: What are the layout capabilities of Adaptive Forms based on core components?
description: Layout and appearances of Adaptive Forms on various devices are governed by the layout settings. Understand the various layouts and how to apply them.
feature: Adaptive Forms, Core Components
keywords: Layout of Adaptive Form based on core components, Diffrent layouts for forms, Dynamic Form Layouts AEM, AEM Cloud Service Form Layouts, Form Layout Types in AEM Core Components, Adaptive Form layouts
role: User, Developer, Admin
---

# Layout capabilities of Adaptive Forms based on Core Components{#layout-capabilities-of-adaptive-forms}


| Version | Article link |
| -------- | ---------------------------- |
| AEM 6.5  |    [Click here](https://experienceleague.adobe.com/docs/experience-manager-65/forms/adaptive-forms-basic-authoring/layout-capabilities-adaptive-forms.html)                  |
| AEM as a Cloud Service (Foundation Components)    | [Click here](/help/forms/layout-capabilities-adaptive-forms.md)        |
| AEM as a Cloud Service (Core Components)    | This article         |

[!DNL Adobe Experience Manager] lets you create easy-to-use Adaptive Forms that offer dynamic experiences to end users. AEM Cloud Service Form layout controls how items or components are displayed in an Adaptive Form. The dynamic form layouts are the first class components that are used to structure and design forms effectively. 


## Prerequisite knowledge 

Before learning the different layout capabilities of Adaptive Forms, it is important to be familiar with

* [Adaptive Forms Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/adaptive-forms/introduction.html) 
* [Create an Adaptive Form based on Core Components](/help/forms/creating-adaptive-form-core-components.md)
* [Create and use Adaptive Form themes](/help/forms/using-themes-in-core-components.md)

## Types of AEM Forms layouts {#types-of-layouts}

An Adaptive Form based on Core Components provides you with the following types of layouts:
* **Panel layout**
* **Wizard layout**
* **Vertical layout**
* **Horizontal layout**
* **Accordion layout**


>[!BEGINTABS]

>[!TAB Panel Layout]

A Panel layout arranges components/items within distinct, often collapsible, sections or panels in an Adaptive Form. Panel layouts are useful for organizing large amounts of information in a way that makes it easier to navigate and find specific content.

![Panel Layout](/help/forms/assets/panel-layout.png)

Panel Layout

To learn about the different properties available in the Configure Dialog, refer to the [Panel Layout](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/panel) article.

>[!TAB Wizard Layout]

A Wizard layout guides users through a multi-step process, often seen in forms or setup processes. Each step represents a different part of the process, and users navigate through the steps sequentially, often with **Next** and **Previous** buttons. This layout simplifies complex processes by breaking them into manageable steps.

![Wizard Layout](/help/forms/assets/wizard-layout-compare.gif)

Wizard Layout

>[!TAB Vertical Tabs Layout]

A Vertical layout arranges components/items one below the other in a column in a form. It is a common layout for webpages, forms, and lists, where content is stacked vertically for easy reading and navigation.

![Vertical Layout](/help/forms/assets/vertical-tab.gif)

To learn about the different properties available in the Configure Dialog, refer to the [Vertical Tabs Layout](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/vertical-tab) article.

Vertical Tabs Layout

>[!TAB Horizontal Tabs Layout]

In a Horizontal/Tabs on top layout, components/items are arranged side-by-side in a row in a form. This layout is used for navigation menus, toolbars, or any content that should be presented in a linear manner across the width of the container.

![Horizontal Layout](/help/forms/assets/horizontal-layout.gif)

Horizontal Tabs Layout

To learn about the different properties available in the Configure Dialog, refer to the [Horizontal Tabs Layout](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/horizontal-tabs) article.

>[!TAB Accordion Layout]

An Accordion layout displays content in collapsible sections or panels in an Adaptive Form. When a section is expanded, it reveals the content within, while other sections remain collapsed. This layout is ideal for displaying large amounts of information in a compact form.

![Accordion Layout](/help/forms/assets/accordion-layout-compare.gif)

Accordion Layout

To learn about the different properties available in the Configure Dialog, refer to the [Accordion Layout](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/accordion) article.

>[!ENDTABS]

To learn about the different properties available in the Configure Dialog, refer to the [Wizard Layout](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/adaptive-forms-components/wizard) article.

Let us understand difference between various layouts in the next section.

### Difference between various Adaptive Form layouts

The table below highlights the differences between various layouts, comparing features such as purpose, navigation, structure and many more:

| Feature                  | Panel Layout | Wizard Layout                                      | Tabs on the Top/Vertical Tabs Layout                             | Tabs on the Left/Horizontal Tabs Layout                             | Accordion Layout                                      |
|--------------------------|-----------------------------------------------------|----------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------|--------|
| **Purpose**             | Groups related content into distinct sections | Guides users through a multi-step process or form | Allows switching between sections/views on the same page | Similar to top tabs but arranged vertically on the left | Organizes content into collapsible sections           |
| **Structure**         |  Distinct sections   | Sequential steps/pages                             | Horizontal tabs at the top                         | Vertical tabs on the left                           | Collapsible panels/sections                            |
| **Navigation**        |  - Click on panel headers to navigate| - Forward: “Next” button<br>- Backward: “Back” button<br>- Optional skipping steps | - Click on tabs to switch sections                  | - Click on tabs to switch sections                   | - Click headers to expand/collapse sections           |
| **User Experience**     | Organizes large amounts of content in a manageable way | Step-by-step guidance, reducing overwhelm          | Clear, accessible switching between views          | Efficient use of vertical space, always visible tabs| Compact view with expanded/collapsed sections         |
| **Use Case**            |Complex forms with categorized sections | Setup processes, complex forms                     | Organizing settings or content categories          | Dashboards, complex data views                      | FAQs, settings menus, detailed content sections       |




## Add form components to layouts

You can add [Adaptive Form components](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/introduction) to different layouts for an Adaptive Form based on Core Components in two ways:
    - [Drag and drop the Adaptive Forms Core components into the layout using the Content tree](#drag-and-drop-the-adaptive-forms-core-components-into-the-layout-using-the-content-tree)
    - [Insert the Adaptive Forms Core components into the layout using the Add icon.](#insert-the-adaptive-forms-core-components-into-the-layout-using-the-add-icon)

### Drag and drop the Adaptive Forms Core components into the layout using the Content tree

You can drag and drop the [Adaptive Form components](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/adaptive-forms/introduction) into the layout using the content tree. It allows you to position and arrange components visually within your layout, offering a straightforward way to build and customize your Adaptive Forms.

Perform the following steps to drag and drop the form components into the layout:

To add Adaptive Forms Core components to your layout using the Content tree, follow these steps:

1. Open the Adaptive Form for editing.
1. Navigate to the content tree panel within your authoring environment. It displays the hierarchical structure of your form components.

    ![Content Tree Panel](/help/forms/assets/content-tree-view.png)

1. Browse through the content tree to find the component and select the desired component, which can be a specific form field, button, or other component.

1. Drag the component by clicking and holding the selected component, then drag it over to the layout area to place it.

1. Drop the component into the layout by releasing the mouse. 

The component is added to your layout, and you can adjust its properties and settings as required.

### Insert the Adaptive Forms Core components into the layout using the Add icon.

You can insert the components in the layout using the **Add** icon in the form editor. It allows you to easily access a list of available components and insert them into your layout by selecting the desired element.

Perform the following steps to insert Adaptive Forms Core components into your layout using the Add icon:

1. Open an Adaptive Form for editing to modify the structure of your form.
1. To add the component, click the **Add** icon within the form editor. The icon is typically represented by a plus sign (+) that signifies the option to add new components.

    ![Add Component](/help/forms/assets/add-component.png)

    Clicking the **Add** icon displays a **Insert New Component** dialog box that displays various components for insertion.
1. Browse the available components in the dialog box that appears.
1. Select the desired Adaptive Forms Core component to your layout, which can be a specific form field, button, or other essential form element.

    ![Insert New Component Dialog Box](/help/forms/assets/insert-new-component.png)

Once selected, the component is inserted into your layout at the position indicated by your cursor or based on the default insertion point.

The **Add** icon provides a streamlined way to integrate components into your layout by offering a straightforward selection and insertion process.

## Change the layout

You can change the layout of an Adaptive Form that involves modifying how components are arranged and displayed within the form. 

Perform the following steps to change the layout of a form:

1. Open an Adaptive Form for editing 
1. Click on the properties icon of the layout.
1. Click the Replace icon and the **[!UICONTROL Replace Component]** dialog box appears.

    ![Replace Layout](/help/forms/assets/replace-layout.png)

1. Select the desired layout from the **[!UICONTROL Replace Component]** dialog box.
     
   ![Replace Component dialog box](/help/forms/assets/replace-component.png)

After selecting the layout, the arrangement of the components within the layout changes accordingly.


## See Also

{{see-also}}