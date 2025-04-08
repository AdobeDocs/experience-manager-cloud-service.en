---
title: Understanding Universal Editor
description: This tutorial helps you get up and running with the Universal Editor interface. It guides you in understanding the user interface to create your own Edge Delivery Services forms in Universal Editor.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: 90321e81-bb55-48b2-b329-4944bf926309
---

# Exploring the Universal Editor (WYSIWYG) Interface

The [Universal Editor](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) offers a simple, visual, and intuitive What You See Is What You Get (WYSIWYG) interface for Adobe Edge Delivery Services Forms. It provides a modern interface with drag-and-drop functionality for efficient form authoring.

![Universal Editor User Interface](/help/edge/docs/forms/universal-editor/assets/universal-editor-interface.png)

## What You'll Learn

By the end of this tutorial, you'll:

- Understand the main components of the Universal Editor interface
- Navigate confidently through the different interface sections
- Know how to access and use essential form-building tools
- Be familiar with keyboard shortcuts that increase productivity

## Understanding the Universal Editor Interface

When you edit a form using the Universal Editor, the console opens an interactive WYSIWYG interface that allows you to immediately start editing. This interface provides real-time visual feedback as you work, showing exactly how your form will appear to end users.

>[!NOTE]
>
> To learn how to author forms using the Universal Editor, see the article [Getting Started with Edge Delivery Services for AEM Forms using Universal Editor (WYSIWYG)](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md).

![Universal Editor User Interface](/help/edge/docs/forms/universal-editor/assets/universal-editor-interface1.png)

The Universal Editor interface is divided into four logical parts:

- **[A: Experience Cloud Header](#experience-cloud-header)**
- **[B: Universal Editor Toolbar](#universal-editor-toolbar)**
- **[C: Properties Panel](#properties-panel)**
- **[D: Editor](#editor)**

Let's explore each section in detail.

### Experience Cloud Header

The Experience Cloud Header appears at the top of the console and provides navigation context within the broader Adobe Experience Cloud ecosystem. It shows your current location and allows quick access to other Experience Cloud applications.

![Universal Editor Experience Cloud Header](/help/edge/docs/forms/universal-editor/assets/universal-editor-experience-manager-header.png)

Let's examine each component:

- **Adobe Experience Cloud**
    
    Clicking the **Adobe Experience Cloud** link on the left side of the screen allows you to navigate to the root of the Experience Manager solution. From there, you can access other tools such as Experience Manager Sites, Experience Manager Assets, and Experience Manager Guides.

    ![Adobe Experience Manager](/help/edge/docs/forms/universal-editor/assets/universal-editor-experience-manager.png)

- **Organization Name**
    
    The **Organization Name** displays the name of the Identity Management System (IMS) organization you're currently signed into. If you have access to multiple organizations, you can switch between them using this dropdown menu. For example, in the screenshot, the currently selected IMS organization is "AEM Forms Internal01."

    ![Organization](/help/edge/docs/forms/universal-editor/assets/universal-editor-organization.png)

- **Help**

    The Help icon provides quick access to learning and support resources. This is particularly valuable when you encounter challenges or need guidance on specific features. You can also submit feedback through this section.
    
    ![Help](/help/edge/docs/forms/universal-editor/assets/ue-help.png)

- **Notifications**
    
    The **Notifications** section displays the number of currently assigned incomplete notifications, requests, and current tasks in your IMS organization. Keeping an eye on this section helps you stay on top of your workflow.

    ![Notification](/help/edge/docs/forms/universal-editor/assets/ue-notification.png)

- **Solutions**
  
    The **Solutions** menu allows you to switch to other Adobe Experience Cloud solutions, making it easy to move between different tools in your workflow.
    
    ![Solutions](/help/edge/docs/forms/universal-editor/assets/ue-solutions.png)

- **User Profile**
    
    This icon displays your profile information, along with the name of the IMS organization you're currently signed into. Click this icon to access account settings and sign-out options.
    
    ![Author](/help/edge/docs/forms/universal-editor/assets/ue-author.png)

### Universal Editor Toolbar

The toolbar provides essential navigation and editing tools. With it, you can move between forms, publish or unpublish forms, edit form properties, and access the rule editor for adding dynamic behaviors.

![Universal Editor Toolbar](/help/edge/docs/forms/universal-editor/assets/ue-toolbar.png)

Here's what each component offers:

- **Home Button**
    
    The Home button returns you to the start page of the Universal Editor. This is useful when you need to start working on a different form. You can also directly enter a URL in the location bar to navigate to any form you want to edit.
    
    ![Universal Editor Home](/help/edge/docs/forms/universal-editor/assets/ue-home.png)

- **Location Bar**
    
    The **Location Bar** displays the address of the form you're currently editing. To switch to a different form, simply click the location bar and enter its URL. The keyboard shortcut to focus the location bar is `l`.
    
    ![Location Bar](/help/edge/docs/forms/universal-editor/assets/ue-locationbar.png)

- **Rule Editor**
    
    The **Rule Editor** enables you to add dynamic behaviors to your forms through an intuitive visual interface. With it, you can create conditions, validations, and actions that respond to user input, making your forms interactive and intelligent.

    ![Rule Editor](/help/edge/docs/forms/universal-editor/assets/ue-ruleeditor.png)

    >[!NOTE]
    >
    > - The Rule Editor extension is not enabled by default in Universal Editor. To enable this powerful feature, contact us at [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) from your official email address.
    > - To learn how to create and manage rules, refer to the article [Introduction to Rule Editor in WYSIWYG Authoring](/help/edge/docs/forms/universal-editor/rule-editor-universal-editor.md).

- **Edit Form Properties**
    
     The **Edit Form Properties** option allows you to configure important form settings such as the Form Data Model (FDM) and publication date. These properties influence how your form behaves and integrates with back-end systems.
    
    ![Edit Form Properties](/help/edge/docs/forms/universal-editor/assets/ue-formproperties.png)

- **Authentication Header Settings**
    
    The **Authentication Header Settings** option lets you set custom authentication headers for local development purposes. This is particularly useful when testing forms that require authentication credentials.
    
    ![Authentication Header](/help/edge/docs/forms/universal-editor/assets/ue-authenticationheader.png)

- **Responsive Mode**
    
    The **Responsive Mode** feature allows you to test how your form will appear on different devices. By default, the editor opens in desktop layout, but you can switch to mobile view to ensure your form remains usable and attractive on smaller screens.

    ![Responsive mode](/help/edge/docs/forms/universal-editor/assets/ue-responsivemode.png)

- **Preview Mode**
    
    **Preview Mode** shows your form exactly as it will appear when published. This allows you to interact with the form by clicking links and buttons, just as your users would. This is an essential step before publishing to verify everything works as expected. Toggle between edit and preview modes using the keyboard shortcut `p`.
    
    ![Preview](/help/edge/docs/forms/universal-editor/assets/ue-preview.png)

- **Open Page**
    
    The **Open Page** button opens your form in a new browser tab for preview. This gives you a full-screen view of your form without the editor interface. The keyboard shortcut for this action is `o`.
    
    ![Open Page](/help/edge/docs/forms/universal-editor/assets/ue-openpage.png)

- **Publish**
    
    Once your form is ready for users, the **Publish** button makes it live and available to your audience. This is the final step in your form creation workflow.
    
    ![Publish](/help/edge/docs/forms/universal-editor/assets/ue-publish.png)

- **Ellipsis Menu**
    
    Clicking the ellipsis (…) reveals additional options, including the ability to **Unpublish** a form that's currently live. This is useful when you need to temporarily remove a form from public access or replace it with an updated version.
    
    ![Ellipsis](/help/edge/docs/forms/universal-editor/assets/ue-ellipsis.png)

### Properties Panel

The **Properties Panel** appears on the right side of the interface and displays contextual information based on what you've selected in the form. When no component is selected, it shows the overall form structure.

![Properties Panel](/help/edge/docs/forms/universal-editor/assets/ue-properties-panel.png)

Let's explore its key components:

- **Properties Mode**
    
    The **Properties** mode displays settings and options for your currently selected component. This is where you customize individual elements of your form to meet your specific requirements. The keyboard shortcut to open properties of a selected component is `d`.

    ![Properties](/help/edge/docs/forms/universal-editor/assets/ue-properties.png)

- **Content Tree** 
    
    The **Content Tree** displays your form's hierarchical structure. This visual representation helps you understand how components are nested within one another. Clicking any item in the tree selects it in the editor and scrolls to its location. This is especially helpful in complex forms. Toggle the content tree view with the keyboard shortcut `f`.

    ![Content tree](/help/edge/docs/forms/universal-editor/assets/ue-contenttree.png)

- **Generate Variations**
    
    The **Generate Variations** feature harnesses artificial intelligence to create different versions of your form based on specific prompts. This helps you experiment with different approaches and designs without manually creating each variation. Prompts can be provided by Adobe or customized by you.

    ![Generate Variations](/help/edge/docs/forms/universal-editor/assets/ue-variations.png)
 
    >[!NOTE]
    >
    > For detailed instructions on using Generate Variations for forms, refer to the [Generate Variations](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/generative-ai/generate-variations) article.

- **Experimentation**

    The **Experimentation** feature allows you to run controlled tests comparing different form designs and layouts. By analyzing how users interact with each variant, you can make data-driven decisions to optimize conversion rates and user experience.
    
    ![Experimentation](/help/edge/docs/forms/universal-editor/assets/ue-experimentation.png)

- **Personalization**
    
    The **Personalization** settings allow you to connect your forms with Adobe Experience Platform (AEP) or external applications. This connection enables you to create tailored form experiences based on user data and behaviors, increasing relevance and engagement.
    
    ![Personalization](/help/edge/docs/forms/universal-editor/assets/ue-personalizaton.png)

- **A/B Testing**
    
    **A/B Testing** helps you compare specific variations of your form to determine which performs better. Unlike broader experimentation, A/B tests typically focus on comparing specific elements or changes to identify the most effective option.
    
    ![A/B Testing](/help/edge/docs/forms/universal-editor/assets/ue-abtesting.png)

- **Task Management**
    
    The **Task Management** feature streamlines collaboration by helping your team organize, track, and complete tasks related to form creation and optimization. This keeps projects moving forward efficiently with clear accountability.
    
    ![Task Management](/help/edge/docs/forms/universal-editor/assets/ue-taskmanagement.png)

- **Content Drafts**
    
    The **Content Drafts** feature allows you to create and save preliminary versions of text elements in your form. You can create drafts using existing form text or start from scratch, then edit or delete them as needed. By default, you'll see three drafts, but clicking **Show All** reveals additional drafts.

    ![Content Drafts](/help/edge/docs/forms/universal-editor/assets/ue-contentdraft.png)

- **Data Source**
    
    The **Data Source** option lets you configure and select the data sources for your Form Data Model (FDM). This integration makes all data model objects, properties, and services from your selected sources available for use in the form, enabling dynamic data retrieval and submission.
    
    ![Data Source](/help/edge/docs/forms/universal-editor/assets/ue-datasource.png)

- **Add**

    The **Add** button reveals a dropdown list of components that can be added to the currently selected container. For example, when an Adaptive Form section is selected, this list shows all components that can be added to that section. The keyboard shortcut to open this component list is `a`.
    
    ![Add Icon](/help/edge/docs/forms/universal-editor/assets/ue-add.png)

- **Duplicate**
    
    The **Duplicate** option creates an exact copy of your selected component. This saves time when you need multiple similar elements, as you can duplicate and then modify instead of creating from scratch.
    
    ![Duplicate Icon](/help/edge/docs/forms/universal-editor/assets/ue-duplicate.png)

- **Delete** 
    
    The **Delete** option removes the selected component from your form. Be careful when using this option, as it immediately removes the element without a confirmation prompt.

    ![Delete](/help/edge/docs/forms/universal-editor/assets/ue-delete.png)

### Editor

The Editor is the central workspace where you create and modify your form. It displays the form specified in the location bar and provides a WYSIWYG experience that shows exactly how your form will appear to users. In preview mode, you can interact with the form just as your users would, testing navigation through buttons and links.

![Editor](/help/edge/docs/forms/universal-editor/assets/ue-editor.png)

The Editor is where you'll spend most of your time, adding components, configuring their properties, and arranging them to create an intuitive, effective form experience.

## Keyboard Shortcuts Summary

To boost your productivity, remember these essential keyboard shortcuts:

- `l` - Focus the location bar
- `p` - Toggle between edit and preview modes
- `o` - Open the form in a new tab
- `d` - Open properties of the selected component
- `f` - Toggle the content tree view
- `a` - Open the list of components to add


