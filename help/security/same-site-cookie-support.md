---
title: Same Site Cookie Support for Adobe Experience Manager as a Cloud Service
description: Same Site Cookie Support for Adobe Experience Manager as a Cloud Service.
exl-id: 2cec7202-4450-456f-8e62-b7ed3791505c
feature: Security
role: Admin
---
# Same Site Cookie Support for Adobe Experience Manager as a Cloud Service {#same-site-cookie-support-for-adobe-experience-manager-as-a-cloud-service}

Since version 80, Chrome, and later Safari, introduced a new model for cookie security. This mode is designed to introduce security controls around availability of cookies to third-party sites, through a setting called `SameSite`. For more detailed information, see [web.dev - SameSite cookies explained](https://web.dev/articles/samesite-cookies-explained).

The default value of this setting (`SameSite=Lax`) might cause authentication between AEM instances or services to not work. This is because the domains or URL structures of these services might not fall under the constraints of this cookie policy.

To get around this, set the SameSite cookie attribute to `None` for the login token.

>[!CAUTION]
>
>The `SameSite=None` setting is only applied if the protocol is secure (HTTPS). 
>
>If the protocol is not secure (HTTP), then the setting is ignored and the server shows this warning message:
>
>`WARN com.day.crx.security.token.TokenCookie Skip 'SameSite=None'`

You can add the setting by following the below steps:

1. Install a version of the AEM SDK Quickstart locally
1. Go to the Web Console at `http://serveraddress:serverport/system/console/configMgr`
1. Search for and click the **Adobe Granite Token Authentication Handler**
1. Set the **SameSite attribute for the login-token cookie** to `None`, as shown in the image below
   ![samesite](/help/security/assets/samesite1.png)
1. Click Save
1. Generate the JSON format configurations for this particular setting by following the steps outlined in [Generating OSGi Configurations using the AEM SDK Quickstart](/help/implementing/deploying/configuring-osgi.md#generating-osgi-configurations-using-the-aem-sdk-quickstart)
1. Apply the settings by following the steps in the [Cloud Manager API Format for Setting Properties](/help/implementing/deploying/configuring-osgi.md#cloud-manager-api-format-for-setting-properties) OSGi documentation.

After this setting is updated and users are logged off and logged on again, `login-token` cookies have the `None` attribute set and is included in cross-site requests.
