---
title: Manually Configuring the Integration with Adobe Target
description: Learn how to manually configure the integration with Adobe Target.
---

# Manually Integrating with Adobe Target {#manually-integrating-with-adobe-target}

In addition to using [Launch by Adobe to integrate AEM with Adobe Target](/help/sites-cloud/integrating/adobe-target.md) you can also manually integrate with Adobe Target.

>[!NOTE]
>
>The Target Library file, [AT.JS](https://experienceleague.adobe.com/docs/target/using/implement-target/client-side/implement-target-for-client-side-web.html), is a new implementation library for Adobe Target that is designed for both typical web implementations and single-page applications. 
>
>mbox.js has been deprecated and will be removed at a later stage.
>
>Adobe recommends that you use AT.js instead of mbox.js as the client library.
>
>AT.js offers several improvements over the mbox.js library:
>
>* Improved page load times for web implementations
>* Improved security
>* Better implementation options for single-page applications
>* AT.js contains the components that were included in target.js, so there is no longer a call to target.js
>
>You can select AT.js or mbox.js in the **Client library** drop-down menu.

## Creating a Target Cloud Configuration {#creating-a-target-cloud-configuration}

To enable AEM to interact with Adobe Target, create a Target cloud configuration. To create the configuration, you provide the Adobe Target client code and user credentials.

You create the Target cloud configuration only once because you can associate the configuration with multiple AEM campaigns. If you have several Adobe Target client codes, create one configuration for each client code.

You can configure the cloud configuration to synchronize segments from Adobe Target. If you enable synchronization, segments are imported from Target in the background as soon as the cloud configuration is saved.

Use the following procedure to create a Target cloud configuration in AEM:

1. Navigate to **Legacy Cloud Services** via the **AEM logo** &gt; **Tools** &gt; **Cloud Services** &gt; **Legacy Cloud Services**. 
   For example: ([http://localhost:4502/libs/cq/core/content/tools/cloudservices.html](http://localhost:4502/libs/cq/core/content/tools/cloudservices.html))

   The **Adobe Experience Cloud** overview page opens.

1. In the **Adobe Target** section, click **Configure Now**.
1. In the **Create Configuration** dialog:

    1. Give the configuration a **Title**.
    1. Select the **Adobe Target Configuration** template.
    1. Click **Create**.

You can now select the new configuration dor editing.

1, The edit dialog opens.

   ![config-target-settings-dialog](assets/config-target-settings-dialog.png)

<!-- Can this still occur?
   >[!NOTE]
   >
   >When configuring A4T with AEM, you may see a Configuration reference missing entry. To be able to select the analytics framework, do the following:
   >
   >1. Navigate to **Tools** &gt; **General** &gt; **CRXDE Lite**.
   >1. Navigate to **/libs/cq/analytics/components/testandtargetpage/dialog/items/tabs/items/tab1_general/items/a4tAnalyticsConfig**
   >1. Set the property **disable** to **false**.
   >1. Tap or click **Save All**.
-->

1. In the **Adobe Target Settings** dialog, provide values for these properties.

   * **Authentication**: this defaults to IMS (User Credentials is deprecated)

   * **Client Code**: the Target account Client Code

   * **Tenant ID**: the tenant ID

   * **IMS Configuration**: select the required configuration from the drop down list

   * **API Type**: defaults to REST (XML is deprecated)

   * **A4T Analytics Cloud Configuration**: Select the Analytics cloud configuration that is used for target activity goals and metrics. You need this if you are using Adobe Analytics as the reporting source when targeting content. If you do not see your cloud configuration, see note in [Configuring A4T Analytics Cloud Configuration](#configuring-a-t-analytics-cloud-configuration).

   * **Use accurate targeting:** By default this check box is selected. If selected, the cloud service configuration will wait for the context to load before loading content. See note that follows.

   * **Synchronize Segments from Adobe Target:** Select this option to download segments that are defined in Target to use them in AEM. You must select this option when the API Type property is REST, because inline segments are not supported and you always need to use segments from Target. (Note that the AEM term of 'segment' is equivalent to the Target 'audience'.)

   * **Client library:** this defaults to AT.js (mbox.js is deprecated)

   * **Use Tag Management System to deliver client library** - Select this option to use the client library from Adobe Launch or another tag management system (or DTM, which is deprecated).

   * **Custom AT.js**: Browse to upload your custom AT.js. Leave blank to use the default library.

   >[!NOTE]
   >
   >By default when you opt into the Adobe Target configuration wizard, Accurate Targeting is enabled.
   >
   >Accurate targeting means that the cloud service configuration waits for the context to load before loading content. As a result, in terms of performance, accurate targeting may create a few millisecond delay before loading content.
   >
   >Accurate targeting is always enabled on the author instance. However, on the publish instance you can opt to turn accurate targeting off globally by clearing the check mark next to Accurate Targeting in the cloud service configuration (**http://localhost:4502/etc/cloudservices.html**). You can also still turn accurate targeting on and off for individual components regardless of your setting in the cloud service configuration.
   >
   >If you have ***already*** created targeted components and you change this setting, your changes do not affect those components. You must make any changes to those component directly.

1. Click **Connect to Adobe Target** to initialize the connection with Target. If the connection is successful, the message **Connection successful** is displayed. Click **OK** on the message and then **OK** on the dialog.

   If you cannot connect to Target, see the [troubleshooting](/help/sites-administering/target-configuring.md#troubleshooting-target-connection-problems) section.

<!-- Is this section needed? -->

## Adding a Target Framework {#adding-a-target-framework}

After you configure the Target cloud configuration, add a Target framework. The framework identifies the default parameters that are sent to Adobe Target from the available [Client Context](/help/sites-administering/client-context.md) or [ContextHub](/help/sites-developing/ch-configuring.md) components. Target uses the parameters to determine the segments that apply to the current context.

You can create multiple frameworks for a single Target configuration. Multiple frameworks are useful when you need to send a different set of parameters to Target for different sections of your website. Create a framework for each set of parameters that you need to send. Associate each section of your website with the appropriate framework. Note that a web page can use only one framework at a time.

1. On your Target configuration page, click the **+** (plus sign) next to Available Configurations.

1. In the Create Framework dialog, specify a **Title**, select the **Adobe Target Framework**, and click **Create**.

   ![config-target-framework-dialog](assets/config-target-framework-dialog.png)

   The framework page opens. Sidekick provides components that represent information from the [Client Context](/help/sites-administering/client-context.md) or [ContextHub](/help/sites-developing/ch-configuring.md) that you can map.

   <!-- ![chlimage_1-162](assets/chlimage_1-162.png) -->

1. Drag the Client Context component that represents the data that you want to use for mapping to the drop target. Alternatively, drag the **ContextHub Store** component to the framework.

   >[!NOTE]
   >
   >When mapping, parameters are passed to an mbox via simple strings. You cannot map arrays from ContextHub.

   For example, to use **Profile Data** about your site vistors to control your Target campaign, drag the **Profile Data** component to the page. The profile data variables that are available for mapping to Target parameters appear.

   <!-- ![chlimage_1-163](assets/chlimage_1-163.png) -->

1. Select the variables that you want to make visible to the Adobe Target system by selecting the **Share** checkbox in the appropriate columns.

   <!-- ![chlimage_1-164](assets/chlimage_1-164.png) -->

   >[!NOTE]
   >
   >Synchronizing parameters is one way only - from AEM to Adobe Target.

Your framework is created. To replicate the framework to the publish instance, use the **Activate Framework** option from the sidekick.

## Associating Activities With the Target Cloud Configuration  {#associating-activities-with-the-target-cloud-configuration}

Associate your [AEM activities](/help/sites-authoring/activitylib.md) with your Target cloud configuration so that you can mirror the activities in [Adobe Target](https://docs.adobe.com/content/help/en/target/using/experiences/offers/manage-content.html).

>[!NOTE]
>
>What types of activities are available is determined by the following:
>
>
>* If the **xt_only** option is enabled on the Adobe Target tenant (clientcode) used on the AEM side to connect to Adobe Target, then you can create **only** XT activities in AEM.
>
>* If the **xt_only** options is **not** enabled on the Adobe Target tenant (clientcode), then you can create **both** XT and A/B activities in AEM.
>
>**Additional note:** **xt_only** options is a setting applied on a certain Target tenant (clientcode) and can only be modified directly in Adobe Target. You cannot enable or disable this option in AEM.

## Associating the Target Framework With Your Site {#associating-the-target-framework-with-your-site}

After you create a Target framework in AEM, associate your web pages with the framework. The targeted components on the pages send the framework-defined data to Adobe Target for tracking. (See [Content Targeting](/help/sites-authoring/content-targeting-touch.md).)

When you associate a page with the framework, the child pages inherit the association.

1. In the **Sites** console, navigate to the site that you want to configure.
1. Using either [quick actions](/help/sites-authoring/basic-handling.md#quick-actions) or [selection mode](/help/sites-authoring/basic-handling.md), select **View Properties.**
1. Select the **Cloud Services** tab.
1. Tap/click **Edit**.
1. Tap/click **Add Configuration** under **Cloud Service Configurations** and select **Adobe Target**.

   <!-- ![chlimage_1-165](assets/chlimage_1-165.png) -->

1. Select the framework you want under **Configuration Reference**.

   >[!NOTE]
   >
   >Make sure that you select the specific **framework** that you created and not the Target cloud configuration under which it was created.

1. Tap/click **Done**.
1. Activate the root page of the website to replicate it to the publish server. (See [How To Publish Pages](/help/sites-authoring/publishing-pages.md).)

   >[!NOTE]
   >
   >If the framework you attached to the page was not activated yet, a wizard opens which allows you to publish it as well.

## Troubleshooting Target Connection Problems {#troubleshooting-target-connection-problems}

Perform the following tasks to troubleshoot problems that occur when connecting to Target:

* Make sure that the user credentials that you provide are correct.
* Make sure that the AEM instance can connect to the Target server. For example, make sure that firewall rules are not blocking outbound AEM connections, or that AEM is configured to use necessary proxies.
* Look for helpful messages in the AEM error log. The error.log file is located in the **crx-quickstart/logs** directory where AEM is installed.
* When editing the activity in Adobe Target, the URL is pointing to localhost. Work around this by setting the AEM externalizer to the correct URL.
