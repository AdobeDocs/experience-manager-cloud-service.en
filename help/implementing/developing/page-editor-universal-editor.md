---
title: Page Editor and Universal Editor
description: The Page Editor remains supported by Adobe, but the Universal Editor bring exiting new possibilities to your new projects.
feature: Developing
role: Admin, Architect, Developer
---

# Page Editor and Universal Editor {#page-editor-universal-editor}

The Page Editor remains supported by Adobe, but the Universal Editor bring exiting new possibilities to your new projects.

## Background {#background}

Adobe introduced the [Universal Editor](/help/implementing/universal-editor/introduction.md) in 2024 as a streamlined  editor embracing a modern Javacript-based development approach. The Universal Editor is Adobe's vision for a seamless and extensible graphical content authoring experience.

Recognizing the Page Editor's rich feature set and innumerable projects investing in it over the long history of AEM, Adobe continues to fully support the Page Editor, though innovation will be focused on the Universal Editor.

## Recommendation {#recommendation}

Though quickly narrowing, there remains a feature gap between the Universal Editor and Page Editor. For this reason, no blanket recommendation can be made. A feature comparison can be found in the next section.

As a rule of thumb:

* **New projects** should default to leveraging the Universal Editor unless there is a compelling reason to use the Page Editor.
* **Existing projects** should continue to use the Page Editor as long as it meets your project's needs.

**Which editor you choose should be driven entirely by your individual project's needs.**

## Feature Comparison {#feature-comparison}

Because the feature gap between the two editors is constantly shrinking be sure to consult the release notes of the Universal Editor for the latest developments.

### Delivery {#delivery}

||Page Editor|Universal Editor|
|---|---|---|
|Classic AEM Delivery|[!BADGE Available]{type=Positive}||
|Edge Delivery|||

### Persistence {#persistence}

### Capabilities {#capabilities}

## Migrating to the Universal Editor {#migrate-ue}

The Universal Editor offers many advantages, making migration to it a great solution for new projects.

* **Visual Editing:** Like for the Page Editor, authors can edit content directly within the preview and instantly see how their changes affect the visitor experience.
* **Future-Proofing:** AEM’s roadmap prioritizes the Universal Editor as visual editor. Adopting it ensures access to the latest innovations and enhancements.
* **Simpler Integration:** No AEM-specific SDK is required to use the Universal Editor, reducing tech stack lock-in.
* **Bring Your Own App:** The Universal Editor supports any web framework or architecture, allowing adoption without requiring complex refactoring.
* **Extensibility:** The Universal Editor benefits from a robust [extension framework,](/help/implementing/universal-editor/extending.md) including integrations with GenAI, Workfront, and more.

There is no direct migration path from the Page Editor to the Universal Editor. This is due to fundamental differences in the two technologies.

* The Universal Editor does not reintroduce features like the Template Editor, Style System, or Responsive Grid. 
  * These use cases can now be handled more efficiently with lean frontend CSS and JS in Edge Delivery Services or headless projects.
* Since the  Universal Editor is an editor-as-a-service, it cannot allow implementors to inject CSS or JS into the component dialogs.
  * This prevents automatic conversion of component dialogs from the Page Editor.
  * This affects many areas of the dialogs, like custom widgets, field validation, show/hide rules, and template-based customizations.
