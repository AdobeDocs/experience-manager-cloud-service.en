---
title: Using User Mapping Tool
description: Using User Mapping Tool
---

# Using User Mapping Tool {#user-mapping-tool}

## Overview {#overview}

As part of the transition journey to AEM as a Cloud Service, you need to move users and groups from your existing AEM system to AEM as a Cloud Service. This is done by the Content Transfer Tool. 

A major change to AEM as a Cloud Service is the fully integrated use of Adobe IDs for accessing the author tier.  This requires use of the Adobe Admin Console for managing users and user groups. The user-profile information is centralized in the Adobe Identity Management System (IMS) that provides single-sign-on across all Adobe cloud applications. For more details, refer to Identity Management. Because of this change, existing users and groups need to be mapped to their IMS IDs to avoid duplicate users and groups on the Cloud Service author instance.

## Important Considerations {#important-considerations} 

There are a few exceptional cases to be considered. The following specific cases will be logged and the user or group in question will not be mapped:

1. If a user has no email address in the `profile/email` field of their jcr node.

1. If a given email is not found on the IMS system for the Organization ID used (or if the IMS ID cannot be retrieved for another reason).

1. If the user is currently disabled it is treated the same as if it were not disabled.  It will be mapped and migrated as normal, and will remain disabled on the cloud instance.

## Using the User Mapping Tool {#using-user-mapping-tool}

The User Mapping Tool uses an API that allows it to lookup IMS users by email and return their IMS IDs. This API requires the user to create a Client ID for their organization, a Client Secret, and an Access Token/Bearer Token.  

Follow these steps to set this up:

1. Navigate to [Adobe Developer Console](https://console.adobe.io) using your Adobe ID.
1. Create a new project or open an existing project
1. Add an API
1. Choose User Management API
1. Create a JWT credential
1. Generate a key pair, or Upload a public key (rsa is no good)
1. Generate an access token (or JWT token or bearer token).
1. Save all this information (Client ID, Client Secret, Technical Account ID, Technical Account Email, Organization ID, Access Token) in a safe place.