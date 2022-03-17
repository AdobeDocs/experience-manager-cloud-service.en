---
title: Accessing Repositories
description: Learn how to access and manage your git repository using the self-service git account management from Cloud Manager.
exl-id: 0c0671a3-e400-46f3-ad86-166a6cfdd44b
---
# Accessing Repositories {#accessing-repos}

Learn how to access and manage your git repository using the self-service git account management from Cloud Manager.

## Using Self-Service Repository Account Management {#self-service-repos}

Cloud Manager makes it easy to retrieve your repository info by using the **Access Repo Info** button available prominently on the pipeline card.

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization and program.

1. Navigate to **Pipelines** card from your **Program Overview** page and find the **Access Repo Info** button to access and manage your git Repository.

   ![Access Repo Info button on Environments card](/help/implementing/cloud-manager/assets/repos/access-repo1.png)

1. Click on the **View Repo Info** button to open a dialog to view:

   * The URL to the Cloud Manager git repository.
   * The git username.
   * The git password, the value of which is shown when the **Generate Password** button is clicked.

   ![](/help/implementing/cloud-manager/assets/repos/access-repo-create.png)

Using these credentials, the user can clone a local copy of the repository, and make changes in that local repository, and when ready can commit any code changes back to the remote code repository in Cloud Manager.

The **Access Repo Info** option is also available on the **Non-Production** pipeline tab of the **Pipelines** card.

![Access Repo Info button on non-production tab](/help/implementing/cloud-manager/assets/repos/access-repo-nonprod.png)

>[!NOTE]
>
>The **Access Repo Info** option is visible to users with **Developer** or **Deployment Manager** roles.
