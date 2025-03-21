---
title: Manage notifications
description: Monitor the operations performed on the assets or folders available in the repository using the Assets view notifications.
exl-id: 1fe6a845-37d5-43c2-bb96-c5b149c238ab
feature: Assets Essentials
role: User, Leader
---
# Watch assets, folders, and collections {#watch-assets-folders}

<table>
    <tr>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/dm-prime-ultimate.md"><b>Dynamic Media Prime and Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/assets-ultimate-overview.md"><b>AEM Assets Ultimate</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/integrate-aem-assets-edge-delivery-services.md"><b>AEM Assets integration with Edge Delivery Services</b></a>
        </td>
        <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/aem-assets-view-ui-extensibility.md"><b>UI Extensibility</b></a>
        </td>
          <td>
            <sup style= "background-color:#008000; color:#FFFFFF; font-weight:bold"><i>New</i></sup> <a href="/help/assets/dynamic-media/enable-dynamic-media-prime-and-ultimate.md"><b>Enable Dynamic Media Prime and Ultimate</b></a>
        </td>
    </tr>
    <tr>
        <td>
            <a href="/help/assets/search-best-practices.md"><b>Search Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/metadata-best-practices.md"><b>Metadata Best Practices</b></a>
        </td>
        <td>
            <a href="/help/assets/product-overview.md"><b>Content Hub</b></a>
        </td>
        <td>
            <a href="/help/assets/dynamic-media-open-apis-overview.md"><b>Dynamic Media with OpenAPI capabilities</b></a>
        </td>
        <td>
            <a href="https://developer.adobe.com/experience-cloud/experience-manager-apis/"><b>AEM Assets developer documentation</b></a>
        </td>
    </tr>
</table>

Assets view notifications enable you to monitor the operations performed on the assets, folders, or collections available in the repository. You need to select and subscribe to the content for which the notifications are sent to you. You can also configure the categories for which the notifications are sent to you.

## Subscribe to notification categories {#subscribe-to-notification-categories}

You can choose and subscribe from a list of categories to receive notifications. Assets view sends the notifications to you only for the categories that you select from the available options:

<table>
    <tbody>
     <tr>
      <th><strong>Notification category</strong></th>
      <th><strong>Description</strong></th>
     </tr>
     <tr>
      <td>Requests</td>
      <td>When you assign a task to a user, you receive notifications when there are actions performed on that task by that user.</td>
     </tr>
     <tr>
      <td>Assigned to me</td>
      <td>You receive a notification when there is a task assigned to you from another user.</td>
     </tr>
     <tr>
      <td>Comment on subscribed content</td>
      <td>You receive a notification when a user comments on your subscribed asset.</td>
     </tr>
     <tr>
      <td>Deletion of subscribed content</td>
      <td>You receive a notification when a user deletes your subscribed asset, folder, or collection.</td>
     </tr>
     <tr>
      <td>External Share of subscribed content</td>
      <td>You receive a notification when a user generates a public link for your subscribed asset, folder, or collection.</td>
     </tr>
     <tr>
      <td>Modification of subscribed content</td>
      <td>You receive a notification when a user creates a new version for your subscribed asset.</td>
     </tr>
     <tr>
      <td>Move/Rename of subscribed content</td>
      <td>You receive a notification when a user moves or renames your subscribed asset or folder.</td>
     </tr>
     <tr>
      <td>Updates on subscribed folders and collections</td>
      <td>You receive a notification when a user adds or removes an asset from a subscribed folder or collection.</td>
     </tr>    
    </tbody>
   </table>

To subscribe to the notification categories:

1. Click ![bell icon](assets/bell-icon.svg) at the right end of the menu bar on the Assets view user interface.

1. Click ![settings icon](assets/settings-icon.svg) to view the [!UICONTROL Experience Cloud preferences] page.

1. Click the **[!UICONTROL Notifications]** option available in the left pane.

1. In the **[!UICONTROL Notifications]** section, navigate to the [!UICONTROL Assets view] section and ensure that the toggle option is switched to the ON state.

   ![Notifications in Assets view](assets/enable-notifications.png)

1. Click **[!UICONTROL Customize]** to view the notification categories.
   ![Notifications in Assets view](assets/enable-notification-categories.png)

1. Select the notification categories for which you need to be notified.

## Watch and unwatch folders, assets, or collections {#watch-unwatch-assets}

After [subscribing to the notification categories](#subscribe-to-notification-categories), you must subscribe to the content to start receiving notifications.

>[!NOTE]
>
>* For **[!UICONTROL Requests]** and **[!UICONTROL Assigned to me]** notification categories, you do not need to subscribe to the content after subscribing to the notification categories. Notifications are automatically sent to you for requests created by you and when a task is assigned to you.
>* Assets view sends notifications only when other users perform actions on the subscribed content. You do not receive notifications for the actions that you perform on the subscribed content.

To subscribe to the content, select the folder, asset, or collection that you need to subscribe to and click **[!UICONTROL Watch]**.

Assets view displays a success message. You can click **[!UICONTROL Go to notification preferences]** available on the success message to edit your [subscription to notification categories](#subscribe-to-notification-categories).

![Notifications in Assets view](assets/watch-assets.png)

Assets view now sends notifications for the subscribed categories. You can also select multiple assets, folders, or collections and click **[!UICONTROL Watch]** to save time. However, if you select multiple entities out of which some of them have already been subscribed, then the **[!UICONTROL Watch]** option does not display.

Similarly, to unsubscribe, select the asset, folder, or collection that you have subscribed for and click **[!UICONTROL Unwatch]**.

## View notifications {#view-notifications}

The notifications appear at the right end of the menu bar on the Assets view user interface.

![Notifications in Assets view](assets/notifications-assets-essentials.png)

When you click a notification, Assets view navigates you to the appropriate asset or folder that is referred to in the notification.
