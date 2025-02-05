---
title: Style System
description: The Style System allows a template author to define style classes in the content policy of a component so that a content author is able to select them when editing the component on a page. These styles can be alternative visual variations of a component, making it more flexible.
exl-id: 224928dd-e365-4f3e-91af-4d8d9f47efdd
solution: Experience Manager Sites
feature: Authoring
role: User
---
# Style System{#style-system}

The Style System allows a template author to define style classes in the content policy of a component so that a content author is able to select them when editing the component on a page. These styles can be alternative visual variations of a component, making the component more flexible.

This eliminates the need to develop a custom component for each style or to customize the component dialog to enable such style functionality. It leads to more reusable components that can be quickly and easily adapted to the needs of content authors without any AEM back-end development.

## Use Case {#use-case}

Template authors not only need the ability to configure how components function for the content authors, but also to configure several alternative visual variations of a component.

Likewise, content authors not only need the ability to structure and arrange their content, but also to select how it is presented visually.

The Style System provides a unified solution to both the template author's and content author's requirements:

* Template authors can define style classes in the content policy of components.
* Content authors can then select these classes from a drop-down list when editing the component on a page so they can apply the corresponding styles.

The style class is then inserted on the decoration wrapper element of the component so that the component developer does not need to be concerned with handling the styles beyond providing their CSS rules.

## Overview {#overview}

Using the Style System generally takes the following form.

1. The web designer creates different visual variations of a component.

1. The HTML developer is provided with the HTML output of the components and the desired visual variations to implement.  

1. The HTML developer defines the CSS classes that correspond to each visual variation and are to be inserted on the element wrapping the components.  

1. The HTML developer implements the corresponding CSS code (and optionally JS code) for each of the visual variations so that they look as defined.

1. The AEM developer places the provided CSS (and optional JS) in a [Client Library](/help/implementing/developing/introduction/clientlibs.md) and deploys it.

1. The AEM developer or template author configures the page templates and edits the policy of each styled component, adding the defined CSS classes, giving user-friendly names to each style, and indicating which styles can be combined.

1. The AEM page author can then choose the designed styles in the page editor via the style menu of the component's toolbar.

Only the last three steps are actually carried out in AEM. This means all development of the necessary CSS and JavaScript can be done without AEM.

Actually implementing the styles only requires deployment on AEM and selection within the components of the desired templates.

The following diagram illustrates the architecture of the Style System.

![aem-style-system](/help/sites-cloud/authoring/assets/style-system-architecture.png)

## Use {#use}

To demonstrate the feature, we will use [WKND](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-wknd-tutorial-develop/overview.html)'s implementation of the core component's [title component](https://www.adobe.com/go/aem_cmp_title_v2) as an example.

The following sections [As a Content Author](#as-a-content-author) and [As a Template Author](#as-a-template-author) describe how to test the functionality of the Style System using the Style System of WKND.

If you want to use the Style System for your own components do the following:

1. Install the CSS as client libraries as discussed in the section [Overview](#overview).
1. Configure the CSS classes that you want to make available to your content authors as described in the section [As a Template Author](#as-a-template-author).
1. Content authors can then use the styles as described in the section [As a Content Author](#as-a-content-author).

### As a Content Author {#as-a-content-author}

1. After installing the WKND project, navigate to WKND's English language master home page at `http://<host>:<port>/sites.html/content/wknd/language-masters/en` and edit the page.
1. Select a **Title** component further down the page

   ![Style System for the author](/help/sites-cloud/authoring/assets/style-system-author1.png)

1. Select the **Styles** button on the toolbar of the **List** component to open the style menu and change the appearance of the component.

   ![Selecting styles](/help/sites-cloud/authoring/assets/style-system-author2.png)

   >[!NOTE]
   >
   >In this example, the **Colors** styles (**Black**, **White**, and **Gray**) are mutually exclusive, while the **Style** options (**Underline**, **Align Right**, and **Mini Spacing**) can be combined. This can be [configured in the template as the template author](#as-a-template-author).

### As a Template Author {#as-a-template-author}

1. While editing WKND's English language master home page at `http://<host>:<port>/sites.html/content/wknd/language-masters/en`, edit the template of the page via **Page Information &gt; Edit Template**.

   ![Edit Template](/help/sites-cloud/authoring/assets/style-system-edit-template.png)

1. Edit the policy of the **Title** component by tapping or clicking the **Policy** button of the component.

   ![Edit policy](/help/sites-cloud/authoring/assets/style-system-edit-policy.png)

1. On the Styles tab of the properties, you can see how the styles have been configured.

   ![Edit properties](/help/sites-cloud/authoring/assets/style-system-properties.png)

    * **Group Name:** Styles can be grouped together within the style menu that the content author sees when configuring the style of the component.
    * **Styles can be combined:** Allows for multiple styles within that group to be selected at one time.
    * **Style Name:** The description of the style that will display to the content author when configuring the style of the component.
    * **CSS Classes:** The actual name of the CSS class associated with the style.

   Use the drag handles to arrange the order of the groups and the styles within the groups. Use the add or delete icons to add or remove groups or styles within the groups.

>[!CAUTION]
>
>The CSS classes &ndash; and any necessary JavaScript &ndash; configured as style properties of a component's policy, must be deployed as [Client Libraries](/help/implementing/developing/introduction/clientlibs.md) to work.

## Setup {#setup}

Core Components version 2 and later are fully enabled to take advantage of the Style System and require no additional configuration.

The following steps are only necessary to enable the Style System for your own custom components or to [enable the optional Styles tab in the Edit dialog](#enable-styles-tab-edit).

### Enable Style Tab in Design Dialog {#enable-styles-tab-design}

For a component to work with AEM's Style System and show the style tab in its design dialog, the component developer must include the style tab with the following settings on the component:

* `path = "/mnt/overlay/cq/gui/components/authoring/dialog/style/tab_design/styletab"`
* `sling:resourceType = "granite/ui/components/coral/foundation/include"`

>[!NOTE]
>This uses [overlays](/help/implementing/developing/introduction/overlays.md), by means of the [Sling Resource Merger](/help/implementing/developing/introduction/sling-resource-merger.md).

With the component configured, the styles configured by the page authors are automatically inserted by AEM on the decoration element that AEM automatically wraps around every editable component. The component itself need not do anything else to make this happen.

### Enable Styles Tab in Edit Dialog {#enable-styles-tab-edit}

An optional Styles tab in the Edit Dialog is also available. Unlike the Design Dialog tab, the tab in the Edit Dialog is not essential for the Style System to function, but is an optional alternative interface for a content author to set styles.

The edit dialog tab can be included in a similar way to the design dialog tab:

* `path = "/mnt/overlay/cq/gui/components/authoring/dialog/style/tab_edit/styletab"`
* `sling:resourceType = "granite/ui/components/coral/foundation/include"`

>[!NOTE]
>This uses [overlays](/help/implementing/developing/introduction/overlays.md), by means of the [Sling Resource Merger](/help/implementing/developing/introduction/sling-resource-merger.md).

>[!NOTE]
>
>The Styles tab on the Edit Dialog is not enabled by default.

### Styles with Element Names {#styles-with-element-names}

A developer can also configure a list of allowed element names for styles on the component with the `cq:styleElements` string array property. Then in the Styles tab of the policy within the design dialog, the template author can also choose an element name to be set for each style. This will set the element name of the wrapper element.

This property is set on the `cq:Component` node. For example:

* `/apps/<yoursite>/components/content/list@cq:styleElements=[div,section,span]`

>[!CAUTION]
>
>Avoid defining element names for styles that can be combined. When multiple element names are defined, the order of priority is:
>
>1. HTL takes precedence over everything: `data-sly-resource="${'path/to/resource' @ decorationTagName='span'}`
>1. Then among multiple active styles, the first style in the list of styles configured in the component's policy is taken.
>1. Finally, the component's `cq:htmlTag`/ `cq:tagName` is considered as a fallback value.
>

This ability to define style names is useful for generic components, like the Layout Container, or the Content Fragment component, to provide them with additional meaning.

For instance it allows a Layout Container to be given semantics like `<main>`, `<aside>`, `<nav>`, and so on.
