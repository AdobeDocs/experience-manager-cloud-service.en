---
title: Notification Center
description: Leverage the Notification Center to conveniently take action on incidents and other important information
---

# Notification Center {#notification-center}

>[!NOTE]
>This feature has not been released.

Once configured, AEM as Cloud Service sends notifications about important information for which a customer should take action. Examples of notifications include a blocked queue, or an expiring set of credentials. The full set of notification types can be viewed in the [table below](#current-notification-types), and will expand over time. Notifications are received via both email and as a new entry under the notification widget (accessed by clicking the bell icon) in the top right corner of many DX user screens. Customers can configure their notification settings.

When a notification is received, it can be clicked, which opens AEM as a Cloud Service's Notification Center with a popup showing additional context so that the expected action is explained.

In addition to showing information about the just-clicked notification, The Notification Center serves as a hub where customers can view and manage the set of current and older notifications. <!-- It can be accessed directly at the url TBD (Alexandru: I'm intentionally keeping it TBD for now so customers don't find it) -->

There are two high level categories of notifications:

1. Incidents - an event has occurred, which typically requires prompt resolution. For example, a blocked queue
1. Proactive - Adobe has a recommendation for an action a customer should take in the near future. For example, usage of a deprecated UI.

See the [table below](#current-notification-types) for the currently supported notifications.

From the Notification Center screen, you can select a specific program and environment, which has the effect of filtering for that scope.

## Configuration {#configuration}

You can follow the steps below to configure the Notification Center:

1. Create the following Product Profiles, as described [in this page](/help/journey-onboarding/user-groups.md), assigning the appropriate Adobe IDs from your organization to those profiles.
1. Determine the notification configuration settings. At [https://experience.adobe.com/preferences/notification-section](https://experience.adobe.com/preferences/notification-section), make sure the Experience Manager Subscription is enabled and the **Others** checkbox is selected. In addition, it is recommended that the Emails section is set to **Instant Notifications** so you receive notifications immediately when an incident occurs.

>[!NOTE]
>Subscriptions function at the organization level so subscribers will receive notifications for all programs and environments within those programs.

## Detailed User Flow {#detailed-user-flow}

Clicking on the email will bring you to the notification center, with a popup showing context for the notification you clicked on and in some cases, links to additional information describing how to take corrective action.

![Incident details](/help/operations/assets/incident-details.png)

Clicking the **Learn More** link navigates the user to this article, where the notification can be referenced in the table below, which provides guidance on what action to take.

When in the notification center, you can see a list of other recent notifications. It is recommended that using the Actions list, you acknowledge a notification in order to signal to Adobe that your organization is aware of the task, and to resolve the notification when corrective action has been taken.

![Notification list](/help/operations/assets/notification-list.png)

In most cases, the notification should provide all the necessary context to resolve the issue. However, if there are questions for Adobe Support, you can click the **Contact Support** link in the notification popup. This will bring up a form from where you can describe the question and submit it to create the Support ticket, which will also include a reference to the specific notification so that an Adobe Support Engineer has the relevant context.

![Contact support 1](/help/operations/assets/contact-support1.png)

![Contact support 2](/help/operations/assets/contact-support2.png)

Like all support tickets, it will appear in the [Adobe Admin Console Support Cases tab](https://helpx.adobe.com/enterprise/using/support-for-enterprise.html), where you can track it and add additional comments.

![Admin Console Support](/help/operations/assets/admin-console-support.png)

## Current Notification Types {#current-notification-types}

The table below lists the currently supported Notification Types

| Notification Type  | Related Product Profile  | Corrective Action |
|---|---|---|
| Blocked replication queue  | Incident  | Unblock queue by following instructions in the [Replication Documentation](/help/operations/replication.md#troubleshooting)  |
| Expiring S2S certificate  | Proactive  | Learn how to refresh a credential in the [Generating Access Tokens for Server Side APIs documentation](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md#refresh-credentials)  |
| SSL certificate expiration  |   |   |
| Deprecated OSGI property  | Incident Notification  |   |
| Deprecated Java API  | Incident Notification  |   |
| Poor cache hit ratio  | Proactive  |   |
| Failed asset rendition processing  | Incident Notification  |   |
| Advanced Networking: VPN bandwidth high  | Incident Notification  |   |
| Advanced Networking: VPN disconnected  | Incident Notification  |   |
| Splunk Forwarding not working properly   | Incident Notification  |   |