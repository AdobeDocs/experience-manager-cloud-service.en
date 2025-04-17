---
title: Page Editor and Universal Editor
description: The Page Editor remains supported by Adobe, but the Universal Editor bring exiting possibilities to your new projects.
feature: Developing
role: Admin, Architect, Developer
exl-id: 0a13fb52-623e-4aff-b254-186d8d117e4d
---
# Page Editor and Universal Editor {#page-editor-universal-editor}

The Page Editor remains supported by Adobe, but the Universal Editor bring exiting possibilities to your new projects.

## Background {#background}

Adobe introduced the [Universal Editor](/help/implementing/universal-editor/introduction.md) in 2024 as a streamlined editor embracing a modern Javascript-based development approach. The Universal Editor is Adobe's vision for a seamless and extensible visual content authoring experience.

Recognizing the [Page Editor](/help/sites-cloud/authoring/page-editor/introduction.md)'s rich feature set and innumerable projects investing in it over the long history of AEM, Adobe continues to fully support the Page Editor, though innovation will be focused on the Universal Editor.

## Recommendation {#recommendation}

Though quickly narrowing, there remains a feature gap between the Universal Editor and Page Editor ([a feature comparison can be found in the next section](#feature-comparison)). 

As a rule of thumb:

* **New projects** should default to leveraging the Universal Editor.
* **Existing projects** should continue to use the Page Editor and consider the Universal Editor when starting Edge Delivery or Headless efforts.

**Which editor you choose should be driven entirely by your individual project's needs.**

## Feature Comparison {#feature-comparison}

Because the feature gap between the two editors is constantly shrinking, be sure to consult the [release notes of the Universal Editor](/help/release-notes/universal-editor/current.md) for the latest developments.

### Delivery {#delivery}

||Page Editor|Notes|Universal Editor|Notes|
|---|---|---|---|---|
|[Classic AEM Delivery](/help/sites-cloud/authoring/author-publish.md)|[!BADGE Available]{type=Positive}|Recommended for use with the Core Components|[!BADGE Unavailable]{type=Negative}|Classic AEM pages typically rely on several Page Editor-specific features that are difficult to replicate as-is with the Universal Editor.|
|[Edge Delivery](/help/edge/overview.md)|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}||
|[Headless Delivery](/help/headless/introduction.md)|[!BADGE Partially Available]{type=Caution}|Only with [the SPA Editor,](/help/implementing/developing/hybrid/introduction.md) which was [deprecated](/help/implementing/developing/hybrid/spa-editor-deprecation.md) in favor of the Universal Editor|[!BADGE Available]{type=Positive}|The Universal Editor allows developers to bring their own web app without imposing any specific framework requirements or implementation constraints.|

### Persistence {#persistence}

||Page Editor|Notes|Universal Editor|Notes|
|---|---|---|---|---|
|Editing Page components|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|Editing [Content Fragments](/help/assets/content-fragments/content-fragments.md)|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}|Including inserting new and reordering fragments|

### Capabilities {#capabilities}

||Page Editor|Notes|Universal Editor|Notes|
|---|---|---|---|---|
|Page Templates|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|The Universal Editor is agnostic of the template system used. However, the typical implementation pattern favors developer-defined templates, as modern frontend tooling makes it much easier for developers to define and maintain template logic directly in code. |
|WYSIWYG Editing|[!BADGE Available]{type=Positive}|Limited to Pages|[!BADGE Available]{type=Positive}|Supporting Pages and Content Fragments|
|[Generate Variations](/help/generative-ai/generate-variations.md)|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}|[Available as an extension](/help/implementing/universal-editor/extending.md)|
|Insert new block|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|Reorder Block|[!BADGE Available]{type=Positive}|Possible with in-context drag-and-drop, but not in the "tree view" side panel|[!BADGE Available]{type=Positive}|Possible via drag-and-drop in the "tree view" side panel, but not yet in-context (planned)|
|Cut/Copy-Paste Block|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned|
|Apply Styles|[!BADGE Available]{type=Positive}|Styles can be applied to components using [the Style System.](/help/sites-cloud/authoring/page-editor/style-system.md)|[!BADGE Available]{type=Positive}|Styles can be applied using regular component (or Content Fragment) properties. The same Style picker is not available in the Universal Editor, however using a multiselect widget a very similar UX can be achieved.|
|Apply Layout|[!BADGE Available]{type=Positive}|Sites must implement the [AEM Responsive Grid](/help/implementing/developing/introduction/responsive-design.md) to enable authors to resize components across three predefined breakpoints.|[!BADGE Available]{type=Positive}|Layouts can be applied using regular component (or Content Fragment) properties, however the Responsive Grid is not supported.|
|Undo-Redo|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned|
|Publish (also to preview)|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|[Start workflow](/help/sites-cloud/authoring/workflows/overview.md)|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Available as an extension|
|Commenting|[!BADGE Available]{type=Positive}|Using [annotations](/help/sites-cloud/authoring/page-editor/annotations.md)|[!BADGE Unavailable]{type=Negative}|Planned|
|Workfront integration|[!BADGE Unavailable]{type=Negative}||[!BADGE Available]{type=Positive}|Available as an extension|
|[MSM and Launches](/help/sites-cloud/administering/msm-and-translation.md)|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Available for pages as an extension|
|Experimentation and personalization|[!BADGE Available]{type=Positive}|Using [Target mode](/help/sites-cloud/authoring/personalization/targeted-content.md)|[!BADGE Available]{type=Positive}|Available as an extension for Edge Delivery Services|
|Content tree|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Also allows reordering within the tree|
|Device simulation|[!BADGE Available]{type=Positive}|[Configured devices can be simulated,](/help/sites-cloud/administering/responsive-layout.md) but the user cannot manually enter any different screen dimensions to simulate.|[!BADGE Available]{type=Positive}|[Any screen dimensions to simulate can be manually entered,](/help/sites-cloud/authoring/universal-editor/navigation.md#emulator) but default breakpoints can not be configured.|
|[Page locking](/help/sites-cloud/authoring/sites-console/managing-pages.md)|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Respects lock status set in Sites Console with extension available to lock/unlock pages from the editor|
|[Page properties](/help/sites-cloud/authoring/sites-console/page-properties.md)|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Available from the Site Admin, with extension to also access the properties of pages from the editor|
|Multi-field properties|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned|
|[Remote DAM](/help/assets/dynamic-media-open-apis-overview.md)|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|[Page versioning](/help/sites-cloud/authoring/sites-console/page-versions.md)|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}||
|[TimeWarp](/help/sites-cloud/authoring/sites-console/page-versions.md#timewarp) and [Diff View](/help/sites-cloud/authoring/sites-console/page-diff.md)|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Planned|
|View in admin|[!BADGE Available]{type=Positive}||[!BADGE Available]{type=Positive}|Available as an extension for pages|
|View page status|[!BADGE Available]{type=Positive}||[!BADGE Unavailable]{type=Negative}|Available in the Sites Console|
|Extensibility|[!BADGE Available]{type=Positive}|As AEM overlays|[!BADGE Available]{type=Positive}|As clearly-defined extension points using the App Builder and very little AEM-specific knowledge|

## Adopting the Universal Editor {#adopt-ue}

The Universal Editor offers many advantages, making it a great solution for new projects.

* **Visual Editing:** Like for the Page Editor, authors can edit content directly within the preview and instantly see how their changes affect the visitor experience.
* **Future-Proofing:** AEM’s roadmap prioritizes the Universal Editor as visual editor. Adopting it ensures access to the latest innovations and enhancements.
* **Simpler Integration:** No AEM-specific SDK is required to use the Universal Editor, reducing tech stack lock-in.
* **Bring Your Own App:** The Universal Editor supports any web framework or architecture, allowing adoption without requiring complex refactoring.
* **Extensibility:** The Universal Editor benefits from a robust [extension framework,](/help/implementing/universal-editor/extending.md) including integrations with GenAI, Workfront, and more.

### Migrating to the Universal Editor {#migrate-ue}

There is no direct migration path from the Page Editor to the Universal Editor. This is due to fundamental differences in the two technologies.

* The Universal Editor does not reintroduce features like the Template Editor, Style System, or Responsive Grid. 
  * These use cases can now be handled more efficiently with lean frontend CSS and Javascript in Edge Delivery Services or headless projects.
* Since the  Universal Editor is an editor-as-a-service, it can not allow implementors to inject CSS or JS into the component dialogs.
  * This prevents automatic conversion of component dialogs from the Page Editor.
  * This affects many areas of the dialogs, like custom widgets, field validation, show/hide rules, and template-based customizations.
    * While such capabilities are still possible, the Universal Editor solves them through configuration, instead of custom JavaScript deployed in dialogs.

While the Universal Editor can technically enable editing for classic AEM pages (e.g. built with the Core Components), these sites typically rely on several Page Editor-specific features, such as the Style System, Responsive Grid, Editable Templates, and custom Javascript within dialogs.

Since the Universal Editor follows a more streamlined, modern approach that does not support these legacy features, migrating such sites would require significant refactoring. For this reason, **migrating Page Editor sites to the Universal Editor is only recommended for projects transitioning to Edge Delivery Services.**
