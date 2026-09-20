---
title: Use Canary Deployments to Validate Code
description: Learn about canary deployments in Cloud Manager. Test new code on production infrastructure before you promote it to live traffic.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
badge: label="Beta" type="Positive" url="/help/implementing/cloud-manager/release-notes/current.md"

---
# Use canary deployments to validate code {#canary-deployments}

For AEM Cloud Service implementations, canary deployments in Cloud Manager let you validate new code on the live production infrastructure's publish tier before you route real user traffic to it. You deploy the new version alongside the current stable version and reach it through a dedicated request header. After you confirm that the new version works successfully, you can either promote it to all traffic (this happens automatically after a 12-hour window) or roll it back.

Dev and stage environments remain the primary places to test code releases; canary deployments serve as an additional opportunity to sanity check that a release functions as you expect. For example, it could be useful if AEM production integrates with an external service's production endpoint, which could not be explicitly validated in lower AEM environments.

Canary deployments are intended for internal validation, not gradual traffic shifting real user traffic from the old release to the new one — since only requests with an explicit header reach the canary instances, real user traffic never routes there automatically.

>[!IMPORTANT]
>
>Canary deployments are currently a beta feature. Behavior can change before general availability. To request access or share feedback, email [aemcs-canary-deployments-beta@adobe.com](mailto:aemcs-canary-deployments-beta@adobe.com).

## Canary deployment process {#how-canary-deployments-work}

When you run a full stack pipeline that has canary deployments enabled, Cloud Manager starts a separate set of canary instances for the new build while your stable instances continue serving your users. The process follows these steps:

1. You run a full stack deployment pipeline, stage or production, that has canary deployments enabled. 
    See [Run a pipeline](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#running-pipelines) and [Enable canary deployments](#enable-canary-deployments).
1. During the deployment step, Cloud Manager starts canary instances that run the new version of your code.
1. Your existing stable instances continue to serve live traffic.
1. You reach the new version selectively by adding a canary request header. See [Access the canary release](#access-the-canary-release).
1. During a validation window, you promote the canary release to all traffic or cancel it. See [Validate and promote or cancel](#validate-and-promote-or-cancel).

## Enable canary deployments {#enable-canary-deployments}

You enable (turn on) canary deployments on the full stack pipeline. Canary deployments are supported only for **stage** and **production** environments. Note that a pipeline configured to deploy to both stage and production runs the canary deployment only in production, as shown below.

**Canary deployment behavior by pipeline type**
Where the canary deployment runs depends on the type of pipeline.

| Pipeline type | Where it runs |
| --- | --- |
| [Stage-only pipeline](/help/implementing/cloud-manager/configuring-pipelines/stage-prod-only.md#stage-only) | The canary deployment runs in the stage environment. This allows you gain familiarity with how the canary will function when deployed on the production environment |
| Production-only pipeline | The canary deployment runs in the production environment. |
| Stage and production pipeline | The canary deployment runs only in the production environment. |


**To enable canary deployments:**

1. In Cloud Manager, [add a new pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline) or [edit an existing pipeline](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#editing-pipelines) that deploys full stack code to a stage or production environment.

    ![Editing an existing pipeline](/help/implementing/cloud-manager/assets/canary-deployment-edit.png)

1. In the **Edit Production Pipeline** dialog box, click the **Source Code** tab.

    ![Pipeline deployment options with the Canary Deployment beta checkbox selected](/help/implementing/cloud-manager/assets/canary-deployment-checkbox.png)

1. In the **Pipeline** section, under the **[!UICONTROL Production Deployment Options]** heading, click **[!UICONTROL Canary Deployment (beta)]**.
1. Click **[!UICONTROL Update]** to complete the pipeline enablement.

    During the validation window, only requests that include the canary header reach the newly deployed release. All other requests continue to reach the stable release.

## Access the canary release {#access-the-canary-release}

After Cloud Manager starts the canary instances, you reach the new version by adding an HTTP header to your requests. The stable version continues to serve requests without the header.

To send a request to the canary release, include the following header:

```
X-Aem-Canary: true
```

## Validate and promote or cancel {#validate-and-promote-or-cancel}

When the canary instances are ready, a validation window opens so that you can test the new version. Cloud Manager shows the [!UICONTROL Promote to production] and [!UICONTROL Cancel deployment] options in the **Deploy to Production** section. 

>[!IMPORTANT]
>
>If you take no action within the 12-hour validation window, Cloud Manager automatically promotes the canary release.

![Cloud Manager deployment step showing the Cancel deployment and Promote to production actions for a ready canary release.](/help/implementing/cloud-manager/assets/canary-deployments-cancel-or-promote-options.png)

### Promote the canary release {#promote-the-canary-release}

To route all live traffic to the new version, click **[!UICONTROL Promote to production]**. When you promote the canary release:

* The canary version becomes the new stable release.
* Cloud Manager routes all live traffic to the new version.
* Rollback is no longer available.

### Cancel the canary deployment {#cancel-the-canary-deployment}

If you find issues during the validation window, click **[!UICONTROL Cancel deployment]**. When you cancel the canary deployment:

* Cloud Manager stops the canary release and removes the canary instances.
* The previous stable version continues to serve traffic.
* Cancellation is available only during the validation window.

<!--
## Canary header behavior after promotion {#header-behavior-after-promotion}

After Cloud Manager promotes the canary release and removes the canary instances, requests that still include the `X-Aem-Canary: true` header return an HTTP `503` response.

>[!TIP]
>
>To make these requests succeed instead, use the fallback header `X-Aem-Canary: fallback`. With the fallback header, requests route to the stable instances when the canary instances return a `503` response.
-->

## Scope and limitations {#scope-and-limitations}

Consider the following scope and limitations when you use canary deployments:

* Canary deployments apply to the publish tier only. The author tier stays on the stable version during canary validation.
* Your changes must be backward compatible so that the canary publish instances can serve your existing content structures.
* Mutable content changes in a release apply after you promote the canary release. These changes are not available on the canary instances during validation.

## More help on this topic {#more-help}

* [Deploy your code](/help/implementing/cloud-manager/deploy-code.md)
* [Introduction to CI/CD pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md)
* [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md)
* [How rolling deployments work](/help/implementing/deploying/overview.md#how-rolling-deployments-work)
