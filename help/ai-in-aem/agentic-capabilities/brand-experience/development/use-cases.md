---
title: Development Agentic Capabilities Overview
description: Learn how the Development Agentic Capabilities in AEM help you accelerate your content creation and automatically orchestrate changes.
feature: Edge Delivery Services, Agentic AI
role: User, Admin, Developer
---

# Development Agentic Capabilities {#development-agentic-capabilities}

The Development Agentic Capability of Adobe Enterprise Manager (AEM) as a Cloud Service collaborates with [Coworker Chat](https://experienceleague.adobe.com/en/docs/cx-enterprise-ai/experience-cloud-ai/coworker/chat/overview) to help traditional AEM Java-stack developers and administrators create, debug, deploy, and optimize code more efficiently.

## Use cases {#use-cases}

A range of use-cases are covered.

### AEM Cloud Manager Pipeline Troubleshooting

The AEM Cloud Manager Pipeline Troubleshooting skill helps you get to the bottom of a failed pipeline execution without digging through raw logs yourself. Reference a failed pipeline and it investigates issues that occurred in the Build & Unit Testing step and the Code Scanning step in Full Stack Deployment and Code Quality pipelines. It also supports dispatcher configuration issues in web tier config pipelines. It explains what went wrong in plain language.

When a fix is identified with enough confidence, the skill can go a step further: it shows you the exact diff for review that you can download, and optionally pushes it to a new branch if you approve. 

Review the diagnosis and any proposed fix before acting on it — particularly before merging a pushed fix into your target branch.

| Capability | Sample Prompts |
| --- | --- |
| Troubleshooting a pipeline | Troubleshoot my failed pipeline. Troubleshoot pipeline execution 1234567. |
| Generating a fix (with a diff) | Generate a fix for my failed pipeline execution 1234567 |

### Manage Cloud Manager pipelines

The AEM Cloud Manager Pipeline Management skill lets you manage your CI/CD pipelines directly through natural language, without switching between Cloud Manager screens to find the information or controls you need. You can list and create pipelines, kick off or cancel executions, and check status and history — all from a single conversation.

When something goes wrong, the skill goes beyond status checks: it can retrieve step metrics, logs, artifacts, and execution failures so you can diagnose an issue without downloading and searching through raw log files yourself. It also handles day-to-day pipeline configuration — managing pipeline variables, invalidating cached artifacts, and adjusting pipeline settings — so routine maintenance tasks that used to require several clicks through the UI can be done with a single request.

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

### AEM Cloud Manager Environment Management

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

### AEM Cloud Manager Program Management

The AEM Cloud Manager Program Management skill lets you look up and manage your Cloud Manager programs through natural language, instead of navigating Cloud Manager's program listings to find the one you're after. You can list all the programs you have access to, pull up details for a specific one, and delete a program when it's no longer needed.

Since programs are the umbrella that pipelines and environments live under, this skill also acts as a quick entry point into those related resources — you can ask it to show the pipelines or environments tied to a given program without first tracking down the program ID yourself.

AI can make mistakes so review suggested actions before applying them, particularly for destructive operations.

| Capability | Sample Prompts |
| --- | --- |
| Listing all programs | "List my Cloud Manager programs"<br><br>"What programs do I have access to?" |
| Getting program details | "Get details for program 12345"<br><br>"Show me information about Main Program" |
| Deleting a program | "Delete program 12345"<br><br>"Remove the old-demo program" |
| Showing pipelines for a program | "What pipelines are in program 12345?"<br><br>"List pipelines for Main Program" |
| Showing environments for a program | "Show me the environments in program 12345"<br><br>"What environments does Main Program have?" |

### AEM Cloud Manager Release Management

The AEM Cloud Manager Release Management skill lets you control when Adobe applies automated maintenance updates to your program, without digging through Cloud Manager settings to find the right screen. You can check your current update schedule, set a daily Quiet Hours window — a recurring time each day when Adobe pauses updates — and schedule a multi-day Update-Free Period around events like a product launch or a holiday freeze, when you do not want any changes landing on your environments.

If your plans change, you can remove an Update-Free Period just as easily as you scheduled it. The skill can also show you Adobe's own global Code-Freeze periods — the windows Adobe has already blocked off for planned maintenance exclusions — so you know upfront which dates are already off-limits before you try to schedule your own.

AI can make mistakes so review suggested actions before applying them — this is especially true for update-schedule changes, since an incorrectly scheduled or removed Update-Free Period could allow updates to land during a window you meant to protect.

| Capability | Sample Prompts |
| --- | --- |
| Getting current update schedule settings | "What's my current Quiet Hours window?"<br><br> "Show me the update schedule for program 12345" |
| Configuring the daily Quiet Hours window | "Set Quiet Hours from 10pm to 6am for program 12345"<br><br> "Update my Quiet Hours window to start an hour earlier" |
| Scheduling an Update-Free Period | "Schedule an update-free period from Dec 20 to Jan 2"<br><br> "Block updates for program 12345 during launch week, March 3-10" |
| Removing an Update-Free Period | "Remove the update-free period for program 12345"<br><br> "Cancel the blackout window I scheduled for next week" |
| Viewing Adobe's global Code-Freeze periods | "When is Adobe freezing updates this quarter?"<br><br> "Show me Adobe's planned maintenance exclusion periods" |
