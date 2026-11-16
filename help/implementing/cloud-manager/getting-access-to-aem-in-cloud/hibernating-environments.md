---
title: Hibernate and De-Hibernate Sandbox Environments
description: Learn how the environments of a sandbox program automatically enter a hibernation mode and how you can de-hibernate them.
exl-id: c0771078-ea68-4d0d-8d41-2d9be86408a4
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: a01bfd36-4ab8-4bf8-9dc0-5b45b890552e
    internal-label: APIs
subfeature_v2:
  - id: d9eb3b3e-9447-4ed4-bf4a-96c7b245cb27
    internal-label: Cloud Manager APIs
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Hibernate and De-Hibernate Sandbox Environments {#hibernating-introduction}

Environments of a sandbox program enter a hibernation mode if no activity is detected for eight hours. Hibernation is unique to sandbox program environments. Production program environments cannot be hibernated.

## Hibernation {#hibernation-introduction}

Hibernation can occur either automatically or manually. 

* **Automatic** - Sandbox program environments are automatically hibernated after eight hours of inactivity. Inactivity is defined as the absence of requests to the author, preview, and publish services.
* **Manual** - You can manually hibernate a sandbox program environment. There is no requirement to do so because hibernation occurs automatically as previously described.

Sandbox program environments enter hibernation mode within minutes. Data is preserved during hibernation.

### Hibernate a sandbox program environment manually {#using-manual-hibernation}

You can manually hibernate your sandbox program from the Developer Console. Access to the Developer Console for a sandbox program is available to any user of Cloud Manager.

**To hibernate a sandbox program environment manually:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, click a *sandbox program* that you want to hibernate to show its details.

1. On the **Environments** card, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) and click **Developer Console**. 

   * See [Accessing Developer Console](/help/implementing/cloud-manager/manage-environments.md#accessing-developer-console) for additional details about the Developer Console.

   ![Developer Console menu option](/help/implementing/cloud-manager/assets/developer-console-menu-option.png)

1. On the **Developer Console** page, click **Hibernate**.

<!-- UPDATE THESE SCREENSHOTS WHEN NEW AEM DEVELOPER CONSOLE UI IS RELEASED. AS OF OCTOBER 14, 2024, NEW UI IS STILL IN PRIVATE BETA -->

   ![Hibernate button](assets/hibernate-1.png)

1. Click **Hibernate** to confirm the step.

   ![Confirm hibernation](assets/hibernate-2.png)

When the hibernation is successful, you see the hibernation process completion notification for your environment in the **Developer Console** screen.

![Hibernation confirmation](assets/hibernate-4.png)

In the Developer Console, click the **Environments** link in the breadcrumbs above the **Pod** drop-down list to view environments available for hibernation.

![List of environments to hibernate](assets/hibernate-1b.png)

## De-hibernate a sandbox program from the Developer Console manually {#de-hibernation-introduction}

You can manually hibernate your sandbox program from the Developer Console. 

>[!IMPORTANT]
>
>A user with a **Developer** role can de-hibernate a sandbox program environment.

**To de-hibernate a sandbox program from the Developer Console manually:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, click the program you want to de-hibernate to show its details.

1. On the **Environments** card, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) and click **Developer Console**. 

   * See [Accessing Developer Console](/help/implementing/cloud-manager/manage-environments.md#accessing-developer-console) for additional details about the Developer Console.

1. Click **De-hibernate**.

    ![De-hibernate button](assets/de-hibernation-img1.png)
    
1. Click **De-hibernate** to confirm the step.

   ![Confirm de-hibernation](assets/de-hibernation-img2.png)

1. You receive notification that the de-hibernation process has started and are updated with the progress.
   
   ![Hibernation progress notification](assets/de-hibernation-img3.png)
   
1. Once the process completes, the sandbox program environment is active again.
 
   ![De-hibernation complete](assets/de-hibernation-img4.png)

In the Developer Console, click the **Environments** link in the breadcrumbs above the **Pod** drop-down list to access environments available for de-hibernation.
 
![List of hibernated pods](assets/de-hibernate-1b.png)

### Permissions to de-hibernate {#permissions-de-hibernate}

Any user with a product profile giving them access to AEM as a Cloud Service can access the **Developer Console**. This lets them de-hibernate the environment. 

## Access a hibernated environment {#accessing-hibernated-environment}

When a user makes a browser request to the author, preview, or publish service of a hibernated environment, they encounter a landing page. This page explains the environment's hibernated status and provides a link to the Developer Console for de-hibernation.

![Hibernated service landing page](assets/de-hibernation-img5.png)

## Deployments and AEM updates {#deployments-updates}

Hibernated environments still allow for deployments and manual AEM upgrades.

* A user uses a pipeline to deploy custom code to hibernated environments. The environment remains hibernated and the new code appears in the environment once de-hibernated.

* AEM upgrades can be applied to hibernated environments and can be manually triggered from Cloud Manager. The environment remains hibernated and the new release appears in the environment once de-hibernated.

## Hibernation and deletion {#hibernation-deletion}

* Environments in a sandbox program are automatically hibernated after eight hours of inactivity. 
  * Inactivity is defined as the absence of requests to the author, preview, and publish services.
  * Once hibernated, they can be [manually de-hibernated](#de-hibernation-introduction).
* Sandbox programs are deleted after three months of being in continuous hibernation mode, after which time they can be recreated.

>[!NOTE]
>
>Only sandbox environments are automatically deleted after three months of continuous hibernation. The sandbox program with its repository and code is retained.
