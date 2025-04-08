---
title: Submitting an AEM Connector
description: Learn how to correctly reference and deploy connectors in Adobe Experience Manager (AEM) as a Cloud Service.
exl-id: 9be1f00e-3666-411c-9001-c047e90b6ee5
feature: Operations
role: Admin
---
# Submitting an AEM Connector

Provided below is useful information for submitting Adobe Experience Manager (AEM) Connectors and should be read with articles about [implementing](implement.md) and  [maintaining](maintain.md) connectors.

AEM Connectors are listed on the [Adobe Exchange](https://partners.adobe.com/technologyprogram/experiencecloud.html).

In previous AEM solutions, [Package Manager](/help/implementing/developing/tools/package-manager.md) was used to install connectors on various AEM instances. However, with AEM as a Cloud Service, connectors are deployed during the CI/CD process in Cloud Manager. For the connectors to be deployed, connectors must be referenced in the maven project's pom.xml.

There are various options of how the packages can be included in a project:

1. Partner's public repository - a partner would host the content package in a publicly accessible maven repository
1. Partner's password-protected repository - a partner would host the content package in a password-protected maven repository. See [password-protected maven repositories](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/create-application-project/setting-up-project.html#password-protected-maven-repositories) for instructions.
1. Bundled artifact - in this case, the connector package is included locally in the customer's maven project.

Regardless of where they are hosted, packages must be referenced as dependencies in the pom.xml, as provided by the vendor.

```xml
<!-- UberJAR Dependency to be added to the project's Reactor pom.xml -->
<dependency>
  <groupId>com.partnername</groupId>
  <artifactId>my-artifact</artifactId>
  <version>V123</version> <!-- use the latest! -->
  <scope>provided</scope>
  <classifier>my_classifier</classifier>
</dependency>
```

If the ISV partner hosts the connector on an internet-accessible (such as Cloud Manager accessible) maven repository, the ISV should provide the repository configuration where the `pom.xml` can be placed. The reason is so the connector dependencies (above) can be resolved at build time, both locally, and by Cloud Manager.

```xml
<repository>
    <id>the-repository</id>
    <name>The Repository Where the Connector is Hosted</name>
    <url>https://repo.partnername.com/repositories/aem_connector_repo</url>
    <releases>
        <enabled>true</enabled>
        <updatePolicy>never</updatePolicy>
    </releases>
    <snapshots>
        <enabled>false</enabled>
    </snapshots>
</repository>
```

If the ISV partner chooses to distribute the Connector as downloadable files, then the ISV should provide instructions. The instruction should describe how the files can be deployed to a local-filesystem maven repository that must be checked into Git as part of the AEM project. This ensures that Cloud Manager can resolve these dependencies.
