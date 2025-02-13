---
title: Editable Templates
description: Learn about how editable templates are used when creating a page, defining its initial content, structured content, authoring policies, and layout.
exl-id: ea42fce9-9af2-4349-a4e4-547e6e8da05c
feature: Developing
role: Admin, Architect, Developer
---
# Editable Templates {#editable-templates}

Learn about how editable templates are used when creating a page, defining its initial content, structured content, authoring policies, and layout.

## Overview {#overview}

When creating a page you need to select a template. The page template is used as the base for the new page. The template can define the structure of the resultant page, any initial content, and the components that can be used (design properties).

* Editable templates allow authors to create and use templates.
* Editable templates can be used to create pages that are editable with both the
  * [Page Editor](/help/sites-cloud/authoring/page-editor/templates.md) and
  * [Universal Editor](/help/sites-cloud/authoring/universal-editor/templates.md)

Pages templates used to create pages editable with the Universal Editor use a limited subset of editable template functionality. Therefore, the remainder of this document focuses on editable templates used to create pages that are editable with the Page Editor.

## Editable Templates and Pages Edited with the Page Editor {#page-editor}

When creating templates for creating pages that are editable with the Page Editor, normally specialized authors are identified.

* Such specialized authors are called **template authors**
* Template authors must be members of the `template-authors` group.
* Editable templates retain a dynamic connection to any pages created from them. This ensures that any changes to the template are reflected in the pages themselves.
* Editable templates make the page component more generic so the core page component can be used without customization.

With editable templates, the pieces that make a page are isolated within components. You can configure the necessary combinations of components in a UI, thereby eliminating the need for a new page component to be developed for each page variation.

This document:

* Gives an overview of creating an editable template
* Describes the admin/developer tasks required to create editable templates
* Describes the technical underpinnings of editable templates
* Describes how AEM evaluates a template's availability

>[!NOTE]
>
>This document assumes that you are already familiar with creating and editing templates. See the authoring document [Templates to Create Pages that are Editable with the Page Editor](/help/sites-cloud/authoring/page-editor/templates.md), which details the capabilities of editable templates as exposed to the template author.

>[!TIP]
>
>[The WKND tutorial](/help/implementing/developing/introduction/develop-wknd-tutorial.md) goes into depth into how to use editable templates by implementing an example and is quite useful for understanding how to set up a template in a new project

## Creating a New Editable Template {#creating-a-new-template}

Creating editable templates is primarily done with the [template console and template editor](/help/sites-cloud/authoring/page-editor/templates.md) by a template author. This section gives an overview of this process and follows with a description of what occurs at a technical level.

When creating an editable template you:

1. Create a [folder for the templates](#template-folders). This is not mandatory, but is recommended best practice.
1. Select a [template type](#template-type). This is copied to create the [template definition](#template-definitions).

   >[!NOTE]
   >
   >A selection of template types are provided out-of-the-box. You can also [create your own site-specific template types](#creating-template-types) if necessary.

1. Configure the structure, content policies, initial content, and layout of the new template.

   **Structure**

    * The structure allows you define components and content for your template.
    * Components defined in the template structure cannot be moved on a resulting page nor deleted from any resulting pages.
    * If you want page authors to be able to add and remove components, add a paragraph system to the template.
    * Components can be unlocked and locked again to allow you to define initial content.

   For details on how a template author defines the structure, see [Templates to Create Pages that are Editable with the Page Editor](/help/sites-cloud/authoring/page-editor/templates.md#editing-a-template-structure-template-author).

   For technical details of the structure, see [Structure](#structure) in this document.

   **Policies**

    * The content policies define the design properties of a component.

        * For example, the components available or minimum/maximum dimensions.

    * These are applicable to the template (and pages created with the template).

   For details on how a template author defines policies, see [Templates to Create Pages that are Editable with the Page Editor](/help/sites-cloud/authoring/page-editor/templates.md#editing-a-template-structure-template-author).

   For technical details of policies, see [Content Policies](#content-policies) in this document.

   **Initial Content**

    * Initial Content defines content that will appear when a page is first created based on the template.
    * Initial content can then be edited by page authors.

   For details on how a template author defines the structure, see [Templates to Create Pages that are Editable with the Page Editor](/help/sites-cloud/authoring/page-editor/templates.md#editing-a-template-initial-content-author).

   For technical details on initial content, see [Initial Content](#initial-content) in this document.

   **Layout**

    * You can define the template layout for a range of devices.
    * Responsive layout for templates operates as it does for page authoring.

   For details on how a template author defines the template layout, see [Templates to Create Pages that are Editable with the Page Editor](/help/sites-cloud/authoring/page-editor/templates.md#editing-a-template-layout-template-author).

   For technical details on template layout, see [Layout](#layout) in this document.

1. Enable the template, then allow it for specific content trees.

    * A template can be enabled or disabled to make it available or unavailable to page authors.
    * A template can be made available or unavailable for certain page branches.

   For details on how a template author enables a template, see [Templates to Create Pages that are Editable with the Page Editor](/help/sites-cloud/authoring/page-editor/templates.md#enabling-and-allowing-a-template-template-author).

   For technical details on enabling a template, see [Enabling and Allowing a Template for Us](#enabling-and-allowing-a-template-for-use)e in this document

1. Use it to create content pages.

    * When using a template to create a page there is no visible difference and no indication between static and editable templates.
    * For the page author, the process is transparent.

   For details on how a page author uses templates to create a page, see [Creating and Organizing Pages](/help/sites-cloud/authoring/sites-console/organizing-pages.md#templates).

   For technical details on creating pages with editable templates, see [Resultant Content Pages](#resultant-content-pages) in this document.

>[!TIP]
>
>Never enter any information that must be internationalized into a template. For internalization purposes, the [localization features of the Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/get-started/localization.html) are recommended.

>[!NOTE]
>
>Templates are powerful tools to streamline your page creation workflow. However too many templates can overwhelm the authors and make page creation confusing. A good rule of thumb is to keep the number of templates under 100.
>
>Adobe does not recommend having more than 1000 templates due to potential performance impacts.

>[!NOTE]
>
>The editor client library assumes the presence of the `cq.shared` namespace in content pages, and if it is absent the JavaScript error `Uncaught TypeError: Cannot read property 'shared' of undefined` will result.
>
>All sample content pages contain `cq.shared`, so any content based on them automatically includes `cq.shared`. However, if you decide to create your own content pages from scratch without basing them on sample content, you must make sure to include the `cq.shared` namespace.
>
>See [Using Client-Side Libraries](/help/implementing/developing/introduction/clientlibs.md) for further information.

## Template Folders {#template-folders}

For organizing your templates you can use the following folders:

* `global`
* Site-specific

>[!NOTE]
>
>Even though you can nest your folders, when the user views them in the **Templates** console they are presented as a flat structure.

In a standard AEM instance the `global` folder already exists in the template console. This holds default templates and acts as a fallback if no policies and/or template-types are found in the current folder. You can add your default templates to this folder or create a folder (recommended).

>[!NOTE]
>
>It is best practice to create a folder to hold your customized templates and not to use the `global` folder.

>[!CAUTION]
>
>Folders must be created by a user with `admin` rights.

Template types and policies are inherited across all folders according to the following order of precedence:

1. The current folder
1. Parent(s) of the current folder
1. `/conf/global`
1. `/apps`
1. `/libs`

A list of all allowed entries is created. If any configurations overlap ( `path`/ `label`), only the instance closest to the current folder is presented to the user.

To create a folder, you can either do this:

* Programmatically or with CRXDE Lite
* Using the [Configuration Browser](/help/implementing/developing/introduction/configurations.md#using-configuration-browser)

## Using CRXDE Lite {#using-crxde-lite}

1. A new folder (under /conf) can be created for your instance either programmatically or with CRXDE Lite.

   The following structure must be used:

   ```xml
   /conf
       <your-folder-name> [sling:Folder]
           settings [sling:Folder]
               wcm [cq:Page]
                   templates [cq:Page]
                   policies [cq:Page]
   ```

1. You can then define the following properties on the folder root node:

   `<your-folder-name> [sling:Folder]`

    * Name: `jcr:title`
    * Type: `String`
    * Value: The title (for the folder) you want to appear in the **Templates** console.

1. In addition to the standard authoring permissions and privileges (for example, `content-authors`) you now need to assign group(s) and define the required access rights (ACLs) for your authors to be able to create templates in the new folder.

   The `template-authors` group is the default group that must be assigned. See the section [ACLs and Groups](#acls-and-groups) for details.

   <!--See [Access Right Management](/help/sites-administering/user-group-ac-admin.md#access-right-management) for full details on managing and assigning access rights.-->

### Using the Configuration Browser {#using-the-configuration-browser}

1. Go to **Global Navigation** &gt; **Tools** &gt; [**Configuration Browser**](/help/implementing/developing/introduction/configurations.md#using-configuration-browser).

   The existing folders are listed to the left including the `global` folder.

1. Click **Create**.
1. In the **Create Configuration** dialog the following fields need to be configured:

    * **Title**: Provide a title for the configuration folder
    * **Editable Templates**: Tick to allow for editable templates within this folder

1. Click **Create**

>[!NOTE]
>
>In the [Configuration Browser](/help/implementing/developing/introduction/configurations.md#using-configuration-browser), you can edit the global folder and activate the **Editable Templates** option if you want to create templates within this folder, however this is not recommended best practice.

### ACLs and Groups {#acls-and-groups}

Once your template folders are created (either via CRXDE or with the Configuration Browser), ACLs must defined for the appropriate groups for the template folders to ensure proper security.

The template folders for the [WKND tutorial](/help/implementing/developing/introduction/develop-wknd-tutorial.md) can be used as an example.

#### The template-authors Group {#the-template-authors-group}

The `template-authors` group is the group used to manage access to templates and comes standard with AEM, but is empty. Users must be added to the group for the project/site.

>[!CAUTION]
>
>The `template-authors` group is only for users that must be able to create new templates.
>
>Editing templates is very powerful and if not done properly existing templates can be broken. Therefore this role should be focused and only include qualified users.

The following table details the necessary permissions for template editing.

<table>
 <tbody>
  <tr>
   <th>Path</th>
   <th>Role / Group</th>
   <th>Permissions<br /> </th>
   <th>Description</th>
  </tr>
  <tr>
   <td rowspan="3"><code>/conf/&lt;<i>your-folder</i>&gt;/settings/wcm/templates</code></td>
   <td>Template Authors<br /> </td>
   <td>read, write, replicate</td>
   <td>Template authors that create, read, update, delete, and replicate templates in site specific <code>/conf</code> space</td>
  </tr>
  <tr>
   <td>Anonymous Web User</td>
   <td>read</td>
   <td>Anonymous Web User must read templates while rendering a page</td>
  </tr>
  <tr>
   <td>Content Authors</td>
   <td>replicate</td>
   <td>replicateContent authors need to activate the templates of a page when activating a page</td>
  </tr>
  <tr>
   <td rowspan="3"><code>/conf/&lt;<i>your-folder</i>&gt;/settings/wcm/policies</code></td>
   <td><code>Template Author</code></td>
   <td>read, write, replicate</td>
   <td>Template authors that create, read, update, delete, and replicate templates in site specific <code>/conf</code> space</td>
  </tr>
  <tr>
   <td>Anonymous Web User</td>
   <td>read</td>
   <td>Anonymous Web User must read policies while rendering a page</td>
  </tr>
  <tr>
   <td>Content Authors</td>
   <td>replicate</td>
   <td>Content authors need to activate the policies of a template of a page when activating a page</td>
  </tr>
  <tr>
   <td rowspan="2"><code>/conf/&lt;site&gt;/settings/template-types</code></td>
   <td>Template Author</td>
   <td>read</td>
   <td>Template author creates a new template based on one of the predefined template types.</td>
  </tr>
  <tr>
   <td>Anonymous Web User</td>
   <td>none</td>
   <td>Anonymous Web User must not access the template types</td>
  </tr>
 </tbody>
</table>

This default `template-authors` group only covers the project setups, where all `template-authors` members are allowed to access and author all templates. For more complex setups, where multiple template authors groups are needed to separate access to templates, more custom template authors groups must be created. However the permissions for the template authors groups would still be the same.

## Template Type {#template-type}

When creating a template you need to specify a template type:

* Template types effectively provide templates for a template. When creating a template the structure and initial content of the selected template type is used to create to the new template.

  * The template type is copied to create the template.
  * Once the copy has occurred, the only connection between the template and the template type is a static reference for information purposes.

* Template types allow you to define:

  * The resource type of the page component.
  * The policy of the root node, which defines the components allowed in the template editor.
  * It is recommended to define the breakpoints for the responsive grid and setup of the mobile emulator at on the template type.

* AEM provides a small selection of out-of-the-box template types such as HTML5 Page and Adaptive Form Page.

  * Additional examples are provided as a part of the [WKND tutorial](/help/implementing/developing/introduction/develop-wknd-tutorial.md).

* Template types are typically defined by developers.

The out-of-the box template types are stored under:

* `/libs/settings/wcm/template-types`

>[!CAUTION]
>
>You must not change anything in the `/libs` path. This is because the content of `/libs` can be overwritten at any time by an update to AEM.

Your site-specific template types should be stored in the comparable location of:

* `/apps/settings/wcm/template-types`

Definitions for your customized templates types should be stored in user-defined folders (recommended) or alternatively in `global`. For example:

* `/conf/<my-folder-01>/<my-folder-02>/settings/wcm/template-types`
* `/conf/<my-folder>/settings/wcm/template-types`
* `/conf/global/settings/wcm/template-types`

>[!CAUTION]
>
>The template types have to respect the correct folder structure (that is, `/settings/wcm/...`), otherwise the template types will not be found.

<!--
### Template Type and Mobile Device Groups {#template-type-and-mobile-device-groups-br}

The [device groups](/help/sites-developing/mobile.md#device-groups) used for an editable template (set as relative path of the property `cq:deviceGroups`) define which mobile devices are available as emulators in the [layout mode](/help/sites-authoring/responsive-layout.md) of page authoring. This value can be set in two places:

* On the editable template type
* On the editable template

When creating an editable template, the value is copied from the template type to the individual template. If the value is not set on the type, it can be set on the template. Once a template is created, there is no inheritance from the type to the template.

>[!CAUTION]
>
>The value of `cq:deviceGroups` must be set as a relative path such as `mobile/groups/responsive` and not as an absolute path such as `/etc/mobile/groups/responsive`.

>[!NOTE]
>
>With static templates /help/sites-developing/page-templates-static.md, the value of `cq:deviceGroups` could be set at the root of the site.
>
>With editable templates, this value is now stored at the template level and is not supported at the page root level.
-->

### Creating Template Types {#creating-template-types}

If you have created a template that can serve as the basis of other templates, you can copy this template as a template type.

1. Create a template as you would any Page Template. See [Templates to Create Pages that are Editable with the Page Editor](/help/sites-cloud/authoring/page-editor/templates.md#creating-a-new-template-template-author). This will serve as the basis of your template type.
1. Using CRXDE Lite, copy the created template from the `templates` node to the `template-types` node under the [template folder](#template-folders).
1. Delete the template from the `templates` node under the [template folder](#template-folders).
1. In the copy of the template that is under the `template-types` node, delete all `cq:template` and `cq:templateType` properties from all `jcr:content` nodes.

You can also develop your own template type using an example editable template as a basis, available on GitHub.

CODE ON GITHUB

You can find the code of this page on GitHub

* [Open aem-sites-example-custom-template-type project on GitHub](https://github.com/Adobe-Marketing-Cloud/aem-sites-example-custom-template-type)
* Download the project as [a ZIP file](https://github.com/Adobe-Marketing-Cloud/aem-sites-example-custom-template-type/archive/master.zip)

## Template Definitions {#template-definitions}

Definitions for editable templates are stored [user-defined folders](#template-folders) (recommended) or alternatively in `global`. For example:

* `/conf/<my-folder>/settings/wcm/templates`
* `/conf/<my-folder-01>/<my-folder-02>/settings/wcm/templates`
* `/conf/global/settings/wcm/templates`

The root node of the template is of type `cq:Template` with a skeleton structure of:

```xml
<template-name>
  initial
    jcr:content
      root
        <component>
        ...
        <component>
  jcr:content
    @property status
  policies
    jcr:content
      root
        @property cq:policy
        <component>
          @property cq:policy
        ...
        <component>
          @property cq:policy
  structure
    jcr:content
      root
        <component>
        ...
        <component>
      cq:responsive
        breakpoints
  thumbnail.png
```

The main elements are:

* `<template-name>`

    * ` [initial](#initial-content)`
    * `jcr:content`
    * ` [structure](#structure)`
    * ` [policies](#policies)`
    * `thumbnail.png`

### jcr:content {#jcr-content}

This node holds properties for the template:

* **Name**: `jcr:title`
* **Name**: `status`
  * ``**Type**: `String`
  * **Value**: `draft`, `enabled` or `disabled`

### Structure {#structure}

Defines the structure of the resultant page:

* Is merged with the initial content ( `/initial`) when creating a page.
* Changes made to the structure are reflected in any pages created with the template.
* The `root` ( `structure/jcr:content/root`) node defines the list of components that are available in the resulting page.
  * Components defined in the template structure cannot be moved on or deleted from any resultant pages.
  * After a component is unlocked the `editable` property is set to `true`.
  * After a component that already contains content is unlocked, this content is moved to the `initial` branch.

* The `cq:responsive` node holds definitions for the responsive layout.

### Initial Content {#initial-content}

Defines the initial content that a new page will have upon creation:

* Contains a `jcr:content` node that is copied to any new pages.
* Is merged with the structure ( `/structure`) when creating a page.
* Any existing pages will not be updated if the initial content is changed after creation.
* The `root` node holds a list of components to define what is available in the resulting page.
* If content is added to a component in structure mode and that component is subsequently unlocked (or conversely), then this content is used as initial content.

### Layout {#layout}

When [editing a template you can define the layout](/help/sites-cloud/authoring/page-editor/templates.md), this uses [standard responsive layout](/help/sites-cloud/administering/responsive-layout.md), which can be [configured on the page by the content author](/help/sites-cloud/authoring/page-editor/responsive-layout.md).

### Content Policies {#content-policies}

The content policies define the design properties of a component. For example, the components available or minimum/maximum dimensions. These are applicable to the template (and pages created with the template). Content policies can be created and selected in the template editor.

* The property `cq:policy`, on the `root` node
  `/conf/<your-folder>/settings/wcm/templates/<your-template>/policies/jcr:content/root`
  Provides a relative reference to the content policy for the page's paragraph system.

* The property `cq:policy`, on the component-explicit nodes under `root`, provide links to the policies for the individual components.

* The actual policy definitions are stored under:
  `/conf/<your-folder>/settings/wcm/policies/wcm/foundation/components`

>[!NOTE]
>
>The paths of policy definitions depend on the path of the component. `cq:policy` holds a relative reference to the configuration itself.

### Page Policies {#page-policies}

Page policies allow you to define the [content policy](#content-policies) for the page (main parsys), in either the template or resultant pages.

### Enabling and Allowing a Template for Use {#enabling-and-allowing-a-template-for-use}

1. **Enable the Template**

   Before a template can be used it must be enabled by either:

    * [Enabling the template](/help/sites-cloud/authoring/page-editor/templates.md) from the **Templates** console.

    * Setting the status property on the `jcr:content` node.

        * For example, on:
          `/conf/<your-folder>/settings/wcm/templates/<your-template>/jcr:content`

        * Define the property:

            * Name: status
            * Type: String
            * Value: `enabled`

1. **Allowed Templates**

    * [Define the Allowed Template path(s) on the **Page Properties**](/help/sites-cloud/authoring/page-editor/templates.md#allowing-a-template-author) of the appropriate page or root page of a sub-branch.
    * Set the property:
      `cq:allowedTemplates`
      On the `jcr:content` node of the required branch.

   For example, with a value of:

   `/conf/<your-folder>/settings/wcm/templates/.*`

## Resultant Content Pages {#resultant-content-pages}

Pages created from editable templates:

* Are created with a subtree that is merged from `structure` and `initial` in the template

* Have references to information held in the template and template type. This is achieved with a `jcr:content` node with the properties:

  * `cq:template` - Provides the dynamic reference to the actual template; enables changes to the template to be reflected on the actual pages.

  * `cq:templateType` - Provides a reference to the template type.

![How templates, content, and components interrelate](assets/templates-content-components.png)

The above diagram shows how templates, content, and components interrelate:

* Controller - `/content/<my-site>/<my-page>` - The resultant page that references the template. The content controls the entire process. According to the definitions it accesses the appropriate template and components.
* Configuration - `/conf/<my-folder>/settings/wcm/templates/<my-template>` - The [template and related content policies](#template-definitions) define the page configuration.
* Model - OSGi bundles - The [OSGI bundles](/help/implementing/deploying/configuring-osgi.md) implement the functionality.
* View - `/apps/<my-site>/components` - On both the author and publish environments the content is rendered by components.

When rendering a page:

* **Templates**:

  * The `cq:template` property of its `jcr:content` node is referenced to access the template that corresponds to that page.

* **Components**:

  * The page component will merge the `structure/jcr:content` tree of the template with the `jcr:content` tree of the page.
    * The page component will only allow the author to edit the nodes of the template structure that have been flagged as editable (and any children).
    * When rendering a component on a page, the relative path of that component is taken from the `jcr:content` node; the same path under the `policies/jcr:content` node of the template will then be searched.
      * The `cq:policy` property of this node points to the actual content policy (that is, it holds the design configuration for that component).
        * This lets you have multiple templates that re-use the same content policy configurations.

### Template Availability {#template-availability}

When creating a page in the site admin interface, the list of available templates depends on the location of the new page and the restrictions on placement specified in each template.

The following properties determine whether a template `T` is allowed to be used for a new page to be placed as a child of page `P`. Each of these properties is a multi-value string holding zero or more Regular Expressions that are used for matching with paths:

* The `cq:allowedTemplates` property of the `jcr:content` subnode of `P` or an ancestor of `P`.

* The `allowedPaths` property of `T`.

* The `allowedParents` property of `T`.

* The `allowedChildren` property of the template of `P`.

The evaluation works as follows:

* The first non-empty `cq:allowedTemplates` property found while ascending the page hierarchy starting with `P` is matched against the path of `T`. If none of the values match, `T` is rejected.

* If `T` has a non-empty `allowedPaths` property, but none of the values match the path of `P`, `T` is rejected.

* If both of the above properties are either empty or non-existent, `T` is rejected unless it belongs to the same application as `P`. `T` belongs to the same application as `P` if and only if the name of the second level of the path of `T` is the same as the name of the second level of the path of `P`. For example, the template `/apps/wknd/templates/foo` belongs to the same application as the page `/content/wknd`.

* If `T` has an non-empty `allowedParents` property, but none of the values match the path of `P`, `T` is rejected.

* If the template of `P` has a non-empty `allowedChildren` property, but none of the values match the path of `T`, `T` is rejected.

* In all other cases, `T` is allowed.

The following diagram depicts the template evaluation process:

![Template evaluation process](assets/template-evaluation.png)

>[!CAUTION]
>
>AEM offers multiple properties to control the templates allowed under **Sites**. However, combining them can lead to very complex rules that are difficult to track and manage.
>
>Therefore, Adobe recommends that you start simple, by defining:
>
>* only the `cq:allowedTemplates` property
>
>* only on the site root
>
>For an example, see the [WKND tutorial](/help/implementing/developing/introduction/develop-wknd-tutorial.md) content: `/content/wknd/jcr:content`
>
>The properties `allowedPaths`, `allowedParents`, and `allowedChildren` can also be placed on the templates to define more sophisticated rules. However, when possible, it is *much* simpler to define further `cq:allowedTemplates` properties on sub-sections of the site if there is a need to further restrict the allowed templates.
>
>An additional advantage is that the `cq:allowedTemplates` properties can be updated by an author in the **Advanced** tab of the **Page Properties**. The other template properties cannot be updated using the (standard) UI, so would need a developer to maintain the rules and a code deployment for every change.

#### Limiting templates used in child pages {#limiting-templates-used-in-child-pages}

To limit what templates can be used to create child pages under a given page, use the `cq:allowedTemplates` property of `jcr:content` node of the page to specify the list of templates to be allowed as child pages. Each value in the list must be an absolute path to a template for an allowed child page, for example, `/apps/wknd/templates/page-content`.

You can use the `cq:allowedTemplates` property on the template's  `jcr:content` node to have this configuration applied to all created pages that use this template.

If you want to add more constraints, for example, regarding the template hierarchy, you can use the `allowedParents/allowedChildren` properties on the template. You can then explicitly specify that pages created from a template T have to be parents/children of pages created from a template T.
