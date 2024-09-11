---
title: Important Considerations for User Mapping Tool (Legacy)
description: Important Considerations for User Mapping Tool (Legacy)
exl-id: 0d39a5be-93e1-4b00-ac92-c2593c02b740
hide: yes
hidefromtoc: yes
feature: Migration
role: Admin
---
# Important Considerations for User Mapping Tool (Legacy) {#important-considerations}

>[!INFO]
>
>This documentation refers to a deprecated version of the tool. For more information on the latest version, see [Group Migration](/help/journey-migration/content-transfer-tool/using-content-transfer-tool/group-migration.md).

## Exceptional cases {#exceptional-cases}

The following specific cases are logged: 

1. If a user has no email address in the `profile/email` field of their *jcr* node, the user or group in question is migrated but not mapped. This rule is the case even if the email address is used as a user name for logging in.

1. If an email is not found on the Adobe Identity Management System (IMS) system for the Organization ID used (or, if the IMS ID cannot be retrieved), the user, or group is migrated, but not mapped. 

1. If the user is disabled, it is treated the same as if it were not disabled. It is mapped and migrated as normal, and remain disabled on the cloud instance.

1. If a user exists on the target AEM Cloud Service instance with the same user name (rep:principalName) as one of the users on the source AEM instance, the user or group is not migrated.

1. If a user is migrated without first being mapped by way of User Mapping, on the target cloud system they are not able to log on using their IMS ID. They might be able to log on using the traditional AEM method, but this workflow is not normally what is wanted or expected.

## Additional Considerations {#additional-considerations}

* If the setting **Wipe existing content on Cloud instance before ingestion** is set, already transferred users on the Cloud Service instance are deleted. The entire existing repository is also deleted and a new repository is created into which content is ingested. This action also resets all settings including permissions on the target Cloud Service instance and is true for an admin user added to the **administrators** group. The admin user must be readded to the **administrators** group to retrieve the access token for CTT.

* Adobe recommends that you remove any existing user from the target Cloud Service AEM instance before running CTT with User Mapping. This action is necessary to prevent any conflict between migrating users from the source AEM instance to the target AEM instance. Conflicts can occur during ingestion if the same user exists on the source AEM instance and the target AEM instance. 

* When content top-ups are performed, if content is not transferred because it has not changed since the previous transfer, users and groups associated with that content are not transferred either. This rule is true even if the users and groups have changed in the meantime. The reason is because users and groups are migrated along with the content they are associated with.  

* If the AEM Cloud Service has a user with a different user name but same email address as a user on the source AEM instance, and User Mapping is enabled, an error message is logged. Also, the source AEM user is not transferred, as only one user with a given email address is allowed on the target system.

* If two users on the source AEM instance have the same email address, and User Mapping is enabled, an error message is logged. Also, one of the source AEM users is transferred because only one user with a given email address is allowed on the target system.

### What's Next {#whats-next}

Once you have learned the important considerations and exceptional cases, you are now ready to use the tool. See [Using User Mapping Tool](/help/journey-migration/content-transfer-tool/user-mapping-tool-legacy/using-user-mapping-tool-legacy.md) for more details.
