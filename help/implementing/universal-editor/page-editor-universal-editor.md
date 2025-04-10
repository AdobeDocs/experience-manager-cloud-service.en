---
title: Page Editor and Universal Editor
description: The Page Editor remains supported by Adobe, but the Universal Editor bring exiting possibilities to your new projects.
feature: Developing
role: Admin, Architect, Developer
---

# Page Editor and Universal Editor {#page-editor-universal-editor}

The Page Editor remains supported by Adobe, but the Universal Editor bring exiting possibilities to your new projects.

## Background {#background}

Adobe introduced the [Universal Editor](/help/implementing/universal-editor/introduction.md) in 2024 as a streamlined editor embracing a modern Javascript-based development approach. The Universal Editor is Adobe's vision for a seamless and extensible graphical content authoring experience.

Recognizing the Page Editor's rich feature set and innumerable projects investing in it over the long history of AEM, Adobe continues to fully support the Page Editor, though innovation will be focused on the Universal Editor.

## Recommendation {#recommendation}

Though quickly narrowing, there remains a feature gap between the Universal Editor and Page Editor (a feature comparison can be found in the next section). For this reason, no general recommendation can be made for which editor to use for your project. 

As a rule of thumb:

* **New projects** should default to leveraging the Universal Editor unless there is a compelling reason to use the Page Editor.
* **Existing projects** should continue to use the Page Editor as long as it meets your project's needs.

**Which editor you choose should be driven entirely by your individual project's needs.**

## Feature Comparison {#feature-comparison}

Because the feature gap between the two editors is constantly shrinking, be sure to consult the [release notes of the Universal Editor](/help/release-notes/universal-editor/current.md) for the latest developments.

### Delivery {#delivery}

||Page Editor|Notes|Universal Editor|Notes|
|---|---|---|---|---|
|Classic AEM Delivery|[!BADGE Available]{type=Positive}|Recommended for use with the Core Components|[!BADGE Unavailable]{type=Negative}|Classic AEM pages typically rely on several Page Editor-specific features not available OotB with the Universal Editor.|
|Edge Delivery|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}||
|Headless Delivery|[!BADGE Partially Available]{type=Caution}|Only with [the SPA Editor,](/help/implementing/developing/hybrid/introduction.md) which was [deprecated](/help/implementing/developing/hybrid/spa-editor-deprecation.md) in favor of the Universal Editor in headless use cases|[!BADGE Available]{type=Positive}|The UE allows developers to bring their own web app without imposing any specific framework or implementation style.|

### Persistence {#persistence}

||Page Editor|Note|Universal Editor|Notes|
|---|---|---|---|---|
|Editing Page Components|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|Editing Content Fragments|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}|Including inserting new and reordering fragments|

### Capabilities {#capabilities}

||Page Editor|Note|Universal Editor|Notes|
|---|---|---|---|---|
|Page Templates|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|The Universal Editor is agnostic of the template system used.<br>- For Edge Delivery, templates are defined in code and don't require AEM's Editable Template system<br>- For headless implementations, the Universal Editor works with any template approach chosen by the frontend, as it doesn’t impose AEM-specific mechanisms.|
|Editable Templates|[!BADGE Available]{type=Positive}|Authors can adjust some template options.|[!BADGE Unavailable]{type=Negative}|Templates are adjusted by developers, not authors. For this reason, there are no plans to introduce Editable Templates.|
|WYSIWYG Editing|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|Generate Variations|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}|Available as an extension|
|Insert new block|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|Reorder Block|[!BADGE Available]{type=Positive}|Possible with in-context drag-and-drop, but not in the "tree view" side panel|[!BADGE Available]{type=Positive}|Possible via drag-and-drop in the "tree view" side panel, but not yet in-context (planned)|
|Cut/Copy-Paste Block|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned|
|Apply Styles|[!BADGE Available]{type=Positive}|Styles can be applied to components using the Style System.|[!BADGE Available]{type=Positive}|Styles can be applied using regular component (or Content Fragment) properties, using the multiselect widget a very similar UX can be achieved, however the Style System is not supported.|
|Apply Layout|[!BADGE Available]{type=Positive}|Sites must implement the AEM Responsive Grid to enable authors to resize components across three predefined breakpoints.|[!BADGE Available]{type=Positive}|Layouts can be applied using regular component (or Content Fragment) properties, however the Responsive Grid is not supported.|
|Undo-Redo|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned|
|Publish|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|Publish to preview|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}||
|Start workflow|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Available as an extension|
|Commenting|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned as an extension|
|Workfront integration|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}|Available as an extension|
|MSM and Launches|[!BADGE Available]{type=Positive}|Allows managing inheritance per component|[!BADGE Available]{type=Positive}|Managing inheritance by component is available as an extension for pages only.|
|Experimentation and personalization|[!BADGE Available]{type=Positive}|Using Target mode|[!BADGE Available]{type=Positive}|Available as an extension|
|Content tree|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Also allows reordering within the tree|
|Device simulation|[!BADGE Available]{type=Positive}|Configurable devices and breakpoints, but the user cannot manually enter any different screen dimensions to simulate|[!BADGE Available]{type=Positive}|Any screen dimensions to simulate can be manually entered, but default breakpoints can not be configured.|
|Page locking|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Available for pages as an extension|
|Page properties|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Available for pages as an extension to allow opening the properties in a new browser tab|
|Multi-field properties|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned|
|Remote DAM|[!BADGE Available]{type=Positive}||[!BADGE Partially Available]{type=Caution}|Full availability planned|
|Content versioning|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|TimeWarp and Diff View|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned|
|View in admin|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Available as an extension for pages|
|View page status|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Available in the Sites Console|
|Extensibility|[!BADGE Available]{type=Positive}|As AEM overlays|[!BADGE Available]{type=Positive}|As clearly-defined extension points using the App Builder and very little AEM-specific knowledge|

## Migrating to the Universal Editor {#migrate-ue}

The Universal Editor offers many advantages, making migration to it a great solution for new projects.

* **Visual Editing:** Like for the Page Editor, authors can edit content directly within the preview and instantly see how their changes affect the visitor experience.
* **Future-Proofing:** AEM’s roadmap prioritizes the Universal Editor as visual editor. Adopting it ensures access to the latest innovations and enhancements.
* **Simpler Integration:** No AEM-specific SDK is required to use the Universal Editor, reducing tech stack lock-in.
* **Bring Your Own App:** The Universal Editor supports any web framework or architecture, allowing adoption without requiring complex refactoring.
* **Extensibility:** The Universal Editor benefits from a robust [extension framework,](/help/implementing/universal-editor/extending.md) including integrations with GenAI, Workfront, and more.

There is no direct migration path from the Page Editor to the Universal Editor. This is due to fundamental differences in the two technologies.

* The Universal Editor does not reintroduce features like the Template Editor, Style System, or Responsive Grid. 
  * These use cases can now be handled more efficiently with lean frontend CSS and Javascript in Edge Delivery Services or headless projects.
* Since the  Universal Editor is an editor-as-a-service, it can not allow implementors to inject CSS or JS into the component dialogs.
  * This prevents automatic conversion of component dialogs from the Page Editor.
  * This affects many areas of the dialogs, like custom widgets, field validation, show/hide rules, and template-based customizations.

While the Universal Editor can technically enable editing for classic AEM pages (e.g. built with the Core Components), these sites typically rely on several Page Editor-specific features, such as the Style System, Responsive Grid, Editable Templates, and custom Javascript within dialogs.

Since the Universal Editor follows a more streamlined, modern approach that does not support these legacy features, migrating such sites would require significant refactoring. For this reason, **migrating Page Editor sites to the Universal Editor is only recommended for projects transitioning to Edge Delivery Services.**
