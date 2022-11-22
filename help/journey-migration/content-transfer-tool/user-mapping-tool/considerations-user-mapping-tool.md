---
title: Important Considerations for User Mapping Tool
description: Important Considerations for User Mapping Tool
exl-id: 0d39a5be-93e1-4b00-ac92-c2593c02b740
---
# Important Considerations for User Mapping Tool {#important-considerations}


## Exceptional cases {#exceptional-cases}

The following specific cases will be logged: 

1. If a user has no email address in the `profile/email` field of their *jcr* node the user or group in question will be migrated but not mapped.

1. If a given email is not found on the Adobe Identity Management System (IMS) system for the Organization ID used (or if the IMS ID cannot be retrieved for another reason) the user or group in question will be migrated but not mapped. 

1. If the user is currently disabled, it is treated the same as if it were not disabled. It will be mapped and migrated as normal, and will remain disabled on the cloud instance.

1. If a user exists on the target AEM Cloud Service instance with the same user name (rep:principalName) as one of the users on the source AEM instance the user or group in question will be not be migrated.

## Additional Considerations {#additional-considerations}

* If the setting **Wipe existing content on Cloud instance before ingestion** is set, already transferred users on the Cloud Service instance will be deleted along with the entire existing repository and a new repository will be created to ingest content into. This also resets all settings including permissions on the target Cloud Service instance and is true for an admin user added to the **administrators** group. The admin user will need to be re-added to the **administrators** group to retrieve the access token for CTT.

* It is recommended to remove any existing user from the target Cloud Service AEM instance before running CTT with User Mapping. This is to prevent any conflict between migrating users from the source AEM instance to the target AEM instance. Conflicts will occur during ingestion if the same user exists on the source AEM instance and the target AEM instance. 

* When content top-ups are performed, if content is not transferred because it has not changed since the previous transfer, users and groups associated with that content will not be transferred either, even if the users and groups have changed in the meantime. This is because users and groups are migrated along with the content they are associated with.  

* If the target AEM Cloud Service instance has a user with a different user name but same email address as one of the users on the source AEM instance, and User Mapping is enabled, an error message will be written in the logs, and the source AEM user will not be transferred, as only one user with a given email address is allowed on the target system.

* If two users on the source AEM instance have the same email address, and User Mapping is enabled, an error message will be written in the logs and one of the source AEM users will not be transferred, as only one user with a given email address is allowed on the target system.

### What’s Next {#whats-next}

Once you have learned the important considerations and exceptional cases, you are now ready to use the tool. See [Using User Mapping Tool](/help/journey-migration/content-transfer-tool/user-mapping-tool/using-user-mapping-tool.md) for more details.
