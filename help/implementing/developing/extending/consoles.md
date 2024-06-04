---
title: Customizing Consoles
description: Learn about the different options that AEM provides to customize the consoles of your authoring instance.
exl-id: 832f9a86-07c4-4229-a0dc-8ad50a8195b0
feature: Developing
role: "Admin, Architect, Developer"
---
# Customizing Consoles {#customizing-consoles}

AEM provides options to customize the consoles (and the [page authoring functionality](/help/implementing/developing/extending/page-authoring.md)) of your authoring instance.

## Clientlibs {#clientlibs}

Clientlibs allow you to extend the default implementation to offer new functionality, while reusing standard functions, objects, and methods. When customizing with clientlibs, you can create your own clientlib under `/apps.` For example, it can hold the code required for your custom component.

See [Using Client-Side Libraries on AEM as a Cloud Service](/help/implementing/developing/introduction/clientlibs.md).

## Overlays {#overlays}

Overlays are based on node definitions and allow you to overlay the standard functionality found under `/libs` with your own customized functionality under `/apps`. When creating an overlay, a 1:1 copy of the original is not required, as [Sling resource merger](/help/implementing/developing/introduction/sling-resource-merger.md) allows for inheritance.

Overlays can be used in many ways to extend your AEM consoles. Several examples are provided in the following sections.

See also [Overlays for Adobe Experience Manager as a Cloud Service](/help/implementing/developing/introduction/overlays.md).

>[!TIP]
>
>If you are interested in options to customize the authoring experience, see [Customizing Page Authoring](/help/implementing/developing/extending/page-authoring.md).

## Customizing the Default View for a Console {#customizing-the-default-view-for-a-console}

You can customize the default view (column, card, list) for a console:

* You can reorder the views by overlaying the required entry under:

  * `/libs/wcm/core/content/sites/jcr:content/views`

  * The first entry is the default.

  * The nodes available correlate to the view options available:

    * `column`
    * `card`
    * `list`

* For example, in an overlay for a list:

  * `/apps/wcm/core/content/sites/jcr:content/views/list`

  * Define the following property:

    * **Name**: `sling:orderBefore`
    * **Type**: `String`
    * **Value**: `column`

### Add a New Action to the Toolbar {#add-a-new-action-to-the-toolbar}

You can build your own components and include the corresponding client libraries for custom actions.

* For example, you may want to create a **Promote to Social Media** action at:

  * `/apps/wcm/core/clientlibs/sites/js/socialmedia.js`

  * This can then be connected to a toolbar item on your console:

  * `/apps/<yourProject>/admin/ext/launches`

  * For example, in selection mode:

  * `content/jcr:content/body/content/header/items/selection/items/socialmedia`

### Restrict a Toolbar Action to a Specific Group {#restrict-a-toolbar-action-to-a-specific-group}

You can use a custom rendering condition to overlay the standard action and impose specific conditions that must be fulfilled before it is rendered.

For example, you may want to create a component to control the render conditions according to a group:

* `/apps/myapp/components/renderconditions/group`

To apply these to the **Create Site** action on the sites console:

* `/libs/wcm/core/content/sites`

1. Create the overlay:

   * `/apps/wcm/core/content/sites`

1. Then add the render condition for the action:

   * `jcr:content/body/content/header/items/default/items/create/items/createsite/rendercondition`

Using properties on this node you can define the `groups` allowed to perform the specific action; for example, `administrators`

### Customizing Columns in List View {#customizing-columns-in-list-view}

To customize the columns in the list view:

1. Overlay the list of available columns.

    * On the node:

      `/apps/wcm/core/content/common/availablecolumns`

1. Add your new columns or remove existing ones.

If you want to insert additional data, you need to write a [PageInfoProvider](https://developer.adobe.com/experience-manager/reference-materials/cloud-service/javadoc/com/day/cq/wcm/api/PageInfoProvider.html) with a `pageInfoProviderType` property.

>[!NOTE]
>
>This feature is optimized for columns of text fields. For other data types it is possible to overlay `cq/gui/components/siteadmin/admin/listview/columns/analyticscolumnrenderer` in `/apps`.

### Filtering Resources {#filtering-resources}

When using a console, a user must often select from resources such as pages, components, or assets. This can take the form of a list from which the author must choose an item.

To keep the list to a reasonable size and also relevant to the use case, a filter can be implemented in the form of a custom predicate. See [Customizing Page Authoring](/help/implementing/developing/extending/page-authoring.md#filtering-resources) for details.
