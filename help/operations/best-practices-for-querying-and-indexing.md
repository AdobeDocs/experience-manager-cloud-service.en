---
title: Best Practices for Queries and Indexing
seo-title: Best Practices for Queries and Indexing
description: This article provides guidelines on how to optimize your indexes and queries.
seo-description: This article provides guidelines on how to optimize your indexes and queries.
topic-tags: best-practices
---

# Best Practices for Queries and Indexing{#best-practices-for-queries-and-indexing}

Unlike previous versions in AEM as a Cloud Service all operational aspects regarding indexing are automated. This allows developers to focus on creating efficient queries and and their corresponding index definitions.

## When to use queries {#when-to-use-queries}

Queries are a way to get access to content, but not the only one. For that reason it must be evaluated if queries are the best and most performant way to access content. In many situations content in the repository can be accessed more performant by other means.

### Repository and Taxonomy Design {#repository-and-taxonomy-design}

When designing the taxonomy of a repository, several factors need to be taken into account. These include access controls, localization, component and page property inheritance among others.

While designing a taxonomy that addresses these concerns, it is also important to consider the "traversability" of the indexing design. In this context, the traversability is the ability of a taxonomy that allows content to be predictably accessed based on its path. This will make for a more performant system that is easier to maintain than one that will require a lot of queries to be executed.

Additionally, when designing a taxonomy, it is important to consider whether ordering is important. In cases where explicit ordering is not required and a large number of sibling nodes are expected, it is preferred to use an unordered node type such as `sling:Folder` or `oak:Unstructured`. In cases where ordering is required, `nt:unstructured` and `sling:OrderedFolder` would be more appropriate.

### Queries in Components {#queries-in-components}

Since queries can be one of the more taxing operations done on an AEM system, it is a good idea to avoid them in your components. Having several queries execute each time a page is rendered can often degrade the performance of the system. There are two strategies that can be used to avoid executing queries when rendering components: **traversing nodes** and **prefetching results**.

### Traversing Nodes {#traversing-nodes}

If the repository is designed in such a way that allows prior knowledge of the location of the required data, code that retrieves this data from the necessary paths can be deployed without having to run queries in order to find it.

An example of this would be rendering content that fits within a certain category. One approach would be to organize the content with a category property that can be queried to populate a component that shows items in a category.

A better approach would be to structure this content in a taxonomy by category so that it can be manually retrieved.

For example, if the content is stored in a taxonomy similar to:

```xml
/content/myUnstructuredContent/parentCategory/childCategory/contentPiece
```

the `/content/myUnstructuredContent/parentCategory/childCategory` node can simply be retrieved, its children can be parsed and used to render the component.

Additionally, when you are dealing with a small or homogenous result set, it can be faster to traverse the repository and gather the required nodes, rather than crafting a query to return the same result set. As a general consideration, queries should be avoided where it is possible to do so.

### Prefetching Results {#prefetching-results}

Sometimes the content or the requirements around the component will not allow the use of node traversal as a method of retrieving the required data. In these cases, the required queries need to be executed before the component is rendered so that optimal performance is ensured.

If the results that are required for the component can be calculated at the time that it is authored and there is no expectancy that the content will change, the query can be executed after a change has been done.

If the data or content will change regularly, the query can be executed on a schedule or via a listener for updates to the underlying data. Then, the results can be written to a shared location in the repository. Any components that need this data can then pull the values from this single node without needing to execute a query at runtime.
A similar strategy can be used to keep the result in an in-memory cache, which is populated on startup and updated whenever changes are done (using a JCR ObservationListener or a Sling ResourceChangeListener).

## Optimizing queries {#optimizing-queries}

The Oak documentation provides a [high-level overview how queries are executed](https://jackrabbit.apache.org/oak/docs/query/query-engine.html#query-processing). This forms the basis of all optimization activities described in this document.

AEM as a Cloud Serivce provides the Query Performance Tool, which is designed to support implementing efficient queries.
* It displays already executed queries with their relevant performance characteristics and the query plan.
* It allows to perform adhoc queries in various levels, starting from just displaying the query plan up to executing the full query.

The Query Performance Tool is reachable via the [Developer Console in Cloud Manager](https://experienceleague.adobe.com/docs/experience-manager-learn/cloud-service/debugging/debugging-aem-as-a-cloud-service/developer-console.html#queries). Unlike the Query performance tool of previous versions of AEM 6.x, the performance query tool provided for AEM as a Cloud Service delivers more information about the details of the query execution, which are useful to improve a query.


The general approach how to use the Query Performance Tool to optimize queries is described in this chart.
    ![Query Optimization Flow](assets/query-optimization-flow.png)



### Use an index {#use-an-index}

Every query should use an index to deliver optimal performance. In the majority of all cases existing out-of-the-box indexes should be sufficient to handle queries. 
Sometimes custom properties need to be added to an existing index, so additional constraints can be queried using this index. See [Content Search and Indexing](/help/operations/indexing.md#changing-an-index) for more details. The [JCR Query Cheatsheet](#jcr-query-cheatsheet) describes how an property definition on an index has to look like to support a specific query type.



### Use the right criteria

The primary constraint on any query should be a property match, as this is the most efficient type. Adding more property constraints limit the result further. 
The query engine considers just a single index; that means that an existing index can and should be customized by adding more custom index properties to it.

The [JCR Query cheatsheet](#jcr-query-cheatsheet) lists the available constraints and also outlines how an index definition needs to look like so it picked up. Use the [Query Performance Tool](#query-performance-tool) to test the query and to make sure that the right index is used and that the query engine does not need to evaluate constraints outside of the index. 


### Ordering

If a specific order of the result is requested, there are 2 ways for the Query Engine to achieve this:

1. Either the index can deliver the result completely and in the right order; this works if the properties which are used for ordering are annotated with ```ordered=true``` in the index definition.
2. If the Query Engine needs to perform filtering outside of the index or if the ordering property is not annotated with the ```ordered=true``` property, the Query Engine also performs the ordering process. This case requires that the complete result set is read into memory for sorting, which is much slower than the first option.





### Restrict the result size

The retrieved size of the query result is an important factor in query performance. As the result is fetched in a lazy manner, there is a difference in just fetching the first 20 results compared to fetching 10'000 results, both in runtime and memory usage.

This also means that the size of the result set can only be determined correctly, if all results are fetched. For this reason the fetched result set should always be limited, either by augmenting the query (see the [JCR Query cheatsheet](#jcr-query-cheatsheet) for details) or by limiting the reads of the results.
Such a limit also prevents the query engine of hitting the **traversal limit** of 100'000 nodes, which leads to a forced stop of the query.

See the section [Queries with large results](#queries-with-large-result-sets) below if a potentially large result set must be processed completly.


## JCR Query Cheatsheet

To support the creation of efficient JCR queries and index definitions, the [JCR Query Cheat Sheet](https://experienceleague.adobe.com/docs/experience-manager-65/deploying/practices/best-practices-for-queries-and-indexing.html#jcrquerycheatsheet) is available for download and use as a reference during development. It contains sample queries for QueryBuilder, XPath and SQL-2, covering multiple scenarios which behave differently in terms of query performance. It also provides recommendations for how to build or customize Oak indexes. The content of this Cheat Sheet applies to AEM 6.5 and AEM as a Cloud Service.


## Queries with large result sets

Although it is recommended to avoid queries with a large result set, there are valid cases where large result must be processed. Often the size of result is not known upfront, thus some precautions should be taken to make the processing reliable.

* the query should not be executed within a request; instead the query should be executed as part of a Sling Job or an AEM workflow. These do not have any limitations in their total runtime, and are re-started in case the instance goes down during the processing of the query and its results.
* To overcome the query limit of 100'000 nodes read you should consider to use [Keyset Pagination](https://jackrabbit.apache.org/oak/docs/query/query-engine.html#Keyset_Pagination) and split the query in multiple sub-queries.
  


## Query traversing the repository

Queries traversing the repository are not using an index and are logging message like this:

```text
28.06.2022 13:32:52.804 *WARN* [127.0.0.1 [1656415972414] POST /libs/settings/granite/operations/diagnosis/granite_queryperformance.explain.json HTTP/1.1] org.apache.jackrabbit.oak.plugins.index.Cursors$TraversingCursor Traversed 98000 nodes with filter Filter(query=select [jcr:path], [jcr:score], * from [nt:base] as a /* xpath: //* */, path=*) called by com.adobe.granite.queries.impl.explain.query.ExplainQueryServlet.getHeuristics; consider creating an index or changing the query
```

This log snippet contains relevant information:

* the query itself: ```//* ```
* the java code which executed this query: ```com.adobe.granite.queries.impl.explain.query.ExplainQueryServlet::getHeuristics```; this helps to identify the creator of this query.

With this information it is possible to optimize this query using the methods described in [Optimizing Queries](#optimizing-queries).