---
title: Cloud Manager FAQs
description: Find answers to the most frequently-asked questions about Cloud Manager in AEM as a Cloud Service.
exl-id: eed148a3-4a40-4dce-bc72-c7210e8fd550
---

# Cloud Manager FAQs {#cloud-manager-faqs}

This document provides answers to the most frequently-asked questions about Cloud Manager in AEM as a Cloud Service.

## Is it possible to use Java 11 with Cloud Manager builds? {#java-11-cloud-manager}

Your AEM Cloud Manager build may fail when attempting to switch the build from Java 8 to 11. The problem can have many causes and most common ones are documented in this section.

* Add the `maven-toolchains-plugin` with proper settings for Java 11.
  * This is documented [here](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/using-the-wizard.md#getting-started).
  * For example, see the [wknd project sample project code](https://github.com/adobe/aem-guides-wknd/commit/6cb5238cb6b932735dcf91b21b0d835ae3a7fe75).

* If you encounter the following error, then you need to remove `maven-scr-plugin` and convert all OSGi annotations to OSGi R6 annotations.
  * For instructions, see [here.](https://cqdump.wordpress.com/2019/01/03/from-scr-annotations-to-osgi-annotations/).

   ```text
   [main] [ERROR] Failed to execute goal org.apache.felix:maven-scr-plugin:1.26.4:scr (generate-scr-scrdescriptor) on project helloworld.core: /build_root/build/testsite/src/main/java/com/adobe/HelloWorldServiceImpl.java : Unable to load compiled class: com.adobe.HelloWorldServiceImpl: com/adobe/HelloWorldServiceImpl has been compiled by a more recent version of the Java Runtime (class file version 55.0), this version of the Java Runtime only recognizes class file versions up to 52.0 -> [Help 1]
   ```

* For Cloud Manager builds, the `maven-enforcer-plugin` fails with error `"[main] [WARNING] Rule 1: org.apache.maven.plugins.enforcer.RequireJavaVersion"`. This is a known issue due to Cloud Manager using a different version of Java to run the maven command versus compiling code. For now, omit `requireJavaVersion` from your `maven-enforcer-plugin` configurations.

## The code quality check failed and our deployment is stuck. Is there a way to bypass this check? {#deployment-stuck}

All code quality check failures except for the security rating are non-critical metrics, so they can be bypassed by expanding the items in the results UI.  

A user in the [Deployment Manager, Program Manager, or Business Owner](/help/onboarding/learn-concepts/aem-cs-team-product-profiles.md) role can override the issues, in which case the pipeline proceeds. These uses can also accept the issues, in which case the pipeline stops with a failure.

See the document [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md) for more details.

## Can I use SNAPSHOT for the version of the Maven project? How does versioning of the packages and bundle jar files work for stage and production deployments? {#snapshot-version}

The following scenarios deal with package and bundle jar file versioning for stage and production deployments.

* For developer deployments, the git branch `pom.xml` files must contain `-SNAPSHOT` at the end of the `<version>` value.
  * This allows subsequent deployment to still be installed when the version did not change. In developer deployments, no automatic version is added or generated for the maven build.

* In stage and production deployments, an automatic version is generated as [documented here.](/help/implementing/cloud-manager/managing-code/project-version-handling.md)

* For custom versioning in stage and production deployments, set a proper three-part maven version like `1.0.0`. Increase the version each time you deploy to production.

* Cloud Manager automatically adds its version to stage and production builds and creates a git branch. No special configuration is required. If you do not set a maven version as described previously, the deployment will still succeed and a version will automatically be set.

* You can set the version to `-SNAPSHOT` for stage and production builds or deployments with no issue. Cloud Manager automatically sets a proper version number and creates a tag for you in git. This tag can be referred to later, if required.

* If you want to try out some experimental code in a development environment, you can create a new git branch and set the pipeline to use that branch.
  * This is useful when deployments fail and you would like to test with older versions of the code to determine what change caused the failure.

   * The git command below creates a remote branch named `testbranch1` based on the pre-existing commit `485548e4fbafbc83b11c3cb12b035c9d26b6532b`.  This branch can be used in Cloud Manager without affecting any other branches.

   ```shell
   git push origin 485548e4fbafbc83b11c3cb12b035c9d26b6532b:refs/heads/testbranch1
   ```

   * See the [git documentation](https://git-scm.com/book/en/v2/Git-Internals-Git-References) for more details.

   * If you want to delete the test branch later, then use the delete command:

   ```shell
   git push origin --delete testbranch1
   ```

## My maven build fails for Cloud Manager deployments but it builds locally without errors. What is wrong? {#maven-build-fail}

See [Git Resource](https://github.com/cqsupport/cloud-manager/blob/main/cm-build-step-fails.md) for more details.

## What do I do if a Cloud Manager deployment fails at the deploy step in AEM as a Cloud Service? {#cloud-manager-deployment-cloud-service}

The most common reason for a deployment to fail is due to insufficient permissions for the `sling-distribution-importer` user. In this situation, the deploy step fails during a Cloud Manager deployment and errors such as the following are generated.

```text
[Queue Processor for Subscriber agent forwardPublisherSubscriber] org.apache.jackrabbit.vault.fs.io.Importer Error while committing changes. Retrying import from checkpoint at /. Retries 4/10
[Queue Processor for Subscriber agent forwardPublisherSubscriber] org.apache.sling.distribution.journal.impl.subscriber DistributionSubscriber Error processing queue item
org.apache.sling.distribution.common.DistributionException: Error processing distribution package
dstrpck-1583514457813-c81e7751-2da6-4d00-9814-434187f08d32. Retry attempts 162/infinite.
Caused by: org.apache.sling.api.resource.PersistenceException: Unable to commit changes to session.
Caused by: javax.jcr.AccessDeniedException: OakAccess0000: Access denied [EventAdminAsyncThread #7] org.apache.sling.distribution.journal.impl.publisher.DistributionPublisher [null] Error processing distribution package` `dstrpck-1583514457813-c81e7751-2da6-4d00-9814-434187f08d32. Retry attempts 344/infinite. Message: Error trying to extract package at path /etc/packages/com.myapp/myapp-base.ui.content-5.1.0-SNAPSHOT.
```

In this case, the `sling-distribution-importer` user needs additional permissions for the content paths defined in the `ui.content package`.  This usually means you need to add permissions for both `/conf` and `/var`.

The solution is to add a [RepositoryInitializer OSGi configuration](/help/implementing/deploying/overview.md#repoint) script to your apps deployment package to add ACLs for the `sling-distribution-importer` user.

In the previous example error, the package `myapp-base.ui.content-*.zip` includes content under `/conf` and `/var/workflow`. In order for the deployment to succeed, permissions for the `sling-distribution-importer` under those paths is needed.

Here's an example [org.apache.sling.jcr.repoinit.RepositoryInitializer-DistributionService.config](https://github.com/cqsupport/cloud-manager/blob/main/org.apache.sling.jcr.repoinit.RepositoryInitializer-distribution.config) of one such OSGi configuration that adds additional permissions for the `sling-distribution-importer` user.  This configuration adds permissions under `/var`.  This xml file below [1] needs to be added to the application package under `/apps/myapp/config` (where myapp is the folder where your application code is stored).
org.apache.sling.jcr.repoinit.RepositoryInitializer-DistributionService.config

If adding a RepositoryInitializer OSGi configuration did not solve the error, it may be due to one of these additional issues.

* The deployment might be failing due to a bad OSGi configuration that breaks an out-of-the box service. 
  * Check the logs during deployment to see if there are any obvious errors.

* The deployment might fail due to bad dispatcher or Apache configurations.
  * Make sure to test your Apache and dispatcher configurations locally using the Docker image included in the SDK.
  * See [Dispatcher in the Cloud](/help/implementing/dispatcher/disp-overview.md#content-delivery) on how to set up the dispatcher Docker container for easy local testing.

* The deployment might fail due to some other failure during replication of the content packages (Sling distribution) from author to publish instances. 
  * Follow these steps to simulate the issue on a local setup.
    1. Install an author and publish instance locally using the latest AEM SDK jars.
    1. Log into the author instance.
    1. Go to **Tools** -&gt; **Deployment** -&gt; **Distribution**.
    1. Distribute the content packages that are part of the code base and see if the queue gets blocked with an error.

## I am unable to set a variable using an aio command. What can I do? {#set-variable} 

You may receive a `403` error such as the following when attempting to list or set pipeline variables via `aio` commands.

```shell
$ aio cloudmanager:list-pipeline-variables 222

Cannot get variables: https://cloudmanager.adobe.io/api/program/111/pipeline/222/variables (403 Forbidden)

$ aio cloudmanager:set-pipeline-variables 222 --variable TEST 1

Cannot get variables: https://cloudmanager.adobe.io/api/program/111/pipeline/222/variables (403 Forbidden)

$ aio cloudmanager:set-environment-variables 1755 --variable TEST 1

setting variables... !

Cannot set variables: https://cloudmanager.adobe.io/api/program/111/environment/222/variables (403 Forbidden)
```

In this case, the user executing these commands needs to be added to the **Deployment Manage** role in the Admin Console.

See [API Permissions](https://www.adobe.io/apis/experiencecloud/cloud-manager/docs.html#!AdobeDocs/cloudmanager-api-docs/master/permissions.md) for more details.
