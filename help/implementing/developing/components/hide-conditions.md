---
title: Using Hide Conditions
description: Hide conditions can be used to determine if a component resource is rendered or not.
exl-id: 2a96f246-fb0f-4298-899e-ebbf9fc1c96f
---
# Using Hide Conditions {#using-hide-conditions}

Hide conditions can be used to determine if a component resource is rendered or not. An example of this would be when an template author configures the Core Component [list component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/list.html) in the [template editor](/help/sites-cloud/authoring/features/templates.md) and decides to disable the options to build the list based on child pages. Disabling this option in the design dialog sets a property so that when the list component is rendered, the hide condition is evaluated and the option to show child pages is not displayed.

## Overview {#overview}

Dialogs can become very complex with numerous options for the user, who may only use a fraction of the options that are at their disposal. This can lead to overwhelming user interface experiences for users.

By using hide conditions, admins, developers, and super users have a way to hide resources based on a set of rules. This feature allows them to decide what resources should be displayed when an author edits content.

>[!NOTE]
>
>Hiding a resource based on an expression does not replace ACL permissions. Content remains editable but is simply not displayed.

## Implementation and Usage Details {#implementation-and-usage-details}

`com.adobe.granite.ui.components.FilteringResourceWrapper` is responsible filtering the resources based on the existence and value of the `granite:hide` property, located on the field to be filtered. The implementation of `/libs/cq/gui/components/authoring/dialog/dialog.jsp` includes an instance of `FilteringResourceWrapper.`

The implementation makes use of the Granite [ELResolver API](https://helpx.adobe.com/experience-manager/6-5/sites/developing/using/reference-materials/granite-ui/api/jcr_root/libs/granite/ui/docs/server/el.html) and adds a `cqDesign` custom variable via the ExpressionCustomizer.

Here are a few examples of hide conditions on a design node located either under `etc/design` or as a Content Policy.

```
${cqDesign.myProperty}
${!cqDesign.myProperty}
${cqDesign.myProperty == 'someText'}
${cqDesign.myProperty != 'someText'}
${cqDesign.myProperty == true}
${cqDesign.myProperty == true}
${cqDesign.property1 == 'someText' && cqDesign.property2 || cqDesign.property3 != 1 || header.myHeader}
```

When defining your hide expression keep in mind:

* To be valid, the scope in which property is found should be expressed (e.g. `cqDesign.myProperty`).
* Values are read only.
* Functions (if required) should be limited to a given set provided by the service.

## Example {#example}

Examples of hide conditions can be found throughout AEM and the [core components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html) in particular. For example, consider the [list core component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/list.html) as implemented in the [WKND tutorial.](/help/implementing/developing/introduction/develop-wknd-tutorial.md)

[Using the template editor](/help/sites-cloud/authoring/features/templates.md), the template author can define in the design dialog which options of the list component that are available to the page author. Such options as whether to allow the list to be a static list, a list of child pages, a list of tagged pages, etc. can be enabled or disabled.

If a template author chooses to disable the child pages option, a design property is set and a hide condition is evaluated against it, which causes the option to not render for the page author.

1. By default, the page author can use the list core component to build a list using child pages by choosing the option **Child pages**.

   ![List Component settings](assets/hide-conditions-list-settings.png)

1. In the design dialog of the list core component, the template author can choose the option **Disable Children** to prevent the option to generate a list based on child pages from being shown to the page author.

   ![List Component design dialog](assets/hide-conditions-list-design.png)

1. A policy node is created under `/conf/wknd/settings/wcm/policies/wknd/components/list` with a property `disableChildren` set to `true`.

   ![Node structure of hide condition](assets/hide-conditions-node-structure.png)

1. The hide condition is defined as the value of a `granite:hide` property on the dialog property node `/libs/core/wcm/components/list/v2/list/cq:dialog/content/items/tabs/items/listSettings/items/columns/items/column/items/listFrom/items/children`

   ![Evaluation of hide condition](assets/hide-conditions-evaluation.png)

1. The value of `disableChildren` is pulled from the design configuration and the expression `${cqDesign.disableChildren}` evaluates to `false`, meaning the option will not be rendered as part of the component.

1. The option **Child pages** is no longer rendered for the page author when using the list component.

   ![List Component with child option disabled](assets/hide-conditions-child-disabled.png)
