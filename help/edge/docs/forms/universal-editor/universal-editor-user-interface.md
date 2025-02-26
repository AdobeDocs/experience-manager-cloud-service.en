---
title: Understanding Universal Editor - Developer Tutorial
description: This tutorial helps you get up and running with the Universal Editor interface. It guides you in understanding the user interface to create your own Edge Delivery Services forms in Universal Editor.
feature: Edge Delivery Services
role: Admin, Architect, Developer
exl-id: 90321e81-bb55-48b2-b329-4944bf926309
---
# Exploring the Universal Editor (WYSIWYG) Interface

The [Universal Editor](/help/edge/docs/forms/universal-editor/overview-universal-editor-for-edge-delivery-services-for-forms.md) offers a simple, visual, and intuitive What You See Is What You Get (WYSIWYG) interface for Adobe Edge Delivery Services (EDS) Forms. It provides a modern interface with drag-and-drop functionality for efficient form authoring. 

![Universal Editor User Interface](/help/edge/docs/forms/universal-editor/assets/universal-editor-interface.png)

## Understanding Universal Editor Interface

When the form author edits the form using the Universal Editor, the console opens an interactive WYSIWYG interface, allowing the user to start editing the form.

>[!NOTE]
>
> To learn how to author forms using the Universal Editor, see the article [Getting Started with Edge Delivery Services for AEM Forms using Universal Editor (WYSIWYG)](/help/edge/docs/forms/universal-editor/getting-started-universal-editor.md).

![Universal Editor User Interface](/help/edge/docs/forms/universal-editor/assets/universal-editor-interface1.png)

The Universal Editor interface is divided into four parts:

* **[A: Experience Cloud Header](#experience-cloud-header)**
* **[B: Universal Editor Toolbar](#universal-editor-toolbar)**
* **[C: Properties Panel](#properties-panel)**
* **[D: Editor](#editor)**

### Experience Cloud Header

The Experience Cloud header is located at the top of the console. It provides information about the current location within Experience Cloud. It also allows you to navigate to other Experience Cloud applications.

![Universal Editor Experience Cloud Header](/help/edge/docs/forms/universal-editor/assets/universal-editor-experience-manager-header.png)


Let's understand each of its components.

* **Adobe Experience Cloud**
    
    You can click the **Adobe Experience Cloud** link on the left side of the screen to navigate to the root of the Experience Manager solution and access tools such as Experience Manager Sites, Experience Manager Assets, and Experience Manager Guides.

    ![Adobe Experience Manager](/help/edge/docs/forms/universal-editor/assets/universal-editor-experience-manager.png){width=50%,height=50%}

* **Organization name**
    
    The **Organization name** displays the name of the IMS organization you are currently signed into. You can switch to another IMS organization, if they have access to other organizations, by selecting from the drop-down list. For example, the currently selected IMS organization name is `AEM Forms Internal01`.

    ![Organization](/help/edge/docs/forms/universal-editor/assets/universal-editor-organization.png){width=50%,height=50%}


* **Help**

    The help icon provides quick access to learning and support resources. The form author can also add the feedback in the **Help** section.
    ![Help](/help/edge/docs/forms/universal-editor/assets/ue-help.png){width=50%,height=50%}
    

* **Notifications**
    
    The **Notification** section displays the number of currently assigned incomplete notifications, the requests and, current tasks in the IMS organization.

    ![Notification](/help/edge/docs/forms/universal-editor/assets/ue-notification.png){width=50%,height=50%}


* **Solutions**
  
    You can switch to other Experience Cloud solutions using the **Solutions** link.
    ![Solutions](/help/edge/docs/forms/universal-editor/assets/ue-solutions.png){width=50%,height=50%}


* **Author**
    The icon represents the details of the form author, along with the name of the IMS organization in which the author is currently signed in.
    ![Author](/help/edge/docs/forms/universal-editor/assets/ue-author.png){width=50%,height=50%}

### Universal Editor Toolbar

The toolbar enables you to navigate to and edit other forms. It also allows them to publish or unpublish the form, edit the form's properties, and access the rule editor.
![Universal Editor Toolbar](/help/edge/docs/forms/universal-editor/assets/ue-toolbar.png)

Let's understand each of its components.

* **Home Button**
    The home button allows you to navigate to the start page of the Universal Editor. You can also directly enter the URL of the form they want to edit using the Universal Editor.
    ![Universal Editor Home](/help/edge/docs/forms/universal-editor/assets/ue-home.png)



* **Location Bar**
      The **location bar** displays the address of the form that the author is editing. You can also enter another form URL by clicking on the location bar. The shortcut key to open the location bar is key `l`.
    ![Location Bar](/help/edge/docs/forms/universal-editor/assets/ue-locationbar.png){width=50%,height=50%}



* **Rule Editor**
    
    The **Rule Editor** offers an intuitive visual interface for creating and managing rules. You can add dynamic form behaviour using the Rule Editor.

    ![Rule Editor](/help/edge/docs/forms/universal-editor/assets/ue-ruleeditor.png)

    >[!NOTE]
    >
    > * In Universal Editor, the Rule Editor extension is not enabled by default. To enable the Rule Editor extension write to us at [aem-forms-ea@adobe.com](mailto:aem-forms-ea@adobe.com) from your official email id.
    > * To learn how to create rules, refer to the article [Introduction to Rule Editor in WYSIWYG Authoring](/help/edge/docs/forms/universal-editor/rule-editor-universal-editor.md).

* **Edit Form Properties**
     You can edit the form properties, such as the form data model and publish date, by clicking the **Edit Form Properties** option.
    ![Edit Form Properties](/help/edge/docs/forms/universal-editor/assets/ue-formproperties.png)

   

* **Authentication Header Settings**
    The **authentication header settings** allows the author to set a custom authentication header for local development purposes.
    ![authentication header](/help/edge/docs/forms/universal-editor/assets/ue-authenticationheader.png){width=50%,height=50%}
 


* **Responsive Mode**
    **Responsive Mode** option allows you to define how the Universal Editor renders the form. By default, the editor opens in a desktop layout, where the height and width are automatically determined by the browser. Alternatively, you can choose to emulate a mobile device and check how the form appears on mobile devices.

    ![Responsive mode](/help/edge/docs/forms/universal-editor/assets/ue-responsivemode.png){width=50%,height=50%}


* **Preview Mode**
      In preview mode, the form appears in the editor exactly as it is published. This allows the author to navigate the form by clicking links and buttons. Once satisfied with the edits, the author can publish the form for live users. The shortcut key to toggle between edit and preview mode is `p`.
    ![Preview](/help/edge/docs/forms/universal-editor/assets/ue-preview.png)

* **Open Page**
    The **Open Page** option opens the form in a new tab for preview. The shortcut key to open the form in preview mode in a new tab is `o`.
    ![Open Page](/help/edge/docs/forms/universal-editor/assets/ue-openpage.png)

* **Publish**
    
    You can make the form available to live users using the **Publish** button. 
    ![Publish](/help/edge/docs/forms/universal-editor/assets/ue-publish.png){width=50%,height=50%}

* **Ellipsis**
    When the author clicks the (…) ellipsis option, the **Unpublish** option appears. You can unpublish a form by using the **Unpublish** option.
    ![Ellipsis](/help/edge/docs/forms/universal-editor/assets/ue-ellipsis.png){width=50%,height=50%}

### Properties Panel

The **Properties Panel** is located on the right side of the editor. It displays the details of the component selected in the hierarchy of the form. It is the default structure when no component is selected.
![ue-properties panel](/help/edge/docs/forms/universal-editor/assets/ue-properties-panel.png){width=50%,height=50%}


Let's understand each of its components.


* **Properties Mode**
    In **Properties** option shows the properties of the selected component in the editor. For example, the image displays the properties of the selected number input component. You can modify the properties of the component using this option. The shortcut key to open properties of the component is `d`.

    ![ue-properties](/help/edge/docs/forms/universal-editor/assets/ue-properties.png){width=50%,height=50%}


* **Content Tree** 
    The **Content Tree** option displays the form's hierarchy. When the author clicks on an item in the content tree, the editor selects it and scrolls to that component. The shortcut key to toggle between the content tree view is key `f`.

    ![Content tree](/help/edge/docs/forms/universal-editor/assets/ue-contenttree.png){width=50%,height=50%}


* **Generate Variations**
    **Generate Variations** uses artificial intelligence to produce different versions of forms based on specific prompts. These prompts can either be supplied by Adobe or crafted and managed by the form author. 

    ![variation](/help/edge/docs/forms/universal-editor/assets/ue-variations.png){width=50%,height=50%}

 
    >[!NOTE]
    >
    > For instructions on using Generate Variations for forms, refer to the [Generate Variations](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/generative-ai/generate-variations) article

* **Experimentation**: 

    **Experimentation** refer to techniques used to test different variations of forms and layout  to optimize user experience and performance.
    ![experimentation](/help/edge/docs/forms/universal-editor/assets/ue-experimentation.png){width=50%,height=50%}


* **Personalization**
    The **Personalization** option configures the settings to establish a connection between the forms and Adobe Experience Platform (AEP) that are part of the Adobe ecosystem or external applications.
    ![Personalization](/help/edge/docs/forms/universal-editor/assets/ue-personalizaton.png){width=50%,height=50%}


* **A/B Testing**: 
    **A/B Testing** refer to techniques used to test different variations of forms and layout  to optimize user experience and performance.
    ![A/B Testing](/help/edge/docs/forms/universal-editor/assets/ue-abtesting.png){width=50%,height=50%}



* **Task Management**:
    The **Task Management** feature enables you to streamline workflows and enhance collaboration by allowing teams to manage, track, and execute tasks related to the customization and optimization of forms
    ![task management](/help/edge/docs/forms/universal-editor/assets/ue-taskmanagement.png){width=50%,height=50%}

.
* **Content Drafts**
    
    The **Content Drafts** option allows you to create drafts for rich text elements. Drafts can be created using existing form text or from scratch. You can edit or delete drafts as needed. By default, only three drafts are visible, but clicking **Show All** displays the rest.

    ![task management](/help/edge/docs/forms/universal-editor/assets/ue-contentdraft.png){width=50%,height=50%}


* **Data Source**
    
    The **Data Source** option allows you to configure data sources and select them when creating a Form Data Model (FDM). It makes all data model objects, properties, and services from the selected data sources available for use in the Form Data Model.
    ![Data Source](/help/edge/docs/forms/universal-editor/assets/ue-datasource.png){width=50%,height=50%}

* **Add**

    The **Add** option opens a drop-down list of components that can be added to the selected container. For example, in an Adaptive Form section, the list displays the available components that can be added to a form. The shortcut key to open the list of components is `a`.
    ![Add icon](/help/edge/docs/forms/universal-editor/assets/ue-add.png){width=50%,height=50%}

* **Duplicate**
    
    The **Duplicate** option creates a copy of the component, which is selected either in the content tree or the editor.
    ![Duplicate icon](/help/edge/docs/forms/universal-editor/assets/ue-duplicate.png){width=50%,height=50%}


* **Delete** 
    The **Delete** option deletes a component, which is selected either in the content tree or the editor.

    ![Delete](/help/edge/docs/forms/universal-editor/assets/ue-delete.png){width=50%,height=50%}

### Editor

The editor allows you to edit the form, and the form specified in the location bar is rendered in the editing area. If the editor is in preview mode, you can navigate the form using the available buttons and links.
![Editor](/help/edge/docs/forms/universal-editor/assets/ue-editor.png){width=50%,height=50%}

## See also

{{universal-editor-see-also}}
