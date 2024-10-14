---
title: Metadata management and best practices
description: Learn about metadata best practices to effectively manage your digital assets.
role: User, Admin
exl-id: d90519df-55a6-4e23-81ad-ff2365d71c0d
feature: Metadata, Best Practices
---
<!-- Keywords to focus on:
metadata best practices
aem metadata 
experience manager metadata-->

# Metadata management and best practices {#metadata-best-practices}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- |---------|----|-----|

To make your business stand out and engage more customers, utilizing high-quality visuals like images, videos, and other digital assets is crucial. To achieve this, you need a process that allows you to add metadata to all digital assets, making them easily searchable. Metadata is the data that provides essential details about digital assets, including the asset's name, type, location within a repository, modified date, and associated tags. Metadata streamlines asset management, improves searchability and accessibility, and ensures effective version control.

Learn how to use metadata in the Digital Asset Management (DAM) system to effectively [manage metadata of your digital assets](manage-metadata.md).

## Types of metadata 

Based on the various aspects of data, metadata is categorized as Technical metadata, Informational metadata, and Administrative metadata.

### Technical metadata

Technical metadata comprises the technical aspects of an asset. This type of metadata is crucial for the users to understand the inherent characteristics of digital assets, facilitating efficient processing and utilization.
It includes details such as:

* File size
* Format
* Resolution
* Dimensions
* Color mode

### Informational metadata

Informational metadata encompasses descriptive information that enhances understanding of an asset's content. This metadata is pivotal in content discovery, searchability, and comprehension of the asset's significance. Informational metadata includes keywords, captions, and descriptions.

For example, when managing a video in Experience Manager Assets, we can include the following informational metadata:

* **Keywords**: Marketing, Product launch, Promo
* **Caption**: Introducing our latest product with exciting features
* **Description**: A detailed overview of the video content.

Users searching for marketing-related content can easily find and understand the significance of the above video.

### Administrative metadata

Administrative metadata deals with the managerial aspects of digital assets. It ensures access control, compliance, and managing the overall lifecycle of assets within the digital asset management system. It includes information related to:

* Asset ownership
* Usage rights
* Permissions
* Other administrative details

Administrative metadata ensures the correct asset management, controlling access, and compliance within the digital asset management system.

## Metadata best practices

### Define your metadata strategy from the beginning

Metadata management begins with defining a metadata strategy to provide a foundation to assess the long-term value.

Creating a custom metadata schema per your requirements is crucial when planning your metadata strategy. A well-designed schema provides a structured framework for categorizing and organizing assets within Experience Manager.

#### Video: Add custom fields to metadata schema

>[!VIDEO](https://video.tv.adobe.com/v/3425977)

Your metadata strategy may include defining the following:

* **Objectives:** Clearly describe the objectives and expected results of the metadata. Identify what you aim to achieve by adding the metadata.

* **Purpose:** Define why you are capturing metadata. Specify the value that it adds to your processes, systems, or organization.

* **Accessibility plan:** Create a plan to make the metadata easily accessible and discoverable. Explain who is going to use it, and the tools or methods to use. 

* **Metadata properties:** Identify and define each metadata property carefully. Ensure that each property has a clear reason for being included, connecting to the objectives and purpose.

To ensure consistent results throughout the repository, thoughtfully plan the strategy. Learn more about [metadata schemas](metadata-schemas.md).

### Create a metadata governance plan

Data governance ensures that the organization's metadata management efforts are aligned with the overall business objectives.
The governance strategy may include:

* Establishing policies and procedures for data and metadata management.
* Setting standards for data quality and integrity.
* Defining roles and responsibilities in data management.

Determine where the information comes from and examine the details of the metadata strategy, including the properties and their sources. It can scale depending on the complexity of the strategy. In larger enterprises, there's a master metadata management system overseeing multiple systems in the master stack.

>[!NOTE]
>
>Learn how to [manage metadata of your digital assets](https://experienceleague.adobe.com/docs/experience-manager-65/assets/using/metadata.html).

### Be consistent with the metadata strategy

A consistent metadata strategy ensures effective organization and retrieval of digital assets. Adopt a strategic approach to capture and implement metadata values, allowing the flexibility for evolution without unnecessary changes. <br>

In enterprise-wide metadata management, consistency is important when naming and referencing assets. For example, when managing multiple assets simultaneously, "consider adding metadata in bulk. <br>

Here are some of the best practices to follow:

   * **Avoid duplicate values:** If you have a collection of images from a marketing campaign, use consistent names and avoid duplicates.<br>
   For instance, instead of using duplicate names like *campaign_image_001* and *campaign_image_002*, implement a systematic naming convention such as *event_promotion* and *product_launch*, ensuring a clear and ordered identification.

   * **Use controlled vocabularies effectively:** Implement controlled vocabularies by employing standardized terms for tags. Learn how to implement [AEM Tagging Framework](/help/implementing/developing/introduction/tagging-framework.md) effectively.  <br>
   For example, consistently use terms such as *product_launch* or *event_promotion* when tagging images with themes to maintain systematic sequence.

* **Maintain accuracy and completeness:** To keep metadata consistent, accuracy, completeness, and alignment across various sources are crucial.
  For instance, when adding metadata to a PDF document, verify that details like author names and keywords are accurate and complete.

#### Video: Add bulk metadata to assets

>[!VIDEO](https://video.tv.adobe.com/v/3425978)

### Assess and improve metadata searchability

Assess your metadata strategy to improve metadata searchability. Simplify workflows and enhance search capabilities for efficient reuse. Avoid dealing with metadata that lacks a clear purpose.

You can consider the following best practices to optimize your metadata searchability:

* **Keyword optimization:** Improve metadata searchability by optimizing keywords associated with assets. You can improve the relevance of keywords for particular assets in the [!UICONTROL Assets Manager] by following these steps:

   1. Go to **[!UICONTROL Assets]** > **[!UICONTROL File]** > **[!UICONTROL [Asset folder]]**.
   1. Select the asset for which you want to update the metadata, and then click **[!UICONTROL Properties]**.
   1. Navigate to the **[!UICONTROL Advanced]** tab, and then click **[!UICONTROL Add]** under the **[!UICONTROL Elevate for search keywords]**. <br>You must use the default metadata schema to elevate the search keywords. 
   1. Enter the keyword for which you want to boost the search, and then click **[!UICONTROL Add]**.<br>
   You can add multiple keywords and arrange them as per your priority.
   1. Click **[!UICONTROL Save & Close]**.
   Search the asset using the keywords you added. The asset appears among the top search results.
   
   Learn how to [boost search in Experience Manager](https://experienceleague.adobe.com/docs/experience-manager-learn/assets/search-and-discovery/search-boost.html).

* **Custom metadata fields:** Customize your metadata fields to capture additional information about assets. For example, add specific fields for project details, copyright information, or any other relevant data that enhances search capabilities. Learn [how to edit or add custom metadata](meta-edit.md) in Experience Manager Assets.


* **Metadata validation:** Implement validation checks for metadata entries to ensure consistency and accuracy. Using controlled vocabularies makes the validation process smoother and decreases the chance of unclear or inconsistent entries. This can involve setting guidelines for certain metadata properties to avoid ambiguous or inconsistent information.

* **Usage tracking:** Assess the relevance and usage of different metadata properties over time. Identify and prioritize frequently used metadata or significantly contribute to search and retrieval processes.

#### Video: Add keywords to improve searchability

>[!VIDEO](https://video.tv.adobe.com/v/3425979)

### Keep metadata simple and easy to understand

Simplify metadata for better governance and user adoption. Keep it straightforward and easy to understand, encouraging users to add essential information. 
Try the following best practices to simplify the metadata:

* **Optimize property options:** Focus on highlighting essential properties without burdening the users with too many metadata fields to fill in. For instance, when adding metadata for an image, include only key fields like title, description, and tags for effective categorization.

* **Eliminate unnecessary default properties:** Simplify the metadata form by eliminating default out-of-the-box properties irrelevant to your use case. Remove rarely used default properties for a cleaner interface and experience.

* **Periodically review and update metadata:** Regularly update metadata and adapt to changing needs and technologies to ensure that users provide valuable information over time.

### Analyze content journey

   Examine the content supply chain to find metadata sources and involve all stakeholders, starting from the top, for a thorough best practice approach. Involve different staff members to ensure complete support across the organization. <br>Incorporate metadata at various stages to share the responsibility of providing asset details during uploading. For instance, integrating [!DNL Experience Manager Assets] and [!DNL Workfront] offers substantial benefits in terms of metadata management, enhancing efficiency and collaboration in content creation and management. This integration ensures effective metadata synchronization for linked assets, automatically updating project details when changes are made in [!DNL Workfront].

   Communicate objectives, progress, milestones, and challenges early to receive input and cooperation from all stakeholders. Encourage collaboration throughout the organization to create efficient processes and valuable metadata. 

Learn more about [metadata and its related concepts](https://experienceleague.adobe.com/docs/experience-manager-65/assets/administer/metadata-concepts.html) to effectively manage your Experience Manager metadata.
