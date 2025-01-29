---
title: Generating Access Tokens for Server-Side APIs
description: Learn how to facilitate communication between a third-party server and AEM as a Cloud Service by generating a secure JWT Token
exl-id: 20deaf8f-328e-4cbf-ac68-0a6dd4ebf0c9
feature: Developing
role: Admin, Architect, Developer
---
# Generating Access Tokens for Server-Side APIs {#generating-access-tokens-for-server-side-apis}

Some architectures rely on making calls to AEM as a Cloud Service from an application hosted on a server outside of AEM infrastructure. For example, a mobile application that calls a server, which then makes API requests to AEM as a Cloud Service.

The server-to-server flow is described below, along with a simplified flow for development. The AEM as a Cloud Service [Developer Console](development-guidelines.md#crxde-lite-and-developer-console) is used to generate tokens needed for the authentication process.

<!-- Alexandru: hiding this until the tutorials reflect the new UI

>[!NOTE]
>
>In addition to this documentation, you can also consult the tutorials on [Token-based authentication for AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/overview.html#authentication) and [Getting a Login Token for Integrations](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/cloud-5/cloud5-getting-login-token-integrations.html). -->

## The Server-to-server Flow {#the-server-to-server-flow}

Users with an IMS org administrator role, and who are a member of the AEM Users or AEM Administrators Product Profile on AEM Author, can generate a set of credentials from AEM as a Cloud Service. Each credential is a JSON payload that includes a certificate (the public key), a private key, and a technical account consisting of a `clientId` and `clientSecret`. Those credentials can later be retrieved by a user with the AEM as a Cloud Service Environment administrator role and should be installed on a non-AEM server and treated carefully as a secret key. This JSON format file contains all the data required to integrate with an AEM as a Cloud Service API. The data is used to create a signed JWT token, which is exchanged with the Adobe Identity Management Services (IMS) for an IMS access token. This access token can then be used as a Bearer authentication token to make requests to AEM as a Cloud Service. The certificate in the credentials expires after one year by default, but they can be refreshed when needed, see [Refresh Credentials](#refresh-credentials).

The server-to-server flow involves the following steps:

* Fetch the credentials on AEM as a Cloud Service from the Developer Console
* Install the credentials for AEM as a Cloud Service on a non-AEM server making calls to AEM
* Generate a JWT token and exchange that token for an access token using Adobe's IMS APIs
* Calling the AEM API with the access token as a Bearer Authentication token
* Set appropriate permissions for the technical account user in the AEM environment

### Fetch the AEM as a Cloud Service Credentials {#fetch-the-aem-as-a-cloud-service-credentials}

Users with access to the AEM as a Cloud Service developer console see the integrations tab in the Developer Console for a given environment. A user with the AEM as a Cloud Service Environment administrator role can create, view, or manage credentials.

Clicking **Create new technical account**, a set of credentials is created that includes client id, client secret, private key, certificate, and configuration for author and publish tiers of the environment, regardless of the pod selection.

![Creating a new Technical Account](/help/implementing/developing/introduction/assets/s2s-createtechaccount.png)

A new browser tab opens up, displaying the credentials. You can use this view to download the credentials by pressing the download icon next to the status title:

![Download Credentials](/help/implementing/developing/introduction/assets/s2s-credentialdownload.png)

After the credentials are created, they will appear under the **Technical Accounts** tab in the **Integrations** section:

![View Credentials](/help/implementing/developing/introduction/assets/s2s-viewcredentials.png)

Users can later view the credentials using the View action. In addition, as described later in the article, users can edit the credentials for the same technical account. They accomplish this editing by creating a private key or certificate, for cases when the certificate must be renewed or revoked.

Users with the AEM as a Cloud Service Environment Administrator role can later create credentials for additional technical accounts. This ability is useful when different APIs have differing access requirements. For example, read versus read-write.

>[!NOTE]
>
>Customers can create up to ten technical accounts, including those accounts that have already been deleted.

>[!IMPORTANT]
>
>An IMS org administrator (typically the same user who provisioned the environment by way of the Cloud Manager), who is also a member of the AEM Users or AEM Administrators Product Profile on AEM Author, must first access the Developer Console. Then, click **Create new technical account** for the credentials to be generated and later retrieved by a user with admin permissions to the AEM as a Cloud Service environment. If the IMS org administrator has not created the technical account yet, a message informs them that they need the IMS org Administrator role.

### Install the AEM Service Credentials on a Non-AEM Server {#install-the-aem-service-credentials-on-a-non-aem-server}

The application making calls to AEM should be able to access the credentials for AEM as a Cloud Service, treating it as a secret.

### Generate a JWT Token and Exchange It for an Access Token {#generate-a-jwt-token-and-exchange-it-for-an-access-token}

Use the credentials to create a JWT token in a call to Adobe's IMS service to retrieve an access token, which is valid for 24 hours.

The AEM CS Service Credentials may be exchanged for an access token using client libraries designed for this purpose. The client libraries are available from [Adobe's public GitHub repository](https://github.com/adobe/aemcs-api-client-lib), which contains more detailed guidance and latest information.

```
/*jshint node:true */
"use strict";

const fs = require('fs');
const exchange = require("@adobe/aemcs-api-client-lib");

const jsonfile = "aemcs-service-credentials.json";

var config = JSON.parse(fs.readFileSync(jsonfile, 'utf8'));
exchange(config).then(accessToken => {
    // output the access token in json form including when it will expire.
    console.log(JSON.stringify(accessToken,null,2));
}).catch(e => {
    console.log("Failed to exchange for access token ",e);
});
```

The same exchange can be performed in any language capable of generating a signed JWT Token with the correct format and calling the IMS Token Exchange APIs.

The access token defines when it expires, which is typically 24 hours. There is sample code in the git repository to manage an access token and refresh it before it expires.

>[!NOTE]
>If there are multiple credentials, make sure to reference the appropriate json file for the API call to AEM that is later invoked.

### Calling the AEM API {#calling-the-aem-api}

Make the appropriate server-to-server API calls to an AEM as a Cloud Service environment, including the access token in the header. So for the "Authorization" header, use the value `"Bearer <access_token>"`. For example, using `curl`:

```curlc
curl -H "Authorization: Bearer <your_ims_access_token>" https://author-p123123-e23423423.adobeaemcloud.com/content/dam.json
```

### Set the Appropriate Permissions for the Technical Account User in AEM {#set-the-appropriate-permissions-for-the-technical-account-user-in-aem}

First, a new product profile must be created in the Adobe Admin Console.

1. Go to the Adobe Admin Console at [https://adminconsole.adobe.com/](https://adminconsole.adobe.com/).
1. Press the **Manage** link under the **Products and Services** column on the left.
1. Select **AEM as a Cloud Service**.
1. Press the **New Profile** button.
   
   ![New Profile](/help/implementing/developing/introduction/assets/s2s-newproductprofile.png)

1. Name the profile and press **Save**.

   ![Save Profile](/help/implementing/developing/introduction/assets/s2s-saveprofile.png)
   
1. Select the profile that you created from the profile list.
1. Select **Add User**.

   ![Add User](/help/implementing/developing/introduction/assets/s2s-addusers.png)

1. Add the technical account that you created (in this case `84b2c3a2-d60a-40dc-84cb-e16b786c1673@techacct.adobe.com`), and click **Save**.

   ![Add Tech Account](/help/implementing/developing/introduction/assets/s2s-addtechaccount.png)

1. Wait 10 minutes for the changes to take effect and make an API call to AEM with an access token generated from the new credential. As a cURL command, it would be represented similar to this example:

   `curl -H "Authorization: Bearer <access_token>" https://author-pXXXXX-eXXXXX.adobeaemcloud.net/content/dam.json `


After making the API call, the product profile appears as a user group in the AEM as a Cloud Service author instance, with the appropriate technical account as a member of that group.

To check this information, do the following:

1. Log on to the author instance.
1. Go to **Tools** > **Security**, then click the **Groups** card.
1. Locate the name of the profile that you created in the list of groups and click it:

   ![Group Profile](/help/implementing/developing/introduction/assets/s2s-groupprofile.png)

1. In the following window, switch over to the **Members** tab and check if the technical account is correctly listed there:

   ![Members tab](/help/implementing/developing/introduction/assets/s2s-techaccountmembers.png)


Alternatively, you can also verify that the technical account appears in the user's list by performing the below steps on the author instance:

1. Go to **Tools** > **Security** > **Users**.
1. Check that your technical account is the user list and select it.
1. Click the **Groups** tab so you can verify that the user is a part of the group that corresponds to your product profile. This user is also a member of a handful of other groups, including Contributors:

   ![Group Membership](/help/implementing/developing/introduction/assets/s2s-groupmembership.png)

>[!NOTE]
>
>Before mid-2023, before it was possible to create multiple credentials, customers were not guided to create a product profile in the Adobe Admin Console. As such, the technical account was not associated with a group other than "Contributors" in the AEM as a Cloud Service instance. For the sake of consistency, it is recommended that for this technical account, you create a product profile in the Adobe Admin Console as described above, and add the existing technical account to that group.

<u>**Set the Appropriate Group Permissions**</u>

Finally, configure the group with the appropriate permissions necessary so you can invoke or lock down your APIs appropriately.

1. Log on to the appropriate author instance, and navigate to **Settings** > **Security** > **Permissions**
1. Search for the name of the group corresponding to the product profile in the left-hand pane (in this case Read-only APIs) and select it:

   ![Search for Group](/help/implementing/developing/introduction/assets/s2s-searchforgroup.png)
   
1. Click the Edit button in the following window:

   ![Edit permissions](/help/implementing/developing/introduction/assets/s2s-editpermissions.png) 

1. Modify the permissions appropriately and click **Save**

   ![Confirm editing of permissions](/help/implementing/developing/introduction/assets/s2s-confirmeditpermissions.png)

>[!INFO]
>
>Learn more about the Adobe Identity Management System (IMS) and AEM users and groups. See the [documentation](/help/security/ims-support.md).

## Developer Flow {#developer-flow}

Developers likely want to test using a development instance of their non-AEM application (either running on their laptop or hosted) that makes requests to a development AEM as a Cloud Service dev environment. However, because developers do not necessarily have IMS admin role permissions, Adobe cannot assume they can generate the JWT bearer described in the regular server-to-server flow. Therefore, Adobe provides a mechanism for a developer to generate an access token directly that can be used in requests to environments on AEM as a Cloud Service which they have access to. 

See the [Developer Guidelines documentation](/help/implementing/developing/introduction/development-guidelines.md#crxde-lite-and-developer-console) for information about the required permissions to use the AEM as a Cloud Service developer console.

>[!NOTE]
>
>The local development access token is valid for a maximum of 24 hours after which it must be regenerated using the same method.

Developers may use this token to make calls from their non-AEM test application to an AEM as a Cloud Service environment. Typically, the developer uses this token with the non-AEM application on their own laptop. Also, the AEM as a Cloud is typically a non-production environment.

The developer flow involves the following steps:

* Generate an access token from the Developer Console
* Call the AEM application with the access token.

Developers can also make API calls to an AEM project running on their local machine, in which case an access token is not needed.

### Generating the Access Token {#generating-the-access-token}

1. Go to the **Local token** under **Integrations**
1. Click **Get Local Development Token** in the Developer Console so you can generate an access token.

### Call the AEM Application with an Access Token {#call-the-aem-application-with-an-access-token}

Make the appropriate server-to-server API calls from the non-AEM application to an AEM as a Cloud Service environment, including the access token in the header. So for the "Authorization" header, use the value `"Bearer <access_token>"`.

## Refresh Credentials {#refresh-credentials}

By default, the credentials on AEM as a Cloud Service expire after one year. To ensure service continuity, developers have the option of refreshing the credentials, extending their availability for an extra year.

To achieve this refresh extension, do the following:

* Use the **Add certificate** button under **Integrations** - **Technical Accounts** in the Developer Console, as shown below

  ![Credential Refresh](/help/implementing/developing/introduction/assets/s2s-credentialrefresh.png)

* After pressing the button, a set of credentials that includes a new certificate is generated. Install the new credentials on your off-AEM server and ensure that connectivity is as expected, without removing the old credentials.
* Make sure that the new credentials are used instead of the old ones when generating the access token.
* Optionally revoke (and then delete) the prior certificate so it can no longer be used to authenticate with AEM as a Cloud Service.

## Credentials Revocation {#credentials-revocation}

If the private key is compromised, you must create credentials with a new certificate and new private key. After your application uses the new credentials so you can generate access tokens, you can revoke and delete the old certificates by doing the following:

1. First, add the new key. This key generates credentials with a new private key and a new certificate. The new private key is marked in the user interface as **current** and is, therefore, used for all new credentials for this technical account going forward. The credentials associated with the older private keys are still valid until revoked. To achieve this revocation, select the three dots (**...**) under your current technical account, then select **Add new private key**:

   ![Add new private key](/help/implementing/developing/introduction/assets/s2s-addnewprivatekey.png)

1. Select **Add** at the prompt that follows:

   ![Confirm adding of new private key](/help/implementing/developing/introduction/assets/s2s-addprivatekeyconfirm.png)

   A new browse tab with the new credentials opens and the user interface is updated to show both private keys with the new one marked as **current**:

   ![Private keys in the UI](/help/implementing/developing/introduction/assets/s2s-twokeys.png)

1. Install the new credentials on the non-AEM server and ensure connectivity works as expected. See [Server to Server Flow section](#the-server-to-server-flow) for details.
1. Revoke the old certificate by selecting the three dots (**...**) to the right of the certificate, and selecting **Revoke**:

   ![Revoke certificate](/help/implementing/developing/introduction/assets/s2s-revokecert.png)

   Then, confirm the revocation in the following prompt by pressing the **Revoke** button:

   ![Revoke certificate confirmation](/help/implementing/developing/introduction/assets/s2s-revokecertificateconfirmation.png)

1. Finally, delete the compromised certificate.
