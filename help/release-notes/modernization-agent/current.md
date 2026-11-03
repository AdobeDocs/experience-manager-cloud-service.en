---
title: Experience Modernization Agent 2026.11.02 Release Notes
description: These are the release notes for the 2026.11.02 release of the Experience Modernization Agent.
feature: Release Information
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

# Experience Modernization Agent 2026.11.02 Release Notes {#release-notes}

These are the release notes for the 2 November 2026 release of the Experience Modernization Agent (EMA) and its console.

>[!TIP]
>
>The console also summarizes the highlights of the latest release in a **What's new** notice at the top of the page. To learn what the agent does and how to start, see the [Experience Modernization Agent overview.](/help/ai-in-aem/agents/brand-experience/modernization/overview.md)

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What's New {#what-is-new}

* **Guided review of your migration plan:** When planning finishes, the agent offers to **Review scoping results**. It first fixes clear issues itself, such as moving outliers, merging look-alike block variants, and correcting names, and tells you what it changed. It then walks you through the remaining decisions one at a time. Choose **Autopilot** at the start, or **Finish for me** on any step, to let it complete the review alone. Items it is still unsure about are left unchanged and flagged in its report. See [Review the catalog.](/help/ai-in-aem/agents/brand-experience/modernization/site-catalog.md#review-catalog)
* **Page limits for auto-mode migrations:** Before you start an auto-mode migration, the page shows how many pages each migration can include for your account. Where your account permits it, you can choose how many pages a full-site migration includes. See [Auto-mode limits.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#auto-mode-limits)

## Other Improvements {#other-improvements}

* Chat, Home, and Settings now fit phone and tablet screens.
* The chat input has been updated and keeps its existing features.
* A **Demo site** button in the header now explains, before you start working, that work in the demo site isn't saved. See [Demo mode.](/help/ai-in-aem/agents/brand-experience/modernization/getting-started.md#demo-mode)
* Planning progress now shows the current step.
* Site discovery is more reliable.
* Prompt hints no longer flag suggested prompts that you send unchanged or only extend. Rewording a suggestion triggers the usual checks.
* Agent guidance uses plain language instead of internal migration terms.
* Long task lists scroll within the chat, and you can expand or collapse the pending tasks.
* Preview now uses the site configuration to find the correct code repository.
* The agent recognizes requests to restore or preview a Document Authoring page, and explains when writing to remote content is not allowed.
* Conversations with many screenshots no longer fail. Older screenshots are shortened automatically.
* **Upload to AEM** for AEM authoring projects fails less often.
