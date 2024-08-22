---
title: Enabling JSON Export for a Component
description: Components can be adapted to generate JSON export of their content based on a modeler framework.
exl-id: e9be5c0c-618e-4b56-a365-fcdd185ae808
feature: Developing
role: Admin, Architect, Developer
---
# Enabling JSON Export for a Component {#enabling-json-export-for-a-component}

Components can be adapted to generate JSON export of their content based on a modeler framework.

## Overview {#overview}

The JSON Export is based on [Sling Models](https://sling.apache.org/documentation/bundles/models.html), and on the [Sling Model Exporter](https://sling.apache.org/documentation/bundles/models.html#exporter-framework-since-130) framework (which itself relies on [Jackson annotations](https://github.com/FasterXML/jackson-annotations/wiki/Jackson-Annotations)).

This means that the component must have a Sling Model if it must export JSON. Therefore, follow these two steps to enable JSON export on any component.

* [Define a Sling Model for the component](#define-a-sling-model-for-the-component)
* [Annotate the Sling Model interface](#annotate-the-sling-model-interface)

## Define a Sling Model for the Component {#define-a-sling-model-for-the-component}

First a Sling Model must be defined for the component.

>[!NOTE]
>
>For an example of using Sling Models see the article [Developing Sling Model Exporters in AEM](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/development/develop-sling-model-exporter.html).

The Sling Model implementation class must be annotated with the following:

```java
@Model(... adapters = {..., ComponentExporter.class})
@Exporter(name = ExporterConstants.SLING_MODEL_EXPORTER_NAME, extensions = ExporterConstants.SLING_MODEL_EXTENSION)
@JsonSerialize(as = MyComponent.class)
```

This ensures that your component could be exported on its own, using the `.model` selector and the `.json` extension.

In addition, this specifies that the Sling Model class can be adapted into the `ComponentExporter` interface.

>[!NOTE]
>
>Jackson annotations are not usually specified at the Sling Model class level, but rather at the Model interface level. This is to ensure that the JSON Export is considered as part of the component API.

>[!NOTE]
>
>The `ExporterConstants` and `ComponentExporter` classes come from the `com.adobe.cq.export.json` bundle.

### Using Multiple Selectors {#multiple-selectors}

Although not a standard use case, it is possible to configure multiple selectors in addition to the `model` selector.

```
https://<server>:<port>/content/page.model.selector1.selector2.json
```

However in such a case the `model` selector must be the first selector and the extension must be `.json`.

## Annotate the Sling Model Interface {#annotate-the-sling-model-interface}

To be taken into account by the JSON Exporter framework, the Model interface should implement the `ComponentExporter` interface (or `ContainerExporter`, in the case of a container component).

The corresponding Sling Model interface (`MyComponent`) would be then annotated using [Jackson annotations](https://github.com/FasterXML/jackson-annotations/wiki/Jackson-Annotations) to define how it should be exported (serialized).

The Model interface must be properly annotated to define which methods should be serialized. By default, all methods that respect the usual naming convention for getters are serialized and will derive their JSON property names naturally from the getter names. This can be prevented or overridden using `@JsonIgnore` or `@JsonProperty` to rename the JSON property.

## Example {#example}

[The Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html) support JSON export and can be used as a reference.

For an example, see the Sling Model implementation of the Image Core Component and its annotated interface.

## Related Documentation {#related-documentation}

* [Content Fragments](/help/sites-cloud/administering/content-fragments/overview.md)
* [Content Fragment Models](/help/sites-cloud/administering/content-fragments/managing-content-fragment-models.md)
* [Authoring with Content Fragments](/help/sites-cloud/authoring/fragments/content-fragments.md)
* [Core Components](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/introduction.html) and the [Content Fragment component](https://experienceleague.adobe.com/docs/experience-manager-core-components/using/components/content-fragment-component.html)
