---
title: Maven Project Version Handling
description: For staging and production deployments of AEM as a Cloud Service, Cloud Manager generates a unique, incrementing version.
exl-id: 658bcbed-0733-45da-a3e3-9a5f817099c5
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Developer
product_v2:
  - id: fd1f54a9-f50c-467d-8956-cebbaf4f3eb8
    internal-label: Experience Manager
feature_v2:
  - id: a01bfd36-4ab8-4bf8-9dc0-5b45b890552e
    internal-label: APIs
subfeature_v2:
  - id: d9eb3b3e-9447-4ed4-bf4a-96c7b245cb27
    internal-label: Cloud Manager APIs
role_v2:
  - id: c66ffd68-0f65-42bb-aa23-b4020f12e0bd
    internal-label: Admin
  - id: ff6a42d2-313e-452e-93a6-792e4fad9ff8
    internal-label: Developer
---

# Maven project version handling {#maven-project-version-handling} 

For staging and production deployments of AEM as a Cloud Service, Cloud Manager generates a unique, incrementing version

This version is seen on the [pipeline execution details page](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#view-details) and the activity page. When a build is run, the Maven project is updated to use this version and a tag is created in the git repository with that version as its name. 

If the original project version meets certain criteria, the updated Maven project version merges both the original project version and the Cloud Manager generated version. The tag, however, always uses the generated version. For this merging to occur, the original project version must be formed with exactly three version segments, for example, `1.0.0` or `1.2.3`, but not `1.0` or `1`, and the original version must not end in `-SNAPSHOT`. 

>[!IMPORTANT]
>
>This original project version value must be statically set in the `<version>` element of the top-level `pom.xml` file in the git repository branch.

If the original version does not meet these criteria, the generated version is appended to the original version as a new version segment. The generated version is also adjusted to support accurate sorting and version management. For example, assuming a generated version of `2019.926.121356.0000020490` yields the following results.

| Version | Version in `pom.xml` | Comment |
| --- |--- | --- |
| `1.0.0` | `1.0.0.2019_0926_121356_0000020490` | Properly formed original version |
| `1.0.0-SNAPSHOT` | `2019.926.121356.0000020490` | Snapshot version, overwritten |
| `1` | `2019.926.121356.0000020490` | Incomplete version, overwritten |

>[!NOTE]
>
>Regardless of whether or not the original version was incorporated into the Cloud Manager-initialized version, the original version is available as a Maven property with the name `cloudManagerOriginalVersion`.
