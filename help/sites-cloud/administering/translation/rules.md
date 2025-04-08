---
title: Identifying Content to Translate
description: Learn how translation rules identify content that needs translating.
feature: Language Copy
role: Admin
exl-id: 24cc6aa6-5b3c-462b-a10a-8b25277229dc
solution: Experience Manager Sites
---
# Identifying Content to Translate {#identifying-content-to-translate}

Translation rules identify the content to translate for pages, components, and assets that are included in, or excluded from, translation projects. When a page or asset is being translated, AEM extracts this content so that it can be sent to the translation service.

>[!TIP]
>
>If you are new to translating content, see [Sites Translation Journey](/help/journey-sites/translation/overview.md), which is guided path through translating your AEM Sites content using AEM's powerful translation tools, ideal for those with no AEM or translation experience.

## Content Fragments and Translation Rules {#content-fragments}

The translation rules described in this document apply to Content Fragments only if the **Enable Content Model Fields for Translation** option has not been activated at the [translation integration framework configuration level](integration-framework.md#assets-configuration-properties).

If the **Enable Content Model Fields for Translation** option is active, AEM will use the **Translatable** field on [Content Fragment Models](/help/sites-cloud/administering/content-fragments/content-fragment-models.md#properties) to determine if the field is to be translated and automatically creates translation rules accordingly. This option supersedes any translation rules you may have created and requires no intervention or additional steps.

If you want to use translation rules for translating your Content Fragments, the **Enable Content Model Fields for Translation** option on the translation integration framework configuration must be disabled and you need to follow the steps outlined below to create your rules.

## Overview {#overview}

Pages and assets are represented as nodes in the JCR repository. The content that is extracted is one or more property values of the nodes. Translation rules identify the properties that contain the content to extract.

Translation rules are expressed in XML format and stored in these possible locations:

* `/libs/settings/translation/rules/translation_rules.xml`
* `/apps/settings/translation/rules/translation_rules.xml`
* `/conf/global/settings/translation/rules/translation_rules.xml`

The file applies to all translation projects.

Rules include the following information:

* The path of the node to which the rule applies
  * The rule also applies to the descendants of the node.
* The names of the node properties that contain the content to translate
  * The property can be specific to a specific resource type or to all resource types.

For example, you can create a rule that translates the content that authors add to all text components on your pages. The rule can identify the `/content` node and the `text` property for the `core/wcm/components/text/v2/text` component.

There is a [console](#translation-rules-ui) that has been added for configuring translation rules. The definitions in the UI will populate the file for you.

For an overview of the content translation features in AEM, see [Translating Content for Multilingual Sites](overview.md).

>[!NOTE]
>
>AEM supports one-to-one mapping between resource types and reference attributes for translation of referenced content on a page.

## Rule Syntax for Pages, Components, and Assets {#rule-syntax-for-pages-components-and-assets}

A rule is a `node` element with one or more child `property` elements and zero or more child `node` elements:

```xml
<node path="content path">
          <property name="property name" [translate="false"]/>
          <node resourceType="component path" >
               <property name="property name" [translate="false"]/>
          </node>
</node>
```

Each of these `node` elements has the following characteristics:

* The `path` attribute contains the path to the root node of the branch to which the rules apply.
* Child `property` elements identify the node properties to translate for all resource types:
  * The `name` attribute contains the property name.
  * The optional `translate` attribute equals `false` if the property is not translated. By default the value is `true`. This attribute is useful when overriding previous rules.
* Child `node` elements identify the node properties to translate for specific resource types:
  * The `resourceType` attribute contains the path that resolves to the component that implements the resource type.
  * Child `property` elements identify the node property to translate. Use this node in the same way as the child `property` elements for node rules.

The following example rule causes the content of all `text` properties to be translated for all pages below the `/content` node. The rule is effective for any component that stores content in a `text` property, such as the text component.

```xml
<node path="/content">
          <property name="text"/>
</node>
```

The following example translates the content of all `text` properties, and also translates other properties of the image component. If other components have same-named properties, the rule does not apply to them.

```xml
<node path="/content">
      <property name="text"/>
      <node resourceType="core/wcm/components/image/v2/image">
         <property name="image/alt"/>
         <property name="image/jcr:description"/>
         <property name="image/jcr:title"/>
      </node>
</node>
```

## Rule Syntax for Extracting Assets from Pages  {#rule-syntax-for-extracting-assets-from-pages}

Use the following rule syntax to include assets that are embedded in or referenced from components:

```xml
<assetNode resourceType="path to component" assetReferenceAttribute="property that stores asset"/>
```

Each `assetNode` element has the following characteristics:

* One `resourceType` attribute that equals the path that resolves to the component
* One `assetReferenceAttribute` attribute that equals the name of the property that stores the asset binary (for embedded assets) or the path to the referenced asset

The following example extracts images from the image component:

```xml
<assetNode resourceType="core/wcm/components/image/v2/image" assetReferenceAttribute="fileReference"/>
```

## Overriding Rules {#overriding-rules}

The `translation_rules.xml` file consists of a `nodelist` element with several child `node` elements. AEM reads the node list from top to bottom. When multiple rules target the same node, the rule that is lower in the file is used. For example, the following rules cause all content in `text` properties to be translated except for the `/content/mysite/en` branch of pages:

```xml
<nodelist>
     <node path="/content">
           <property name="text" />
     </node>
     <node path="/content/mysite/en">
          <property name="text" translate="false" />
     </node>
<nodelist>
```

## Filtering Properties {#filtering-properties}

You can filter nodes that have a specific property by using a `filter` element.

For example, the following rules cause all content in `text` properties to be translated except for the nodes that have the property `draft` set to `true`.

```xml
<nodelist>
    <node path="/content">
     <filter>
   <node containsProperty="draft" propertyValue="true" />
     </filter>
        <property name="text" />
    </node>
<nodelist>
```

## Translation Rules UI {#translation-rules-ui}

A console is also available for configuring translation rules.

To access it:

1. Navigate to **Tools** and then **General**.

1. Select **Translation Configuration**.

In the translation rules UI you can:

1. **Add Context**, which lets you add a path.

   ![Add translation context](../assets/add-translation-context.png)

1. Use the path browser to select the required context and select the **Confirm** button to save.

   ![Select context](../assets/select-context.png)

1. Then you need to select your context and then click **Edit**. This opens the Translation Rules Editor.

   ![Translation Rules Editor](../assets/translation-rules-editor.png)

There are four attributes that you can change via the UI:

* `isDeep`
* `inherit`
* `translate`
* `updateDestinationLanguage`

### isDeep {#isdeep}

**`isDeep`**  is applicable on node filters and is true by default. It checks if the node (or its ancestors) contains that property with the specified property value in the filter. If false, it only checks at the current node.

For example, child nodes are added to a translation job even when the parent node has the property `draftOnly` set to true to flag draft content. Here `isDeep` comes into play and checks if the parent nodes have property `draftOnly` as true and excludes those child nodes.

In the editor, you can check/uncheck **Is Deep** in the **Filters** tab.

![Filter rules](../assets/translation-rules-editor-filters.png)

Here is an example of the resulting XML when **Is Deep** is unchecked in the UI:

```xml
 <filter>
    <node containsProperty="draftOnly" isDeep="false" propertyValue="true"/>
</filter>
```

### inherit {#inherit}

**`inherit`** is applicable to properties. By default every property is inherited, but if you want some property not to be inherited by the child, then you can mark this property to be false so that it is applied only to that specific node.

In the UI, you can check/uncheck **Inherit** in the **Properties** tab.

### translate {#translate}

**`translate`** is used simply to specify whether or not to translate a property.

In the UI, you can check/uncheck **Translate** in the **Properties** tab.

### updateDestinationLanguage {#updatedestinationlanguage}

**`updateDestinationLanguage`** is used for properties that do not have text but language codes, for example, `jcr:language`. The user is not translating text but the language locale from source to destination. Such properties are not sent for translation.

In the UI, you can check/uncheck **Translate** in the **Properties** tab to modify this value, but for the specific properties that have language codes as value.

To help clarify the difference between `updateDestinationLanguage` and `translate`, here is a simple example of a context with only two rules:

![updateDestinationLanguage example](../assets/translation-rules-updatedestinationlanguage.png)

The result in the xml will look like this:

```xml
<property inherit="true" name="text" translate="true" updateDestinationLanguage="false"/>
<property inherit="true" name="jcr:language" translate="false" updateDestinationLanguage="true"/>
```

## Editing the Rules File Manually {#editing-the-rules-file-manually}

The `translation_rules.xml` file that is installed with AEM contains a default set of translation rules. You can edit the file to support the requirements of your translation projects. For example, you can add rules so that the content of your custom components are translated.

If you edit the `translation_rules.xml` file, keep a backup copy in a content package. Reinstalling certain AEM packages can replace the current `translation_rules.xml` file with the original. To restore your rules in this situation, you can install the package that contains your backup copy.

>[!NOTE]
>
>After you create the content package, rebuild the package each time you edit the file.

## Example Translation Rules File {#example-translation-rules-file}

```xml
<?xml version="1.0" encoding="UTF-8"?><nodelist>
  <node path="/content">
    <property name="addLabel"/>
    <property name="allowedResponses"/>
    <property name="alt"/>
    <property name="attachFileLabel"/>
    <property name="benefits"/>
    <property name="buttonLabel"/>
    <property name="chartAlt"/>
    <property name="confirmationMessageToggle"/>
    <property name="confirmationMessageUntoggle"/>
    <property name="constraintMessage"/>
    <property name="contentLabel"/>
    <property name="denyText"/>
    <property name="detailDescription"/>
    <property name="emptyText"/>
    <property name="helpMessage"/>
    <property name="image/alt"/>
    <property name="image/jcr:description"/>
    <property name="image/jcr:title"/>
    <property name="jcr:description"/>
    <property name="jcr:title"/>
    <property name="heading"/>
    <property name="label"/>
    <property name="main"/>
    <property name="listLabel"/>
    <property name="moreText"/>
    <property name="pageTitle"/>
    <property name="placeholder"/>
    <property name="requiredMessage"/>
    <property name="resetTitle"/>
    <property name="subjectLabel"/>
    <property name="subtitle"/>
    <property name="tableData"/>
    <property name="text"/>
    <property name="title"/>
    <property name="navTitle"/>
    <property name="titleDivContent"/>
    <property name="toggleLabel"/>
    <property name="transitionLabel"/>
    <property name="untoggleLabel"/>
    <property name="name"/>
    <property name="occupations"/>
    <property name="greetingLabel"/>
    <property name="signInLabel"/>
    <property name="signOutLabel"/>
    <property name="pretitle"/>
    <property name="cq:panelTitle"/>
    <property name="actionText"/>
    <property name="cq:language" updateDestinationLanguage="true"/>
    <node pathContains="/cq:annotations">
      <property name="text" translate="false"/>
    </node>
    <node path="/content/wknd"/>
  </node>
  <node path="/content/forms">
    <property name="text" translate="false"/>
  </node>
  <node path="/content/dam">
    <property name="dc:description"/>
    <property name="dc:rights"/>
    <property name="dc:subject"/>
    <property name="dc:title"/>
    <property name="defaultContent"/>
    <property name="jcr:description"/>
    <property name="jcr:title"/>
    <property name="pdf:Title"/>
    <property name="xmpRights:UsageTerms"/>
    <property name="main"/>
    <property name="adventureActivity"/>
    <property name="adventureDescription"/>
    <property name="adventureDifficulty"/>
    <property name="adventureGearList"/>
    <property name="adventureGroupSize"/>
    <property name="adventureItinerary"/>
    <property name="adventurePrice"/>
    <property name="adventureTitle"/>
    <property name="adventureTripLength"/>
    <property name="adventureType"/>
    <node pathContains="/jcr:content/metadata/predictedTags">
      <property name="name"/>
    </node>
  </node>
  <assetNode assetReferenceAttribute="fragmentPath" resourceType="cq/experience-fragments/editor/components/experiencefragment"/>
  <assetNode assetReferenceAttribute="fragmentVariationPath" resourceType="core/wcm/components/experiencefragment/v1/experiencefragment"/>
  <assetNode assetReferenceAttribute="fileReference" resourceType="dam/cfm/components/contentfragment"/>
  <assetNode resourceType="docs/components/download"/>
  <assetNode resourceType="docs/components/image"/>
  <assetNode assetReferenceAttribute="fileReference" resourceType="foundation/components/image"/>
  <assetNode assetReferenceAttribute="asset" resourceType="foundation/components/video"/>
  <assetNode assetReferenceAttribute="fileReference" resourceType="foundation/components/download"/>
  <assetNode assetReferenceAttribute="fileReference" resourceType="core/wcm/components/download/v1/download"/>
  <assetNode assetReferenceAttribute="fileReference" resourceType="wcm/foundation/components/image"/>
  <assetNode assetReferenceAttribute="fragmentPath" resourceType="core/wcm/components/contentfragment/v1/contentfragment"/>
  <assetNode assetReferenceAttribute="fileReference" resourceType="core/wcm/components/image/v2/image"/>
</nodelist>

```
