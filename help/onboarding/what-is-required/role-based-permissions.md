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
|Add Program|Add a New Program.|x||||
|Create Environment|Create Prod+Stage, Dev, Playground Environments.|x|x|||
|Update Environment|Update Prod+Stage, Dev, Playground Environments.|x|x|||
|Delete Environment|Delete Non-prod, Dev, Playground Environments.|x|x|||
|Delete Environment|Delete Prod+Stage Environment.|||||
|Program Setup|Configure Program (including KPIs).|x||||
|Program Setup|Git Commit Access.||x||x|
|Pipeline Setup|Setup or Edit Pipeline.||x|||
|Pipeline Execution|Start the Pipeline.|x|x|||
|Pipeline Execution|Reject/Approve Important 3-Tier Failures.|x|x|x||
|Pipeline Execution|Provide GoLive Approval.|x|x|x||
|Pipeline Execution|Schedule Production Deployment.|x|x|x||
|Pipeline Execution|Resume Production Pipeline.|||||
|Manage Environment|Add Publish-Dispatcher segment from the Manage Environment Screen.|x|x||||
|Push Update|Start Push Update Pipeline.|||||
|Generate Personal Access Token|Generate Personal Access Token.||x||x|

