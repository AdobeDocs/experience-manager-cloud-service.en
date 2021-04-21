---
title: Replication
description: Distribution and Troubleshooting replication.
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

### Managed Publication {#managed-publication}

You can invoke the replication of an entire content tree by using **Managed Publication** if you select **Include Children** and leave **Include only immediate children** disabled. This triggers a workflow that you will be able to view in Workflow instances.

To do this, follow the below steps:

1. In the AEM as a Cloud Service homepage, go to **Sites**
1. Select the node you wish to activate
1. Select **Managed Publication** in the top action menu that appears
   
   ![Managed Publication](/help/operations/assets/managed.png)

1. In the following screen, choose to replicate at a later date by clicking the **Later** radio button and selecting a date
1. Click **Next**
1. Now, tick the box next to the content node you wish to replicate, and select **Include Children**
1. In the following window, untick **Include only immediate children**. Otherwise, tree replication will not be invoked
   
   ![Immediate Children](/help/operations/assets/immediatechildren.png)

1. Click **Add**
1. Finally, set a name for the ensuing Workflow and press **Publish Later**.

### Replication Workflows {#replication-workflows}

Alternatively to the above mentioned method of Managed Publication, you can also trigger a tree replication by creating a Workflow Model that uses the `Treereplication` process step:

1. From the AEM as a Cloud Service homepage, go to **Tools - Workflow - Models**
1. In the Workflow Models page, press **Create** in the upper right corner of the screen
1. Add a title and a name to your model. For more information, see [Creating Workflow Models](https://experienceleague.adobe.com/docs/experience-manager-65/developing/extending-aem/extending-workflows/workflows-models.html)
1. Select the newly created model from the list, and press **Edit**
1. In the following window, drag and drop the Process Step to the current model flow:
   
   ![Process Step](/help/operations/assets/processstep.png)

1. Click the Process step in the flow and select **Configure** by pressing the wrench icon
1. Click on the **Process** tab and select `Treeactivation` from the drop down list
   
   ![Treeactivation](/help/operations/assets/treeactivation.png)

1. Set any additional parameters in the **Arguments** field. Multiple comma separated arguments can be stringed together. For example:
   
   `enableVersion=true,agentId=publish`  

   >[!NOTE]
   >
   >For the list of parameters, see the **Parameters** section below

1. Press **Done** to save the Workflow model.


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
