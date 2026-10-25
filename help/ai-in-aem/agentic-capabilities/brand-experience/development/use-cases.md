---
title: Development Agentic Capabilities Overview
description: Learn how the Development Agentic Capabilities in AEM help your traditional AEM Java-stack developers and administrators create, debug, deploy, and optimize code more efficiently.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: f2d27a5f-0d67-4d85-8a24-86a8d8a3574b
    internal-label: Developer tools
  - id: ac5ecfc1-cc78-4ecc-a90a-0362685062ce
    internal-label: AI Tools
subfeature_v2:
  - id: f88183b7-5ea5-436c-ac46-96b53f0281ea
    internal-label: Edge Delivery Services
  - id: f1710108-e0d1-47e5-9952-1888729a03da
    internal-label: Agentic AI
role_v2:
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Development Agentic Capabilities {#development-agentic-capabilities}

The Development Agentic Capability of Adobe Experience Manager (AEM) as a Cloud Service collaborates with [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview) to help traditional AEM Java-stack developers and administrators create, debug, deploy, and optimize code more efficiently.

## Use Cases {#use-cases}

A range of use-cases are covered.

### Manage Cloud Manager Pipelines {#aem-cloud-manager-pipeline-management}

The AEM Cloud Manager Pipeline Management skill lets you manage your CI/CD pipelines directly through natural language, without switching between Cloud Manager screens to find the information or controls you need. You can list and create pipelines, kick off or cancel executions, and check status and history — all from a single conversation.

When something goes wrong, the skill goes beyond status checks: it can retrieve step metrics, logs, artifacts, and execution failures so you can diagnose an issue without downloading and searching through raw log files yourself. It also handles day-to-day pipeline configuration — managing pipeline variables, invalidating cached artifacts, and adjusting pipeline settings — so routine maintenance tasks that used to require several clicks through the UI can be done with a single request.

To find out why an execution failed, see [AEM Cloud Manager Pipeline Troubleshooting](#aem-cloud-manager-pipeline-troubleshooting).

AI can make mistakes so review suggested actions before applying them, particularly for destructive operations.

| Capability | Sample Prompts |
| --- | --- |
| Listing pipelines | "List pipelines for program 12345"<br><br>"What pipelines do I have in Main Program?" |
| Creating pipelines | "Create a new Full Stack pipeline for program 12345"<br><br>"Set up a Code Quality pipeline for my dev environment" |
| Executing a pipeline | "Run the Dev Pipeline"<br><br>"Start execution for pipeline 67890" |
| Canceling a running pipeline step | "Cancel the current build step on Dev Pipeline"<br><br>"Stop the running Code Scan step for execution 12345" |
| Viewing execution history and status | "What's the status of the current pipeline execution?"<br><br>"Show me the last 5 executions of Dev Pipeline" |
| Getting step metrics | "Show me the build step metrics for execution 12345"<br><br>"How long did the Code Scan step take on my last run?" |
| Getting logs | "Get me the build log links for pipeline execution 12345"<br><br>"Pull the logs for the failed Code Scan step" |
| Getting artifacts | "Show me the artifacts produced by execution 12345"<br><br>"Where can I download the build artifact from my last run?" |
| Getting execution failures | "Why did my Dev Pipeline execution fail?"<br><br>"List all failed executions for program 12345 this week" |
| Managing pipeline variables | "Show me the variables for Dev Pipeline"<br><br>"Update the API_ENDPOINT variable on pipeline 67890" |
| Invalidating cached artifacts | "Invalidate the cached artifact for Dev Pipeline"<br><br>"Clear the build cache before my next run" |
| Configuring pipeline settings | "Enable email notifications for Dev Pipeline"<br><br>"Change the trigger branch for pipeline 67890 to release" |

### AEM Cloud Manager Pipeline Troubleshooting {#aem-cloud-manager-pipeline-troubleshooting}

The AEM Cloud Manager Pipeline Troubleshooting skill helps you find out why a pipeline execution failed, without downloading and searching through raw log files yourself. Reference a failed execution by pipeline name or execution ID, and the skill confirms the failure in Cloud Manager, identifies the failed step, and explains in plain language what went wrong, why, and what to do next. If your request matches more than one pipeline, the skill asks you to choose one before it continues.

Note that this capability is implemented as a specialist agent and so does not visually appear as a listed skill in the Coworker Customizations interface.

The skill investigates failures in the following pipelines and steps:

* The Build & Unit Testing step and the Code Scanning step in full-stack Deployment and Code Quality pipelines.
* Build and code quality failures in [web tier config pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines), such as Dispatcher configuration validation errors.
* Deployment failures in [config pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#config-deployment-pipeline), such as an invalid CDN configuration.

For failures in other steps, such as the deployment step of a full-stack pipeline, the skill reports the failed step without diagnosing it. In that case, inspect the logs as described in [Access and Download Logs](/help/implementing/cloud-manager/manage-logs.md), or contact Adobe Support.


You can also start troubleshooting without writing a prompt. Click **Troubleshoot with AI** on a failed pipeline execution in Cloud Manager, or in the **Failed Pipelines** widget on the Experience Manager home page, to open Coworker with that execution already referenced. See [Troubleshoot a Failed Pipeline from Cloud Manager](#troubleshoot-from-cloud-manager) and [Troubleshoot from the Failed Pipelines Widget](#troubleshoot-from-experience-home-widget).

AI can make mistakes so review the diagnosis before acting on it.

| Capability | Sample Prompts |
| --- | --- |
| Troubleshooting a failed pipeline | "Troubleshoot my failed pipeline"<br><br>"Help me troubleshoot the last pipeline that failed in Main Program" |
| Troubleshooting a specific execution | "Troubleshoot pipeline execution 1234567"<br><br>"Troubleshoot execution 1234567 of Dev Pipeline in program 12345" |
| Troubleshooting web tier and config pipelines | "Debug my web tier build failure on pipeline 67890"<br><br>"Why did my config pipeline deployment fail in program 12345?" |

#### Permissions {#pipeline-troubleshooting-permissions}

To use the AEM Cloud Manager Pipeline Troubleshooting skill, you must have either the **Developer** or the **Program Manager** role in Cloud Manager. See [Role-based permissions](/help/onboarding/cloud-manager-introduction.md#role-based-permissions).

#### Troubleshoot a Failed Pipeline from Cloud Manager {#troubleshoot-from-cloud-manager}

Starting from the failed pipeline execution is the fastest way to troubleshoot, because Coworker receives the execution as context and you do not have to write a prompt.

1. Sign in to [Adobe Experience Cloud](https://experience.adobe.com), then open **Experience Manager**.

    ![Experience Manager home page, showing the Ask Coworker anything box and Cloud Manager in the left rail](/help/ai-in-aem/agentic-capabilities/brand-experience/development/assets/dev-ac-experience-manager-home.png)

    >[!TIP]
    >
    >To troubleshoot without opening Cloud Manager, type a prompt such as *Troubleshoot my failed pipeline* in the **Ask Coworker anything** box on this page.

1. In the left rail, click **Cloud Manager**, then select your program.

1. On the **Program Overview** page, in the **Pipelines** card, click the pipeline that failed.

    ![Program Overview page in Cloud Manager, showing the Environments and Pipelines cards](/help/ai-in-aem/agentic-capabilities/brand-experience/development/assets/dev-ac-program-overview-pipelines.png)

1. On the pipeline execution page, note the **Failed** status next to the pipeline name, and the step that failed.

    ![Pipeline execution page in Cloud Manager, showing a failed Artifact Preparation step](/help/ai-in-aem/agentic-capabilities/brand-experience/development/assets/dev-ac-failed-pipeline-execution.png)

1. Click **Troubleshoot with AI**. The button appears near the upper-right corner of the page and in the **Step errors** box of the failed step.

    ![Troubleshoot with AI buttons in the page header and in the Step errors box of a failed step](/help/ai-in-aem/agentic-capabilities/brand-experience/development/assets/dev-ac-troubleshoot-with-ai-button.png)

    Coworker opens in a panel on the right side of the page, with the failed execution referenced in the prompt. Coworker identifies the failed step, explains the root cause, and suggests a fix that you can apply manually.

    ![Coworker panel next to a failed pipeline execution, showing the root cause analysis](/help/ai-in-aem/agentic-capabilities/brand-experience/development/assets/dev-ac-coworker-troubleshooting-response.png)

1. Review the diagnosis. To ask follow-up questions or request more detail, type in the **Ask Coworker anything** box.

#### Troubleshoot from the Failed Pipelines Widget {#troubleshoot-from-experience-home-widget}

The Experience Manager home page includes a **Failed Pipelines** widget that lists pipeline failures across your programs, so you can start troubleshooting without first opening Cloud Manager. Each row shows the pipeline name, the date and time of the last run, the duration, and the step that failed, along with a **Troubleshoot with AI** button.

>[!NOTE]
>
>The **Failed Pipelines** widget appears only when the **Admin & IT** preset is selected. If you do not see the widget, select **Admin & IT** from the **Preset** list in the upper-right corner of the home page.

![Failed Pipelines widget on the Experience Manager home page, showing a failed pipeline with the Troubleshoot with AI button highlighted](/help/ai-in-aem/agentic-capabilities/brand-experience/development/assets/dev-ac-failed-pipelines-widget.png)

1. Sign in to [Adobe Experience Cloud](https://experience.adobe.com), open **Experience Manager**, then scroll to the **Failed Pipelines** widget.

1. In the row of the pipeline that you want to investigate, click **Troubleshoot with AI**.

    Coworker opens with the failed execution referenced and starts its analysis, identifying the root cause and suggesting a fix.

1. Review the diagnosis. To ask follow-up questions or request more detail, type in the **Ask Coworker anything** box.

### AEM Cloud Manager Environment Management {#aem-cloud-manager-environment-management}

The AEM Cloud Manager Environment Management skill lets you manage your Cloud Manager environments through natural language, without navigating through Cloud Manager's UI screens to find the right program, environment, or configuration panel. You can list your environments, pull up details on a specific one, and create, clone, or delete environments as your project needs change.

Day-to-day environment upkeep is covered too: managing environment variables, downloading logs for debugging, resetting a Rapid Development Environment (RDE) when you need a clean slate, and configuring region deployments — all from a single conversation instead of several trips through Cloud Manager. When something needs to be rolled back, the skill can also restore an environment from a backup.

AI can make mistakes so review suggested actions before applying them, particularly for destructive operations.

| Capability | Sample Prompts |
| --- | --- |
| Listing environments | "List environments for program 12345"<br><br>"Show me all environments in Main Program" |
| Getting environment details | "Get details for the stage environment in program 12345"<br><br>"What's the status of my production environment?" |
| Creating environments | "Create a new dev environment for program 12345"<br><br>"Set up a stage environment for testing" |
| Cloning environments | "Clone my production environment to a new dev environment"<br><br>"Duplicate the stage environment for program 12345" |
| Deleting environments | "Delete the old-dev environment in program 12345"<br><br>"Remove the unused test environment" |
| Managing environment variables | "Show me the variables for my dev environment"<br><br>"Set the API_BASE_URL variable on my stage environment" |
| Downloading environment logs | "Get me the logs for the production environment"<br><br>"Download the dispatcher logs for my stage environment" |
| Resetting RDE | "Reset my RDE"<br><br>"Reset the rapid development environment for program 12345" |
| Managing region deployments | "Add a new region deployment for program 12345"<br><br>"Show me the region deployments for my production environment" |
| Restoring from backup | "Restore my production environment from last night's backup"<br><br>"Show me available backups for the stage environment" |

### AEM Cloud Manager Program Management {#aem-cloud-manager-program-management}

The AEM Cloud Manager Program Management skill lets you look up and manage your Cloud Manager programs through natural language, instead of navigating Cloud Manager's program listings to find the one you are looking for. You can list all the programs you have access to, pull up details for a specific one, and delete a program when it is no longer needed.

Since programs are the umbrella that pipelines and environments live under, this skill also acts as a quick entry point into those related resources — you can ask it to show the pipelines or environments tied to a given program without first tracking down the program ID yourself.

AI can make mistakes so review suggested actions before applying them, particularly for destructive operations.

| Capability | Sample Prompts |
| --- | --- |
| Listing all programs | "List my Cloud Manager programs"<br><br>"What programs do I have access to?" |
| Getting program details | "Get details for program 12345"<br><br>"Show me information about Main Program" |
| Deleting a program | "Delete program 12345"<br><br>"Remove the old-demo program" |
| Showing pipelines for a program | "What pipelines are in program 12345?"<br><br>"List pipelines for Main Program" |
| Showing environments for a program | "Show me the environments in program 12345"<br><br>"What environments does Main Program have?" |

### AEM Cloud Manager Release Management {#aem-cloud-manager-release-management}

The AEM Cloud Manager Release Management skill lets you control when Adobe applies automated maintenance updates to your program, without digging through Cloud Manager settings to find the right screen. You can check your current update schedule, set a daily Quiet Hours window — a recurring time each day when Adobe pauses updates — and schedule a multi-day Update-Free Period around events like a product launch or a holiday freeze, when you do not want any changes landing on your environments.

If your plans change, you can remove an Update-Free Period just as easily as you scheduled it. The skill can also show you Adobe's own global Code-Freeze periods — the windows Adobe has already blocked off for planned maintenance exclusions — so you know upfront which dates are already off-limits before you try to schedule your own.

The skill also helps you avoid scheduling errors. As it guides you through a request, it flags the limits that apply, such as the maximum of three Update-Free Periods within a floating 365-day window, the mandatory one-week interval between periods, and Adobe's planned maintenance exclusion windows. Instead of discovering a constraint after a configuration fails, you reach a valid schedule in the same conversation. This approach protects critical business windows from automatic maintenance updates and reduces back-and-forth and misconfiguration. See [Quiet hours and Update free periods](/help/implementing/deploying/quiet-hours-update-free-periods.md).

AI can make mistakes so review suggested actions before applying them — this is especially true for update-schedule changes, since an incorrectly scheduled or removed Update-Free Period could allow updates to land during a window you meant to protect.

| Capability | Sample Prompts |
| --- | --- |
| Getting current update schedule settings | "What's my current Quiet Hours window?"<br><br> "Show me the update schedule for program 12345" |
| Configuring the daily Quiet Hours window | "Set Quiet Hours from 10pm to 6am for program 12345"<br><br> "Update my Quiet Hours window to start an hour earlier" |
| Scheduling an Update-Free Period | "Schedule an update-free period from Dec 20 to Jan 2"<br><br> "Block updates for program 12345 during launch week, March 3-10" |
| Removing an Update-Free Period | "Remove the update-free period for program 12345"<br><br> "Cancel the blackout window I scheduled for next week" |
| Viewing Adobe's global Code-Freeze periods | "When is Adobe freezing updates this quarter?"<br><br> "Show me Adobe's planned maintenance exclusion periods" |

### AEM Workflow Inspection {#aem-workflow-inspection}

The AEM Workflow Inspection skill lets you check on workflow activity in plain language. Ask Coworker which workflows are running, what's waiting in your inbox, or why a workflow failed, without opening the Workflow user interface.

You can look up a specific workflow, browse available workflow models, and ask follow-up questions as you troubleshoot. This skill is read-only: it helps you see and understand what's happening, but it doesn't start, change, or stop workflows.

AI can make mistakes, so review findings before acting on them.

| Use case | Sample prompts |
| --- | --- |
| Check workflow activity | "What workflows are running right now?"<br><br>"Are any workflows suspended?" |
| Get a status summary | "How many workflows are running, completed, suspended, or terminated?"<br><br>"Give me a quick breakdown of workflows by status." |
| Find workflows that need attention | "Are any running or suspended workflows visible to me showing recorded errors?"<br><br>"Summarize the errors found in the workflows you inspected." |
| Investigate workflow errors | "What diagnostic information is available for that workflow's error?"<br><br>"Explain the error on the second workflow in that list." |
| Recheck a workflow | "Check that workflow again. What error information is returned now?"<br><br>"Has its status or current step changed since we last checked?" |
| Inspect a specific workflow | "Show the content, status, and start time for the second workflow in that list."<br><br>"Who started it, when, and what work-item information is available?" |
| See what's waiting on me | "What's in my workflow inbox?"<br><br>"Show only workflow steps, not Tasks." |
| Discover workflow models | "What workflow models are available?"<br><br>"Is a model named Editorial Review available?" |

### AEM Dispatcher Insights {#aem-dispatcher-insights}

The AEM Dispatcher Insights skill helps you understand how your Dispatcher and Apache web tier handle requests in AEM as a Cloud Service. Ask Coworker to analyze cache performance, investigate traffic and delivery issues, and review security configuration without manually searching log files. Where supported by the available data, Coworker can present findings as charts and request-timing visualizations.

For environment-specific analysis, identify the environment and time period (within a seven-day log window) you want to investigate. Currently, the skill does not access your source repository so for configuration and code reviews, paste or upload the relevant files. Coworker can also inspect reachable URLs to check response status, headers, and redirects.

Across these topics, you can ask Coworker to propose changes, explain their potential impact, and provide validation and rollback guidance. After you apply and deploy a change, ask Coworker to reassess the available logs or live URL behavior.

ithin Cloud Manager's seven-day log window.

Currently, the skill does not modify your repository, deploy changes, publish or unpublish content, or clear caches. CDN cache purges, edge traffic-filter rule authoring, and changes to Adobe-managed infrastructure settings are outside its scope.

AI can make mistakes, so review findings and proposed changes before acting on them.

#### Caching and Performance {#dispatcher-caching-performance}

Understand cache effectiveness, investigate slow or stale responses, and identify opportunities to reduce requests to publish.

| Capability | Sample Prompts |
| --- | --- |
| Understanding cache health and trends | "Summarize Dispatcher cache performance for production today and compare it with yesterday."<br><br>"Cache performance dropped after our latest deployment. Compare the log evidence with recent deployments and the configuration diff I've shared." |
| Identifying cache misses and non-cacheable requests | "Which paths are missing or bypassing the cache, and where could we improve cacheability?"<br><br>"Review why these GraphQL persisted-query responses are not being cached." |
| Evaluating query-parameter caching | "Our cache hit ratio dropped after adding campaign tracking parameters. Review these cache rules."<br><br>"Which parameters can I safely ignore without breaking search or pagination?" |
| Reviewing cache headers and expiration policies | "Review these response headers and explain how browser, CDN, and Dispatcher caching interact."<br><br>"Recommend a caching policy for our versioned client libraries and DAM assets using the configuration I've shared." |
| Investigating content freshness and cache invalidation | "Why is this page still showing old content after publication? Review the logs and configuration I've shared."<br><br>"How would changing statfileslevel or gracePeriod affect invalidation, and when should we refresh a page's cache?" |
| Investigating slow responses | "Which paths have the slowest responses today?"<br><br>"For representative page requests, show the observed Dispatcher and publish processing stages and where time is spent." |
| Understanding post-deployment cache warm-up | "Our site is slow after deployments. What should we check about cache warm-up?"<br><br>"Check whether this page is included in our sitemap and explain how sitemap coverage affects warm-up." |

#### Traffic and Request Handling {#dispatcher-traffic-request-handling}

Understand the traffic reaching Dispatcher and investigate how requests are filtered, routed, and served.

| Capability | Sample Prompts |
| --- | --- |
| Analyzing traffic patterns and bots | "Which user agents and paths drove today's traffic increase?"<br><br>"Is automated traffic being absorbed by the cache, or increasing requests to publish?" |
| Investigating HTTP errors | "Investigate the intermittent 502 and 503 responses in production between 10:00 and 11:00 UTC today."<br><br>"Which paths account for today's 403 and 404 responses, and what evidence helps explain them?" |
| Understanding request filtering and endpoint routing | "Review these filter rules alongside the Sling servlet I've shared. Will the intended requests reach it?"<br><br>"Explain how rule ordering affects requests to our GraphQL endpoint." |
| Reviewing multi-site and hostname routing | "Review these vhosts and farms. Does each hostname map to the intended site?"<br><br>"Requests to our new domain are serving the wrong site. Check the host aliases and farm mappings I've shared." |
| Troubleshooting redirects, rewrites, and vanity URLs | "Inspect this URL's redirect chain and help explain the loop using the rewrite rules I've shared."<br><br>"This vanity URL works on publish but returns 404 through Dispatcher. What should I check?" |
| Reviewing header forwarding and handling | "Which request headers does this configuration forward to publish?"<br><br>"Explain which headers belong in clientheaders.any and which are handled in the vhost or cache configuration." |
| Inspecting environment and logging settings | "List the Cloud Manager environment variables for stage and explain the Dispatcher-related settings."<br><br>"How can I enable Dispatcher or rewrite debug logging in stage without changing production logging?" |

#### Security {#dispatcher-security}

Ask Coworker for an overall security review, or focus on a specific concern in your customer-controlled Dispatcher configuration and related AEM code.

| Capability | Sample Prompts |
| --- | --- |
| Checking sensitive-path exposure and least-privilege filters | "Check whether these rules could expose administrative or repository paths."<br><br>"Can this endpoint's allow rule be narrowed while preserving the required requests?" |
| Reviewing security headers | "Review these response-header settings for missing or ineffective security protections."<br><br>"Explain the security benefits and potential application impact of the Content-Security-Policy change you recommend." |
| Reviewing permission-sensitive caching | "Review this auth_checker configuration and permission-check servlet."<br><br>"What should we verify to prevent unauthorized access when caching authenticated content?" |
| Reviewing security in related AEM code | "Review these Sling servlets and filters for permission-checking issues."<br><br>"Review these OSGi CSRF and CORS configurations alongside the Dispatcher rules I've shared." |
| Performing an overall security review | "Review the Dispatcher configuration and related AEM code I've shared for security weaknesses."<br><br>"Prioritize the findings by severity and recommend improvements within our control in AEM as a Cloud Service." |
