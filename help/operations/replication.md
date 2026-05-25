---
title: Replication
description: Learn about distribution and troubleshooting replication in AEM as a Cloud Service.
exl-id: c84b4d29-d656-480a-a03a-fbeea16db4cd
feature: Operations
role: Admin
---
# Replication {#replication}

Adobe Experience Manager as a Cloud Service uses the [Sling Content Distribution](https://sling.apache.org/documentation/bundles/content-distribution.html) capability to move the content to replicate to a pipeline service run on Adobe Developer that is outside of the AEM runtime.

>[!NOTE]
>
>Read [Distribution](/help/overview/architecture.md#content-distribution) for more information.

## Methods of Publishing Content {#methods-of-publishing-content}

>[!NOTE]
>
>If you are interested in bulk publishing content, create a workflow using the [Tree Activation Workflow Step](/help/operations/tree-replication-workflows.md#tree-activation), which can efficiently handle large payloads. 
>It is not recommended to build your own bulk publishing custom code. 
>If you must customize for whatever reason, you can trigger a workflow with this step by using existing Workflow APIs. 
>It is always a good practice to only publish content that must be published. And be prudent about not trying to publish large numbers of content, if not necessary. However, there are no limits as to how much content you can send through workflows with the Tree Activation Workflow Step.

### Quick Un/Publish - Planned Un/Publish {#publish-unpublish}

This feature lets you publish the selected pages immediately, without the additional options possible through the Manage Publication approach.

For more information, see [Manage Publication](/help/sites-cloud/authoring/sites-console/publishing-pages.md#manage-publication).

### On and Off Times - Trigger Configuration {#on-and-off-times-trigger-configuration}

The additional possibilities of **On Time** and **Off Time** are available from the [Basic tab of Page Properties](/help/sites-cloud/authoring/sites-console/page-properties.md#basic).

To realize the automatic replication for this feature, enable **Auto Replicate** in the [OSGi configuration](/help/implementing/deploying/configuring-osgi.md) **On Off Trigger Configuration**: 

   ![OSGi On Off Trigger Configuration](/help/operations/assets/replication-on-off-trigger.png)

### Manage Publication {#manage-publication}

Manage Publication offers more options than Quick Publish, allowing for the inclusion of child pages, customization of the references, and starting any applicable workflows and offering the option to publish later.

Including a folder's children for the "publish later" option invokes the Publish Content Tree workflow, described in [Tree Replication Workflows](/help/operations/tree-replication-workflows.md#publish-content-tree-workflow).

You can find more detailed information on Manage Publication on the [Publishing Fundamentals documentation](/help/sites-cloud/authoring/sites-console/publishing-pages.md#manage-publication).

To replicate deep content hierarchies in bulk, use a workflow-based approach. See [Tree Replication Workflows](/help/operations/tree-replication-workflows.md) for the recommended Tree Activation workflow step, configuration parameters, and monitoring guidance. The deprecated Publish Content Tree workflow is also documented there for reference.

### Replication API {#replication-api}

You can publish content using the Replication API featured in AEM as a Cloud Service.

For more information, see the [API Documentation](https://javadoc.io/doc/com.adobe.aem/aem-sdk-api/latest/com/day/cq/replication/package-summary.html).

**Basic Usage of the API**

```
@Reference
Replicator replicator;
@Reference
ReplicationStatusProvider replicationStatusProvider;

....
Session session = ...
// Activate a single page to all agents, which are active by default
replicator.replicate(session,ReplicationActionType.ACTIVATE,"/content/we-retail/en");
// Activate multiple pages (but try to limit it to approx 100 at max)
replicator.replicate(session,ReplicationActionType.ACTIVATE, new String[]{"/content/we-retail/en","/content/we-retail/de"});

// ways to get the replication status
Resource enResource = resourceResolver.getResource("/content/we-retail/en");
Resource deResource = resourceResolver.getResource("/content/we-retail/de");
ReplicationStatus enStatus = enResource.adaptTo(ReplicationStatus.class);
// if you need to get the status for more than 1 resource at once, this approach is more performant
Map<String,ReplicationStatus> allStatus = replicationStatusProvider.getBatchReplicationStatus(enResource,deResource);
```

**Replication Agents**

AEM as a Cloud Service provides two predefined replication agents that route content from author to a target tier through Sling Content Distribution:

* **publish** — Replicates activated content to the live publish tier. This agent is enabled by default and is used when you publish from the UI, workflows, or the Replication API unless you specify otherwise.
* **preview** — Replicates content to the preview tier so authors can review changes before they go live. This agent is not enabled by default.

You can view and monitor both agents from **Tools** > **Deployment** > **Distribution**:

   ![Distribution agents showing publish and preview](/help/operations/assets/replication-agents.png "Distribution agents")

Selecting an agent card opens its status, logs, and [queue details](#replication-queues).

**Replication with Specific Agents**

When you replicate with the API as shown above, only agents that are enabled by default are used—in AEM as a Cloud Service, that is **publish** only. To replicate exclusively to the preview tier, pass an `AgentFilter` that selects the preview agent:

See the following example:

```
private static final String PREVIEW_AGENT = "preview";

ReplicationStatus beforeStatus = enResource.adaptTo(ReplicationStatus.class); // beforeStatus.isActivated == false

ReplicationOptions options = new ReplicationOptions();
options.setFilter(new AgentFilter() {
  @Override
  public boolean isIncluded (Agent agent) {
    return agent.getId().equals(PREVIEW_AGENT);
  }
});
// will replicate only to preview
replicator.replicate(session,ReplicationActionType.ACTIVATE,"/content/we-retail/en", options);

ReplicationStatus afterStatus = enResource.adaptTo(ReplicationStatus.class); // afterStatus.isActivated == false
ReplicationStatus previewStatus = afterStatus.getStatusForAgent(PREVIEW_AGENT); // previewStatus.isActivated == true
```

If you replicate without an `AgentFilter`, only **publish** is used and the preview tier is not affected.

The overall `ReplicationStatus` of a resource updates only when the replication includes at least one agent that is enabled by default. In the example above, only **preview** was used, so `ReplicationStatus.isActivated` remains `false`. Use `getStatusForAgent()` to check status for a specific agent—for example, `getStatusForAgent("preview")` after a preview-only replication, or `getStatusForAgent("publish")` for the live publish tier.

### Methods of Invalidating Content {#invalidating-content}

You can directly invalidate content by using either Sling Content Invalidation (SCD) from author (the preferred method) or by using the Replication API to invoke the publish Dispatcher flush replication agent. See [Caching](/help/implementing/dispatcher/caching.md) page for further details.

**Replication API Capacity Limits**

Replicate fewer than 100 paths at a time, with 500 being the limit. Above the limit, a `ReplicationException` is thrown. 
If your application logic does not require atomic replication, this limit can be overcome by setting the `ReplicationOptions.setUseAtomicCalls` to false, which accepts any number of paths, but internally creates buckets to stay below this limit.

The size of the content transmitted per replication call must not exceed `10 MB`. This rule includes the nodes and properties, but not any binaries (workflow packages and content packages are considered binaries). 


## Replication Queues {#replication-queues}

Each replication agent displays two replication queues. AEM as a Cloud Service no longer shows a separate queue for each publish pod—the publish tier scales automatically, so per-pod queues added complexity without practical benefit. Queue status is consolidated as follows:

* **persisted** — The change is durably stored on the publish tier. After an item clears this queue, the content is persisted; publish instances reach a consistent state over time.
* **fully published** — The change is live on all publish pods and the Dispatcher cache is cleared for the affected paths. After an item clears this queue, visitors receive the updated content.

### Monitor Replication Queues {#monitor-replication-queues}

1. From the AEM [Global Navigation](/help/sites-cloud/authoring/basic-handling.md#global-navigation), navigate to **Tools** > **Deployment**.

   ![Navigate to Distribution from Tools](/help/operations/assets/replication-agent-navigation.png "Distribution navigation")

1. Select **Distribution**, then open the **publish** or **preview** agent card.

1. On the **Status** tab, verify each queue shows a healthy status. Review **Items Pending** for work waiting to process, and **Last Item Processed** for recent activity.

   ![Replication queues showing persisted and fully published](/help/operations/assets/replication-queues.png "Replication queues")

1. Select **Test Connection** to verify the agent can reach the distribution service.
1. Select the **Logs** tab to view the history of content publications.

   ![Replication logs](/help/operations/assets/publish-logs.png "Logs")

## Troubleshooting {#troubleshooting}

If content cannot be published, the publication is reverted from the AEM Publish Service. Use [Monitor Replication Queues](#monitor-replication-queues) to open the agent **Status** tab and identify the affected queue.

When a queue shows a red status, review its pending items to find what caused the failure. Select the queue to view pending items, then clear individual items or the entire queue if needed.
