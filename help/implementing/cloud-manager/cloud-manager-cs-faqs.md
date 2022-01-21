---
title: Cloud Manager - Cloud Services FAQs
seo-title: Cloud Manager FAQs
description: Refer to Cloud Manager for Cloud Services FAQs to get some troubleshooting tips
seo-description: Follow this page to get answers on Cloud Manager - Cloud Services FAQs
exl-id: eed148a3-4a40-4dce-bc72-c7210e8fd550
---
# Cloud Manager FAQs {#cloud-manager-faqs}

The following section provides answers to frequently asked questions related to Cloud Manager for Cloud Services.

## Is it possible to use Java 11 with Cloud Manager builds? {#java-11-cloud-manager}

AEM Cloud Manager build fails when attempting to switch the build from Java 8 to 11. The problem can have many causes and most common ones are documented below:

* Add the maven-toolchains-plugin with the correct settings for Java 11 as documented [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/getting-started/create-application-project/using-the-wizard.html?lang=en#getting-started).  For example, see the [wknd sample project code](https://github.com/adobe/aem-guides-wknd/commit/6cb5238cb6b932735dcf91b21b0d835ae3a7fe75).

* If you encounter the error below then you need to remove use of `maven-scr-plugin` and convert all OSGi annotations to OSGi R6 annotations. For instructions, see [here](https://cqdump.wordpress.com/2019/01/03/from-scr-annotations-to-osgi-annotations/).

   `[main] [ERROR] Failed to execute goal org.apache.felix:maven-scr-plugin:1.26.4:scr (generate-scr-scrdescriptor) on project helloworld.core: /build_root/build/testsite/src/main/java/com/adobe/HelloWorldServiceImpl.java : Unable to load compiled class: com.adobe.HelloWorldServiceImpl: com/adobe/HelloWorldServiceImpl has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version of the Java Runtime only recognizes class file versions up to 52.0 -> [Help 1]`

* For Cloud Manager builds, the maven enforcer plugin fails with error `"[main] [WARNING] Rule 1: org.apache.maven.plugins.enforcer.RequireJavaVersion"`. This is a known issue due to Cloud Manager using a different version of Java to run the maven command versus compiling code. For now, omit `requireJavaVersion` from your maven-enforcer-plugin configurations.

## Our deployment is stuck because the Code Quality check failed. Is there a way to bypass this check? {#deployment-stuck}

All Code Quality failures except for *Security Rating* are non-critical metrics, so they can be bypassed by expanding the items in the results UI.  

A user with [Deployment Manager, Project Manager, or Business Owner](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/requirements/setting-up-users-and-roles.html?lang=en#requirements) role can override the issues, in which case the pipeline proceeds or they can accept the issues, in which case the pipeline stops with a failure.  See [Three-Tier Gates while Running a Pipeline](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/how-to-use/understand-your-test-results.html?lang=en#how-to-use) for more details.


## Are we allowed to use SNAPSHOT in the version of the Maven project? How does versioning of the packages and bundle jar files work for Stage and Production deployments? {#snapshot-version}

Refer to the following scenarios to learn about versioning of the packages and bundle jar files for Stage and Production deployments:

1. For developer deployments, the Git branch `pom.xml` files must contain `-SNAPSHOT` at the end of the `<version>` value. This allows subsequent deployment where the version does not change to still get installed. In developer deployments, no automatic version is added or generated for the maven build.

1. In Stage and Production deployment, an automatic version is generated as documented [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/using/managing-code/activating-maven-project.html?lang=en#managing-code).

1. For custom versioning in Stage and Production deployments, set a 3 part proper maven version like `1.0.0`. Increase the version each time you have to do another deploy to production.

1. Cloud Manager automatically adds its version to Stage and Production builds and even creates a Git branch. No special configuration is required. If step 3 above is skipped, the deployment would still work fine and a version would automatically be set.

1. There are no issues, if you leave the version with `-SNAPSHOT` for Stage and Production builds or deployments. Cloud Manager automatically sets a proper version number and creates a tag for you in Git. This tag can be referred to later, if required.

1. If you want to try out some experimental code on Development environment, you can create a new Git branch and set the pipeline to use that different branch. This is useful when deployments start failing and you would like to test with older versions of the code to see when it broke.

   The Git command below creates a remote branch named *testbranch1* against a specific pre-existing commit `485548e4fbafbc83b11c3cb12b035c9d26b6532b`.  This special branch could be used in Cloud Manager without affecting any other branches:

   `git push origin 485548e4fbafbc83b11c3cb12b035c9d26b6532b:refs/heads/testbranch1`

   See the [Git documentation](https://git-scm.com/book/en/v2/Git-Internals-Git-References) for more details.

   If you want to delete the test branch later, then use the delete command:

   `git push origin --delete testbranch1`

## Maven build fails in Cloud Manager deploys but builds locally without errors. How to debug? {#maven-build-fail}

See [Git Resource](https://github.com/cqsupport/cloud-manager/blob/main/cm-build-step-fails.md) for more details.

## What to do if Cloud Manager deployment fails at deploy step in AEM as a Cloud Service Environment? {#cloud-manager-deployment-cloud-service}

The most common reason for deploys to fail is due to insufficient permissions for the *sling-distribution-importer* user.
Refer to the example below to understand an issue, cause, and solution:

**Issue**
During a Cloud Manager deployment on AEM as a Cloud Service environments the deploy step fails and errors like the ones below are observed.

`[Queue Processor for Subscriber agent forwardPublisherSubscriber] org.apache.jackrabbit.vault.fs.io.Importer Error while committing changes. Retrying import from checkpoint at /. Retries 4/10`
`[Queue Processor for Subscriber agent forwardPublisherSubscriber] org.apache.sling.distribution.journal.impl.subscriber DistributionSubscriber Error processing queue item`
`org.apache.sling.distribution.common.DistributionException: Error processing distribution package`
`dstrpck-1583514457813-c81e7751-2da6-4d00-9814-434187f08d32. Retry attempts 162/infinite.`
`Caused by: org.apache.sling.api.resource.PersistenceException: Unable to commit changes to session.`
`Caused by: javax.jcr.AccessDeniedException: OakAccess0000: Access denied [EventAdminAsyncThread #7] org.apache.sling.distribution.journal.impl.publisher.DistributionPublisher [null] Error processing distribution package` `dstrpck-1583514457813-c81e7751-2da6-4d00-9814-434187f08d32. Retry attempts 344/infinite. Message: Error trying to extract package at path /etc/packages/com.myapp/myapp-base.ui.content-5.1.0-SNAPSHOT.`

**Cause**

The sling-distribution-importer user needs additional permissions per the content paths defined in the ui.content package.  This usually means we need to add permissions for both /conf and /var.

**Solution**
The solution to this is to add a [RepositoryInitializer OSGi configuration](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/deploying/overview.html?lang=en#deploying) script to your apps deployment package to add ACLs for the sling-distribution-importer user.
In the example error above, the package myapp-base.ui.content-*.zip includes content under `/conf` and `/var/workflow`. In order for the deployment to not fail, we would need to add permissions for sling-distribution-importer under those paths. 
Here's an example [org.apache.sling.jcr.repoinit.RepositoryInitializer-DistributionService.config](https://github.com/cqsupport/cloud-manager/blob/main/org.apache.sling.jcr.repoinit.RepositoryInitializer-distribution.config) of one such OSGi configuration that adds additional permissions for the sling-distribution-importer user.  This configuration adds permissions under /var.  This xml file below [1] needs to be added to the application package under `/apps/myapp/config` (where myapp is the folder where your application code is stored).
org.apache.sling.jcr.repoinit.RepositoryInitializer-DistributionService.config

1. If the *sling-distribution-importer* is not the cause, then the deploy might be failing due to a bad OSGi configuration that breaks an out of the box service. Check the logs during deployment to see if there are any obvious errors.

1. The deployment might fail due to bad dispatcher or apache configurations. Make sure to test your Apache configurations and Dispatcher configurations locally using the Docker image included in the SDK. See [Dispatcher in the Cloud](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/implementing/content-delivery/disp-overview.html?lang=en#content-delivery) on how to set up the dispatcher Docker container for easy local testing.

1. The deployment might fail due to some other failure during replication of the content packages (sling distribution) from author to publish instances. 

   Refer to the steps below to simulate this on a local setup:

      * Install an Author and Publish instance (using the latest AEM SDK jars)
      * Log into the Author instance
      * Go to **Tools** -> **Deployment** -> **Distribution**
      * Distribute the content packages that are part of the code base and see if the queue gets blocked with an error 

## Unable to set a variable via aio cloud manager set pipeline variables. How to debug these issues? {#set-variable} 

If you are getting a `403` error when attempting to list or set pipeline variables via commands similar to the ones below, then you need to be added as a *Deployment Manager* Cloud Manager product role in the Admin Console.  
See [API Permissions](https://www.adobe.io/apis/experiencecloud/cloud-manager/docs.html#!AdobeDocs/cloudmanager-api-docs/master/permissions.md) for more details.

Related commands and errors:

`$ aio cloudmanager:list-pipeline-variables 222`

*Error*: `Cannot get variables: https://cloudmanager.adobe.io/api/program/111/pipeline/222/variables (403 Forbidden)`

`$ aio cloudmanager:set-pipeline-variables 222 --variable TEST 1`

*Error*: `Cannot get variables: https://cloudmanager.adobe.io/api/program/111/pipeline/222/variables (403 Forbidden)`

`$ aio cloudmanager:set-environment-variables 1755 --variable TEST 1`

`setting variables... !`

*Error*: `Cannot set variables: https://cloudmanager.adobe.io/api/program/111/environment/222/variables (403 Forbidden)`
