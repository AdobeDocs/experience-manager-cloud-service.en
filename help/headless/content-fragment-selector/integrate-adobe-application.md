---
title: Integrate Content Fragment Selector with an Adobe application
description: Integrate Content Fragment selector with various Adobe applications.
role: Admin, User
---
# Integrate Content Fragment Selector with Adobe application {#integrate-content-fragment-selector-with-adobe-application}

The Content Fragment Selector allows you to integrate using various Adobe applications to enable them to work together seamlessly.

## Prerequisites {#prerequisites}

Use the following prerequisites if you are integrating Content Fragment Selector with an Adobe application:

* [Communication methods](/help/headless/content-fragment-selector/overview.md#prerequisites)
* imsOrg
* imsToken
* apikey

## Integrate Content Fragment Selector with an Adobe application {#integrate-content-fragment-selector-with-an-adobe-application}

The following example demonstrates the usage of Content Fragment Selector when running an Adobe application under Unified Shell or when you already have `imsToken` generated for authentication.

Include the Content Fragment Selector package in your code using the `script` tag, as shown in _lines 6&ndash;15_ of the example below. Once the script is loaded, the `PureJSSelectors` global variable is available for use. Define the Content Fragment Selector [properties](/help/headless/content-fragment-selector/properties.md) as shown in _lines 16&ndash;23_. The `imsOrg` and `imsToken` properties are both required for authentication in Adobe application. The `handleSelection` property is used to handle the selected fragments. To render the Content Fragment Selector, call the `renderFragmentSelector` function as mentioned in _line 17_. The Content Fragment Selector is displayed in the `<div>` container element, as shown in _lines 21 and 22_.

By following these steps, you can use Content Fragment Selector with your Adobe application.

```html {line-numbers="true"}
<!DOCTYPE html>
<html>
<head>
    <title>Fragment Selector</title>
    <script src="https://experience.adobe.com/solutions/CQ-fragmentss-selectors/static-fragments/resources/fragments-selectors.js"></script>
    <script>
        // get the container element in which we want to render the FragmentSelector component
        const container = document.getElementById('fragment-selector-container');
        // imsOrg and imsToken are required for authentication in Adobe application
        const fragmentSelectorProps = {
            imsOrg: 'example-ims@AdobeOrg',
            imsToken: "example-imsToken",
            apiKey: "example-apiKey-associated-with-imsOrg",
            handleSelection: (fragmentss: SelectedFragmentType[]) => {},
        };
        // Call the `renderFragmentSelector` available in PureJSSelectors globals to render FragmenttSelector
        PureJSSelectors.renderFragmentSelector(container, fragmentSelectorProps);
    </script>
</head>

<body>
    <div id="fragment-selector-container" style="height: calc(100vh - 80px); width: calc(100vw - 60px); margin: -20px;">
    </div>
</body>

</html>
```

<!--For detailed example, visit [Fragment Selector Code Example](https://github.com/adobe/aem-fragments-selectors-mfe-examples).-->

### ImsAuthProps {#imsauthprops}

The `ImsAuthProps` properties define the authentication information and flow that the Content Fragment Selector uses to obtain an `imsToken`. By setting these properties, you can control how the authentication flow should behave and register listeners for various authentication events.

| Property Name | Description|
|---|---|
| `imsClientId`| A string value representing the IMS client ID used for authentication purposes. This value is provided by Adobe and is specific to your Adobe AEM CS organization.|
| `imsScope`| Describes the scopes used in authentication. The scopes determine the level of access that the application has to your organization resources. Multiple scopes can be separated by commas.|
| `redirectUrl` | Represents the URL where the user is redirected after authentication. This value is typically set to the current URL of the application. If a `redirectUrl` is not supplied, `ImsAuthService` uses the redirectUrl used to register the `imsClientId`|
| `modalMode`| A boolean indicating whether the authentication flow should be displayed in a modal (pop-up) or not. If set to `true`, the authentication flow is displayed in a pop-up. If set to `false`, the authentication flow is displayed in a full page reload. _Note:_ for better UX, you can dynamically control this value if the user has browser pop-up disabled. |
| `onImsServiceInitialized`| A callback function that is called when the Adobe IMS authentication service is initialized. This function takes one parameter, `service`, which is an object representing the Adobe IMS service. See [`ImsAuthService`](#imsauthservice-ims-auth-service) for more details.|
| `onAccessTokenReceived`| A callback function that is called when an `imsToken` is received from the Adobe IMS authentication service. This function takes one parameter, `imsToken`, which is a string representing the access token. |
| `onAccessTokenExpired`| A callback function that is called when an access token has expired. This function is typically used to trigger a new authentication flow to obtain a new access token. |
| `onErrorReceived`| A callback function that is called when an error occurs during authentication. This function takes two parameters: the error type and error message. The error type is a string representing the type of error and the error message is a string representing the error message. |

### ImsAuthService {#imsauthservice}

`ImsAuthService` class handles the authentication flow for the Fragment Selector. It is responsible for obtaining an `imsToken` from the Adobe IMS authentication service. The `imsToken` is used to authenticate the user and authorize access to the Adobe Experience Manager as a Cloud Service repository. ImsAuthService uses the `ImsAuthProps` properties to control the authentication flow and register listeners for various authentication events. You can use the convenient [`registerFragmentsSelectorsAuthService`](#purejsselectorsregisterfragmentsselectorsauthservice) function to register the _ImsAuthService_ instance with the Fragment Selector. The following functions are available on the `ImsAuthService` class. However, if you are using the _registerFragmentsSelectorsAuthService_ function, you do not need to call these functions directly.

| Function Name | Description |
|---|---|
| `isSignedInUser` | Determines whether the user is currently signed in to the service and returns a boolean value accordingly.|
| `getImsToken`    | Retrieves the authentication `imsToken` for the currently signed-in user, which can be used to authenticate requests to other services.|
| `signIn`| Initiates the sign-in process for the user. This function uses the `ImsAuthProps` to show authentication in either a pop-up or a full page reload |
| `signOut`| Signs the user out of the service, invalidating their authentication token and requiring them to sign in again to access protected resources. Invoking this function will reload the current page.|
| `refreshToken`| Refreshes the authentication token for the currently signed-in user, preventing it from expiring and ensuring uninterrupted access to protected resources. Returns a new authentication token that can be used for subsequent requests. |

### Validation with provided IMS token {#validation-with-provided-ims-token}

```
<script>
    const apiToken="<valid IMS token>";
    function handleSelection(selection) {
    console.log("Selected fragment: ", selection);
    };
    function renderFragmentSelectorInline() {
    console.log("initializing Fragment Selector");
    const props = {
    "repositoryId": "delivery-p64502-e544757.adobeaemcloud.com",
    "apiKey": "ngdm_test_client",
    "imsOrg": "<IMS org>",
    "imsToken": apiToken,
    handleSelection,
    hideTreeNav: true
    }
    const container = document.getElementById('fragment-selector-container');
    PureJSSelectors.renderFragmentSelector(container, props);
    }
    $(document).ready(function() {
    renderFragmentSelectorInline();
    });
</script>
```

### Register callbacks to IMS service {#register-callbacks-to-ims-service}

```
// object `imsProps` to be defined as below 
let imsProps = {
    imsClientId: <IMS Client Id>,
        imsScope: "openid",
        redirectUrl: window.location.href,
        modalMode: true,
        adobeImsOptions: {
            modalSettings: {
            allowOrigin: window.location.origin,
},
        useLocalStorage: true,
},
onImsServiceInitialized: (service) => {
            console.log("onImsServiceInitialized", service);
},
onAccessTokenReceived: (token) => {
            console.log("onAccessTokenReceived", token);
},
onAccessTokenExpired: () => {
            console.log("onAccessTokenError");
// re-trigger sign-in flow
},
onErrorReceived: (type, msg) => {
            console.log("onErrorReceived", type, msg);
},
}
```
