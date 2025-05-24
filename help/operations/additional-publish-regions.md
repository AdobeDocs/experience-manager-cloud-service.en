---
title: Additional Publish Regions
description: Learn how AEM as a Cloud Service supports additional publish regions for increased availability and reduced latency.
exl-id: b9ac3c6a-eb8b-461d-8f1d-a0356046a3f9
feature: Operations
role: Admin
---

# Additional Publish Regions {#additional-publish-regions}

Additional publish regions can be licensed and enabled on programs set up with AEM Sites. When configured, traffic on stage and production environments is routed to multiple publish farms, which has the following benefits:

* Reduced Latency - Requests that route from the CDN to the AEM publish instances are directed to the nearest publish region, which is advantageous for websites and applications visited by users in multiple geographies.
* Higher Availability - If a region is not available, the CDN directs traffic to the other available region(s).

Organizations may license up to three additional publish regions.

>[!NOTE]
>
>* This feature is available for the Sites and Forms solutions.
>* This feature cannot be applied to [sandbox programs](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/introduction-sandbox-programs.md).
>* This feature requires your program to be updated to AEM release version 12142 or higher.

## Use Cases {#use-cases}

The following are a few use cases where organizations can benefit from licensing additional publish regions.

1. For organizations that receive significant or business-critical traffic from users far away from the primary region, additional publish regions can reduce latency experienced by those visitors.
1. For organizations that may suffer significant monetary or reputational damage when a site is not available, this can be mitigated by using additional publish regions to make the AEM publish tier more resilient to regional failure.
1. For organizations whose content authors are located in a geographic location that is distant from the majority of publish tier visitors, the primary region can be chosen near the content authors' location, while additional publish regions can be configured near the publish side traffic, with both audiences benefiting from an optimized experience.

## Enabling and Configuring {#enabling-and-configuring}

After licensing an additional publish region, the regions are configured using Cloud Manager. See the [Cloud Manager documentation](/help/implementing/cloud-manager/manage-environments.md#multiple-regions) for detailed instructions.

Additional publish regions are applied to stage and production environments, but not to RDE or development environments.

In the event a region becomes unavailable, customers do not need to manage the routing of traffic to available regions since it is managed by the Adobe CDN.

As described in the Advanced Networking Considerations section below, it is recommended that customers using advanced networking configure it for each additional publish region in order for availability to be maintained if a region becomes unavailable.


## Advanced Networking Considerations {#advanced-networking-considerations}

When an additional publish region is enabled on a program with advanced networking already configured, the traffic in the additional publish region that matches the advanced networking rules will by default route through the primary region. To take advantage of increased availability, it is recommended to enable advanced networking on the additional regions.

See the [Advanced Networking Configuration for Additional Publish Regions](/help/security/configuring-advanced-networking.md#advanced-networking-configuration-for-additional-publish-regions) section in the Advanced Networking documentation for details, including how to add advanced networking configurations to additional regions without incurring loss of connectivity.

## Logging {#logging}

If additional publish regions are enabled, separate logs for each region will be made available through Cloud Manager. For more information, see [Accessing and Managing Logs](/help/implementing/cloud-manager/manage-logs.md) and [Logs for Additional Publish Regions](/help/implementing/developing/introduction/logging.md#logs-for-additional-publish-regions). 

## Limitations {#limitations}

Keep in mind the following limitations when considering using additional publish regions.

* Additional publish regions may only be added to AEM Sites or AEM Forms.
  * Additional publish regions do not extend to other AEM solutions or related functionality deployed in the same program (for example, AEM Assets or Adobe Learning Manager).
  * However these solutions can be added to a program as long as it has at least one Sites or Forms solution applies to it.
* Additional regions can only be added if associated entitlements are available and unused in the tenant.
* A maximum of three additional publish regions can be added to any individual environment.
* Additional regions are available on production programs only. The feature is not available in sandbox programs.
* Additional publish regions are applied to stage and production environments only, not to RDE or development environments.
* Additional publish regions require your program to be updated to AEM release version 12142 or higher.
