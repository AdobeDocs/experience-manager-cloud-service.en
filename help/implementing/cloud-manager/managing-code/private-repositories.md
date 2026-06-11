---
title: Add a private GitHub Repository in Cloud Manager
description: Learn how to set up Cloud Manager to work with your own private GitHub repositories.
exl-id: 5232bbf5-17a5-4567-add7-cffde531abda
feature: Cloud Manager, Developing
role: Admin, Developer
---
# Add a private GitHub Enterprise Cloud repository in Cloud Manager {#private-repositories}

By setting up Cloud Manager to integrate with your private GitHub Cloud (repositories hosted on `github.com`), you can validate your code directly within GitHub using Cloud Manager. This configuration removes the requirement to sync your code regularly with the Adobe repository.

>[!IMPORTANT]
>Cloud Manager validates GitHub repository ownership in one of the following two ways, depending on where the repository is hosted:
>
>* This page applies to repositories hosted on `github.com`, including GitHub Enterprise Cloud deployments hosted on `github.com`. These repositories use the Adobe GitHub app to validate ownership. No webhook configuration is required because Cloud Manager integrates directly through the app.
>* If you want to add any of the following repository types, see [Add external repositories in Cloud Manager](/help/implementing/cloud-manager/managing-code/external-repositories.md). These repositories use a PAT (Personal Access Token) and a manually configured webhook to validate ownership.
>
>   * GitHub Enterprise Server (self-hosted version of GitHub) repositories.
>   * GitLab (both `gitlab.com` and the self-hosted version of GitLab) repositories.
>   * Bitbucket (only `bitbucket.org`, cloud version) repositories. The self-hosted version of Bitbucket was deprecated as of February 15, 2024.
>   * Azure DevOps (`dev.azure.com`) repositories.

## Configuration {#configuration}

Configuration of a private GitHub Cloud repository in Cloud Manager consists of two steps:

1. [Add a private GitHub Cloud repository](#add-repo) to a selected program.
1. Then, [validate ownership of the private GitHub Cloud repository](#validate-ownership).



### Add a private GitHub Cloud repository to a program {#add-repo}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program to which you want to link a private Git repository.

1. In the side menu, under **Services**, select ![Folder icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Folder_18_N.svg) **Repositories**.

   ![The Repositories page](/help/implementing/cloud-manager/managing-code/assets/repositories-tab.png)

1. Near the upper-right corner of the **Repositories** page, click **Add Repository**.

1. In the **Add Repository** dialog box, select **Private Repository** as the repository type.

   ![Add own repository](/help/implementing/cloud-manager/assets/repos/add-own-github.png)

1. In each respective field, provide the following details about your repository:

    | Field | Description |
    | --- | --- |
    | Repository Name | An expressive name for your new repository. |
    | Repository URL | The URL of the private repository, which must end in `.git`.<br>For example, *`https://github.com/org-name/repo-name.git`* (URL path is for illustration purposes only).  |
    | Description (optional) | A detailed description of the repository. |

1. Select **Save**.
    Now, you can [validate ownership of the private repository](#validate-ownership).

>[!TIP]
>
>For details about managing repositories in Cloud Manager, see [Cloud Manager Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md).


### Validate ownership of a private GitHub repository {#validate-ownership}

Cloud Manager is now configured with your GitHub repository, but it still requires authorization to access the repository. To grant access, you need to install the Adobe GitHub app and verify that you own the specified repository.

**To validate ownership of a private GitHub repository:**

1. After adding your repository, follow the remaining steps in the **Private Repository Ownership Validation** dialog box.

   ![Private Repository Ownership Validation](/help/implementing/cloud-manager/assets/repos/private-repo-validate.png)

    |  | Description |
    | --- | --- |
    | **Step 1: GitHub App** | Cloud Manager uses a GitHub app to interact with your private repository securely.<br>&bull; An owner of your GitHub organization must install the app located at `https://github.com/apps/cloud-manager-for-aem` and grant access to the repository.<br>&bull; For details on installing and granting access is done, see GitHub's documentation. |
    | **Step 2: Secret File** | To enhance security, you must create a secret file in the default branch of your repository.<br>&bull; Click **Generate**, then click **Confirm**. Cloud Manager generates the content of the private file in the **Secret file content** text field.<br>&bull; Click ![Copy icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Copy_18_N.svg) to copy the content from that field. The contents of the secret file is only shown once. If you do not copy the content before closing this dialog box, regenerate the secret. |

1. Create a new file in the default branch of your GitHub repository with the name

    `.well-known/adobe/cloud-manager-challenge`
    
1. Paste the secret file content into the new file, and save.

    Once the app is installed and the secret file exists in the repository, continue the steps.

1. In the **Private Repository Ownership Validation** dialog box, click **Validate**.

The app can be installed and a secret file can be created in either order. However, both steps must be completed before you can validate.

Until validation, the repository is listed with a red icon, indicating that it is not yet validated and is not available for use.

![Unvalidated repo](/help/implementing/cloud-manager/assets/repos/unvalidated-repo.png)

The **Type** column in the table on the **Repositories** page identifies Adobe-provided repositories (**Adobe**) and your own private repositories (**GitHub**).

To access the repository later to complete the validation, on the **Repositories** page, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) in the row representing the GitHub repository you added. In the drop-down list, select **Ownership Validation**.


## Use private GitHub Cloud repositories with Cloud Manager {#using}

After the GitHub repository is validated in Cloud Manager, the integration is complete. You can use the repository with Cloud Manager.

**To use private GitHub Cloud repositories with Cloud Manager:**

1. When you create a pull request, a GitHub check starts automatically.

    ![GitHub checks](/help/implementing/cloud-manager/assets/repos/github-checks.png)

1. For each pull request, a [full stack code quality pipeline](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md) is created automatically. This pipeline is started at each pull request update.

1. The GitHub check remains in a running state until the code quality check is complete. The code quality results are then propagated to the GitHub check.

    ![GitHub code quality checks](/help/implementing/cloud-manager/assets/repos/github-code-quality.png)

When the pull request is merged or closed, the full stack code quality pipeline created is automatically deleted.

>[!TIP]
>
>See [GitHub Check Annotations](github-annotations.md) for details on the information provided through GitHub when pull request checks are run.

>[!TIP]
>
>You can control the pipelines that are created automatically to validate each pull request to a private repository. See [GitHub Check Configuration for Private Repositories](github-check-config.md) for more information.



## Associate private GitHub Cloud repositories with pipelines {#pipelines}

Validated private repositories can be associated with [full-stack and frontend pipelines](/help/implementing/cloud-manager/configuring-pipelines/introduction-ci-cd-pipelines.md).



## Limitations {#limitations}

The following limitations apply when using private repositories with Cloud Manager.

* No Git tag is created and pushed when using private repositories on production full stack pipelines.
* If the Adobe GitHub app is removed from your GitHub organization, it removes the pull request validation feature for all repositories.
* Pipelines using private GitHub Cloud repositories and the "on-commit" build trigger are not started automatically when a new commit is pushed into the selected branch.
* [Artifact reuse functionality](/help/implementing/cloud-manager/getting-access-to-aem-in-cloud/setting-up-project.md#build-artifact-reuse) does not apply to private repositories.
* You cannot pause the pull request validation using the GitHub check from Cloud Manager. If the GitHub repository is validated in Cloud Manager, Cloud Manager always tries to validate the pull requests created for that repository.
* If your GitHub organization enforces IP restrictions, open a support case to obtain the list of IP addresses that must be allowed.
