---
title: Tree Replication Workflows in AEM as a Cloud Service
description: Learn how to replicate deep content hierarchies using the Tree Activation workflow step and related workflows in AEM as a Cloud Service.
feature: Operations
role: Admin
---
# Tree Replication Workflows in AEM as a Cloud Service {#tree-replication-workflows}

When you must publish a large branch of the content tree, standard page-by-page publishing can be slow and resource-intensive. AEM as a Cloud Service provides workflow-based approaches that replicate deep content hierarchies in manageable chunks, pause when replication queues are busy, and resume if interrupted.

Use the **Tree Activation Workflow Step** for bulk tree replication. It is the recommended approach for large payloads. The **Publish Content Tree Workflow** remains documented for reference but is deprecated in favor of the Tree Activation step.

For other replication topics, see [Replication](/help/operations/replication.md).

## Tree Activation Workflow Step {#tree-activation}

The Tree Activaton workflow step is intended to performantly replicate a deep hierarchy of content nodes. It automatically pauses when the queue grows too large in order to allow other replications to proceed in parallel with minimal latency. 

Create a Workflow Model that uses the `TreeActivation` process step:

1. From the AEM as a Cloud Service homepage, go to **Tools - Workflow - Models**.
1. In the Workflow Models page, press **Create** in the upper right corner of the screen.
1. Add a title and a name to your model. For more information, see [Creating Workflow Models](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html).
1. Select the created model from the list, and press **Edit**
1. In the following window, delete the Step that appears by default
1. Drag and drop the Process Step to the current model flow:
   
   ![Process Step](/help/operations/assets/processstep.png)

1. Select the Process step in the flow and select **Configure** by pressing the wrench icon.
1. Select the **Process** tab and select `Publish Content Tree` from the drop-down list, then check the **Handler Advance** check box
   
   ![Treeactivation](/help/operations/assets/new-treeactivationstep.png)

1. Set any additional parameters in the **Arguments** field. Multiple comma-separated arguments can be strung together. For example:
   
   `enableVersion=false,agentId=publish,chunkSize=50,maxTreeSize=500000,dryRun=false,filters=onlyModified,maxQueueSize=10`  
   
   >[!NOTE]
   >
   >For the list of parameters, see the **Parameters** section below.

1. Press **Done** to save the Workflow model.

**Parameters**

| Name           | default | description                                                     |
| -------------- | ------- | --------------------------------------------------------------- |
| path           |         | root path to start from                                         |
| agentId        | publish | Agent that receives the replication (`publish` or `preview`)    |
| chunkSize      | 50      | Number of paths to bundle into a single replication             |
| maxTreeSize    | 500000  | Maximum number of nodes for a tree to be considered small       |
| maxQueueSize   | 10      | Maximum number of items in replication queue                    |
| enableVersion  | false   | Enable versioning                                               |
| dryRun         | false   | When set to true replication is not acutally called             |
| userId         |         | only for job. On workflow the user calling the workflow is used |
| filters        |         | List of node filter names. See supported filter below           |

**Support Filters**

| Name          | Description                                 |
| ------------- | ------------------------------------------- |
| onlyModified  | Nodes: both new, and pre-existing that have been modified since the last publish |
| onlyActivated | Nodes: that have been published before the last publish |


**Resume Support**

The workflow processes content in chunks, each of which represents a subset of the full content to be published.  If the workflow is stopped by the system, it will continue where it left off. 

**Monitoring Workflow Progress**

1. From the AEM as a Cloud Service homepage, go to **Tools - General - Jobs**.
1. Look at the row corresponding to your workflow. The *progress* column gives an indication of how the replication is progressing. For example, it may display 41/564 and upon refreshing, it may be updated to 52/564.

   ![Treeactivation progress](/help/operations/assets/treeactivation-progress.png)


1. Selecting the row and opening it will provide additional details about the status of the workflow execution.

   ![Treeactivation status details](/help/operations/assets/treeactivation-progress-details.png)



## Publish Content Tree Workflow {#publish-content-tree-workflow}

>[!NOTE]
>
>This feature is deprecated in favor of the more performant Tree Activation step, which can be included in a custom workflow.  

+++ Click here to learn more about this deprecated feature.

You can trigger a tree replication by choosing **Tools - Workflow - Models** and copying the **Publish Content Tree** out-of-the-box workflow model, as shown below:

![The Publish Content Tree Workflow Card](/help/operations/assets/publishcontenttreeworkflow.png)

Do not invoke the original model. Instead, make sure to first copy the model and invoke that copy.

Like all workflows, it can also be invoked via API. For more information, see [Interacting with Workflows Programmatically](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-program-interaction.html#extending-aem).

Alternatively, you can create a Workflow Model that uses the `Publish Content Tree` process step. 

1. From the AEM as a Cloud Service homepage, go to **Tools - Workflow - Models**.
1. In the Workflow Models page, press **Create** in the upper right corner of the screen.
1. Add a title and a name to your model. For more information, see [Creating Workflow Models](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html).
1. Select the created model from the list, and press **Edit**
1. In the following window, drag and drop the Process Step to the current model flow:
   
   ![Process Step](/help/operations/assets/processstep.png)

1. Select the Process step in the flow and select **Configure** by pressing the wrench icon.
1. Select the **Process** tab and select `Publish Content Tree` from the drop-down list, then check the **Handler Advance** check box
   
   ![Treeactivation](/help/operations/assets/newstep.png)

1. Set any additional parameters in the **Arguments** field. Multiple comma-separated arguments can be strung together. For example:
   
   `enableVersion=true,agentId=publish,includeChildren=true`  

   
   >[!NOTE]
   >
   >For the list of parameters, see the **Parameters** section below.

1. Press **Done** to save the Workflow model.

**Parameters**

* `includeChildren` (boolean value, default: `false`). The value `false` means that only the path is published; `true` means that children are published too.
* `replicateAsParticipant` (boolean value, default: `false`). If configured as `true`, the replication is using the `userid` of the principal which performed the participant step.
* `enableVersion` (boolean value, default: `false`). This parameter determines if a new version is created upon replication.
* `agentId` (string value, default means only agents for publish are used). Specify the target agent explicitly—for example, `publish` for the live publish tier or `preview` for the preview tier.
* `filters` (string value, default means that all paths are activated). Available values are: 
  * `onlyActivated` - only activate pages that have (already) been activated. Acts as a form of reactivation.
  * `onlyModified` - activate only paths which are already activated and have a modification date later than the activation date.
  * The above can be ORed with a pipe "|". For example, `onlyActivated|onlyModified`.  

**Logging**

When the tree activation workflow step starts, it logs its configuration parameters on the INFO loglevel. When paths are activated, an INFO statement is also logged.

A final INFO statement is logged after the workflow step has replicated all paths.

Also, you can increase the loglevel of the loggers below `com.day.cq.wcm.workflow.process.impl` to DEBUG/TRACE to get even more log information.

If there are errors, the workflow step terminates with a `WorkflowException`, which wraps the underlying Exception.

The following are examples of logs that are generated during a sample publish content tree workflow:

```
21.04.2021 19:14:55.566 [cm-p123-e456-aem-author-797aaaf-wkkqt] *INFO* [JobHandler: /var/workflow/instances/server60/2021-04-20/brian-tree-replication-test-2_1:/content/wknd/us/en/adventures] com.day.cq.wcm.workflow.process.impl.treeactivation.TreeActivationWorkflowProcess TreeActivation options: replicateAsParticipant=false(userid=workflow-process-service), agentId=publish, chunkSize=100, filter=, enableVersion=false
```

```
21.04.2021 19:14:58.541 [cm-p123-e456-aem-author-797aaaf-wkkqt] *INFO* [JobHandler: /var/workflow/instances/server60/2021-04-20/brian-tree-replication-test-2_1:/content/wknd/us/en/adventures] com.day.cq.wcm.workflow.process.impl.ChunkedReplicator closing chunkedReplication-VolatileWorkItem_node1_var_workflow_instances_server60_2021-04-20_brian-tree-replication-test-2_1, 17 paths replicated in 2971 ms
```

+++
