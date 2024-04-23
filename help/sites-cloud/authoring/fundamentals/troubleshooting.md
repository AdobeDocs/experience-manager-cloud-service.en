---
title: Troubleshooting AEM when Authoring
description: Some issues that you might encounter when using AEM
exl-id: b9c0584d-255e-486d-b829-09e07499ecd2
---
# Troubleshooting AEM when Authoring {#troubleshooting-aem-when-authoring}

The following section covers some issues that you might encounter when using AEM, together with suggestions on how to troubleshoot them.

## Old page version still on published site {#old-page-version-still-on-published-site}

* **Issue**:
  * You have made changes to a page and published the page to the publish site, but the *old* version of the page is still being shown on the publish site.
* **Reason**:
  * This can have several causes, most often the cache (either your local browser or the Dispatcher), though it can sometimes be an issue with the replication queue.
* **Solutions**:
  * There are various possibilities here:
  * Confirm that the page has been replicated correctly. Check the page status and if necessary, the state of the replication queue.
  * Clear the cache in your local browser and access your page again.
  * Add `?` to the end of the page URL. For example:
    * `http://<host>:<port>/sites.html/content?`
    * This will request the page directly from AEM and bypass the Dispatcher. If you receive the updated page, it is an indication that you should clear the Dispatcher cache.
  * Contact your system administrator is there are issues with the replication queues.

## Component Actions not visible on Toolbar {#component-actions-not-visible-on-toolbar}

* **Issue**:
  * The full range of applicable component actions are not visible when editing a content page on the author environment.
* **Reason**:
  * In rare cases a previous action might impact the toolbar.
* **Solution**:
  * Refresh the page.
