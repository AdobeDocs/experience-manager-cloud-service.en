---
title: Registration, Login, and User Profile 
description: Learn about Registration, Login, and User Profile on the Publish Tier
---

# Registration, Login, and User Profile {#registration-login-and-userprofile}

## Introduction {#introduction}

Web applications often provide account management features for end users to register on a website, which persists their user profile information, allowing them to login in the future and enjoy a consistent experience. This article describes:

* Registration
* Login
* Storing user profile data
* Group membership
* Data Synchronization

>[!IMPORTANT]
>
>In order for the functionality described in this article to work, the User Data Synchronization feature must be enabled, which at this time requires a request to customer support indicating the appropriate program and environments. If not enabled, user information will be persisted for just a short period (1 to 24 hours) before disappearing.

## Registration {#registration}

When an end-user registers for an account on an AEM application, a user account is created on the AEM Publish service, as reflected on a user resource under `/home/users` in the JCR repository.

There are two approaches to implementing registration, as described below.

### AEM Managed {#aem-managed-registration}

Custom registration code can be written that takes, minimally, the end user's username and password, and creates a user record in AEM which can then be used to authenticate against during login. The following steps are typically used to construct this registration mechanism:

1. Display a custom AEM component that collects registration info
1. Upon submission, a properly provisioned service user is used to
   1. Verify that an existing user does not already exist, using one of the UserManager API's `findAuthorizables()` methods
   1. Create a user record using one of the UserManager API's `createUser()` methods
   1. Persist any profile data captured using the Authorizable interface's `setProperty()` methods
1. Optional flows, such as requiring the user to validate their email.

### External {#external-managed-registration}

In some cases, registration or user creation has previously happened in infrastructure outside of AEM. In that scenario, the user record is created in AEM during login.

## Login {#login}

Once an end-user is registered on the AEM Publish service, these users can log in to have authenticated access (using AEM authorization mechanisms) and persisted, user-specific data such as profile data.

## Implementation {#implementation}

Login can be implemented with the following two approaches:

### AEM Managed {#aem-managed-implementation}

Customers can write their own custom components. To learn more, consider becoming familiar with:

* The [Sling Authentication Framework](https://sling.apache.org/documentation/the-sling-engine/authentication/authentication-framework.html) 
* And consider [asking the AEM Community Experts session](http://bit.ly/ATACEFeb15) about login.

### Integration with an Identity Provider {#integration-with-an-idp}

Customers can integrate with an IdP (identity provider), which authenticates the user. Integration technologies include SAML and OAuth/SSO, as described below.

**SAML BASED** 

Customers can use SAML-based authentication via their preferred SAML IdP. When using an IdP with AEM, the IdP is responsible for authenticating the end user's credentials and brokering the user's authentication with AEM, creating the user record in AEM as needed, and managing the user's group membership in AEM, as described by the SAML assertion.

>[!NOTE]
>
>Only the initial authentication of the user's credentials are authenticated by the IdP, and subsequent requests to AEM are performed using an AEM login token cookie, as long as the cookie is available.

See documentation for more information about the [SAML 2.0 Authentication Handler](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/saml-2-0-authenticationhandler.html?lang=en#saml-authentication-handler).

**OAuth/SSO**

See the [Single Sign On (SSO) documentation](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/configuring/single-sign-on.html) for information about using AEM's SSO Authentication Handler Service.

The `com.adobe.granite.auth.oauth.provider` interface can be implemented with the OAuth provider of your choice.

### Sticky sessions and Encapsulated Tokens {#sticky-sessions-and-encapsulated-tokens}

AEM as a Cloud Service has cookie-based sticky sessions enabled, which ensures that an end-user is routed to the same publish node on each request. In order to increase performance, the encapsulated token feature is enabled by default so the user record in the repository does not need to be referenced on each request. If the publish node which an end-user has an affinity to is replaced, their user id record will be available on the new publish node, as described in the data synchronization section below.

## User Profile {#user-profile}

There are various approaches to persisting data, depending on the nature of that data.

### AEM Repository {#aem-repository}

User profile information can be written and read in two ways:

* Server-side use with the `com.adobe.granite.security.user` Interface UserPropertiesManager interface, which will place data under the user's node in `/home/users`. Make sure that pages that are unique per user are not cached. 
* Client-side using ContextHub, as described by [the documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/personalization/contexthub.html?lang=en#personalization).

### Third-party data stores {#third-party-data-stores}

End-user data can be sent to third-party vendors such as CRMs and retrieved via APIs upon the user's login to AEM and persisted (or refreshed) on the AEM user's profile node, and used by AEM as needed.

Real-time access to 3rd party services to retrieve profile attributes is possible, however, it is important to ensure this does not materially impact request processing in AEM.

## Permissions (Closed User Groups) {#permissions-closed-user-groups}

Publish-tier access policies, also called Closed User Groups (CUGs), are defined in the AEM author as [described here](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/cug.html?lang=en#applying-your-closed-user-group-to-content-pages). In order to restrict certain sections or pages of a website from some users, apply the CUGs as needed using the AEM author, as described here, and replicate them to the publish tier.

* If users log in by authenticating with an identity provider (IdP) using SAML, the authentication handler will identify the user's group memberships (which should match the CUGs on the publish tier), and persist the association between the user and the group through a repository record
* If login is accomplished without IdP integration, custom code can apply the same repository structure relationships.

Independent of login, custom code can also persist and manage a user's group memberships as required by an organization's unique requirements.

## Data Synchronization {#data-synchronization}

Website end users have an expectation of a consistent experience on every web page request or even when they log in using a different browser, even if unbeknownst to them, they are brought to different server nodes of the publish tier infrastructure. AEM as a Cloud Service accomplishes this by quickly synchronizing the `/home` folder hierarchy (user profile information, group membership, etc) across all the nodes of the publish tier.

Unlike other AEM solutions, user and group membership synchronization in AEM as a Cloud Service does not use a point-to-point messaging approach, instead implementing a publish-subscribe approach that does not require customer configuration.

>[!NOTE]
>
>By default, user profile and group membership synchronization are not enabled and so data will not be synchronized to or even permanently persisted on the publish tier. To enable the feature, send a request to Customer Support indicating the appropriate program and environments.

## Cache Considerations {#cache-considerations}

Authenticated HTTP requests can be difficult to cache on both the CDN and Dispatcher since they carry the possibility of user-specific state being transferred as part of the request's response. Inadvertently caching authenticated requests and serving them to other requesting browsers can result in incorrect experiences, or even leaking protected or user data.

Approaches for maintaining high cache-ability of requests while supporting user-specific responses include:

* AEM Dispatcher Permissions sensitive caching
* Sling Dynamic Include
* AEM ContextHub