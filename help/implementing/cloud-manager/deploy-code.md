---
title: Deploy your Code - Cloud Services
description: Deploy your Code - Cloud Services
exl-id: 2c698d38-6ddc-4203-b499-22027fe8e7c4
---
# Deploying your Code {#deploy-your-code} 

## Deploying Code with Cloud Manager in AEM as a Cloud Service {#deploying-code-with-cloud-manager}

Once you have configured your Production Pipeline (repository, environment, and testing environment), you are ready to deploy your code.

1. Click **Deploy** from the Cloud Manager to start the deployment process.

   ![](assets/deploy-code1.png)


1. The **Pipeline Execution** screen displays.

   Click **Build** to start the process.

   ![](assets/deploy-code2.png)

1. The complete build process deploys your code.

   The following stages are involved in the build process:

    1. Stage Deployment
    1. Stage Testing
    1. Production Deployment

   >[!NOTE]
   >
   >Additionally, you can review the steps from various deployment processes by viewing logs, or reviewing results, for the testing criteria.

   The **Stage Deployment**, involves the following steps:

    * Validation: This step ensures that the pipeline is configured to use the currently available resources, for example, that the configured branch exists, the environments are available.
    * Build & Unit Testing: This step runs a containerized build process. See [Build Environment Details](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/build-environment-details.md) for details on the build environment.
    * Code Scanning: This step evaluates the quality of your application code. See [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md) for details on the testing process.
    * Build Images: This step has a log file from the process used to build images. This process is responsible for transforming the content and dispatcher packages produced by the build step into Docker images and Kubernetes configuration.
    * Deploy to Stage

       ![](assets/stage-deployment.png)

   The **Stage testing**, involves the following steps:

    * **Product Functional Testing**: Cloud Manager pipeline executions will support execution of tests that run against the stage environment. 
       Refer to [Product Functional Testing](/help/implementing/cloud-manager/functional-testing.md#product-functional-testing) for more details.

   * **Custom Functional Testing**: This step in the pipeline is always present and cannot be skipped. However, if no test JAR is produced by the build, the test passes by default.  
      Refer to [Custom Functional Testing](/help/implementing/cloud-manager/functional-testing.md#custom-functional-testing) for more details.

   * **Custom UI Testing**: This step is an optional feature that enables our customers to create and automatically run UI tests for their applications. UI tests are Selenium-based tests packaged in a Docker image in order to allow a wide choice in language and frameworks (such as Java and Maven, Node and WebDriver.io, or any other framework and technology built upon Selenium).
      Refer to [Custom UI Testing](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/using-cloud-manager/test-results/functional-testing.html?lang=en#custom-ui-testing) for more details.


   * **Experience Audit**: This step in the pipeline is always present and cannot be skipped. As a production pipeline is executed, an experience audit step is included after custom functional testing that will run the checks. The pages that are configured will be submitted to the service and evaluated. The results are informational and allow the user to see the scores and the change between the current and previous scores. This insight is valuable to determine if there is a regression that will be introduced with the current deployment. 
      Refer to [Understanding Experience Audit results](/help/implementing/cloud-manager/experience-audit-testing.md) for more details.

      ![](assets/stage-testing.png)


## Deployment Process {#deployment-process}

All Cloud Service deployments follow a rolling process to ensure zero downtime. Refer to [How Rolling Deployments Work](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/overview.html#how-rolling-deployments-work) to learn more.

### Deployment to Production Phase {#deployment-production-phase}

The process for deploying to production topologies differs slightly in order to minimize impact to AEM Site visitors. 

Production deployments generally follow the same steps as above, but in a rolling manner:

1. Deploy AEM packages to author.
1. Detach dispatcher1 from the load balancer.
1. Deploy AEM packages to publish1 and the dispatcher package to dispatcher1, flush dispatcher cache.
1. Put dispatcher1 back into the load balancer.
1. Once dispatcher1 is back in service, detach dispatcher2 from the load balancer.
1. Deploy AEM packages to publish2 and the dispatcher package to dispatcher2, flush dispatcher cache.
1. Put dispatcher2 back into the load balancer.
This process continues until the deployment has reached all publishers and dispatchers in the topology.
