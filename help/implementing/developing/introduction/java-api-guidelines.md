---
title: Java API Guidelines
description: AEM is built on a rich open-source software stack that exposes many Java APIs for use.
exl-id: 0be33ec9-a4c3-4400-99d3-ed8366c5b5f9
---
# Java API Guidelines {#java-api-guidelines}

Adobe Experience Manager (AEM) is built on a rich open-source software stack that exposes many Java APIs for use during development.

AEM is built on the following four primary Java API sets in descending order of preference.

1. **[Adobe Experience Manager (AEM)](https://docs.adobe.com/content/help/en/experience-manager-cloud-service-javadoc/index.html)** - Product abstractions such as pages, assets, workflows, etc.
1. **[Apache Sling Web Framework](https://sling.apache.org/apidocs/sling11/)** - REST and resource-based abstractions such as resources, value maps, and HTTP requests.
1. **[JCR (Apache Jackrabbit Oak)](http://jackrabbit.apache.org/oak/docs/oak_api/overview.html)** - Data and content abstractions such as node, properties and sessions.
1. **[OSGi (Apache Felix)](https://felix.apache.org)** - OSGi application container abstractions such as services and (OSGi) components.

If an API is provided by AEM, prefer it over Sling, JCR, and OSGi. If AEM doesn’t provide an API, then prefer Sling over JCR and OSGi.

For details of these guidelines, see the document [Understand Java API Best Practices.](https://experienceleague.adobe.com/docs/experience-manager-learn/foundation/development/understand-java-api-best-practices.html)
