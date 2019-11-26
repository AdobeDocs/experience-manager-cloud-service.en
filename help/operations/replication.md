---
title: Replication
seo-title: Replication
description: Distribution and Troubleshooting replication.
seo-description: Distribution and Troubleshooting replication. 
---

# Replication {#replication}

Adobe Experience Manager as a Cloud Service  uses the [Sling Content Distribution](https://sling.apache.org/documentation/bundles/content-distribution.html) capability to move the content to replicate to a pipeline service run on Adobe I/O that is outside of the AEM runtime. 

>[!NOTE]
>
> Read [Distribution](/help/core-concepts/architecture.md#content-distribution) for more information.

## Methods of Publishing Content {#methods-of-publishing-content}

### Quick Un/Publish - Planned Un/Publish {#publish-unpublish}

These standard AEM functionalities for the authors do not change with AEM Cloud Service.

### Tree Activation {#tree-activation}

To perform a tree activation:

1. From the AEM Start Menu navigate to **Tools > Deployment > Distribution**
2. Select the card **forwardPublisher**
3. Once in the forwardPublisher Web console UI, **select Distribute**
![Distribute](assets/distribute.png "Distribute")
4. Select the path in the path browser, choose to add a node, tree or delete as required and select **Submit**

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
