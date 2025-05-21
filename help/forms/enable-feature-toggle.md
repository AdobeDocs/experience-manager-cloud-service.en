# Enable Feature Toggle  on Local Cloud-Ready Setup

## Introduction

Feature Toggle in AEM allows administrators to enable or disable features at runtime—ideal for managing Early Adopter and Prerelease features without code changes. It supports gradual rollouts, A/B testing, and quick deactivation of unstable features.

This article covers how to enable feature toggles in a local cloud-ready setup, which simulates AEM as a Cloud Service using the SDK and Dispatcher. This setup helps teams test in a production-like environment before deploying to the cloud.

## Why Use Feature Toggles in a Cloud-Ready Setup?

When working in a cloud-ready local environment (e.g., containerized AEM setups), feature toggles help:

* Test experimental features safely.

* Roll out new components in phases.

* Maintain a single codebase across multiple environments.

* Reduce risk during deployments and upgrades.

## Prerequisites

Before enabling feature toggles in your local cloud-ready setup, ensure the following:

- Required bundles are active

    ![Feature Toggle](/help/forms/assets/aem-web-console-bundle.png)

- Permissions to modify OSGi configurations

### Enable Feature Toggle

Follow these steps to enable feature toggles in your local AEM cloud-ready instance:

1. Log in to your AEM Forms instance.

1. Navigate to http://<author-instance-url>:portnumber/system/console/configMgr.

1. Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.

    ![Feature Toggle](/help/forms/assets/aem-web-console-confi.png)

1. Click the icon  ✏️ .
1. In the Enabled Toggles section, click➕ .

    ![Feature Toggle](/help/forms/assets/feature-toggle.png)

1. Add the feature toggle id for the feature as shown in the image below.
1. Click Save

>[!NOTE] You can find the feature toggle id in the document    
> 
>You can find the feature toggle id in the document specific to the early adopter features.

### Disable Feature Toggle

To disable the feature toggle(s) for features whose toggle(s) are enabled, follow the steps below:
1. Log in to your AEM Forms instance.
1. Navigate to http://<author-instance-url>:portnumber/system/console/configMgr.
1. Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.
1. Click the icon ✏️.
1. In the Disabled Toggles section, click ➕.
1. Add the toggle number for the feature to be disabled.

    ![Feature Toggle](/help/forms/assets/disable-toggle-feature.png)

### Technical Consideration

Feature toggles are runtime-managed and best suited for development or testing setups. In a local cloud-ready setup, ensure toggles are version-controlled and synced with CI/CD. Page refresh or cache clearing may be needed for changes to reflect.