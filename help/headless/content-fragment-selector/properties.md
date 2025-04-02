---
title: Micro-Frontend Content Fragment Selector Properties for Adobe Experience Manager as a Cloud Service
description: Properties to configure the Micro-Frontend Content Fragment Selector to search, find, and retrieve content fragments from your application.
role: Admin, User
exl-id: c81b5256-09fb-41ce-9581-f6d1ad316ca4
---
# Content Fragment Selector - Related Properties {#content-fragment-selector-related-properties}

The Micro-Frontend Content Fragment Selector allows you to browse or search Content Fragments in the repository, and use them in your application.

You can use the following properties to customize how the Content Fragment Selector is rendered and how it can be used:

## Content Fragment Selector Properties {#content-fragment-selector-properties}

| Property | Type | Required | Default | Description |
|--- |--- |--- |--- |--- |
| `imsToken` | string | No | | IMS token used for authentication.  |
| `repoId` | string  | No | | Repository ID used for authentication. |
| `orgId` | string | Yes | | Organization ID used for authentication. |
| `locale` | string | No | | Locale data. |
| `env` | Environment | No | | Content Fragment Selector deployment environment. |
| `filters` | FragmentFilter | No | | Filters to be applied for the list of content fragments. By default, fragments under `/content/dam` will be displayed. Default value: `{ folder: "/content/dam" }` |
| `isOpen` | boolean | Yes | `false` | Flag to trigger opening or closing the selector. |
| `onDismiss` | () => void | Yes | | Function to be called when **Dismiss** is selected. |
| `onSubmit` | ({ contentFragments: `{id: string, path: string}[]`, domainNames: `string[]` }) => void | Function to be called when **Select** is used after selecting one or more Content Fragments. <br><br>The function will receive:<br><ul><li> the selected Content Fragments with `id` and `path` fields</li><li>and domain names related to the repository's program id and environment id, which have the status `ready` and the `tier` Publish</li></ul><br>If there are no domain names it will be use the Publish instance as a fallback domain. |
| `theme` | "light" | "dark" | No | | Theme of the Content Fragment Selector. Default theme is set to the theme of the UnifiedShell environment. |
| `selectionType` | "single" | "multiple" | No | `single` | Selection type that can be used to restrict selection for the FragmentSelector. |
| `dialogSize` | "fullscreen" | "fullscreenTakeover" | No | `fullscreen`   | Optional property to control the dialog size. |
| `waitForImsToken` | boolean | No | `false` | Indicates whether the Content Fragment Selector is rendered in the context of SUSI flow, and needs to wait for the `imsToken` to be ready. |
| `imsAuthInfo` | ImsAuthInfo | No | | Object containing the IMS authentication information of the logged in user. |
| `runningInUnifiedShell` | boolean | No | | Indicates whether the Content Fragment Selector is running under UnifiedShell or standalone. |
| `readonlyFilters` | ResourceReadonlyFiltersField | No | | Readonly filters that can be applied for the list of content - and cannot be removed. |

## ImsAuthProps Properties {#imsauthprops-properties}

The `ImsAuthProps` properties define the authentication information and flow that the Content Fragment Selector uses to obtain an `imsToken`. By setting these properties, you can control how the authentication flow should behave and register listeners for various authentication events.

| Property Name | Description |
|--- |--- |
| `imsClientId` | A string value representing the IMS client ID used for authentication purposes. This value is provided by Adobe and is specific to your Adobe AEM CS organization. |
| `imsScope` | Describes the scopes used in authentication. The scopes determine the level of access that the application has to your organization resources. Multiple scopes can be separated by commas. |
| `redirectUrl` | Represents the URL where the user is redirected after authentication. This value is typically set to the current URL of the application. If a `redirectUrl` is not supplied, `ImsAuthService` will use the redirectUrl used to register the `imsClientId` |
| `modalMode` | A boolean indicating whether the authentication flow should be displayed in a modal (pop-up) or not. If set to `true`, the authentication flow is displayed in a pop-up. If set to `false`, the authentication flow is displayed in a full page reload.<br>**Note:** for better UX, you can dynamically control this value if the user has browser pop-up disabled. |
| `onImsServiceInitialized` | A callback function that is called when the Adobe IMS authentication service is initialized. This function takes one parameter, `service`, which is an object representing the Adobe IMS service. See [`ImsAuthService`](#imsauthservice-ims-auth-service) for more details. |
| `onAccessTokenReceived` | A callback function that is called when an `imsToken` is received from the Adobe IMS authentication service. This function takes one parameter, `imsToken`, which is a string representing the access token. |
| `onAccessTokenExpired` | A callback function that is called when an access token has expired. This function is typically used to trigger a new authentication flow to obtain a new access token. |
| `onErrorReceived` | A callback function that is called when an error occurs during authentication. This function takes two parameters: the error type and error message. The error type is a string representing the type of error and the error message is a string representing the error message. |

## ImsAuthService Properties {#imsauthservice-properties}

The `ImsAuthService` class handles the authentication flow for the Content Fragment Selector. It is responsible for obtaining an `imsToken` from the Adobe IMS authentication service. The `imsToken` is used to authenticate the user and authorize access to the Adobe Experience Manager (AEM) CS repository. ImsAuthService uses the `ImsAuthProps` properties to control the authentication flow and register listeners for various authentication events. You can use the convenient `registerContentFragmentSelectorAuthService` function to register the `ImsAuthService` instance with the Content Fragment Selector. The following functions are available on the `ImsAuthService` class. However, if you are using the `registerContentFragmentSelectorAuthService` function, you do not need to call these functions directly.

| Function Name | Description |
|--- |--- |
| `isSignedInUser` | Determines whether the user is currently signed in to the service and returns a boolean value accordingly. |
| `getImsToken` | Retrieves the authentication `imsToken` for the currently signed-in user, which can be used to authenticate requests to other services such as generating asset _rendition._|
| `signIn` | Initiates the sign-in process for the user. This function uses the `ImsAuthProps` to show authentication in either a pop-up or a full page reload. |
| `signOut` | Signs the user out of the service, invalidating their authentication token and requiring them to sign in again to access protected resources. Invoking this function will reload the current page. |
| `refreshToken` | Refreshes the authentication token for the currently signed-in user, preventing it from expiring and ensuring uninterrupted access to protected resources. Returns a new authentication token that can be used for subsequent requests. |
