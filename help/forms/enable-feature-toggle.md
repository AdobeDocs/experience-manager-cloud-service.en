# Enable Feature Toggle  on Local Cloud-Ready Setup

## Introduction

Feature Toggle in AEM allows administrators to dynamically enable or disable specific product features without code changes or full deployments. When working in a local cloud-ready AEM setup, this functionality is essential for testing Early Adopter or Prerelease features in a controlled environment. Enabling feature toggles locally ensures that teams can validate new capabilities, manage risk, and maintain configuration consistency across environments before pushing changes to production.

### Enable Feature Toggle

Feature Toggles for early adopters or new features can be configured through the AEM Web Console Configuration by following the steps below:
Log in to your AEM Forms instance.

1. Navigate to [Adobe Experience Manager Web Console
Configuration](http://localhost:4502/system/console/configMgr) (http://<author-instance-url>:portnumber/system/console/configMgr).

![Feature Toggle](/help/forms/assets/aem-web-console-confi.png)

2.Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.

3.Click the icon  .
4.In the Enabled Toggles section, click  .
5.Add the feature toggle id for the feature as shown in the image below.
6.Click Save

>[!NOTE] You can find the feature toggle id in the document    
> 
>specific to the early adopter features.

![Feature Toggle](/help/forms/assets/feature-toggle.png)

![Feature Toggle](/help/forms/assets/aem-web-console-bundle.png)

![Feature Toggle](/help/forms/assets/adaptive-form%202.png)

### Disable Feature Toggle

1. To disable the feature toggle(s) for features whose toggle(s) are enabled, follow the steps below:
1. Log in to your AEM Forms instance.
Navigate to http://<author-instance-url>:portnumber/system/console/configMgr.
1. Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.
1. Click the icon.
1. In the Disabled Toggles section, click.
1. Add the toggle number for the feature to be disabled.

## Technical Consideration

Feature Toggles are environment-specific and are managed at runtime, so they do not require a server restart. However, some features might require refreshing the relevant pages or clearing the cache to reflect changes.
You can access the list of features enabled through feature toggle for your environment via http://<author-instance-url>:4502/etc.clientlibs/toggles.json.

