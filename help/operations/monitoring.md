---
title: Infrastructure and Service Monitoring in AEM as a Cloud Service
description: Infrastructure and Service Monitoring in AEM as a Cloud Service
---

# Infrastructure and Service Monitoring in AEM as a Cloud Service {#monitoring-in-aem-as-a-cloud-service}

Adobe Experience Manager as a Cloud Service provides observability and monitoring of infrastructure, services and user experience utilizing a variety of solutions. The goal of this document is to provide insight into observability and monitoring to our customers' technical staff and business stakeholders. Since there are several layers of monitoring, this page is organized into three sections: [external availability](external-availability) , [internal module monitoring](#module-monitoring) and [customer observability](#customer-observability). The last section covers [monitoring protocols](#monitoring-protocol).

AEM as a Cloud Service uses hundreds of cloud-native monitors to report on the state of each environment 24/7 and 365 days a year. The monitor's definitions are not static, they are continuously reviewed to improve the early detection capability. Additionally, Adobe has on-call procedures set up to respond to alerts.

If you require information about other types of monitoring like logging or monitoring through Cloud Manager please see the [Additional Resources](#resources) section.

## External Availability {#external-availability}

External availability is composed of two parts: Service Edge and Custom Monitoring.

### Service Edge {#service-edge}

All of your AEM as a Cloud Service environments are monitored for availability and alerts are sent to the engineering team in case a problem is detected. However, Service Edge Monitoring is set up only for production environments and the metrics are used to calculate the customer's SLA. It takes environment runtime and the AEM as a Cloud Service CDN into consideration. Service Edge Monitoring employs five distinct locations close to your chosen region and checks periodically for availability. A site's unavailability triggers an alert and will engage our on-call support teams and processes.

### Custom Monitoring {#custom-monitoring}

With Custom monitoring, customers have the option to provide up to five distinct web property URLs prior to going live. These URLs should be valid and return an HTTP 200 response code. These monitors support customers who [bring their own CDN](/help/implementing/dispatcher/cdn.md#point-to-point-CDN) in front of the Adobe CDN  and any external traffic routing employed in front of AEM as a Cloud Service that is not under Adobe’s control.

## Internal Module Monitoring {#module-monitoring}

While external availability is focused on end-user monitoring, internal module monitoring observes whether the architectural sub-systems are operating nominally without feature or performance degradation. In case of a problem, alerts are triggered so repairs can be done either automatically or through the involvement of the operations team, with the goal of preventing compromised availability. The following sub-sections will introduce various categories of monitors with some example checks.

**Pod check**

A pod encapsulates one or more applications.  There are pods for publish, author, preview and more.

Example check:

| Check | Condition |
| --- | --- |
| Pod CPU iowait percentage | Greater than N over two minutes. |
| Pod reports major fault (Memory Check) | Greater than N over two minutes. |
| Container Check | Restarts more than once over a 30 minute period. |

**Deployment check**

A deployment tells the orchestration engine how to create and/or modify instances of a pod that holds a containerized application.

Example check:

| Check | Condition |
| --- | --- |
| Author deployment is not available | X% of the time in the last one hour or five minutes OR X% of the time in the last six hours or 30 minutes. |

**Disk on host and document node store check**

This group of monitors checks for disk usage, read and write operations on disk. AEM repository size is also monitored.

Example check:

| Check | Condition |
| --- | --- |
| Disk Usage | X% or higher for warning or Y% or higher for critical. |
| Author repository Size | X GB or higher. |

**Backup**

Backup operations are checked for execution and successful completion.

**Document store database**

Dozens of monitors are used to watch the MongoDB health and performance. These monitors include checks for database cluster health, CPU, IO, JVM and more.

**Service Check**

Monitors are setup to check the health and performance of services across the infrastructure landscape. Some of these monitors are: Assets compute, dispatcher process replication queue, audit purge, data consistency check, data garbage collection, version purge, index (Async, consistency, job, size and more).

| Check | Condition |
| --- | --- |
| Replication queue blocked | More than five minutes. |
| Version Purge Failed | Two consecutive times. |
| Data Consistency Check | Failed once. |
| Index Size | Document count greater than X. |
| Query | Not using index or traversing. |

Additional checks are added to environments provisioned for Forms. There is also a check for user synchronization services.

## Customer observability {#customer-observability}

Customers can use the [New Relic Application Performance Monitoring](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/user-access-new-relic.html) suite that provides real time performance data collected and charted for analysis and troubleshooting. By using the monitoring suite, customers can directly observe various metrics such as: JVM performance metrics, transaction time for Java, background external calls and database calls.

## Monitoring protocol {#monitoring-protocol}

The engineering team responds to Service Edge Monitoring alerts. The Cloud Subject Matter (CSME) team attend to alerts resulting from Custom Monitoring checks.

## Additional Resources {#resources}

* [New Relic Application Performance Monitoring](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/user-access-new-relic.html)
* [Logging for AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/logging.html)
* [Monitoring Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/content/using/monitoring-environments.html)
