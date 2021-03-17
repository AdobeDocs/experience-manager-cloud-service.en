---
title: Checking Status of an SSL Certificate - Managing SSL Certificates
description: Checking Status of an SSL Certificate - Managing SSL Certificates
---

# Checking Status of an SSL Certificate {#checking-status-an-ssl-certificate}

The status of your SSL certificates can be understood at a glance from the SSL certificate page.

You can identify the status of an SSL certificate from the following color schemes:

* **Green** 
   Indicates that your certificate is valid for at least 60 days into the future.

* **Orange** 
   Indicates that your certificate is due to expire in under 60 days. It is time to ensure you have a plan to renew your certificate and replace it via Cloud Manager UI in order to avoid possible site access or outages. Cloud Manager will send regular notifications in the UI to alert you of an impending certificate expiration.

* **Red** 
   Indicates that despite multiple notifications, your SSL certificate has expired.

## Pre-existing CDN Configurations for IP Allow Lists {#pre-existing-cdn}

Customers with environments that includes pre-existing CDN configurations for IP Allow Lists, SSL Certificates or Custom Domain Names will see the following message in the the **IP Allow List** and the **Environment** details page. The message displayed on the UI will disappear once the customer has fully migrated all pre-existing environment configurations via the UI and it may take 1-2 business days for the message to disappear.

>[!NOTE]
>In order to see and manage the pre-existing configurations they must be added via the UI. Refer to [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) for more details.

![](/help/implementing/cloud-manager/assets/ip-allow-list-message1.png)

![](/help/implementing/cloud-manager/assets/ip-allow-list-message2.png)