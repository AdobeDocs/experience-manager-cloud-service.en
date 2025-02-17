---
title: Properties that can be used with the Micro-Frontend Content Fragment Selector for Adobe Experience Manager as a Cloud Service
description: Properties to configure the Micro-Frontend Content Fragment Selector to search, find, and retrieve content fragments from your application.
role: Admin, User
---

# Content Fragment Selector - Properties {#content-fragment-selector-properties}

The Micro-Frontend Content Fragment Selector allows you to browse or search Content Fragments in the repository, and use them in your application.

You can use the following properties to customize how the Content Fragment Selector is rendered and how it can be used:

| Property | Type | Description |
|---|---|---|
| `ìmsToken`| `string` | IMS token used for authentication. |
| `repoId` | `string` | Repository ID used for authentication. |
| `orgId` | `string` | Organization ID used for authentication. |
| `env` | `string` | Deployment environment. |
| `filters` | `FragmentFilter` | Filters to be applied for the list of Content Fragments. By default, fragments under `/content/dam` will be displayed. Default value: `{ folder: "/content/dam" }` |
| `isOpen` | `boolean` | Flag to trigger opening/closing the selector. |
| `onDismiss` | `() => void` | Function to be called when the **Dismiss** icon is selected. |
| `onSubmit` | `({ contentFragments: {id: string, path: string}[], domainNames: string[] }) => void` | Function to be called when **Select** is used after selecting one or more Content Fragments. <br><br>The function will receive:<br><ul><li> the selected Content Fragments with `id` and `path` fields</li><li>and domain names related to the repository's program id and environment id, which have the status `ready` and the `tier` Publish</li></ul><br>If there are no domain names it will be use the Publish instance as a fallback domain. |
| `selectionType` | `string` | Type of fragment selection (single or multiple). Default type of selection is `single`.|
| `dialogSize` | `string` | Size of the dialog that is to be used (`fullscreen` or `fullscreenTakover`). Default type of selection is `fullscreen`. |
| `readonlyFilters` | `ResourceReadonlyFiltersField` | Readonly filters that can be applied for the list of content - and cannot be removed.|
