---
title: Notification Center
description: Leverage the Notification Center to conveniently take action on incidents and other important information
---

# Notification Center {#notification-center}

>[!NOTE]
>This feature has not been released.

Once configured, AEM as Cloud Service sends notifications about important information for which a customer should take action. Examples of notifications include a blocked queue, or an expiring set of credentials. The full set of notification types can be viewed in the table below <!-- (link) -->, and will expand over time. Notifications are received via both email and as a new entry under the notification widget (accessed by clicking the bell icon) in the top right corner of many DX user screens. Customers can configure their notification settings.

When a notification is received, it can be clicked, which navigates the user AEM as a Cloud Service's Notification Center, with a popup showing additional context so the user can understand what action is expected. 

In addition to showing information about the just-clicked notification, The Notification Center serves as a hub where customers can view and manage the set of current and older notifications. <!-- It can be accessed directly at the url TBD (Alexandru: I'm intentionally keeping it TBD for now so customers don't find it) -->

There are two high level categories of notifications:

1. Incidents - an event has occurred, which typically requires prompt resolution. For example, a blocked queue
1. Proactive - Adobe has a recommendation for an action a customer should take in the near future. For example, usage of a deprecated UI

See the table below for the currently supported notifications. <!-- Alexandru: will probably have to hide this until there's a table>

From the Notification Center screen, users can select a specific program and environment, which has the effect of filtering for that scope.

## Configuration {#configuration}

Follow the below steps to configure the Notification Center: <!-- Alexandru: revisit this phrasing -->

1. Create the following Product Profiles, as described [in this page](/help/journey-onboarding/user-groups.md), assigning the appropriate Adobe IDs from your organization to those profiles.
1. Determine the notification configuration settings. At [https://experience.adobe.com/preferences/notification-section](https://experience.adobe.com/preferences/notification-section), make sure the Experience Manager Subscription is enabled and the **Others** checkbox selected. Also, it is recommended that the Emails section is set to **Instant Notifications** so you receive notifications immediately when an incident occurs. <!-- ALexandru: revisit this phrasing too -->

>[!NOTE]
>Subscriptions are at the organization level so subscribers will receive notifications for all programs and environments within those programs.