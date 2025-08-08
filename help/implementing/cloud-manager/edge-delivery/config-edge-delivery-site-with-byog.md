---
title: Configure an Edge Delivery site to use an external Git repository
description: Learn how to link an Edge Delivery site to a private or enterprise Git repository.
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Configure an Edge Delivery site to use an external Git repository

You can configure your Edge Delivery site to pull code from any private Git repository already onboarded in Cloud Manager.

**Supported Git Vendors**

| Support level | Vendors | Notes |
| --- | --- | --- |
| General availability | &bull; GitHub Enterprise (self-hosted version)<br>&bull; Bitbucket (Cloud version)<br>&bull; GitLab (Cloud and self-hosted version) | Connect without enablement requests |
| Alpha program | Azure DevOps (Cloud version) | [Request access](mailto:grp-cloudmanager_byog@adobe.com) |
| Beta program | Adobe-hosted repository (created in Cloud Manager) |  [Request access](mailto:grp-cloudmanager_byog@adobe.com) |

**To configure an Edge Delivery site to use an external Git repository:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate program.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program with Edge Delivery Services configured, where you want to configure an Edge Delivery site to use an external Git repo.

1. In the left rail, under the **Program** heading, click **![Overview icon](/help/implementing/cloud-manager/edge-delivery/assets/overview.svg ) Overview**.

1. On the **Program Overview** page, click the **Edge Delivery** tab. 

1. In the **Edge Delivery sites** table, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose site you want to configure to use an external repo, then click **Bring your own Git**.

1. In the Bring your own Git dialog box, in the **Repository Name** drop-down list, choose a Git repo with `READY` status, then click **Confirm**.
    
    Cloud Manager returns a one-time secret token. If you reconfigure the site, Cloud Manager generates a new secret token.

1. Copy the token and add it the site configuration in **helix-admin**, as described in the [BYO Git guide](https://www.aem.live/developer/byo-git).

1. Back in Cloud Manager, click ![More icon](https://spectrum.adobe.com/static/icons/workflow_18/Smock_More_18_N.svg) at the end of a row whose site you just configured to use an external repo, then click **Sync code**.

1. Pick the branch to sync, and click **Sync**.

Each commit on any branch now triggers an automatic sync. Use **Sync code** again whenever a full manual sync is required.

