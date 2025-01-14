---
title: Disallow the Serialization of ResourceResolvers via Sling Model Exporter
description: Disallow the Serialization of ResourceResolvers via Sling Model Exporter
exl-id: 63972c1e-04bd-4eae-bb65-73361b676687
feature: Developing
role: Admin, Architect, Developer
---
# Disallow the Serialization of ResourceResolvers via Sling Model Exporter {#disallow-the-serialization-of-resourceresolvers-via-sling-model-exporter}

The Sling Model Exporter feature allows serializing Sling Model objects into JSON format. This feature is widely used as it enables SPAs (single page applications) to easily access data from AEM. On the implementation side, the Jackson Databind library is used to serialize these objects.

The serialization is a recursive operation. Starting from a "root object," it recursively iterates through all eligible objects and serializes them and their children. You can find a description of what fields are serialized in the article [Jackson - Decide What Fields Get Serialized/Deserialized.](https://www.baeldung.com/jackson-field-serializable-deserializable-or-not)

This approach serializes all types of objects into JSON. Naturally it can also serialize a Sling `ResourceResolver` object, if it is covered by the serialization rules. This is problematic, as the `ResourceResolver` service (and therefore also the service object representing it) holds potentially sensitive information, which should not get disclosed. For example:

* The user id
* The search paths to resolve relative paths
* The `propertyMap`

Especially sensitive is the `propertyMap` (see the API documentation of [`getPropertyMap`](https://sling.apache.org/apidocs/sling12/org/apache/sling/api/resource/ResourceResolver.html#getPropertyMap--)), as it's an internal data structure, which can be used for many purposes, for example caching objects which share the same lifecycle as the `ResourceResolver`. Serializing these can leak implementation details and potentially have a security impact, as data is exposed which should not be readable and accessible to an end user. For that reason `ResourceResolvers` should not be serialized into JSON.

Adobe plans to disable the serialization of `ResourceResolvers` in a two-step approach:

1. Starting with AEM as a Cloud Service release 14697, whenever a `ResourceResolver` is serialized, AEM will log a warning message. All customers are encouraged to check their application logs for these log statements and adapt their codebase accordingly.
1. At a later point Adobe will disable the serialization of `ResourceResolver`s as JSON.

## Implementation {#implementation}

The WARN message is logged both in AEM as a Cloud Service and local AEM SDK instances, and it looks like this:

```text
[127.0.0.1 [1705061734620] GET /content/../page.model.json HTTP/1.1] org.apache.sling.models.jacksonexporter.impl.JacksonExporter A ResourceResolver is serialized with all its private fields containing implementation details you should not disclose. Please review your Sling Model implementation(s) and remove all public accessors to a ResourceResolver.
```

This log message means that during the process of serializing the `/content/…/page` into JSON a `ResourceResolver` is serialized already. By requesting `/content/../page.model.json` you can check where exactly the fields of the `ResourceResolver` are showing up, and use that to identify the Sling Model class which is actually triggering this behavior.


>[!NOTE] 
>
>[AEM Core Components](https://experienceleague.adobe.com/en/docs/experience-manager-core-components/using/introduction) have been validated not to be affected by this problem.

## Requested Action {#requested-action}

Adobe requests all customers to check their application logs and code bases to see if they are affected by this problem, and change the custom application where necessary, so that this warning message no longer appears in logs.

It is assumed that in most cases these required changes are straight forward. The `ResourceResolver` objects are not required in the JSON output at all, since the information contained there is normally not required by frontend applications, meaning in most cases it should be sufficient to exclude the `ResourceResolver` object from being considered by Jackson (see the [rules.](https://www.baeldung.com/jackson-field-serializable-deserializable-or-not))

In case a Sling Model is affected by this problem but not changed, the explicit disabling of serialization of the `ResourceResolver` object (as executed by Adobe as the second step) will enforce a change in the JSON output.
