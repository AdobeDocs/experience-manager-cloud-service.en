---
title: Code Quality Testing
description: Learn how code quality testing of pipelines works and how it can improve the quality of your deployments.
exl-id: e2981be9-fb14-451c-ad1e-97c487e6dc46
---
# Code Quality Testing {#code-quality-testing}

Learn how code quality testing of pipelines works and how it can improve the quality of your deployments.

>[!CONTEXTUALHELP]
>id="aemcloud_nonbpa_codequalitytests"
>title="Code Quality Testing"
>abstract="Code quality testing evaluates your application code based on a set of quality rules. It is the primary purpose of a code-quality only pipeline and is executed immediately following the build step in all production and non-production pipelines."

## Introduction {#introduction}

Code quality testing evaluates your application code based on a set of quality rules. It is the primary purpose of a code-quality only pipeline and is executed immediately following the build step in all production and non-production pipelines.

Refer to the document [Configuring Your CI-CD Pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) to learn more about different types of pipelines.

## Code Quality Rules {#understanding-code-quality-rules}

Code quality testing scans the source code to ensure that it meets certain quality criteria. This is implemented by a combination of SonarQube and content package-level examination using OakPAL. There are over 100 rules, combining generic Java rules and AEM-specific rules. Some of the AEM-specific rules are created based on best practices from AEM Engineering and are referred to as [custom code quality rules](/help/implementing/cloud-manager/custom-code-quality-rules.md).

>[!NOTE]
>
>You can download the complete list of rules [with this link.](/help/implementing/cloud-manager/assets/CodeQuality-rules-latest-CS.xlsx)

### Three-Tiered Ratings {#three-tiered-gate}

Issues identified by code quality testing are assigned to one of three categories.

* **Critical** - These are issues which cause an immediate failure of the pipeline.

* **Important** - These are issues which cause the pipeline to enter a paused state. A deployment manager, project manager, or business owner can either override the issues, in which case the pipeline proceeds, or they can accept the issues, in which case the pipeline stops with a failure.

* **Info** - These are issues which are provided purely for informational purposes and have no impact on the pipeline execution

>[!NOTE]
>
>In a code quality only pipeline, important failures in the Code Quality gate cannot be overridden since the code quality testing step is the final step in the pipeline.

### Ratings {#ratings}

The results of this step is delivered as **Ratings**. 

The following table summarizes the ratings and failure thresholds for each of the critical, important and information categories.

|Name|Definition|Category|Failure Threshold|
|--- |--- |--- |--- |
|Security Rating|A = No vulnerabilities <br/>B = At least 1 minor vulnerability<br/> C = At least 1 major vulnerability <br/>D = At least 1 critical vulnerability <br/>E = At least 1 blocker vulnerability|Critical|&lt; B|
|Reliability Rating|A = No bugs <br/>B = At least 1 minor bug <br/>C = At least 1 major bug <br/>D = At least 1 critical bug<br>E = At least 1 blocker bug|Critical|&lt; D|
|Maintainability Rating|Defined by the outstanding remediation cost for code smells as a percentage of the time that has already gone into the application<br/><ul><li>A = &lt;=5%</li><li>B = 6-10%</li><li>C = 11-20%</li><li>D = 21-50%</li><li>E = >50%</li></ul>|Important|&lt; A|
|Coverage|Defined by a mix of unit test line coverage and condition coverage using the formula: <br/>`Coverage = (CT + CF + LC)/(2*B + EL)`  <ul><li>`CT` = Conditions that have been evaluated as `true` at least once while running unit tests</li><li>`CF` = Conditions that have been evaluated as `false` at least once while running unit tests</li><li>`LC` = Covered lines = lines_to_cover - uncovered_lines</li><li>`B` = total number of conditions</li><li>`EL` = total number of executable lines (lines_to_cover)</li></ul>|Important|&lt; 50%|
|Skipped Unit Tests|Number of skipped unit tests|Info|> 1|
|Open Issues|Overall issue types - Vulnerabilities, Bugs, and Code Smells|Info|&gt; 0|
|Duplicated Lines|Defined as the number of lines involved in duplicated blocks. A block of code is considered duplicated under the following conditions.<br>Non-Java Projects:<ul><li>There should be at least 100 successive and duplicated tokens.</li><li>Those tokens should be spread over at least: </li><li>30 lines of code for COBOL </li><li>20 lines of code for ABAP </li><li>10 lines of code for other languages</li></ul>Java Projects:<ul></li><li> There should be at least 10 successive and duplicated statements regardless of the number of tokens and lines.</li></ul>Differences in indentation as well as in string literals are ignored when detecting duplicates.|Info|&gt; 1%|
|Cloud Service Compatibility|Number of identified cloud service compatibility issues|Info|> 0|

>[!NOTE]
>
>Refer to [SonarQube's metric definitions](https://docs.sonarqube.org/display/SONAR/Metric+Definitions) for more detailed definitions.

>[!NOTE]
>
>To learn more about the custom code quality rules executed by [!UICONTROL Cloud Manager], please refer to the document [Custom Code Quality Rules](/help/implementing/cloud-manager/custom-code-quality-rules.md).

## Dealing with False Positives {#dealing-with-false-positives}

The quality scanning process is not perfect and will sometimes incorrectly identify issues which are not actually problematic. This is referred to as a **false positive**.

In these cases, the source code can be annotated with the standard Java `@SuppressWarnings` annotation specifying the rule ID as the annotation attribute. For example, one common false positive is that the SonarQube rule to detect hardcoded passwords can be aggressive about how a hardcoded password is identified.

The following code is fairly common in an AEM project, which has code to connect to some external service.

```java
@Property(label = "Service Password")
private static final String PROP_SERVICE_PASSWORD = "password";
```

SonarQube will then raise a blocker vulnerability. But after reviewing the code, you recognize that this is not a vulnerability and can annotate the code with the appropriate rule ID.

```java
@SuppressWarnings("squid:S2068")
@Property(label = "Service Password")
private static final String PROP_SERVICE_PASSWORD = "password";
```

However, if the code was actually this:

```java
@Property(label = "Service Password", value = "mysecretpassword")
private static final String PROP_SERVICE_PASSWORD = "password";
```

Then the correct solution is to remove the hardcoded password.

>[!NOTE]
>
>While it is a best practice to make the `@SuppressWarnings` annotation as specific as possible, i.e. annotate only the specific statement or block causing the issue, it is possible to annotate at a class level.

>[!NOTE]
>While there is no explicit security testing step, there are security-related code quality rules evaluated during the code quality step. Refer to the document [Security Overview for AEM as a Cloud Service](/help/security/cloud-service-security-overview.md) to learn more about security in Cloud Service.

## Content Package Scanning Optimization {#content-package-scanning-optimization}

As part of the quality analysis process, Cloud Manager performs analysis of the content packages produced by the Maven build. Cloud Manager offers optimizations to accelerate this process, which are effective when certain packaging constraints are observed. Most significant is the optimization performed for projects that output a single content package, generally referred to as an "all" package, which contains a number of other content packages produced by the build, which are marked as skipped. When Cloud Manager detects this scenario, rather than unpack the "all" package, the individual content packages are scanned directly and sorted based on dependencies. For example, consider the following build output.

* `all/myco-all-1.0.0-SNAPSHOT.zip` (content-package)
* `ui.apps/myco-ui.apps-1.0.0-SNAPSHOT.zip` (skipped-content-package)
* `ui.content/myco-ui.content-1.0.0-SNAPSHOT.zip` (skipped-content-package)

If the only items inside `myco-all-1.0.0-SNAPSHOT.zip` are the two skipped content packages, then the two embedded packages will be scanned in lieu of the "all" content package.

For projects that produce dozens of embedded packages, this optimization has been shown to save upwards of 10 minutes per pipeline execution.

A special case can occur when the "all" content package contains a combination of skipped content packages and OSGi bundles. For example, if `myco-all-1.0.0-SNAPSHOT.zip` contained the two embedded packages previously mentioned as well as one or more OSGi bundles, then a new, minimal content package is constructed with only the OSGi bundles. This package is always named `cloudmanager-synthetic-jar-package` and the contained bundles are placed in `/apps/cloudmanager-synthetic-installer/install`.

>[!NOTE]
>
>* This optimization does not impact the packages which are deployed to AEM.
>* Because the matching between the embedded content packages and the skipped content packages is based on file names, this optimization cannot be performed if multiple skipped content packages have exactly the same file name or if the file name is changed while embedding.
