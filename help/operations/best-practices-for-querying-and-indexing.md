---
title: Best Practices for Queries and Indexing
seo-title: Best Practices for Queries and Indexing
description: This article provides guidelines on how to optimize your indexes and queries.
seo-description: This article provides guidelines on how to optimize your indexes and queries.
topic-tags: best-practices
---

# Best Practices for Queries and Indexing{#best-practices-for-queries-and-indexing}

Unlike previous versions in AEM as a Cloud Service all operational aspects regarding indexing are automated. This allows to focus on creating efficient queries and and their corresponding index definitions.


## When to use queries {#when-to-use-queries}

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
A similar strategy can be used to keep the result in an in-memory cache, which is populated on startup and updated whenever changes are done.
  

## Optimizing queries
* How does the Oak query engine work? Link to Oak docs
* Point out the importance of sound index definitions
* How to test if a query is "good"?



## The Query Performance tool

* high level feature description
* video?



## JCR Query Cheatsheet

* link to the cheatsheet (+ mention that it's valid for AEM 6.5 as well)


## Queries with large result sets

* Impact on performance + caches
* Oak Keyset Pagination (https://jackrabbit.apache.org/oak/docs/query/query-engine.html#Keyset_Pagination)


## Query traversing the repository

* How to detect them, how to interprete the log message
* 


## Efficient indexes


## Should I Create an Index? {#should-i-create-an-index}


## Customizing out-of-the-box indexes

