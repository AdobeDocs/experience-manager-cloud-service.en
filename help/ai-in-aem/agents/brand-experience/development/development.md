---
title: Development Agent Overview
description: Learn how the Development Agent in AEM analyzes failed pipelines in Cloud Manager and build logs to suggest code fixes and speed up debugging; also how to retrieve Cloud Manager information, replication failure help, and how to set quiet hours and update free periods for AEM updates.
feature: Agentic AI, AI Assistant, AI Tools, User Roles
role: User, Admin, Developer
exl-id: 2194556f-aac2-4cdd-8f7f-00c92c8c4424
---

# Development Agent Overview {#development-agent-overview}

[As part of the Brand Experience Agent,](/help/ai-in-aem/agents/brand-experience/overview.md) the Development Agent helps traditional AEM Java-stack developers and administrators create, debug, deploy, and optimize code more efficiently.

It supports the following jobs, which are accessible through the AI Assistant's conversational interface.

* Cloud Manager Job: read-only operations, including listing of programs and environments, and pipeline status
* Pipeline Troubleshooting Job: debug failed pipelines
* Quiet Hours and Update Free Periods Management Job (Limited Availability): view, create, and edit Quiet Hours and Update Free Periods
* Replication Troubleshooting Job (Beta): debug replication-related issues such as blocked queues.

>[!NOTE]
>
> Developers will also find these AI-powered features useful:
> * [IDE Agent Skills](/help/ai-in-aem/local-development-with-ai-tools.md#agent-skills) for local development scenarios such as generating AEM components.
> * [Local MCP servers](/help/ai-in-aem/local-development-with-ai-tools.md#aem-quickstart-mcp-server) for local development, particularly debugging AEM and dispatcher issues.
> * [Remote MCP servers](/help/ai-in-aem/mcp-support/using-mcp-with-aem-as-a-cloud-service.md) for accessing APIs and AEM agents.

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses. 
>
>See also [Adobe Experience Cloud Generative AI User Guidelines](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html).

You can email development agent–specific feedback to [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com).

## Cloud Manager Job {#cloud-manager-job}

Find information about your AEM programs and environments, including:
* listing programs and environments
* listing environment variables
* finding the names of pipelines and current execution status and step details
* retrieving links to logs that can be downloaded

### Sample prompts {#sample-cm-job-prompts}


| Prompt | Result |
| --- | --- |
| *List all my AEM Cloud Service programs* | Lists programs that you have access to. |
| *Get details for program 12345* | Retrieve details about the program. |
| *List environments in program 12345* | Lists environments in the program. |
| *Get logs for the production environment* | Retrieves links to various AEM, dispatcher, and CDN log files so they can be downloaded for debugging or other purposes. |
| *list pipelines for program 12345* | List pipelines in the program. |
| *What's the status of the current pipeline execution?* | Responds with status of the pipeline. |
| *Get me the build log links for pipeline execution 12345* | Retrieves links to pipeline build logs for a specific pipeline execution. |


## Quiet Hours and Update Free Periods Management Job {#control-updates-job}

>[!AVAILABILITY]
>
>This feature is in a Limited Availability phase and will be rolled out over the next few weeks. Email [aem-devagent@adobe.com.](mailto:aem-devagent@adobe.com) for immediate access.

View, create, and edit Quiet Hours and Update Free Periods directly through the AEM AI Assistant.

The key benefit is fewer scheduling errors. As you make a request, the assistant guides you through what is possible and flags the limits that apply, such as the three-period cap, the mandatory one-week gap between periods, and the planned maintenance exclusion windows you cannot schedule over. 

So instead of discovering a constraint after a failed configuration, Business Owners and Deployment Managers are steered to a valid schedule in the same conversation. This protects critical business windows from automatic maintenance updates while reducing back-and-forth and misconfiguration.

### Sample prompts {#sample-updates-prompts}

| Prompt | Result |
| --- | --- |
| *What's the current update schedule for program 12345?* | Results in a listing of the current AEM update rules. |
| *Block AEM updates from 9 AM to 5 PM EST for program 12345* | Sets up a rule so AEM updates aren't applied during standard work hours. |
| *Remove the daily update block for program 12345* | Removes the rules preventing AEM updates. |
| *Pause AEM updates starting in two weeks for program 12345* | Creates a rule to prevent AEM updates. |
| *My program keeps getting updated at inconvenient times. What options do I have?* | Responds with information about how to set rules to control the AEM update schedule. |



## Pipeline Troubleshooting Job  {#cloud-manager-pipeline-troubleshooting}

This job can retrieve pipeline statuses and help you troubleshoot failing build steps by suggesting fixes, saving time when debugging AEM as a Cloud Service deployments to development, stage, and production environments. It examines build logs and related code to recommend a fix that you can apply manually. 

>[!VIDEO](https://video.tv.adobe.com/v/3478006?quality=12&learn=on)

>[!NOTE]
>
>Pipeline Troubleshooting is limited to Full Stack pipelines (Deployment and Code Quality), and Web Tier Config Pipeline.

<!--
To access this agent, please refer to the [release notes](/help/release-notes/release-notes-cloud/release-notes-current.md#aem-beta-programs) for instructions on how to enroll in the beta program, being sure to indicate your interest in the  Development Agent. You can also email development agent–specific feedback to [aem-devagent@adobe.com.](mailto:aem-devagent@adobe.com)

-->

[Follow along a tutorial](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/ai/agents/development-agent-troubleshoot-ci-cd-pipeline) to learn how to use the Development Agent to troubleshoot pipeline failures.

### Access the Development Agent through Cloud Manager {#how-to-access-the-agent}

You access the Development Agent through the AI Assistant found in user interfaces including Cloud Manager or Experience Hub.

1. To get started, click [Adobe Experience Cloud](https://experience.adobe.com/#/@foundationinternal/home) to open its home page.

    ![Adobe Experience Cloud home page](/help/implementing/cloud-manager/assets/experience-cloud-experiencemanager.png)

1. In the left rail, under the **Services** heading, click **Cloud Manager**.

    ![The drop-down list showing the Content Author preset is selected](/help/implementing/cloud-manager/assets/experience-hub-role-selection.png)

    >[!IMPORTANT]
    >
    >The widgets, tools, and artifacts shown depend on the user persona, entitlements, and AEM deployment type (AEM as a Cloud Service or Managed Services 6.5/6.5 LTS).

1. In the left rail, under **Program**, click **![Overview icon](/help/implementing/cloud-manager/configuring-pipelines/assets/overview.svg) Overview**.

1. On the **Program Overview** page, in the **Pipelines** card, click a pipeline.

    ![Selected pipeline](/help/ai-in-aem/agents/brand-experience/development/assets/dev-agent-pipeline-select.png)

1. In the **Build and Code Scanning** page, note the failed pipeline.

    ![Pipeline failure as seen in the Build and Code Scanning page](/help/ai-in-aem/agents/brand-experience/development/assets/dev-agent-pipeline-failure.png)

1. Near the upper-right corner of the AEM user interface (either from Cloud Manager pages or the author instance of the AEM environments), click the **AI Assistant** icon.

    ![AI Assistant icon on the toolbar](/help/implementing/cloud-manager/assets/ai-assistant-icon.png)

    See also [AI Assistant in AEM](/help/implementing/cloud-manager/ai-assistant-in-aem.md).

1. In the **AI Assistant** panel text box near the bottom, type your question or prompt, then press `Enter` or click ![Send icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Send_18_N.svg).

    For example:
    *In the "eda-org-01-no-access" program, analyze the failure to the "no-access" pipeline and troubleshoot.*

    The prompt results in the following response.

    ![AI Assistant prompt and resulting response](/help/ai-in-aem/agents/brand-experience/development/assets/dev-agent-prompt-response.png)

#### Troubleshoot directly from a failed pipeline execution {#troubleshoot-with-ai-button}

When a pipeline execution fails, Cloud Manager also surfaces a **Troubleshoot with AI** button directly on the pipeline execution page. This is the fastest way to start a troubleshooting session because the failed execution is automatically passed as context to the AI Assistant — no manual prompt entry is required.

1. In Cloud Manager, open the failed pipeline execution. The status banner displays **Failed** and the **Troubleshoot with AI** button appears near the upper-right corner of the page.

    ![Failed pipeline execution page showing the Troubleshoot with AI button and the AI Assistant panel with a pre-loaded analysis](/help/ai-in-aem/agents/brand-experience/development/assets/dev-agent-troubleshoot-button.png)

1. Click **Troubleshoot with AI**.

    The AI Assistant panel opens on the right side of the screen. The assistant automatically references the failed pipeline execution and begins its analysis, identifying the failing step and suggesting a fix you can apply manually.

1. Review the response and, if needed, continue the conversation in the **AI Assistant** text box to ask follow-up questions or request more detail.

### Permissions {#permissions}

The pipeline troubleshooting job requires either the Cloud Manager - Developer role or the Cloud Manager - Program Manager role.

### Sample prompts {#sample-pipeline-prompts}

| Prompt | Result |
| --- | --- |
| *Troubleshoot my failed pipeline* | Performs an analysis of why a pipeline failed; if it is unclear which pipeline is being referred to, additional questions will be asked to the user.|
| *List my failed pipelines for program Main Program.* | While results may vary, this prompt outputs a table of failed pipelines, with a follow-up suggestion to reference a specific pipeline to analyze. |
| *Analyze my failed pipeline called "Dev Pipeline."* | This prompt results in an analysis of the failed pipeline with suggestions to fix. If there are multiple failures, additional questions will be asked of the user. |
| *Troubleshoot pipeline execution 1234567* | By providing an exact pipeline execution id, a pipeline analysis is performed. |

### Out-of-scope features {#out-of-scope-features}

Pipeline troubleshooting operates on the Build & Unit Testing step and Code Scanning step in Full Stack Deployment and Code Quality pipelines. It also supports [web tier config pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md#web-tier-config-pipelines). 

For other pipeline types and steps, debug failures by downloading and inspecting the logs. See [Access and Download Logs](/help/implementing/cloud-manager/manage-logs.md) for more information.



## Replication Troubleshooting Job (Beta) {#replication-troubleshooting-job}

Debug replication-related issues such as blocked queues.

Please email [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com) for access to the beta program.
