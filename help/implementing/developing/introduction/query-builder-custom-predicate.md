---
title: Implementing a Custom Predicate Evaluator for the Query Builder
description: The Query Builder in AEM offers an easy, customizable way to query the content repository
exl-id: 8c2f8c22-1851-4313-a1c9-10d6d9b65824
feature: Developing
role: Admin, Architect, Developer
---
# Implementing a Custom Predicate Evaluator for the Query Builder {#implementing-a-custom-predicate-evaluator-for-the-query-builder}

This document describes how to extend the [Query Builder](query-builder-api.md) by implementing a custom predicate evaluator.

## Overview {#overview}

The [Query Builder](query-builder-api.md) offers an easy way to query the content repository. AEM comes with [a set of predicate evaluators](#query-builder-predicates.md) that help you query your data.

However you might want to simplify your queries by implementing a custom predicate evaluator that hides some complexity and ensures a better semantic.

A custom predicate could also perform other things not directly possible with XPath, for example:

* Querying data from another service
* Custom filtering based on a calculation

>[!NOTE]
>
>Performance issues must be considered when implementing a custom predicate.

>[!TIP]
>
>You can find examples of queries in the [Query Builder](query-builder-api.md) document.

>[!TIP]
>
>You can find the code of this page on GitHub
>
>* [Open aem-search-custom-predicate-evaluator project on GitHub](https://github.com/Adobe-Marketing-Cloud/aem-search-custom-predicate-evaluator)
>* Download the project as [a ZIP file](https://github.com/Adobe-Marketing-Cloud/aem-search-custom-predicate-evaluator/archive/master.zip)

>[!NOTE]
>
>This linked code on GitHub and the code snippets in this document are provided for demonstration purposes only.

### Predicate Evaluator in Detail {#predicate-evaluator-in-detail}

A predicate evaluator handles the evaluation of certain predicates, which are the defining constraints of a query.

It maps a higher-level search constraint (such as `width>200`) to a specific JCR query that fits the actual content model (for example, `metadata/@width > 200`). Or it can manually filter nodes and check their constraints.

>[!TIP]
>
>For more information about the `PredicateEvaluator` and the `com.day.cq.search` package see the [Java documentation](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/index.html?com/day/cq/search/package-summary.html).

### Implementing a Custom Predicate Evaluator for Replication Metadata {#implementing-a-custom-predicate-evaluator-for-replication-metadata}

As an example this section describes how to create a custom predicate evaluator that helps data based on the replication metadata:

* `cq:lastReplicated` that stores the date of the last replication action
* `cq:lastReplicatedBy` that stores the id of the user who triggered the last replication action
* `cq:lastReplicationAction` that stores the last replication action (for example, Activation, Deactivation)

#### Querying Replication Metadata with Default Predicate Evaluators {#querying-replication-metadata-with-default-predicate-evaluators}

The following query fetches the list of nodes in `/content` branch that have been activated by `admin` since the beginning of the year.

```xml
path=/content

1_property=cq:lastReplicatedBy
1_property.value=admin

2_property=cq:lastReplicationAction
2_property.value=Activate

daterange.property=cq:lastReplicated
daterange.lowerBound=2013-01-01T00:00:00.000+01:00
daterange.lowerOperation=>=
```

This query is valid but hard to read and does not highlight the relationship between the three replication properties. Implementing a custom predicate evaluator will reduce the complexity and improve the semantic of this query.

#### Objectives {#objectives}

The goal of the `ReplicationPredicateEvaluator` is to support the above query using the following syntax.

```xml
path=/content

replic.by=admin
replic.since=2013-01-01T00:00:00.000+01:00
replic.action=Activate
```

Grouping replication metadata predicates with a custom predicate evaluator helps to create a meaningful query.

#### Updating Maven Dependencies {#updating-maven-dependencies}

>[!TIP]
>
>The set up of new AEM projects including using maven is explained in detail by [the WKND tutorial](develop-wknd-tutorial.md).

First you need to update the Maven dependencies of your project. The `PredicateEvaluator` is part of the `cq-search` artifact so it must be added to your Maven pom file.

>[!NOTE]
>
>The scope of the `cq-search` dependency is set to `provided` because `cq-search` is provided by the `OSGi` container.

The following snippet shows the differences in the `pom.xml` file, in [unified diff format](https://en.wikipedia.org/wiki/Diff#Unified_format)

```text
@@ -120,6 +120,12 @@
             <scope>provided</scope>
         <dependency>
+            <groupid>com.day.cq</groupid>
+            <artifactid>cq-search</artifactid>
+            <version>5.6.4</version>
+            <scope>provided</scope>
+        </dependency>
+        <dependency>
             <groupid>junit</groupid>
             <artifactid>junit</artifactid>
             <version>3.8.1</version></dependency>
```

#### Writing The ReplicationPredicateEvaluator {#writing-the-replicationpredicateevaluator}

The `cq-search` project contains the `AbstractPredicateEvaluator` abstract class. This can be extended with a few steps to implement your own custom predicate evaluator `(PredicateEvaluator`).

>[!NOTE]
>
>The following procedure explains how to build an `Xpath` expression to filter data. Another option would be to implement the `includes` method that selects data on a row basis. See the [Java documentation](https://www.adobe.io/experience-manager/reference-materials/cloud-service/javadoc/com/day/cq/search/eval/PredicateEvaluator.html) for more information.

1. Create a new Java class which extends `com.day.cq.search.eval.AbstractPredicateEvaluator`
1. Annotate your class with a `@Component` like snippet shows in [unified diff format](https://en.wikipedia.org/wiki/Diff#Unified_format)

   ```text
   @@ -19,8 +19,11 @@
     */
    package com.adobe.aem.docs.search;

   +import org.apache.felix.scr.annotations.Component;
   +import com.day.cq.search.eval.AbstractPredicateEvaluator;

   +@Component(metatype = false, factory = "com.day.cq.search.eval.PredicateEvaluator/repli")
    public class ReplicationPredicateEvaluator extends AbstractPredicateEvaluator {

    }
   ```

   >[!NOTE]
   >
   >The `factory`must be a unique string starting with `com.day.cq.search.eval.PredicateEvaluator/`and ending with the name of your custom `PredicateEvaluator`.

   >[!NOTE]
   >
   >The name of the `PredicateEvaluator` is the predicate name, which is used when building queries.

1. Override:

   ```java
   public String getXPathExpression(Predicate predicate, EvaluationContext context)
   ```

   In the override method you build a `Xpath` expression based on the `Predicate` given in argument.

### Example of a Custom Predicate Evaluator for Replication Metadata {#example-of-a-custom-predicate-evaluator-for-replication-metadata}

The complete implementation of this `PredicateEvaluator` might be similar to the following class.

```java
/*
 * #%L
 * aem-docs-custom-predicate-evaluator
 * %%
 * Copyright (C) 2013 Adobe Research
 * %%
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * #L%
 */

package com.adobe.aem.docs.search;

import org.apache.felix.scr.annotations.Component;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.day.cq.search.Predicate;
import com.day.cq.search.eval.AbstractPredicateEvaluator;
import com.day.cq.search.eval.EvaluationContext;

@Component(metatype = false, factory = "com.day.cq.search.eval.PredicateEvaluator/repli")

public class ReplicationPredicateEvaluator extends AbstractPredicateEvaluator {

    static final String PE_NAME = "replic";


    static final String PN_LAST_REPLICATED_BY = "cq:lastReplicatedBy";
    static final String PN_LAST_REPLICATED = "cq:lastReplicated";
    static final String PN_LAST_REPLICATED_ACTION = "cq:lastReplicationAction";

    static final String PREDICATE_BY = "by";
    static final String PREDICATE_SINCE = "since";
    static final String PREDICATE_SINCE_OP = " >= ";
    static final String PREDICATE_ACTION = "action";

    Logger log = LoggerFactory.getLogger(getClass());

    /**
     * Returns a XPath expression filtering by replication metadata.
     *
     * @see com.day.cq.search.eval.AbstractPredicateEvaluator#getXPathExpression(com.day.cq.search.Predicate,
     *      com.day.cq.search.eval.EvaluationContext)
     */

    @Override

    public String getXPathExpression(Predicate predicate,
            EvaluationContext context) {

        log.debug("predicate {}", predicate);

        String date = predicate.get(PREDICATE_SINCE);
        String user = predicate.get(PREDICATE_BY);
        String action = predicate.get(PREDICATE_ACTION);

        StringBuilder sb = new StringBuilder();

        if (date != null) {

            sb.append(PN_LAST_REPLICATED).append(PREDICATE_SINCE_OP);
            sb.append("xs:dateTime('").append(date).append("')");

        }

        if (user != null) {

            addAndOperator(sb);
            sb.append(PN_LAST_REPLICATED_BY);
            sb.append("='").append(user).append("'");

        }

        if (action != null) {

            addAndOperator(sb);
            sb.append(PN_LAST_REPLICATED_ACTION);
            sb.append("='").append(action).append("'");

        }

        String xpath = sb.toString();

        log.debug("xpath **{}**", xpath);

        return xpath;

    }

    /**
     * Add an and operator if the builder is not empty.
     *
     * @param sb a {@link StringBuilder} containing the query under construction
     */

    private void addAndOperator(StringBuilder sb) {

        if (sb.length() != 0) {

            sb.append(" and ");

        }

    }

}
```
