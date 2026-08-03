---
title: Micro-Frontend Content Fragment Selector Properties for Adobe Experience Manager as a Cloud Service
description: Properties to configure the Micro-Frontend Content Fragment Selector to search, find, and retrieve content fragments from your application.
role: Admin, User, Developer
exl-id: c81b5256-09fb-41ce-9581-f6d1ad316ca4
---
# Content Fragment Selector - Related Properties {#content-fragment-selector-related-properties}

The Micro-Frontend Content Fragment Selector allows you to browse or search Content Fragments in the repository, and use them in your application.

You can use the following properties to customize how the Content Fragment Selector is rendered and how it can be used:

## Content Fragment Selector Properties {#content-fragment-selector-properties}

| Property | Type | Required | Default | Description |
|--- |--- |--- |--- |--- |
| `ref` | FragmentSelectorRef | No | | Reference to the `ContentFragmentSelector` instance, allowing access to provided functionality such as `reload`. |
| `apiKey` | string | No | | API key reported to analytics on `digitalData.page.attributes.apiKey`. Used only for tracking — not for data API calls. If not provided, it is derived from the `imsToken` (`client_id` claim), falling back to the package default. |
| `imsToken` | string | No | | IMS token used for authentication. If not provided, the IMS login flow will be initiated. |
| `repoId` | string | No | | Repository ID used for the Fragment Selector. When provided, the selector automatically connects to the specified repository, and the repository dropdown is hidden. If not provided, the user can select a repository from the list of available repositories they have access to. |
| `allowedRepositoryIds` | string[] | No | | List of repository IDs to filter repositories and content fragments in the Content Fragment Selector. When provided with repository IDs, only these repositories will be visible in the repository selector. If not provided or empty array, all repositories the user has access to will be available. |
| `defaultRepoId` | string | No | | Repository ID that will be selected by default when the repository selector is shown. Used only when `repoId` is not provided. If `repoId` is set, the repository selector is hidden, and this value is ignored. |
| `orgId` | string | No | | Organization ID used for authentication. If not provided, the user can select a repository from different organizations they have access to. If the user doesn't have access to any repository or organization, the content will not be loaded. |
| `locale` | string | No | "en-US" | Locale. |
| `env` | string | No | | Deployment environment. See the `Env` type for allowed environment names. |
| `filters` | FragmentFilter | No | `{ folder: "/content/dam" }` | Filters to be applied to the list of content fragments. By default, fragments under `/content/dam` will be displayed. |
| `repoFilters` | Record<string, FragmentFilterWithReadonlySupport> | No | | Per-repository filter overrides keyed by repository id. <br>Use when the selector exposes multiple repositories, but each needs different filters (e.g. Status: Draft for one author instance while others use Status: Published, Modified). <br>When the active repository has an entry, it fully replaces filters for that repository (the defaults are not merged in), so each override must declare the complete filter set it needs. Repositories without an entry fall back to filters, so omitting `repoFilters` preserves the existing behavior. The override is re-applied automatically when the user switches repositories. Each entry supports the same readonly markers as filters. |
| `isOpen` | boolean | No | `false` | Flag to control whether the selector is open or closed. |
| `noWrap` | boolean | No | `false` | Determines whether the Fragment Selector is rendered without a wrapping dialog. When set to `true`, the Fragment Selector is embedded directly in the parent container. Useful for integrating the selector into custom layouts or workflows. |
| `onSelectionChange` | ({ contentFragments: `ContentFragmentSelection`, domainName?: `string`, tenantInfo?: `string`, repoId?: `string`, deliveryRepos?: `DeliveryRepository[]` }) => void | No | | Callback function triggered whenever the selection of content fragments changes. Provides the currently selected fragments, domain name, tenant info, repository ID, and delivery repositories. |
| `onDismiss` | () => void | No | | Callback function triggered when the dismiss action is performed (e.g., closing the selector). |
| `onSubmit` | ({ contentFragments: `ContentFragmentSelection`, domainName?: `string`, tenantInfo?: `string`, repoId?: `string`, deliveryRepos?: `DeliveryRepository[]` }) => void | No | | Callback function triggered when the user confirms their selection. Receives the selected content fragments, domain name, tenant info, repository ID, and delivery repositories. |
| `theme` | "light" or "dark" | No | | Theme for the Fragment Selector. By default, it is set to the unifiedShell environment theme. |
| `selectionType` | "single" or "multiple" | No | `single` | Selection type can be used to restrict selection for the Fragment Selector. |
| `maxItems` | number | No | | Maximum number of items that can be selected when `selectionType` is `multiple`. When not specified, unlimited selection is allowed. Not applicable for single selection mode. |
| `dialogSize` | "fullscreen" or "fullscreenTakeover" | No | `fullscreen` | Optional prop to control the dialog size. |
| `runningInUnifiedShell` | boolean | No | | Whether DestinationSelector is running under UnifiedShell or standalone. |
| `selectedFragments` | ContentFragmentIdentifier[] | No | `[]` | Initial selection of content fragments to be pre-selected when the selector opens. |
| `hipaaEnabled` | boolean | No | `false` | Indicates whether HIPAA compliance is enabled. |
| `inventoryView` | InventoryViewType | No | `table` | Inventory default view type to be used in the selector. |
| `inventoryViewToggleEnabled` | boolean | No | `false` | Indicates whether the inventory view toggle is enabled, allowing the user to switch between table and grid views. |
| `selectFields` | boolean  | No | `false`| Indicates whether the field-selection step is enabled. When `true`, the user picks which fields to expose for each selected fragment, and the chosen fields are returned as a per-fragment `selectedFields` map on the `onSelectionChange` and `onSubmit` payloads. When `false` (default), the step is skipped and `selectedFields` is omitted from each fragment. |
| `variationsFilters`| object | No | | Optional.<br>Adjusts the variation dropdown (not the main list—use filters for that). Only status is supported today, with "PUBLISHED" as the supported value (e.g. { status: ["PUBLISHED"] }). Other keys are ignored. Omit the prop to show all variations. |
| `rememberState` | boolean | No | `false` | When `true`, the selector persists the user's active filters, saved searches, and last-used repository to IndexedDB and restores them automatically on the next load. Opt-in — existing consumers require no changes when omitted. |
| `amsRepositories` | Array<{ label: string; value: string; orgId?: string }> | No | | Optional list of AMS repositories to include in the repository picker. These are concatenated with cloud repositories from the discovery service. Each entry may include an optional `orgId` for multi-org users. When omitted, the top-level orgId prop is used, then an Adobe IMS lookup. AMS repos always use the raw `imsToken` (no cloud token exchange). Subject to `allowedRepositoryIds` filtering when that prop is also provided. |

## ImsAuthProps Properties {#imsauthprops-properties}

The `ImsAuthProps` properties define the authentication information and flow that the Content Fragment Selector uses to obtain an `imsToken`. By setting these properties, you can control how the authentication flow should behave and register listeners for various authentication events.

| Property Name | Description |
|--- |--- |
| `imsClientId` | A string value representing the IMS client ID used for authentication purposes. This value is provided by Adobe and is specific to your Adobe AEM CS organization. |
| `imsScope` | Describes the scopes used in authentication. The scopes determine the level of access that the application has to your organization resources. Multiple scopes can be separated by commas. |
| `redirectUrl` | Represents the URL where the user is redirected after authentication. This value is typically set to the current URL of the application. If a `redirectUrl` is not supplied, `ImsAuthService` will use the redirectUrl used to register the `imsClientId` |
| `modalMode` | A boolean indicating whether the authentication flow should be displayed in a modal (pop-up) or not. If set to `true`, the authentication flow is displayed in a pop-up. If set to `false`, the authentication flow is displayed in a full page reload. _Note:_ for better UX, you can dynamically control this value if the user has browser pop-up disabled. |
| `onImsServiceInitialized` | A callback function that is called when the Adobe IMS authentication service is initialized. This function takes one parameter, `service`, which is an object representing the Adobe IMS service. See [`ImsAuthService`](#imsauthservice-ims-auth-service) for more details. |
| `onAccessTokenReceived` | A callback function that is called when an `imsToken` is received from the Adobe IMS authentication service. This function takes one parameter, `imsToken`, which is a string representing the access token. |
| `onAccessTokenExpired` | A callback function that is called when an access token has expired. This function is typically used to trigger a new authentication flow to obtain a new access token. |
| `onErrorReceived` | A callback function that is called when an error occurs during authentication. This function takes two parameters: the error type and error message. The error type is a string representing the type of error and the error message is a string representing the error message. |

## ImsAuthService Properties {#imsauthservice-properties}

The `ImsAuthService` class handles the authentication flow for the Content Fragment Selector. It is responsible for obtaining an `imsToken` from the Adobe IMS authentication service. The `imsToken` is used to authenticate the user and authorize access to the Adobe Experience Manager (AEM) CS repository. ImsAuthService uses the `ImsAuthProps` properties to control the authentication flow and register listeners for various authentication events. You can use the convenient `registerContentFragmentSelectorAuthService` function to register the `ImsAuthService` instance with the Content Fragment Selector. The following functions are available on the `ImsAuthService` class. However, if you are using the `registerContentFragmentSelectorAuthService` function, you do not need to call these functions directly.

| Function Name | Description |
|--- |--- |
| `isSignedInUser` | Determines whether the user is currently signed in to the service and returns a boolean value accordingly. |
| `getImsToken` | Retrieves the authentication `imsToken` for the currently signed-in user, which can be used to authenticate requests to other services such as generating asset rendition. |
| `signIn` | Initiates the sign-in process for the user. This function uses the `ImsAuthProps` to show authentication in either a pop-up or a full page reload. |
| `signOut` | Signs the user out of the service, invalidating their authentication token and requiring them to sign in again to access protected resources. Invoking this function will reload the current page. |
| `refreshToken` | Refreshes the authentication token for the currently signed-in user, preventing it from expiring and ensuring uninterrupted access to protected resources. Returns a new authentication token that can be used for subsequent requests. |
