---
title: Query Builder Predicate Reference
description: Predicate reference for the Query Builder API in AEM as a Cloud Service.
exl-id: 77118ef7-4d29-470d-9c4b-20537a408940
feature: Developing
role: Admin, Architect, Developer
---
# Query Builder Predicate Reference {#query-builder-predicate-reference}

## General {#general}

### root {#root}

The root predicate group. It supports all features of a group and allows setting global query parameters.

The name "root" is never used in a query; it's implicit.

#### Properties {#properties-18}

* **`p.offset`** -  number indicating the start of the result page, that is, how many items to skip.
* **`p.limit`** - number indicating the page size.
* **`p.guessTotal`** - recommended: avoid calculating the full result total, which can be costly. Either a number indicating the maximum total to count up to (for example, 1000, a number that gives users enough feedback on the rough size and exact numbers for smaller results). Or, `true` to count only up to the minimum necessary `p.offset` + `p.limit`.
* **`p.excerpt`** - if set to `true`, include full text excerpt in the result.
* **`p.indexTag`** - if set will include an index tag option in the query (see [Query Option Index Tag](https://jackrabbit.apache.org/oak/docs/query/query-engine.html#query-option-index-tag)).
* **`p.facetStrategy`** - if set to `oak`, Query Builder will delegate facet extraction to Oak (see [Facets](https://jackrabbit.apache.org/oak/docs/query/query-engine.html#facets)).
* **`p.hits`** - (only for the JSON servlet) select the way the hits are written as JSON, with these standard ones (extensible by way of the ResultHitWriter service).
  * **`simple`** - minimal items like `path`, `title`, `lastmodified`, `excerpt` (if set).
  * **`full`** - sling JSON rendering of the node, with `jcr:path` indicating the path of the hit. By default, just lists the direct properties of the node, include a deeper tree with `p.nodedepth=N`, with 0 meaning the entire, infinite subtree. Add `p.acls=true` to include the JCR permissions of the current session on the given result item (mappings: `create` = `add_node`, `modify` = `set_property`, `delete` = `remove`).
  * **`selective`** - only properties specified in `p.properties`, which is a space separated (use `+` in URLs) list of relative paths. If the relative path has a depth `>1`, these properties are represented as child objects. The special `jcr:path` property includes the path of the hit.

### group {#group}

This predicate allows building nested conditions. Groups can contain nested groups. Everything in a Query Builder query is implicitly in a root group, which can have `p.or` and `p.not` parameters as well.

The following is an example for matching either one of two properties against a value:

```text
group.p.or=true
group.1_property=jcr:title
group.1_property.value=My Page
group.2_property=navTitle
group.2_property.value=My Page
```

Conceptually, it is `(1_property` OR `2_property)`.

The following is an example for nested groups:

```text
fulltext=Management
group.p.or=true
group.1_group.path=/content/wknd/ch/de
group.1_group.type=cq:Page
group.2_group.path=/content/dam/wknd
group.2_group.type=dam:Asset
```

Searches for the term **Management** within pages in `/content/wknd/ch/de` or in assets in `/content/dam/wknd`.

Conceptually, it is `fulltext AND ( (path AND type) OR (path AND type) )`. Such OR joins need good indexes for performance reasons.

#### Properties {#properties-6}

* **`p.or`** - if set to `true`, only one predicate in the group must match. Defaults to `false`, meaning all must match
* **`p.not`** - if set to `true`, it negates the group (defaults to `false`)
* **`<predicate>`** - adds nested predicates
* **`N_<predicate>`** - adds multiple nested predicates of the same time, like `1_property, 2_property, ...`

### orderby {#orderby}

This predicate allows sorting the results. If ordering by multiple properties is required, this predicate must be added multiple times using the number prefix, such as `1_orderby=first`, `2_oderby=second`.

#### Properties {#properties-13}

* **`orderby`** - either JCR property name indicated by a leading @, for example, `@jcr:lastModified` or `@jcr:content/jcr:title`, or another predicate in the query, for example, `2_property`, on which to sort
* **`sort`** - sort direction, either `desc` for descending or `asc` for ascending (default)
* **`case`** - if set to `ignore`, it makes sorting case insensitive, meaning `a` comes before `B`; if empty or left out, sorting is case-sensitive, meaning `B` comes before `a`

## Predicates {#predicates}

### boolproperty {#boolproperty}

This predicate matches on JCR boolean properties. Only accepts the values `true` and `false`. If the value is `false`, it matches if the property has the value `false`, or if it does not exist at all. This predicate is useful for checking for boolean flags that are only set when enabled.

The inherited `operation` parameter has no meaning.

This predicate supports facet extraction and provides buckets for each `true` or `false` value, but only for existing properties.

#### Properties {#properties}

* **`boolproperty`** -  relative path to property, for example, `myFeatureEnabled` or `jcr:content/myFeatureEnabled`
* **`value`** - value to check property for, `true` or `false`

### contentfragment {#contentfragment}

This predicate restricts the result to content fragments.

* It does not support filtering.
* It does not support facet extraction.

#### Properties {#properties-1}

* **`contentfragment`** - It can be used with any value to check for content fragments.

### `dateComparison` {#datecomparison}

This predicate compares two JCR date properties with each other. Can test if they are equal, unequal, greater than or greater-than-or-equal.

A filtering-only predicate and cannot use a search index.

#### Properties {#properties-2}

* **`property1`** - path to first date property
* **`property2`** - path to second date property
* **`operation`**
  * `=` for exact match (default)
  * `!=` for inequality comparison
  * `>` for `property1` greater than `property2`
  * `>=` for `property1` greater than or equal to `property2`

### daterange {#daterange}

This predicate matches JCR date properties against a date/time interval. Uses the ISO8601
format for dates and times (`YYYY-MM-DDTHH:mm:ss.SSSZ`) and allows also partial representations, like `YYYY-MM-DD`. Alternatively, the timestamp can be provided as POSIX time.

You can look for anything between two timestamps, anything newer or older than a given date, and also chose between inclusive and open intervals.

It supports facet extraction and provides buckets `today`, `this week`, `this month`, `last 3 months`, `this year`, `last year`, and `earlier than last year`.

It does not support filtering.

#### Properties {#properties-3}

* **`property`** - relative path to a `DATE` property, for example, `jcr:lastModified`
* **`lowerBound`** - lower date bound to check property for, for example, `2014-10-01`
* **`lowerOperation`** - `>` (newer) or `>=` (at or newer), applies to the `lowerBound`. The default is `>`
* **`upperBound`** - upper bound to check property for, for example, `2014-10-01T12:15:00`
* **`upperOperation`** - `<` (older) or `<=` (at or older), applies to the `upperBound`. The default is `<`
* **`timeZone`** - ID of timezone to use when it is not given as an ISO-8601 date string. The default is the default timezone of the system.

### excludepaths {#excludepaths}

This predicate excludes nodes from the result where their path matches a regular expression.

A filtering-only predicate and cannot use a search index.

It does not support facet extraction.

#### Properties {#properties-4}

* **`excludepaths`** - regular expression matched against result paths, excluding matching ones from the result.

### fulltext {#fulltext}

Searches for terms in the fulltext index.

It does not support filtering.

It does not support facet extraction.

#### Properties {#properties-5}

* **`fulltext`** - the fulltext search terms
* **`relPath`** - the relative path to search in the property or subnode. This property is optional.

### hasPermission {#haspermission}

This predicate restricts the result to items where the current session has the specified [JCR privileges](https://developer.adobe.com/experience-manager/reference-materials/spec/jcr/2.0/16_Access_Control_Management.html#16.2.3%20Standard%20Privileges).

A filtering-only predicate and cannot use a search index. It does not support facet extraction.

#### Properties {#properties-7}

* **`hasPermission`** - all comma-separated JCR privileges that the current user session must have for the node in question. For example, `jcr:write`, `jcr:modifyAccessControl`

### language {#language}

This predicate finds AEM pages in a specific language. It looks at both the page language property and the page path which often includes the language or locale in a top-level site structure.

A filtering-only predicate and cannot use a search index.

It supports facet extraction and provides buckets for each unique language code.

#### Properties {#properties-8}

* **`language`** - ISO language code, for example, `de`

### mainasset {#mainasset}

This predicate checks if a node is a DAM main asset and not a sub asset. It is basically every node not inside a sub assets node. It does not check for the `dam:Asset` node type. To use this predicate, set `mainasset=true` or `mainasset=false`. There are no further properties.

A filtering-only predicate and cannot use a search index.

It supports facet extraction and provides two buckets for main and sub assets.

#### Properties {#properties-9}

* **`mainasset`** - boolean, `true` for main assets, `false` for sub assets

### memberOf {#memberof}

This predicate finds items that are member of a specific [sling resource collection](https://developer.adobe.com/experience-manager/reference-materials/cloud-service/javadoc/org/apache/sling/resource/collection/ResourceCollection.html).

A filtering-only predicate and cannot use a search index.

It does not support facet extraction.

#### Properties {#properties-10}

* **`memberOf`** - path of Sling resource collection

### nodename {#nodename}

This predicate matches on JCR node names.

It supports facet extraction and provides buckets for each unique node name (filename).

#### Properties {#properties-11}

* **`nodename`** - node name pattern that allows wildcards: `*` = any or no char, `?` = any char, `[abc]` = only chars in brackets

### notexpired {#notexpired}

This predicate matches items by checking if a JCR date property is greater or equal than the current server time. It can be used to check on an `expiresAt` value and limits results to only those values that have not yet expired (`notexpired=true`), or that have expired already (`notexpired=false`).

It does not support filtering.

It supports facet extraction in the same way as the [`daterange`](#daterange) predicate.

#### Properties {#properties-12}

* **`notexpired`** - boolean, `true` for not yet expired (date in the future or equal), `false` for expired (date in the past) (required)
* **`property`** - relative path to the `DATE` property to check (required)

### path {#path}

This predicate searches within a given path.

It does not support facet extraction.

#### Properties {#properties-14}

* **`path`** - Defines the path pattern.
  * Depending on the `exact` property, either the entire subtree matches (like appending `//*` in xpath, but note that it does not include the base path), or only an exact path is matched, which can include wildcards (`*`).
    * Defaults to `true`.
<!---   * If the `self`property is set, the entire subtree including the base node is searched.--->
* **`exact`** - if `exact` is `true`, the exact path must match, but it can contain simple wildcards (`*`), that match names, but not `/`; if it is `false` (default) all descendants are included (optional).
* **`flat`** - searches only the direct children (like appending `/*` in xpath) (only used if `exact` is not true, optional).
* **`self`** - searches the subtree but includes the base node given as path (no wildcards).
  * *Important Note*: An issue has been identified with `self` property in the current implementation of query builder and using it in queries may not produce correct search results. Changing the current implementation of `self` property is also not feasible because it might break the existing applications that rely on it. Due to this functionality, `self` property is now deprecated; it is advised to avoid using it.

### property {#property}

This predicate matches on JCR properties and their values.

It supports facet extraction and provides buckets for each unique property value in the results.

#### Properties {#properties-15}

* **`property`** - relative path to property, for example, `jcr:title`.
* **`value`** - value to check property for; follows the JCR property type to string conversions.
* **`N_value`** - use `1_value`, `2_value`, ... to check for multiple values (combined with `OR` by default, with `AND` if `and=true`).
* **`and`** - set to `true` for combining multiple values (`N_value`) with `AND`
* **`operation`**
  * `equals` for exact match (default).
  * `unequals` for inequality comparison.
  * `like` for using the `jcr:like` xpath function (optional).
  * `not` for no match (for example, `not(@prop)` in xpath, value param is ignored).
  * `exists` for existence check.
    * `true` the property must exist.
    * `false` is the same as `not` and is the default.
* **`depth`** - number of wildcard levels underneath which the property/relative path can exist (for example, `property=size depth=2` checks `node/size`, `node/*/size`, and `node/*/*/size`).

### rangeproperty {#rangeproperty}

This predicate matches a JCR property against an interval. It applies to properties with linear types such as `LONG`, `DOUBLE`, and `DECIMAL`. For `DATE`, see the [`daterange`](#daterange) predicate that has optimized date format input.

You can define a lower bound, an upper bound, or both. The operation (for example, lesser than, or lesser than or equal to) can also be specified for lower and upper bound individually.

It does not support facet extraction.

#### Properties {#properties-16}

* **`property`** - relative path to property
* **`lowerBound`** - lower bound to check property
* **`lowerOperation`** - `>` (default) or `>=`, applies to the `lowerValue`
* **`upperBound`** - upper bound to check property
* **`upperOperation`** - `<` (default) or `<=`, applies to the `lowerValue`
* **`decimal`** - `true` if the checked property is of type Decimal

### relativedaterange {#relativedaterange}

This predicate matches `JCR DATE` properties against a date/time interval using time offsets relative to the current server time. You can specify `lowerBound` and `upperBound` using either a millisecond value or the Bugzilla syntax `1s 2m 3h 4d 5w 6M 7y` (one second, two minutes, three hours, four days, five weeks, six months, seven years). Prefix with `-` to indicate a negative offset before the current time. If you only specify `lowerBound` or `upperBound`, the other one defaults to `0`, representing the current time.

For example:

* `upperBound=1h` (and no `lowerBound`) selects anything in the next hour
* `lowerBound=-1d` (and no `upperBound`) selects anything in the last 24 hours
* `lowerBound=-6M` and `upperBound=-3M` selects anything in the last 3 to six months
* `lowerBound=-1500` and `upperBound=5500` selects anything between 1500 milliseconds old and 5500 milliseconds in the future
* `lowerBound=1d` and `upperBound=2d` selects anything the day after tomorrow

It does not take leap years into consideration and all months are 30 days.

It does not support filtering.

It supports facet extraction in the same way as the [`daterange`](#daterange) predicate.

#### Properties {#properties-17}

* **`upperBound`** - upper date bound in milliseconds or `1s 2m 3h 4d 5w 6M 7y` (one second, two minutes, three hours, four days, five weeks, six months, seven years) relative to current server time, use `-` for negative offset
* **`lowerBound`** - lower date bound in milliseconds or `1s 2m 3h 4d 5w 6M 7y` (one second, two minutes, three hours, four days, five weeks, six months, seven years) relative to current server time, use `-` for negative offset

### savedquery {#savedquery}

This predicate includes all predicates of a persisted Query Builder query into the current query as a sub group predicate.

It does not run an extra query but extends the current query.

Queries can be persisted programmatically using `QueryBuilder#storeQuery()`. The format can be either a multi-line `String` property or an `nt:file` node that contains the query as a text file in Java&trade; properties format.

It does not support facet extraction for the predicates of the saved query.

#### Properties {#properties-19}

* **`savedquery`** - path to the saved query (`String` property or `nt:file` node)

### similar {#similar}

This predicate is a similarity search using JCR XPath's `rep:similar()`.

It does not support filtering and does not support facet extraction.

#### Properties {#properties-20}

* **`similar`** - absolute path to the node for which to find similar nodes
* **`local`** - a relative path to a descendant node or `.` for the current node (optional, default is `.`)

### tag {#tag}

This predicate searches for content tagged with one or more tags, by specifying tag title paths.

It supports facet extraction and provides buckets for each unique tag, using their current tag title path.

#### Properties {#properties-21}

* **`tag`** - tag title path to look for, for example, `properties:orientation/landscape`
* **`N_value`** - use `1_value`, `2_value`, ... to check for multiple tags (combined with `OR` by default, with `AND` if `and=true`)
* **`property`** - property (or relative path to property) to look at (default `cq:tags`)

### tagid {#tagid}

This predicate searches for content tagged with one or more tags, by specifying tag IDs.

It supports facet extraction and provides buckets for each unique tag, using their current tag ID.

#### Properties {#properties-22}

* **`tagid`** - tag ID to look for, for example, `properties:orientation/landscape`
* **`N_value`** - use `1_value`, `2_value`, ... to check for multiple tag IDs (combined with `OR` by default, with `AND` if `and=true`)
* **`property`** - property (or relative path to property) to look at (default `cq:tags`)

### tagsearch {#tagsearch}

This predicate searches for content tagged with one or more tags, by specifying keywords. It searches first for tags containing these keywords in their titles, then restricts the result to only items tagged with these keywords.

It does not support facet extraction.

#### Properties {#Properties-1}

* **`tagsearch`** - keyword to search for in tag titles
* **`property`** - property (or relative path to property) to consider (default `cq:tags`)
* **`lang`** - to search in a certain localized tag title only (for example, `de`)
* **`all`** - boolean value to search entire tag fulltext, that is, all titles, descriptions, and so on (takes precedence over `lang`)

### type {#type}

This predicate restricts results to a specific JCR node type, both primary node types or `mixin` types. It also finds sub types of that node type. Repository search indexes must cover the node types for efficient execution.

It supports facet extraction and provides buckets for each unique type in the results.

#### Properties {#Properties-2}

* **`type`** - node type or `mixin` name to search for, for example, `cq:Page`
