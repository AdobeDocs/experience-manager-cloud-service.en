---
title: Integrate Content Fragment Selector with non-Adobe or third party application
description: Integrate Content Fragment selector with various Adobe, non-Adobe, and third party applications.
role: Admin, User, Developer
---
# Integration with a non-Adobe application {#integration-with-non-adobe-application}

The Content Fragment Selector allows you to integrate with various non-Adobe or third party applications to enable them to work together seamlessly.

## Prerequisites {#prerequisites} 

Use the following prerequisites if you are integrating Content Fragment Selector with a non-Adobe application:

* [Prerequisites](/help/headless/content-fragment-selector/overview.md#prerequisites)
* imsClientId
* imsScope
* redirectUrl
* imsOrg
* apikey

When you are integrating it with a non-Adobe application, the Content Fragment Selector supports authentication to the Adobe Experience Manager (AEM) as a Cloud Service repository using Identity Management System (IMS) properties such as `imsScope` or `imsClientID`.

<!-- check against /help/headless/content-fragment-selector/overview.md#prerequisites
### Communication methods {#communication-methods}

You must ensure the following communication methods:

* The host application is running on HTTPS.
* You cannot run the application on `localhost`. If you want to integrate the Fragment Selector on your local machine, you need to create a custom domain for example `[https://<your_campany>.localhost.com:<port_number>]` and add this custom domain in the `redirectUrl list`.
* You can configure and add clientID into the AEM Cloud Service environment variable with the respective `imsClientId`.
* The list of IMS scopes needs to be defined in the environment configuration. 
* The URL of the application is in the IMS client's allowed list of redirect URLs.
* The IMS login flow is configured and rendered using a popup on the web browser. Therefore, popups should be enabled or allowed on the target browser.

Use the above prerequisites if you require the IMS authentication workflow of Fragment Selector. Alternatively, if you are already authenticated with the IMS workflow, you can add the IMS information instead. 
-->

## Configure Content Fragment Selector for a non-Adobe application {#configure-content-fragment-selector-for-a-non-adobe-application}

To configure the Content Fragment Selector for a non-Adobe application, you must first log a support ticket for provisioning before proceeding with the integration steps.

### Logging a support ticket {#logging-a-support-ticket}

Steps to log a support ticket via the Admin Console:

1. Add **Content Fragment Selector with AEM Fragments** in the title of the ticket.

1. In the description, provide the following details:

    * Experience Manager as a Cloud Service URL (Program ID and Environment ID).
    * Domain names where the non-Adobe web application is hosted.

## Integration steps {#integration-steps}

Use the following example `index.html` file for authentication when integrating the Content Fragment Selector with a non-Adobe application: 

* Access the Content Fragment Selector package using the `Script` tag.

* Define the IMS flow properties, such as `imsClientId`, `imsScope`, and `redirectURL`. 

  * The function requires that you define at least one of the `imsClientId` and `imsScope` properties. 
  * If you do not define a value for `redirectURL`, the registered redirect URL for the client ID is used.

* As the example does not have an `imsToken` generated, use the `registerFragmentsSelectorsAuthService` and `renderFragmentSelectorWithAuthFlow` functions. 

  * Use the `registerFragmentsSelectorsAuthService` function before `renderFragmentSelectorWithAuthFlow` to register the `imsToken` with the Content Fragment Selector. 
  * Adobe recommends calling `registerFragmentsSelectorsAuthService` when you instantiate the component.

* Define the authentication and other Fragments as a Cloud Service access-related properties in the `const props` section.
* The `PureJSSelectors` global variable, is used to render the Content Fragment Selector in the web browser.
* The Content Fragment Selector is rendered on the `<div>` container element. The example uses a dialog to display the Content Fragment Selector.

**Example `ìndex.html`**

```html {line-numbers="true"}
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta charset="utf-8">
    <title>Content Fragment Selectors</title>
    <link rel="stylesheet" href="index.css">
    <script id="fragment-selector"
        src="https://experience.adobe.com/solutions/CQ-fragments-selectors/static-fragments/resources/fragments-selectors.js"></script>
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
            const registeredTokenService = PureJSSelectors.registerFragmentsSelectorsAuthService(imsProps);
            imsInstance = registeredTokenService;
        };

        // initialize the IMS flow before attempting to render the Content Fragment selector
        load();
        

        //function that will render the Content Fragment selector
        function renderFragmentSelectorWithAuthFlowFlow() {
            const otherProps = {
            // any other props supported by Content Fragment selector
            }
            const fragmentSelectorProps = {
                "imsOrg": "imsorg",
                ...otherProps
            }
             // container element on which you want to render the FragmentSelector/DestinationSelector component
            const container = document.getElementById('content-fragment-selector');

            /// Use the PureJSSelectors in globals to render the FragmentSelector/DestinationSelector component
            PureJSSelectors.renderFragmentSelectorWithAuthFlow(container, fragmentSelectorProps, () => {
                const fragmentSelectorDialog = document.getElementById('fragment-selector-dialog');
                fragmentSelectorDialog.showModal();
            });
        }
    </script>

</head>
<body class="fragment-selectors">
    <div>
        <button onclick="renderFragmentSelectorWithAuthFlowFlow()">Content Fragment Selector - Select Fragments with Ims Flow</button>
    </div>
        <dialog id="fragment-selector-dialog">
            <div id="fragment-selector" style="height: calc(100vh - 80px); width: calc(100vw - 60px); margin: -20px;">
            </div>
        </dialog>
    </div>
</body>

</html>

```

## Unable to access delivery repository {#unable-to-access-delivery-repository}

If you have integrated Content Fragment Selector using the Sign up Sign In workflow but still unable to access the delivery repository, ensure that browser cookies have been cleaned. 

Otherwise, you may end up seeing the `invalid_credentials All session cookies are empty` error in the console.
