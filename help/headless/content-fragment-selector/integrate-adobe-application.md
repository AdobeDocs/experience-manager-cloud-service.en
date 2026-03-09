---
title: Integrate Content Fragment Selector with an Adobe application
description: Integrate Content Fragment selector with various Adobe applications.
role: Admin, User, Developer
exl-id: af7837e2-e213-46a9-837c-a6965c997737
---
# Integrate Content Fragment Selector with Adobe application {#integrate-content-fragment-selector-with-adobe-application}

The Content Fragment Selector allows you to integrate with various Adobe applications to enable them to work together seamlessly.

## Prerequisites {#prerequisites}

Use the following prerequisites if you are integrating the Content Fragment Selector with an Adobe application:

* [Prerequisites](/help/headless/content-fragment-selector/overview.md#prerequisites)
* imsOrg
* imsToken
* apikey

## Integrate Content Fragment Selector with an Adobe application {#integrate-content-fragment-selector-with-an-adobe-application}

The following example demonstrates the use of the Content Fragment Selector when running an Adobe application under Unified Shell, or when you already have an `imsToken` generated for authentication.

Include the Content Fragment Selector package in your code using the `script` tag, as shown in the example below. 

* Once the script is loaded, the `PureJSContentFragmentSelectors` global variable is available for use. 
* Define the Content Fragment Selector [properties](/help/headless/content-fragment-selector/properties.md):

  * the `imsOrg` and `imsToken` properties are both required for authentication in Adobe application
  * the `handleSelection` property is used to handle the selected fragments. 

* To render the Content Fragment Selector, call the `renderFragmentSelector` function.
* The Content Fragment Selector is displayed in the `<div>` container element.

By following such steps, you can use Content Fragment Selector with your Adobe application.

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
        // Call the `renderFragmentSelector` available in PureJSContentFragmentSelectors globals to render FragmenttSelector
        PureJSContentFragmentSelectors.renderFragmentSelector(container, fragmentSelectorProps);
    </script>
</head>

<body>
    <div id="fragment-selector-container" style="height: calc(100vh - 80px); width: calc(100vw - 60px); margin: -20px;">
    </div>
</body>

</html>
```

### ImsAuthProps {#imsauthprops}

The `ImsAuthProps` properties define the authentication information and flow that the Content Fragment Selector uses to obtain an `imsToken`. By setting these properties, you can control how the authentication flow behaves and register listeners for various authentication events.

For property details see [ImsAuthProps Properties](/help/headless/content-fragment-selector/properties.md#imsauthprops-properties)

### ImsAuthService {#imsauthservice}

`ImsAuthService` class handles the authentication flow for the Fragment Selector. It is responsible for obtaining an `imsToken` from the Adobe IMS authentication service. The `imsToken` is used to authenticate the user and authorize access to the AEM as a Cloud Service repository. `ImsAuthService` uses the `ImsAuthProps` properties to control the authentication flow and register listeners for various authentication events. You can use the  `registerFragmentsSelectorsAuthService` function to register the `ImsAuthService` instance with the Fragment Selector. The following functions are available on the `ImsAuthService` class. However, if you are using the `registerFragmentsSelectorsAuthService` function, you do not need to call these functions directly.

For property details see [ImsAuthService Properties](/help/headless/content-fragment-selector/properties.md#imsauthservice-properties)

### Validation with provided IMS token {#validation-with-provided-ims-token}

```javascript
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
    PureJSContentFragmentSelectors.renderFragmentSelector(container, props);
    }
    $(document).ready(function() {
    renderFragmentSelectorInline();
    });
</script>
```

### Register callbacks to IMS service {#register-callbacks-to-ims-service}

```java
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
