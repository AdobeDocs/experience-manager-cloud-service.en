---
title: Notification Center
description: Leverage the Notification Center to conveniently take action on incidents and other important information
hidefromtoc: yes
exl-id: d5a95ac4-aa88-44d5-ba02-7c9702050208
---
# Notification Center {#notification-center}

>[!NOTE]
>This feature has not been released.

Once configured, AEM as Cloud Service sends notifications about important information for which customers should take action. Examples of notifications include a blocked queue, or an expiring set of credentials. The full set of notification types can be viewed in the [table below](#current-notification-types), and will expand over time. Notifications are received via both email and as a new entry under the notification widget, which is accessed by clicking the bell icon in the top right corner throughout the Adobe Experience Cloud. Notification settings can be configured.

When a notification is received, it can be clicked to open AEM as a Cloud Service's Notification Center with a popup displaying additional context explaining the recommended action for a customer to take.

In addition to displaying information about the just-clicked notification, The Notification Center serves as a hub where you can view and manage the set of current and older notifications. <!-- It can be accessed directly at the url TBD (Alexandru: I'm intentionally keeping it TBD for now so customers don't find it) -->

There are two high level categories of notifications:

1. Incidents - an event has occurred, which typically requires prompt resolution. For example, resolving a blocked queue
1. Proactive - Adobe has a recommendation for an action a customer should take in the near future. For example, to stop referencing a deprecated UI.

See the [table below](#current-notification-types) for the currently supported notifications.

From the Notification Center screen, you can select a specific program and environment, which has the effect of filtering for that scope.

## Configuration {#configuration}

You can follow the steps below to configure receiving notifications:

1. Create the following Product Profiles, as described [in this article](/help/journey-onboarding/notification-profiles.md), assigning the appropriate Adobe IDs from your organization to those profiles.
1. Determine the notification configuration settings. [On this page](https://experience.adobe.com/preferences/notification-section), make sure the Experience Manager Subscription is enabled and the **Others** checkbox is selected. In addition, it is recommended that the Emails section is set to **Instant Notifications** so you receive notifications immediately after an incident occurs.

>[!NOTE]
>Subscriptions function at the organization level so subscribers will receive notifications for all programs and environments within those programs.

## Detailed User Flow {#detailed-user-flow}

Clicking on the email will bring you to the Notification Center, with a popup showing context for the notification you clicked on and in some cases, links to additional information describing how to take corrective action.

![Incident details](/help/operations/assets/incident-details.png)

Clicking the **Learn More** link navigates the user to this article, where the notification can be referenced in the table below, which provides guidance on what action to take.

In the Notification Center, you can see a list of other recent notifications. It is recommended that using the Actions list, you acknowledge a notification in order to signal to Adobe that your organization is aware of the task, and to later resolve the notification when corrective action has been taken.

![Notification list](/help/operations/assets/notification-list.png)

In most cases, the notification should provide all the necessary context to resolve the issue. However, if there are questions for Adobe Support, you can click the **Contact Support** link in the notification popup. This will bring up a form from where you can describe the question and submit it to create the Support ticket, which will also include a reference to the specific notification so that an Adobe Support Engineer has the relevant context.

![Contact support 1](/help/operations/assets/contact-support1.png)

![Contact support 2](/help/operations/assets/contact-support2.png)

Like all support tickets, it will appear in the [Adobe Admin Console's Support Cases tab](https://helpx.adobe.com/enterprise/using/support-for-enterprise.html), where you can track it and add additional comments.

![Admin Console Support](/help/operations/assets/admin-console-support.png)

## Current Notification Types {#current-notification-types}

The table below lists the currently supported Notification Types

| Notification Type  | Related Product Profile  | Corrective Action |
|---|---|---|
| Blocked replication queue  | Incident  | Unblock queue by following instructions in the [Replication Documentation](/help/operations/replication.md#troubleshooting)  |
| Expiring S2S certificate  | Proactive  | Learn how to refresh a credential in the [Generating Access Tokens for Server Side APIs documentation](/help/implementing/developing/introduction/generating-access-tokens-for-server-side-apis.md#refresh-credentials)  |
