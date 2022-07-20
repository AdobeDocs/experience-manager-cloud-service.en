---
title: Content Fragments - Configuration Browser
description: Learn how to enable specific Content Fragment functionality in the Configuration Browser.
exl-id: 55d442ae-ae06-4dfa-8e4e-b415385ccea5
---
# Content Fragments - Configuration Browser{#content-fragments-configuration-browser}

Learn how to enable specific Content Fragment functionality in the Configuration Browser.

## Enable Content Fragment Functionality for your Instance {#enable-content-fragment-functionality-instance}

Before using Content Fragments you need to use the **Configuration Browser** to enable:

* **Content Fragment Models** - mandatory
* **GraphQL Persistent Queries** - optional

>[!CAUTION]
>
>If you do not enable **Content Fragment Models**:
>
>* the **Create** option will not be available for creating new models.
>* you will not be able to [select the Sites configuration to create the related end-point](/help/headless/graphql-api/graphql-endpoint.md).

To enable content fragment functionality you need to:

* Enable the use of content fragment functionality via the configuration browser
* Apply the configuration to your Assets folder

### Enable Content Fragment Functionality in Configuration Browser {#enable-content-fragment-functionality-in-configuration-browser}

To [use certain Content Fragment functionality](#creating-a-content-fragment-model) you **must** first enable them via the **Configuration Browser**:

>[!NOTE]
>
>For further details see also [Configuration Browser:](/help/implementing/developing/introduction/configurations.md#using-configuration-browser).

>[!NOTE]
>
>[Sub-configurations](/help/implementing/developing/introduction/configurations.md#configuration-resolution) (a configuration nested within another configuration) are fully supported for use with Content Fragments, Content Fragment Models and GraphQL queries.
>
>Just to note that:
>
>
>* After creating models in a sub-configuration, it is NOT possible to move or copy the model to another sub-configuration.
>
>* A GraphQL endpoint will (still) be based on a parent (root) configuration.
>
>* Persisted queries will (still) be saved relevant to the parent (root) configuration.


1. Navigate to **Tools**, **General**, then open the **Configuration Browser**.

1. Use **Create** to open the dialog, where you:

   1. Specify a **Title**.
   1. To enable their use select 
      * **Content Fragment Models** 
      * **GraphQL Persistent Queries**

      ![Define configuration](assets/cfm-conf-01.png)

1. Select **Create** to save the definition.

<!-- 1. Select the location appropriate to your website. -->

### Apply the Configuration to your Folder {#apply-the-configuration-to-your-folder}

When the configuration **global** is enabled for content fragment functionality, this then applies to any Assets folder - accessible through the **Assets** console.

To use other configurations (i.e. excluding global) with a comparable Assets folder, then you have to define the connection. This is done by selecting the appropriate **Configuration** in the **Cloud Services** tab of the **Folder Properties** of the appropriate folder.

![Apply configuration](assets/cfm-conf-02.png)
