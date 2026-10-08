---
title: Auto-tag assets with [!DNL Adobe AI] smart service
description: Tag assets with an artificially intelligent service that applies contextual and descriptive business tags.
feature: Smart Tags,Tagging
role: Admin,User
badgeSaas: label="AEM Assets" type="Positive" tooltip="Applies to AEM Assets)."
exl-id: 05304c5e-f620-4cca-8cfe-76a6fa2e3f4a
---
# Smart Tags Training

**Smart tags training** teaches the tagging engine your organization's specific tag structure and business taxonomy, so it can define custom tags when the default set does not cover the specifics of a business's assets. Smart tags training uses [**[!DNL Adobe AI]**](https://business.adobe.com/ai/adobe-genai.html), Adobe's artificial intelligence (AI) framework, to train its image recognition algorithm on your tag structure and business taxonomy. This trained content intelligence then automatically applies relevant, business-specific tags to new and previously untagged assets. **[!DNL Experience Manager Assets]** automatically applies smart tags to uploaded assets by default.

## How Smart Tags Training Works

Smart tags training aligns automated image recognition with the way a specific business classifies and searches for its content. The process works as follows:

1. **Provide a tag structure and taxonomy** — Supply the tags and business taxonomy that reflect how your organization categorizes assets.
2. **Train the recognition algorithm** — **[!DNL Adobe AI]** analyzes the labeled assets and learns the visual patterns associated with each tag.
3. **Build content intelligence** — The trained model develops an understanding of your specific tag structure rather than relying only on generic, out-of-the-box tags.
4. **Apply tags automatically** — **[!DNL Experience Manager Assets]** uses this content intelligence to apply relevant tags to new and previously untagged assets on upload.

Because the algorithm is trained on your own taxonomy, the resulting tags are more relevant to your business than default tags alone. This is especially valuable when the standard tag set does not recognize domain-specific products, categories, or attributes.

## Key Benefits of Smart Tags Training

- **Business-specific tagging** — Recognizes and applies tags aligned with your organization's taxonomy, not just generic labels.
- **Automatic application** — By default, **[!DNL Experience Manager Assets]** tags uploaded assets without manual effort.
- **Improved searchability** — More accurate, relevant tags make assets easier to find and organize within the digital asset management system.
- **Scalable consistency** — Once trained, the algorithm applies consistent tags across large volumes of new and previously untagged assets.

By combining **[!DNL Adobe AI]** image recognition with your own tag structure and business taxonomy, smart tags training extends automated tagging beyond default capabilities, ensuring assets are labeled in a way that matches how your organization actually classifies and retrieves its content.

## Determining the requirement of smart tags training {#smart-tag-training-requirement}

**Smart tags training** teaches the automated tagging model to recognize and apply relevant labels to your assets. Training is required in the following scenarios:

* **Add an automated labeler** to eliminate repetitive labeling, because trained smart tags apply labels automatically each time you upload the same asset—saving manual iterations.
* **Improve tag relevance** so assets are matched with the most contextually appropriate labels.
* **Increase tagging accuracy** for the labels that appear on an asset, reducing incorrect or irrelevant tags.
* **Add unavailable or missing labels** that the default model does not yet recognize.


>[!NOTE]
>
>Training smart tags is applicable in an ***image-type*** of asset only. As a result, smart tags training does not apply to non-image asset types.

## Steps involved in training smart tags

**Smart Tags** are metadata labels that [!DNL Experience Manager] as a [!DNL Cloud Service] applies automatically to digital assets using machine-learning models, making assets easier to search, filter, and organize. **[!DNL Experience Manager] as a [!DNL Cloud Service] auto-generates Smart Tags for text-based assets and videos by default.** Because these models are pre-trained for text and video content, no additional configuration is required to tag those asset types.

Images, however, benefit from a custom-trained model. Training the model teaches [!DNL Experience Manager] to recognize the specific objects, styles, or brand-relevant concepts present in your image library. As a result, tagging becomes more accurate and consistent, which directly improves asset discoverability and search relevance for teams that manage large image collections.

### Workflow for training Smart Tags on images

To train Smart Tags for images, complete the following tasks in sequence:

1. **[Understand tag models and guidelines](#understand-tag-models-guidelines)** — Review how tag models work and the guidelines for preparing training data, so the model learns from well-structured, representative examples.
2. **[Train the model](#train-model)** — Supply sample images and train the model to recognize the tags relevant to your assets.
3. **[Tag your digital assets](#tag-assets)** — Apply the trained model to generate Smart Tags across your image assets.
4. **[Manage the tags and searches](#manage-smart-tags-and-searches)** — Review, refine, and manage the resulting tags to keep searches accurate and up to date.

Following these steps in order ensures the model is properly configured before tagging, producing reliable Smart Tags that enhance search and asset management within [!DNL Experience Manager] as a [!DNL Cloud Service].

## Understand tag models and guidelines {#understand-tag-models-guidelines}

A **tag model** is a group of related tags associated with the distinct visual aspects—such as design, usage, color, or style—of the images being tagged. Each tag within a model maps to a clearly different visual characteristic, so that when the tags are applied to an image, they enable the search service to retrieve specific types of images with precision. Because the tags in a single model share a common theme, grouping them together improves the accuracy and relevance of image search results.

For example, a shoes collection can contain many different tags, yet all of those tags relate to shoes and can belong to the same tag model. When these tags are applied to the shoe images, they help users find different types of shoes—for instance, **by design** (such as sneakers, formal, or sandals) or **by usage** (such as running, hiking, or casual wear). This organization ensures that each search query resolves to the most relevant subset of images, because every tag encodes a meaningful visual distinction.

Before you create a tag model and train the service, follow these steps to ensure reliable results:

1. **Identify a set of unique tags** that best describe the objects in the images in the context of your business. Each tag should represent a distinct, non-overlapping visual aspect so that the model can differentiate between image types.
2. **Ensure that the assets in your curated set conform to** [the training guidelines](#training-guidelines). Adherence to these guidelines is essential, because well-curated, guideline-compliant assets directly determine how accurately the trained service applies tags during search.

### Training guidelines {#training-guidelines}

Ensure that the images in the training set conform to the following guidelines. A well-prepared training set is relevant, consistent, and clearly scoped, which directly improves the accuracy of the resulting tag model:

* **Relevance**: Include only images that clearly represent the tags you intend to train. Each image should be a recognizable, representative example of its tag.
* **Consistency**: Use images of comparable quality, clarity, and framing so the model learns reliable visual patterns rather than noise.
* **Clear scope**: Group tags into a single tag model only when they belong to the same logical category. Avoid mixing unrelated categories in one model.
* **Sufficient quantity**: Provide enough distinct examples per tag so the model can generalize, and avoid duplicating the same subjects across multiple models.

<table>
   <tr>
      <th> Metrics </th>
      <th> Description </th>
   </tr>
   <tr>
      <td> <b>Quantity and size </b></td>
      <td> Minimum 10 and maximum 50 images per tag. </td>
   </tr>
   <tr>
      <td> <b>Coherence</b> </td>
      <td> Ensure that the images for a tag are visually similar. It is best to add the tags about the same visual aspects (such as the same type of objects in an image) together into a single tag model. For example, it is not a good idea to tag all of these images as <i>my-party</i> (for training) because they are not visually similar. </td>
   </tr>
   <tr>
      <td colspan="2"> <img src="assets/do-not-localize/coherence.png"><br><i>Figure: Illustrative images of Coherence to exemplify the guidelines for training</i>
      </td>
   </tr>
   <tr>
      <td> <b>Coverage</b></td>
      <td> There should be sufficient variety in the images in the training. The idea is to supply a few but reasonably diverse examples so that learns to focus on the right things. If you're applying the same tag on visually dissimilar images, include at least five examples of each kind. For example, for the tag <i>model-down-pose</i>, include more training images similar to the highlighted image below for the service to identify similar images more accurately during tagging.</td>
   </tr>
   <tr>
   <td colspan="2"> <img src="assets/do-not-localize/coverage_1.png"><br><i>Figure: Illustrative images of Coverage to exemplify the guidelines for training</i>
   </td>
   </tr>
   <tr>
      <td><b>Distraction/obstruction</b> </td>
      <td> The service trains better on images that have less distraction (prominent backgrounds, unrelated accompaniments, such as objects/persons with the main subject). For example, for the tag <i>casual-shoe</i>, the second image is not a good training candidate. </td>
   </tr>
   <tr>
      <td colspan="2"> <img src="assets/do-not-localize/distraction.png"><br><i>Figure: Illustrative images of Distraction/obstruction to exemplify the guidelines for training</i>
      </td>
   </tr>
   <tr>
      <td> <b>Completeness</b> </td>
      <td> If an image qualifies for more than one tag, add all applicable tags before including the image for training. For example, for tags, such as <i>raincoat</i> and <i>model-side-view</i>, add both the tags on the eligible asset before including it for training. </td>
   </tr>
   <tr>
      <td colspan="2"> <img src="assets/do-not-localize/completeness.png"><br><i>Figure: Illustrative images of Completeness to exemplify the guidelines for training</i>
      </td>
   </tr>
   <tr>
      <td> <b>Number of tags</b> </td>
      <td> Adobe recommends that you train a model using at least two distinct tags and at least ten different images for each tag. In a single tag model, do not add more than 50 tags. </td>
   </tr>
   <tr>
      <td> <b>Number of examples</b> </td>
      <td> For each tag, add at least ten examples. However, Adobe recommends about 30 examples. A maximum of 50 examples per tag are supported. </td>
   </tr>
   <tr>
      <td> <b>Prevent false positives and conflicts</b> </td>
      <td> Adobe recommends creating a single tag model for a single visual aspect. Structure the tag models in a way that avoids overlapping tags between the models. For example, do not use a common tags like <i>sneakers</i> in two different tag models names <i>shoes</i> and <i>footwear</i>. The training process overwrites one trained tag model with the other for a common keyword. </td>
   </tr>
</table>

**Examples**: Some more examples for guidance are:

* Recommended tag model scope — Create a tag model that only includes:

  * The tags related to car models.
  * The tags related to jackets for adults and kids.

* What to avoid — Do not create:

  * A tag model that includes car models released in 2019 and 2020.
  * Multiple tag models that include the same few car models.

>[!NOTE]
>
>You can use the same images to train different tag models. However, **do not associate an image with more than one tag in a tag model**, because assigning conflicting tags within the same model introduces ambiguous training signals and reduces prediction accuracy. It is possible to tag the same image with different tags belonging to different tag models, which lets you reuse a shared image library across multiple, distinctly scoped models.
>**You cannot undo the training.** Because training is irreversible, carefully review and finalize your image selection beforehand. Following these guidelines improves tag-model accuracy, since it ensures the training set is relevant, consistent, and unambiguous before you commit to training.

## Train the model for your custom tags {#train-model}

Training a custom model for your business-specific tags teaches Smart Tags to recognize categories that matter to your organization, improving the accuracy and relevance of automated tagging. To create and train a model for your business-specific tags, follow these steps:

1. Create the necessary tags and the appropriate tag structure. Upload the relevant images to the Digital Asset Management (DAM) repository.
1. In [!DNL Experience Manager Cloud Service] user interface, access **[!UICONTROL Assets]** > **[!UICONTROL Smart Tag Training]**.
1. Click **[!UICONTROL Create]**. Provide a **[!UICONTROL Title]**, **[!UICONTROL Description]**.
1. Click on the folder icon in **[!UICONTROL Tags]** field. A popup window opens.
1. Search or select the appropriate tags from the existing tags in `cq-tags` that you want to add to the model. Click **[!UICONTROL Next]**.

   >[!NOTE]
   >
   >You can sort the tags structure in ascending or descending order based on the **[!UICONTROL Name]** (alphabetical order), **[!UICONTROL Created]** date, or **[!UICONTROL Modified]** date.


1. In the **[!UICONTROL Select Assets]** dialog, click **[!UICONTROL Add Assets]** against each tag. Search or browse the Digital Asset Management (DAM) repository to select **at least 10 and at most 50 images** for each tag. This range provides enough visual variety to train an accurate model while preventing overfitting or excessive training loads. Select assets and not the folder. Once you have selected the images, click **[!UICONTROL Select]**.

   ![View training status](assets/smart-tags-training-status.png)

1. To preview the thumbnails of the selected images, click the accordion in front of a tag. Modify the selection by clicking **[!UICONTROL Add Assets]**. Once satisfied with the selection, click **[!UICONTROL Submit]**. The user interface displays a notification at the bottom of the page confirming that training has started.
1. Check the status of the training in the **[!UICONTROL Status]** column for each tag model. Possible statuses are:
   - **[!UICONTROL Pending]** — the training request has been submitted and is queued or in progress.
   - **[!UICONTROL Trained]** — the model has been successfully trained and is ready to apply your custom tags.
   - **[!UICONTROL Failed]** — the training did not complete successfully and must be retried, typically after reviewing the tag selection and associated assets.

![Workflow to train tagging model for Smart Tags](assets/smart-tag-model-training-flow.png)

*Figure: Steps of the training workflow to train tagging model.*

### View training status and report {#training-status}

To check whether the Smart Tags service is trained on your tags in the training set of assets, review the training workflow report from the Reports console.

1. In [!DNL Experience Manager Cloud Service] interface, go to **[!UICONTROL Tools]** > **[!UICONTROL Assets]** > **[!UICONTROL Reports]**.
1. In the **[!UICONTROL Asset Reports]** page, click **[!UICONTROL Create]**.
1. Select the **[!UICONTROL Smart Tags Training]** report, and then click **[!UICONTROL Next]** from the toolbar.
1. Specify a title and description for the report. Under **[!UICONTROL Schedule Report]**, leave the **[!UICONTROL Now]** option selected. If you want to schedule the report for later, select **[!UICONTROL Later]** and specify a date and time. Then, click **[!UICONTROL Create]** from the toolbar.
1. In the **[!UICONTROL Asset Reports]** page, select the report you generated. To view the report, click **[!UICONTROL View]** from the toolbar.
1. Review the details of the report. The report displays the training status for the tags you trained. **Green** color in the **[!UICONTROL Training Status]** column indicates that the Smart Tags service is **fully trained** for the tag, meaning it has learned enough labeled examples to apply the tag reliably. **Yellow** color indicates that the service is **partially trained** for a particular tag, so tagging accuracy for that tag may be lower until training is completed. To train the service completely for a tag, add more images with the particular tag and execute the training workflow, because the service requires sufficient labeled examples to recognize the tag accurately. If you do not see your tags in this report, execute the training workflow again for these tags.
1. To download the report, select it from the list, and click **[!UICONTROL Download]** from the toolbar. The report downloads as a spreadsheet.

>[!NOTE]
>
>Transferring Smart Tags training between instances via an export depends on the Adobe Identity Management System (IMS) organization structure.
>You do not need to export Smart Tags training if the environment belongs to the same IMS org, because the training is automatically shared across environments within that org. If the environment is across IMS orgs, then there is no way to share or export Smart Tags training.

## Limitations and best practices related to smart tags {#limitations-smart-tags-training}

* To train the model, use the most appropriate, representative images, because the model learns tag associations directly from these examples. **The training cannot be reverted, and a trained model cannot be removed.** Because tagging accuracy depends directly on the current training, select training images carefully; incorrect or unrepresentative images permanently reduce tagging accuracy.
* You cannot train the service that applies Smart Tags to videos using any specific videos. Video Smart Tagging operates solely on **default [!DNL Adobe AI] settings** and cannot be customized with your own videos.


>[!NOTE]
>
>The ability of the Smart Tags service to train on your tags and apply them on other images depends on the quality of images you use for training. Higher-quality, consistent images produce more reliable tag associations, because the model generalizes from the visual patterns it observes during training.
>For best results, Adobe recommends that you use visually similar images to train the service for each tag. Visually similar training images help the service recognize shared visual characteristics, which improves the consistency and accuracy of the tags applied to new assets.


**See also**

* [Translate Assets](/help/assets/translate-assets.md)
* [Assets HTTP API](/help/assets/mac-api-assets.md)
* [Assets supported file formats](/help/assets/file-format-support.md)
* [Search assets](/help/assets/search-assets.md)
* [Connected assets](/help/assets/use-assets-across-connected-assets-instances.md)
* [Asset reports](/help/assets/asset-reports.md)
* [Metadata schemas](/help/assets/metadata-schemas.md)
* [Download assets](/help/assets/download-assets-from-aem.md)
* [Manage metadata](/help/assets/manage-metadata.md)
* [Manage Dynamic Media templates](/help/assets/dynamic-media/manage-dynamic-media-templates.md)
* [Manage reports in Assets view](/help/assets/manage-reports-assets-view.md)
* [Search facets](/help/assets/search-facets.md)
* [Manage collections](/help/assets/manage-collections.md)
* [Bulk metadata import](/help/assets/metadata-import-export.md)
* [Publish Assets to AEM and Dynamic Media](/help/assets/publish-assets-to-aem-and-dm.md)
