---
title: Best practices for organizing your digital assets for using Dynamic Media Image Profiles or Video Profiles
description: "Tips and best-practices for naming, organizing, and managing Dynamic Media image files and video asset files."
contentOwner: Rick Brough
feature: Asset Management,Image Profiles,Video Profiles
topic: Business Practitioner
---

# Best practices for organizing your digital assets for using Image profiles or Video profiles{#best-practices-for-organizing-your-digital-assets-for-using-profiles}

An important concept regarding the use of Dynamic Media Image Profiles or Video Profiles is that they are assigned to folders. Within a profile are settings for an image or video. These settings process the contents of a folder along with any of its subfolders. Therefore, how you name files and folders, arrange subfolders, and handle the files within these folders, impacts how those assets are processed by the profile.

By using consistent and appropriate file and folder naming strategies, along with good metadata practice, you can make the most of your digital asset collection and ensure that the right files are processed by the right profile.

See [About Dynamic Media Image Profile and Video Profiles](about-image-video-profiles.md).

The following are best practice tips for organizing your digital asset files.

* Organize your files based on the metadata that you add to them instead of on the folders in which they reside. You can accomplish this practice by adding metadata profiles.

  * See [Metadata Profiles.](/help/assets/metadata-profiles.md)
  * See [Metadata for Digital Asset Management](/help/assets/manage-metadata.md).

* Usually, your collection of digital assets are always growing. Therefore, it is important&mdash;earlier on&mdash;to formalize metadata use, folder structure, and file naming among all your uploaded assets. Standardizing on these things ensures that as your pool of digital assets grows, you can apply processing profiles to folders with greater precision and consistency.
* Use folders only to impose a consistent storage structure for your digital assets. For example, folder structures that can help you refine what profiles to assign can include the following:

  * **Development folders** &ndash; contains digital assets that you are currently working on.
  * **Client folders** &ndash; contains digital assets based on clients or project names.
  * **Primary source folders** &ndash; contains original, source digital assets.
  * **Rendition folders** &ndash; contains renditions and copies of the original, source digital assets.
  * **File Size folders** &ndash; contains digital assets based on small, medium, or large file sizes.
  * **Staging folders** &ndash; contains digital assets that are ready to publish live on your website.
  * **Mime type folders** &ndash; contains digital assets that are specific to MIME types such as images, documents, and multimedia.
  * **Archive folders** &ndash; contains retired digital assets.
  * **Date-based folders** &ndash; contains digital assets based on a creation date or a last modified date.

* Create a directory of folders that are not likely to change so that any assigned profiles do not break.
* Suppose that an asset is already published, then you use Adobe Experience Manager to move the asset to another folder and republish from its new location. The original published asset location is still available, along with the newly republished asset. The original published asset, however, is "lost" to Experience Manager and cannot be unpublished. Therefore, as a best practice, unpublish assets first before you move them to a different folder.

