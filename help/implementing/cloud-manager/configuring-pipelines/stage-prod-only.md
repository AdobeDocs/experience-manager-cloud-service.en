---
title: Stage-Only and Prod-Only Pipelines
description: Learn how you can split staging and production deployments using dedicated pipelines.
---

# Stage-Only and Production-Only Pipelines {#stage-prod-only}

Learn how you can split staging and production deployments using dedicated pipelines.

## Overview {#overview}

Staging and production environments are tightly coupled and by default, deployments to them are linked to a singular pipeline. That is, in a [production program,](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-production-programs.md) a deployment pipeline deploys to both the staging and production environments in that production program. Similarly, in a [sandbox program,](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md) a deployment pipeline deploys to both the staging and production environments in that sandbox program.

While this coupling is suitable in most cases, there are certain use cases where disadvantages are present:

* If you wish to deploy to stage-only, you can only do this by rejecting the **Promote to Prod** step in the pipeline. However the execution will be marked as cancelled.
* If you wish to deploy the latest code in a staging environment to production , you need to redeploy the entire pipeline including the staging deployment even though no code was changed there. 
* Since environments can not be updated during deployments, ff you want to pause and test in the staging environment for multiple days before promoting to production, the production environment can not be updated, such as updating [environment variables.](/help/implementing/cloud-manager/environment-variables.md)

Stage-only and prod-only pipelines offers solutions to these use-cases by providing dedicated deployment options.

* **Stage-Only Deployment Pipelines**: Deploy to a staging environment with the execution finishing once the deployment and tests are done.
  * A stage-only pipeline behaves identically to the coupled full stack prod pipeline but without the production deployment steps (approval, schedule, deploy).
* **Prod-Only Deployment Pipelines**: Deploy to a production environment only with the option to select an execution successfully finished and validated on Stage and deploy its artifacts on Prod.  
  * Prod-only pipelines will reuse the artifacts from the stage deployments, skipping building phase.

Neither stage-only nor prod-only pipelines will be executed while a full-stack production pipeline is running and vice versa.

These dedicated pipelines offer more flexibility, but please note the following details of operation and recommendations.

>[!NOTE]
>
>Prod-only pipelines will always use the artifacts from the stage-only pipeline, regardless of  about what may have been deployed on stage via the coupled production pipeline in the meantime.
>
>* This could lead to unwanted code rollbacks.
>* Adobe recommends to stop using the coupled production pipeline once you start using the prod-only and stage-only pipelines.
>* If you still decide to run both the coupled pipelines and stage/prod-only pipelines, keep in mind reuse of artifacts.

