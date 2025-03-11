---
title: Add External Repositories in Cloud Manager - Limited beta
description: Learn how to add an external repository into Cloud Manager. Cloud Manager supports integration with GitHub Enterprise Server, GitLab, and Bitbucket repositories.
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
exl-id: aebda813-2eb0-4c67-8353-6f8c7c72656c
---
# Add external repositories in Cloud Manager - Limited beta {#external-repositories}

Learn how to add an external repository into Cloud Manager. Cloud Manager supports integration with GitHub Enterprise Server, GitLab, and Bitbucket repositories.

>[!NOTE]
>
>This feature is only available through the early adoption program. For more details and to sign up as an early adopter, see [Bring Your Own Git - now with support for GitLab and Bitbucket](/help/implementing/cloud-manager/release-notes/2024/2024-10-0.md#gitlab-bitbucket).

## Configure an external repository

Configuration of an external repository in Cloud Manager consists of three steps:

1. [Add an external repository](#add-external-repo) to a selected program.
1. Provide an access token to the external repository.
1. Validate ownership of the private GitHub repository.



## Add an external repository {#add-ext-repo}

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program to which you want to link an external repository.

1. In the side menu, under **Services**, click ![Folder outline icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_FolderOutline_18_N.svg) **Repositories**.

   ![The Repositories page](/help/implementing/cloud-manager/managing-code/assets/repositories-tab.png)

1. Near the upper-right corner of the **Repositories** page, click **Add Repository**.

1. In the **Add Repository** dialog box, select **Private Repository** to link an external Git repository to your program.
 
   ![Add own repository](/help/implementing/cloud-manager/managing-code/assets/repositories-private-repo-type.png)

1. In each respective field, provide the following details about your repository: 

    | Field | Description |
    | --- | --- |
    | **Repository Name** | Required. An expressive name for your new repository. | 
    | **Repository URL** | Required. The URL of the repository.<br><br>If you are using a GitHub-hosted repository, the path must end in `.git`.<br>For example, *`https://github.com/org-name/repo-name.git`* (URL path is for illustration purposes only).<br><br>If you are using an external repository, it must use the following URL path format:<br>`https://git-vendor-name.com/org-name/repo-name.git`<br> or<br>`https://self-hosted-domain/org-name/repo-name.git`<br>And match your Git vendor. |
    | **Select Repository Type** | Required. Select the repository type that you are using:<ul><li>**GitHub** (GitHub Enterprise Server and the self-hosted version of GitHub)</li><li>**GitLab** (both `gitlab.com` and the self-hosted version of GitLab) </li><li>**Bitbucket** (both `bitbucket.org` and Bitbucket Server, and the self-hosted version of Bitbucket)</li></ul>If the repository URL path above includes the Git vendor name, such as GitLab or Bitbucket, the repository type is already pre-selected for you. |
    | **Description** | Optional. A detailed description of the repository. |

1. Select **Save** to add the repository.

1. In the **Private Repository Ownership Validation** dialog box, provide an access token to validate ownership of the external repository so you can access it.

    ![Selecting an existing access token for a repository](/help/implementing/cloud-manager/managing-code/assets/repositories-exisiting-access-token.png)
    *Selecting an existing access token for a Bitbucket repository.*

    | Token type | Description |
    | --- | --- |
    | **Use existing Access Token** | If you have already provided a repository access token for your organization and have access to multiple repositories, you can select an existing token. Use the **Token Name** drop-down list to choose the token you want to apply to the repository. Otherwise, add a new access token. |
    | **Add new Access Token** |**Repository type: GitHub**<br>&bull; In the **Token Name** text field, type a name for the access token you are creating.<br>&bull; Create a personal access token by following the instructions in the [GitHub documentation](https://docs.github.com/en/enterprise-server@3.14/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).<br>&bull; For required permissions, see the following information: ![Create new PAT for GitHub](/help/implementing/cloud-manager/managing-code/assets/webhook-github-enterprise-server.png)<br>&bull; In the **Access Token** field, paste the token you just created. | 
    |  | **Repository type: GitLab**<br>&bull; In the **Token Name** text field, type a name for the access token you are creating.<br>&bull; Create a personal access token by following the instruction in the [GitLab documentation](https://docs.gitlab.com/user/profile/personal_access_tokens/).<br>&bull; For required permissions, see the following information: ![Create a new PAT for GitLab](/help/implementing/cloud-manager/managing-code/assets/webhook-gitlab.png)<br>&bull; In the **Access Token** field, paste the token you just created. |    
    |  | **Repository type: Bitbucket**<br>&bull; In the **Token Name** text field, type a name for the access token you are creating.<br>&bull; Create a repository access token using the [Bitbucket documentation](https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-access-token/).<br>&bull; For required permissions, see the following information ![Create a new PAT for Bitbucket](/help/implementing/cloud-manager/managing-code/assets/webhook-bitbucket.png). |

    >[!NOTE]
    >
    >The feature **Add new Access Token** is currently in the Early Adopters phase. Additional functionalities are being planned. As a result, the required permissions for access tokens may change. Additionally, the user interface for managing tokens may be updated, potentially including features like token expiration dates. And, automated checks to ensure that tokens linked to repositories remain valid. 

1. Click **Validate**.

After validation, the external repository is ready to use and link to a pipeline.

## Link a validated external repository to a pipeline {#validate-ext-repo}

1. Add or edit a pipeline:
    * [Add a production pipeline](/help/implementing/cloud-manager/configuring-pipelines/configuring-production-pipelines.md)
    * [Add a non-production pipelines](/help/implementing/cloud-manager/configuring-pipelines/configuring-non-production-pipelines.md)
    * [Edit a pipeline](/help/implementing/cloud-manager/configuring-pipelines/managing-pipelines.md#editing-pipelines)

    ![Pipeline's source code repository and Git branch](/help/implementing/cloud-manager/managing-code/assets/pipeline-repo-gitbranch.png)
    *Add Non-Production Pipeline dialog box with selected repository and Git branch,*  

1. When adding or editing a pipeline, to specify the **Source Code** location for your new or existing pipeline, choose the external repository you want to use from the **Repository** drop-down list. 

1. In the **Git Branch** drop-down list, select the branch as the source for the pipeline.

1. Click **Save**.


>[!TIP]
>
>For details about managing repositories in Cloud Manager, see [Cloud Manager Repositories](/help/implementing/cloud-manager/managing-code/managing-repositories.md).

## Configure a webhook for an external repository {#configure-webhook}

Cloud Manager lets you configure webhooks for external Git repositories that you have added. See [Add an external repository](#add-ext-repo). These webhooks permit Cloud Manager to receive events that are related to different actions within your Git vendor solution.

For example, webhooks allow Cloud Manager to trigger actions based on events such as the following:

* Pull request (PR) creation – Initiates PR validation functionality.
* Push events – Starts pipelines when the "On Git Commit" trigger is turned on (enabled).
* Future comment-based actions – Allows workflows, such as direct deployment from a PR, to a Rapid Development Environment (RDE).

Webhook configuration is not required for repositories hosted on `GitHub.com` because Cloud Manager integrates directly through the GitHub app.
For all other external repositories that are onboarded with an access token, such as GitHub Enterprise Server, GitLab, and Bitbucket, webhook configuration is available and must be set up manually.

**To configure a webhook for an external repository:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program to which you want to configure a webhook for an external Git repository.

1. In the upper-left corner of the page, click ![Show menu icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_ShowMenu_18_N.svg) to reveal the left side menu.

1. In the left side menu, Under the **Program** heading, click ![Folder outline icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_FolderOutline_18_N.svg) **Repositories**.

1. On the **Repositories** page, using the **Type** column to guide you in your selection, locate the repository you want, then click ![Ellipsis - More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) next to it.

   ![Config Webhook option on drop-down menu for a selected repository](/help/implementing/cloud-manager/managing-code/assets/repository-config-webhook.png)

1. From the drop-down menu, click **Config Webhook**.

    ![Configure Webhook dialog box](/help/implementing/cloud-manager/managing-code/assets/config-webhook.png)

1. In the **Config Webhook** dialog box, do the following:

    1. Next to the **Webhook URL** field, click ![Copy icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Copy_18_N.svg).
    Paste the URL in a plain text file. The copied URL is required for your Git vendor's Webhook settings.
    1. Next to the **Webhook Secret** token/key field, click **Generate**, then click ![Copy icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_Copy_18_N.svg).
    Paste the secret in a plain text file. The copied secret is required for your Git vendor's Webhook settings.
1. Click **Close**. 
1. Navigate to your Git vendor solution (GitHub Enterprise, GitLab, or Bitbucket).
1. Locate the solution's **Webhook** Settings section.
1. Paste the Webhook URL that you copied earlier into the URL text field.
    1. Replace the `api_key` query parameter in the Webhook URL with your own real API key.

        To generate an API key, you must create an integration project in Adobe Developer Console. See [Creating an API Integration Project](https://developer.adobe.com/experience-cloud/cloud-manager/guides/getting-started/create-api-integration/) for full details.
    
1. Paste the Webhook Secret that you copied earlier into the **Secret** (or **Secret key**, or **Secret token**) text field.
1. Configure the webhook to send the appropriate events that Cloud Manager expects.

    All the details on the webhook configuration and the events that are required for each vendor are available at the following:

    * [Set up webhooks for GitHub Enterprise Server](https://git.corp.adobe.com/pages/experience-platform/cloud-manager-repository-service/#/./git-vendors/create-new-github-pat?id=webhook-events).
    * [Set up webhooks for GitLab](https://git.corp.adobe.com/pages/experience-platform/cloud-manager-repository-service/#/./git-vendors/create-new-gitlab-pat?id=webhook-events).
    * [Set up webhooks for Bitbucket](https://git.corp.adobe.com/pages/experience-platform/cloud-manager-repository-service/#/./git-vendors/create-new-bitbucket-pat?id=webhook-events).

### Validation of pull requests with webhooks

After webhooks are correctly configured, Cloud Manager automatically triggers pipeline executions or PR validation checks for your repository. 

The following behaviors apply:

* **GitHub Enterprise Server**

    When the check is created, it appears like the following screenshot below. The key difference from `GitHub.com` is that `GitHub.com` uses a check-run, while GitHub Enterprise Server (using personal access tokens) generates a commit status:

    ![Commit status to indicate PR validation process on GitHub Enterprise Server](/help/implementing/cloud-manager/managing-code/assets/repository-webhook-github-pr-validation.png)

* **Bitbucket**

    When code quality validation is running:

    ![Status while code quality validation is running](/help/implementing/cloud-manager/managing-code/assets/repository-webhook-bitbucket1.png)

    Uses commit status for tracking PR validation progress. In the following case, the screenshot shows what happens when a code quality validation fails due to a customer issue. A comment is added with detailed error information, and a commit check is created, which shows the failure (visible on the right):

    ![Pull request validation status for Bitbucket](/help/implementing/cloud-manager/managing-code/assets/repository-webhook-bitbucket2.png)

* **GitLab**

    GitLab interactions rely solely on comments. When validation begins, a comment is added. When validation is complete (whether successful or failed), the initial comment is removed and replaced with a new comment containing validation results or error details.

    When code quality validation is running:

    ![When code quality validation is running](/help/implementing/cloud-manager/managing-code/assets/repository-webhook-gitlab1.png)

    When cold quality validation is finished:

    ![When cold quality validation is finished](/help/implementing/cloud-manager/managing-code/assets/repository-webhook-gitlab2.png)

    When code quality validation fails with an error:

    ![When code quality validation fails with an error](/help/implementing/cloud-manager/managing-code/assets/repository-webhook-gitlab3.png)

    When the code quality validation fails due to customer issues:

    ![When the code quality validation fails due to customer issues](/help/implementing/cloud-manager/managing-code/assets/repository-webhook-gitlab4.png)


## Troubleshoot webhook issues

* Ensure that the Webhook URL includes a valid API key.
* Check that webhook events are correctly configured in your Git vendor settings.
* If PR validation or pipeline triggers are not working, verify that the Webhook Secret is up to date in both Cloud Manager and your Git vendor.








## Limitations

* External repositories cannot be linked to Configuration pipelines.
* Pipelines with external repositories (not hosted on GitHub) and the "On Git Changes" trigger do not start automatically. They can only be initiated manually.


<!-- THIS BULLET REMOVED AS PER https://wiki.corp.adobe.com/display/DMSArchitecture/Cloud+Manager+2024.12.0+Release. THEY CAN NOW START AUTOMATICALLY>
* Pipelines using external repositories (excluding GitHub-hosted repositories) and the **Deployment Trigger** option [!UICONTROL **On Git Changes**], triggers are not automatically started. They must be manually started. -->


