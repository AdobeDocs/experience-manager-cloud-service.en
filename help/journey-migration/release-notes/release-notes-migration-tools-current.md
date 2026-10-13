---
title: Current Release Notes for Migration Tools in AEM as a Cloud Service
description: Current Release Notes for Migration Tools in AEM as a Cloud Service.
feature: Release Information
exl-id: 52709511-eab2-47a7-8bea-1b707cd568a1
role: Admin
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: ed762d86-a04b-452b-a08f-86359bb8ff27
    internal-label: Configuration and operations
subfeature_v2:
  - id: c21ccc2b-e0c8-4853-bf41-f12259ed93f8
    internal-label: Release information
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
---
# Release Notes for Migration Tools in AEM as a Cloud Service {#release-notes}

This page outlines the current Release Notes for Migration Tools in AEM as a Cloud Service. For earlier releases, see the previous versions listed in the navigation.

## 2026 {#2026}

### AI-Assisted Code Migration {#ai-assisted-code-migration}

AI-Assisted Code Migration provides an IDE-based, AI-driven path for migrating AEM 6.5 (or earlier) Java-stack projects to AEM as a Cloud Service. A migration agent skill reads Best Practices Analyzer findings and applies the required code transformations one pattern at a time, while a companion Cloud Migration MCP server fetches those findings directly from Cloud Acceleration Manager. The skill also generates a read-only migration runbook that assesses the whole project and lists every applicable pattern before it changes any code.

The skill now includes these patterns:

* Legacy UI: Classic UI, ExtJS, and Coral 2 dialogs convert to Coral 3, and custom ExtJS design widgets migrate to Granite UI.
* Template modernization: static templates convert to editable templates with AEM Modernize Tools rewrite rules.
* Guava cache to Caffeine: Guava cache usage switches to Caffeine, the supported Cloud Service cache library.
* Dispatcher configuration conversion: AMS and on-premise Apache HTTPD and Dispatcher configurations convert to the Cloud Service structure.
* Unsupported run mode (URC) detection: the skill flags OSGi configuration folders with unsupported run modes and reorders them safely where possible.

Existing supported patterns include Sling Scheduler, ResourceChangeListener, Replication API, OSGi EventListener and EventHandler, Assets API, HTL lint fixes, and OSGi configuration conversion.

For more information, see [AI-Assisted Code Migration to AEM as a Cloud Service](/help/journey-migration/cloud-migration-skill/overview-cloud-migration-skill.md).
