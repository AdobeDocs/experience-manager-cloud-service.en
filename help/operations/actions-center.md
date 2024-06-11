---
title: Actions Center
description: Leverage the Actions Center to conveniently act on incidents and other important information
exl-id: d5a95ac4-aa88-44d5-ba02-7c9702050208
---
# Actions Center {#actions-center}

AEM as Cloud Service sends Actions Center email notifications when critical incidents occur that require immediate action, and proactive recommendations for optimizations. Examples include a blocked queue, or an expiring set of credentials; the full set of Actions Center notification types can be viewed in the [table below](#supported-notification-types), which will expand over time.

When an Actions Center email notification is received, it can be clicked to open AEM as a Cloud Service's Actions Center with a pop-up displaying additional context explaining the action for a customer to take.

In addition to displaying information about the just-clicked email notification, the Actions Center serves as a hub where you can view and manage the set of current and older notifications. <!-- It can be accessed directly at the url TBD (Alexandru: I'm intentionally keeping it TBD for now so customers do not find it) -->

There are two high level categories of notifications that appear in the Actions Center:

1. Operational incidents - an event has occurred, which typically requires prompt resolution. For example, resolving a blocked queue.
1. Proactive recommendations - Adobe has a recommendation for an action a customer should take in the near future. For example, to stop referencing a deprecated UI.

See the [table below](#supported-notification-types) for the notifications currently supported in Actions Center.

From the Actions Center, you can select a specific program and environment, which has the effect of filtering for that scope.

## Configuration {#configuration}

To configure receiving Actions Center email notifications, create the Product Profiles described [in this article](/help/journey-onboarding/notification-profiles.md), namely Incident Notification - Cloud Service and Proactive Notification - Cloud Service. Also assign the appropriate Adobe IDs from your organization to those profiles. This allows an administrator to determine which users qualify to receive these email notifications.

>[!NOTE]
>Actions Center email notifications function at the organization level so subscribers will receive notifications for all programs and environments within those programs.

## Detailed User Flow {#detailed-user-flow}

Clicking on the email will bring you to the Actions Center, with a pop-up showing context for the notification you clicked on and in some cases, links to additional information describing how to take corrective action. You can also access Actions Center directly at [https://experience.adobe.com/aem/actions-center](https://experience.adobe.com/aem/actions-center/), where you can select the relevant program and environment.

![Incident details](/help/operations/assets/incident-details.png)

Clicking the **Learn More** link navigates the user to this article, where the notification type can be referenced in the [supported notification types table](#supported-notification-types) below, which provides guidance on what action to take.

In the Actions Center, you can see a list of other recent notifications. It is recommended that using the Actions list, you acknowledge a notification to signal to Adobe that your organization is aware of the task, and to later resolve the notification when corrective action has been taken.

![Notification list](/help/operations/assets/notification-list.png)

In most cases, the pop-up should provide all the necessary context to resolve the issue. However, if there are questions for Adobe Support, you can click the **Contact Support** link in the pop-up. This will bring up a form from where you can describe the question and submit it to create a Support ticket, which will also include a reference to the specific notification so an Adobe Support Engineer has the relevant context.

![Contact support 1](/help/operations/assets/contact-support1.png)

![Contact support 2](/help/operations/assets/contact-support2.png)

Like all support tickets, it will appear in the [Adobe Admin Console's Support Cases tab](https://helpx.adobe.com/enterprise/using/support-for-enterprise.html), where you can track it and add additional comments.

![Admin Console Support](/help/operations/assets/admin-console-support.png)

## Which Notifications Appear? {#which-notification}

AEM as a Cloud Service has several types of notifications, but only a subset appears in the Actions Center, as illustrated in the table below.

| Notification Type               | Description                                   | How to configure                                                                                                                                                                                                                                        | Appears in Actions Center | 
|---------------------------------|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Operational incidents           | Critical incidents requiring immediate action | User assigned to "Incident Notification - Cloud Service" product profile                                                                                                                                                                                | X                         |
| Proactive recommendations       | Optimizations that should be planned          | User assigned to "Proactive Notification - Cloud Service" product profile                                                                                                                                                                               | X                         |
| Cloud Manager pipeline statuses | Information about the state of your pipelines | User with Business Owner, Program Manager, or Deployment Manager roles, "Others" checkbox selected in [Experience Cloud Preferences](https://experience.adobe.com/preferences), as [described here](/help/implementing/cloud-manager/notifications.md). |                           |

## Supported Notification Types {#supported-notification-types}

The following table lists the notification types currently supported in Actions Center. Notifications are currently limited to production environments.

| Notification Type               | Related Product Profile | Corrective Action                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blocked replication queue       | Incident                | Unblock queue by following instructions in the [Replication Documentation](/help/operations/replication.md#troubleshooting)                                                                                                                                                                                                                                                                                     |
| Invalid persisted GraphQL query | Incident                | Fix the invalid GraphQL query by referencing the [Persisted GraphQL queries troubleshooting documentation](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/headless/graphql-api/persisted-queries-troubleshoot.html)                                                                                                                                                           |
| Traffic spike at origin         | Incident                | Protect your origin by configuring rate limit traffic filter rules that trigger at lower thresholds than the default traffic spike at origin alert.  See the [Blocking DoS and DDoS attacks using traffic rules](/help/security/traffic-filter-rules-including-waf.md#blocking-dos-and-ddos-attacks-using-traffic-filter-rules) section of the Traffic Filter Rules documentation, which references a tutorial. |
|Pages contain a large number of nodes        | Incident               | Reduce total number of nodes within a page. Refer to [Page Complexity documentation](https://experienceleague.adobe.com/en/docs/experience-manager-pattern-detection/table-of-contents/pcx)               | |
|Large number of running workflow instances           | Incident             | Terminate running workflows that are no longer needed. Learn how to [configure a purge job](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/maintenance)              |               |
| Expiring S2S certificate        | Proactive               | Learn how to refresh a credential in the [Generating Access Tokens for Server Side APIs documentation](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md#refresh-credentials)                                                                                                                                                                                         | High Connection Count           | Proactive               | Learn about connection pooling in [Connection Pooling alongside Advanced Networking documentation](/help/security/configuring-advanced-networking.md#connection-pooling-advanced-networking)                                                |
| Deprecated Service User Mapping | Proactive               | Learn how to use the newer Sling Service User Mapping format, as indicated in [Best Practices for Sling Service User Mapping and Service User Definition](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/best-practices-for-sling-service-user-mapping-and-service-user-definition)                                                                               |
| High Connection Count           | Proactive               | Learn about connection pooling in the [Advanced Networking documentation](/help/security/configuring-advanced-networking.md#connection-pooling-advanced-networking)                                                                                                                                                                                                                                             |  |
|Users added directly to custom group           | Proactive           | Relevant IMS Groups need to be added as members of AEM groups. Align with [IMS best practices]( https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/ims-support)                                                                                                                                                                                                  | |
|Missing JCR content            | Proactive           | Add missing JCR Content node. Refer to [Assets Content Validator documentation](https://experienceleague.adobe.com/en/docs/experience-manager-pattern-detection/table-of-contents/acv)                                                                                                                                                                                                 | |
|Completed workflows not purged            | Proactive           | Minimize number of workflow instances and improve performance by purging workflow instances that are more than 90 days old. Learn how to [configure maintenance tasks](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/operations/maintenance)                                                                                                                                                                                                 |
