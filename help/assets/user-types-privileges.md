---
title: Assets as a Cloud Service user types and privileges
description: 
feature: Asset Management
role: User, Admin
---
# [!DNL Assets] as a Cloud Service user types and privileges {#assets-user-types-privileges}

| [Search Best Practices](/help/assets/search-best-practices.md) |[Metadata Best Practices](/help/assets/metadata-best-practices.md)|[Content Hub](/help/assets/product-overview.md)|[Dynamic Media with OpenAPI capabilities](/help/assets/dynamic-media-open-apis-overview.md)|[AEM Assets developer documentation](https://developer.adobe.com/experience-cloud/experience-manager-apis/)|
| ------------- | --------------------------- |---------|----|-----|

## [!DNL Assets] as a Cloud Service Ultimate package and user types {#assets-ultimate-package-user-types-privileges}

Assets as a Cloud Service Ultimate package enables you to perform various key Digital Asset Management operations, such as:

* Asset management tasks, such as metadata management, permissions management, and asset governance.

* Trainable Smart Tags for better search.

* Automated content creation by creating asset variations using Adobe Express.

* Integrating Assets available in the Cloud Service repository with Adobe and non-Adobe applications using Asset Selector.

* Delivery of assets using Publish URL.

* Advanced asset management operations, such as, custom schema, metadata translations, custom processing profiles, and so on.

* Custom workflow management.

* API-driven UI extensibility.

* Basic and advanced reporting, such as, downloads, uploads, asset performance, and asset usage by user.

* Additional Stage and Development environments.

The operations that you can perform within Assets as a Cloud Service depends on your user type. See [Available user types](#available-user-types) for more information.


## Why Assets as a Cloud Service Ultimate Package? {#why-ultimate-package-existing-new-users}

New users

Existing users

## What are available user types and privileges? {#available-user-types}

Assets as a Cloud Service offers four types of user types. Each user type provides different set of privileges. The user types include:

* **Administrator**: The standard administrator user, who configures the other three user types within the organization.

* **Limited Users**: Limited users can access and leverage approved assets from your organization using AEM Assets Content Hub portal.

* **Collaborator users**: As a Collaborator user, you can:

   * Work with assets from Experience manager via integrations of Assets available to your organization in other Adobe products and non-Adobe applications.

   * Create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on.

   * Access and leverage approved assets from your organization using AEM Assets Content Hub portal.

* **Power users**: As a Power user, you can:

   * Access all AEM Assets capabilities including managing assets, permissions, metadata and the overall governance and automation around digital assets. 
   
   * Work with assets from Experience manager via integrations of Assets available to your organization in other Adobe and non-Adobe applications.

   * Create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on.

   * Access and leverage approved assets from your organization using AEM Assets Content Hub portal.

The following table summarizes the available Content Hub user types, the privileges they have, and the product profiles that are required to get those privileges:


| User Role    | Limited users | Collaborator users  | Power users | Administrators |
|---------------|----------|----------|-------------------------|---|
| **Capabilities**|
| Access brand approved assets on the Content Hub portal |&#10003; | &#10003;|   &#10003;  |&#10003;|
| Create and edit assets using built-in Adobe Express and Firefly    | &minus; |  &#10003; | &#10003;   |&#10003;|
| Integration of assets within your organization with Adobe and non-Adobe applications     |  &minus; |   &#10003; |     &#10003;   | &#10003;|
| Access all AEM Assets capabilities, such as, managing assets, permissions, metadata and the overall governance and automation        | &minus; | &minus; |    &#10003;   |&#10003;|
| **User needs to be in these product profiles (Admin Console)**|
| AEM > Delivery instance > AEM Assets Limited Users | &#10003;  | &#10003;  |   &#10003;     |&#10003;|
| AEM > Production Author instance > AEM Assets Collaborator Users         | &minus; | &#10003; |   &minus;    |&minus;|
| AEM > Production Author instance > AEM Assets Power Users |  &minus; | &minus; | &#10003;  |&minus;|
| AEM > Production Author instance > AEM Administrators | &minus;  | &minus; | &minus;  |&#10003;|
| **More information**          |  |   |     ||

