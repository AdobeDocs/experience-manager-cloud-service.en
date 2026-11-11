---
title: Code Assessment Skill
description: Learn how to use the code-assessment skill to find and fix AEM as a Cloud Service anti-patterns and deprecated APIs with an AI coding agent.
feature: Developing
role: Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: f2d27a5f-0d67-4d85-8a24-86a8d8a3574b
    internal-label: Developer tools
  - id: ac5ecfc1-cc78-4ecc-a90a-0362685062ce
    internal-label: AI Tools
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
* Apply surgical fixes one pattern at a time, on a dedicated Git branch, or in place if the project is not a Git repository, with every change verified by a compile before you review it.
<!-- Owner review: NOT FOUND AS WRITTEN (no marker comment from Alexandru). "on a dedicated Git branch" is unconditional, but the skill also edits in place when the project is not a Git repository (runbook.md "Git vs in-place"; git-workflow.md). Suggest: "...on a dedicated Git branch, or in place if the project is not a Git repository, with every change verified by a compile before you review it." -->

Describe the issue, and the skill routes the request to the appropriate remediation workflow.

## How the Skill Works {#how-the-skill-works}

The skill works in two phases. Keeping them separate lets you review every finding before any code changes, and lets you commit each type of fix independently.

|Phase|What happens|Changes code|
|---|---|---|
|**Review**|The skill runs its detectors across the project and returns a report of findings, grouped by pattern and ordered by severity, with a planned action for each finding.|No|
|**Apply**|You select one pattern. The skill reads that pattern's remediation recipe, shows a plan, and waits for your confirmation. It then makes the edits and verifies them with a compile.|Yes, on a new Git branch, or in place if the project is not a Git repository. The skill never commits, pushes, or opens a pull request.|

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: Apply row (plan shown and confirmation required before edits, in-place editing outside Git, never opens a pull request). -->
<!-- Owner review: CONFIRMED. Source: references/runbook.md Steps 7-8 (explicit "yes" required, declining = aborted), references/git-workflow.md ("does not commit, push, or open PRs"). No change needed. -->

If a prompt does not make clear whether you want a report or a fix, the skill reports first and then asks whether to apply the changes.

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. -->
<!-- Owner review: CONFIRMED. Source: references/runbook.md "User intent: report vs apply" (ambiguous discover prompts: report first, then ask "Apply these changes?"). No change needed. -->

The skill is organized as a main skill that routes each request to an expert sub-skill for one pattern. Each sub-skill contains the recipe for its pattern, including the conditions under which a fix must be skipped. Detection uses a deterministic analyzer that parses your workspace locally. For deprecated APIs, a preflight step first loads the current list of AEM deprecations, because that list changes over time.

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: detection uses a deterministic analyzer that parses the workspace locally. -->
<!-- Owner review: CONFIRMED. Source: SKILL.md "Findings sources" (scripts/analyze.sh parses once, runs detectors); remove-deprecated-api/scripts/detect.sh preflight. No change needed. -->

## Supported Checks {#supported-checks}

Each check is a pattern with its own identifier, which you can use in your prompts. The report orders findings by the severity of their pattern. More patterns are added over time.

|Pattern|What it detects and fixes|Severity|Fix type|
|---|---|---|---|
|`remove-deprecated-api`|Usage of Java APIs that are [deprecated or removed](/help/release-notes/deprecated-removed-features.md) in AEM as a Cloud Service, such as Google Guava (`com.google.common.*`), along with deprecated Maven dependencies and unmodifiable OSGi configurations. After an API reaches its removal date, its usage fails the Cloud Manager pipeline. The skill replaces each usage with its documented successor where one is available and safe, and reports the rest as manual action.|High|Guided|
|`inject-in-sling-model`|`@Inject` fields in Sling Model (`@Model`) classes. The skill migrates them to injector-specific annotations.|High|Mechanical|
|`outbound-call-timeouts`|Outbound HTTP clients built without connect, read, or connection-pool timeouts, in Apache HttpClient, OkHttp, and the JDK HTTP client. A slow downstream service can otherwise hold a request thread indefinitely. The skill adds bounded timeouts, reusing timeout configuration that already exists in the file.|High|Mechanical|
|`unbounded-query`|Explicitly unbounded queries, such as the `p.limit=-1` Query Builder predicate or `setLimit(-1)`. Unbounded queries are a common cause of out-of-memory outages. The skill caps the result set where that is provably safe, and otherwise asks for a pagination decision.|High|Guided|
|`tuning-oak-query-indexes`|JCR and Oak queries that are not served by an index, and index definitions that are subtly misconfigured. The skill proposes the property or Lucene index-definition change. It needs the index definition and defers the finding if you do not supply it.|High|Guided|
|`scheduler`|Usage of the Sling Commons `Scheduler` API and Sling Commons Scheduler `Job` implementations. The skill migrates them to scheduler configuration through OSGi properties or to Sling Jobs, which are compatible with AEM as a Cloud Service.|High|Guided|
|`resource-change-listener`|JCR `EventListener` implementations and OSGi `EventHandler` implementations for resource topics. The skill migrates them to a lightweight `ResourceChangeListener` that hands processing to a `JobConsumer`. Listeners that already follow this pattern are reported as compliant.|High|Guided|
|`event-migration`|OSGi `EventHandler` implementations that run business logic inline for other topics, such as replication or workflow events. The skill splits them into a lightweight `EventHandler` and a `JobConsumer`, with leader-only execution where needed.|High|Guided|
|`replication`|Usage of the CQ `Replicator` API and Sling replication agents. The skill migrates it to the Sling Distribution API.|High|Guided|
|`asset-manager`|DAM `AssetManager` methods for creating, uploading, and deleting assets that are not available in AEM as a Cloud Service. The skill migrates uploads to direct binary access and deletions to supported APIs.|High|Guided|
|`outdated-dependencies`|Versioned Maven dependencies from a default allowlist, such as `aem-sdk-api` and Mockito. The skill updates them to target versions that you supply. It does not look up the latest versions online.|Medium|Mechanical|

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the full rows for inject-in-sling-model, tuning-oak-query-indexes, scheduler, event-migration, replication, and asset-manager; the Severity and Fix type columns; deprecated Maven dependencies and unmodifiable OSGi configurations (remove-deprecated-api); OkHttp (outbound-call-timeouts); the p.limit=-1 predicate (unbounded-query); the EventListener and EventHandler migration description (resource-change-listener); no online version lookup (outdated-dependencies). -->
<!-- Owner review: MOSTLY CONFIRMED, 3 wording fixes. Severity/fix type match references/patterns.md; Maven deps + unmodifiable OSGi configs (remove-deprecated-api/recipe.md Category C), OkHttp, p.limit=-1 are correct. FIX (a) replication: the target is the "Sling Distribution API" (Distributor + SimpleDistributionRequest, replication/SKILL.md:11), not "Sling Content Distribution API". FIX (b) scheduler: the detector matches `implements org.apache.sling.commons.scheduler.Job` and the Scheduler API (scheduler/SKILL.md:54-60); "Sling `Job` implementations" is ambiguous - say "Sling Commons Scheduler `Job` implementations". FIX (c) outdated-dependencies: by default only com.adobe.aem:aem-sdk-api and org.mockito:* are checked unless --all is passed (outdated-dependencies/SKILL.md:49-55); say "versioned Maven dependencies from a default allowlist, such as aem-sdk-api and Mockito". -->

Mechanical fixes are deterministic edits that the skill applies directly. Guided fixes need a judgment call, so the skill walks you through each decision. The skill also provides guidance for the HTL build warning about redundant constant value comparisons in `data-sly-test`.

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: HTL data-sly-test guidance. -->
<!-- Owner review: CONFIRMED. Source: SKILL.md hints table + references/data-sly-test-redundant-constant.md. No change needed. -->

Patterns that are planned but do not have a detector yet are listed under [Limitations](#limitations).

## Before You Begin {#before-you-begin}

Make sure the following are in place:

* The `code-assessment` skill is installed for your AI coding agent. See [Install Skills](/help/ai-in-aem/local-development-with-ai-tools.md#install-skills).
* A local JDK, Java 11 or later, is available. The analyzer runs on it, and detection stops if no JDK is found.
  <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. -->
  <!-- Owner review: CONFIRMED. Source: runbook.md Step 4 (JDK 11+, stops with a clear message), SKILL.md "Critical rules". No change needed. -->
* Your AEM as a Cloud Service project is a Maven project that builds locally. The skill compiles the project before and after it makes changes. If the baseline build fails, the skill can still apply fixes, but it marks them as unverified. The skill asks you to confirm before applying.
  <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: applying fixes after a failed baseline and marking them as unverified. -->
  <!-- Owner review: MINOR WORDING GAP. Substance is right: runbook.md Step 5 requires an explicit "yes" acknowledging the edits will be UNVERIFIED for ANY failed baseline (apply is not blocked). The doc omits that confirmation step. Suggest adding: "The skill asks you to confirm before applying." Note for skill owners: runbook.md Step 9 only defines the terminal status `applied-unverified` for baseline_reason `toolchain-jdk-lombok` and `missing-private-repo`, so the skill spec is ambiguous for `other`; keep the doc general until that is resolved. -->
* For the `remove-deprecated-api` pattern only, your machine can reach Maven Central. The skill also uses Experience League as an optional fallback source for that pattern. All other patterns run entirely in your local workspace, with no network calls. If you are offline, the skill skips `remove-deprecated-api` and tells you why.
  <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: Maven Central requirement, no network calls for other patterns, offline behavior. -->
  <!-- Owner review: CONFIRMED. Source: SKILL.md "Critical rules" (documented exception for remove-deprecated-api: Maven Central + optional Experience League; offline = that pattern skipped). No change needed. -->

Using Git is recommended but not required. In a Git repository, the skill isolates each pattern's changes on a new branch, and starting from a clean working tree keeps each fix in its own diff. Outside Git, the skill edits files in place, and you review and revert changes in your IDE.

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: Git not required, in-place editing outside Git. -->
<!-- Owner review: CONFIRMED. Source: runbook.md "Git vs in-place" (dirty tree = warning only; in_place edits files directly). No change needed. -->

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

To assess specific files, name them in the prompt. The skill then analyzes only those files.

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. -->
<!-- Owner review: CONFIRMED. Source: runbook.md Step 3 ("with_findings": pass named paths via analyze.sh --files). No change needed. -->

During a whole-project review, the skill typically:

1. Classifies the request and selects the detectors to run. A broad prompt runs all detectors in report-only mode.
1. Runs a deprecated-API preflight against the latest AEM SDK using the [AEM as a Cloud Service SDK Build Analyzer Maven Plugin](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/developing/archetype/build-analyzer-maven-plugin), and compiles the project to establish a baseline. Depending on your AI coding agent, long-running steps can run in the background while the agent reads your source code, OSGi configurations, and content packages.
   <!-- Owner review: NOT FOUND IN SKILL (no marker comment from Alexandru). The skill source does not state that long-running steps run in the background (runbook.md Steps 4-5 just run java -version and mvn compile). Likely agent/IDE behavior, not a skill guarantee - suggest removing the sentence "Long-running steps can run in the background while the agent reads your source code, OSGi configurations, and content packages." unless the demo videos show it. -->
1. Runs the analyzer and reads the remediation recipe for each pattern that it found.
1. Confirms the facts that determine each planned action, as defined by the pattern's recipe.
   <!-- Owner review: NOT FOUND IN SKILL (no marker comment from Alexandru). runbook.md Step 3/6 only validates analyzer findings against the live file and applies each pattern's Resolution contract; generic caller analysis is not a skill step. Only individual recipes ask this (e.g. unbounded-query/recipe.md checks cross-method consumption; remove-deprecated-api removes unused code). Suggest rewording to "Confirms the facts that determine each planned action, as defined by the pattern's recipe." -->
1. Writes a run log to `.autofix/last-run.json` in the project and returns the report inline. The `.autofix` folder contains its own `.gitignore` file, so the run log is not committed with your code.
   <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the .autofix folder's own .gitignore file. -->
   <!-- Owner review: CONFIRMED. Source: git-workflow.md ("writes .autofix/.gitignore containing `*`"). No change needed. -->

### Read the Report {#read-the-report}

The report uses the same sections in every run, so you can compare runs across sessions:

|Section|Content|
|---|---|
|**Run metadata**|The patterns audited, the invocation mode (`discover` for a project scan, `with_findings` for named files, or `with_findings_preresolved` when another tool supplies complete findings), the intent (`report` or `apply`), and the edit mode (`git` or `in_place`).|
|**Preflight**|The Git status and current branch, and any warnings.|
|**Compile (baseline)**|The result of compiling the project before any change. If the baseline fails, the report states the likely cause, such as a JDK mismatch or an unreachable private Maven repository, and warns that applied fixes cannot be verified.|
|**Discover warnings**|Warnings raised during the scan, for example files the analyzer could not parse, findings outside the workspace, ambiguous `pom.xml` matches, or detector errors. An empty list means that the scan raised no warnings.|
|**Candidates**|One table per pattern, ordered by severity. For each finding, the table shows the file and line, the code that was found, the planned action, and the target or reasoning for the fix.|
|**Summary counts**|The number of findings to apply and to skip, and the number of deferred items. Applied and skipped findings always add up to the total number of findings.|
|**Deferred**|Patterns that have no recipe yet, or that were not selected for the current session.|
|**Next step**|How to continue, for example by replying `apply` to make edits, or by naming files or versions to narrow the scope.|

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the same sections in every run; the with_findings invocation mode and in_place edit mode (Run metadata); the Preflight content (Git status, branch, warnings); the Compile (baseline) section and its failure causes. -->
<!-- Owner review: MOSTLY CONFIRMED, 2 minor wording fixes. Sections match the Step 7 template in runbook.md; failure causes match Step 5 (toolchain-jdk-lombok, missing-private-repo, other, no-maven-project). FIX: "Discover warnings" is not only unparseable files - it also carries discover-time checks (e.g. duplicate pom locator, runbook.md Step 3) and analyzer warnings such as unknown-pattern, outside-workspace, detector-error (scripts/analyzer/Analyze.java). Also the Invocation field can be `with_findings_preresolved` (git-workflow.md) when an upstream caller supplies complete {pattern, file, line, snippet} findings (not categorically the migration skill, which hands over (pattern, file) pairs). -->

Every finding has exactly one planned action: it is either applied or skipped. The skill never drops a finding silently. When it skips a finding, it states the reason so that you can decide whether to act on it yourself. Common skip reasons include:

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the skill never drops a finding silently. -->
<!-- Owner review: CONFIRMED. Source: SKILL.md "Critical rules" (skip with a reason, never silently drop), runbook.md Step 7 (apply + skipped == total). No change needed. -->

|Skip reason|Meaning|
|---|---|
|`needs-pagination`|Capping the query would silently truncate results that callers depend on. Decide on a pagination approach first.|
|`needs-user-target`|The skill needs you to supply a target version. For `aem-sdk-api`, align the version with the AEM SDK used by your Cloud Manager environment rather than assuming the latest version.|
|`already-compliant`|The code was flagged for review and verified as compliant. This is a pass, not a defect.|
|`manual-only: <reason>`|The fix requires a design decision, for example a Guava usage whose JDK replacement would change behavior.|
|`stale-finding`, or another pattern-specific reason such as `literal-not-found`|The skill could not find the exact code to change, for example because the file changed after the scan.|

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the manual-only: <reason> format and the unlocatable row. -->
<!-- Owner review: PARTLY CONFIRMED, wording fix. `manual-only: <reason>` is real (remove-deprecated-api/recipe.md 4e). `unlocatable` is only a report-level category (runbook.md Step 7 count invariant, git-workflow.md commit-message trailer), not an exact reason string; exact reasons are pattern-specific (`literal-not-found`, `property-missing`, `ambiguous-locator`, `inject-ambiguous-field`, `discovery-no-match`, `stale-finding`, `deprecated-import-not-found`, ...). Suggest rewording the row, e.g. "`stale-finding` / pattern-specific not-found reasons: the skill could not find the exact code to change, for example because the file changed after the scan". Also: the skill is inconsistent on `needs-user-target` (outdated-dependencies/SKILL.md:20) vs `needs-target` (runbook.md Step 7); the doc follows the pattern skill. Flagged to skill owners. -->

>[!NOTE]
>
>If a pattern returns no findings, it means that the detectors found no matches. It does not mean that the project is free of every issue. See [Limitations](#limitations).

## Apply Fixes {#apply-fixes}

Ask the skill to fix one pattern at a time. The skill declines requests to fix every pattern at once. Applying one pattern per session keeps each change set focused on a single concern, so you can review it as one diff and revert it atomically if needed.

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the skill declines requests to fix every pattern at once. -->
<!-- Owner review: CONFIRMED. Source: SKILL.md "One pattern per session" ("Refuse 'fix everything' for the apply phase"). No change needed. -->

```
apply unbounded-query
```

When you apply a pattern, the skill:

1. Reads the pattern's sub-skill and recipe in full before making any edit.
1. Shows a plan and waits for your explicit confirmation. If you decline, no files change.
   <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. -->
   <!-- Owner review: CONFIRMED. Source: runbook.md Step 7 (declined = status aborted) and git-workflow.md ("When to create the branch": only after the user confirms; declining creates no branch). No change needed. -->
1. In a Git repository, creates a branch named `autofix/<pattern>/<YYYY-MM-DD>-<short-hash>`, where the short hash is the first seven characters of the current commit. Outside Git, it edits files in place.
   <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the short hash being the first seven characters of the current commit, and in-place editing outside Git. -->
   <!-- Owner review: CONFIRMED. Source: git-workflow.md "Branch naming" (autofix/<pattern-slug>/<YYYY-MM-DD>-<short-hash>, 7 chars of HEAD SHA; in_place = no branch). Note the date is UTC. No change needed. -->
1. Makes surgical edits to the affected files only, without reformatting or making unrelated changes. Mechanical fixes apply directly. Guided fixes walk you through each decision.
1. Verifies the change by compiling the project again. Some patterns also run the existing tests or re-run the detector. If the compile fails after a baseline that passed, the skill rolls back its edits. In a Git repository, it restores the files and deletes the branch. If the baseline already failed, the skill asks you to confirm before it applies the fix. It then keeps the edits but marks them as unverified, so build them in a working environment or CI before you merge.
   <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: automatic rollback, and keeping edits marked as unverified when the baseline already failed. -->
   <!-- Owner review: NEEDS QUALIFIER (minor). Rollback on a failed verify compile is correct (git-workflow.md "Rollback"). The "keeps edits, marked unverified when the baseline already failed" part matches runbook.md Step 9 for `toolchain-jdk-lombok` / `missing-private-repo`; for other baseline failures the skill spec is ambiguous (Step 5 says unverified, Step 9 does not define the terminal status). Suggest adding that the skill asks for confirmation before applying on a failed baseline; keep the wording general. -->
1. Updates the run log and returns a summary of what changed, why it chose that approach, the verification results, and any action it left for you.

Large fixes run in resumable batches of up to 40 files. The skill records its progress in the run log after each file, so a later session skips files that are already done. To continue with the next batch, reply `apply <pattern>`.

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the 40-file batch size and progress recorded after each file. -->
<!-- Owner review: CONFIRMED. Source: git-workflow.md "Resuming a large apply" (batch_cap default 40, checkpoint after each file, applied-partial, reply "apply <pattern>"). No change needed. -->

### Review and Commit the Changes {#review-and-commit}

The skill never commits, pushes, or opens a pull request. It leaves its edits uncommitted so that you can review them first.

<!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: never opens a pull request. -->
<!-- Owner review: CONFIRMED. Source: SKILL.md "Critical rules" (never commit, push, or open a PR), git-workflow.md. No change needed. -->

1. Review the changes. In a Git repository, review the working tree:

   ```bash
   git status
   git --no-pager diff
   ```

   Because nothing is committed yet, compare the working tree rather than running `git diff main...HEAD`. Outside Git, review the changed files that the summary lists in your IDE.
   <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: reviewing changed files in the IDE outside Git. -->
   <!-- Owner review: CONFIRMED. Source: runbook.md "Git vs in-place" handoff ("List modified paths; user reviews in IDE"). No change needed. -->

1. If the changes look right, stage and commit them yourself. The skill's summary suggests a commit message, for example `autofix: outbound-call-timeouts - bound outbound HTTP calls`.
1. Merge the branch through your usual review process, then run your Cloud Manager [code quality pipeline](/help/implementing/cloud-manager/code-quality-testing.md) to confirm compliance.
1. Apply the next pattern from the report.

## Example: Add Timeouts to Outbound Calls {#example-outbound-call-timeouts}

In this example, a project has two outbound HTTP calls that the review reported under `outbound-call-timeouts`:

* `InventoryServiceImpl`, an OSGi service that uses Apache HttpClient 4.x. One of its methods already builds a `RequestConfig` from OSGi-configured timeouts. A second method creates its client with `HttpClients.createDefault()`, which runs on effectively infinite connect and socket timeouts.
* `ProductFeedClient`, which uses the JDK `java.net.http` client. The client sets a connect timeout, but the JDK client has no client-level read timeout, so a feed that connects and then stalls holds the request thread indefinitely.

Enter the following prompt:

```
apply outbound-call-timeouts
```

The recipe's rule is to reuse a `RequestConfig` already present in a file rather than introduce a second one. In this example, the skill reuses the existing configuration instead of hard-coding the recipe's generic default values, here by extracting it into a helper method that both calls use. This keeps both calls honoring the timeouts configured for the environment:
<!-- Owner review: EXAMPLE OVERCLAIM. outbound-call-timeouts/recipe.md only requires reusing an existing RequestConfig/builder; extracting a shared helper method is one possible outcome, not guaranteed. Suggest: "In this example, the skill reuses the existing configuration, here by extracting it into a helper method." -->

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

The skill then compiles the project. In this run, it also ran the existing unit tests and re-ran the detector, which returned no remaining findings for the pattern. Only the compile is guaranteed for every pattern.
<!-- Owner review: EXAMPLE OVERCLAIM. Only the verification compile is mandatory (runbook.md Step 9). Running existing tests and re-running the detector are not guaranteed steps. The doc already says "In this run", but the Apply Fixes step 5 phrasing "Some patterns also run..." is the safe wording; consider the same hedge here or confirm with the demo run. -->

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

Before choosing a replacement, the skill checks which successors are resolvable on the module's classpath and how the module declares its dependencies. If a successor is not on the classpath, the skill adds a Maven dependency only with your consent, or reports the usage as a manual action. In this project, Apache Commons Collections4 is available only transitively through the AEM SDK, so the skill uses JDK-only replacements and adds no new dependency:
<!-- Owner review: CLARIFY. The classpath check is real (remove-deprecated-api/recipe.md successor-on-classpath verification), but if a successor is not on the classpath the skill adds a Maven dependency only with user consent, or records `successor-not-on-classpath` / manual action. JDK-only is this example's outcome, not a general rule. Same for the table intro (line ~59) "replaces each usage with its documented successor": some usages become manual-only (recipe.md 4e). Suggest "replaces each usage with its documented successor where one is available and safe, and reports the rest as manual action". -->

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

* **Detection is local static analysis.** The skill does not connect to a live AEM instance and cannot see runtime state. Behavior such as Sling Model adaptation and service user mappings still needs to be validated by deploying to a development environment. To inspect runtime behavior on your local SDK, use the [AEM Quickstart MCP Server](/help/ai-in-aem/local-development-with-ai-tools.md#aem-quickstart-mcp-server).
  <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. Applies to: the skill does not connect to a live AEM instance. -->
  <!-- Owner review: CONFIRMED. Source: SKILL.md "Scope & limitations" (no live AEM instance, local static detection only). No change needed. -->
* **Some anti-patterns are planned but do not have a detector yet.** These include unclosed `ResourceResolver` or JCR `Session` objects, thread and lock contention, and heavy work in `@PostConstruct` methods. Others are in-process image processing, unbounded recursion, unbounded GraphQL queries, and logging in loops. The agent may still mention them as observations, but the absence of a finding is not a clean bill of health.
* **Some fixes need your input.** Findings that require a design decision, a pagination strategy, or a target dependency version are skipped with a stated reason rather than fixed automatically.

## Related Resources {#related-resources}

* [Local Development with AI Tools](/help/ai-in-aem/local-development-with-ai-tools.md)
* [AI-Assisted Code Migration to AEM as a Cloud Service](/help/journey-migration/cloud-migration-skill/overview-cloud-migration-skill.md), whose migration skill hands individual findings to the `code-assessment` skill for transformation
  <!-- Alexandru: from the public source and not in the preso videos, to confirm if accurate. -->
  <!-- Owner review: CONFIRMED. Source: migration/SKILL.md:22 (hands the identified pattern + file to code-assessment/<pattern>/SKILL.md for transformation); code-assessment SKILL.md "Invocation from the migration skill". No change needed. -->
* [Deprecated and Removed Features and APIs](/help/release-notes/deprecated-removed-features.md)
* [Code Quality Testing](/help/implementing/cloud-manager/code-quality-testing.md)
* [Development Agentic Capabilities](/help/ai-in-aem/agentic-capabilities/brand-experience/development/use-cases.md), for troubleshooting failed Cloud Manager pipelines with AI
* [adobe/skills repository](https://github.com/adobe/skills/tree/main/plugins/aem/cloud-service)

Feel free to email [aemcs-ai-ide-tools-feedback@adobe.com](mailto:aemcs-ai-ide-tools-feedback@adobe.com) with feedback to help shape product development.
