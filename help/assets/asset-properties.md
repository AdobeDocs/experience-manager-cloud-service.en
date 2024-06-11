---
title: View asset properties in [!DNL the content module of Adobe GenStudio]
description: View asset properties in [!DNL the content module of Adobe GenStudio]
role: User
---

# Manage asset properties in the content module of Adobe GenStudio {#asset-properties}

![Metadata banner image](assets/metadata-banner-image.png)

[!DNL The content module of Adobe GenStudio] allows you to view information about the asset which is critical for efficient asset management. It is the collection of all the data available for an asset.

Viewing asset properties help you further categorize assets and is helpful as the amount of digital information grows. It is possible to manage a few hundred files based on just the filenames, thumbnails, and memory. However, this approach is not scalable when the number of people involved, and the number of managed assets increase. In addition, the value of a digital asset grows, as the asset becomes:

* More accessible - systems and users can find it easily.
* Easier to manage - you can find assets with the same set of properties easily and apply changes to them.
* Complete - asset carries more information and context.

## Evaluate information for the searched assets  {#evaluate-info}

Assets provide you with the right means of creating, managing, and exchanging information for your digital assets.

### View properties of an asset {#properties-ui}

Before you use, share, or download an asset, you can view it more closely. The preview feature lets you view not just the images but a few other supported asset types as well. You can not only view the asset but also view its detailed information and take other actions. To view information of an asset, navigate to the asset or [search](search-assets.md) the asset. Then, click the asset to open its properties. The following figure demonstrates the fields available on an asset preview screen: 

![Properties of an asset UI](assets/properties-ui.png)

* **A:** Title of an asset 
* **B:** Percentage of zoom or preview asset more closely by zooming in or out 
* **C:** Undo zoom to the previously selected percentage 
* **D:** Proceed to previous or next asset 
* **E:** Assets count
* **F:** Download the asset 
* **G:** Collapse or preview information of an asset 
* **H:** Share the asset 
* **I:** Add asset to [!DNL Collection] 
* **J:** Close preview screen
* **K:** Information of an asset which includes title, format, size, resolution, tags, color tags, and smart tags. 

## Supported formats {#supported-formats}

The following table demonstrates the supported file formats in [!DNL the content module of Adobe GenStudio]: 

<table> 
    <tbody>
     <tr>
      <th><strong>File type</strong></th>
      <th><strong>Supported formats</strong></th>
     </tr>
     <tr>
      <td>Image</td>
      <td>
        <ul>
            <li>[!UICONTROL JPEG]</li> 
            <li>[!UICONTROL PNG]</li> 
            <li>[!UICONTROL SVG]</li>
        </ul>
      </td>
     </tr>
     <tr>
      <td>Video</td>
      <td>
        <ul>
            <li>[!UICONTROL Quicktime]</li>  
            <li>[!UICONTROL MP4]</li> 
        </ul>
      </td>
     </tr>
      <tr>
      <td>Document</td>
      <td>
        <ul>
            <li>[!UICONTROL txt] (Plain)</li>  
            <li>[!UICONTROL Doc/Docx]</li> 
            <li>[!UICONTROL XML]</li>
        </ul>
      </td>
     </tr>
     <tr>
      <td>Print media</td>
      <td>
        <ul>
            <li>[!UICONTROL PDF]</li>  
        </ul>
      </td>
     </tr>  
    </tbody>
   </table>

### Derived properties after uploading an asset {#derived-properties}

Once you upload an asset, the content module of Adobe GenStudio derives some properties that are generated automatically. The following is a list of some of them:

* **Size:** Size demonstrates the logical value of an asset as per its dimensions. It clarifies the space that an asset is taking in a repository. [!DNL The content module of Adobe GenStudio] supports assets up to 2GB. 

<!--* **Tags:** Tags help you categorize assets that can be browsed and searched more efficiently. Tagging helps in propagating the appropriate taxonomy to other users and workflows. -->

* **Smart Tags:** [!DNL The content module of Adobe GenStudio] uses Adobe Sensei's smart content services to train assets using recognition algorithm on the tags-based structure. This content intelligence is then used to apply relevant tags on a different set of assets. Smart Tags increase the content velocity of your projects by helping that you find relevant assets quickly. The smart tags are an example of asset information that is not contained in the image. [!DNL The content module of Adobe GenStudio] automatically applies smart tags to assets, by default. 

* **Color Tags:** [Color tags](#https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/assets/manage/color-tag-images.html?lang=en) help you recognize an asset using colors that are automatically identified in an asset using Adobe's Sensei AI capabilities. 

See more at [search predicates](#assets-search.md#narrow-down-search-results).

<!--

### Date range {#date-range} 

The date range allows you to select dates you want to see the assets. You can customize date range by choosing the start and end dates. 

-->

