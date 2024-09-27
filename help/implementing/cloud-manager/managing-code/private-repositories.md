---
title: Add Private Repositories in Cloud Manager
description: Learn how to set up Cloud Manager to work with your own private GitHub repositories.
exl-id: 5232bbf5-17a5-4567-add7-cffde531abda
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---
# Add private repositories in Cloud Manager {#private-repositories}

By setting up Cloud Manager to integrate with your private GitHub repositories, you can validate your code directly within GitHub using Cloud Manager. This configuration removes the requirement to regularly sync your code with the Adobe repository.

>[!NOTE]
>
>This feature is exclusive to public GitHub. Support for self-hosted GitHub is not available.

## Configuration {#configuration}

Configuration of a private repository in Cloud Manager consists of two steps:

1. First, [add a private repository](#add-repo).
1. Second, [validat ownership of the private repository](#validate-ownership).

### Add a private repository {#add-repo}

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
>For details about managing repositories in Cloud Manager, see [Cloud Manager Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md).

### Private repository ownership validation {#validate-ownership}

Cloud Manager now knows about your GitHub repository, but it still needs access to it. To grant access, you need to install the Adobe GitHub app and verify that you own the specified repository.

1. After adding your own repository, the **Private Repository Ownership Validation** dialog opens.

   ![Private Repository Ownership Validation](/help/implementing/cloud-manager/assets/repos/private-repo-validate.png)

1. Cloud Manager uses a GitHub app to interact with your repository securely.
   * An owner of your GitHub organization must install the app located at `https://github.com/apps/cloud-manager-for-aem` and grant access to the repository.
   * For details on installing and granting access is done, see GitHub's documentation.

1. To enhance security, you must create a secret file in the default branch of your repository. Select **Generate**.

1. Confirm the generation of the secret file by clicking **Confirm**.

    ![Confirm secret generation](/help/implementing/cloud-manager/assets/repos/confirm-generation.png)

1. In the **Private Repository Ownership Validation** dialog box, Cloud Manager has generated the content of the private file in the **Secret file content** field. 

1. Click ![Copy icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Copy_18_N.svg) to copy the content from that field.

    The contents of the secret file is only shown once. If you do not copy the content before closing this dialog box, regenerate the secret.

    ![Copy secret file content](/help/implementing/cloud-manager/assets/repos/new-secret.png)

1. Create a new file in the default branch of your GitHub repo called:

    `.well-known/adobe/cloud-manager-challenge`
    
1. Paste the secret file content into the new file you just created, and save.

    Once the app is installed and the secret file exists in the repository, continue with the steps.

1. In the **Private Repository Ownership Validation** dialog box, click **Validate**.

The app can be installed and a secret file can be created in any order. However, both steps must be completed before you can validate.

Until validation, the repository is listed with a red icon, indicating that it is not yet validated and cannot yet be used.

![Unvalidated repo](/help/implementing/cloud-manager/assets/repos/unvalidated-repo.png)

The **Type** column in the table on the **Repositories** page identifies Adobe-provided repositories (**Adobe**) and your own GitHub repositories (**GitHub**).

If you need to return to the repository later to complete the validation, on the **Repositories** page, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) in the row representing the GitHub repository you just added. In the drop-down list, select **Ownership Validation**.

## Use private repositories with Cloud Manager {#using}

After the GitHub repository is validated in Cloud Manager, the integration is completed. You can use the repository with Cloud Manager.

1. When you create a pull request, a GitHub check starts automatically.

    ![GitHub checks](/help/implementing/cloud-manager/assets/repos/github-checks.png)

1. For each pull request, a [full stack code quality pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) is created automatically. This pipeline is started at each pull request update.

1. The GitHub check remains in a running state until the code quality check is complete. The code quality results are then propagated to the GitHub check.

    ![GitHub code quality checks](/help/implementing/cloud-manager/assets/repos/github-code-quality.png)

When the pull request is closed or merged, the full stack code quality pipeline created is automatically deleted.

>[!TIP]
>
>See the document [GitHub Check Annotations](github-annotations.md) for details on the information provided by way of GitHub when pull request checks are run.

>[!TIP]
>
>You can control the pipelines that are created automatically to validate each pull request to a private repository. See [GitHub Check Configuration for Private Repositories](github-check-config.md) for more information.

## Associate private repositories with pipelines {#pipelines}

Validated private repositories can be associated with [full-stack and frontend pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md).

>[!NOTE]
>
>Web tier and config pipelines are not supported with private repositories.

## Limitations {#limitations}

Certain limitations apply when using private repositories with Cloud Manager.

* You cannot pause the pull request validation using the GitHub check from Cloud Manager.
If the GitHub repository is validated in Cloud Manager, Cloud Manager always tries to validate the pull requests created for that repository.
* If the Adobe GitHub app is removed from your GitHub organization, it removes the pull requests validation feature for all repositories.
* Web tier and config pipelines are not supported with private repositories.
* No Git tag is created and pushed when using private repositories on production full stack pipelines.
* Pipelines using private repositories and the on-commit build trigger are not started automatically when a new commit is pushed into the selected branch.
* [Artifact reuse functionality](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/setting-up-project.md#build-artifact-reuse) does not apply to private repositories.
