---
title: AEM System Overview
description: AEM System Overview
---

# AEM System Overview {#aem-system}

This page describes AEM as a Cloud Service that provides new capability with an architecture that is a significant enhancement over earlier AEM versions. Upgrading to this new architecture requires significant effort.

## Description {#background}

The ACRA meta-pattern is used to identify several issues related to upgrades to AEM as a Cloud Service. It supports several types of advisory information through a combination of the pattern's *referring* and "referencedBy" values and its *context* object. The *type* value within the *context* object determines the specific issue which has been detected.

The readiness issues included in the ACRA pattern are expected to have relatively few instances causing the advisory. There are other readiness issues related to AEM as a Cloud Service that may have many instances that need attention and these are given their own pattern code. (See UUI and URS.)

## Pattern Data {#pattern-data}

The following objects are included in the JSON representation of the pattern:

* **item.message**: The readiness issue type. (See below.)
* **data**: A JSON object containing the data corresponding to the type.

### Possible implications and risks {#possible-implications}

TBD

### Possible solutions  {#possible-solutions} 

TBD
