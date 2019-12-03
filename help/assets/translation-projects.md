---
title: Creating Translation Projects
description: Learn how to create translation projects in AEM.
contentOwner: AG

---

# Create translation projects {#creating-translation-projects}

To create a language copy, trigger one of the following language copy workflows available under the References rail in the Assets UI:

**Create and translate**

In this workflow, assets to be translated are copied to the language root of the language to which you want to translate. In addition, depending upon the options you choose, a translation project is created for the assets in the Projects console. Depending on the settings, the translation project can be started manually or allowed to run automatically as soon as the translation project is created.

**Update language copies**

You run this workflow to translate an additional group of assets and include it in a language copy for a particular locale. In this case, the translated assets are added to the target folder that already contains previously-translated assets.

>[!NOTE]
>
>Asset binaries are translated only if the translation service provider supports the translation of binaries.

>[!NOTE]
>
>If you launch a translation workflow for complex assets, such as PDFs and InDesign files, their subassets or renditions (if any) are not submitted for translation.

## Create and translate workflow {#create-and-translate-workflow}

You use the Create and translate workflow to generate language copies for a particular language for the first time. The workflow provides the following options:

* Create structure only
* Create a new translation project
* Add to existing translation project

### Create structure only {#create-structure-only}

Use the **Create structure only** option to create a target folder hierarchy within the target language root to match the hierarchy of the source folder within the source language root. In this case, source assets are copied to the destination folder. However, no translation project is generated.

1. In the Assets UI, select the source folder for which you want to create a structure in the target language root.
1. Open the **[!UICONTROL References]** pane and click/tap **[!UICONTROL Language Copies]** under **[!UICONTROL Copies]**.
1. Click/tap **[!UICONTROL Create & Translate]** at the bottom.
1. From the **[!UICONTROL Target Languages]** list, select the language for which you want to create a folder structure.
1. From the **[!UICONTROL Project]** list, choose **[!UICONTROL Create structure only]**.
1. Click/tap **[!UICONTROL Create]**. The new structure for the target language is listed under **[!UICONTROL Language Copies]**.
1. Click/tap the structure from the list, and then click/tap **[!UICONTROL Reveal in Assets]** to navigate to the folder structure within the target language.

## Prepare assets for translation {#prepare-assets-for-translation}

Multilingual assets means assets with binaries, metadata, and tags in multiple languages. Generally, binaries, metadata, and tags for assets exist in one language, which are then translated to other languages for use in multilingual projects.

In Adobe Experience Manager (AEM) Assets, multilingual assets are included in folders, where each folder contains the assets in a different language.

Each language folder is called a language copy. The root folder of a language copy, known as the language root, identifies the language of the content in the language copy. For example, `/content/dam/it` is the Italian language root for the Italian language copy. Language copies must use a [correctly-configured language root](#create-a-language-root) so that the correct language is targeted when translations of source assets are performed.

The language copy for which you originally add assets is the language master. The language master is the source that is translated into other languages. A sample folder hierarchy includes several language roots:

/content
&nbsp; &nbsp; /- dam
&nbsp; &nbsp; &nbsp; |- en
&nbsp; &nbsp; &nbsp; |- fr
&nbsp; &nbsp; &nbsp; |- de
&nbsp; &nbsp; &nbsp; |- es
&nbsp; &nbsp; &nbsp; |- it
&nbsp; &nbsp; &nbsp; |- ja
&nbsp; &nbsp; &nbsp; |- zh

Perform the following steps to prepare your assets for translation:

1. Create the language root of your language master. For example, the language root of the English language copy in the sample folder hierarchy is */content/dam/en*. Ensure that the language root is correctly configured according to the information in [Create a language root](#create-a-language-root).

1. Add assets to your language master.
1. Create the language root of each target language for which you require a language copy.

### Create a Language Root {#create-a-language-root}

To create the language root, you create a folder and use an ISO language code as the value for the Name property. After you create the language root, you can create a language copy at any level within the language root.

For example, the root page of the Italian language copy of the sample hierarchy has `it` as the Name property. The Name property is used as the name of the asset node in the repository, and therefore determines the path of the assets. (*&lt;server&gt;:&lt;port&gt;/assets.html/content/dam/it/*)

1. From the Assets console, click/tap **[!UICONTROL Create]** and choose **[!UICONTROL Folder]** from the menu.
1. In the Name field type the country code in the format of `<language-code>`.
1. Click or tap **[!UICONTROL Create]**. The language root is created in the Assets console.

### View language roots {#view-language-roots}

The touch-optimized UI provides a References panel that shows a list of language roots that have been created within AEM Assets.

1. In the Assets console, select the language master for which you want to create language copies.
1. Click or tap the GlobalNav icon, and choose **[!UICONTROL References]** to open the Reference pane.
1. In the References pane, click or tap **[!UICONTROL Language Copies]**. The Language Copies panel shows the language copies of the assets.

### Create a new translation project {#create-a-new-translation-project}

If you use this option, assets to be translated are copied to the language root of the language to which you want to translate. Depending upon the options you choose, a translation project is created for the assets in the Projects console. Depending on the settings, the translation project can be started manually or runs automatically as soon as the translation project is created.

1. In the Assets UI, select the source folder for which you want to create a Language copy.
1. Open the **[!UICONTROL References]** pane and click/tap **[!UICONTROL Language Copies]** under **[!UICONTROL Copies]**.
1. Click/tap **[!UICONTROL Create & Translate]** at the bottom.
1. From the **[!UICONTROL Target Languages]** list, select the language(s) for which you want to create a folder structure.
1. From the **[!UICONTROL Project]** list, select **[!UICONTROL Create a new translation project]**.
1. In the **[!UICONTROL Project Title]** field, enter a title for the project.
1. Click/tap on **[!UICONTROL Create]**. Assets from the source folder are copied to the target folders for the locales you selected in step 4.
1. To navigate to the folder, select the language copy, and click **[!UICONTROL Reveal in Assets]**.
1. Navigate to the Projects console. The translation folder is copied to the Projects console.
1. Open the folder to view the translation project.
1. Click/tap the project to open the details page.
1. To view the status of the translation job, click the ellipsis at the bottom of the **[!UICONTROL Translation Job]** tile. <!-- For more details around job statuses, see [Monitoring the Status of a Translation Job](/help/sites-administering/tc-manage.md#monitoring-the-status-of-a-translation-job). -->
1. In the Assets user interface, open the Properties page for each of the translated assets to view the translated metadata.

>[!NOTE]
>
>This feature is available both for assets and folders. When an asset is selected instead of a folder, the entire hierarchy of folders up to the language root is copied to create a language copy for the asset.

### Add to existing translation project {#add-to-existing-translation-project}

If you use this option, the translation workflow runs for assets that you add to the source folder after running a previous translation workflow. Only the newly-added assets are copied to the target folder that contains previously-translated assets. No new translation project is created in this case.

1. In the Assets UI, navigate to the source folder that contains untranslated assets.
1. Select an asset you want to translate, and open the **[!UICONTROL Reference pane]**. The **[!UICONTROL Language Copies]** section displays the number of translation copies that are currently available.
1. Click/tap **[!UICONTROL Language Copies]** under **[!UICONTROL Copies]**. A list of available translation copies is displayed.
1. Click/tap **[!UICONTROL Create & Translate]** at the bottom.
1. From the **[!UICONTROL Target Languages]** list, select the language(s) for which you want to create a folder structure.
1. From the **[!UICONTROL Project]** list, select **[!UICONTROL Add to existing translation project]** to run the translation workflow on the folder.
   >[!NOTE]
   >
   >If you choose the **[!UICONTROL Add to existing translation project]** option, your translation project is added to a pre-existing project only if your project settings exactly match the settings of the pre-existing project. Otherwise, a new project is created.
1. From the **[!UICONTROL Existing translation project]** list, select a project to add the asset for translation.
1. Click/tap **[!UICONTROL Create]**. The assets to be translated are added to the target folder. The updated folder is listed under the **[!UICONTROL Language Copies]** section.
1. Navigate to the Projects console, and open the existing translation project you added to.
1. Click/tap the translation project view the project details page.
1. Click/tap the ellipsis at the bottom of the **Translation Job** tile to view the assets in the translation workflow. The translation job list also displays entries for asset metadata and tags. These entries indicate that the metadata and tags for the assets are also translated.

   >[!NOTE]
   >
   >If you delete the entry for tags or metadata, no tags or metadata are translated for any of the assets.

   >[!NOTE]
   >
   >If you use Machine Translation, asset binaries aren't translated.

   >[!NOTE]
   >
   >If the asset you add to the translation job includes subassets, select the subassets and remove them for the translation to proceed without any glitches.

1. To start the translation for the assets, click/tap the arrow on the **[!UICONTROL Translation Job]** tile and select **[!UICONTROL Start]** from the list. A message notifies the commencement of the translation job.
1. To view the status of the translation job, click/tap the ellipsis at the bottom of the **[!UICONTROL Translation Job]** tile. <!-- For more details, see [Monitoring the Status of a Translation Job](/help/sites-administering/tc-manage.md#monitoring-the-status-of-a-translation-job). -->
1. After the translation completes, the status changes to Ready to Review. Navigate to the Assets UI, and open the Properties page for each of the translated assets to view the translated metadata.

## Update language copies {#update-language-copies}

Run this workflow to translate any additional set of assets and include it in a lanugage copy for a particular locale. In this case, the translated assets are added to the target folder that already contains previously-translated assets. Depending upon the choice of options, a translation project is created or an existing translation project is updated for the new assets. The Update language copies workflow includes the following options:

* Create a new translation project
* Add to existing translation project

### Create a new translation project {#create-a-new-translation-project-1}

If you use this option, a translation project is created for the set of assets for which you want to update a language copy.

1. From the Assets UI, select the source folder where you added an asset.
1. Open the **[!UICONTROL References]** pane, and click/tap **[!UICONTROL Language Copies]** under **[!UICONTROL Copies]** to display the list of language copies.
1. Select the check box before **[!UICONTROL Language Copies]**, and then select the target folder corresponding to the appropriate locale.
1. Click/tap **[!UICONTROL Update language copies]** at the bottom.
1. From the **[!UICONTROL Project]** list, choose **[!UICONTROL Create a new translation project]**.
1. In the **[!UICONTROL Project Title]** field, enter a title for the project.
1. Click/tap **[!UICONTROL Start]**.
1. Navigate to the Projects console. The translation folder is copied to the Projects console.
1. Open the folder to view the translation project.
1. Click/tap the project to open the details page.
1. To start the translation for the assets, click the arrow on the **[!UICONTROL Translation Job]** tile and select **[!UICONTROL Start]** from the list. A message notifies the commencement of the translation job.
1. To view the status of the translation job, click/tap the ellipsis at the bottom of the **[!UICONTROL Translation Job]** tile. <!-- For more details around job statuses, see [Monitoring the Status of a Translation Job](../sites-administering/tc-manage.md#monitoring-the-status-of-a-translation-job). -->
1. Navigate to the Assets UI, and open the Properties page for each of the translated assets to view the translated metadata.

### Add to existing translation project {#add-to-existing-translation-project-1}

If you use this option, the set of assets are added to an existing translation project to update the language copy for the locale you choose.

1. From the Assets UI, select the source folder where you added an asset folder.
1. Open the **[!UICONTROL References pane]**, and click/tap **[!UICONTROL Language Copies]** under **[!UICONTROL Copies]** to display the list of language copies.
1. Select the check box before **[!UICONTROL Language Copies]**, which selects all language copies. Unselect other copies except the language copy (copies) corresponding to the locale(s) to which you want to translate.
1. Click/tap **[!UICONTROL Update language copies]** at the bottom.
1. From the **[!UICONTROL Project]** list, choose **[!UICONTROL Add to existing translation project]**.
1. From the **[!UICONTROL Existing translation project]** list, select a project to add the asset for translation.
1. Click/tap **[!UICONTROL Start]**.
1. See steps 9-14 of [Add to existing translation project](translation-projects.md#add-to-existing-translation-project) to complete the rest of the procedure.

## Creating temporary language copies {#creating-temporary-language-copies}

When you run a translation workflow to update a language copy with edited versions of original assets, the existing language copy is preserved until you approve the translated asset(s). AEM Assets stores the newly-translated asset(s) at a temporary location and updates the existing language copy after you explicitly approve the asset(s). If you reject the asset(s), the language copy remains unchanged.

1. Click/tap the source root folder under **[!UICONTROL Language Copies]** for which you already created a languag copy, and then click/tap **[!UICONTROL Reveal in Assets]** to open the folder in AEM Assets.
1. From the Assets UI, select an asset you already translated and click/tap the **[!UICONTROL Edit]** icon from the toolbar to open the asset in edit mode.
1. Edit the asset and then save the changes.
1. Perform steps 2-14 of the [Add to existing translation project](#add-to-existing-translation-project) procedure to update the language copy.
1. Click/tap the ellipsis at the bottom of the **[!UICONTROL Translation Job]** tile. From the list of assets in the **[!UICONTROL Translation Job]** page, you can clearly view the temporary location where the translated version of the asset is stored.
1. Select the checkbox next to **[!UICONTROL Title]**.
1. From the toolbar, click/tap **[!UICONTROL Accept Translation]** and then click/tap **[!UICONTROL Accept]** in the dialog to overwrite the translated asset in the target folder with the translated version of the edited asset.

   >[!NOTE]
   >
   >To enable the translation workflow to update the destination asset(s), accept both the asset and metadata.

   Click/tap **[!UICONTROL Reject Translation]** to retain the originally translated version of the asset in the target locale root and reject the edited version.

1. Navigate to the Assets console, and open the Properties page for each of the translated assets to view the translated metadata.

For tips on translating metadata for assets efficiently, see [5 Steps for Efficiently Translating Metadata](https://blogs.adobe.com/experiencedelivers/experience-management/translate_aemassets_metadata/).

