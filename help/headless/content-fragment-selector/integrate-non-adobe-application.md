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
* The `PureJSContentFragmentSelectors` global variable, is used to render the Content Fragment Selector in the web browser.
* The Content Fragment Selector is rendered on the `<div>` container element. The example uses a dialog to display the Content Fragment Selector.

**Example `ìndex.html`**

```html {line-numbers="true"}

<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <link rel="icon" type="image/svg+xml" href="/vite.svg" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>testing-cf-mfe-integration-with-3rd-party-app</title>
        <script
            id="content-fragments-selector"
            src="https://experience.adobe.com/solutions/CQ-sites-content-fragment-selector/static-assets/resources/content-fragment-selector.js"
        ></script>
        <script>
            const imsProps = {
                imsClientId: '<IMS_CLIENT_ID>',
                imsScope:
                    'additional_info.projectedProductContext, AdobeID, openid, read_organizations',
                redirectUrl: window.location.href,
                onImsServiceInitialized: (service) => {
                    // invoked when the ims service is initialized and is ready
                    console.log('onImsServiceInitialized', service);
                },
                onAccessTokenReceived: (token) => {
                    console.log('onAccessTokenReceived', token);
                },
                onAccessTokenExpired: () => {
                    console.log('onAccessTokenError');
                    // re-trigger sign-in flow
                },
                onErrorReceived: (type, msg) => {
                    console.log('onErrorReceived', type, msg);
                },
            };

            function load() {
                const registeredTokenService =
                    PureJSContentFragmentSelectors.registerContentFragmentSelectorAuthService(
                        imsProps
                    );
                imsInstance = registeredTokenService;
            }

            // initialize the IMS flow before attempting to render the content fragment selector
            load();

            // function that will render the content fragment selector
            function renderContentFragmentSelectorWithAuthFlow() {
                const contentFragmentSelectorDialog = document.getElementById(
                    'content-fragment-selector-dialog'
                );

                const contentFragmentSelectorProps = {
                    inventoryViewToggleEnabled: true,
                    isOpen: true,
                    noWrap: false,
                    orgId: 'YOUR_ORG_ID@AdobeOrg',
                    // repoId: "author-p12345-e67890.adobeaemcloud.com", // if wanted to restrict to a specific repo
                    runningInUnifiedShell: false,
                    onDismiss: () => contentFragmentSelectorDialog.close(),
                    onSubmit: ({ contentFragments }) => {
                        const selectedContentFragment = contentFragments[0];
                        alert(selectedContentFragment.path);
                    },
                };
                // container element on which you want to render the ContentFragmentSelector component
                const container = document.getElementById('content-fragment-selector');

                /// Use the PureJSContentFragmentSelectors in globals to render the ContentFragmentSelector component
                PureJSContentFragmentSelectors.renderContentFragmentSelectorWithAuthFlow(
                    container,
                    contentFragmentSelectorProps,
                    () => contentFragmentSelectorDialog.showModal()
                );
            }
        </script>
    </head>
    <body>
        <div>
            <button onclick="renderContentFragmentSelectorWithAuthFlow()">
                Content Fragment Selector - Select Content Fragments with Ims Flow
            </button>
        </div>
        <dialog id="content-fragment-selector-dialog">
            <div
                id="content-fragment-selector"
                style="height: calc(100vh - 80px); width: calc(100vw - 60px); margin: -20px"
            ></div>
        </dialog>
    </body>
</html>

```

## Unable to access delivery repository {#unable-to-access-delivery-repository}

If you have integrated Content Fragment Selector using the Sign up Sign In workflow but still unable to access the delivery repository, ensure that browser cookies have been cleaned. 

Otherwise, you may end up seeing the `invalid_credentials All session cookies are empty` error in the console.
