---
title: Configure CIF
description: Configure CIF
---

# Configure CIF on AEM as a Cloud Service

This guide helps you configuring CIF on AEM as a Cloud Service.

## Creating Multiple Category and Product Pages



## Caching Options

## GraphQL API Calls

## Multi-Store Setup

The AEM CIF Core Components can be used on multiple AEM site structures and the underlying GraphQL client implementation can connect to different Magento stores / store views. This allows projects to implement complex multi-store / multi-site setups. The recommended setup is to use a 1:1 relationship between AEM site and Magento store view.

....

We have created a complete step by step [tuturial](configuring/multi-store-setup.md) describing a typical multi-store with AEM & Magento.

## Advanced URL Configurations

Individual product and category page URLs

This project includes sample configurations to demonstrate the usage of custom URLs for product and category pages. This allows each project to setup individual URL patterns for product and category pages according to their SEO needs. A combination of UrlProvider config with Sling Mappings is used.

This configuration must be adjusted with the external domain used by the project. The Sling Mappings are working based on the hostname and domain. Therefore this configuration is disabled by default and must be enabled before deployment. To do so rename the Sling Mapping hostname.adobeaemcloud.com folder in ui.content/src/main/content/jcr_root/etc/map.publish/https according to the used domain name and enable this config by adding resource.resolver.map.location="/etc/map.publish" to the JcrResourceResolver config.

For detailed configuration options see Configuring and customizing product and category pages URLs in the CIF Core Components Wiki and the AEM Resource Mapping documentation.

## Additional Resources

* [AEM Project Archetype](https://github.com/adobe/aem-project-archetype)
* [CIF Core Components](https://github.com/adobe/aem-core-cif-components)
