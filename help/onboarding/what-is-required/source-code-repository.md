---
title: Source Code Repository - Cloud Services
description: Source Code Repository - Cloud Services
---

# Source Code Repository {#source-code-repository} 

Cloud Manager program will come auto-provisioned with it’s own git repository. 

For a user to access the Cloud Manager git repository, users will need to use a Git client with a command-line tool, a standalone visual Git client, or the user's IDE such as Eclipse, IntelliJ, NetBeans. 

To learn about how to  manage Git using Cloud Manager UI, refer to [Manage your Git](/help/implementing/cloud-manager/configure-pipeline.md).

Once a Git client is set up, the user can select the **Manage Git** button from the **Piplelines** card to get the information necessary to access Cloud Manager Git repository.

To learn about how to  manage Git using Cloud Manager UI, refer to [Configure your CI/CD Pipeline](/help/implementing/cloud-manager/configure-pipeline.md).

The important considerations to manage your git in Cloud Manager are:

* **URL**: The repository URL
* **Username**: The user name
* **Password**: The value shown when the **Generate Password** button is clicked.

To begin developing the AEM Cloud application, a local copy of the application code must be made by checking it out from the Cloud Manager repository to a location on their local computer where they wish to create their repository.

```java
$ git clone {URL}
```

> [!NOTE]
> A user can check out a copy of their code, and make changes in the local code repository. When ready, the user can commit their code changes back to the remote code repository in Cloud Manager.
