---
title: Release Notes for Cloud Manager 2025.4.0
description: Learn about the release of Cloud Manager 2025.4.0 in Adobe Experience Manager as a Cloud Service.
feature: Release Information
role: Admin
exl-id: 24d9fc6f-462d-417b-a728-c18157b23bbe
---
# Release notes for Cloud Manager 2025.4.0 in Adobe Experience Manager as a Cloud Service {#release-notes}

<!-- https://wiki.corp.adobe.com/display/DMSArchitecture/Cloud+Manager+2025.03.0+Release -->

Learn about the release of Cloud Manager 2025.4.0 in AEM (Adobe Experience Manager) as a Cloud Service.


See also the [current release notes for Adobe Experience Manager as a Cloud Service](/help/release-notes/release-notes-cloud/release-notes-current.md).

## Release dates {#release-date}

The release date for Cloud Manager 2025.4.0 in AEM as a Cloud Service is Thursday, April 10, 2025. 

The next planned release is Thursday, May 8, 2025.
 
## What's new {#what-is-new}

* **(UI) Improved deployment visibility**

    The pipeline execution details page in Cloud Manager now shows a status message ("*Waiting - other update in progress*") when a deployment is waiting for another deployment to finish. This workflow makes it easier to understand sequencing during environment deployment.  <!-- CMGR-66890 -->

    ![Development deployment dialog box showing details and breakdown](/help/implementing/cloud-manager/release-notes/assets/dev-deployment.png)

* **(UI) Domain validation enhancement**

    When adding a domain, Cloud Manager now displays an error if the domain is already installed in a Fastly account: "*The domain is already installed in a Fastly account. Please remove it first from there before adding to Cloud Service.*"

## Early adoption program {#early-adoption}

Participate in Cloud Manager's Early Adoption Program to get exclusive access to upcoming features before their general release.

The following early adoption opportunities are currently available:

### Bring Your Own Git - now with support for GitLab and Bitbucket {#gitlab-bitbucket}

<!-- BOTH CS & AMS -->

The **Bring Your Own Git** feature has been expanded to include support for external repositories, such as GitLab and Bitbucket. This new support is in addition to the already existing support for private and enterprise GitHub repositories. When you add these new repos, you can also link them directly to your pipelines. You can host these repositories on public cloud platforms or within your private cloud or infrastructure. This integration also removes the need for constant code synchronization with the Adobe repository and provides the ability to validate pull requests before merging them into a main branch.

Pipelines using external repositories (excluding GitHub-hosted ones) and the **Deployment Trigger** set to **On Git Changes** now start automatically.

See [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md).

![Add Repository dialog box](/help/implementing/cloud-manager/release-notes/assets/repositories-add-release-notes.png)

>[!NOTE]
>
>Currently, the out-of-the-box pull request code quality checks are exclusive to GitHub-hosted repositories, but an update to extend this functionality to other Git vendors is in the works.

If you are interested in testing this new feature and sharing your feedback, send an email to [Grp-CloudManager_BYOG@adobe.com](mailto:grp-cloudmanager_byog@adobe.com) from your email address associated with your Adobe ID. Be sure to include which Git platform you want to use and whether you are on a private/public or enterprise repository structure.

<!--
### AEM Home {#aem-home}

AEM Home introduces a centralized starting point for managing content, assets, and sites within Adobe Experience Manager. Designed to deliver a personalized experience, AEM Home lets you navigate the AEM ecosystem seamlessly according to your roles and goals. Acting as a guide, it provides key insights and recommended actions to help you achieve your objectives efficiently. With a clear, persona-driven layout, AEM Home ensures quick access to essential tools, supporting a streamlined and effective experience across all AEM features.

Available to early adopters, AEM Home offers an optimized experience focused on improving workflows, prioritizing goals, and delivering results. Opting in lets you influence AEM Home's development by providing feedback that helps shape its future and enhances its value for the entire AEM community.

If you are interested in testing this new capability and sharing your feedback, send an email to [Grp-AemHome@adobe.com](mailto:Grp-AemHome@adobe.com) from your email address associated with your Adobe ID. Be sure to include the following information:

* The role that best fits your profile: Content author, Developer, Business owner, Admin, or Other (provide a description).
* Your primary AEM access surface: AEM Sites, AEM Assets, AEM Forms, Cloud Manager, or Other (provide a description). -->

## Bug fixes

* **Issue with certificates missing Common Name (CN) field** 

    Cloud Manager no longer throws a NullPointerException (NPE) and 500 HTTP response when processing EV/OV certificates that do not include a Common Name (CN) in the Subject field. Modern certificates often omit CN and instead use Subject Alternative Name (SAN). This fix ensures that the absence of CN no longer causes a failure during the configuration build process when SAN is present. <!-- CMGR-67548 -->

* **Domain verification issue with incorrect certificate matching**  

    Cloud Manager no longer incorrectly verifies domains using the wrong certificates. Previously, the validation logic used pattern-based matching instead of exact matching, which caused domains like `should-not-be-verified.example.com` to appear as verified due to overlap with valid certificates for `example.com`. This fix ensures that domain validation now checks for exact matches, preventing erroneous certificate associations. <!-- CMGR-67225 -->

* **Enforced uniqueness for Advanced Networking port forward names**  

    Cloud Manager now enforces unique naming for Advanced Networking port forwards. Previously, duplicate names were allowed, which could lead to conflicts. This fix ensures that each port forward entry has a distinct name, aligning with best practices for network configuration integrity. <!-- CMGR-67082 -->


<!-- ## Known issues {#known-issues} -->

