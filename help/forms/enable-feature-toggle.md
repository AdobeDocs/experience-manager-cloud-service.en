# Enable Feature Toggle  on Local Cloud-Ready Setup

## Introduction

Feature Toggle in AEM lets administrators dynamically enable or disable specific features—ideal for managing Early Adopter and Prerelease features without code changes. As agile and cloud-native practices grow, feature toggles help control releases, improve testing, and simplify deployment. This article explains how to enable them in a local cloud-ready setup for AEM Forms adaptive components.

## Prerequisites

Before enabling feature toggles in your local cloud-ready setup, ensure the following:

- AEM 6.5 or later is installed and running locally
- Access to CRX/DE and OSGi Console
- Basic knowledge of AEM run modes and configurations
- Permissions to modify OSGi configurations

## What is a Feature Toggle?

A feature toggle is a mechanism that lets you control the availability of features in your application at runtime. Instead of pushing new code every time you want to activate a feature, you can flip a switch through configuration or external services.

## Why Use Feature Toggles in a Cloud-Ready Setup?

When working in a cloud-ready local environment (e.g., containerized AEM setups), feature toggles help:

* Test experimental features safely.

* Roll out new components in phases.

* Maintain a single codebase across multiple environments.

* Reduce risk during deployments and upgrades.

### Steps to Enable Feature Toggle Locally

Follow these steps to enable feature toggles in your local AEM cloud-ready instance:

1.  Update the OSGi Configuration
Navigate to: [Adobe Experience Manager Web Console
Configuration](http://localhost:4502/system/console/configMgr/com.adobe.aemds.config.FeatureToggleServiceImpl) (http://localhost:4502/system/console/configMgr/com.adobe.aemds.config.FeatureToggleServiceImpl).

![Feature Toggle](/help/forms/assets/aem-web-console-confi.png)

1. Select OSGI -> Bundles

![Feature Toggle](/help/forms/assets/aem-web-console-bundle.png)

2.Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.

3.Click the icon  ✏️ .
4.In the Enabled Toggles section, click➕ .
5.Add the feature toggle id for the feature as shown in the image below.
6.Click Save

>[!NOTE] You can find the feature toggle id in the document    
> 
>You can find the feature toggle id in the document specific to the early adopter features..

![Feature Toggle](/help/forms/assets/feature-toggle.png)

![Feature Toggle](/help/forms/assets/adaptive-form%202.png)

### Disable Feature Toggle

1. To disable the feature toggle(s) for features whose toggle(s) are enabled, follow the steps below:
1. Log in to your AEM Forms instance.
Navigate to http://<author-instance-url>:portnumber/system/console/configMgr.
1. Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.
1. Click the icon ✏️.
1. In the Disabled Toggles section, click ➕.
1. Add the toggle number for the feature to be disabled.

### Technical Consideration

Feature toggles are runtime-managed and best suited for development or testing setups. Adobe recommends limiting their use in production unless needed for controlled rollouts. 

In a local cloud-ready setup, ensure toggles are version-controlled and synced with CI/CD. Page refresh or cache clearing may be needed for changes to reflect.

## Conclusion
Enabling feature toggles in a local cloud-ready setup empowers teams to build and test flexibly without compromising stability. In the case of AEM's Adaptive Forms Core Components, Adobe's feature toggle framework offers a controlled, scalable way to introduce new features with minimal risk.

Whether you're working in Adobe's ecosystem or any other modern cloud-ready stack, feature toggles are essential tools for safer and faster innovation.