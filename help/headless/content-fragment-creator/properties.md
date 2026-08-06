---
title: Micro-Frontend Content Fragment Creator Properties for Adobe Experience Manager as a Cloud Service
description: Properties to configure the Micro-Frontend Content Fragment Creator to create content fragments from your application.
role: Admin, User, Developer
---
# Content Fragment Creator - Related Properties {#content-fragment-creator-related-properties}

The Micro-Frontend Content Fragment Creator allows you to create Content Fragments in the repository, and use them in your application.

You can use the following properties to customize how the Content Fragment Creator is rendered and how it can be used.

## Content Fragment Creator Properties {#content-fragment-creator-properties}

| Property | Type | Required | Default | Description |
|--- |--- |--- |--- |--- |
| `open` | boolean | Yes | | Controls whether the dialog is visible. |
| `onDismiss` | () => void | Yes | | Callback when the dialog is dismissed (cancel or close). |
| `env` | `Env` ("QA" \| "DEV" \| "DEV_443" \| "STAGE" \| "PROD") | No | | Deployment environment for the embedded dialog. If not provided, it is inferred from the current page's hostname. |
| `imsToken` | string | No | | IMS token for authentication. When provided together with `repoId`, the dialog renders without needing repository discovery. |
| `repoId` | string | No | | Repository ID (AEM host). When provided together with `imsToken`, the dialog uses this repo and skips discovery. |
| `orgId` | string | No | | Organization ID used for repository discovery. |
| `locale` | string | No | | Locale (e.g. `"en-US"`). |
| `selectedFolder` | string | No | | Pre-selected folder path for the new fragment (e.g. the current folder in an inventory view). |
| `meta` | Record<string, unknown> | No | | Optional metadata passed to the create operation (e.g. `useHeadlessEditor`, resource type). |
| `allowedModels` | string[] | No | | Optional list of allowed content fragment model paths/IDs. When provided, only these models can be selected when creating a fragment. |
| `allowedModelsTags` | string[] | No | | Optional list of allowed content fragment model tags, used to filter the models offered in the dialog. |
| `onCreate` | (contentFragment: `ContentFragment`) => void | No | | Callback invoked when a content fragment is successfully created. Receives the created fragment (see below). |

### ContentFragment shape {#contentfragment-shape}

The `ContentFragment` shape (passed to `onCreate`) is:

```typescript
type ContentFragment = {
    id: string;
    path: string;
    title: string;
    [key: string]: unknown;
};
```

## CreateContentFragmentDialog Properties {#createcontentfragmentdialog-properties}

Properties for the `CreateContentFragmentDialog` component:

| Property | Type | Required | Default | Description |
|--- |--- |--- |--- |--- |
| `open` | boolean | Yes | | Controls whether the dialog is visible. |
| `onDismiss` | () => void | Yes | | Callback when the dialog is dismissed (cancel or close). |
| `env` | [Env](https://www.npmjs.com/package/@aem-sites/content-fragment-creator) | No | | Deployment environment for the embedded dialog. If not provided, it is inferred from the hostname of the current page. |
| `imsToken` | string | No | | IMS token for authentication. When provided together with `repoId`, the dialog renders without needing repository discovery. |
| `repoId` | string | No | | Repository ID (AEM host). When provided together with `imsToken`, the dialog uses this repo and skips discovery. |
| `orgId` | string | No | | Organization ID used for repository discovery. |
| `locale` | string | No | | Locale (e.g. `"en-US"`). |
| `selectedFolder` | string | No | | Pre-selected folder path for the new fragment (e.g. the current folder in an inventory view). |
| `meta` | Record<string, unknown> | No | | Optional metadata passed to the create operation (e.g. `useHeadlessEditor`, resource type). |
| `allowedModels` | string[] | No | | Optional list of allowed Content Fragment model paths/IDs. When provided, only these models can be selected when creating a fragment. |
| `allowedModelsTags` | string[] | No | | Optional list of allowed Content Fragment model tags, used to filter the models offered in the dialog. |
| `onCreate` | (contentFragment: `ContentFragment`) => void | No | | Callback invoked when a Content Fragment is successfully created. Receives the created fragment (see below). |

## Related Resources {#related-resources}

* [Content Fragment Creator example](https://github.com/adobe/aem-content-fragment-selector-mfe-examples/tree/main/examples/react#content-fragment-creator)

* [`@aem-sites/content-fragment-creator` on npm](https://www.npmjs.com/package/@aem-sites/content-fragment-creator)
