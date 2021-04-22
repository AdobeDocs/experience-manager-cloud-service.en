---
title: Submitting an AEM Connector
description: Submitting an AEM Connector
exl-id: 9be1f00e-3666-411c-9001-c047e90b6ee5
---
Submitting an AEM Connector
===========================

Provided below is useful information for submitting AEM Connectors and should be read in conjunction with articles about [implementing](implement.md) and  [maintaining](maintain.md) connectors.

AEM Connectors are listed on the [Adobe Exchange](https://partners.adobe.com/exchangeprogram/experiencecloud).

In previous AEM solutions, Package Manager was used to install connectors on various AEM instances. However, with AEM as a Cloud Service, connectors are deployed during the CI/CD process in Cloud Manager. In order for the connectors to be deployed, connectors need to be referenced in the maven project's pom.xml. 

There are various options of how the packages can be included in a project:

1. Partner's public repository - a partner would host the content package in a publicly accessible maven repository
1. Partner’s password protected repository - a partner would host the content package in a password protected maven repository. See [password protected maven repositories at](/help/onboarding/getting-access-to-aem-in-cloud/setting-up-project.md#password-protected-maven-repositories) for instructions.
1. Bundled artifact - in this case, the connector package is included locally in the customer's maven project.

Regardless of where they're hosted, packages need to be referenced as dependencies in the pom.xml, as provided by the vendor.

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

If the ISV partner hosts the connector on a internet accessible (such as Cloud Manager accessible) maven repository, the ISV should provide the repository configuration  where the pom.xml can be placed, so the connector dependencies (above) can be resolved at build time (both locally, and by Cloud Manager).

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

If the ISV partner chooses to distribute the Connector as downloadable files, then the ISV should provide instructions on how the files can be deployed to a local-filesystem maven repository that needs to be checked into Git as part of the AEM project, so that Cloud Manager can resolve these dependencies.
