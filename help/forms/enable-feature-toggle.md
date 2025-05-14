# Enable Feature Toggle  on local cloud-ready setup

## Introduction

Feature Toggle in AEM allows administrators to dynamically enable or disable specific product features without code changes or full deployments. When working in a local cloud-ready AEM setup, this functionality is essential for testing Early Adopter or Prerelease features in a controlled environment. Enabling feature toggles locally ensures that teams can validate new capabilities, manage risk, and maintain configuration consistency across environments before pushing changes to production.

### Enable Feature Toggle

1. Feature Toggles for early adopters or new features can be configured through the AEM Web Console Configuration by following the steps below:
Log in to your AEM Forms instance.
1. Navigate to http://<author-instance-url>:portnumber/system/console/configMgr.
1. Search for Adobe Granite Dynamic Toggle Provider in the Configuration Manager.
1. Click the icon  .
1. In the Enabled Toggles section, click  .
1. Add the feature toggle id for the feature as shown in the image below.
1. Click Save

## Technical Consideration

Feature Toggles are environment-specific and are managed at runtime, so they do not require a server restart. However, some features might require refreshing the relevant pages or clearing the cache to reflect changes.
You can access the list of features enabled through feature toggle for your environment via http://<author-instance-url>:4502/etc.clientlibs/toggles.json.

