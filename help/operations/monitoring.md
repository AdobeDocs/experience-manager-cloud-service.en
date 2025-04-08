---
title: Infrastructure and Service Monitoring in AEM as a Cloud Service
description: Infrastructure and Service Monitoring in AEM as a Cloud Service
exl-id: 82432c11-37ec-48ac-a52b-487abdc859fa
feature: Operations
role: Admin
---
# Infrastructure and Service Monitoring in AEM as a Cloud Service {#monitoring-in-aem-as-a-cloud-service}

Adobe Experience Manager as a Cloud Service provides observability and monitoring of: infrastructure, services, and user experience. Since various solutions are used and there are several layers of monitoring, this page is organized into three sections:

* [External availability](#external-availability)
* [Internal module monitoring](#module-monitoring)
* [Customer observability](#customer-observability)

AEM as a Cloud Service uses hundreds of cloud-native monitors to continually report the state of each environment (24/7) for 365 days a year. The monitor definitions are not static, they are continuously reviewed to improve the early detection capability. Also, Adobe has on-call procedures set up to respond to alerts.

If you require information about other types of monitoring like logging or monitoring through Cloud Manager, see [Additional Resources](#resources).

## External Availability {#external-availability}

External availability is composed of two parts: Service Edge and Custom Monitoring.

### Service Edge {#service-edge}

All your environments of AEM as a Cloud Service are monitored for availability. However, Service Edge Monitoring is set up only for production environments and the metrics are used to calculate the customer's SLA. It takes environment runtime and the AEM as a Cloud Service CDN into consideration. Service Edge Monitoring employs five distinct locations close to your chosen region and checks periodically for availability. A site's unavailability triggers an alert and engages Adobe's on-call support teams and processes.

### Custom Monitoring {#custom-monitoring}

With Custom monitoring, customers can optionally provide up to five distinct web property URLs before [going live](/help/journey-migration/go-live.md). These URLs should be valid and return an HTTP 200 response code. These monitors support customers who [bring their own CDN](/help/implementing/dispatcher/cdn.md#point-to-point-CDN) in front of the Adobe CDN  and any external traffic routing employed in front of AEM as a Cloud Service that is not under Adobe's control. Alerts resulting from Custom Monitoring checks engage Adobe's support teams and processes.

>[!NOTE]
>
> This functionality is only offered for production environments and customers with [Advanced Cloud Support](https://experienceleague.adobe.com/docs/support-resources/data-sheets/overview.html#support-add-ons). If you have any questions, contact your Adobe account team.

## Internal Module Monitoring {#module-monitoring}

While external availability is focused on end-user monitoring, internal module monitoring observes whether the architectural subsystems are operating nominally without feature or performance degradation. If there is a problem, alerts are triggered so repairs can be done either automatically or through the involvement of the operations team, with the goal of preventing compromised availability. There are various categories of monitors, presented below are some example checks:

* The CPU iowait percentage does not exceed a certain threshold.
* Instance redeployments do not exceed a certain frequency.
* Disk usage is below a certain threshold.
* Author repository size is within certain bounds.
* Backup operations are completed successfully.
* Database health and performance are monitored.
* AEM Cloud services are behaving as expected, including no blocked replication queues, consistent data, and performant queries.

Additional checks are added to environments provisioned for Forms. Check definitions are not static and are subject to changes and updates.

## Customer observability {#customer-observability}

Customers can use the [New Relic Application Performance Monitoring](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/user-access-new-relic.html) suite that provides real-time performance data collected and charted for analysis and troubleshooting. By using the monitoring suite, customers can directly observe various metrics such as: JVM performance metrics, transaction time for Java&trade;, background external calls, and database calls.

## Additional Resources {#resources}

* [New Relic Application Performance Monitoring](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/user-access-new-relic.html)
* [Logging for AEM as a Cloud Service](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/implementing/developing/logging.html)
* [Monitoring Environments](https://experienceleague.adobe.com/docs/experience-manager-cloud-manager/content/using/monitoring-environments.html)
