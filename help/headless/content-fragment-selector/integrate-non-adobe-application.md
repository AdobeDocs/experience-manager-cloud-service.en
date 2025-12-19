---
title: Integrate Content Fragment Selector with non-Adobe or third party application
description: Integrate Content Fragment selector with various Adobe, non-Adobe, and third party applications.
role: Admin, User, Developer
---
# Integration with a non-Adobe application {#integration-with-non-adobe-application}

Content Fragment Selector allows you to integrate using various non-Adobe or third party applications to enable them to work together seamlessly.

## Prerequisites {#prerequisites} 

Use the following prerequisites if you are integrating Content Fragment Selector with a non-Adobe application:

* [Communication methods](/help/assets/overview-asset-selector.md#prereqs)
* imsClientId
* imsScope
* redirectUrl
* imsOrg
* apikey

Content Fragment Selector supports authentication to the Experience Manager Assets repository using Identity Management System (IMS) properties such as `imsScope` or `imsClientID` when you are integrating it with a non-Adobe application.

## Configure Content Fragment Selector for a non-Adobe application {#configure-content-fragment-selector-for-a-non-adobe-application}

To configure Content Fragment Selector for a non-Adobe application, you must first log a support ticket for provisioning followed by the integration steps.

### Logging a support ticket {#logging-a-support-ticket}

Steps to log a support ticket via the Admin Console:

1. Add **Content Fragment Selector with AEM Assets** in the title of the ticket.

1. In the description, provide the following details:

    * Experience Manager Assets as a Cloud Service URL (Program ID and Environment ID).
    * Domain names where the non-Adobe web application is hosted.

## Integration steps {#integration-steps}

Use this example `index.html` file for authentication while integrating Content Fragment Selector with a non-Adobe application.

Access the Content Fragment Selector package using the `Script` Tag, as shown in *line 9* to *line 11* of the example `index.html` file.

*Line 14* to *line 38* of the example describes the IMS flow properties, such as `imsClientId`, `imsScope`, and `redirectURL`. The function requires that you define at least one of the `imsClientId` and `imsScope` properties. If you do not define a value for `redirectURL`, the registered redirect URL for the client ID is used.

As you do not have an `imsToken` generated, use the `registerAssetsSelectorsAuthService` and `renderAssetSelectorWithAuthFlow` functions, as shown in line 40 to line 50 of the example `index.html` file. Use the `registerAssetsSelectorsAuthService` function before `renderAssetSelectorWithAuthFlow` to register the `imsToken` with the Content Fragment Selector. Adobe recommends calling `registerAssetsSelectorsAuthService` when you instantiate the component.

Define the authentication and other Assets as a Cloud Service access-related properties in the `const props` section, as shown in *line 54* to *line 60* of the example `index.html` file.

The `PureJSSelectors` global variable, mentioned in *line 65*, is used to render the Content Fragment Selector in the web browser.

Content Fragment Selector is rendered on the `<div>` container element, as mentioned in *line 74* to *line 81*. The example uses a dialog to display the Content Fragment Selector.

```html {line-numbers="true"}
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta charset="utf-8">
    <title>Content Fragment Selectors</title>
    <link rel="stylesheet" href="index.css">
    <script id="asset-selector"
        src="https://experience.adobe.com/solutions/CQ-assets-selectors/static-assets/resources/assets-selectors.js"></script>
    <script>

        const imsProps = {
            imsClientId: "<obtained from IMS team>",
            imsScope: "openid, <other scopes>",
            redirectUrl: window.location.href,
            modalMode: true, // false to open in a full page reload flow
            onImsServiceInitialized: (service) => {
                // invoked when the ims service is initialized and is ready
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

        function load() {
            const registeredTokenService = PureJSSelectors.registerAssetsSelectorsAuthService(imsProps);
            imsInstance = registeredTokenService;
        };

        // initialize the IMS flow before attempting to render the Content Fragment selector
        load();
        

        //function that will render the Content Fragment selector
        function renderAssetSelectorWithAuthFlowFlow() {
            const otherProps = {
            // any other props supported by Content Fragment selector
            }
            const assetSelectorProps = {
                "imsOrg": "imsorg",
                ...otherProps
            }
             // container element on which you want to render the AssetSelector/DestinationSelector component
            const container = document.getElementById('content-fragment-selector');

            /// Use the PureJSSelectors in globals to render the AssetSelector/DestinationSelector component
            PureJSSelectors.renderAssetSelectorWithAuthFlow(container, assetSelectorProps, () => {
                const assetSelectorDialog = document.getElementById('asset-selector-dialog');
                assetSelectorDialog.showModal();
            });
        }
    </script>

</head>
<body class="asset-selectors">
    <div>
        <button onclick="renderAssetSelectorWithAuthFlowFlow()">Content Fragment Selector - Select Assets with Ims Flow</button>
    </div>
        <dialog id="asset-selector-dialog">
            <div id="asset-selector" style="height: calc(100vh - 80px); width: calc(100vw - 60px); margin: -20px;">
            </div>
        </dialog>
    </div>
</body>

</html>

```

## Unable to access delivery repository {#unable-to-access-delivery-repository}

If you have integrated Content Fragment Selector using Sign up Sign In workflow but still unable to access the delivery repository, ensure that browser cookies have been cleaned. 

Otherwise, you may end up seeing the `invalid_credentials All session cookies are empty` error in the console.
