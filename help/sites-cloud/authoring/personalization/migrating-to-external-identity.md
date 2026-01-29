---
title: Migrating to External Identity and Dynamic Group Membership
description: Technical guide for migrating local users and groups to external identity model with dynamic group membership in AEM as a Cloud Service
exl-id: migration-external-identity
solution: Experience Manager Sites
feature: Authoring, Personalization
role: Developer, Admin
---
# Migrating to External Identity and Dynamic Group Membership {#migrating-to-external-identity}

## Overview {#overview}

With [Data Synchronization](user-and-group-sync-for-publish-tier.md#data-synchronization) enabled in AEM as a Cloud Service, SAML Authentication Handler can be configured to automatically migrate to external identities with dynamic group membership when it manages user and group creation. If your project uses custom code to create users or groups, be sure to update it to create external users and groups (not local).

This document provides technical guidance for:

* Understanding the external identity model
* Modifying custom code to create external users and groups
* Migrating existing local users and groups to the external identity model

## Understanding External Identity {#understanding-external-identity}

### External Users {#external-users}

External users are identified by the `rep:externalId` property, which links the user to an external identity provider. The format is:

```
userId;idpName
```

For example: `john.doe;saml-idp`

**Key Properties:**

* `rep:externalId`: Required property that marks a user as external (e.g., `john.doe;saml-idp`)
* `rep:externalPrincipalNames`: Multi-valued property containing external group principals for dynamic membership
* `rep:lastSynced`: Timestamp of last synchronization
* `rep:lastDynamicSync`: Timestamp of last dynamic group membership sync

### External Groups {#external-groups}

External groups are also identified by the `rep:externalId` property and use a principal name format:

```
groupId;idpName
```

For example: `content-authors;saml-idp`

### Dynamic Group Membership {#dynamic-group-membership}

Instead of direct user-to-group relationships stored in the repository, dynamic group membership uses the `rep:externalPrincipalNames` property on the user node. When a user has an external principal name that matches an external group's ID, they become a member of that group automatically.

**Benefits:**

* Reduced repository writes (no group membership nodes are modified when users are added/removed from groups)
* Faster synchronization across publish tier nodes
* Scalable group membership management
* Compatible with Data Synchronization requirements

## Service User Configuration {#service-user-configuration}

All operations that create or modify external users and groups must be performed using a **Service User** that is properly configured to bypass the protection on `rep:externalId` and `rep:externalPrincipalNames` properties.

### Why Service User is Required {#why-service-user-required}

By default, Oak security prevents regular sessions from modifying protected properties like:
* `rep:externalId` - Marks users/groups as external
* `rep:externalPrincipalNames` - Stores dynamic group membership principals

Only a properly configured service user can modify these properties.

### Service User Configuration and Mapping {#service-user-configuration-mapping}

Setting up a service user to manage external identities requires three coordinated configurations:

1. **Create the service user via Repoinit**
2. **Configure ExternalPrincipal protection**
3. **Map the service user to your application bundle**

#### Step 1: Create Service User (Repoinit) {#step-1-repoinit}

Create the service user with necessary permissions using a repoinit script.

**Configuration File:** `org.apache.sling.jcr.repoinit.RepositoryInitializer~group-provisioner.cfg.json`

**Location:** `ui.config/src/main/content/jcr_root/apps/yourproject/osgiconfig/config.publish/`

```json
{
  "scripts": [
    "create service user group-provisioner with path system/yourproject",
    "set ACL for group-provisioner\n  allow jcr:read,jcr:readAccessControl,jcr:modifyAccessControl,rep:userManagement,rep:write on /home/users\n  allow jcr:read,jcr:readAccessControl,jcr:modifyAccessControl,rep:userManagement,rep:write on /home/groups\nend"
  ]
}
```

**Permissions Explained:**
- `jcr:read`: Read users and groups
- `jcr:readAccessControl`: Read ACLs
- `jcr:modifyAccessControl`: Modify ACLs (needed for setting properties)
- `rep:userManagement`: Create and manage users/groups
- `rep:write`: Write properties including `rep:externalId` and `rep:externalPrincipalNames`

>[!NOTE]
>
>The service user is created under `/home/users/system/yourproject` to keep it organized with other system users.

#### Step 2: Configure ExternalPrincipal Protection {#step-2-external-principal}

Whitelist the service user to bypass protection on external identity properties.

**Configuration File:** `org.apache.jackrabbit.oak.spi.security.authentication.external.impl.principal.ExternalPrincipalConfiguration.cfg.json`

**Location:** `ui.config/src/main/content/jcr_root/apps/yourproject/osgiconfig/config.publish/`

```json
{
  "protectExternalIdentities": "Warn",
  "systemPrincipalNames": [
    "group-provisioner",
    "saml-migration-service"
  ]
}
```

**Configuration Properties:**

* `protectExternalIdentities`: Controls the level of protection for external identity properties:
  - `"Strict"`: Only system principals in the whitelist can modify external properties (recommended for production)
  - `"Warn"`: Logs warnings but allows modifications (useful for development/testing)
  - `"None"`: No protection (not recommended)

* `systemPrincipalNames`: Array of service user names allowed to modify `rep:externalId` and `rep:externalPrincipalNames`. Include all service users that need to manage external identities (e.g., `group-provisioner`, `saml-migration-service`)

>[!IMPORTANT]
>
>The service user names in `systemPrincipalNames` must exactly match the service user IDs created in the repoinit script.

#### Step 3: Service User Mapping {#step-3-service-mapping}

Map the service user to your application bundle so your code can use it.

**Configuration File:** `org.apache.sling.serviceusermapping.impl.ServiceUserMapperImpl.amended~group-provisioner.cfg.json`

**Location:** `ui.config/src/main/content/jcr_root/apps/yourproject/osgiconfig/config.publish/`

```json
{
  "user.mapping": [
    "yourproject.core:group-provisioner=[group-provisioner]"
  ]
}
```

**Mapping Format:**
- `yourproject.core`: Your bundle symbolic name (found in `pom.xml` `<Bundle-SymbolicName>`)
- `group-provisioner` (before `=`): The subservice name you'll use in code
- `[group-provisioner]` (after `=`): The actual service user ID created in repoinit

**Example with Real Bundle Name:**

```json
{
  "user.mapping": [
    "aem-wintergw2025-project.core:group-provisioner=[group-provisioner]"
  ]
}
```

### Using the Service User in Code {#using-service-user}

When opening a session to perform migration or user/group creation operations, you must use the service user:

```java
import org.apache.sling.jcr.api.SlingRepository;

@Reference
private SlingRepository repository;

// Login as the service user
Session serviceSession = repository.loginService("group-provisioner", null);

try {
    UserManager userManager = ((JackrabbitSession) serviceSession).getUserManager();
    // Perform operations...
    serviceSession.save();
} finally {
    if (serviceSession != null && serviceSession.isLive()) {
        serviceSession.logout();
    }
}
```

>[!IMPORTANT]
>
>Without proper service user configuration, attempts to set `rep:externalId` or `rep:externalPrincipalNames` will fail with permission errors. Ensure your service user is properly configured in the ExternalPrincipal configuration before attempting migration.

### Complete Configuration Example {#complete-configuration-example}

Here's a complete working example showing all three configurations together:

#### File Structure

```
ui.config/src/main/content/jcr_root/apps/yourproject/osgiconfig/
└── config.publish/
    ├── org.apache.sling.jcr.repoinit.RepositoryInitializer~group-provisioner.cfg.json
    ├── org.apache.jackrabbit.oak.spi.security.authentication.external.impl.principal.ExternalPrincipalConfiguration.cfg.json
    └── org.apache.sling.serviceusermapping.impl.ServiceUserMapperImpl.amended~group-provisioner.cfg.json
```

## Modifying Custom Code {#modifying-custom-code}

### Creating External Users {#creating-external-users}

**Before (Local User):**

```java
UserManager userManager = ((JackrabbitSession) session).getUserManager();
User user = userManager.createUser(userId, password);
```

**After (External User):**

```java
import org.apache.jackrabbit.oak.spi.security.authentication.external.ExternalIdentityRef;

UserManager userManager = ((JackrabbitSession) session).getUserManager();
ValueFactory valueFactory = session.getValueFactory();

// Create user with principal
Principal userPrincipal = new Principal() {
    @Override
    public String getName() {
        return userId;
    }
};

User user = userManager.createUser(userId, null, userPrincipal, null);

// Set rep:externalId
ExternalIdentityRef externalRef = new ExternalIdentityRef(userId, idpName);
String externalId = externalRef.getString(); // Format: userId;idpName
user.setProperty("rep:externalId", valueFactory.createValue(externalId));

// Set sync timestamps to far future (workaround for OAK-12079)
// Set to 10 years in the future to prevent premature cleanup of external group memberships
// See: https://issues.apache.org/jira/browse/OAK-12079
java.util.Calendar future = java.util.Calendar.getInstance();
future.add(java.util.Calendar.YEAR, 10);
user.setProperty("rep:lastSynced", valueFactory.createValue(future));
user.setProperty("rep:lastDynamicSync", valueFactory.createValue(future));

session.save();
```

### Creating External Groups {#creating-external-groups}

**Before (Local Group):**

```java
UserManager userManager = ((JackrabbitSession) session).getUserManager();
Group group = userManager.createGroup(groupId);
```

**After (External Group):**

```java
import org.apache.jackrabbit.oak.spi.security.authentication.external.ExternalIdentityRef;

UserManager userManager = ((JackrabbitSession) session).getUserManager();
ValueFactory valueFactory = session.getValueFactory();

// Create group with principal
Principal groupPrincipal = new Principal() {
    @Override
    public String getName() {
        return groupId;
    }
};

Group group = userManager.createGroup(groupPrincipal);

// Set rep:externalId
ExternalIdentityRef externalRef = new ExternalIdentityRef(groupId, idpName);
String externalId = externalRef.getString(); // Format: groupId;idpName
group.setProperty("rep:externalId", valueFactory.createValue(externalId));

session.save();
```

### Assigning Dynamic Group Membership {#assigning-dynamic-membership}

**Before (Direct Membership):**

```java
Group group = (Group) userManager.getAuthorizable(groupId);
User user = (User) userManager.getAuthorizable(userId);
group.addMember(user);
```

**After (Dynamic Membership):**

```java
User user = (User) userManager.getAuthorizable(userId);
ValueFactory valueFactory = session.getValueFactory();

// Get existing external principal names
Value[] existingValues = user.getProperty("rep:externalPrincipalNames");
List<String> principalNames = new ArrayList<>();

if (existingValues != null) {
    for (Value value : existingValues) {
        principalNames.add(value.getString());
    }
}

// Add new principal name (format: groupId;idpName)
String dynamicGroupPrincipal = groupId + ";" + idpName;
if (!principalNames.contains(dynamicGroupPrincipal)) {
    principalNames.add(dynamicGroupPrincipal);
    
    // Create new Value array
    Value[] newValues = new Value[principalNames.size()];
    for (int i = 0; i < principalNames.size(); i++) {
        newValues[i] = valueFactory.createValue(principalNames.get(i));
    }
    
    // Set the property
    user.setProperty("rep:externalPrincipalNames", newValues);
    
    // Update sync timestamps to far future (workaround for OAK-12079)
    // Set to 10 years in the future to prevent premature cleanup of external group memberships
    // See: https://issues.apache.org/jira/browse/OAK-12079
    java.util.Calendar future = java.util.Calendar.getInstance();
    future.add(java.util.Calendar.YEAR, 10);
    user.setProperty("rep:lastDynamicSync", valueFactory.createValue(future));
    user.setProperty("rep:lastSynced", valueFactory.createValue(future));
}

session.save();
```

## Migration Process {#migration-process}

Migrating existing local users and groups to the external identity model involves three main steps:

>[!IMPORTANT]
>
>All migration steps must be executed using a properly configured service user (e.g., `group-provisioner`) that has been granted permissions to bypass protection on `rep:externalId` and `rep:externalPrincipalNames` properties. See [Service User Configuration](#service-user-configuration) for details.

### Step 1: Create External Group Structure {#step-1-external-groups}

For each local group that needs to be migrated:

1. Create a corresponding external group with principal name: `<localGroupId>;<idpName>`
2. Set the `rep:externalId` property on the external group
3. Add the external group as a member of the original local group

**Example Servlet Endpoint:**

```java
@SlingServletPaths("/bin/migration/step1")
public class MigrationStep1Servlet extends SlingAllMethodsServlet {
    
    @Override
    protected void doPost(SlingHttpServletRequest request, 
                          SlingHttpServletResponse response) {
        String groupPath = request.getParameter("groupPath");
        String idpName = request.getParameter("idpName");
        
        // Get local group
        Authorizable localGroupAuth = userManager.getAuthorizableByPath(groupPath);
        Group localGroup = (Group) localGroupAuth;
        String localGroupId = localGroup.getID();
        
        // Create external group
        String externalGroupPrincipalName = localGroupId + ";" + idpName;
        // The function createExternalGroup performs the following steps:
        // 1. Creates a new external group with the given principal name (format: "<localGroupId>;<idpName>").
        // 2. Sets the 'rep:externalId' property on the group to mark it as an external group (value: "<localGroupId>;<idpName>").
        // 3. Sets the 'rep:principalName' property for the group if required.
        // 4. Assigns any other required group metadata, such as a title or description, if needed.
        // 5. Persists the new group node in the repository at the appropriate path under /home/groups.
        // 6. Returns the created Group object so it can be used for further operations, such as membership assignment.
        Group externalGroup = createExternalGroup(externalGroupPrincipalName, localGroupId, idpName);
        
        // Add external group to local group
        localGroup.addMember(externalGroup);
        
        session.save();
    }
}
```

**Usage:**

```bash
curl -X POST "http://localhost:4503/bin/migration/step1?groupPath=/home/groups/c/content-authors&idpName=saml-idp"
```

### Step 2: Convert Users and Assign Dynamic Membership {#step-2-users}

For each user that is a member of local groups:

1. Ensure the user has `rep:externalId` (convert to external user if needed)
2. For each group membership, add the corresponding external group principal to `rep:externalPrincipalNames`
3. Update sync timestamps

**Important:** Skip system groups like "everyone" during this process.

**Example Servlet Endpoint:**

```java
@SlingServletPaths("/bin/migration/step2")
public class MigrationStep2Servlet extends SlingAllMethodsServlet {
    
    @Override
    protected void doPost(SlingHttpServletRequest request, 
                          SlingHttpServletResponse response) {
        String userId = request.getParameter("userId");
        String idpName = request.getParameter("idpName");
        
        User user = (User) userManager.getAuthorizable(userId);
        
        // Ensure user has rep:externalId
        Value[] externalIdValues = user.getProperty("rep:externalId");
        if (externalIdValues == null || externalIdValues.length == 0) {
            ExternalIdentityRef externalRef = new ExternalIdentityRef(userId, idpName);
            user.setProperty("rep:externalId", 
                           valueFactory.createValue(externalRef.getString()));
        }
        
        // Get all group memberships
        Iterator<Group> groupIterator = user.declaredMemberOf();
        List<String> principalNames = new ArrayList<>();
        
        while (groupIterator.hasNext()) {
            Group group = groupIterator.next();
            String groupId = group.getID();
            
            // Skip system groups
            if ("everyone".equals(groupId)) {
                continue;
            }
            
            // Add dynamic group principal
            String dynamicGroupPrincipal = groupId + ";" + idpName;
            principalNames.add(dynamicGroupPrincipal);
        }
        
        // Set rep:externalPrincipalNames
        if (!principalNames.isEmpty()) {
            Value[] newValues = new Value[principalNames.size()];
            for (int i = 0; i < principalNames.size(); i++) {
                newValues[i] = valueFactory.createValue(principalNames.get(i));
            }
            user.setProperty("rep:externalPrincipalNames", newValues);
        }
        
        // Update timestamps to far future (workaround for OAK-12079)
        // Set to 10 years in the future to prevent premature cleanup of external group memberships
        // See: https://issues.apache.org/jira/browse/OAK-12079
        java.util.Calendar future = java.util.Calendar.getInstance();
        future.add(java.util.Calendar.YEAR, 10);
        user.setProperty("rep:lastDynamicSync", valueFactory.createValue(future));
        user.setProperty("rep:lastSynced", valueFactory.createValue(future));
        
        session.save();
    }
}
```

**Usage:**

```bash
curl -X POST "http://localhost:4503/bin/migration/step2?userId=john.doe&idpName=saml-idp"
```

### Step 3: Remove Direct User Memberships {#step-3-cleanup}

After users have dynamic group membership configured:

1. Remove direct user memberships from local groups
2. Keep group-to-group memberships (including the external group membership)

**Example Servlet Endpoint:**

```java
@SlingServletPaths("/bin/migration/step3")
public class MigrationStep3Servlet extends SlingAllMethodsServlet {
    
    @Override
    protected void doPost(SlingHttpServletRequest request, 
                          SlingHttpServletResponse response) {
        String groupPath = request.getParameter("groupPath");
        
        Authorizable localGroupAuth = userManager.getAuthorizableByPath(groupPath);
        Group localGroup = (Group) localGroupAuth;
        
        // Process each member
        Iterator<Authorizable> members = localGroup.getDeclaredMembers();
        
        while (members.hasNext()) {
            Authorizable member = members.next();
            
            // Remove only user members, keep group members
            if (!member.isGroup()) {
                localGroup.removeMember(member);
            }
        }
        
        session.save();
    }
}
```

**Usage:**

```bash
curl -X POST "http://localhost:4503/bin/migration/step3?groupPath=/home/groups/c/content-authors"
```

## Migration Workflow {#migration-workflow}

### Pre-Migration Checklist {#pre-migration-checklist}

- [ ] **Configure Service User**: Create and configure the service user (e.g., `group-provisioner`) with proper permissions
- [ ] **Verify ExternalPrincipal Configuration**: Ensure the service user is configured to bypass protection on `rep:externalId` and `rep:externalPrincipalNames`
- [ ] **Test Service User Permissions**: Verify the service user can set external identity properties in development
- [ ] Identify all custom code that creates users or groups
- [ ] Review and update custom code to use external identity model
- [ ] Test updated code in development environment
- [ ] Inventory all existing local users and groups to migrate
- [ ] Plan migration order (groups first, then users)
- [ ] Test migration process in lower environments

### Execution Steps {#execution-steps}

1. **Deploy Updated Code**: Deploy custom code changes to create external users/groups

2. **Migrate Groups** (for each local group):
   ```bash
   curl -X POST "http://localhost:4503/bin/migration/step1?groupPath=/home/groups/g/my-group&idpName=saml-idp"
   ```

3. **Migrate Users** (for each user):
   ```bash
   curl -X POST "http://localhost:4503/bin/migration/step2?userId=username&idpName=saml-idp"
   ```

4. **Cleanup** (for each migrated group):
   ```bash
   curl -X POST "http://localhost:4503/bin/migration/step3?groupPath=/home/groups/g/my-group"
   ```

5. **Verify**: Check user group memberships and test access permissions

6. **Enable Data Synchronization**: Contact Customer Support to enable the feature

### Post-Migration Validation {#post-migration-validation}

Verify the migration:

1. **Check User Properties**:
  
   On user nodes verify presence of:
   - `rep:externalId`: Format should be `userId;idpName`
   - `rep:externalPrincipalNames`: Array of group principals in format `groupId;idpName`
   - `rep:lastSynced`: Timestamp set to far future (approximately 10 years from migration date)
   - `rep:lastDynamicSync`: Timestamp set to far future (approximately 10 years from migration date)
   
   **Note**: The timestamps are intentionally set to a far future date as a workaround for OAK-12079. This is expected behavior.

2. **Check Group Properties**:
      
   On Group nodes verify presence of:
   - External group member with format `groupId;idpName`
   - No direct user members (only after Step 3)

3. **Test User Login**: Verify users can log in and have correct permissions

4. **Test Access Control**: Verify users can access content protected by CUGs/ACLs

## Troubleshooting {#troubleshooting}

### Common Issues {#common-issues}

**Issue: Permission errors when setting `rep:externalId` or `rep:externalPrincipalNames`**

**Error Messages:**
- `javax.jcr.AccessDeniedException: Access denied`
- `OakAccess0000: Access denied`
- `Cannot set property 'rep:externalId'`

**Solution**: The session must be opened using a properly configured service user that has been granted permissions to bypass protection on external identity properties.

**Steps to resolve:**

1. **Verify service user exists**: Ensure the service user (e.g., `group-provisioner`) is created via repoinit
2. **Check service user mapping**: Verify the servlet or service is using `repository.loginService("group-provisioner", null)`
3. **Verify ExternalPrincipal configuration**: Ensure `org.apache.jackrabbit.oak.spi.security.authentication.external.impl.principal.ExternalPrincipalConfiguration` is properly configured
4. **Check service user permissions**: The service user needs `rep:write` and `rep:userManagement` permissions on `/home/users` and `/home/groups`

See [Service User Configuration](#service-user-configuration) for complete setup instructions.

**Issue: `OakConstraint0072: Property 'rep:externalPrincipalNames' requires 'rep:externalId' to be present`**

**Solution**: Users must have `rep:externalId` set before setting `rep:externalPrincipalNames`. Ensure Step 2 converts users to external users first.

**Issue: Users lose group memberships after migration**

**Solution**: Verify that:
- External group was created with correct principal name format (`groupId;idpName`)
- External group was added as member of local group (Step 1)
- User has correct external principal names in `rep:externalPrincipalNames` (Step 2)
- Step 3 cleanup was performed only after Steps 1 and 2 were completed

**Issue: External group memberships are unexpectedly removed (OAK-12079)**

**Problem**: Due to Oak bug [OAK-12079](https://issues.apache.org/jira/browse/OAK-12079), the Oak synchronization mechanism may prematurely clean up external group memberships based on the `rep:lastSynced` and `rep:lastDynamicSync` timestamps.

**Solution**: Set `rep:lastSynced` and `rep:lastDynamicSync` timestamps to a far future date (10 years from now) instead of the current time. This prevents the synchronization cleanup process from removing the external group memberships.

**Implementation:**

```java
// Workaround for OAK-12079
// Set to 10 years in the future to prevent premature cleanup
// See: https://issues.apache.org/jira/browse/OAK-12079
java.util.Calendar future = java.util.Calendar.getInstance();
future.add(java.util.Calendar.YEAR, 10);
user.setProperty("rep:lastSynced", valueFactory.createValue(future));
user.setProperty("rep:lastDynamicSync", valueFactory.createValue(future));
```

**Why this works**: By setting the timestamps to a far future date, the Oak synchronization logic treats these users as "recently synchronized" and does not trigger the cleanup process that would remove the external principal names and group memberships.

**Note**: This is a temporary workaround until OAK-12079 is resolved in a future Oak release. All code examples in this document already include this workaround.

**Issue: System group "everyone" causes errors**

**Solution**: Always skip the "everyone" system group during user migration (Step 2). This group is automatically managed by AEM.

### Rollback Procedure {#rollback-procedure}

If migration encounters issues:

1. Stop migration process
2. Restore from backup if critical data was affected
3. Rollback the changes on the code to create external users and groups with dynamic group membership
5. Review and fix issues before reattempting migration

## Best Practices {#best-practices}

* **Test Thoroughly**: Always test migration in development and staging environments before production
* **Batch Processing**: For large user bases, process migrations in batches to avoid timeout issues
* **Monitor Performance**: Watch repository performance during migration
* **Maintain Audit Trail**: Log all migration operations for troubleshooting
* **Service User Permissions**: Ensure migration servlets use appropriate service users with required permissions. The service user must be configured in the ExternalPrincipal configuration to bypass protection on `rep:externalId` and `rep:externalPrincipalNames` properties
* **Idempotent Operations**: Design migration code to be safely re-runnable
* **Validate at Each Step**: Check results after each migration step before proceeding

## Additional Resources {#additional-resources}

* [User and Group Sync for Publish Tier](user-and-group-sync-for-publish-tier.md)
* [SAML 2.0 Authentication Handler](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/authentication/saml-2-0.html)
* [External Identity Provider](https://jackrabbit.apache.org/oak/docs/security/authentication/externalloginmodule.html)
* [Dynamic Group Membership](https://jackrabbit.apache.org/oak/docs/security/authentication/external/dynamic.html)
