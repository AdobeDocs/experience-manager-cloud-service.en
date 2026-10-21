---
title: Customizing Page Publishing
description: Learn about the mechanisms that AEM as a Cloud Service provides to customize page publishing functionality.
feature: Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Customizing Page Publishing {#customizing-page-publishing}

You can publish a page from various locations in Adobe Experience Manager as a Cloud Service (AEM). Whether a new page version is created upon publish is determined by the location from where you trigger the publish event.

To ensure a new version is always created you can use a Cloud Manager Environment variable.

>[!CAUTION]
>
>Activating this variable will ensure that a new version is created when you publish a page from:
>
>* Manage Publication for Pages from the Sites console
>* Manage Publication for Experience Fragments
>
>Other locations for publishing a page already trigger a new version. Such locations include the Page Editor and the Universal editor.
>
>Disabling the variable will only deactivate creating a new version from the same locations. It will not deactivate creating a new version from all locations.

## Environment variable to control version creation upon publish {#environment-variable-to-control-version-creation-upon-publish}

To enable creating a new page version when publishing a page from specific locations in AEM create a [Cloud Manager environment variable](/help/implementing/cloud-manager/environment-variables.md):

* name: `PAGE_VERSION_ON_PUBLISH`

* value: 

  * `true`: to enable creating a new version of the page when publishing from the specified location
  * `false` to disable creating a new version of the page when publishing from the specified location