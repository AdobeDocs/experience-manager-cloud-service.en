---
title: Content Fragments and Content Packages
description: Learn how to use Content Packages for deploying Content Fragments Models and Persisted Queries
feature: Headless, Content Fragments,GraphQL API
exl-id: 5ba6921f-b06e-463d-b956-d1fb434090c9
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: bfd4bc52-c397-5127-8f86-8953ba9fc0a3
    internal-label: Headless
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Content Fragment Models, Persisted Queries and Content Packages {#content-fragment-models-persisted-queries-and-content-packages}

Content Fragment Models and persisted GraphQL queries are content that you can create and update:

* Content Fragment Models: `/conf/<config>/settings/dam/cfm/models)`
* persisted GraphQL queries: (/conf/<config>/settings/graphql/persistentQueries)`

Many projects keep them in Git and ship them in a content package. The filter mode of such a package determines what happens (including models and queries created on author):

* `mode="replace"`

  * every node:
    1. covered by the filter 
    1. but not contained within the package
    1. is deleted on author and publish whenever the package is installed during a Cloud Manager deployment

  * is the default mode when no mode is explicitly defined.

Persisted queries that depend on a model deleted in this way then fail with `Schema provider failed`.

FileVault applies the first filter entry when the root covers a path, so the order of filter entries matters. A broad entry such as `/conf/<config>` will take priority when placed before a more specific entry.

Recommended setups, depending on who owns the models and queries:

* Maintained in Git: 

  * one filter root per model or persisted query the package owns, placed before broader `/conf` entries. 
    Then content created on author is not impacted.

* Mixed ownership: 

  * `mode="update_properties"`: adds and updates but never deletes. 

    The trade-off is that a model or field removed in Git stays in AEM.

* Owned by authors: 

  * Do not include them in the package, or only seed them once with `mode="merge_properties"`
  
    Merge is not suitable for models maintained in Git, as existing nodes are left untouched and model changes are never deployed. FileVault also deprecated merge and update in favor of `merge_properties` and `update_properties`.

Example for a project that maintains two models in Git and lets authors create others:

```javascript
<filter root="/conf/wknd/settings/dam/cfm/models/article"/>
<filter root="/conf/wknd/settings/dam/cfm/models/author"/>
<filter root="/conf/wknd" mode="update_properties"/>
```

## Further Resources {#further-resources}

See also:

* [Deploying to AEM as a Cloud Service](/help/implementing/deploying/overview.md)
* [Workspace filter](https://jackrabbit.apache.org/filevault/filter.html)
