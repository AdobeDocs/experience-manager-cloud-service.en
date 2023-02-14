---
title: Additional Publish Regions
description: Additional publish regions for increased availability and reduced latency
---

# Additional Publish Regions {#additional-publish-regions}

Additional Publish Regions can be licensed and enabled on programs set up with AEM Sites. It results in traffic on stage and production environments being routed to multiple publish farms, which has the following benefits:

* Reduced latency - requests that route from the CDN to the AEM publish instances are directed to the nearest publish region, which is advantageous for websites and applications visited by users in multiple geographies
* Higher availability - if a region is not available, the CDN directs traffic to the other available region(s). Note that if a request needs to retrieve files from the data store, but the primary region's data store is not reachable, those files will not be accessible.

Organizations may license up to three additional publish regions.

>[!NOTE]
>
>This feature is currently only available for AEM Sites. It also cannot be applied sandbox programs. In addition, please be aware that Additional Publish Regions require your program to be updated to AEM release version 10912 or higher.

## Scenarios {#scenarios}

Below are a few scenarios where organizations can benefit from licensing additional publish regions:

1. Organizations that receive significant or business-critical traffic from users far away from the primary region. Additional publish regions can reduce latency experienced by those visitors.
1. Organizations that may suffer significant monetary or reputational damage when a site is not available. This can be mitigated by using additional publish regions to make the AEM publish tier more resilient to regional failure.
1. Organizations whose content authors are located in a geographic location that is distant from the majority of publish tier visitors. The primary region can be chosen near the content authors' location, while additional publish regions can be configured near the publish side traffic, with both audiences benefiting from an optimized experience.

## Enabling and Configuring {#enabling-and-configuring}

After licensing an additional publish region, it is configured using Cloud Manager. See the [Cloud Manager documentation](/help/implementing/cloud-manager/manage-environments.md#multiple-regions) for detailed instructions.

Additional publish regions are applied to stage and producton environments, but not RDE or development environments.

## Advanced Networking Considerations {#advanced-networking-considerations}

When an additional publish region is enabled on a program with advanced networking already configured, the traffic in the additional publish region that matches the advanced networking rules will by default route through the primary region. In order to take advantage of increased availability, it is recommended to enable advanced networking for the secondary region.

Read the [Advanced Networking Considerations for Additional Publish Regions section](/help/security/configuring-advanced-networking.md#advanced-networking-configuration-for-additional-publish-regions) in the Advanced Networking documentation for details, including how to add advanced networking configurations for additional regions without incurring loss of connectivity.
