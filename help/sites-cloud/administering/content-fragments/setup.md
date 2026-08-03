---
title: Content Fragments - Setup
description: Learn how to enable Content Fragment, and GraphQL, functionality for use with AEM headless delivery features and page authoring.
feature: Content Fragments
role: Developer
badgeSaas: label="AEM Sites" type="Positive" tooltip="Applies to AEM Sites)."
exl-id: 3974d698-1e7d-4a5f-a6d5-cbf8d96b4095
solution: Experience Manager Sites
---
# Content Fragments - Setup {#content-fragments-setup}

Content Fragments within Adobe Experience Manager (AEM) as a Cloud Service allow you to prepare content ready for use in multiple locations, and over multiple channels. This is ideal for headless delivery, and page authoring.

To enable your instance for the Content Fragment functionality you need to enable:

* **Content Fragment Models** - mandatory

  >[!CAUTION]
  >
  >If you do not enable **Content Fragment Models**:
  >
  >* the **Create** option will not be available for [creating models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md)
  >* you will not be able to [select the Sites configuration to create the related end-point](/help/headless/graphql-api/graphql-endpoint.md)

* **[GraphQL Persisted Queries](/help/headless/graphql-api/persisted-queries.md)** - optional, needed for use of GraphQL
* **[Cloud Configurations](#customize-the-environment-with-a-content-fragment-cloud-configuration)** - optional, used for configuring various aspects of the Content Fragment environment

Setting up your instance is done:

* by [enabling functionality in the Configuration Browser](#enable-content-fragment-functionality-configuration-browser)
* then [applying the configuration to your individual Assets folders](#apply-the-configuration-to-your-folder)

Then, if needed:

* [enable your GraphQL endpoint](/help/headless/graphql-api/graphql-endpoint.md)
* customize the new Content Fragment editor by defining, and applying, a [Content Fragment Cloud Configuration](#customize-the-editor-with-a-content-fragment-cloud-configuration)

## Enable Content Fragment Functionality in the Configuration Browser {#enable-content-fragment-functionality-configuration-browser}

To use the Content Fragment functionality, of Content Fragment Models and GraphQL Persisted Queries, you **must** first enable them via the **Configuration Browser**:

>[!NOTE]
>
>For more details, see [Configuration Browser](/help/implementing/developing/introduction/configurations.md#using-configuration-browser).

>[!NOTE]
>
>[Subconfigurations](/help/implementing/developing/introduction/configurations.md#configuration-resolution) (a configuration nested within another configuration) are fully supported for use with Content Fragments, Content Fragment Models and GraphQL queries.
>
>Just to note that:
>
>* After creating models in a subconfiguration, it is NOT possible to move or copy the model to another subconfiguration.
>
>* A GraphQL endpoint will (still) be based on a parent (root) configuration.
>
>* Persisted queries will (still) be saved relevant to the parent (root) configuration.

1. Navigate to **Tools**, **General**, then open the **Configuration Browser**.

1. Use **Create** to open the dialog, where you:

   1. Specify a **Title**.
   1. Upon creation, the **Name** becomes the node name in the repository.
      You can enter a name. If you leave the field blank it is automatically generated based on the title, then adjusted according to [AEM naming conventions](/help/implementing/developing/introduction/naming-conventions.md); you can adjust the result if necessary.
   1. To enable their use, as required, select 
      * **Content Fragment Models** 
      * **GraphQL Persisted Queries** 
      * **Cloud Configurations** 

      ![Define configuration](/help/sites-cloud/administering/content-fragments/assets/cf-setup-create-conf.png)

1. Select **Create** to save the definition.

## Apply the Configuration to your Folder {#apply-the-configuration-to-your-folder}

When the configuration **global** is enabled for Content Fragment functionality, it then applies to any Assets folder - accessible through the **Assets** console.

To use other configurations (therefore excluding global) with a comparable Assets folder, you have to define the connection. Do this by selecting the appropriate **Configuration** in the **Cloud Services** tab of the **Folder Properties** of the appropriate folder.

![Apply configuration](/help/sites-cloud/administering/content-fragments/assets/cf-setup-apply-conf.png)

## Customize the environment with a Content Fragment Cloud Configuration {#customize-the-environment-with-a-content-fragment-cloud-configuration}

With a [Content Fragment Cloud Configuration](/help/implementing/developing/extending/content-fragments-cloud-configurations.md) you can customize various aspects of your Content Fragment environment, including certain actions and the new Content Fragment editor.

After [creating](/help/implementing/developing/extending/content-fragments-cloud-configurations.md#create-a-content-fragment-cloud-configuration) and defining the configuration you also [apply the Cloud Configuration to your individual Assets folders](/help/implementing/developing/extending/content-fragments-cloud-configurations.md#apply-the-configuration-to-your-folder), so that it is applied to all the Content Fragments in that folder.
