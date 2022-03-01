---
title: Deploying Your Code
description: Learn how to deploy your code using Cloud Manager pipelines in AEM as a Cloud Service.
exl-id: 2c698d38-6ddc-4203-b499-22027fe8e7c4
---

# Deploying Your Code {#deploy-your-code} 

Learn how to deploy your code using Cloud Manager pipelines in AEM as a Cloud Service.

## Deploying Your Code with Cloud Manager in AEM as a Cloud Service {#deploying-code-with-cloud-manager}

Once you have [configured your production Pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md) including repository, environment, and testing environment, you are ready to deploy your code.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. Click on the program for which you want to deploy code.

1. Click **Deploy** from the call-to-action on the **Overview** screen to start the deployment process.

   ![CTA](assets/deploy-code1.png)

1. The **Pipeline Execution** screen displays. Click **Build** to start the process.

   ![Pipeline Execution screen](assets/deploy-code2.png)

The build process deploys your code including these stages.

1. Stage Deployment
1. Stage Testing
1. Production Deployment

>[!TIP]
>
>You can review the steps from various deployment processes by viewing logs, or reviewing results, for the testing criteria.

## Stage Deployment {#stage-deployment}

The **Stage Deployment** stage. involves these steps.

* **Validation**  - This step ensures that the pipeline is configured to use the currently available resources. E.g. testing that the configured branch exists and that the environments are available.
* **Build &amp; Unit Testing** - This step runs a containerized build process.
  * Please see the document [Build Environment Details](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md) for details on the build environment.
* **Code Scanning** - This step evaluates the quality of your application code.
  * Please see the document [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md) for details on the testing process.
* **Build Images** - This process is responsible for transforming the content and dispatcher packages produced by the build step into Docker images and Kubernetes configurations.

![Stage Deployment](assets/stage-deployment.png)

## Stage Testing {#stage-testing}

The **Stage testing** stage involves these steps.

* **Product Functional Testing** - Cloud Manager pipeline executions support execution of tests that run against the stage environment.
   * Please refer to the document [Product Functional Testing](/help/implementing/cloud-manager/functional-testing.md#product-functional-testing) for more details.

* **Custom Functional Testing** - This step in the pipeline is always executed and cannot be skipped. If no test JAR is produced by the build, the test passes by default.  
   * Please refer to the document [Custom Functional Testing](/help/implementing/cloud-manager/functional-testing.md#custom-functional-testing) for more details.

* **Custom UI Testing** - This step is an optional feature that automatically run UI tests created for custom applications.
   * UI tests are Selenium-based tests packaged in a Docker image to allow a wide choice in language and frameworks (such as Java and Maven, Node and WebDriver.io, or any other framework and technology built upon Selenium).
   * Please refer to the document [Custom UI Testing](//help/implementing/cloud-manager/functional-testing.md#custom-ui-testing) for more details.

* **Experience Audit** - This step in the pipeline is always executed and cannot be skipped. As a production pipeline is executed, an experience audit step is included after custom functional testing that will run the checks.
   * The pages that are configured are submitted to the service and evaluated. 
   * The results are informational and show the scores and the change between the current and previous scores.
   * This insight is valuable to determine if there is a regression that will be introduced with the current deployment.
   * Please refer to the document [Understanding Experience Audit results](/help/implementing/cloud-manager/experience-audit-testing.md) for more details.

![Stage Testing](assets/stage-testing.png)

## Deployment Process {#deployment-process}

All Cloud Service deployments follow a rolling process to ensure zero downtime. Please refer to the document [How Rolling Deployments Work](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/overview.html#how-rolling-deployments-work) to learn more.

### Deployment to Production Phase {#deployment-production-phase}

The process for deploying to production topologies differs slightly in order to minimize impact visitors to an AEM site.

Production deployments generally follow the same steps as previously described, but in a rolling manner.

1. Deploy AEM packages to author.
1. Detach dispatcher1 from the load balancer.
1. Deploy AEM packages to publish1 and the dispatcher package to dispatcher1, flush dispatcher cache.
1. Put dispatcher1 back into the load balancer.
1. Once dispatcher1 is back in service, detach dispatcher2 from the load balancer.
1. Deploy AEM packages to publish2 and the dispatcher package to dispatcher2, flush dispatcher cache.
1. Put dispatcher2 back into the load balancer.

This process continues until the deployment has reached all publishers and dispatchers in the topology.
