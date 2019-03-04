---
lastModified: 2018-06-28
title: Using links in documentation
seo-title: Using links in Adobe Git/Markdown documentation
description: this article provides guidance on creating links to content and images.
seo-description: this article provides guidance on creating links to content and images for Adobe documentation.
---
# Using links in documentation

This article describes using hyperlinks in documentation pages. Links are easy to add into markdown with a few varying conventions. Links point users to content in the same page, point off into other neighboring pages, or point to external sites and URLs.

> [!IMPORTANT]
> All links must be secure (`https` vs `http`) whenever the target supports it (which the vast majority should).

## Link to URLs

The words that you include in link text should be the title of the page that you're linking to or specific, descriptive text.

**Examples:**

- `For more information, see the [overview article](https://github.com/AdobeDocs/target.en/help/overview.md).`

- `For more details, see [Adobe Legal Concerns](https://www.adobe.com/legal).`

## Link from one article to another

To create an inline link from one article to another article within the same repository, use the following link syntax:

- An article in a directory links to another article in the same directory:

  `[link text](article-name.md)`

- An article links from a subdirectory to an article in the root directory:

  `[link text](../article-name.md)`

- An article links from a sub-subdirectory to an article in the root directory:

  `[link text](../../article-name.md)`

- An article in the root directory links to an article in a subdirectory:

  `[link text](./directory/article-name.md)`

- An article in a subdirectory links to an article in another subdirectory:

  `[link text](../directory/article-name.md)`

- An article in a sub-subdirectory links to an article in another subdirectory:

  `[link text](../../directory/article-name.md)`
  
## Link to anchors

You do not have to create anchors. They're automatically generated at publishing time for all H2 headings. The only thing you have to do is create links to the H2 (##) sections.

- To link to a heading within the same article:

  `[link](#the-text-of-the-level2-section-separated-by-hyphens)`
  
  `[Link to anchors](#links-to-anchors)`

- To link to an anchor in another article in the same subdirectory:

  `[link text](article-name.md#anchor-name)`
  
  `[Configure your profile](overview.md#getting-started)`

- To link to an anchor in another service subdirectory:

  `[link text](../directory/article-name.md#anchor-name)`
  
  `[Configure your profile](../overview.md#configure-your-profile)`

## Link to images

As a best practice, images and files are stored in an `assets` directory at the same level as the Markdown file that links to it.

- An article links to an image in the `assets` subdirectory:

  `![alt text](assets/image-name.png)`

- An article links to an image in the `assets/no-localize` subdirectory:

  `![alt text](assets/no-localize/image-name.png)`

<!--
## Bob's link test

<table id="table_C27955F6B52A45B28BEEAAF14FFC86D8"> 
 <thead> 
  <tr> 
   <th colname="col1" class="entry"> File Type </th> 
   <th colname="col2" class="entry"> Description </th> 
  </tr> 
 </thead>
 <tbody> 
  <tr> 
   <td colname="col1"> <p> <span class="filepath"> .csv </span> </p> </td> 
   <td colname="col2"> <p>A comma-separated values file (such as one created in Excel). This is the file that contains the customer attribute data. See [Link TEST](/help/setup/full-workflow.md) </p> <p> <b>Naming requirements:</b> Ensure that file name extensions do not contain white spaces. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <span class="filepath"> .fin </span> </p> </td> 
   <td colname="col2"> <p>(Required) The <span class="filepath"> .fin </span> file tells the system that you are finished uploading data. The name of the <span class="filepath"> .fin </span> file must match the name of the <span class="filepath"> .csv </span> file. </p> <p>Adobe recommends creating an empty text file with a <span class="filepath"> .fin </span> extension. An empty file saves space and upload time. </p> <p> <p>Note:  Renaming a <span class="filepath"> .fin </span> file is not allowed after it is uploaded. The <span class="filepath"> .fin </span> file must be uploaded separately and cannot be a renamed, previously uploaded file. </p> </p> <p>After you upload the <span class="filepath"> .fin </span> file in the customer attributes FTP, the system retrieves data quickly (within one minute). This differs from other Adobe FTP-based systems, which pick up data less frequently (around once per hour). </p> <p>The <span class="filepath"> .fin </span> file is not required when using the drag-and-drop upload method. </p> </td> 
  </tr> 
  <tr> 
   <td colname="col1"> <p> <span class="filepath"> .gz </span> or <span class="filepath"> .zip </span> </p> </td> 
   <td colname="col2"> <p> <span class="filepath"> .gz </span> (gzip) or <span class="filepath"> .zip </span> - for compressed files. A <span class="filepath"> .zip </span> file cannot contain more than one file in the archive. </p> <p> <b>Naming requirements:</b> The name of the <span class="filepath"> .zip </span> or <span class="filepath"> .gz </span> should match the name of the <span class="filepath"> .csv </span>. For example, if your <span class="filepath"> .csv </span> file is <span class="filepath"> crm_small.csv </span>, the <span class="filepath"> .zip </span> file should be <span class="filepath"> crm_small.csv.zip </span>. </p> <p>The .fin file must match the .csv. </p> </td> 
  </tr> 
 </tbody> 
</table>
-->
