---
title: Extending the storefront
description: Learn how to extend and configure the storefront.
index: no
hide: yes
hidefromtoc: yes
---
# Extending the Storefront {#extending-storefront}

Learn how to extend and configure the storefront.

## The Story So Far {#story-so-far}

In the previous document of the AEM Content and Commerce developer journey, [Integration of Product Catalog](catalog-integration.md), you learned how to integrate a catalog in your storefront.

This article builds on those fundamentals so you can take the next configuration steps.

## Objective {#objective}

This document helps you understand how to extend and configure the storefront.

## Commerce Multi-Store Setup {#multi-store}

The AEM CIF Core Components can be used on multiple AEM site structures and the underlying GraphQL client implementation can connect to different Magento stores / store views. This allows projects to implement complex multi-store / multi-site setups.

AEM Multi-Site Management features of Live Copy and Language Copy are used in conjunction with the Commerce Integration Framework to globally manage sites across regions and locales.

The recommended setup is to use a 1:1 relationship between AEM site and Magento store view.

To connect an AEM site and AEM CIF Core Components so too to a dedicated store view follow the steps below:

## Configuration {#configuration}

1. Configure multiple stores & store views according to the pattern described in [Magento Websites, Stores & Views](https://docs.magento.com/m2/ce/user_guide/stores/websites-stores-views.html)

2. Make sure the connection between AEM & Magento is working.

3. Create a child configuration of the CIF Cloud Service config following these steps:

   * In AEM go to Tools -> General -> [Configuration Browser](/help/implementing/developing/introduction/configurations.md#using-configuration-browser)
   * Select the base configuration you created
   * Create a new configuration using the steps described at point 2 above

   This new configuration will be created as a child configuration of the base one. You can now go to Tools -> General -> Configuration Browser and create the configuration settings.

   >[!TIP]
   >
   > Commerce catalogs can be addressed by using IDs or UIDs. UIDs got introduced in Magento 2.4.2. Only enable this if your commerce backend supports a GraphQL schema of version 2.4.2 or later.

4. Assign the child configuration to an AEM site

   * Go to AEM Sites console
   * Navigate to the region or language root of your site structure e.g. /content/venia/us _or_ /content/venia/us/en for the Venia sample page
   * Select the page and open page properties
   * Select the Advanced tab
   * In the `Configuration` section select the configuration you created at step


## What's Next {#what-is-next}

Now that you have completed this part of the journey you should:

* Be able to extend and configure your storefront.

Build on this knowledge and continue your journey by next reviewing the document [Building Product Experiences](building-experiences.md), where you will learn how to build product experiences.

## Additional Resources {#additional-resources}

While it is recommended that you move on to the next part of the journey by reviewing the document [Building Product Experiences](building-experiences.md) the following are some additional, optional resources that do a deeper dive on some concepts mentioned in this document, but they are not required to continue on the headless journey.

* [Customize CIF Core Components](/help/commerce-cloud/customizing/customize-cif-components.md) - Learn how to customize AEM CIF Core Components.
* [Commerce Multi-Store Setup](/help/commerce-cloud/configuring/multi-store-setup.md)

