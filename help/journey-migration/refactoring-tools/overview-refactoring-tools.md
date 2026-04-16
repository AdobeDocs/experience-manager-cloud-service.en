---
title: Refactoring Tools Overview
description: Learn how to get started with AEM Refactoring Tools
exl-id: b8137e01-87e8-4298-b0cc-b376330cb730
---
<!--
 Alexandru: temporarily commeting this out, since it breaks validation

>[!CONTEXTUALHELP]
>id="aemcloud_rs_overview"
>title="Overview"
>abstract="Refactoring Tools is a solution developed by Adobe to help refactor existing AEM projects for compatibility with AEM as a Cloud Service. The tools are executed via Cloud Acceleration Manager (CAM) and automate key modernization tasks."
>additional-url="https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/migration-journey/cloud-migration/content-transfer-tool/guidelines-best-practices-content-transfer-tool.html" text="Guidelines and Best Practices"

-->

# Refactoring Tools Overview {#refactoring-tools-overview}

**Refactoring Tools** streamline the process of updating existing AEM projects to be compatible with **AEM as a Cloud Service (AEMaaCS)**. These tools automate common refactoring and modernization tasks and are integrated with the **Cloud Acceleration Manager (CAM)** for a seamless experience.

Previously available only as CLI utilities, Refactoring Tools now provide a unified interface with features like automated inspection, configuration generation, and job execution — reducing manual overhead and improving visibility.

## Inspection Workflow {#inspection-workflow}

The **Inspection Workflow** simplifies the preparation process for running refactoring tools.

### Key Features:

* **Automatic Trigger** – Uploading a project automatically starts the inspection.
* **Configuration Generation** – The tools inspect the uploaded source code and generate the necessary configurations.
* **Payload Submission** – These configurations are passed directly to the selected tools for execution.

## Available Refactoring Tools

### Repository Modernizer {#repo-modernizer}

The **Repository Modernizer** restructures your AEM project's repository layout and content to align with AEMaaCS standards and best practices. It replaces the legacy repository modernization tool with enhanced automation and accuracy.

### Code Transformer {#code-transformer}

The **Code Transformer** uses intelligent pattern recognition and AI-driven analysis to detect and update code segments that are incompatible with AEMaaCS. This tool simplifies the migration effort and reduces manual code changes.

## Refactoring Workflow Phases {#phases-in-refactoring-tools}

The Refactoring Tools follow a structured two-phase process:

### Phase 1: Upload Your Source Code

* Upload your source code (in ZIP format) using the CAM interface.
* Once uploaded, the **Inspection Workflow** is automatically triggered to analyze the project and prepare it for tool execution.

>[!NOTE]
>During the inspection process, uploading another project is not permitted.

### Phase 2: Trigger a Refactoring Job

After a successful inspection, you can run one or more refactoring tools:

* **Run Repository Modernizer** – Executes repository modernization.
* **Run Code Transformer** – Runs code transformation based on inspection output.
* **Run All Tools Together** – Executes all available tools in a single operation.

>[!NOTE]
>Refactoring jobs can only be started after the source code has been successfully uploaded and inspected.

>[!NOTE]
>Users can trigger multiple refactoring jobs parallelly, but each job will be executed separately.
