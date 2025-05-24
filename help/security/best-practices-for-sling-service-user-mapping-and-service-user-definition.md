---
title: Best Practices for Sling Service User Mapping and Service User Definition
description: Learn about the best practices for sling service user mapping and service user definition
exl-id: 72f0dcbf-b4e6-4a73-8232-3574a212ac19
feature: Security
role: Admin
---
# Best Practices for Sling Service User Mapping and Service User Definition {#best-practices-for-sling-service-user-mapping-and-service-user-definition}

## Service User Mapping {#service-user-mapping}

To add a mapping from your service to the corresponding system-user(s) you need to create a factory configuration for the `ServiceUserMapper` service. To keep this modular, such configurations can be provided using the Sling "amend" mechanism (see [SLING-3578](https://issues.apache.org/jira/browse/SLING-3578) for more details). The recommended way to install such configurations with your bundle is by adding it to the Quickstart provisioning model, as described in the following example:

```
org.apache.sling.serviceusermapping.impl.ServiceUserMapperImpl.amended-my-mapping
    user.default=""
    user.mapping=[
        "com.adobe.cq.my-bundle:my-subservice\=[content-writer-service]",
        "com.adobe.cq.my-bundle:my-subservice-different-task\="[myfeature-configuration-writer-service,content-reader-service]"
    ]
```

### Mapping Format {#mapping-format}

Since AEM 6.4, the mapping format is defined as follows:

>[!NOTE]
>
>The `userName` is deprecated and should no longer be used.

```
bundleId [:subserviceName] = userName | [principalNames]   
```

`bundleId` and `subserviceName` identify the service, `userName/principalNames` identify the service user and `principalNames` is a comma separated list.

Also, note that `principalNames` is the list of service user principal names which out of the box are the same as the id.


**Best Practice**

* Subservice names for different tasks - if the services of your bundle perform different tasks it is recommended to identify `subserviceNames` to group them by tasks
* If a given service performs different operations (for example, reading asset content and updating information below a subtree of `/var`), it is recommended to reflect this by aggregating different service principals reflecting the individual operation, like aggregating the common `dam-reader-service` with your feature specific `assetreport-writer-service`
* Each service is ideally bound to a very specific and limited set of operations
* The new format with `[one,or,multiple,principalNames]` is the recommended way to define service user mappings as of AEM 6.4.

Below is a list of reasons for changing the format and why Adobe recommends you use it instead of the version mapping just for a single userID:

* The ability to reuse service users by combining customers' special needs with common tasks
* Avoid duplication of permission setup
* Better understanding of the effective permissions (and tasks) a given service is actually performing
* No need for explicit group membership of service users. This can have troublesome side effects as group permissions change
* Performance improvements and scalability

## Mapping Resolution and Service Login {#mapping-resolution-and-service-login}

### Service Mapping Resolution {#service-mapping-resolution}

The sequence of calls to resolve the service mapping described below:

1. Search for active `principalNames` mapping for the given `bundleId` and `subserviceName`
1. `principalNames` mapping for the `bundleId` and null `subserviceName`
1. `userName` mapping for the `bundleId` and `subserviceName`
1. `userName` mapping for `bundleId` and null `subserviceName`
1. Default mapping
1. Default user

### SlingRepository - Service Login {#slingrepository-servicelogin}

The sequence for obtaining a service `Session/ResourceResolver` works as follows:

1. Get principal names from `ServiceUserMapper` => pre-auth repository login as described below
1. Retrieve user id from `ServiceUserMapper`
1. Check for deprecated 1ServiceUserConfiguration` for the current user id
1. Default Sling service login with the user id (for example, a sequence of `createAdministrativeSession` and impersonate for service user id)

The new mapping with principal names results in the following simplified repository login:

* Set of principal names is treated as the effective Principal(s) to be used to populate the `Subject`
* Repository login can consequently be pre-authenticated
* No group membership resolution
 
  >[!NOTE]
  >
  >All required permissions need to declared for the service users. 'everyone' and other Group permissions will no longer be inherited.

* No additional admin-login to have the service-`Session/ResourceResolver` are created.

### Deprecated ServiceUserConfiguration {#deprecated-serviceUserConfiguration}

Please note that specifying a single user name in the mapping is equivalent to the existing `ServiceUserConfiguration.simpleSubjectPopulation`. With the new format the workaround provided by the `ServiceUserConfiguration` can directly be reflected with the service user mapping. The `ServiceUserConfiguration` has therefore been deprecated for AEM and all existing usages have be replaced.

## Service Users {#service-users}

### Reusing Existing Service Users {#reusing-existing-service-users}

It is recommended to re-use existing service users if the following conditions are met:

* Your needs match the intent of the existing service user
* Your service requires to perform a common task that is covered by an existing common service user. In this case, it is recommended to re-use the service user instead of introducing duplication
* Your service requires a specific task covered by an existing service user. If you are unsure about this, ask the feature team that owns it.

Don't re-use existing service users if:

* You would need to modify its permission in an unrelated way to make it work
* If you only need a small subset of the permission it provides and you would just re-use it because it makes your feature work not because it's a real match
* If its name indicates a total different intention that what you require. Picking it because it works can cause problems down the road as the feature team that owns a specific service may change the permissions and break your feature.

### Creating a Service User {#creating-a-service-user}

After you verified that no existing service user in AEM is applicable for your use-case and the corresponding RTC issues have been approved you can go ahead and add the new user to the default content. Ideally a member of the extended security team is involved in the RTC voting, so please make sure you also involve the appropriate stakeholders.

**Naming Convention**

The AEM security team has defined the following naming convention for service users to add consistency to new service users and to improve their readability and maintainability.

A service user name consists of 3 elements separated by a dash **'-'**:

1. The logical entity/feature that is targeted by the service operations (avoid paths elements that may change)
1. The task the services are going to perform
1. Trailing **'service'** to be able to easily spot from the id and principal name that the user is a service user

**Best Practices**

* Don't mix different entities/features. Split to individual service users and aggregrate them in the mapping if your service has different needs
* Limit yourself to one well defined task per service user. Split if you end up granting too many or unrelated permissions
* Spend time identifying the real need of your service
* Spend time finding a good, meaningful and self-explanatory service user name
* Ask for feedback and review: developers not familiar with your feature should be able to read and understand your intention. They might in the future be tasked to fix or maintain it.

At the end, the service user name should reveal:

* How it is intended to be used and if it can be re-used:

  * Very generic: `content-writer-service`. Safe to re-use in aggregation if your service(s) also need to be able to read the all content
  * Very specific: `asset-linkshare-service`. Not so safe to re-use unless your service really does link-sharing of assets too.

* What the feature set and permission setup can be expected to look like:

  * The logical entity needs to match the permission setup:

    * A `content-foo-service` should only be associated with operations on content. Granting it permissions to operate on other entities like configuration or users would be wrong
    * A specific service like `personalization-foo-service` should also come with specific permissions. If you end up with granting permissions on all content it's no longer specific. Reflect that in the name or re-use a common user in aggregation
    * A feature specific service like `msm-xyz-service` should only have msm-related permissions. Don't expand permissions to unrelated features like managing communities configuration or screens users.

  * The task needs to match the permissions:

    * A `foo-reader-service` should only be able to read regular items. Never grant write permissions
    * A `foo-writer-service` can be expected to perform write operations. However, it should not be granted permissions to read/modify access control content
    * A `foo-replicator-service` can be expected to have `crx:replicate` granted.

**Examples**

Examples for `configuration-reader-service`:

* The name indicates that it refers to configurations in general and not configuration of a particulare feature, like configuration of DM integration. A service user specifially targeted for reading configuration of such an integration would rather be named `dmconfig-reader-service` or `s7config-reader-service`

  >[!NOTE]
  >
  >No path information is included in the naming. Configurations have moved from `/etc` to `/conf`.

* The task-element indicates that services bound to that user will only perform read operations.

Examples for `userproperties-copy-service`:

* Services bound to this service user are going to operate on user/group properties like profiles or preferences
* It's specifically targeted to just copy that information in contrast to a name like `userproperties-writer-service` which would include any kind of write operations. Therefore, it would be possible that the permission setup for these copy tasks only allows adding items at one location and removing items at another location.

**Best Practices for Permissions Setup**

* Always use principal-based access control setup for service users. For more details, see examples below:

  * Allow mark service users and their permissions as immutable application content in skyline
  * No need to create paths and tree structures

* Only grant permissions, never deny
* Limit permissions

  * Only grant the minimal set of permissions needed
  * For more information, consult the [Mapping Privileges to Items](https://jackrabbit.apache.org/oak/docs/security/privilege/mappingtoitems.html) and [Mapping API Calls to Privileges](https://jackrabbit.apache.org/oak/docs/security/privilege/mappingtoprivileges.html) documentation
  * Do not grant permission for `jcr:all`. That is most likely not the minimal set.

* Reduce scope

  * Place access control policies at feature specific subtrees
  * In case of distributed items: use restrictions to limit scope (consult [the documentation](https://jackrabbit.apache.org/oak/docs/security/authorization/restriction.html) for list of built-in restrictions).

* Ensure Consistency

  * Make permissions consistent with the entity and task you used in the service user name
  * Avoid adding unrelated permissions. For example, it would be odd to have a `workflow-administration-service` and grant it permissions to perform user-management operations at `/home/users/screens` or let it read s7-config.

* Completeness

  * Make sure your service has all permissions it needs to perform the tasks it's designed to do. Your service needs to work out of the box also in customer environments.
  * Never expect/ask customers to expand the permission setup (for example, below `/apps`)

* Avoid duplication of permission setup

  * Re-use common service users
  * Aggregate them with your feature specific service users that provide the specific permission you need in addition

* Do not split permission setup across different features. The need for doing so indicates that your service user is not well defined or does too many different things
* Don't place service users in groups, because:

  * It mixes implementation details from service users with 'public' groups
  * You lack of control for permission changes (prone to regressions and privilege escalations)
  * Login and evaluation performance
  * Does not work with principal-based ac-setup

* Access to the user-home node (or any subtree contained therein), which does not have a predictable path is achieved in repo init by using home(`userId`). See the sling repo init [documentation](https://sling.apache.org/documentation/bundles/repository-initialization.html) for details.
* RTC: create a dedicated RTC issue if you alter permissions of an existing service user and make sure you get it reviewed by the security team.

**Creation with Repository Initialization**

Always use `repo-init` to define service users and their permission setup and place both in the correct section of the Quickstart feature model:

**Best Practices**

* Always use `repo-init` to create the service user 
* Always specify an intermediate path for service user creation
* All built-in service users for AEM must be located below `system/cq:services/internal`
* Additionally append to the intermediate relative path to group service users by feature: `system/cq:services/internal/<your-feature>`
* Customer defined service users must be located below `system/cq:services/<customer-intermediate-rel-path>` and never below the internal tree
* Use **with forced path** instead of **with path** if a user already existed and needs to be moved to the new location that supports principal-based authorization.

**Examples**

```
create service user my-new-feature-readcomment-service with path system/cq:services/internal/myfeature
set principal ACL for my-new-feature-readcomment-service
    allow rep:readProperties on /content/myFeature restriction(rep:itemNames,commentTitle,commentDate,commentTxt)
end
```

```
create service user my-existing-feature-addcomment-service with forced path system/cq:services/internal/myfeature
set principal ACL for my-existing-feature-addcomment-service
    allow jcr:addChildNodes,rep:addProperties on /content/myfeature restrictions(rep:glob,*/comments/*)
end
```

```
create service user myfeature-ims-service with path system/cq:services/internal/myfeature
set principal ACL for myfeature-ims-service
    allow jcr:read on home(myfeature-ims-service)
end
```

### Cleanup Service Users and Permissions {#cleanup-service-users-and-permissions}

The following repo init command can be used to clean up unused service users and their permissions:

```
# Remove the principal-based access control policy for principal my-feature-service
delete principal ACL for my-feature-service

# Remove all resource-based access control entries (ACEs) for principal my-feature-service
delete ACL for my-feature-service

# Disable the service user
disable service user my-feature-service : "My feature is no longer used"

# Remove the service user
delete service my-feature-service 
```

### Testing Service Users {#testing-service-users}

It is crucial to write server side tests for service users and their permission setup. This not only verifies that your setup really works but also helps you spot regressions and unintended mistakes when changing access control content or service users.

The `com.adobe.granite.testing.clients` library provides a lot of utilities that makes writing SSTs for service users easy.
