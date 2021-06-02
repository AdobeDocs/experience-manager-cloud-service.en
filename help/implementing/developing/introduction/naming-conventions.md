---
title: Naming Conventions
description: Nodes in the repository are subject to naming conventions of the Java Content Repository
exl-id: 3c5c39dd-b209-488b-a93e-e840786fe224
---
# Naming Conventions{#naming-conventions}

Nodes in the repository are subject to naming conventions of the Java Content Repository. However AEM imposes further conventions for the name of page nodes.

## Naming Conventions for Pages {#naming-conventions-for-pages}

These naming conventions are implemented at various levels:

* JcrUtil: the AEM implementation of the [JCR utilities](#jcr-utilities).
* PageManager: the [Page Manager](#page-manager) provides methods for page level operations.
* Within the AEM UI {#ui-behavior}

### JCR Utilities {#jcr-utilities}

[JcrUtil](https://experienceleague.adobe.com/docs/experience-manager-cloud-service-javadoc/com/day/cq/commons/jcr/JcrUtil.html) is the AEM implementation of the JCR utilities. Of particular interest to validating names are the character mappings that it controls and the following validations:

* `isValidName`
  * Checks if the name is not empty and contains only valid chars.
  * Can be used to check whether a proposed name is valid.
* `createValidName`
  * This creates a valid label out of an arbitrary string.
  * It can be used to create a name from a title.

### Page Manager {#page-manager}

[PageManager](https://experienceleague.adobe.com/docs/experience-manager-cloud-service-javadoc/com/day/cq/wcm/api/PageManager.html) provides methods for page level operations, based on [JCRUtil](#jcr-utilities).

### AEM UI Behavior {#ui-behavior}

When managing content, the AEM UI:

* Validates the name according to the restrictions imposed by PageManager when either:
  * a page title is provided for conversion into the node name
  * an explicit node name is provided
