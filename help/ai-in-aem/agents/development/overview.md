---
title: Development Agent Overview
description: Learn about AEM's Development agent
feature: Development agent
role: Admin, Architect, Developer
---

# Development Agent Overview {#development-agent}

The Development Agent empowers technical roles — developers and administrators — by streamlining the creation, debugging, deployment, and optimization of code. 

The agent currently fulfills the job of retrieving the pipeline statuses and troubleshooting a failing build step by suggesting fixes, saving time when debugging AEM as a Cloud Services deployments to dev, stage, and production environments.

// ### Cloud Manager Pipeline Troubleshooting  {#cloudmanager-troubleshooting}

#### How to Access the Agent {#access}

Access the Development Agent through the AI Assistant found in user interfaces including Cloud Manager and Experience Hub.

#### Permissions {#permissions}

The Development Agent's pipeline troubleshooting job requires Cloud Manager Developer or Program Manager roles.

#### Sample Prompts {#sample-prompts}

*List my failed pipelines for program Main Program.*

While results may vary, this should output a table of failed pipelines, with a followup suggestion to reference a specific pipeline to analyze.

*Analyze my failed pipeline called "Dev Pipeline".*

This should result in an analysis of the failed pipeline with suggestions to fix.


#### Out of Scope Features {#out-of-scope}

Pipeline troubleshooting operates on the Full-Stack pipeline's build step. For other pipeline types and steps, debug failures by downloading and inspecting the logs.

