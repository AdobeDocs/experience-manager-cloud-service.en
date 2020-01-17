---
product: adobe experience manager
git-repo: https://github.com/AdobeDocs/experience-manager-cloud-service.en
index: y
solution-title: Adobe Experience Manager as a Cloud Service
solution-hub-url: https://helpx.adobe.com/support/experience-cloud/core-services.html
getting-started-title: Getting Started
getting-started-url: https://helpx.adobe.com/experience-cloud-core-services/get-started.html
tutorials-title: Tutorials
tutorials-url: https://helpx.adobe.com/analytics/how-to/adobe-launch-publishing-process.html
---

# Metadata for internal use

Metadata in the GitHub authoring system is hierarchal and is defined the the following increasing levels of precedent.

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

Additional information about the metadata can be found in the [internal authoring guide.](https://docs.adobe.com/help/en/collaborative-doc-instructions/collaboration-guide/markdown/metadata.html#solution-metadata)