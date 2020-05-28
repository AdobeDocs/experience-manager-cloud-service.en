---
title: Customization Detected
description: Customization Detected
---

# Customization Detected {#cust-pattern}

This page describes Customization Detected pattern code.

## Background {#background}

This pattern code is used to identify customizations that have been made to the AEM instance. Because customization of AEM is common, this pattern does not necessarily indicate that there is a problem. It identifies a record of customizations so that they can be evaluated with respect to their impact on upgrade plans.

Customizations which are detected include:

* Customer code (packages) and configurations
* Third-party packages
* Integrations with third-party services
* Non-standard Oak indexes

## Pattern Data {#pattern-data}

The following objects are included in the JSON representation of the pattern:

* **item.message**: refers to the message of the pattern.
* **item.context**: refers to additional information about the overview information:
   * *type*: customization.detected.
   * *data*: A JSON object containing the data describing the customization

### Possible implications and risks {#possible-implications}

Not applicable.

### Possible solutions  {#possible-solutions} 

Not applicable.
