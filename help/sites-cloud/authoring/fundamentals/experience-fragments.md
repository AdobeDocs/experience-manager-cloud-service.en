---
title: Experience Fragments
description: Use Adobe Experience Manager as a Cloud Service Experience Fragments to make your experiences reusable and flexible.
exl-id: 9dc33677-141f-47e5-a01e-6c7488686314
---
# Experience Fragments {#experience-fragments}

Within Adobe Experience Manager as a Cloud Service, an Experience Fragment:
* is a group of one or more components
* includes both content and layout
* can be referenced within pages
* can contain any component

An Experience Fragment:

* Is a part of an experience (page).
* Can be used across multiple pages.
* Is based on a template (editable only) to define structure and components.
* Is made up of one or more components, with layout, in a paragraph system.
* Can contain other experience fragments.
* Can be combined with other components (including other Experience Fragments) to form a complete page (experience).
* Can have different variations, which may share content and/or components.
* Can be broken down into building blocks that can be used across multiple variations of the fragment.

You can use Experience Fragments:

* If an author wants to re-use parts (a fragment of an experience) of a page. 
  Without Experience Fragments, the author would need to copy and paste that fragment. Creating and maintaining these copy/paste experiences is time-consuming and prone to user errors. 
  Experience Fragments eliminate the need for copy/paste.
* To support the headless CMS use-case. 
  Authors want to use AEM only for authoring but not for delivering to the customer. A third party system/touchpoint would consume that experience and then deliver to the end user.

>[!NOTE]
>
>Write access for experience fragments requires the user account to be registered in the group:
>
>* `experience-fragments-editors`
>
>Please contact your system administrator if you are experiencing any issues.

## When Should You Use Experience Fragments? {#when-should-you-use-experience-fragments}

Experience Fragments should be used:

* Whenever you want to reuse experiences.
  * Experiences that will be reused with same or similar content.
* When you use AEM as a content delivery platform for third parties.
  * Any solution that wants to use AEM as the content delivery platform.
  * Embedding content in third party touchpoints.
* If you have an Experience with different variations or renditions.
  * Channel or context-specific variations.
  * Experiences that make sense to group; for example a campaign with different experiences across channels.
* When you use Omnichannel Commerce.
  * Sharing commerce-related content on [social media](/help/implementing/developing/extending/experience-fragments.md#social-variations) channels at scale.
  * Making touchpoints transactional.

## Organizing your Experience Fragments {#organizing-your-experience-fragments}

It is recommended to:
* use folders to organize your Experience Fragments, 

* [configure the allowed templates on these folders](#configure-allowed-templates-folder).

Creating folders allows you to:

* create a meaningful structure for your Experience Fragments; for example, according to classification

  >[!NOTE]
  >
  >It is not necessary to align the structure of your Experience Fragments with the page structure of your site.

* [allocate the allowed templates at the folder level](#configure-allowed-templates-folder)

  >[!NOTE]
  >
  >You can use the [template editor](/help/sites-cloud/authoring/features/templates.md) to create your own template. 

The WKND project structures some Experience Fragments according to `Contributors`. The structure used also illustrates how other features, such as Multi Site Management (including language copies), can be used. 

See:

`http://localhost:4502/aem/experience-fragments.html/content/experience-fragments/wknd/language-masters/en/contributors/kumar-selveraj/master`

   ![Folders for Experience Fragments](/help/sites-cloud/authoring/assets/xf-folders.png)

## Creating and Configuring a Folder for your Experience Fragments {#creating-and-configuring-a-folder-for-your-experience-fragments}

To create and configure a folder for your Experience Fragments it is recommended to:

1. [Create a folder](/help/sites-cloud/authoring/fundamentals/organizing-pages.md#creating-a-new-folder).

1. [Configure the allowed Experience Fragment templates for that folder](#configure-allowed-templates-folder).

>[!NOTE]
>
>It is also possible to configure the [Allowed Templates for your instance](#configure-allowed-templates-instance), but this method is **not** recommended as the values can be overwritten upon upgrade.

### Configure the Allowed Templates for your Folder {#configure-allowed-templates-folder}

>[!NOTE]
>
>This is the recommended method for specifying the **Allowed Templates**, as the values will not be overwritten upon upgrade.

1. Navigate to the required **Experience Fragments** folder.

1. Select the folder, and then **Properties**.

1. Specify the regular expression for retrieving the required templates in the **Allowed Templates** field.
   
   For example:
   `/conf/(.*)/settings/wcm/templates/experience-fragment(.*)?`
   
   See:
   `http://localhost:4502/mnt/overlay/cq/experience-fragments/content/experience-fragments/folderproperties.html/content/experience-fragments/wknd`

   ![Experience Fragment Properties - Allowed Templates](/help/sites-cloud/authoring/assets/xf-folders-templates.png)

   >[!NOTE]
   >
   >See [Templates for Experience Fragments](/help/implementing/developing/extending/experience-fragments.md#templates-for-experience-fragments) for further details.

1. Select **Save and Close**.

### Configure the Allowed Templates for your Instance {#configure-allowed-templates-instance}

>[!CAUTION]
>
>It is not recommended to change the **Allowed Templates** by this method, as the templates specified can be overwritten upon upgrade.
>
>Please use this dialog for information purposes only.

1. Navigate to the required **Experience Fragments** console.

1. Select **Configuration options**:

   ![Configuration button](/help/sites-cloud/authoring/assets/xf-18.png)

1. Specify the required templates in the **Configure Experience Fragments** dialog:

   ![Configure Experience Fragments](/help/sites-cloud/authoring/assets/xf-19.png)

   >[!NOTE]
   >
   >See [Templates for Experience Fragments](/help/implementing/developing/extending/experience-fragments.md#templates-for-experience-fragments) for further details.

1. Select **Save**.


## Creating an Experience Fragment {#creating-an-experience-fragment}

To create an Experience Fragment:

1. Select **Experience Fragments** from the Global Navigation.

   ![Experience Fragments in the Navigation panel](/help/sites-cloud/authoring/assets/xf-01.png)

1. Navigate to the required folder and select **Create**:

   ![Creating a folder for Experience Fragments](/help/sites-cloud/authoring/assets/xf-02.png)

1. Select **Experience Fragment** to open the **Create Experience Fragment** wizard.

   Select the required **Template**, then **Next**:

   ![Selecting an Experience Fragment template](/help/sites-cloud/authoring/assets/xf-03.png)


1. Enter the **Properties** for your **Experience Fragment**.

   A **Title** is mandatory. If the **Name** is left blank it will be derived from the **Title**.

   ![Experience Fragment properties](/help/sites-cloud/authoring/assets/xf-04.png)

1. Click **Create**.

   A message will be displayed. Select:

    * **Done** to return to the console
    * **Open** to open the fragment editor

## Editing your Experience Fragment {#editing-your-experience-fragment}

The Experience Fragment Editor offers you similar capabilities to the normal page editor.

>[!NOTE]
>
>See [Editing Page Content](/help/sites-cloud/authoring/fundamentals/editing-content.md) for more information on how to use the page editor.

The following example procedure illustrates how to create a teaser for a product:

1. Drag and drop the required component from the [Components Browser](/help/sites-cloud/authoring/fundamentals/environment-tools.md#components-browser).

1. Depending on the component:
   * Add any content and/or assets as required. 
   * Configure the properties as required.

1. Add more components as required.

For example: `http://<host>:<port>/editor.html/content/experience-fragments/wknd/language-masters/en/contributors/stacey-roswells/master.html`

   ![Experience Fragment on page](/help/sites-cloud/authoring/assets/xf-05.png)

## Creating An Experience Fragment Variation {#creating-an-experience-fragment-variation}

You can create variations of your Experience Fragment, depending on your needs:

1. Open your fragment for [editing](#editing-your-experience-fragment).
1. Open the **Variations** tab.

   ![Creating an Experience Fragment variation](/help/sites-cloud/authoring/assets/xf-06.png)

1. **Create** allows you to create:

    * **Variation**
    * **Variation as live-copy**.

1. Define the required properties:

    * **Template**
    * **Title**
    * **Name** - if left blank it will be derived from the Title
    * **Description**
    * **Variation tags**

    For example:

   ![Variation properties](/help/sites-cloud/authoring/assets/xf-07.png)

1. Confirm with **Done**, the new variation will be shown in the panel.

## Using your Experience Fragment {#using-your-experience-fragment}

You can now use your Experience Fragment when authoring your pages:

1. Open any page for editing.

1. Create an instance of the Experience Fragment component, within the page paragraph system:

1. Add the actual Experience Fragment to the component instance; either:

    * Drag the required fragment from the Assets Browser and drop onto the component.
    * Select **Configure** from the component toolbar and specify the fragment to use, confirm with **Done**. 

   >[!NOTE]
   >
   >Edit, in the component toolbar, operates as a shortcut to open the fragment in the fragment editor.

For example: `http://<host>:<port>/editor.html/content/wknd/language-masters/en/about-us.html`

![Experience Fragment in Page Editor](/help/sites-cloud/authoring/assets/xf-08.png)

## Building Blocks {#building-blocks}

You can select one or more components to create a building block for recycling within your fragment:

### Creating a Building Block {#creating-a-building-block}

To create a new Building Block:

1. In the Experience Fragment editor, select the components you want to re-use:

   ![Select component for Building Block](/help/sites-cloud/authoring/assets/xf-09.png)

1. From the components toolbar, select **Convert to building block**:

   ![Building Block button](/help/sites-cloud/authoring/assets/xf-10.png)

1. Enter the name of the **Building Block**, and confirm with **Convert**:

   ![Name Building Block](/help/sites-cloud/authoring/assets/xf-11.png)

1. The **Building Block** will be shown in the left tab (**Local**), and can be selected for further action:

   ![Building Block in the rail](/help/sites-cloud/authoring/assets/xf-12.png)

#### Managing a Building Block {#managing-a-building-block}

Your building block is visible in the **Building Blocks** tab. For each block, the following actions are available:

* **Go to master**: open the master variation in a new tab
* **Rename**
* **Delete**

![Managing Building Blocks](/help/sites-cloud/authoring/assets/xf-13.png)

#### Using a Building Block {#using-a-building-block}

You can drag your building block to the paragraph system of any fragment, as with any component.

When editing an Experience Fragment available Building Blocks are displayed in the left-hanf tab. You can filter according to:

* **Local** - Building Blocks from the current Experience Fragment
* **All** - Building Blocks from all fragments

![Selecting Building Blocks](/help/sites-cloud/authoring/assets/xf-14.png)

## Details of your Experience Fragment {#details-of-your-experience-fragment}

Details of your fragment can be seen:

1. Navigate to the location of your Experience Fragments (do not navigate further down to the variations within the fragment). 
   Details are shown in all views of the **Experience Fragments** console, with the **List View** including details of an export to Target: <!--Details are shown in all views of the **Experience Fragments** console, with the **List View** including details of an [export to Target](/help/sites-administering/experience-fragments-target.md):-->

   ![Experience Fragment details](/help/sites-cloud/authoring/assets/xf-15.png)

1. When you open the **Properties** of the Experience Fragment:

   ![Properties button](/help/sites-cloud/authoring/assets/xf-16.png)

   The properties are available in various tabs:

   >[!CAUTION]
   >
   >These tabs are shown when you open **Properties** from the Experience Fragments console.
   >
   >If you **Open Properties** when editing an Experience Fragment, the appropriate [Page Properties](/help/sites-cloud/authoring/fundamentals/page-properties.md) are shown.

   ![Experience Fragment properties](/help/sites-cloud/authoring/assets/xf-17.png)

    * **Basic**
        * **Title** - mandatory
        * **Description**
        * **Tags**
        * **Total number of variants** - information only
        * **Number of web variants** - information only
        * **Number of non-web variants** - information only
        * **Number of pages using this fragment** - information only
    * **Cloud Services**
        * **Cloud Configuration**
        * **Cloud Service Configurations**
        * **Facebook page ID**
        * **Pinterest board**
    * **References**
        * A list of references
    * **Social Media Status**
        * Details of social media variations

## The Plain HTML Rendition {#the-plain-html-rendition}

Using the `.plain.` selector in the URL, you can access the plain HTML rendition from the browser.

>[!NOTE]
>
>Although this is directly available from the browser, [the primary purpose is to allow other applications (for example, third party web apps, custom mobile implementations) to access the content of the Experience Fragment directly, using only the URL](/help/implementing/developing/extending/experience-fragments.md#the-plain-html-rendition).

## Exporting Experience Fragments {#exporting-experience-fragments}

By default, Experience Fragments are delivered in the HTML format. This can be used by both AEM and third party channels alike.

For export to Adobe Target, JSON can also be used. See Target Integration with Experience Fragments for full information. <!--For export to Adobe Target, JSON can also be used. See [Target Integration with Experience Fragments](/help/sites-administering/experience-fragments-target.md) for full information.-->
