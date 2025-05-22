---
title: Enable Feature Toggle to Integrate Early Adopter and Prerelease Features
description: Feature Toggle is a functionality in AEM that allows administrators to enable new features in a runtime environment.
feature: Adaptive Forms, Foundation Components, Core Components
role: User, Developer
---
# Enable Feature Toggle  on Local Cloud-Ready Setup

Feature Toggle in AEM allows administrators to enable or disable features at runtime ideal for managing Early Adopter and Prerelease features without code changes. It supports gradual rollouts, A/B testing, and quick deactivation of unstable features.

This article covers how to enable feature toggles in a local cloud-ready setup, which simulates AEM as a Cloud Service using the SDK and Dispatcher. This setup helps teams test in a production-like environment before deploying to the cloud.

## Why Use Feature Toggles in a Cloud-Ready Setup?

When working in a cloud-ready local environment, feature toggles help in:

* Testing experimental features safely.

* Rolling out new components in phases.

* Maintaining a single codebase across multiple environments.

* Reducing risk during deployments and upgrades.

## Prerequisites

Before enabling feature toggles in your local cloud-ready setup, ensure the following:

* Navigate to `http://<author-instance-url>:portnumber/system/console/bundles` and check whether **(com.adobe.granite.toggle.impl.dev-1.1.2.jar)** bundle is present or not. In case it is not present [download the bundle from here](/help/forms/assets/com.adobe.granite.toggle.impl.dev-1.1.2.jar).

    ![Feature Toggle](/help/forms/assets/aem-web-console-bundle.png)

* User is member of `forms-users` group.

### Enable Feature Toggle

Follow these steps to enable feature toggles in your local AEM cloud-ready instance:

1. Log in to your AEM Forms instance.

1. Navigate to `http://author-instance-url:portnumber/system/console/configMgr`.

1. Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.

    ![Feature Toggle](/help/forms/assets/aem-web-console-confi.png)

1. Click the icon  ✏️ .
1. In the Enabled Toggles section, click➕ .
1. Add the feature toggle id for the feature as shown in the image below.
    ![Feature Toggle](/help/forms/assets/feature-toggle.png)

1. Click Save

>[!NOTE] 
>
> You can find the feature toggle id in the document specific to the early adopter features.    


### Disable Feature Toggle

To disable the feature toggle(s) for features whose toggle(s) are enabled, follow the steps below:

1. Log in to your AEM Forms instance.
1. Navigate to `http://author-instance-url:portnumber/system/console/configMgr`.
1. Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.
1. Click the icon ✏️.
1. In the Disabled Toggles section, click ➕.
1. Add the toggle number for the feature to be disabled.

    ![Feature Toggle](/help/forms/assets/disable-toggle-feature.png)

### Technical Consideration

Feature toggles are runtime-managed and best suited for development or testing setups. In a local cloud-ready setup, ensure toggles are version-controlled and synced with CI/CD. Page refresh or cache clearing may be needed for changes to reflect.
