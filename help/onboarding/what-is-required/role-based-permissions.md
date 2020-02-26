---
title: Role Based Permissions
description: Role Based Permissions
---

# Role Based Permissions {#role-based-permissions}

[!UICONTROL Cloud Manager] has pre-configured roles with appropriate permissions. For example, a developer develops code and has the permission to push the code to the **Git Repository**. Alternatively, a business owner has different permissions allowing them to define the Key Performance Indicators (KPIs) and approve deployments.

## User Permissions {#user-permissions}

Each of the roles have specific permissions, preconfigured tasks, or permissions, associated with each role. This table lists the functions available and the roles who can execute the function.

|Permission|Description|Business Owner|Deployment Manager|Program Manager|Developer|
|--- |--- |--- |--- |--- |--- |
|Add Program|Add New Program.|x|x|x|x|
|Read Application|Read Program KPIs.|x|x|x|x|
|Write Application|Program setup or edit.|x|||||
|Read Environment|See Environment details.|x|x|x|x|
|Create Execution|Start Pipeline.|x|x|x||
|Read Execution|See execution status.|x|x|x|x|
|Resume Execution|Can resume execution when paused.|x|x|x||x|
|Execution Approve Deploy to Production|Provide GoLive Approval.|x|x|x|||
|Execution Schedule Deploy to Production|Schedule Production Deployment.|x|x|x|
|Execution Cancel|Cancel current execution.|x|x|x||
|Execution Override Quality Gate Failures|Approve Important Quality Gate Failures.|x|x|x||
|Pipeline Create|Setup / Edit Pipeline.||x|||
|Pipeline Read|See Pipeline details.|x|x|x|x|
|Pipeline Write|Setup / Edit Pipeline.||x|||
|Pipeline Modify Approval|Allows editing the Business Owner option.||x|||
|Step Read|See the step quality metrics results.|x|x|x|x|
