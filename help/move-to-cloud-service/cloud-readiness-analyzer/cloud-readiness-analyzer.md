---
title: Assessing Complexity of Moving to Cloud Service
description: Assessing Complexity of Moving to Cloud Service
---

# Cloud Readiness Analyzer {#accesing-complexity}

## Overview {#overview}

The Cloud Readiness Analyzer (CRA) enables you to check existing AEM instances for their readiness to move to Cloud Service by detecting patterns that:

* Use an AEM 6.x feature that is currently not supported on Cloud Service

* Violate certain rules that will be affected by the move to Cloud Service

>[!NOTE]
>The output of the CRA speeds up the assessment of the development effort that will be required to move to Cloud Service.

## Setting up Cloud Readiness Analyzer {#setting-up-cra}

The CRA is released as a package working on any source AEM versions from XX and above, exploring a move to Cloud Service. 

It is available on the Software Distribution Portal and can be installed using the Package Manager.

### Using Cloud Readiness Analyzer {#using-cra}

>[!NOTE]
> CRA can run on any environment, including local development instances. 

>[IMPORTANT]
>However, in order to increase the detection rate and avoid any slowdowns on business critical instances, it is recommended to run it on staging environments that are as close as possible to production ones in the areas of user applications, content and configurations

### Viewing Output on Cloud Readiness Analyzer {#viewing-output-cra}


1. Navigate to AEM Web Console by browsing to **Adobe Experience Manager Web Console Configuration** using `https://serveraddress:serverport/system/console/configMgr`.

1. Select Status - Cloud Readiness Analyzer as shown in the image below.

1. You can also view the output via a reactive text based or regular JSON interface.

>[!NOTE]
> Refer to [Pattern Detector](https://docs.adobe.com/content/help/en/experience-manager-65/deploying/upgrading/pattern-detector.html) for more details on these methods). Need to add this section once CRA is ready for use.

## Next Steps on Cloud Readiness {#the-next-steps}

To get more information about your readiness for Cloud Service, Adobe needs to evaluate the output of the CRA. 

Follow the steps below to send back the file:

1. Navigate to the AEM Web Console and download the xx file as shown in the image below.

1. Open a DayCare ticket to send the file to Adobe by: 
   1. Logging a support ticket in Daycare titled as **Cloud Readiness Analyzer Output**
   1. Attaching an output file to the ticket

