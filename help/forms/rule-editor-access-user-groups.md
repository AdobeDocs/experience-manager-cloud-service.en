---
title: How to provide access to aem adaptive forms rule editor to select user groups?
description: There are different types of users with varied skills that work with Adaptive Forms. Learn how to limit rule editor access to users based on their role or function.
feature: Adaptive Forms
role: User
level: Beginner, Intermediate
hide: yes
hidefromtoc: yes
exl-id: 2ef0e685-458b-4117-b02a-55dd3472577e
---
# Grant rule editor access to select user groups {#grant-rule-editor-access-to-select-user-groups}

## Overview {#overview}

There are different types of users with varied skills that work with Adaptive Forms. While expert users may have the right knowledge to work with scripts and complex rules, there may be basic-level users who must work only with the layout and basic properties of Adaptive Forms.

[!DNL Experience Manager Forms] lets you limit rule editor access to users based on their role or function. In the Adaptive Forms Configuration Service settings, you can specify the [user groups](forms-groups-privileges-tasks.md) that can view and access rule editor.

## Specify user groups that can access rule editor {#specify-user-groups-that-can-access-rule-editor}

1. Log in to [!DNL Experience Manager Forms] as an administrator.
1. In the author instance, click ![Adobe Experience Manager](assets/adobeexperiencemanager.png)Adobe Experience Manager &gt; Tools ![hammer](assets/hammer-icon.svg) &gt; **[!UICONTROL Operations]** &gt; **[!UICONTROL Web Console]**. The Web Console opens in a new window.

   ![1-2](assets/1-2.png)

1. In [!UICONTROL Web Console] Window, locate and click **[!UICONTROL Adaptive Form Configuration Service]**. **[!UICONTROL Adaptive Form Configuration Service]** dialog appears. Do not change any value and click **[!UICONTROL Save]**.

   It creates a file `/apps/system/config/com.adobe.aemds.guide.service.impl.AdaptiveFormConfigurationServiceImpl.config` in CRX-repository.

1. Log in to CRXDE as an administrator. Open file `/apps/system/config/com.adobe.aemds.guide.service.impl.AdaptiveFormConfigurationServiceImpl.config` for editing.
1. Use the following property to specify the name of a group that can access rule editor (For example, RuleEditorsUserGroup) and click **[!UICONTROL Save All]**.

   `af.ruleeditor.custom.groups=["RuleEditorsUserGroup"]`

   To enable access for multiple groups, specify a list of comma separated values:

   `af.ruleeditor.custom.groups=["RuleEditorsUserGroup", "PermittedUserGroup"]`

   ![Create User](assets/create_user_new.png)

   Now, when a user that is not a part of the specified user group (here    `RuleEditorsUserGroup`) taps a field, the Edit Rule icon ( ![edit-rules1](assets/edit-rules1.png)) is not available in the Components toolbar:

   ![componentstoolbarwithre](assets/componentstoolbarwithre.png)

   Components toolbar as visible to a user with rule editor access:

   ![componentstoolbarwithoutre](assets/componentstoolbarwithoutre.png)

   Components toolbar as visible to a user without rule editor access

   For instructions on adding users to groups, see [User Administration and Security](https://experienceleague.adobe.com/docs/experience-manager-65/administering/security/security.html).
