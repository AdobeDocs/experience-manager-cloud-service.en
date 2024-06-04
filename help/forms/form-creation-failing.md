---
title: How to troubleshoot failures of forms creation?
description: Troubleshooting failures of forms creation on AEM Forms as a Cloud Service environment.
feature: Adaptive Forms, Troubleshooting
role: User
exl-id: 169ea727-0941-4a1d-bc33-d9fe208b27ab
---
# Issue while publishing forms{#form-creation-fails}

After users update to AEM Forms as a Cloud Service version `2024.5.16461`:

**Some users** may face issue while creating forms, the issue is such that when a user creates a form, the following error message pops up in the creation dialog box:

`A server error occurred. Try again after sometime.`

## Cause {#cause-form-creation-fails}

The issue occurs because the author publishes the form without **first publishing the template** used in it. This results in the addition of the `jcr:uuid` and other protected and system-generated properties to the `<template-path>/initial/jcr:content` node, causing failures in subsequent form creation.

## Workaround {#resolution-form-creation-fails}

To resolve the issue, perform the following steps:

1. Ensure that the template you use in your form does not have the `jcr:uuid` and other system generated protected properties at the path `<template-path>/initial/jcr:content node`.
1. Publish the template explicitly using the template console.
1. Now, when your template is published, try creating new forms using the template.
1. If the template you used updates in the future releases, Publish the template again (as given in the step 2) to prevent form creation failure issues.


<!--

# Issue {#form-creation-fails}

After updating to AEM Forms as a Cloud Service version `2024.5.16461.20240524T172309Z`, When a user publishes a form using an unpublished template, it fails to create a form and shows an error:

`Property is protected: jcr:uuid = 09e0d6be-f619-4405-b021-27eb1c5326d3`

## Solution {#troubleshoot-form-creation-fails}

To resolve the issue, perform the following workaround steps:

1. Publish the template explicitly using the template console.
    
    >[!NOTE]
    > Prior to this step ensure that the (unpublished) template does not have `jcr:uuid` and other system generated properties under the initial content's `jcr:content node`. To sort out it, first, sanitize the template to publish it explicitly.

    >[!NOTE]
    > This action doesn't replicate the initial content node.
1. Now, when your template is published, try creating new forms using the template.
1. If the template is changed in the future, publish it again as mentioned in the step 1.

-->
