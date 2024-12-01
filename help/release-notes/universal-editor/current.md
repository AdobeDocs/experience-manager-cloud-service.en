---
title: Universal Editor 2024.11.28 Release Notes
description: These are the release notes for the 2024.11.28 release of the Universal Editor.
feature: Release Information
role: Admin
exl-id: d16ed78d-d5a3-45bf-a415-5951e60b53f9
---

# Universal Editor 2024.11.28 Release Notes {#release-notes}

These are the release notes for the 28 November 2024 release of the Universal Editor.

>[!TIP]
>
>For the current release notes for Adobe Experience Manager as a Cloud Service, please see [this page.](/help/release-notes/release-notes-cloud/release-notes-current.md)

## What’s New {#what-is-new}

* **Keyboard Navigation of Content Tree**: The Content Tree side-panel is now fully accessible via keyboard. Authors can navigate and interact with tree view items using standard keyboard controls, adhering to WCAG 2.1 guidelines for accessibility. This enhancement ensures that all interactive elements within the tree are keyboard-operable, improving inclusivity for users who rely on keyboard navigation.
* **Deselection of Editables**: Authors can now deselect previously selected editable elements on the page. This eliminates distractions when authors want to view the page without active selection borders.
* **Fragment Selector**: On AEM as a Cloud Service instances, fragment references now open the Fragment Selector as content picker, delivering improved functionality such obeying allowed Content Fragment Models, search of Content Fragments and an improved overall experience. This aligns with other Adobe UIs and enhances consistency. For AEM 6.5 environments, the existing content picker remains in use.
* **Container Description**: The container component used in the Properties panel to reference content now supports a description attribute, displayed above the container fields. This addition enhances clarity by providing authors with context about the grouped fields they are editing.

## Other Improvements {#other-improvements}

* **Rich Text Field Synchronization**: Improved synchronization of raw and rendered content within rich text fields in the Properties panel, addressing issues within Crosswalk projects where Rich Text content and rendered representation can differ.
* **Editing Mode Events**: The Universal Editor now reliably emits editing mode events also after the remote apps is reload.
