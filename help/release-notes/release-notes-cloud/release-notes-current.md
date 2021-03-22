---
title: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
description: Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service.
---

# Current Release Notes for [!DNL Adobe Experience Manager] as a Cloud Service {#release-notes}

The following section outlines the general Release Notes for the current (latest) version of [!DNL Experience Manager] as a Cloud Service.

>[!NOTE]
>From here you can navigate to release notes of previous versions; for example, for those in 2020, 2021 and so on.

>[!NOTE]
>
>See [Recent Documentation Updates](https://experienceleague.adobe.com/docs/experience-manager-release-information/aem-release-updates/doc-updates/documentation-updates.html) for details of documentation updates not directly related to a release.

## Release Date {#release-date}

The Release Date for [!DNL Adobe Experience Manager] as a Cloud Service 2021.3.0 is March 25, 2021.
The following release (2021.4.0) will be on April 29, 2021.

## [!DNL Adobe Experience Manager Sites] as a Cloud Service {#sites}

<!--
### Progressive Web Apps (PWAs) {#pwa}

* [A Progressive Web App (PWA) version of a site](/help/sites-cloud/authoring/features/enable-pwa.md)  can now be enabled at the project level via simple configuration.
-->

## [!DNL Adobe Experience Manager Assets] as a [!DNL Cloud Service] {#assets}

## What is new in [!DNL Assets] {#what-is-new-assets}

*  [!DNL Experience Manager Assets] as a [!DNL Cloud Service] is entitled to have a pre-configured [!DNL Brand Portal] instance. The [!DNL Cloud Manager] user can activate [!DNL Brand Portal] on [!DNL Experience Manager Assets] as a [!DNL Cloud Service]. See [activate Brand Portal](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/assets/brand-portal/configure-aem-assets-with-brand-portal.html?lang=en).

*  Businesses can now source assets using [!DNL Brand Portal]. Asset sourcing feature leverages [!DNL Brand Portal] to help customers engage with agency users to source assets for new marketing campaigns, photoshoots and projects. See [asset sourcing in [!DNL Brand Portal]](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/asset-sourcing-in-brand-portal/brand-portal-asset-sourcing.html).

* The [!DNL Brand Portal] usage report now displays only the active users. The inactive users are not displayed now. Active users are the ones whose account is assigned to a product profile in the [!DNL Admin Console]. See [[!DNL Brand Portal] reports](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/admin-tools/brand-portal-reports.html).

* In [!DNL Brand Portal], a new download setting is introduced, that lets you create separate folder for each asset when downloading folders, collection, and so on. See [download settings](https://experienceleague.adobe.com/docs/experience-manager-brand-portal/using/download/brand-portal-download-assets.html).

## Bug fixes in [!DNL Assets] {#bug-fixes-assets}

* When a new version of an existing asset is created after resolving the naming conflict, the metadata of original asset is overwritten. (CQ-4313594)
* When an asset with long annotation text is printed, the annotation text is trimmed, even if space is available. (CQ-4314101)
* When multiple assets are selected to update the properties, sometimes either an error occurs or properties of a deselected asset get updated. (CQ-4316532)
* When attempting to open [!UICONTROL Assets Admin Search Rail], the page remains blank and clicking on [!UICONTROL Edit] > [!UICONTROL Settings] generates an error. (CQ-4315079)

## Adobe Experience Manager Commerce as a Cloud Service {#cloud-services-commerce}

### What is New {#what-is-new-commerce}

* Product Experience Management: Enrich product catalog pages individually with Experience Fragments.

* Extended product console properties to show linked Assets and Experience Fragments, including action to quickly navigaet to the associated content.

* Released CIF Venia Reference Site - 2021.02.24 that includes the latest CIF Core Components version v1.8.0. Refer to [CIF Venia Reference Site](https://github.com/adobe/aem-cif-guides-venia/releases/tag/venia-2021.02.24) for more details.

* Released CIF Core Components v1.8.0. Refer to [CIF Core Components](https://github.com/adobe/aem-core-cif-components/releases/tag/core-cif-components-reactor-1.8.0) for more details.

## Cloud Manager {#cloud-manager}

This section outlines the Release Notes for Cloud Manager in AEM as a Cloud Service 2021.3.0.

## Release Date {#release-date-cm-march}

The Release Date for Cloud Manager in AEM as a Cloud Service 2021.3.0 is March 11, 2021.
The next release is planned for April 08, 2021.

### What's New {#what-is-new-march}

* Customers with environments with pre-existing Custom Domain Name configurations for [IP Allow Lists](/help/implementing/cloud-manager/ip-allow-lists/check-ip-allow-list-status.md#pre-existing-cdn), [SSL Certificates](/help/implementing/cloud-manager/managing-ssl-certifications/check-status-ssl-certificate.md#pre-existing-cdn) and [Custom Domain Names](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md#pre-existing-cdn) will see a message about their previously existing configurations and will be able to self-serve via the UI. 

* Users with requisite permissions can now edit a Program, allowing them to do the following in a self-service manner: 

   * Add Sites solution to an existing program with Assets or vice-versa.
   * Remove Sites or Assets from an existing program with both Sites and Assets.
   * Add second, unused solution entitlement either to an existing program or as a new Program. 

* **AEM Push Update** label will now be displayed for both *Pipeline Execution* and *Activity* screens.

*  If an environment is hibernated but there is also an AEM update available, the **Hibernated** status will take precedence over **Update available**.

* Users can now see their Cloud Manager role(s) by selecting the 'View Cloud Manager Role(s)' option after navigating to the User Profile icon (top right) of Unified Shell. 

* The label **Application for Approval** has been relabeled to **Production Approval** for greater clarity.

* The **Version** label has been relabeled to **Git Tag** in the Production pipeline execution screen.

* The labels which define the behavior when important metrics do not meet the defined threshold have been relabeled to reflect their true behavior: **Cancel Immediately** and **Approve Immediately**.

* The class and method deprecation lists have been updated based on version `2021.3.4997.20210303T022849Z-210225` of the AEM Cloud Service SDK.

* Cloud Manager Production pipeline will now include [Custom UI Testing](/help/implementing/cloud-manager/functional-testing.md#custom-ui-testing) capability.

### Bug Fixes {#bug-fixes-cm-march}

* Package versioning was skipped in some cases during AEM push upgrade.

* Some quality issues were not properly discovered when packages were embedded in other packages.

* In obscure situations, the default program name generated upon opening the Add Program dialog could be a duplicate of an existing program name. 

* On occasion, if user navigates away from pipeline execution page immediately after starting a pipeline, an error message is displayed stating that the action failed, although the execution actually starts.

* The build step was unnecessarily restarted when customer builds resulted in invalid packages.

* On occasion, user may see a green "active" status next to an IP Allowlist even when that configuration was not deployed.

* All existing production pipelines will be automatically enabled with the Experience Audit step.

## Content Transfer Tool {#content-transfer-tool}

### Release Date {#release-date-ctt}

The Release Date for Content Transfer Tool v1.3.4 is March 19, 2021.

### Bug Fixes {#bug-fixes-ctt}

* CTT was skipping content from folders with the same name but with a hyphen in the name. This has been fixed. 


### Release Date {#release-date-ctt-march}

The Release Date for Content Transfer Tool v1.3.0 is March 04, 2021.

### What is new in Content Transfer Tool {#what-is-new-ctt-march}

* CTT now installs to `/apps` instead of `/libs` Browser bookmarks to certain pages may no longer be valid.
* When CTT is installed, user will have to navigate an additional level to get to the Content Transfer page. See [Using Content Transfer Tool](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/moving/cloud-migration/content-transfer-tool/using-content-transfer-tool.html) for more details.

### Bug Fixes {#bug-fixes-ctt-march}

* When migrating content from a specific path, CTT was pulling in unrelated resources. This has been fixed

## Code Refactoring Tools {#code-refactoring-tools}

### What is new in Code Refactoring Tools {#what-is-new-crt}

* New features and enhancements for Repository Modernizer. Refer to [GitHub Resource: Repository Modernizer](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/repository-modernizer) for the latest version.
  * Normalize OSGi configs (except RepoInit configs) to the preferred .cfg.json format.
  * Rename OSGi config folders to the specified format.
  * Generate the ui.apps.structure project.
  * Create the analyze module.
  
* New features and enhancements for Dispatcher Converter. Refer to [GitHub Resource: Dispatcher Converter](https://github.com/adobe/aem-cloud-service-source-migration/tree/master/packages/dispatcher-converter)
  * Creation of separate files for different inclusions instead of in lining the content.
  * Ability to handle both folder path of vhosts and path to vhost files.
  * Generation of farm files with large customer configurations in range of 600 and more.

## [!DNL Adobe Experience Manager] as a Cloud Service Foundation {#aem-as-a-cloud-service-foundation}

### Known Issues {#known-issues-foundation}

**Some builds might fail because of an issue with the Build Analyzer Plugin**

In certain cases a project build can fail during the execution of the `aemanalyser-maven-plugin` with the following error message:

```
[ERROR] repoinit: Parsing error in repoinit from extension : Encountered "" at line 15, column 37.
 
Was expecting one of:
 
     
 
[ERROR] Analyser detected errors on feature
```

**Workaround**

To work around this issue, select the latest version of the `aemanalyser-maven-plugin` in the parent `pom.xml` file:

```xml
<aemanalyser.version>0.9.2</aemanalyser.version>
```

