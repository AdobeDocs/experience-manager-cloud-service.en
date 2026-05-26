---
product: adobe experience manager
description: Adobe Experience Manager as a Cloud Service documentation.
git-repo: https://github.com/AdobeDocs/experience-manager-cloud-service.en
index: true
type: Documentation
solution: Experience Manager, Experience Manager as a Cloud Service
feature-set: Experience Manager Assets, Experience Manager Sites, Experience Manager, Experience Manager Forms, Experience Manager Cloud Manager, Experience Manager Screens
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: "Experience Manager"
usetq: true
landing-page-name: experience-manager
landing-page-breadcrumb-title: AEM
version: Experience Manager as a Cloud Service
cloud: Experience Cloud
recommendations: noDisplay
---

# Metadata for internal use

Metadata in the GitHub authoring system is hierarchal and is defined the following increasing levels of precedent.

1. metadata.md
1. ToC
1. Article

Metadata defined in the metadata.md file apply to the entire repo, but can be overridden at the ToC and article levels. Any overriding of the metadata should be done at the lowest level possible.

The metadata in the experience-manager-cloud-service.en repo is the minimum required.

metadata.md

* `product`
* `git-repo`
* `index`
* `solution-title`
* `solution-hub-url`
* `getting-started-title`
* `getting-started-url`
* `tutorials-title`
* `tutorials-url`

ToCs

* `sub-product`
* `user-guide-title`

Article

* `title`
* `description`
* `contentOwner` (only on core asset content under `/help/assets`)
