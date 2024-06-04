---
title: Working with Your Own GitHub Repositories in Cloud Manager
description: Learn how to set up Cloud Manager to work with your own GitHub repositories.
feature: "Cloud Manager, Developing"
exl-id: 15178de8-8a8a-4300-8510-88875ad0fc8c
solution: Experience Manager
role: "Admin, Architect, Developer"
---

# Working with Your Own GitHub Repositories in Cloud Manager {#byo-github}

By configuring Cloud Manager to work with your own GitHub repositories, you can validate your code directly within your GitHub repository through Cloud Manager, eliminating the need to consistently sync your code with the Adobe repository.

>[!NOTE]
>
>This feature is only available to [the early adopter program.](/help/implementing/cloud-manager/release-notes/current.md#early-adoption)

>[!NOTE]
>
>This feature is exclusive to public GitHub. Support for self-hosted GitHub is not available.

## Configuration {#configuration}

Configuration consists of two main steps:

1. [Add repository](#add-repo)
1. [Private repository ownership validation](#validate-ownership)

### Add Repository {#add-repo}

1. In Cloud Manager, from the **Program Overview** page, select the **Repositories** tab to switch to the **Repositories** page and click **Add Repository**.

1. In the **Add Repository** dialog, select **Private Repository** as the repository type.

1. Provide the details of your repository

   * **Repository Name** - An expressive name
   * **Repository URL** - The URL of the repository, which must end in `.git`
   * **Description** (optional) - A longer description of the repository as necessary

   ![Add own repository](/help/implementing/cloud-manager/assets/repos/add-own-github.png)

1. Select **Save**.

>[!TIP]
>
>For details about managing repositories in Cloud Manager, see [Cloud Manager Repositories](/help/implementing/cloud-manager/managing-code/cloud-manager-repositories.md).

### Private Repository Ownership Validation {#validate-ownership}

Cloud Manager now knows about your GitHub repository, but it still needs access to it. To grant access, you need to install the Adobe GitHub app and verify that you own the specified repository.

1. After adding your own repository, the **Private Repository Ownership Validation** dialog opens.

   ![Private Repository Ownership Validation](/help/implementing/cloud-manager/assets/repos/private-repo-validate.png)

1. Cloud Manager uses a GitHub app to securely interact with your repository.
   * An owner of your GitHub organization must install the app located at `https://github.com/apps/cloud-manager-for-aem` and grant access to the repository.
   * See GitHub's documentation for details on how this is done.

1. To enhance security, you must create a secret file in the default branch of your repository. Select **Generate**.

1. Confirm the generation of the secret file by tapping or clicking **Confirm**.

    ![Confirm secret generation](/help/implementing/cloud-manager/assets/repos/confirm-generation.png)

1. Back in the **Private Repository Ownership Validation** window, Cloud Manager has generated the content of the private fil in the **Secret file content** field. Copy the content from that field.

    * The contents of the secret file will only be shown once. If you do not copy the content before closing this window, regenerate the secret.

    ![Copy secret file content](/help/implementing/cloud-manager/assets/repos/new-secret.png)

1. Create a new file in the default branch of your GitHub repo called `.well-known/adobe/cloud-manager-challenge` and paste the secret file content into that file and save.

1. Once the app is installed and the secret file exists in the repository, you can select **Validate** in the **Private Repository Ownership Validation** dialog.

The app can be installed and secret file can be created in any order. However both steps must be completed before you can validate.

Until validation, the repository will be listed with a red icon, indicating that it is not yet validated and cannot yet be used.

![Unvalidated repo](/help/implementing/cloud-manager/assets/repos/unvalidated-repo.png)

The **Type** column easily identifies Adobe-provided repositories (**Adobe**) and your own GitHub repositories (**GitHub**).

If you need to return to the repository at a later date to complete the validation, on the **Repositories** page, select the ellipsis button in the row representing the GitHub repository you just added and select **Ownership Validation** from the drop-down menu.

## Using Your Own GitHub Repositories with Cloud Manager {#using}

After the GitHub repository is validated in Cloud Manager the integration is completed and you can use the repository with Cloud Manager.

1. When you create a pull request, a GitHub check will start automatically.

    ![GitHub checks](/help/implementing/cloud-manager/assets/repos/github-checks.png)

1. For each pull request, a [full stack code quality pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) will be created automatically. This pipeline is started at each pull request update.

1. The GitHub check remains in a running state until the code quality checks complete. The code quality results will then be propagated to the GitHub check.

    ![GitHub code quality checks](/help/implementing/cloud-manager/assets/repos/github-code-quality.png)

When the pull request is closed or merged, the full stack code quality pipeline created is automatically deleted.

## Limitations {#limitations}

Limitations when using your own GitHub repositories with Cloud Manager.

* You cannot use the GitHub repositories as the direct repository source for the pipelines you manage.
  * This functionality is planned.
* You cannot pause the pull request validation using the GitHub check from cloud manager.
  * If the GitHub repository is validated in Cloud Manager, Cloud Manager will always try to validate the pull requests created for that repository.
If the Adobe GitHub app is removed from your GitHb organization, this will remove the pull requests validation feature for all repositories.
