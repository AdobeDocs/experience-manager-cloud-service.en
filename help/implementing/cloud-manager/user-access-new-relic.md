---
title: User Access to New Relic
description: Learn about New Relic application performance monitoring data for AEM as a Cloud Service.
---

# User Access to New Relic {#user-access}

Learn about New Relic application performance monitoring data for AEM as a Cloud Service.

## Introduction {#introduction}

Adobe places a great emphasis on the monitoring, availability, and performance of your application. To help achieve this goal, AEM as a Cloud Service provides access to a custom New Relic monitoring suite as a part of the standard product offering to ensure your teams have the maximum visibility to your AEM as a Cloud Service system and environment performance metrics.

This document describes the New Relic monitoring features enabled on your AEM as a Cloud Service environments to help bolster the performance and allow you to get the most out of AEM as a Cloud Service.

## Features {#transaction-monitoring}

New Relic application performance monitoring for AEM as a Cloud Service has many features.

* Direct access to a dedicated New Relic One account (access managed by Adobe Support)

* Instrumented New Relic APM agent that shows exact method calls with line numbers, including external dependencies and databases

* Holistic performance optimization by combining key metrics from infrastructure-level monitoring as well as application (Adobe Experience Manager) monitoring

* Exposure of AEM as a Cloud Service JMX Mbeans and health checks directly within New Relic Insights metrics, allowing for deep inspection of application stack performance and health metrics.

## Accessing New Relic {#accessing-new-relic}

Follow these steps to get access to your New Relic sub-account associated with your AEM as a Cloud Service Program.

1. Please open a request by accessing the Support tab in the Admin Console. 
1. In your request, include the details of your Program ID, as well as the list of users who require access to New Relic. 
   * The full names and valid email addresses of all users must be provided. 

Refer to the document [AEM Support Portal for Experience Cloud](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html) for more details on opening tickets.

Once the access has been provided, New Relic sends a confirmation email to each user, so the user can complete the setup process and sign in. 

If the user cannot locate the original account confirmation email follow these steps.

1. Navigate to New Relic's login page at [`login.newrelic.com/login`](https://login.newrelic.com/login).

1. Select **Forgot your password?**.

   ![New Relic login](/help/implementing/cloud-manager/assets/new-relic/newrelic-1.png)

1. Type the account email address, and select **Send my reset link**.

   ![Enter email address](/help/implementing/cloud-manager/assets/new-relic/newrelic-2.png)

1. New Relic will send the user an email containing a link to confirm the account.

If you complete the sign up process and are unable to log in to your account due to email or password error messages, please log a support ticket via the [Admin Console](https://adminconsole.adobe.com/).

>[!TIP]
>
>If you don't receive an email from New Relic:
>
>* Check your [spam filters](https://docs.newrelic.com/docs/accounts/accounts-billing/account-setup/create-your-new-relic-account/).
>* If applicable, [add New Relic to your email allow list](https://docs.newrelic.com/docs/accounts/accounts/account-maintenance/account-email-settings/#email-whitelist).
>* If neither suggestion help, please provide feedback on the support ticket and Adobe Support team will help you further.

### Verifying Your Email {#verify-email}

If you are asked to verify your email during login, it means your email is associated with multiple accounts. This allows you to choose which account to access.

If you do not verify your email address, New Relic will attempt to log you in with the most recently created user record associated with your email address. To avoid verifying your email during each login, click the **Remember Me** checkbox in the login screen.

For more help, please open a support ticket via the [AEM Support Portal](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

## Exceptions {#exceptions}
 
AEM as a Cloud Service only offers the New Relic APM solution and does not provide support for alerting, logging, or API integrations.

For more help or additional guidance on New Relic offerings for your AEM as a Cloud Service Program, please open a support ticket via the [AEM Support Portal](https://helpx.adobe.com/enterprise/using/support-for-experience-cloud.html).

## Frequently Asked Questions for New Relic Account {#faqs}

### What does Adobe monitor with New Relic? {#adobe-monitor}

Adobe monitors the AEM as a Cloud Service author, publish and preview (where available) services via New Relic APM Java plug-in. Adobe enables custom New Relic APM telemetry and monitoring across non-production and production AEM as a Cloud Service environments. 

Your New Relic account is attached to a primary Adobe-maintained account and has multiple applications reporting into it: three per AEM as a Cloud Service Environment. 

* One application for the author service per environment
* One application for the publish service per environment (including Golden Publish)
* One application for the preview service per environment

Please note:

* Each application uses one license key.
* AEM as a Cloud Service environments report to only one New Relic account.
* Full monitoring metrics and events for both New Relic APM are retained for 7 days.

### Who can access the New Relic cloud service data? {#access-new-relic-cloud}

Full read access will be granted for up to 10 members of your team. Read access will include all APM metrics collected by the New Relic agent.

### Is custom SSO configuration supported? {#custom-sso}

Custom SSO configuration is not supported for the New Relic account provisioned by Adobe.

### What if I already have an on-premises New Relic subscription? {#new-relic-subscription}

The new observability platform from New Relic, called New Relic One, enables Adobe support and your teams to observe, monitor, and view metrics and events, all in one place.

New Relic One provides users the ability to search across all accounts where they have access and visualize the data from all services and hosts in one view. While Adobe support will monitor the AEM as a Cloud Service application using New Relic and other in-house tools as part of your service, your teams can continue to leverage New Relic for on-premises hosted services and infrastructure. They will be able to visualize the data from both Adobe and customer managed New Relic accounts.

>[!NOTE]
>User must have the right permissions and use the same login methodology for both accounts (Adobe and customer managed New Relic account).


