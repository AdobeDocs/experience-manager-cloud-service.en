---
title: Release Notes for Cloud Manager 2024.12.0 in Adobe Experience Manager as a Cloud Service
description: Learn about the release of Cloud Manager 2024.12.0 in AEM as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2024.12.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

Learn about the release of Cloud Manager 2024.12.0 in AEM (Adobe Experience Manager) as a Cloud Service.

>[!NOTE]
>
>See the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2024.12.0 in AEM as a Cloud Service is Thursday, December 5, 2024. 

The next planned release is January 23, 2025.
 

## What's new {#what-is-new}

<!-- * **Java 21 support:** Customers can now optionally build with Java 17 or Java 21, benefiting from performance improvements and new language features. See [Build environment](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md) for configuration steps, including updating your Maven project description, and certain library versions. When the build version is set to Java 17 or Java 21, the runtime defaults to Java 21.

    Starting February 2025, sandboxes and dev environments upgrade to the Java 21 runtime, regardless of the build version (Java 8, 11, 17, or 21). Production environments follow with an upgrade in April 2025. -->

* **A record types:** Support for A record types has been added to improve Go Live Readiness for domains using CDN configurations in AEM Cloud Manager. You now have the option to go live by adding either a CNAME record type or an A record type representing Fastly's IPs, simplifying domain routing. This enhancement eliminates the restriction of relying solely on CNAME records for domain setup with Fastly.

    See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md). <!-- CMGR-63076 -->

<!-- * The AEM Code Quality step now uses SonarQube 9.9 Server, replacing the older 7.4 version. This upgrade brings additional security, performance, and code quality checks, offering more comprehensive analysis and coverage for your projects. -->

* **Add multiple domains to an Edge Delivery Site:** You can now add multiple domains, including both apex and non-apex domains, to an Edge Delivery Site (EDS) in AEM Cloud Manager. This enhancement resolves prior limitations that restricted the ability to associate multiple domains with an EDS origin. The update ensures better flexibility for managing domain configurations and simplifies the Go Live processes for sites with complex domain setups. <!-- CMGR-63007 -->

* **Advanced filtering options:** Advanced filtering options have been introduced on Pipeline execution pages and SSL certificate pages in AEM Cloud Manager. You can now filter by multiple criteria, giving you faster access to relevant data and improving deployment efficiency. <!-- CMGR-26263 -->

    * **Pipeline activities filtering:** Includes pipeline activity filtering, letting you refine search results for specific pipeline activities. Available filters include pipeline, action, and status.
    ![Pipeline activities filtering](/help/implementing/cloud-manager/assets/filters-pipeline.png)


    * **SSL certificates filering:** Includes SSL certificates filtering, letting you refine search results for specific certificates. Available filters include SSL certificate name, ownership, and status.
    ![SSL certificate filtering](/help/implementing/cloud-manager/assets/filters-ssl-certificates.png)

## Early adoption program {#early-adoption}

Be a part of Cloud Manager's early adoption program and have a chance to test upcoming features.

### Bring Your Own Git - now with support for GitLab and Bitbucket {#gitlab-bitbucket}

<!-- BOTH CS & AMS -->

The **Bring Your Own Git** feature has been expanded to include support for external repositories, such as GitLab and Bitbucket. This new support is in addition to the already existing support for private and enterprise GitHub repositories. When you add these new repos, you can also link them directly to your pipelines. You can host these repositories on public cloud platforms or within your private cloud or infrastructure. This integration also removes the need for constant code synchronization with the Adobe repository and provides the ability to validate pull requests before merging them into a main branch.

Pipelines using external repositories (excluding GitHub-hosted ones) and the **Deployment Trigger** set to **On Git Changes** now start automatically.

See [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md).

![Add Repository dialog box](/help/implementing/cloud-manager/release-notes/assets/repositories-add-release-notes.png)

>[!NOTE]
>
>Currently, the out-of-the-box pull request code quality checks are exclusive to GitHub-hosted repositories, but an update to extend this functionality to other Git vendors is in the works.

If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:Grp-CloudManager_BYOG@adobe.com) from your email address associated with your Adobe ID. Be sure to include which Git platform you want to use and whether you are on a private/public or enterprise repository structure.

## Bug fixes

* A safeguard has been added to prevent the deletion of domains with active domain mappings in AEM Cloud Manager. Users attempting to delete such domains now receive an error message instructing them to first delete the domain mapping before proceeding with the domain deletion. This workflow ensures domain integrity and prevents accidental misconfigurations. <!-- CMGR-63033 --> 
* Infrequently, users were unable to add a domain name or update an SSL certificate due to an incorrect status associated in the respective cases. <!-- CMGR-62816 -->


<!-- ## Known issues {#known-issues} -->
