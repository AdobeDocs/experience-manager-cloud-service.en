---
title: Configure an Edge Delivery site to use an external Git repository
description: Learn how to link an Edge Delivery site to a private or enterprise Git repository.
feature: Cloud Manager, Developing
role: Admin, Developer
exl-id: 1dbaef34-efa3-4287-b7b1-f60db938146d
---
# Configure an Edge Delivery site to use an external Git repository

To pull code from any private Git repository already onboarded in Cloud Manager, you can configure your Edge Delivery site.

<!--
**Supported Git Vendors**

| Support level | Vendors | Notes |
| --- | --- | --- |
| General availability | &bull; GitHub Enterprise (self-hosted version)<br>&bull; Bitbucket (Cloud version)<br>&bull; GitLab (Cloud and self-hosted version) | Connect without enablement requests |
| Alpha program | Azure DevOps (Cloud version) | [Request access](mailto:grp-cloudmanager_byog@adobe.com) |
| Beta program | Adobe-hosted repository (created in Cloud Manager) | [Request access](mailto:grp-cloudmanager_byog@adobe.com) |
-->

**To use an external Git repository, configure an Edge Delivery site:**

{{sign-in-to-cloud-manager}}

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program with Edge Delivery Services configured. Select the program where you want to configure an Edge Delivery site to use an external Git repository.
1. In the left rail, under the **Program** heading, click **![Overview icon](/help/implementing/cloud-manager/edge-delivery/assets/overview.svg ) Overview**.
1. On the **Program Overview** page, click the **Edge Delivery** tab. 
1. In the **Edge Delivery sites** table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose site you want to configure to use an external repo, then click **Bring your own Git**.
1. In the **Bring your own Git** dialog box, in the **Repository Name** drop-down list, choose a Git repo with `READY` status, then click **Confirm**.
    
    Cloud Manager returns a one-time secret token. If you reconfigure the site, Cloud Manager generates a new secret token.

1. Copy the token and add it to the site configuration in **helix-admin**, as described in the [BYO Git guide](https://www.aem.live/developer/byo-git).
1. In Cloud Manager, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose site you configured to use an external repo, then click **Sync code**.
1. Pick the branch to sync, and click **Sync**.

Each commit on any branch now triggers an automatic sync. Use **Sync code** again whenever a full manual sync is required.

<!-- 
REMOVED AS PER CQDOC-23912 ON AUGUST 19, 2026
## Authenticate git clone requests {#authenticate-git-clone-requests}

You can clone your [!DNL Bring Your Own Git] repository from Cloud Manager using either an IMS token or the byogit secret that Cloud Manager generates when you configure the site. Both credentials authenticate against the clone endpoint, so you can use the secret that helix-admin already stores for [!DNL Edge Delivery Services] code sync.

The clone endpoint accepts the credential in the `Authorization` header. Cloud Manager validates the byogit secret against the value stored for that repository. Requests that include neither a valid IMS token nor a valid byogit secret return a `401` response.

>[!NOTE]
>
>Existing IMS-authenticated clone workflows are unaffected. The byogit secret is an additional option, not a replacement.

**To clone the repository with the byogit secret:**

1. Copy the secret that Cloud Manager returns when you configure the site.
1. Run your clone command, and pass the secret in the `Authorization` header.

   `git -c http.extraHeader="Authorization: <byogit-secret>"` clone `https://cm-repo.adobe.io/api/program/<program-id>/repository/<repository-id>.git`

    Replace `<byogit-secret>` with the secret from Cloud Manager, and replace `<program-id>` and `<repository-id>` with the values from your program.
-->

