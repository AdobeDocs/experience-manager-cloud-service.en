---
title: Replication
description: Distribution and Troubleshooting replication.
exl-id: c84b4d29-d656-480a-a03a-fbeea16db4cd
---
# Replication {#replication}

Adobe Experience Manager as a Cloud Service  uses the [Sling Content Distribution](https://sling.apache.org/documentation/bundles/content-distribution.html) capability to move the content to replicate to a pipeline service run on Adobe I/O that is outside of the AEM runtime. 

>[!NOTE]
>
>Read [Distribution](/help/core-concepts/architecture.md#content-distribution) for more information.

## Methods of Publishing Content {#methods-of-publishing-content}

### Quick Un/Publish - Planned Un/Publish {#publish-unpublish}

These standard AEM functionalities for the authors do not change with AEM Cloud Service.

### On and Off Times - Trigger Configuration {#on-and-off-times-trigger-configuration}

The additional possibilities of **On Time** and **Off Time** are available from the [Basic tab of Page Properties](/help/sites-cloud/authoring/fundamentals/page-properties.md#basic).

To realize the automatic replication for this you need to enable **Auto Replicate** in the [OSGi configuration](/help/implementing/deploying/configuring-osgi.md) **On Off Trigger Configuration**: 

   ![OSGi On Off Trigger Configuration](/help/operations/assets/replication-on-off-trigger.png)

### Tree Activation {#tree-activation}

To perform a tree activation:

1. From the AEM Start Menu navigate to **Tools > Deployment > Distribution**
2. Select the card **forwardPublisher**
3. Once in the forwardPublisher Web console UI, **select Distribute**
![Distribute](assets/distribute.png "Distribute")
4. Select the path in the path browser, choose to add a node, tree or delete as required and select **Submit**

### Publish Content Tree Workflow {#publish-content-tree-workflow}

You can trigger a tree replication by choosing to **Tools - Workflow - Models** and choosing the **Publish Content Tree** out-of-the-box workflow model, as shown below:

![](/help/operations/assets/publishcontenttreeworkflow.png)

Like all workflows, it can also be invoked via API. For more information, see [Interacting with Workflows Programatically](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-program-interaction.html?lang=en#extending-aem).

Alternatively, you can also achieve this by creating a Workflow Model that uses the `Publish Content Tree` process step:

1. From the AEM as a Cloud Service homepage, go to **Tools - Workflow - Models**
1. In the Workflow Models page, press **Create** in the upper right corner of the screen
1. Add a title and a name to your model. For more information, see [Creating Workflow Models](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html)
1. Select the newly created model from the list, and press **Edit**
1. In the following window, drag and drop the Process Step to the current model flow:
   
   ![Process Step](/help/operations/assets/processstep.png)

1. Click the Process step in the flow and select **Configure** by pressing the wrench icon
1. Click on the **Process** tab and select `Publish Content Tree` from the drop down list
   
   ![Treeactivation](/help/operations/assets/newstep.png)

1. Set any additional parameters in the **Arguments** field. Multiple comma separated arguments can be stringed together. For example:
   
   `enableVersion=true,agentId=publish`  

   
   >[!NOTE]
   >
   >For the list of parameters, see the **Parameters** section below.

1. Press **Done** to save the Workflow model.

**Parameters**

* `replicateAsParticipant` (boolean value, default: `false`). If configured as `true`, the replication is using the `userid` of the principal which performed the participant step.
* `enableVersion` (boolean value, default: `true`). This parameter determines if a new version is created upon replication.
* `agentId` (string value, default means all enabled agents are used).
* `filters` (string value, default means all paths are activated). Available values are:
  * `onlyActivated` - only paths which are not marked as activated will be activated.
  * `onlyModified` - activate only paths which are already activated and have a modification date later than the activation date.
  * The above can be ORed with a pipe "|". For example, `onlyActivated|onlyModified`.  

**Logging**

When the tree activation workflow step starts, it will log its configuration parameters on the INFO loglevel. When paths are activated, an INFO statement is also logged.

A final INFO statement will then be logged after the workflow step has replicated all paths.

Additionally you can increase the loglevel of the loggers below `com.day.cq.wcm.workflow.process.impl` to DEBUG/TRACE to get even more log information.

In case of errors, the workflow step terminates with a `WorkflowException`, which wraps the underlying Exception.

Below you will find examples of logs that are generated during a sample publish content tree workflow:

```
21.04.2021 19:14:55.566 [cm-p123-e456-aem-author-797aaaf-wkkqt] *INFO* [JobHandler: /var/workflow/instances/server60/2021-04-20/brian-tree-replication-test-2_1:/content/wknd/us/en/adventures] com.day.cq.wcm.workflow.process.impl.treeactivation.TreeActivationWorkflowProcess TreeActivation options: replicateAsParticipant=false(userid=workflow-process-service), agentId=publish, chunkSize=100, filter=, enableVersion=false
```
```
21.04.2021 19:14:58.541 [cm-p123-e456-aem-author-797aaaf-wkkqt] *INFO* [JobHandler: /var/workflow/instances/server60/2021-04-20/brian-tree-replication-test-2_1:/content/wknd/us/en/adventures] com.day.cq.wcm.workflow.process.impl.ChunkedReplicator closing chunkedReplication-VolatileWorkItem_node1_var_workflow_instances_server60_2021-04-20_brian-tree-replication-test-2_1, 17 paths replicated in 2971 ms
```

**Resume Support**

The workflow processes content in chunks, each of which represents a subset of the full content to be published. If for any reason the workflow is stopped by the system, it will restart and process the chunk that was not yet processed. A log statement will state that content has been resumed from a specific path.

## Troubleshooting {#troubleshooting}

To troubleshoot replication, navigate to the Replication Queues in the AEM Author Service Web UI:

1. From the AEM Start Menu navigate to **Tools > Deployment > Distribution**
2. Select the card **forwardPublisher**
![Status](assets/status.png "Status")
3. Check the queue status which should be green
4. You can test the connection to the replication service
5. Select the **Logs** tab which shows the history of content publications

![Logs](assets/logs.png "Logs")

If the content couldn't be published, the whole publication is reverted from the AEM Publish Service.
In that case, the queues should be reviewed in order to identify which items caused the cancelation of the publication. By clicking on a queue showing a red status, the queue with pending items would show up, from which single or all items can be cleared if needed.
