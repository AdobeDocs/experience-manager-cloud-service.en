---
title: Monitoring in AEM as a Cloud Service
description: Monitoring in AEM as a Cloud Service
---

# Monitoring in AEM as a Cloud Service {#monitoring-in-aem-as-a-cloud-service}

The Adobe Experience Manager (AEM) as a Cloud Service (CS) provides observability and monitoring of infrastructure, services and user experience utilizing a variety of solutions. The goal of this whitepaper is to provide insight into observability and monitoring to our customer’s technical staff and business stakeholders. There are various layers of monitoring. This paper is organized into 3 sections: external availability , internal module monitoring and customer observability. The last section of this paper covers monitoring protocols.

## External Availability {#external-availability}

External availability has two distinct parts: Service Edge and Custom Monitoring. All of your AEM CS environments are monitored for availability and alerts are sent to our engineering team. However, Service Edge Monitoring is only setup for production environment and the metrics are used to calculate customers' SLA. It takes environment runtime and AEM CS CDN into consideration. Service Edge Monitoring employs 5 distinct locations close to your chosen region and checks periodically for availability. A site unavailability triggers an alert and will engage our on-call support teams and processes.  With Custom Monitoring, customers have the option to provide up to 5 distinct web property URLs of their choice prior to go live. The URLs should be valid and return an HTTP 200 response code. These monitors support customers who bring their own CDN in front of the Adobe CDN  and any external traffic routing employed in front of AEM CS that are not under Adobe’s control.

## Internal Module Monitoring {#module-monitoring}

While external availability is focused on end-user monitoring, internal module monitoring observes whether the architectural sub-systems are operating nominally without feature or performance degradation. Alerts are triggered so healing can be done in an automated way or through involvement of the operation team if necessary, with the goal of preventing compromised availability. The following sub-sections will introduce the various categories of monitors with some representative example checks.

**Deployment check**

A deployment tells the orchestration engine how to create and/or  modify instances of a pod  that holds a containerized application.

| Check | Condition |
| --- | --- |
| Author deployment is not available. | X% of the time in the last one hour or five minutes OR X% of the time in the last six hours or 30 minutes. |

**Pod check**

A pod encapsulates one or more applications.  There are pods for publish, author, preview and more.

| Check | Condition |
| --- | --- |
| Pod CPU iowait percentage | Greater than N over two minutes. |
| Pod reports major fault (Memory Check) | Greater than N over two minutes. |
| Container Check | Restarts more than once over a 30 minute period. |

**Disk on host and document node store check**

This group of monitors checks for disk usage, read and write operations on disk. AEM repository size is also monitored under this group.

| Check | Condition |
| --- | --- |
| Disk Usage | X% or higher for warning or Y% or higher for critical. |
| Author repository Size | X GB or higher. |

**Backup**

Backup operations are checked for execution and successful completion.

**Document store database**

Dozens of monitors are used to watch the MongoDB health and performance. The monitors include checks for database cluster health, CPU, IO, JVM and more.

**Service Check**

Monitors are setup to check the health and performance of services across the infrastructure landscape. Some of these monitors are: Assets compute, dispatcher process replication queue, audit purge, data consistency check, data garbage collection, version purge, index (Async, consistency, job, size etc.).

| Check | Condition |
| --- | --- |
| Replication queue blocked | More than five minutes. |
| Version Purge Failed | Two consecutive times. |
| Data Consistency Check | Failed once. |
| Index Size | Document count greater than X. |
| Query | Not using index or traversing. |

Additional checks are added to environments provisioned for Forms. There is also a check for user synchronization services.

## Customer observability {#customer-observability}

Customers have access to New Relic Application Performance Monitoring (APM) that provides real time trending performance data collected and charted for analysis and troubleshooting. Some of the data this tool provides is JVM performance metrics, transaction time for Java, background external calls and database calls. Instructions to get access is located [here](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/user-access-new-relic.html).

## Monitoring protocol {#monitoring-protocol}

The engineering team responds to Service Edge Monitoring alerts. The Cloud Subject Matter (CSME) team attend to alerts resulting from Custom Monitoring checks.

## Conclusion {#page-conclusion}

AEM CS uses hundreds of cloud-native monitors to report on the state of each environment 24x7x365. The monitors' definitions are not static. They are continuously reviewed to improve their early detection capability. The Application Performance Monitor (APM) allows AEM CS Customers to directly observe various metrics. AEM
CS have on-call procedure setup to respond to alerts.
