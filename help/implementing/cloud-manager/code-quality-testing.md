---
title: Code Quality Testing - Cloud Services
description: Code Quality Testing - Cloud Services
exl-id: e2981be9-fb14-451c-ad1e-97c487e6dc46
---
# Code Quality Testing {#code-quality-testing}

The Code Quality Testing evaluates the quality of your application code. It is the core objective of a Code-Quality only pipeline  and is executed immediately following the build step in all non-production and production pipelines. 

Refer to [Configuring your CI-CD Pipeline](/help/implementing/cloud-manager/configure-pipeline.md) to learn more about different types of pipelines.

## Understanding Code Quality Rules {#understanding-code-quality-rules}

In Code Quality Testing, the source code is scanned to ensure that it meets certain quality criteria. Currently, this is implemented by a combination of SonarQube and content package-level examination using OakPAL. There are over 100 rules combining generic Java rules and AEM-specific rules. Some of the AEM-specific rules are created based on best practices from AEM Engineering and are referred to as [Custom Code Quality Rules](/help/implementing/cloud-manager/custom-code-quality-rules.md).

>[!NOTE]
>You can download the complete list of rules [here](/help/implementing/cloud-manager/assets/CodeQuality-rules-CS.xlsx).

**Three-tier Gate**

There is a three-tier structure in this code quality testing step for the identified issues:

* **Critical**: These are issues identified by the gate which cause an immediate failure of the pipeline.

* **Important**: These are issues identified by the gate which cause the pipeline to enter a paused state. A deployment manager, project manager, or business owner can either override the issues, in which case the pipeline proceeds, or they can accept the issues, in which case the pipeline stops with a failure.

* **Info**: These are issues identified by the gate which are provided purely for informational purposes and have no impact on the pipeline execution

The results of this step is delivered as *Ratings*. 

The following table summarizes the ratings and failure thresholds for each of the Critical, Important and Information categories:

|Name|Definition|Category|Failure Threshold|
|--- |--- |--- |--- |
|Security Rating|A = 0 Vulnerability <br/>B = at least 1 Minor Vulnerability<br/> C = at least 1 Major Vulnerability <br/>D = at least 1 Critical Vulnerability <br/>E = at least 1 Blocker Vulnerability|Critical|&lt; B|
|Reliability Rating|A = 0 Bug <br/>B = at least 1 Minor Bug <br/>C = at least 1 Major Bug <br/>D = at least 1 Critical Bug E = at least 1 Blocker Bug|Important|&lt; C|
|Maintainability Rating|Outstanding remediation cost for code smells is: <br/><ul><li>&lt;=5% of the time that has already gone into the application, the rating is A </li><li>between 6 to 10% the rating is a B </li><li>between 11 to 20% the rating is a C </li><li>between 21 to 50% the rating is a D</li><li>anything over 50% is an E</li></ul>|Important|&lt; A|
|Coverage|A mix of unit test line coverage and condition coverage using this formula: <br/>`Coverage = (CT + CF + LC)/(2*B + EL)`  <br/>where: CT = conditions that have been evaluated to 'true' at least once while running unit tests <br/>CF = conditions that have been evaluated to 'false' at least once while running unit tests <br/>LC = covered lines = lines_to_cover - uncovered_lines <br/><br/> B = total number of conditions <br/>EL = total number of executable lines (lines_to_cover)|Important|&lt; 50%|
|Skipped Unit Tests|Number of skipped unit tests.|Info|> 1|
|Open Issues|Overall issue types - Vulnerabilities, Bugs, and Code Smells|Info|&gt; 0|
|Duplicated Lines|Number of lines involved in duplicated blocks. <br/>For a block of code to be considered as duplicated: <br/><ul><li>**Non-Java projects:**</li><li>There should be at least 100 successive and duplicated tokens.</li><li>Those tokens should be spread at least on: </li><li>30 lines of code for COBOL </li><li>20 lines of code for ABAP </li><li>10 lines of code for other languages</li><li>**Java projects:**</li><li> There should be at least 10 successive and duplicated statements whatever the number of tokens and lines.</li></ul> <br/>Differences in indentation as well as in string literals are ignored while detecting duplications.|Info|&gt; 1%|
|Cloud Service Compatibility|Number of identified Cloud Service Compatibility issues.|Info|> 0|

>[!NOTE]
>
>Refer to [Metric Definitions](https://docs.sonarqube.org/display/SONAR/Metric+Definitions) for more detailed definitions.


>[!NOTE]
>
>To learn more about the custom code quality rules executed by [!UICONTROL Cloud Manager], please refer to [Custom Code Quality Rules](/help/implementing/cloud-manager/custom-code-quality-rules.md).

## Dealing with False Positives {#dealing-with-false-positives}

The quality scanning process is not perfect and will sometimes incorrectly identify issues which are not actually problematic. This is referred to as a *false positive*.

In these cases, the source code can be annotated with the standard Java `@SuppressWarnings` annotation specifying the rule ID as the annotation attribute. For example, one common problem is that the SonarQube rule to detect hardcoded passwords can be aggressive about how a hardcoded password is identified.

To look at a specific example, this code would be fairly common in an AEM project which has code to connect to some external service:

```java
@Property(label = "Service Password")
private static final String PROP_SERVICE_PASSWORD = "password";
```

SonarQube will then raise a Blocker Vulnerability. After reviewing the code, you identify that this is not a vulnerability and can annotate this with the appropriate rule id.

```java
@SuppressWarnings("squid:S2068")
@Property(label = "Service Password")
private static final String PROP_SERVICE_PASSWORD = "password";
```

However, on the other hand, if the code was actually this:

```java
@Property(label = "Service Password", value = "mysecretpassword")
private static final String PROP_SERVICE_PASSWORD = "password";
```

Then the correct solution is to remove the hardcoded password.

>[!NOTE]
>
>While it is a best practice to make the `@SuppressWarnings` annotation as specific as possible, i.e. annotate only the specific statement or block causing the issue, it is possible to annotate at a class level.

>[!NOTE]
>While there is no explicit Security Testing step,  there are still security-related code quality rules evaluated during the code quality step. Refer to [Security Overview for AEM as a Cloud Service](/help/security/cloud-service-security-overview.md) to learn more about security in Cloud Service.
