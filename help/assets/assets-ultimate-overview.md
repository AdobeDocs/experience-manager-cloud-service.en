---
title: Assets Ultimate
description: Learn more about key aspects of Assets Ultimate, such as, key benefits, user types and their privileges.
feature: Asset Management
role: User, Admin
exl-id: 3ae96cd2-e0ac-43a5-a0bf-bebb1a028b10
---
# [!DNL Assets] as a Cloud Service Ultimate {#assets-ultimate-user-types-privileges}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

![Assets as a Cloud Service Ultimate](/help/assets/assets/aem-assets-ultimate-banner.png)

Assets as a Cloud Service Ultimate offers advanced DAM capabilities. AEM Assets Ultimate is engineered to manage complex content supply chains, ensuring that every piece of content performs well across all channels. 

## Why Assets Ultimate? {#why-ultimate-existing-new-users}

Assets as a Cloud Service Ultimate offers various key benefits that help manage your organization's asset needs effectively, such as:

* Greater flexibility with more user types and privileges associated with those user types, such as Collaborator users, Power users, and Limited users.

* Seamless asset distribution with Content Hub.

* AI-powered content creation and remixing using Adobe Express with Firefly.

* Smoother onboarding or upgrade experience for new and existing users.

## Key capabilities of Assets Ultimate {#capabilities-assets-ultimate}

Assets as a Cloud Service Ultimate enables you to perform various key Digital Asset Management operations, such as:

* **Asset management and library services**​: Tools that enable users to ingest, store, catalog, control, manage, and govern a brand's digital assets in a centralized repository 

* **Search, Discovery, and Collaboration**: Tools that enable users to browse, discover, share, and collaborate on assets they need to create rich customer experiences.

* **Security & Rights Management**: Tools to manage access, permissions, rights, and security to ensure compliance, consistency, and brand integrity.

* **Creative Cloud Connections**: Tools that enable marketing & creative teams to collaborate with simplified access, comment, review, and annotations to update or finalize digital assets.

* **Experience Cloud Connections**: Tools to support native access to digital assets from other Experience Cloud applications and services.

* **Distribution Portal Experience (Content Hub)**: Tools to expand access to a brand's approved digital assets to extended stakeholders to ensure usage and brand consistency.

* **Integrations**: integrations with other Adobe and non-Adobe applications.

* **Dynamic Media (add-on)**: Tools to transform and deliver images, videos, and other emerging content for rich, interactive, multimedia experiences for any device at scale.

* **Customization**: Tools to customize the DAM User Interface access to APIs for further development.

* **Custom Extensibility**: Extensive flexibility through its robust API-first platform, enabling seamless integration and customization to meet the customer complex IT infrastructure.

* **Content Automation (add-on)**: Tools to unify work management and automate digital asset transformation workflows for content production at scale.

The operations that you can perform within Assets as a Cloud Service depends on your user type. See [Available user types](#available-user-types) for more information.


## What are available user types and privileges? {#available-user-types}

Assets as a Cloud Service offers four user types. Each user type provides a different set of privileges. The user types include:

* **Administrator**: The standard administrator user, who configures the other three user types within the organization.

* **Limited Users**: Limited users can access and leverage approved assets from your organization using AEM Assets Content Hub portal.

* **Collaborator users**: As a Collaborator user, you can:

   * Work with assets from Experience manager via integrations of Assets available to your organization in other Adobe products and non-Adobe applications.

   * Create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on.

   * Access and leverage approved assets from your organization using AEM Assets Content Hub portal.

* **Power users**: As a Power user, you can:

   * Access all AEM Assets capabilities including managing assets, metadata and the overall governance and automation around digital assets. 
   
   * Work with assets from Experience manager via integrations of Assets available to your organization in other Adobe and non-Adobe applications.

   * Create and edit assets using built-in Adobe Express and Firefly leveraging professionally designed templates, brand kits, Adobe Stock assets, and so on.

   * Access and leverage approved assets from your organization using AEM Assets Content Hub portal.

   ![Assets as a Cloud Service Power user](/help/assets/assets/assets-cs-power-users.png)

The following table summarizes the available AEM Assets user types, the privileges they have, and the product profiles that are required to get those privileges:


| User Role    | Limited users | Collaborator users  | Power users | Administrators |
|---------------|----------|----------|-------------------------|---|
| **Capabilities**|
| Access brand approved assets on the Content Hub portal |&#10003; | &#10003;|   &#10003;  |&#10003;|
| Create and edit assets using built-in Adobe Express and Firefly    | &minus; |  &#10003; | &#10003;   |&#10003;|
| Integration of assets within your organization with Adobe and non-Adobe applications     |  &minus; |   &#10003; |     &#10003;   | &#10003;|
| Access all AEM Assets capabilities, such as, managing assets, metadata and the overall governance and automation        | &minus; | &minus; |    &#10003;   |&#10003;|
| Manage permissions on content in AEM Assets author environment        | &minus; | &minus; |    &minus;   |&#10003;|
| **User needs to be in these product profiles (Admin Console)**|
| AEM > Delivery instance > AEM Assets Limited Users | &#10003;  | &#10003;  |   &#10003;     |&#10003;|
| AEM > Production Author instance > AEM Assets Collaborator Users         | &minus; | &#10003; |   &minus;    |&minus;|
| AEM > Production Author instance > AEM Assets Power Users |  &minus; | &minus; | &#10003;  |&minus;|
| AEM > Production Author instance > AEM Administrators | &minus;  | &minus; | &minus;  |&#10003;|
| **More information**          | See [Enable Content Hub](/help/assets/enable-assets-ultimate.md##enable-assets-ultimate-new-users) | See [Onboard Collaborator Users](/help/assets/enable-assets-ultimate.md#onboard-collaborator-users)  | See [Onboard Power Users](/help/assets/enable-assets-ultimate.md#onboard-power-users)    |- |

For information on how to get started with Assets Ultimate, see [Enable AEM Assets Ultimate](/help/assets/enable-assets-ultimate.md).

AEM Assets also provides a lighter weight DAM for customers who do not have advanced requirements such as, UI extensibility, API-driven automation, and custom code deployment. For more information, see [AEM Assets Prime](/help/assets/assets-prime.md).
