---
title: Code Assessment Skill
description: Learn how to use the code-assessment skill to find and fix AEM as a Cloud Service anti-patterns and deprecated APIs with an AI coding agent.
feature: Developing
role: Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---
# Code Assessment Skill {#code-assessment-skill}

>[!NOTE]
>
>This article covers the `code-assessment` skill for **AEM Java stack development**. For an introduction to agent skills, `AGENTS.md`, and the local MCP servers, see [Local Development with AI Tools](/help/ai-in-aem/local-development-with-ai-tools.md).

The `code-assessment` skill detects, reviews, and fixes code-quality and correctness issues in an AEM as a Cloud Service project entirely within your local workspace. Large language models (LLMs) have general knowledge of good Java code. The skill adds AEM-specific conventions, gathered from production experience with AEM as a Cloud Service websites. With these conventions, your AI coding agent finds the patterns that cause Cloud Manager pipeline failures and production incidents, and fixes them in a consistent, reviewable way.

Use the skill to:

* Find usage of [deprecated and removed AEM APIs](/help/release-notes/deprecated-removed-features.md) before a Cloud Manager pipeline fails on them.
* Detect anti-patterns, such as outbound HTTP calls without timeouts and unbounded queries, that can lead to resource exhaustion and outages.
* Apply surgical fixes one pattern at a time, on a dedicated Git branch, with every change verified by a build before you review it.

Describe the issue, and the skill routes the request to the appropriate remediation workflow.

## How the Skill Works {#how-the-skill-works}

The skill works in two phases. Keeping them separate lets you review every finding before any code changes, and lets you commit each type of fix independently.

|Phase|What happens|Changes code|
|---|---|---|
|**Review**|The skill runs its detectors across the project and returns a report of findings, grouped by pattern and severity, with a planned action and a suggested remediation order.|No|
|**Apply**|You select one pattern. The skill reads that pattern's remediation recipe, creates a Git branch, makes the edits, and verifies them with a build.|Yes, on a new branch. The skill never commits or pushes.|

The skill is organized as a main skill that links to one sub-skill per pattern. Each sub-skill contains a recipe that describes how to detect and fix that pattern, along with the conditions under which the fix must be skipped. For deprecated APIs, the sub-skill runs an analyzer script that checks your code against the current list of AEM deprecations, because that list changes over time.

## Supported Checks {#supported-checks}

The skill checks for the following, with more checks added over time:

* Usage of [deprecated and removed AEM APIs](/help/release-notes/deprecated-removed-features.md)
* Outbound HTTP calls without timeouts
* Unbounded queries
* Outdated Maven dependencies
* Sling Model dependency injection that can be modernized
* Sling schedulers, resource change listeners, and JCR or OSGi event handling
* Usage of the Replication and Assets APIs

Depending on the issue, the skill either applies a mechanical fix directly or guides you through one that needs a judgment call.

You can reference a pattern by its identifier in your prompts. Common patterns include:

|Pattern|What it detects|Typical fix|
|---|---|---|
|`remove-deprecated-api`|Imports of Java packages that are deprecated or removed in AEM as a Cloud Service, such as Google Guava (`com.google.common.*`). After an API reaches its removal date, its usage fails the Cloud Manager pipeline.|Replaces the API with its documented successor, or removes code that is no longer used.|
|`outbound-call-timeouts`|HTTP clients created without connect, read, or connection-pool timeouts. A slow downstream service can then hold a request thread indefinitely.|Adds bounded timeouts, reusing timeout configuration that already exists in the class.|
|`unbounded-query`|Queries that load every result into memory, for example by calling `setLimit(-1)`. Unbounded queries are a common cause of out-of-memory outages.|Caps the result set where the calling code reads a single result. Asks for a pagination decision otherwise.|
|`resource-change-listener`|`ResourceChangeListener` implementations, which are flagged for review by design.|Verifies that the listener's paths and change types are correctly scoped. Compliant listeners are reported as a verified pass.|
|`outdated-dependencies`|Versioned Maven dependencies within the skill's allowlist scope, including `aem-sdk-api`.|Locates each dependency coordinate. The skill does not declare a dependency stale or change its version until you supply a target version.|

## Before You Begin {#before-you-begin}

Make sure the following are in place:

* The `code-assessment` skill is installed for your AI coding agent. See [Install Skills](/help/ai-in-aem/local-development-with-ai-tools.md#install-skills).
* Your AEM as a Cloud Service project is a Maven project that builds locally. The skill compiles the project before and after it makes changes, so a failing baseline build limits what it can verify.
* Your project is a Git repository. The skill creates a new branch for each pattern it applies. Starting from a clean working tree keeps each fix isolated in its own diff.

## Review Your Project {#review-your-project}

To get started, open a new agent chat in your AEM as a Cloud Service project.

For a broad or first-time review, ask the skill to assess the whole project. It runs every detector, reports all findings, and changes no code at this stage.

```
scan my AEM project and report any code-quality issues
```

For a more explicit invocation, name the skill directly:

```
/code-assessment review my code for AEM as a Cloud Service issues
```

To focus on a single pattern, name it in the prompt:

```
scan my project for unbounded queries
```

During a whole-project review, the skill typically:

1. Classifies the request and selects the detectors to run. A broad prompt runs all detectors in report-only mode.
1. Runs a deprecated-API preflight against the latest AEM SDK using the [AEM as a Cloud Service SDK Build Analyzer Maven Plugin](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin), and compiles the project to establish a baseline. Long-running steps can run in the background while the agent reads your source code, OSGi configurations, and content packages.
1. Runs the main analyzer and reads the remediation recipe for each pattern that it found.
1. Confirms the facts that determine each planned action, for example whether a flagged method has any callers.
1. Writes a run log to `.autofix/last-run.json` in the project and returns the report inline.

### Read the Report {#read-the-report}

The report is organized into the following sections:

|Section|Content|
|---|---|
|**Run metadata**|The patterns audited, the invocation mode, the intent (for example, `report`), and the edit mode.|
|**Preflight**|The result of the deprecated-API preflight against the latest AEM SDK, and the result of the baseline compile.|
|**Discover warnings**|Files the analyzer could not parse. An empty list means that every file was analyzed.|
|**Candidates**|One table per pattern, with the severity of the pattern and, for each finding, the file and line, the code that was found, the planned action, and the reasoning or target for the fix.|
|**Summary counts**|The number of findings to apply, skip, and defer. Applied, skipped, and deferred findings add up to the total number of findings.|
|**Deferred**|Findings that have no recipe or were not selected.|
|**Observations**|Issues the agent noticed outside of any detector. These are offered as observations, not findings.|
|**Next step**|A suggested order for applying patterns, ranked by impact (blast radius), starting with the pattern that would fail your pipeline today.|

Every finding includes a planned action. When the skill skips a finding, it states the reason so that you can decide whether to act on it yourself. Common skip reasons include:

|Skip reason|Meaning|
|---|---|
|`needs-pagination`|Capping the query would silently truncate results that callers depend on. Decide on a pagination approach first.|
|`needs-user-target`|The skill needs you to supply a target version. For `aem-sdk-api`, align the version with the AEM SDK used by your Cloud Manager environment rather than assuming the latest version.|
|`already-compliant`|The code was flagged for review and verified as compliant. This is a pass, not a defect.|
|`manual-only-guava`|A Guava replacement would change behavior, so it requires a design decision rather than a mechanical rewrite.|

>[!NOTE]
>
>If a pattern returns no findings, it means that the detectors found no matches. It does not mean that the project is free of every issue. See [Limitations](#limitations).

## Apply Fixes {#apply-fixes}

Ask the skill to fix one pattern at a time. Applying one pattern per session keeps each change set focused on a single concern, so you can review it as one diff and revert it atomically if needed.

```
apply unbounded-query
```

When you apply a pattern, the skill:

1. Reads the pattern's recipe and the Git workflow reference in full before making any edit.
1. Creates a branch for the pattern. The branch name includes the pattern identifier, for example `autofix/outbound-call-timeouts/<date>-<id>`.
1. Makes surgical edits to the affected files only, without reformatting or making unrelated changes. Mechanical fixes apply directly. Guided fixes walk you through each decision.
1. Verifies the change. The skill compiles the project, runs the existing tests when the baseline build included them, and re-runs the detector to confirm the findings are resolved.
1. Updates the run log and returns a summary of what changed, why it chose that approach, the verification results, and any action it left for you.

Large fixes run in resumable batches. To continue with the next batch, reply `apply <pattern>`.

### Review and Commit the Changes {#review-and-commit}

The skill never commits or pushes. It leaves its edits uncommitted on the new branch so that you can review them first.

1. Review the working tree changes:

   ```bash
   git status
   git --no-pager diff
   ```

   Because nothing is committed yet, compare the working tree rather than running `git diff main...HEAD`.

1. If the changes look right, stage and commit them yourself. The skill's summary suggests a commit message, for example `autofix: outbound-call-timeouts - bound outbound HTTP calls`.
1. Merge the branch through your usual review process, then run your Cloud Manager [code quality pipeline](/help/implementing/cloud-manager/code-quality-testing.md) to confirm compliance.
1. Apply the next pattern from the suggested order.

## Example: Add Timeouts to Outbound Calls {#example-outbound-call-timeouts}

In this example, a project has two outbound HTTP calls that the review reported under `outbound-call-timeouts`:

* `InventoryServiceImpl`, an OSGi service that uses Apache HttpClient 4.x. One of its methods already builds a `RequestConfig` from OSGi-configured timeouts. A second method creates its client with `HttpClients.createDefault()`, which runs on effectively infinite connect and socket timeouts.
* `ProductFeedClient`, which uses the JDK `java.net.http` client. The client sets a connect timeout, but the JDK client has no client-level read timeout, so a feed that connects and then stalls holds the request thread indefinitely.

Enter the following prompt:

```
apply outbound-call-timeouts
```

The recipe's rule is to reuse a `RequestConfig` already present in a file rather than introduce a second one. Instead of hard-coding the recipe's generic default values, the skill extracts the existing configuration into a helper method and uses it for both calls. This keeps both calls honoring the timeouts configured for the environment:

```java
/**
 * The configured connect, socket, and pool-checkout timeouts. Every outbound call
 * uses these so a slow downstream API cannot hold a request thread indefinitely.
 */
private RequestConfig requestConfig() {
    return RequestConfig.custom()
            .setConnectTimeout(connectTimeoutMillis)
            .setSocketTimeout(socketTimeoutMillis)
            .setConnectionRequestTimeout(2000)
            .build();
}

@Override
public String getPickupWindow(String storePath) {
    try (CloseableHttpClient client = HttpClientBuilder.create()
            .setDefaultRequestConfig(requestConfig())
            .build()) {
        // ...
    }
}
```

The skill also removes the `HttpClients` import, which is no longer used.

For the JDK client, the read timeout can only be set per request, so the skill adds it to the request builder:

```java
HttpRequest request = HttpRequest.newBuilder(URI.create(feedUrl))
        .timeout(Duration.ofSeconds(8))
        .header("Accept", "application/json")
        .GET()
        .build();
```

The skill then compiles the project, runs the existing unit tests, and re-runs the detector, which returns no remaining findings for the pattern.

>[!NOTE]
>
>The JDK `HttpRequest.timeout()` value is a ceiling on the whole request, not an idle timeout between bytes such as the socket timeout in Apache HttpClient. The two settings are not equivalent. If a downstream response can legitimately take longer than the recipe's default, raise the value to a figure measured for that service.

## Example: Remove Deprecated APIs {#example-remove-deprecated-api}

In this example, the review reported four usages of Google Guava under `remove-deprecated-api`. Guava is listed in [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md#com.google.common), so after its removal date, these usages fail the Cloud Manager pipeline. They are not warnings.

Enter the following prompt:

```
apply remove-deprecated-api
```

When the analyzer's hint for a deprecated API does not name a successor, the skill consults the [API Removal Guidance](/help/release-notes/deprecated-removed-features.md#api-removal-guidance) on Experience League once per session. For Guava, the guidance is to replace usage with JDK collections or Apache Commons Collections4.

Before choosing a replacement, the skill checks which successors are resolvable on the module's classpath and how the module declares its dependencies. In this project, Apache Commons Collections4 is available only transitively through the AEM SDK, so the skill uses JDK-only replacements and adds no new dependency:

|Deprecated usage|Replacement|
|---|---|
|`ImmutableSet.copyOf(...)`|`Set.copyOf(Arrays.asList(...))`, which preserves the immutable-set semantics|
|`Iterators.size(...)`|An explicit loop that consumes the iterator exactly as the Guava method did|
|`Splitter`, used only in a private method with no callers|The unused method and its import are removed, rather than ported|

For example:

```java
// Before
public static final Set<String> ISO_LANGUAGES = ImmutableSet.copyOf(Locale.getISOLanguages());

// After
public static final Set<String> ISO_LANGUAGES = Set.copyOf(Arrays.asList(Locale.getISOLanguages()));
```

The fourth usage, `Sets.difference(a, b)`, is reported under **Manual Action Required**. Guava returns a lazy, live view backed by both sets, while every JDK and Collections4 equivalent returns an eager copy. Because that changes behavior for any caller that later modifies the input sets, the skill treats the replacement as a design decision and does not guess. If no caller modifies the inputs afterward, the eager copy is a safe swap, and the skill can apply it on request.

The final summary lists the files modified, each fix with its source, the residual analyzer findings, and any warnings from the build that are unrelated to the edits.

## Limitations {#limitations}

* **Detection is local static analysis.** The skill cannot see runtime state. Behavior such as Sling Model adaptation and service user mappings still needs to be validated by deploying to a development environment. To inspect runtime behavior on your local SDK, use the [AEM Quickstart MCP Server](/help/ai-in-aem/local-development-with-ai-tools.md#aem-quickstart-mcp-server).
* **Not every anti-pattern has a detector yet.** Examples include unclosed `ResourceResolver` or JCR `Session` objects, thread and lock contention, heavy work in `@PostConstruct` methods, in-process image processing, unbounded recursion, unbounded GraphQL queries, and logging in loops. The agent may still mention these as observations, but the absence of a finding is not a clean bill of health.
* **Some fixes need your input.** Findings that require a design decision, a pagination strategy, or a target dependency version are skipped with a stated reason rather than fixed automatically.

## Related Resources {#related-resources}

* [Local Development with AI Tools](/help/ai-in-aem/local-development-with-ai-tools.md)
* [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md)
* [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md)
* [Development Agentic Capabilities](/help/ai-in-aem/agentic-capabilities/brand-experience/development/use-cases.md), for troubleshooting failed Cloud Manager pipelines with AI
* [adobe/skills repository](https://github.com/adobe/skills/tree/main/plugins/aem/cloud-service)

Feel free to email [aemcs-ai-ide-tools-feedback@adobe.com](mailto:aemcs-ai-ide-tools-feedback@adobe.com) with feedback to help shape product development.
