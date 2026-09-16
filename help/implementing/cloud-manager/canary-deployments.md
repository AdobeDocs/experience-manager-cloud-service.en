---
title: Use Canary Deployments to Validate Code
description: Learn about canary deployments in Cloud Manager. Test new code on production infrastructure before you promote it to live traffic.
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
badge: label="Beta" type="Positive" url="/help/implementing/cloud-manager/release-notes/current.md"

---

# Use canary deployments to validate code {#canary-deployments}

Canary deployments let you validate new code on live production infrastructure before you route real user traffic to it. You deploy the new version alongside the current stable version and reach it through a dedicated request header. After you confirm that the new version works, you either promote it to all traffic or roll it back.

>[!IMPORTANT]
>
>Canary deployments are currently a beta feature. Behavior can change before general availability. To request access or share feedback, email [aemcs-canary-deployments-beta@adobe.com](mailto:aemcs-canary-deployments-beta@adobe.com).

## How canary deployments work {#how-canary-deployments-work}

When you run a pipeline that has canary deployments enabled, Cloud Manager starts a separate set of canary instances for the new build while your stable instances keep serving end users. The process follows these steps:

1. You trigger a full stack deployment pipeline that has canary deployments enabled.
1. During the deployment step, Cloud Manager starts canary instances that run the new version of your code.
1. Your existing stable instances continue to serve live traffic.
1. You reach the new version selectively by adding a canary request header. See [Access the canary release](#access-the-canary-release).
1. During a validation window, you promote the canary release to all traffic or cancel it. See [Validate and promote or cancel](#validate-and-promote-or-cancel).

<!-- TODO: Add the canary deployment workflow diagram (source: Canary Deployments Customer Support Guide PDF). -->
![Sequence diagram of the canary deployment workflow between the user and Cloud Manager across the deployment, cancel, and promotion phases. Line style distinguishes user actions, Cloud Manager steps, and canary lifecycle steps.](/help/implementing/cloud-manager/assets/canary-deployment-workflow.png)

## Enable canary deployments {#enable-canary-deployments}

You configure canary deployments on the full stack pipeline. Canary deployments are supported only for stage and production environments. 

**To enable canary deployments:**

1. In Cloud Manager, [add a pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md#adding-production-pipeline) or [edit a pipeline](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#editing-pipelines) that deploys full stack code to a stage or production environment.
1. In the **Edit Production Pipeline** dialog box, click the **Source Code** tab.
1. In the **Pipeline** section, under **[!UICONTROL Production Deployment Options]**, click **[!UICONTROL Canary Deployment (beta)]**.
1. Select **[!UICONTROL Continue]** to complete the pipeline configuration.

<!-- TODO: Add the Deployment Options screenshot with the Canary Deployment (beta) checkbox selected (source: Customer Support Guide in PDF). -->
![Pipeline deployment options with the Canary Deployment beta checkbox selected](/help/implementing/cloud-manager/assets/canary-deployment-checkbox.png)

During the validation window, only requests that include the canary header reach the newly deployed release. All other requests continue to reach the stable release.

### Canary deployment behavior by pipeline type {#behavior-by-pipeline-type}

Where the canary deployment runs depends on the type of pipeline.


| Pipeline type | Where it runs |
| --- | --- |
| Stage-only pipeline | The canary deployment runs in the stage environment. |
| Production-only pipeline | The canary deployment runs in the production environment. |
| Stage and production pipeline | The canary deployment runs only in the production environment. |

## Access the canary release {#access-the-canary-release}

After Cloud Manager starts the canary instances, you reach the new version by adding an HTTP header to your requests. Requests without the header continue to be served by the stable version.

To send a request to the canary release, include the following header:

```
X-Aem-Canary: true
```

## Validate and promote or cancel {#validate-and-promote-or-cancel}

When the canary instances are ready, a validation window opens so that you can test the new version. Cloud Manager shows the [!UICONTROL Promote to production] and [!UICONTROL Cancel deployment] actions on the deployment step. 

>[!IMPORTANT]
>
>If you take no action within the 3-hour validation window, Cloud Manager automatically promotes the canary release.

<!-- TODO: Add the deployment step screenshot showing the Promote to production and Cancel deployment actions -->

### Promote the canary release {#promote-the-canary-release}

To route all live traffic to the new version, click **[!UICONTROL Promote to production]**. When you promote the canary release:

* The canary version becomes the new stable release.
* Cloud Manager routes all live traffic to the new version.
* Rollback is no longer available.

### Cancel the canary deployment {#cancel-the-canary-deployment}

If you find issues during the validation window, click **[!UICONTROL Cancel deployment]**. When you cancel the canary deployment:

* Cloud Manager stops the canary release and removes the canary instances.
* Traffic continues to be served by the previous stable version.
* Cancellation is available only during the validation window.

## Canary header behavior after promotion {#header-behavior-after-promotion}

After Cloud Manager promotes the canary release and removes the canary instances, requests that still include the `X-Aem-Canary: true` header return an HTTP `503` response.

>[!TIP]
>
>To make these requests succeed instead, use the fallback header `X-Aem-Canary: fallback`. With the fallback header, requests route to the stable instances when the canary instances return a `503` response.

## Scope and limitations {#scope-and-limitations}

Keep the following scope and limitations in mind when you use canary deployments:

* Canary deployments apply to the publish tier only. The author tier stays on the stable version during canary validation.
* Your changes must be backward compatible so that the canary publish instances can serve your existing content structures.
* Mutable content changes in a release apply only after you promote the canary release. These changes are not available on the canary instances during validation.

## More help on this topic {#more-help}

* [Deploy your code](/help/implementing/cloud-manager/deploy-code.md)
* [Introduction to CI/CD pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md)
* [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md)
* [How rolling deployments work](/help/implementing/deploying/overview.md#how-rolling-deployments-work)