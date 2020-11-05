---
title: Checking Domain Name Status
description: Checking Domain Name Status
---

# Checking Domain Name Status {#check-status}

You can determine whether your domain name has been verified successfully by clicking the Status icon for the domain name from the table on Environments from the Domain Settings page. 

>[!NOTE]
>Cloud Manager will automatically trigger a TXT verification when you select Save on the verification step of the Add Custom Domain wizard. For subsequent verifications, you must actively select the ‘verify again’ icon next to the status. INSERT IMAGE

Cloud Manager will verify domain ownership via the TXT value and displays one of the following status messages:

* **Domain Verification Failed** 
   TXT value is either missing or is detected with errors. Follow instructions and retry. When ready, you must select the ‘verify again’ icon  next to the status.

* **Domain Verification In Progress**
   Verification in progress. This status is typically seen after you select the ‘verify again’ icon next to the status.

* **Verified, Deployment Failed** 
   TXT verification was successful. However, the CDN deployment failed. An Adobe representative will be notified automatically.

* **Domain Verified & Deployed**
   This status indicates that your custom domain name is ready to be used. Note: At this point, your custom domain name is ready for testing and to be pointed to the Cloud Manager domain name. Go to Configuring DNS Settings INSERT LINK to learn how to do this.

* **Deleting** 
   Deletion of Custom Domain name is in process.

* **Deletion Failed** 
   Deletion of Custom Domain name failed. You must retry. Go to Delete Custom Domain Name to learn more on the topic.


## Configuring DNS Settings {#configure-dns}

After your custom domain name is successfully verified and deployed, you are ready to update the DNS records for your custom domain name with your DNS provider. Doing so enables your site to serve visitors. This activity is therefore typically done before Go-live.

>[!NOTE]
>You or the appropriate individual in your organization must be able to login or contact your DNS provider (the company whom you purchased the domain from) and make updates in your DNS settings.

To do this, you must determine if you must configure your DNS settings to a `CNAME` or Apex record pointing your custom domain name to the Cloud Manager domain name. A `CNAME` or A record, once provisioned will route all internet traffic for the domain to wherever it is pointing. If that location is not provisioned to serve the traffic, there will be an outage. If it has not been tested, there may be errors in the content. This is why this step is always done after testing is complete and the customer is ready for Go-live. 

### CNAME Record {#cname-record}

The following sections will help you determine which type of record is appropriate for your DNS configuration.

A Canonical Name or `CNAME` record is a type of DNS record that maps an alias name to a true or canonical domain name. CNAME records are typically used to map a subdomain such as `www.example.com`  to the domain hosting that subdomain's content. 

Login to your Domain Registrar and create a CNAME record to point your custom domain name to the target as shown below:

|[CNAME|Custom Domain Name Point to Target|
|--- |--- |
|www.customdomain.com|cdn.adobeaemcloud.com|
