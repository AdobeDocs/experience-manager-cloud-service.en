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
|Create Tenant|Create a New Tenant.|||||
|Update Tenant|Update Tenant.|||||
|Add Program|Add a New Program.|x||||
|Create Environment|Create Prod+Stage, Dev, Playground Environments.|x|x|||
|Configure Environment Variables|Configure Environment Variables and Secrets.||x||x|
|Add or Remove Custom Domain Name, Upload or Update SSL Cert|Add / Remove Custom Domain Name, Upload / Update SSL Cert.|x|x|||
|Update Environment|Update Prod+Stage, Dev, Playground Environments.|x|x|||
|Delete Environment|Delete Non-prod, Dev, Playground Environments.|x|x|||
|Delete Environment|Delete Prod+Stage Environment.|||||
|Hibernate Environment|Hibernate Non-prod, Dev, Playground Environments.|x|x|||
|Program Setup|Configure Program (including KPIs).|x||||
|Program Setup|Configure Scaling Policies (General: configuring max number of tiers and On-demand horizontal scale-out: Opt-in).|x||||
|Program Setup|Git Commit Access.||x||x|
|Pipeline Setup|Setup or Edit Pipeline.||x|||
|Pipeline Execution|Start the Pipeline.|x|x|||
|Pipeline Execution|Reject/Approve Important 3-Tier Failures.|x|x|x||
|Pipeline Execution|Provide GoLive Approval.|x|x|x||
|Pipeline Execution|Schedule Production Deployment.|x|x|x||
|Pipeline Execution|Resume Production Pipeline.|||||
|Opt-in (or out of) to Provisioning|Opt-in to On-demand Horizontal provisioning from Program Setup Screen. Configure the max 'allowed' P-D segments that can be horizontally scaled-out on PROD and non-PROD environments.|x||||
|Manage Environment|Add Publish-Dispatcher segment from the Manage Environment Screen.|x|x||||
|Product Update|AEM Update Card is visible and takes user to Update Wizard.|x|x|x|x|
|Product Update|Product Update Wizard can be actioned on.|x|x|||
|Push Update|Start Push Update Pipeline.|||||
|Generate Personal Access Token|Generate Personal Access Token.||x||x|

