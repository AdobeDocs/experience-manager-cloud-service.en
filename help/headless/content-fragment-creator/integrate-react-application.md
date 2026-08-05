---
title: Integrate Content Fragment Create using React
description: Integrate Content Fragment Creator with React applications.
role: Admin, User, Developer
---
# Integrate Content Fragment Creator using React {#integrate-content-fragment-creator-using-react}

You can integrate a React application with Adobe Experience Manager (AEM) as a Cloud repository and select Content Fragments from within that application. 

The integration is done by importing the Content Fragment Creator package and connecting to the AEM as a Cloud Service using the React library. Edit an `index.html` or any appropriate file within your application to:

* Define the authentication details
* Access the AEM as a Cloud Service repository
* Configure the Content Fragment Creator display properties

You can perform authentication without defining some of the IMS properties, if you:

* are integrating an Adobe application on [Unified Shell](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/overview/aem-cloud-service-on-unified-shell)
* already have an IMS token generated for authentication

## Example - React {#example-react}

`CreateContentFragmentDialog` does not include a built-in sign-in flow — it expects a valid imsToken to already be available. For example, from an `ImsAuthService` you registered separately, or from your host application's own auth.

```javascript
import {
    CreateContentFragmentDialog,
    type CreateContentFragmentDialogProps,
} from '@aem-sites/content-fragment-creator';

const MyComponent = () => {
    const [open, setOpen] = React.useState(false);
    const repoId = 'author-pXXXXX-eYYYYY.adobeaemcloud.com';
    // Obtain this from your own auth flow (e.g. an ImsAuthService instance) —
    // CreateContentFragmentDialog does not fetch a token for you.
    const imsToken = getImsTokenFromYourAuthFlow();

    const onCreate = (contentFragment) => {
        console.log('Created content fragment:', contentFragment);
        // Handle the created content fragment (e.g., update state, show a message, etc.)
    };

    return (
        <>
            <button onClick={() => setOpen(true)}>Create fragment</button>
            <CreateContentFragmentDialog
                open={open}
                onDismiss={() => setOpen(false)}
                repoId={repoId}
                imsToken={imsToken}
                orgId="YOUR_ORG_ID@AdobeOrg"
                locale="en-US"
                selectedFolder="/content/dam/myfolder"
                onCreate={onCreate}
            />
        </>
    );
};
```

For a complete, runnable version of this example — including obtaining the `imsToken` from an already-registered `ImsAuthService` before opening the dialog — see 

* [Creator.tsx](https://github.com/adobe/aem-content-fragment-selector-mfe-examples/blob/main/examples/react/src/Creator.tsx)
* and [ContentFragmentCreatorWrapper.tsx](https://github.com/adobe/aem-content-fragment-selector-mfe-examples/blob/main/examples/react/src/ContentFragmentCreatorWrapper.tsx) in the [React demo](https://github.com/adobe/aem-content-fragment-selector-mfe-examples/blob/main/examples/react)

The dialog is rendered via the `@assets/microfrontend` embed (iframe).

## Related Resources {#related-resources}

* For a complete list of all supported properties, their types, defaults, and descriptions, see [Content Fragment Creator - Related Properties](/help/headless/content-fragment-creator/properties.md).
