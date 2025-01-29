---
title: Navigating to Screens Services Provider
description: This page describes how to navigate to Screens Services Provider.
exl-id: 9eff6fe8-41d4-4cf3-b412-847850c4e09c
feature: Administering Screens
role: Admin, Developer, User
---
# Navigating to Screens Services Provider {#setup-screens-services-provider}

## Introduction {#introduction}

**Screens Services Provider**, allows the content author, developers, and administrators to manage displays and players for content playback once the content is added to the channels. Once the users are given access to AEM Cloud Service, they should be able to log into Screens Services Provider.

This section describes how to set up Screens Services Provider.


## Objective {#objective}

The following section how to configure and set up Screens Services Provider.

## Steps to Set up Screens Services Provider {#screens-services-provider}

Follow the steps below to set up Screens Services Provider:

1. Navigate to the [Screens Services Provider](https://experience.adobe.com/screens).

   >[!CAUTION]
   >If you have access to multiple organizations, ensure that you have logged into correct Organization. To change your organization, click the Org name from the top right-hand corner of the screen and choose the required organization to which you need access.

1. Click the gear icon next to Project (upper-left corner)
   
   ![image](/help/screens-cloud/assets/configure/configure-screens0.png)

1. Enter the following details in the Edit Settings dialog box.
   * **Publish Url** - AEM publish URL (for example, `https://publish-p12345-e12345.adobeaemcloud.com`)
   * **Author Url** - AEM author URL (for example, `https://author-p12345-e12345.adobeaemcloud.com`)
   
   >[!NOTE]
   >Ensure you create and publish at least one AEM Screen Channel before configuring the AEM under Screens Service Provider. To create a channel, navigate to /screens.html on your content provider.
   
    ![image](/help/screens-cloud/assets/configure/configure-screens4.png)

1.  Click **Save** to connect to Screens content provider.

1. In case you have configured the AEM publish instance to allow access only to trusted IP addresses by Cloud Manager's IP Allowlist feature, you need to configure a header with a key value in the settings dialog as shown below.
The IPs which need to whitelisted also need to moved to the configuration file and need to be [unapplied](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/using-cloud-manager/ip-allow-lists/apply-allow-list) from the Cloud Manager settings.

   ![image](/help/screens-cloud/assets/configure/configure-screens20b.png)
The same key needs to be configured at  AEM CDN configuration.  It is recommended to not put the header value directly in GITHub and use a [secret reference](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/implementing/content-delivery/cdn-credentials-authentication#rotating-secrets).
A sample [CDN config](https://experienceleague.adobe.com/en/docs/experience-manager-cloud-service/content/security/traffic-filter-rules-including-waf) is given below:

    ```kind: "CDN"
        version: "1"
        metadata:
          envTypes: ["dev", "stage", "prod"]
        data:
          trafficFilters:
            rules:
              - name: "block-request-from-not-allowed-ips"
                when:
                  allOf:
                    - reqProperty: clientIp
                      notIn: ["101.41.112.0/24"]
                     reqProperty: tier
                      equals: publish
                action: block
              - name: "allow-requests-with-header"
                when:
                  allOf:
                    - reqProperty: tier
                      equals: publish
                    - reqProperty: path
                      equals: /screens/channels.json
                    - reqHeader: x-screens-allowlist-key
                      equals: $\
        {CDN_HEADER_KEY}
                action:
                  type: allow
    ```

1. Select **Channels** from the left navigation bar and click **open in content provider**. 

   ![image](/help/screens-cloud/assets/configure/configure-screens1.png)

1. Screens Content Provider opens in another tab that lets you create your content.

   ![image](/help/screens-cloud/assets/configure/configure-screens2.png)



    

## What's Next {#whats-next}

After you have learned how to set up Screens Services Provider, navigate to [Using Screens Content Provider](https://experienceleague.adobe.com/docs/experience-manager-cloud-service/content/screens-as-cloud-service/configure-screens-cloud/using-screens-content-provider.html#screens-content-provider) for more details.
