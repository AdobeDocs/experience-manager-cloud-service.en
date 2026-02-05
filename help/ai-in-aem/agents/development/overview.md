---
title: Development Agent Overview
description: Learn how the Development Agent in AEM analyzes failed pipelines in Cloud Manager and build logs to suggest code fixes and speed up debugging.
feature: Agentic AI, AI Assistant, AI Tools, User Roles
role: User, Admin, Architect, Developer
---

# Development Agent overview {#development-agent-overview}

The Development Agent helps AEM developers and administrators create, debug, deploy, and optimize code more efficiently.

Currently, the agent can retrieve pipeline statuses and help you troubleshoot failing build steps by suggesting fixes, saving time when debugging AEM as a Cloud Service deployments to development, stage, and production environments. It examines build logs and related code to recommend a fix that you can apply manually. 

>[!VIDEO](https://video.tv.adobe.com/v/3478006?quality=12&learn=on)

>[!IMPORTANT]
>
>AI-generated responses may be inaccurate or misleading. Be sure you double-check suggested fixes and responses. 
>
>See also [Adobe Experience Cloud Generative AI User Guidelines](https://www.adobe.com/legal/licenses-terms/adobe-dx-gen-ai-user-guidelines.html). 

<!-- 
## Cloud Manager Pipeline Troubleshooting  {#cloud-manager-pipeline-troubleshooting}
-->

To access this agent, refer to the [release notes](/help/release-notes/release-notes-cloud/release-notes-current.md#aem-beta-programs) for instructions on how to enroll in the beta program, and be sure to indicate your interest in the Development Agent. You can also email Development Agent–specific feedback to [aem-devagent@adobe.com](mailto:aem-devagent@adobe.com).

## Access the Development Agent through Cloud Manager {#how-to-access-the-agent}

You access the Development Agent through the AI Assistant found in user interfaces including Cloud Manager or Experience Hub.

**To access the Development Agent through Cloud Manager:**

1. To get started, click [Adobe Experience Cloud](https://experience.adobe.com/#/@foundationinternal/home) to open its home page.

    ![Adobe Experience Cloud home page](/help/implementing/cloud-manager/assets/experience-cloud-experiencemanager.png)

1. In the left rail, under the **Services** heading, click **Cloud Manager**.

    ![The drop-down list showing the Content Author preset is selected](/help/implementing/cloud-manager/assets/experience-hub-role-selection.png)

    >[!IMPORTANT]
    >
    >The widgets, tools, and artifacts shown depend on the user persona, entitlements, and AEM deployment type (AEM as a Cloud Service or Managed Services 6.5/6.5 LTS).

1. In the left rail, under **Program**, click **![Overview icon](/help/implementing/cloud-manager/configuring-pipelines/assets/overview.svg) Overview**.

1. On the **Program Overview** page, in the **Pipelines** card, click a pipeline.

    ![Selected pipeline](/help/ai-in-aem/agents/development/assets/dev-agent-pipeline-select.png)

1. In the **Build and Code Scanning** page, note the failed pipeline.

    ![Pipeline failure as seen in the Build and Code Scanning page](/help/ai-in-aem/agents/development/assets/dev-agent-pipeline-failure.png)

1. Near the upper-right corner of the AEM user interface (either from Cloud Manager pages or the author instance of the AEM environments), click the **AI Assistant** icon.

    ![AI Assistant icon on the toolbar](/help/implementing/cloud-manager/assets/ai-assistant-icon.png)

    See also [AI Assistant in AEM](/help/implementing/cloud-manager/ai-assistant-in-aem.md).

1. In the **AI Assistant** panel text box near the bottom, type your question or prompt, then press `Enter` or click ![Send icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Send_18_N.svg).

    For example:
    *In the "eda-org-01-no-access" program, analyze the failure to the "no-access" pipeline and troubleshoot.*

    The prompt results in the following response.

    ![AI Assistant prompt and resulting response](/help/ai-in-aem/agents/development/assets/dev-agent-prompt-response.png)


## Permissions {#permissions}

The Development Agent's pipeline troubleshooting job requires either the Cloud Manager - Developer role or the Cloud Manager - Program Manager role.

## Sample prompts {#sample-prompts}

| Prompt | Result |
| --- | --- |
| *Troubleshoot my failed pipeline* | Performs an analysis of why a pipeline failed; if it is unclear which pipeline is being referred to, additional questions will be asked to the user.|
| *List my failed pipelines for program Main Program.* | While results may vary, this prompt outputs a table of failed pipelines, with a follow-up suggestion to reference a specific pipeline to analyze. |
| *Analyze my failed pipeline called "Dev Pipeline."* | This prompt results in an analysis of the failed pipeline with suggestions to fix. If there are multiple failures, additional questions will be asked of the user. |
| *Troubleshoot pipeline execution 1234567* | By providing an exact pipeline execution id, a pipeline analysis is performed. |

## Out-of-scope features {#out-of-scope-features}

Pipeline troubleshooting operates on the Full-Stack pipeline's build step. For other pipeline types and steps, debug failures by downloading and inspecting the logs.

See [Access and Download Logs](/help/implementing/cloud-manager/manage-logs.md).
