---
title: How to restart AEM SDK?
description: Best practices to restart AEM SDK
role: Admin, Developer, User
feature: Adaptive Forms
badgeSaas: label="AEM Forms" type="Positive" tooltip="Applies to AEM Forms)."
exl-id: 5fec2a93-1dda-4240-8690-24a6afae5c2b
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
  - id: b69b2659-1057-424e-8fc5-ed9e016dc554
    internal-label: User
---
# Restarting the AEM SDK 

If you restart the AEM SDK by stopping the Java&trade; processes, may lead to inconsistencies in the AEM development environment an error occurs as:

`javax.jcr.RepositoryException: Applying repoinit operation failed despite retry; set loglevel to DEBUG to see all exceptions. Last exception message was: Failed to set ACL (javax.jcr.ValueFormatException: Invalid type: 0) AclLine ALLOW {principals=[forms-xfa-writers], privileges=[jcr:modifyProperties]} restrictions=[rep:glob=[*/jcr:content/*], rep:itemNames=[xfaForm], fd:condition=[xfaForm, 1]]`

![Restart-aem-sdk-error](/help/forms/assets/restart-sdk-error.png)

## Solution

To restart the AEM SDK, go to active command window and press `Ctrl + C` command to restart the SDK. 

It is recommended to use the 'Ctrl + C' command to restart the SDK. Restarting the AEM SDK using alternative methods, for example, stopping Java&trade; processes, may lead to inconsistencies in the AEM development environment.

## See also

* [Set up local development environment for AEM Forms](/help/forms/setup-local-development-environment.md)

