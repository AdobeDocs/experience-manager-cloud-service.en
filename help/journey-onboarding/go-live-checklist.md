---
title: Go-Live Checklist
description: Learn about all the elements that need to be in place to have a successful Go-Live with AEM as a Cloud Service.
exl-id: b424a9db-0f3b-4a8d-be84-365d68df46ca
feature: Onboarding
role: Admin, User, Developer
---
# Go-Live Checklist {#Go-Live-Checklist}

Review this list of activities to ensure that you perform a smooth and successful Go-Live.

* Run an end-to-end production pipeline with functional and UI testing to ensure an **always current** AEM product experience. See the following resources.
  * [AEM Version Updates](/help/implementing/deploying/aem-version-updates.md)
  * [Custom Functional Testing](/help/implementing/cloud-manager/functional-testing.md#custom-functional-testing)
  * [UI Testing](/help/implementing/cloud-manager/ui-testing.md)
* If you are migrating from AEM 6.5, you should migrate content to production and make sure that a relevant subset is available on staging for testing.
  * DevOps best practices for AEM imply that code moves up from development to the production environment while content moves down from production environments.
* Schedule a code and content freeze period.
  * Also see the section [Code and Content Freeze Timelines for the Migration](#code-content-freeze)
* Perform the final content top-up.
* Validate Dispatcher configurations.
  * Use a local Dispatcher validator that facilitates configuring, validating, and simulating the Dispatcher locally
    * [Set up the local Dispatcher tools](https://experienceleague.adobe.com/en/docs/experience-manager-learn/cloud-service/local-development-environment-set-up/dispatcher-tools#prerequisites).
  * Review the virtual host configuration carefully.
    * The easiest (and default) solution is to include `ServerAlias *` in your virtual host file in the `/dispatcher/src/conf.d/available_vhostsfolder`. Doing so permits the host aliases used by product functional tests, Dispatcher cache invalidation, and clones to function.
    * However, if `ServerAlias *` is not acceptable, at a minimum the following `ServerAlias` entries must be allowed in addition to your custom domains:
      * `localhost`
      * `*.local`
      * `publish*.adobeaemcloud.net`
      * `publish*.adobeaemcloud.com`
* Configure CDN, SSL and DNS.
  * If you are using your own CDN, enter a support ticket to configure appropriate routing.
    * See the section [Customer CDN points to AEM Managed CDN](/help/implementing/dispatcher/cdn.md#point-to-point-cdn) in the CDN documentation for details.
    * Configure SSL and DNS according to the documentation of your CDN vendor.
  * If you are not using an additional CDN, manage SSL and DNS as per the following documentation:
    * Managing SSL Certificates
      * [Introduction to SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/introduction-to-ssl-certificates.md)
      * [Manage SSL certificates](/help/implementing/cloud-manager/managing-ssl-certifications/managing-certificates.md)
    * Managing Custom Domain Names (DNS)
      * Ensure that the DNS cutover does not introduce unexpected problems. Create a test subdomain to connect your production instance to before you go-live and do a round of UAT testing. So, if your domain is example.com, you can create a subdomain test.example.com and apply it to production. During UAT testing of the domain, look for things such as proper link redirection, caching, and Dispatcher configurations. 
      * [Introduction to custom domain names](/help/implementing/cloud-manager/custom-domain-names/introduction.md)
      * [Add a custom domain name](/help/implementing/cloud-manager/custom-domain-names/add-custom-domain-name.md)
      * [Manage a custom domain name](/help/implementing/cloud-manager/custom-domain-names/managing-custom-domain-names.md)
  * Remember to validate the TTL set for your DNS record.
    * The TTL is the amount of time a DNS record stays in a cache before asking the server for an update.
    * If you have a very high TTL, updates to your DNS record take longer to propagate. 
* Run performance and security tests that meet your business requirements and objectives.
    * Perform tests in a stage environment.  It has the same sizing as production. 
    * Development environments do not have the same sizing as stage and production. 
* Cut over and make sure that the actual go-live is performed without any new deployment or content update.
* Create Admin Console User Notification Profiles. See [Notification Profiles](/help/journey-onboarding/notification-profiles.md)
* Consider configuring Traffic Filter Rules to control what traffic should not be allowed on your website.
  * Rate limit Traffic Filter Rules can be an effective tool against DDoS attacks. A special category of Traffic Filter Rules, called WAF (Web Application Firewall) rules, require a separate license.
  * See documentation for some [suggested starter rules](/help/security/traffic-filter-rules-including-waf.md#recommended-starter-rules).
 
You can always reference the list in case you need to recalibrate your tasks during Go-Live.
