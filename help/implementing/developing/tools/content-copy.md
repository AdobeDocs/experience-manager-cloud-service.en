---
title: The Content Copy Tool
description: The content copy tool enables users to copy mutable content on-demand from their AEM as a Cloud Service production environments to lower environments for testing purposes.
---

# The Content Copy Tool {#content-copy}

The content copy tool enables users to copy mutable content on-demand from their AEM as a Cloud Service production environments to lower environments for testing purposes.

## Introduction {#introduction}

Current, real data is extremely valuable for testing, validation, and user-acceptance purposes. The content copy tool allows you to copy content from your production AEM environment to a staging or development environment for such testing.

The content to copy is defined by a content set. A content set consists of a list of JCR paths that contain the mutable content to be copied from a source environment to a target environment within the same Cloud Manager program. The following paths are permitted in a content set.

```text
/content
/conf/**/settings/wcm
/conf/**/settings/dam/cfm/models
/conf/**/settings/graphql/persistentQueries
```

>[!NOTE]
>
>A user needs to belong to the following roles/groups to be able to use the content copy tool:
>
>* The **Deployment Manager** role in the source and target environments
>* The **AEM Administrator** group inn the source and target environments

When copying content, the source environment is the source of truth.

* If content has been modified in the destination environment, it will be overwritten by content in the source, if the paths are the same.
* If the paths are different, content from the source will be merged with the content in the destination.

## Creating a Content Set {#create-content-set}

Before any content can be copied a content set must be defined. Follow these steps to create a content set.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to **Environments** screen from the **Overview** page.

1. Navigate to **Content Sets** page from the **Environments** screen.

1. Tap or click the **Add Content Set** button at the top-right of the screen.

1. On the **Details** tab of the the wizard, provide a name and description for the content set and tap or click **Continue**.

1. On the **Content Paths** tab of the wizard, specify the paths of the mutable content to be included in the content set.

   * Tap or click the **Add Path** button to open the path browser and select a path.
   * You can add as many paths as necessary.
   * Paths can be marked to be excluded to finely tune your content set.

1. Tap or click **Create** to create the content set.

The content set can now be used to copy content between environments.

## Editing a Content Set {#edit-content-set}

Follow similar steps as when creating a content step. Instead of tapping or clicking **Add Content Set**, select an existing set from the console and select **Edit** from the ellipsis menu.

## Copying Content {#copy-content}

Once a content set has been created, you can use it to copy content. Follow these steps to copy content.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to **Environments** screen from the **Overview** page.

1. Navigate to **Content Sets** page from the **Environments** screen.

1. Select an content set from the console and select **Copy Content** from the ellipsis menu.

   >[!NOTE]
   >
   >An environment may not be selectable if:
   >
   >* The user does not have the appropriate permissions.
   >* The environment has a running pipeline or a copy content operation in progress.

1. In the **Copy content** dialog, specify the source and destination for your content copy action and tap or click **Copy**.

The copy process starts. The status of the copy process is reflected in the console for the selected content set. The process can have one of the following statuses.

|Status|Description|
|---|---|
|In progress|Content copy operation is ongoing|
|Failed|Content copy operation failed|
|Completed|Content copy operation completed successfully|
|Cancelled|User cancels a content copy operation after starting it|

If you need to abort a content copy operation after starting it, you have the option to cancel it. To do so, on the **Copy Content** page, can select the **Cancel** action from the ellipsis menu of the copy you previously started.

>[!NOTE]
>
>When you cancel a content copy operation, it can result in a partial copy of the content in the destination environment. This can leave the destination environment in an unusable state.

## Limitations {#limitations}

The content copy tool has the following limitations.

* A content copy can not be performed from a lower environment to a higher environment.
* Cross-program content copy is not possible.
* Running concurrent content copy operations on the same environment is not possible.
* The content copy tool should not be used as a cloning or mirroring tool because it can not track moved or deleted content on the source.
* The content copy tool has no versioning capability and can not automatically detect modified content or newly created content on the source environment in a content set since the last content copy operation.
  * If you wish to update your destination environment with content changes only since the last content copy operation, you need to create a content set and specify the paths on the source instance where changes were made since the last content copy operation.
  