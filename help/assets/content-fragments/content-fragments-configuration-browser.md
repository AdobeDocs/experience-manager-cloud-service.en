---
title: Content Fragments - Configuration Browser
description: Learn how to enable certain Content Fragment functionality in the Configuration Browser.
---

# Content Fragments - Configuration Browser{#content-fragments-configuration-browser}

## Enable Content Fragment Functionality for your Instance {#enable-content-fragment-functionality-instance}

Before using Content Fragments you need to use the Configuration Browser to:

* **Content Fragment Models** - mandatory
* **GraphQL Persistent Queries** - optional

>[!CAUTION]
>
>If do you not enable **Content Fragment Models** the **Create** option will not be available for creating new models.

To enable content fragment functionality you need to:

* Enable the use of content fragment functionality via the configuration browser
* Apply the configuration to your Assets folder

### Enable Content Fragment Functionality in Configuration Browser {#enable-content-fragment-functionality-in-configuration-browser}

To [use certain Content Fragment functionality](#creating-a-content-fragment-model) you **must** first enable them via the [Configuration Browser:](/help/implementing/developing/introduction/configurations.md#using-configuration-browser)

1. Navigate to **Tools**, **General**, then open the **Configuration Browser**.
2. Select the location appropriate to your website.
3. Use **Create** to open the dialog, where you:

    1. Specify a **Title**.
    2. To enable their use select 
       * **Content Fragment Models** 
       * **GraphQL Persistent Queries**

       ![configuration](assets/cfm-models-01.png)

4. Select **Create** to save the definition.

### Apply the Configuration to your Assets Folder {#apply-the-configuration-to-your-assets-folder}

When the configuration **global** is enabled for content fragment functionality, then applies to any Assets folder.

To use other configurations (i.e. excluding global) with a comparable Assets folder, then you have to define the connection. This is done by selecting the appropriate **Configuration** in the **Cloud Services** tab of the **Folder Properties** of the appropriate folder.

