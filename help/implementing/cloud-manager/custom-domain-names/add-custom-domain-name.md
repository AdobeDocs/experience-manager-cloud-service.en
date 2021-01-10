---
title: Adding a Custom Domain Name
description: Adding a Custom Domain Name
---

# Adding a Custom Domain Name {#adding-cdn}

A user must be a Business Owner or Deployment Manager in order to add a Custom Domain name in Cloud Manager.

## Important Considerations {#important-considerations}

* Before adding a custom domain name, a valid SSL certificate that contains the custom domain name must be installed to your Program. Refer to [Adding an SSL Certificate](/help/implementing/cloud-manager/managing-ssl-certifications/add-ssl-certificate.md) to learn more.

* Domain names cannot be added to environments while there is a current running pipeline attached to those environments.

* Only one domain name can be added at a time. However, domains cannot contain wildcards. Custom domains on the author side are not supported.

* Each Cloud Manager Environment can host up to a maximum of 100 custom domains per environment.

* The same domain name cannot be used on more than one environment.

## Adding a Custom Domain Name from Domain Settings page {#adding-cdn-settings}

Follow the steps below to add a Custom Domain Name from Domain Settings page:

1. Navigate to **Environments** screen from **Overview** page.

1. Click on **Domain Settings** from the left navigation menu.

   ![](/help/implementing/cloud-manager/assets/cdn/cdn-create.png)

1. Click on **Add Domain** button to open **Add Domain Name** dialog box.

   ![](/help/implementing/cloud-manager/assets/cdn/cdn-create2.png)

1. Enter the custom domain name in **Domain Name**. 

   >[!NOTE] 
   >You should not include `http://`, `https://`, or spaces when entering in your domain. 

1. Select the **Environment** whose Publish service will be associated with the domain name.

1. Select the **Domain SSL Certificate** from the drop-down and select **Continue**.

1. **Add Domain Name** dialog box appears. This will take you to the Domain Name Verification for your Environment screen. Refer to [Adding a TXT Record](/help/implementing/cloud-manager/custom-domain-names/add-text-record.md) to learn more.
   
   Follow the instructions provided to prove domain ownership for your environment:

1. Click on **Create**. 
1. CDN deployment requires a valid SSL certificate  and successful TXT verification. This is indicated by status **Verified and Deployed**.
   Navigate to [Checking Custom Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) to learn more about various statuses and how to address.

   >[!NOTE]
   >DNS proof can take up to a few hours to recognize, because of DNS propagation delays. Cloud Manager will verify ownership and update the status which can be seen in the Domain Settings Table. Refer to Checking Domain Name Status for more details.

## Adding a Custom Domain Name from Environments page {#adding-cdn-environments}

1. Navigate to Environments Detail page for the environment of interest.

   ![](/help/implementing/cloud-manager/assets/cdn/cdn-create4.png)
   
1. Use the input fields at the top of the Domain Names table to submit  the custom domain name and select the SSL certificate from the drop-down list. Click on **+ Add**.

   ![](/help/implementing/cloud-manager/assets/cdn/cdn-create3.png)

1. Check the fields from the **Add Domain Name** dialog box and click **Continue**.

   ![](/help/implementing/cloud-manager/assets/cdn/cdn-create5.png)

   >[!NOTE]
   >Do not include `http://`, `https://`, or spaces when entering in your domain.

1. Domain Name Verification for your Environment screen displays.

   ![](/help/implementing/cloud-manager/assets/cdn/cdn-create6.png)

   Refer to [Domain Verification](/help/implementing/cloud-manager/custom-domain-names/add-text-record.md) to learn more. Follow the instructions provided to prove domain ownership for your environment.

1. Click on **Create**. 

1. Custom Domain Name deployment requires a valid SSL certificate  and successful TXT verification. This is indicated by status **Verified and Deployed**.  

At this point, your custom domain name is ready for testing and a `CNAME` to point to it. Refer to [Domain Name Status](/help/implementing/cloud-manager/custom-domain-names/check-domain-name-status.md) to learn more about various statuses and how to address.

   >[!NOTE]
   >DNS proof can take up to a few hours to recognize, because of DNS propagation delays. Cloud Manager will verify ownership and update the status which can be seen in the Domain Settings Table. Refer to Checking Domain Name Status to learn more.
