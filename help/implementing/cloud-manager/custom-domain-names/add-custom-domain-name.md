---
title: Adding a Custom Domain Name
description: Adding a Custom Domain Name
---

# Adding a Custom Domain Name {#adding-cdn}

A user must be a Business Owner or Deployment Manager in order to add a Custom Domain name in Cloud Manager.

>[!NOTE]
>Before adding a custom domain name, a valid SSL certificate that contains the custom domain name must be installed to your Program. Refer to Installing an SSL Certificate to learn more.

Only one domain name can be added at a time. Users can, however, add wildcards, for example, `*.wknd.com` as a domain name, and that would allow multiple subdomains to be hosted with a single TXT record.
Each Cloud Manager Environment can host up to a maximum of 50 custom domains per environment.
The same domain name cannot be used on more than one environment.

## Adding a Custom Domain Name from Domain Settings page {#adding-cdn-settings}

Follow the steps below to add a Custom Domain Name from Domain Settings page:

1. Navigate to Domain Settings page from the **Environments Page** 

1. Select **Add custom domain name** to launch the add custom domain name wizard.

1. Enter the custom domain name. 

   >[!NOTE] 
   >You should not include `http://`, `https://`, or spaces when entering in your domain. 

1. Select the Environment whose Publish service will be associated with the domain name.

1. Select the SSL certificate from the drop-down and select Continue.

1. This will take you to the Domain Name Verification for your Environment screen. Refer to Adding a TXT Record to learn more.

   >[!NOTE]
   >Follow the instructions provided to prove domain ownership for your environment.

1. Select Continue. 
1. CDN deployment requires a valid SSL certificate  and successful TXT verification. This is indicated by status **Verified and Deployed**.
1. Navigate to Checking Custom Domain Name Status to learn more about various statuses and how to address.

   >[!NOTE]
   >DNS proof can take up to a few hours to recognize, because of DNS propagation delays. Cloud Manager will verify ownership and update the status which can be seen in the Domain Settings Table. Refer to Checking Domain Name Status for more details.

## Adding a Custom Domain Name from Environments page {#adding-cdn-environments}

1. Navigate to Environment Detail page for the environment of interest.
1. Use the input fields at the top of the Domain Names table to submit  the custom domain name, SSL certificate. Next select Add.
1. This will launch the Add Custom Domain name wizard with the Environment name pre-populated. 
1. Enter the custom domain name. Note: Do not include `http://`, `https://`, or spaces when entering in your domain. Select Continue.
1. This will take you to the Domain Name Verification for your Environment screen. Refer to Domain Verification (Add TXT Record) to learn more.

   >[!NOTE]
   >Follow the instructions provided to prove domain ownership for your environment.

1. Select Continue. 
1. CDN deployment requires a valid SSL certificate  and successful TXT verification. This is indicated by status **Verified and Deployed**.  

At this point, your custom domain name is ready for testing and a `CNAME` to point to it. Refer to Domain Name Status to learn more about various statuses and how to address.

   >[!NOTE]
   >DNS proof can take up to a few hours to recognize, because of DNS propagation delays. Cloud Manager will verify ownership and update the status which can be seen in the Domain Settings Table. Refer to Checking Domain Name Status to learn more.
