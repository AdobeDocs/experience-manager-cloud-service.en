---
title: Configuring DNS Settings 
description: Configuring DNS Settings
---

# Configuring DNS Settings {#configure-dns}

After your custom domain name is successfully verified and deployed, you are ready to update the DNS records for your custom domain name with your DNS provider. Doing so enables your site to serve visitors. This activity is therefore typically done before Go-live.

>[!NOTE]
>You or the appropriate individual in your organization must be able to login or contact your DNS provider (the company whom you purchased the domain from) and make updates in your DNS settings.

To do this, you must determine if you must configure your DNS settings to a `CNAME` or Apex record pointing your custom domain name to the Cloud Manager domain name. A `CNAME` or A record, once provisioned will route all internet traffic for the domain to wherever it is pointing. If that location is not provisioned to serve the traffic, there will be an outage. If it has not been tested, there may be errors in the content. This is why this step is always done after testing is complete and the customer is ready for Go-live. 

## CNAME Record {#cname-record}

The following sections will help you determine which type of record is appropriate for your DNS configuration.

A Canonical Name or `CNAME` record is a type of DNS record that maps an alias name to a true or canonical domain name. CNAME records are typically used to map a subdomain such as `www.example.com`  to the domain hosting that subdomain's content. 

Login to your Domain Registrar and create a CNAME record to point your custom domain name to the target as shown below:

|CNAME|Custom Domain Name Point to Target|
|--- |--- |
|www.customdomain.com|cdn.adobeaemcloud.com|

## APEX Record {#apex-record}

An apex domain is a custom domain that does not contain a subdomain, such as example.com. An apex domain is configured with an `A` , `ALIAS` , or `ANAME` record through your DNS provider. The Apex domains must point to specific IP addresses. 

Add all of the the following A records to your Domain's DNS settings via your domain provider:

* `A RECORD`

* `A record for domain @ pointing to IP 151.101.3.10`

* `A record for domain @ pointing to IP 151.101.67.10`

* `A record for domain @ pointing to IP 151.101.131.10`

* `A record for domain @ pointing to IP 151.101.195.10`
