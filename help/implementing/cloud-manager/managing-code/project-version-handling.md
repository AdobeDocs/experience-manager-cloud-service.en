---
title: Maven Project Version Handling
description: For staging and production deployments of AEM as a Cloud Service, Cloud Manager generates a unique, incrementing version. 
exl-id: 658bcbed-0733-45da-a3e3-9a5f817099c5
---

# Maven Project Version Handling {#maven-project-version-handling} 

For staging and production deployments of AEM as a Cloud Service, Cloud Manager generates a unique, incrementing version

This version is seen on the [pipeline execution details page](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#view-details) as well as the activity page. When a build is run, the Maven project is updated to use this version and a tag is created in the git repository with that version as its name. 

If the original project version meets certain criteria, the updated Maven project version will merge both the original project version and the Cloud Manager generated version. The tag, however, always uses the generated version. For this merging to occur, the original project version must be formed with exactly three version segments, for example, `1.0.0` or `1.2.3`, but not `1.0` or `1`, and the original version must not end in `-SNAPSHOT`. 

>[!IMPORTANT]
>
>This original project version value must be statically set in the `<version>` element of the top-level `pom.xml` file in the git repository branch.

If the original version does meet these criteria, then the generated version will be appended to the original version as a new version segment. The generated version will also be slightly modified to include proper sorting and version handling. For example, assuming a generated version of `2019.926.121356.0000020490` would have the following results.

| Version | Version in `pom.xml` | Comment |
|---|---|---|
| `1.0.0` |  `1.0.0.2019_0926_121356_0000020490` |  Properly formed original version |
| `1.0.0-SNAPSHOT` | `2019.926.121356.0000020490` | Snapshot version, overwritten | 
| `1` | `2019.926.121356.0000020490` |  Incomplete version, overwritten | 

>[!NOTE]
>
>Regardless of whether or not the original version was incorporated into the Cloud Manager-initialized version, the original version is available as a Maven property with the name `cloudManagerOriginalVersion`.
