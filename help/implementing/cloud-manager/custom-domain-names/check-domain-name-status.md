---
title: Check Domain Name Status
description: Learn how to verify that Cloud Manager has successfully confirmed your custom domain name.
exl-id: 8fdc8dda-7dbf-46b6-9fc6-d304ed377197
solution: Experience Manager
feature: Cloud Manager, Developing
role: Admin, Architect, Developer
---

# Check domain name status {#check-status}

Learn how to verify that Cloud Manager has successfully confirmed your custom domain name.

## Check the status of a custom domain name {#how-to}

Before checking your domain name status in Cloud Manager, make sure you have already added a customer managed (OV/EV) SSL certificate for your custom domain as described in [Add a customer managed SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md##add-customer-managed-ssl-cert).

**To check the status of a custom domain name:**

1. Log into Cloud Manager at [my.cloudmanager.adobe.com](https://my.cloudmanager.adobe.com/) and select the appropriate organization.

1. On the **[My Programs](/help/implementing/cloud-manager/navigation.md#my-programs)** console, select the program.

1. Navigate to the **Environments** screen from the **Overview** page.

1. Click **Domain Settings** in the left side menu.

1. Click the **Status** icon for the domain name.

The status detail is shown. Your custom domain is ready to be used when the status **Domain Verified & Deployed** is shown. See the [next section](#statuses) for details on the different statuses and what they mean.

>[!NOTE]
>
>If you are using an *Adobe managed (DV) SSL certificate* with the domain, Cloud Manager automatically triggers verification when you click **Verify** in the Verify domain dialog box when [adding a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md).
>
>If you plan on using a **customer managed (OV/EV) SSL certificate**, your domain is verified *after* you [add the OV/EV SSL certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md). 


## Verification statuses {#statuses}

Cloud Manager verifies domain ownership through the customer managed (OV/EV) SSL certificate. When done, it displays one of the following status messages:

| Status | Description |
| --- | --- |
| Domain verification failed | The Customer managed EV/OV certificate is either missing or is detected with errors.<br> Follow the instructions provided in the status message to resolve the issue. When ready, you must select the **Verify Again** icon next to the status. |
| Domain verification in progress | Verification is in progress.<br>This status is typically seen after you select the **Verify Again** icon next to the status. DNS verification can take a few hours to process because of DNS propagation delays.  |
| Verified - deployment failed| The EV/OV certificate verification was successful, but the CDN deployment failed.<br>In such cases, contact your Adobe representative. |
| Domain verified & deployed | This status indicates that your custom domain name is ready to be used.<br>At this point, your custom domain name is ready for testing and to be pointed to the Cloud Manager domain name. See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) to learn more. |
| Deleting | The deletion of a custom domain name is in progress. |
| Deletion failed | The deletion of a custom domain name failed and must be retried.<br>See [Manage custom domain names](/help/implementing/cloud-manager/custom-domain-names/managing-custom-domain-names.md) to learn more. |


## Domain name errors {#domain-error}

The following are some common domain name verification errors and their typical resolutions.

### Domain not installed error {#domain-not-installed}

This error may occur during domain validation of the EV/OV certificate even after you have checked that the certificate has been updated appropriately.

#### Error cause {#cause}

Fastly locks a domain to the account that first registers it, and other accounts must request permission to register a subdomain. Furthermore, Fastly only lets you assign an apex domain and associated subdomains to one Fastly service and account. If you have an existing Fastly account that links the same apex and subdomains used for your AEM Cloud Service domains you see this error.

#### Error resolution {#resolution}

The error is fixed as follows:

* Remove the apex and subdomains from the existing account before installing the domain in Cloud Manager.

* Use this option to link the apex domain and all subdomains to the AEM as a Cloud Service Fastly account. See [Working with Domains in the Fastly documentation](https://docs.fastly.com/en/guides/working-with-domains) for additional details.

* If your apex domain has multiple subdomains for AEM as a Cloud Service and non-AEM sites that need to link to different Fastly accounts, attempt to install the domain in Cloud Manager. This process helps manage subdomain connections across different Fastly accounts. If the domain installation fails, create a Customer Support ticket with Fastly so Adobe can follow up with Fastly on your behalf.

>[!TIP]
>
>Solving domain delegation issues with Fastly typically takes 1-2 business days. For this reason, it is recommended to install the domains well before their go live date.

>[!NOTE]
>
>Do not route the DNS of your site to AEM as a Cloud Service IPs if the domain was not installed successfully.

## Pre-existing CDN configurations for custom domain names {#pre-existing-cdn}

If you already have a CDN configuration for your custom domain names, an informative message appears on the **Custom Domain Names** and **Environment** pages. It encourages you to add these configurations through the UI so they can be managed and viewed within Cloud Manager.

The message disappears after all pre-existing environment configurations are migrated using the UI. It may take 1-2 business days for the message to disappear.

See [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) for more details.

## Next steps {#next-steps}

After you have verified your domain status in Cloud Manager, configure DNS settings by adding DNS, CNAME, or APEX records that point to AEM as a Cloud Service. Proceed to the document [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md) to continue setting up your custom domain name.
