---
title: Add Users and Roles - What Is Required
description: Add Users and Roles - What Is Required
---

# Add Users and Roles {#add-users-roles}


Many features in [!UICONTROL Cloud Manager] require specific permissions to operate.

[!UICONTROL Cloud Manager] currently defines four roles for users which govern the availability of specific features:

* Business Owner
* Program Manager
* Deployment Manager
* Developer

>[!CAUTION]
>
>To use [!UICONTROL Cloud Manager], you must have an Adobe ID and the Adobe Experience Manager as a Cloud Service Product Context.

## Role Definitions {#role-definitions}

>[!NOTE]
>
>The Developer persona in Admin Console is unrelated to the Developer role in [!UICONTROL Cloud Manager].

The following table summarizes the roles:

|[!UICONTROL Cloud Manager] Roles|Description|
|--- |--- |
|Business Owner|Responsible for defining KPIs, approving production deployments and overriding important 3-tier failures.|
|Program Manager|Uses [!UICONTROL Cloud Manager] to perform team setup, review status and view KPIs. Can approve important 3-tier failures.|
|Deployment Manager|Manages deployment operations. Uses [!UICONTROL Cloud Manager] to execute stage/production deployments. Can edit CI/CD Pipelines. Can approve important 3-tier failures. Can get access to the Git repository.|
|Developer|Develops and tests custom application code. Primarily uses [!UICONTROL Cloud Manager] to view status. Can get access to the Git repository for code commit.|
|Content Author|Generally does not interact with [!UICONTROL Cloud Manager]. May use [!UICONTROL Cloud Manager] Program Switcher (having navigated from [!UICONTROL Experience Cloud]) to access AEM.|

## The Integration Product Profile {#integration-product-profile}

In addition to the above, Cloud Manager will automatically create a product profile named "Integrations - Cloud Service". This product profile is used for the integrations between Adobe Experience Manager and other Adobe products. This product profile **must** not be deleted. If you do accidentally delete this profile, it will need to be manually recreated. The Display Name for this profile **must** be `CM_CS_DEFAULT`.
