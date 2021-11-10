---
title: User Access to New Relic
description: User Access to New Relic
index: no
hide: yes
---

# New Relic APM for AEM as a Cloud Service {#new-relic} 

## Introduction {#introduction}

Adobe places a high emphasis on the monitoring, availability and performance of your application. To help achieve this goal, AEM as a Cloud Service provides access to a custom New Relic monitoring suite as a part of the standard product offering to ensure your teams have the maximum visibility to your Adobe Experience Manager Cloud Service system and environment performance metrics. This white paper describes the New Relic monitoring features enabled on your AEM as a Cloud Service environments to help bolster the performance and allow you to get the most out of AEM as a Cloud Service.

## AEM as a Cloud Service Transaction Monitoring via New Relic {#transaction-monitoring}

* Direct access into a dedicated New Relic One account (access managed by Adobe Support).

* Instrumented New Relic APM agent that shows exact method calls with line numbers, including external dependencies and databases.

* Holistic performance optimization by combining key metrics from infrastructure-level monitoring as well as application (Adobe Experience Manager) monitoring.

* Exposure of AEM as a Cloud Service JMX Mbeans and Health Checks directly into New Relic Insights metrics, allowing for deep inspection of application stack performance and health metrics.

## Accessing your AEM as a Cloud Service New Relic account {#accessing-new-relic}

Your dedicated New Relic account will be provisioned and managed by Adobe via Customer Care engagement. Adobe will remain the owner and administrator and will provision the account on your behalf to provide access to your dedicated sub-account.

In order to get access to your New Relic sub-account associated with your AEM as a Cloud Service Program, please open a request by accessing the Support tab in the Admin Console. Ensure your ticket includes the details of your Program ID, as well as the list of users you request Adobe teams to open the New Relic access to. All users must be provided with full name and valid email address.  For more details on AEM Support Portal please Support for Experience Cloud. 

Once the access has been provided, New Relic sends a confirmation email to each user, so they can complete the setup process and sign in. If they cannot locate the original account confirmation email:

1. Go to New Relic's login page at login.newrelic.com/login.

1. Select Forgot your password.

1. Type the account email address, and select Send my password.

1. When New Relic's system returns an email message, select the link in it to confirm your account again.

   >[!NOTE]
   >If you don't receive an email from New Relic:
   >Check your spam filters. If applicable, add New Relic to your email allow list.
   >Please feedback on the support ticket and our teams will help you further

1. If you complete the signup process and are unable to log in to your account due to email or password error messages, please get us a support ticket via Admin Console.

If you are asked to verify your email during login, it means your email is associated with multiple accounts and will be given the option to verify your email during login. This will allow you to choose which account to access. If you do not verify your email address, New Relic will attempt to log you in with the most recently created user record associated with your email address. To avoid verifying your email during each login, click the Remember Me checkbox in the login screen.

For more help, please open a support ticket via AEM Support Portal.

## Exceptions {#exceptions}
 
AEM as a Cloud Service focuses the offering around New Relic APM solution only and does not provide support for alerting, logging or API integration capabilities. 

For more help or additional guidance on New Relic offerings for your AEM as a Cloud Service Program, please open a support ticket via AEM Support Portal for assistance.

## Frequently Asked Questions for New Relic Account {#faqs}

### What does Adobe monitor with New Relic? {#adobe-monitor}

Adobe monitors the AEM as a Cloud Service Author, Publish and Preview (where available) services via New Relic APM Java plug-in. Adobe enables custom New Relic APM Telemetry and monitoring across non-production and production AEM as a Cloud Service environments. Your New Relic account is attached to a primary Adobe maintained account and has multiple applications reporting into it. Three each per AEM as a Cloud Service environment:

One application for the Author service per environment
One application for the Publish service per environment (including Golden Publish)
One application for the Preview service per environment
Each application uses one license key, AEM as a Cloud Service environments will report to only one New Relic account. Full monitoring metrics and events for both New Relic APM and Infrastructure are retained for 7 days.

### Who can access the New Relic Cloud Service data? {#access-new-relic-cloud}

Full read access will be granted for up to 10 members of your team. Read access will include all APM metrics collected by the New Relic agent.

### Is Custom SSO Configuration Supported? {#custom-sso}

Custom SSO configuration is currently not supported for the New Relic account provisioned by Adobe.

### What if you already have an on-premises New Relic Subscription? {#new-relic-subscription}

The new observability platform from New Relic called New Relic One enables Adobe Support Groups and your teams to observe, monitor, and view metrics and events, all in one place. New Relic One provides users the ability to search across all accounts where they have access and visualize the data from all services and hosts in one view. While Adobe Support Teams will monitor the AEM as a Cloud Service application using New Relic and other in-house tools as part of your service, your teams can continue to leverage New Relic for on-premises hosted services and infrastructure. They will be able to visualize the data from both Adobe and customer managed New Relic accounts.

>[!NOTE]
>User must have the right permissions and use the same login methodology for both accounts (Adobe and customer managed New Relic account).


