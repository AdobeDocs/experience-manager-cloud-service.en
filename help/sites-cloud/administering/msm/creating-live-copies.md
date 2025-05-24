---
title: Creating and Synchronizing Live Copies
description: Learn how to create and synchronize Live Copies to reuse your content across your site.
feature: Multi Site Manager
role: Admin
exl-id: 53ed574d-e20d-4e73-aaa2-27168b9d05fe
solution: Experience Manager Sites
---
# Creating and Synchronizing Live Copies {#creating-and-synchronizing-live-copies}

You can create a Live Copy from a page or blueprint configuration to reuse that content across your site. Manage inheritance and synchronization, you can control how changes to the content are propagated.

## Managing Blueprint Configurations {#managing-blueprint-configurations}

A blueprint configuration identifies an existing website that you want to use as the source for one or more Live Copy pages.

>[!TIP]
>
>Blueprint configurations enable you to push content changes to Live Copies. See [Live Copies - Source, Blueprints and Blueprint Configurations](overview.md#source-blueprints-and-blueprint-configurations).

When you create a blueprint configuration, you select a template that defines the internal structure of the blueprint. The default blueprint template assumes that the source website has the following characteristics:

* The web site has a root page.
* The immediate child pages of the root are language branches of the web site. When creating a Live Copy, the languages are presented as optional content to include in the copy.
* The root of each language branch has one or more child pages. When creating a Live Copy, child pages are presented so that you can include in the Live Copy.

>[!NOTE]
>
>A different structure requires a different blueprint template.

After you create the blueprint configuration, you configure the following properties:

* **Name**: The name of the blueprint configuration
* **Source Path**: The path of the root page of the site that you are using as the source (blueprint)
* **Description**. (Optional) A description of the blueprint configuration, which appears in the list of blueprint configurations to choose from when creating a site

When your blueprint configuration is used, you can associate it with a rollout configuration that determines how the Live Copies of the source/blueprint are synchronized. See [Specifying the Rollout Configurations To Use](live-copy-sync-config.md#specifying-the-rollout-configurations-to-use).

### Creating and Editing Blueprint Configurations {#creating-editing-blueprint-configurations}

Blueprint configurations are considered immutable data and as such are not editable at runtime. For this reason, any configuration changes must be deployed via Git using the CI/CD pipeline.

More information can be found in the article [Notable Changes to Adobe Experience Manager (AEM) as a Cloud Service](/help/release-notes/aem-cloud-changes.md).

The following steps are available to an administrator on a local development instance only for testing and development purposes. These options are not available in any AEMaaCS cloud instance.

#### Creating a Blueprint Configuration Locally {#creating-a-blueprint-configuration}

To create a blueprint configuration:

1. [Navigate](/help/sites-cloud/authoring/basic-handling.md#global-navigation) to the **Tools** menu, then select the **Sites** menu.
1. Select **Blueprints** to open the **Blueprint Configurations** console:

   ![Blueprint configurations](../assets/blueprint-configurations.png)

1. Select **Create**.
1. Select the blueprint template, then **Next** to continue.
1. Select the source page to be used as the blueprint; then **Next** to continue.
1. Define:

    * **Title**: mandatory title for the blueprint
    * **Description**: an optional description to provide more details.

1. **Create** will create the blueprint configuration based on your specification.

### Editing or Deleting a Blueprint Configuration Locally{#editing-or-deleting-a-blueprint-configuration}

You can edit or delete an existing blueprint configuration:

1. [Navigate](/help/sites-cloud/authoring/basic-handling.md#global-navigation) to the **Tools** menu, then select the **Sites** menu.
1. Select **Blueprints** to open the **Blueprint Configurations** console:

   ![Blueprint configurations](../assets/blueprint-configurations.png)

1. Select the required blueprint configuration - the appropriate actions become available in the toolbar:

    * **Properties**; you can use this to view and then edit the properties of the configuration.
    * **Delete**

## Creating a Live Copy {#creating-a-live-copy}

There are several ways to create a Live Copy.

### Creating a Live Copy of a Page {#creating-a-live-copy-of-a-page}

You can create a Live Copy of any page or branch. When you create the Live Copy, you can specify the rollout configurations to use for synchronizing the content:

* The selected rollout configurations apply to the Live Copy page and its child pages.
* If you do not specify any rollout configurations, MSM determines which rollout configurations to use. See [Specifying the Rollout Configuration To Use](live-copy-sync-config.md#specifying-the-rollout-configurations-to-use).

You can create a Live Copy of any page:

* Pages that are referenced by a [blueprint configuration](#creating-a-blueprint-configuration)
* And pages that have no connection to a configuration
* Live Copy within the pages of another Live Copy ([nested Live Copies](overview.md#nested-live-copies))

The only difference is that availability of the **Rollout** command on the source/blueprint pages is dependent on whether source is referenced by a blueprint configuration:

* If you create the Live Copy from a source page that **is** referenced in a blueprint configuration, then the Rollout command is available on the source/blueprint page(s).
* If you create the Live Copy from a source page that **is not** referenced in a blueprint configuration, then the Rollout command will not be available on the source/blueprint page(s).

To create a Live Copy:

1. In the **Sites** console select **Create**, then **Live Copy**.

   ![Create Live Copy](../assets/create-live-copy.png)

1. Select the source page then select **Next**. For example:

   ![Select Live Copy source](../assets/live-copy-from.png)

1. Specify the destination path of the Live Copy (open the parent folder/page of the Live Copy) and then select **Next**.

   ![Select Live Copy destination](../assets/live-copy-to.png)

   >[!NOTE]
   >
   >The destination path cannot be within the source path.

1. Enter:

    * a **Title** for the page.
    * a **Name**, that is used in the URL.

   ![Live Copy properties](../assets/live-copy-properties.png)

1. Use the **Exclude sub pages** checkbox:

    * Selected: create a Live Copy of the selected page only (shallow Live Copy)
    * Not Selected: create a Live Copy that includes all descendants of the selected page (deep Live Copy)

1. (Optional) To specify one or more rollout configurations to use for the Live Copy, use the **Rollout Configs** drop-down list to select them. Selected configurations are shown underneath the drop-down selector.
1. Select **Create**. A confirmation message is shown, from here you can select either **Open** or **Done**.

   >[!NOTE]
   >
   >An error dialog may appear with the message "Fail to submit the form". This happens due to a network timeout. However, the process to create the live copy is running in the background. Wait a few minutes and check the pages of the live copy were correctly created.

### Creating a Live Copy of a Site from a Blueprint Configuration {#creating-a-live-copy-of-a-site-from-a-blueprint-configuration}

Create a Live Copy using a blueprint configuration to create a site based on the blueprint (source) content. When you create a Live Copy from a blueprint configuration, you select one or more language branches of the blueprint source to copy, then you select the chapters to copy from the language branches. See [Creating a Blueprint Configuration](#creating-a-blueprint-configuration).

If you omit some language branches from the Live Copy, you can add them later. See [Creating a Live Copy Inside a Live Copy (Blueprint Configuration)](#creating-a-live-copy-inside-a-live-copy-blueprint-configuration) for details.

>[!CAUTION]
>
>When the blueprint source contains links and references that target a paragraph in a different branch, the targets are not updated in the Live Copy pages, but remain pointed to the original destination.

When you create the site, provide values for the following properties:

* **Initial Languages**: The language branches of the blueprint source to include in the Live Copy
* **Initial Chapters**: The child pages of the blueprint language branches to include in the Live Copy
* **Destination Path**: The location of the root page of the Live Copy site
* **Title**: The title of the root page of the Live Copy site
* **Name**: (Optional) The name of the JCR node that stores the root page of the Live Copy (the default value is based on the title)
* **Site Owner**: (Optional) Information about the party responsible for the Live Copy
* **Live Copy**: Select this option to establish a live relationship with the source site. If you do not select this option, a copy of the blueprint is created but is not subsequently synchronized with the source.
* **Rollout Configs**: (Optional) Select one or more rollout configurations to use for synchronizing the Live Copy. By default, the rollout configurations are inherited from the blueprint. See [Specifying the Rollout Configurations to Use](live-copy-sync-config.md#specifying-the-rollout-configurations-to-use) for more details.

To create a Live Copy of a site from a blueprint configuration:

1. In the **Sites** console, select **Create**, then **Site** from the drop-down selector.
1. Select the blueprint configuration to use as the source of the Live Copy and proceed with **Next**:

   ![Create site from blueprint](../assets/create-site-from-blueprint.png)

1. Use the **Initial Languages** selector to specify the languages of the blueprint site to use for the Live Copy.

   All available languages are selected by default. To remove a language, select the **X** that appears next to the language.

   For example:

   ![Specify properties when creating site](../assets/create-site-properties.png)

1. Use the **Initial Chapters** drop-down to select the sections of the blueprint to include in the Live Copy. All available chapters are included by default, but can be removed.
1. Provide values for the remaining properties and then select **Create**. In the confirmation dialog box, select **Done** to return to the **Sites** console, or **Open Site** to open the root page of the site.

### Creating a Live Copy Inside a Live Copy (Blueprint Configuration) {#creating-a-live-copy-inside-a-live-copy-blueprint-configuration}

When you create a Live Copy inside the existing Live Copy (created using a blueprint configuration), you can insert any language copy or chapters that were not included when the Live Copy was originally created.

## Monitoring your Live Copy {#monitoring-your-live-copy}

### Seeing the Status of a Live Copy {#seeing-the-status-of-a-live-copy}

The properties of a Live Copy page show the following information about the Live Copy:

* **Source**: The source page of the Live Copy page
* **Status**: The synchronization status of the Live Copy including whether the Live Copy is up to date with the source, when the last synchronization occurred, and who performed the synchronization
* **Configuration**:

  * Whether the page is still subject to Live Copy inheritance
  * Whether the configuration is inherited from the parent page
  * Any rollout configurations that the Live Copy uses

To view the properties:

1. In the **Sites** console, select the Live Copy page and open the properties.
1. Select the **Live Copy** tab.

   For example:

   ![Live Copy tab in page properties](../assets/live-copy-inherit.png)

   See the section [Using the Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview) in the article Live Copy Overview Console for more details.

### Seeing the Live Copies of a Blueprint Page {#seeing-the-live-copies-of-a-blueprint-page}

Blueprint pages (that are referenced in a blueprint configuration) provide you with a list of the Live Copy pages that use the current (blueprint) page as the source. Use this list to keep track of the Live Copies. The list appears on the **Blueprint** tab of the [page properties](/help/sites-cloud/authoring/sites-console/page-properties.md).

![Blueprint tab of page properties](../assets/live-copy-blueprint-tab.png)

## Synchronizing your Live Copy {#synchronizing-your-live-copy}

There are several ways to synchronize your Live Copy.

### Rolling Out a Blueprint {#rolling-out-a-blueprint}

Roll out a blueprint page to push content changes to Live Copies. A **Rollout** action executes the rollout configurations that use the [On Rollout](live-copy-sync-config.md#rollout-triggers) trigger.

>[!NOTE]
>
>Conflicts can occur if new pages with the same page name are created in both the blueprint branch and a dependent Live Copy branch.
>
>Such [conflicts need to be handled and resolved upon rollout](rollout-conflicts.md).

#### Rolling Out a Blueprint from Page Properties {#rolling-out-a-blueprint-from-page-properties}

1. In the **Sites** console, select the page in the blueprint and open the properties.
1. Open the **Blueprint** tab.
1. Select **Rollout**.

   ![Rollout button](../assets/rollout.png)

1. Specify the pages and any sub-pages, then confirm with the check mark:

   ![Select pages to roll out](../assets/select-rollout-pages.png)

1. Specify if the rollout job should be executed immediately (**Now**) or at another date/time (**Later**).

   ![Define rollout time](../assets/rollout-now-later.png)

Rollouts are processed as asynchronous jobs and can be checked on the [***Async Jobs Status** page](/help/operations/asynchronous-jobs.md#monitor-the-status-of-asynchronous-operations).

#### Roll Out a Blueprint from the Reference Rail {#roll-out-a-blueprint-from-the-reference-rail}

1. In the **Sites** console, select the page in the live copy and open the **[References](/help/sites-cloud/authoring/basic-handling.md#references)** panel (from the toolbar).
1. Select the **Blueprint** option from the list, to show the blueprints associated with this page.
1. Select the required blueprint from the list.
1. Select **Rollout**.

   ![Rollout blueprint from references rail](../assets/rollout-blueprint-from-references.png)

1. You are asked to confirm details of the rollout:

    * **Rollout scope**:

      Specify whether the scope is for the selected page alone, or should include subpages.

    * **Schedule**:

      Specify if the rollout job should be executed immediately (**Now**) or at a later date/time (**Later**).

      ![Define rollout scope and schedule](../assets/rollout-scope-schedule.png)

1. After confirming these details, select **Rollout** to perform the action.

Rollouts are processed as asynchronous jobs and can be checked on the [**Async Jobs Status** page](/help/operations/asynchronous-jobs.md#monitor-the-status-of-asynchronous-operations).

#### Roll Out a Blueprint from the Live Copy Overview {#roll-out-a-blueprint-from-the-live-copy-overview}

The [**Rollout** action is also available from the Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview), when a Blueprint page is selected.

1. Open the [Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview) and select a Blueprint Page.
1. Select **Rollout** from the toolbar.

   ![Live Copy overview](../assets/live-copy-overview-actions-blueprint.png)

1. Specify the pages and any sub-pages, then confirm with the check mark:

   ![Select pages for rollout](../assets/select-rollout-pages.png)

1. Specify if the rollout job should be executed immediately (**Now**) or at another date/time (**Later**).

   ![Define rollout schedule](../assets/rollout-now-later.png)

Rollouts are processed as asynchronous jobs and can be checked on the [**Async Jobs Status** page](/help/operations/asynchronous-jobs.md#monitor-the-status-of-asynchronous-operations).

### Synchronizing a Live Copy {#synchronizing-a-live-copy}

Synchronize a Live Copy page to pull content changes from the source to the Live Copy.

#### Synchronize a Live Copy from Page Properties {#synchronize-a-live-copy-from-page-properties}

Synchronize a Live Copy to pull changes from the source to the Live Copy.

>[!NOTE]
>
>Synchronizing executes the rollout configurations that use the [On Rollout](live-copy-sync-config.md#rollout-triggers) trigger.

1. In the **Sites** console, select the Live Copy page and open the properties.
1. Open the **Live Copy** tab.
1. Select **Synchronize**.

   ![Synchronize button](../assets/synchronize.png)

   Confirmation is requested, use **Sync** to proceed.

#### Synchronize a Live Copy from the Live Copy Overview {#synchronize-a-live-copy-from-the-live-copy-overview}

The [Synchronize action is also available from the Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview), when a Live Copy page is selected.

1. Open the [Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview) and select a Live Copy Page.
1. Select **Synchronize** from the toolbar.
1. Confirm the **Rollout** action in the dialog after specifying whether you want to include:

    * **Page and Sub Pages**
    * **Page Only**

   ![Rollout pages with or without subpages](../assets/rollout-page-and-subpages.png)

## Changing Live Copy Content {#changing-live-copy-content}

To change Live Copy content, you can:

* Add paragraphs to the page.
* Update existing content by breaking the Live Copy inheritance for any page or component.

>[!TIP]
>
>If you manually create a page in the Live Copy, the new page is local to the Live Copy, meaning it does not have a corresponding source page to which it is attached.
>
>As a best practice so you can create a local page that is part of the relationship is to create the local page in the source and perform a deep rollout. This will create the page locally as Live Copies.

>[!NOTE]
>
>Conflicts can occur if new pages with the same page name are created in both the blueprint branch and a dependent Live Copy branch.
>
>Such [conflicts need to be handled and resolved upon rollout](rollout-conflicts.md).

### Adding Components to a Live Copy Page {#adding-components-to-a-live-copy-page}

You can add components to a Live Copy page at any time. The inheritance status of the Live Copy and its paragraph system does not control your ability to add components.

When the Live Copy page is synchronized with the source page, the added components remain unchanged. See also [Changing the Order of Components on a Live Copy Page](#changing-the-order-of-components-on-a-live-copy-page).

>[!TIP]
>
>Changes made locally to a component marked as a container will not be overwritten by the content of the blueprint on a rollout. See [MSM Best Practices](best-practices.md#components-and-container-synchronization) for more information.

### Suspending Inheritance for a Page {#suspending-inheritance-for-a-page}

When you create a Live Copy, the Live Copy configuration is saved on the root page of the copied pages. All child pages of the root page inherit the Live Copy configurations. The components on the Live Copy pages also inherit the Live Copy configuration.

You can suspend the Live Copy inheritance for a Live Copy page so that you can change page properties and components. When you suspend inheritance, the page properties and components are no longer synchronized with the source.

>[!TIP]
>
>You can also [detach a Live Copy](#detaching-a-live-copy) from its blueprint to remove all connections. Unlike suspending inheritance, the detach action is permanent and non-reversible.

#### Suspending Inheritance from Page Properties {#suspending-inheritance-from-page-properties}

To suspend inheritance on a page:

1. Open the properties of the Live Copy page either using the **View Properties** command of the **Sites** console or using **Page Information** on the page toolbar.
1. Select the **Live Copy** tab.
1. Select **Suspend** from the toolbar. You can then select either:

    * **Suspend**: to suspend current page only.
    * **Suspend with children**: to suspend the current page together with any child pages.

1. Select **Suspend** on the confirmation dialog.

#### Suspending Inheritance from the Live Copy Overview {#suspending-inheritance-from-the-live-copy-overview}

The [Suspend action is also available from the Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview), when a Live Copy page is selected.

1. Open the [Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview) and select a Live Copy Page.
1. Select **Suspend** from the toolbar.
1. Select the appropriate option from:

    * **Suspend**
    * **Suspend with children**

   ![Suspend with children](../assets/suspend-with-children.png)

1. Confirm the **Suspend** action in the **Suspend Live Copy** dialog:

   ![Confirm suspension](../assets/confirm-suspend.png)

### Resuming Inheritance for a Page {#resuming-inheritance-for-a-page}

Suspending Live Copy inheritance for a page is a temporary action. Once suspended the **Resume** action becomes available, allowing you to reinstate the live relationship.

![Resume inheritance](../assets/resume-inheritance.png)

When you re-enable inheritance, the page is not automatically synchronized with the source. You can request a synchronization, if this is required, either:

* In the **Resume**/**Revert** dialog; for example:

  ![Resume and synchronize](../assets/resume-and-synch.png)

* At a later stage, by manually selecting the synchronize action.

>[!NOTE]
>
>When you re-enable inheritance, the page is not automatically synchronized with the source. If this is required, you can manually request a synchronization either at the time of resuming or later.

#### Resuming Inheritance from Page Properties {#resuming-inheritance-from-page-properties}

Once [suspended](#suspending-inheritance-from-page-properties) the **Resume** action becomes in the toolbar of the page properties:

![Resume button](../assets/resume.png)

When selected, the dialog box is shown. You can select a synchronization, if necessary, then confirm the action.

#### Resume a Live Copy Page from the Live Copy Overview {#resume-a-live-copy-page-from-the-live-copy-overview}

The [Resume action is also available from the Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview), when a Live Copy page is selected.

1. Open the [Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview) and select a suspended Live Copy Page. The page is shown as **INHERITANCE CANCELLED**.
1. Select **Resume** from the toolbar.
1. Indicate whether you want to synchronize the page after reverting inheritance, then confirm the **Resume** action in the **Resume Live Copy** dialog.

### Changing Inheritance Depth (Shallow/Deep) {#changing-inheritance-depth-shallow-deep}

On an existing Live Copy you can change the depth for a page, that is, whether child pages are included.

* Switching to a shallow Live Copy:

  * Will have immediate effect and is non-reversible.

  * Detaches child pages explicitly from the Live Copy. Further modifications on children cannot be preserved if undone.

  * Will remove any descendant `LiveRelationships` even if there are nested `LiveCopies`.

* Switching to a deep Live Copy:

  * Leaves child-pages untouched.
  * To see the effect of the switch, you can make a roll-out, any content modifications are applied according the roll-out configuration.

* Switching to a shallow Live Copy, then back to deep:

  * Treats all children of the (formerly) shallow Live Copy as if they had been created manually and are therefore moved away using `[oldname]_msm_moved name`.

To specify or change the depth:

1. Open the properties of the Live Copy page either using the **View Properties** command of the **Sites** console or using **Page Information** on the page toolbar.
1. Select the **Live Copy** tab.
1. In the **Configuration** section, set or clear the **Live Copy Inheritance** option depending on whether child pages are included:

    * Checked - a deep Live Copy (the child pages are included)
    * Unchecked - a shallow Live Copy (child pages are excluded)

   >[!CAUTION]
   >
   >Switching to a shallow Live Copy will have immediate effect and is non-reversible.
   >
   >See [Live Copies - Composition](overview.md#live-copies-composition) for more information.

1. Select **Save** to persist your updates.

### Cancelling Inheritance for a Component {#cancelling-inheritance-for-a-component}

Cancel the Live Copy inheritance for a component so that the component is no longer synchronized with the source component. You can enable inheritance at a later point if necessary.

>[!NOTE]
>
>When you re-enable inheritance, the component is not automatically synchronized with the source. You can manually request a synchronization if this is required.

Cancel inheritance to change the component content or delete the component:

1. Select the component for which you want to cancel inheritance.

   ![Inheritance in the component toolbar](../assets/inheritance-toolbar.png)

1. On the component toolbar, select the **Cancel Inheritance** icon.

   ![Cancel inheritance icon](../assets/cancel-inheritance-icon.png)

1. In the Cancel Inheritance dialog box, confirm the action with **Yes**.

   The component toolbar is updated to include all (appropriate) editing commands.

### Re-Enabling Inheritance for a Component {#re-enabling-inheritance-for-a-component}

To enable inheritance for a component, select the **Re-enable Inheritance** icon on the component toolbar.

![Re-enable inheritance icon](../assets/re-enable-inheritance-icon.png)

### Changing the Order of Components on a Live Copy Page {#changing-the-order-of-components-on-a-live-copy-page}

If a Live Copy contains components that are part of a paragraph system, the inheritance of that paragraph system observes the following rules:

* The order of components in an inherited paragraph system can be modified, even with inheritance established.
* On rollout, the order of the components are restored from the blueprint. If new components were added to the Live Copy before rollout, they are reordered along with the components above which they were added.
* If inheritance of the paragraph system is cancelled, the order of components will not be restored on rollout and will remain as-is in the Live Copy.

>[!NOTE]
>
>When reverting a cancelled inheritance on a paragraph system, the order of components **will not be automatically restored** from the blueprint. You can manually request a synchronization if this is required.

Use the following procedure to cancel inheritance of the paragraph system.

1. Open the Live Copy page.
1. Drag an existing component to a new location on the page.
1. In the **Cancel Inheritance** dialog box, confirm the action with **Yes**.

### Overriding Properties of a Live Copy Page {#overriding-properties-of-a-live-copy-page}

The page properties of a Live Copy page are inherited from the source page by default and are not editable.

You can cancel inheritance for a property when you need to change the property value for the Live Copy. A link icon indicates that inheritance is enabled for the property.

![Inherited page properties](../assets/properties-inherited.png)

When you cancel inheritance, you can change the property value. A broken-link icon indicates that inheritance is cancelled.

![Properties not inherited](../assets/properties-not-inherited.png)

You can later re-enable inheritance for a property if necessary.

>[!NOTE]
>
>When you re-enable inheritance, the Live Copy page property is not automatically synchronized with the source property. You can manually request a synchronization if this is required.

1. Open the properties of the Live Copy page using either the **View Properties** option of the **Sites** console or **Page Information** icon on the page toolbar.
1. To cancel inheritance of a property, select the link icon that appears to the right of the property.

   ![Cancel inheritance button](../assets/cancel-inheritance-button.png)

1. In the **Cancel Inheritance** confirmation dialog, select **Yes**.

### Revert Properties of a Live Copy Page {#revert-properties-of-a-live-copy-page}

To enable inheritance for a property, select the **Revert Inheritance** icon that appears next to the property.

![Revert inheritance button](../assets/revert-inheritance-button.png)

### Resetting a Live Copy Page {#resetting-a-live-copy-page}

You can reset a Live Copy page to do the following:

* Remove all inheritance cancellations and
* Return the page to the same state as the source page.

Resetting affects changes that you have made to page properties, the paragraph system, and components.

#### Reset a Live Copy Page from the Page Properties {#reset-a-live-copy-page-from-the-page-properties}

1. In the **Sites** console, select the Live Copy page and select **View Properties**.
1. Open the **Live Copy** tab.
1. Select **Reset** from the toolbar.

   ![Reset button](../assets/reset.png)

1. In the **Reset Live Copy** dialog box, confirm with **Reset**.

#### Reset a Live Copy Page from the Live Copy Overview {#reset-a-live-copy-page-from-the-live-copy-overview}

The [**Reset** action is also available from the Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview), when a Live Copy page is selected.

1. Open the [Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview) and select a Live Copy Page.
1. Select **Reset** from the toolbar.
1. Confirm the **Reset** action in the **Reset Live Copy** dialog:

   ![Confirm Live Copy reset](../assets/reset-live-copy.png)

## Comparing a Live Copy Page with a Blueprint Page {#comparing-a-live-copy-page-with-a-blueprint-page}

To track the changes you have made, you can view the blueprint page in **References** and compare it with its Live Copy page:

1. In the **Sites** console, [navigate to a blueprint or Live Copy page and select it](/help/sites-cloud/authoring/basic-handling.md#viewing-and-selecting-resources).
1. Open the **[References](/help/sites-cloud/authoring/basic-handling.md#references)** panel and depending on context select either:

    * **Blueprint**
    * **Live Copies**

1. Select your specific Live Copy depending on context select either:

    * **Compare to Blueprint**
    * **Compare to Live Copy**

   For example:

   ![Comparing Live Copies](../assets/compare-live-copy.png)

1. The Live Copy and blueprint pages are opened side-by-side.

   For full information about using the comparison feature see [Page Diff](/help/sites-cloud/authoring/sites-console/page-diff.md).

## Detaching a Live Copy {#detaching-a-live-copy}

The detach action permanently removes the live relationship between a Live Copy and its source/blueprint page. All MSM-relevant properties are removed from the Live Copy and the Live Copy pages become a standalone copy.

>[!CAUTION]
>
>You cannot reinstate the live relationship after you detach the Live Copy.
>
>To remove the live relationship with the option of later reinstating it, you can [cancel Live Copy inheritance](#suspending-inheritance-for-a-page) for the page.

There are implications on where within the tree that you use **Detach**:

* **Detach on a Root Page of a Live Copy**

  When this operation is performed on the root page of a Live Copy it removes the live relationship between all pages of the blueprint and its Live Copy.

  Further changes to pages in the blueprint **will not** impact the Live Copy.

* **Detach on a Sub-Page of a Live Copy**

  When this operation is performed on a sub-page (or branch) within a Live Copy:

  * The live relationship is removed for that sub-page (or branch) and
  * The (sub-)pages in the Live Copy branch are treated as if they had been manually created.

  However, the sub-pages are still subject to the live relationship of the parent branch so a further rollout of the blueprint page(s) will both:

    1. Rename the detached page(s):

        * This is because MSM considers them as manually created pages that cause a conflict as they have the same name as the Live Copy pages it is trying to create.

    1. Create a new Live Copy page with the original name, containing the changes from the rollout.

  >[!NOTE]
  >
  >See [MSM Rollout Conflicts](rollout-conflicts.md) for details of such situations.

### Detach a Live Copy Page from the Page Properties {#detach-a-live-copy-page-from-the-page-properties}

To detach a Live Copy:

1. In the **Sites** console, select the Live Copy page and select **View Properties**.
1. Open the **Live Copy** tab.
1. On the toolbar, select **Detach**.

   ![Detach button](../assets/detach-button.png)

1. A confirmation dialo box is shown, select **Detach** to complete the action.

### Detach a Live Copy Page from the Live Copy Overview {#detach-a-live-copy-page-from-the-live-copy-overview}

The [Detach action is also available from the Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview), when a Live Copy page is selected.

1. Open the [Live Copy Overview](live-copy-overview.md#using-the-live-copy-overview) and select a Live Copy Page.
1. Select **Detach** from the toolbar.
1. Confirm the **Detach** action in the **Detach Live Copy** dialog:

   ![Detaching a Live Copy](../assets/detach-live-copy.png)
